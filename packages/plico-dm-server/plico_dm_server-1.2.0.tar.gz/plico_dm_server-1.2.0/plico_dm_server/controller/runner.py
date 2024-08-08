import os
import sys
import time
from plico.utils.base_runner import BaseRunner
from plico.utils.logger import Logger
from plico.utils.decorator import override, logFailureAndRaise
from plico.utils.control_loop import FaultTolerantControlLoop
from plico_dm_server.controller.simulated_deformable_mirror import \
    SimulatedDeformableMirror
from plico.rpc.zmq_ports import ZmqPorts
from plico_dm.calibration.calibration_manager import CalibrationManager
from plico_dm_server.controller.bmc_deformable_mirror import \
    BmcDeformableMirror
from plico_dm_server.controller.alpao_deformable_mirror import \
    AlpaoDeformableMirror
from plico_dm_server.controller.deformable_mirror_controller import \
    DeformableMirrorController
from plico_dm_server.controller.meadowlark_slm_1920 import MeadowlarkSlm1920,\
    initialize_meadowlark_sdk


class Runner(BaseRunner):

    RUNNING_MESSAGE = "Mirror controller is running."

    def __init__(self):
        BaseRunner.__init__(self)

    def _tryGetDefaultFlatTag(self):
        try:
            mirrorDeviceSection = self.configuration.getValue(
                self.getConfigurationSection(), 'mirror')
            return self.configuration.getValue(
                mirrorDeviceSection, 'default_flat_tag')
        except KeyError as e:
            self._logger.warn(str(e))
            return None

    def _createDeformableMirrorDevice(self):
        mirrorDeviceSection = self.configuration.getValue(
            self.getConfigurationSection(), 'mirror')
        mirrorModel = self.configuration.deviceModel(mirrorDeviceSection)
        if mirrorModel == 'simulatedMEMSMultiDM':
            self._createSimulatedDeformableMirror(mirrorDeviceSection)
        elif mirrorModel == 'simulatedDM':
            self._createSimulatedDeformableMirror(mirrorDeviceSection)
        elif mirrorModel == 'alpaoDM':
            self._createAlpaoMirror(mirrorDeviceSection)
        elif mirrorModel == 'piTipTilt':
            self._createPITipTiltMirror(mirrorDeviceSection)
        elif mirrorModel == 'bmc':
            self._createBmcDeformableMirror(mirrorDeviceSection)
        elif mirrorModel == 'meadowlarkSLM':
            self._createMeadowlarkSlm(mirrorDeviceSection)
        elif mirrorModel == 'SPLATT':
            self._createSPLATTMirror(mirrorDeviceSection)
        else:
            raise KeyError('Unsupported mirror model %s' % mirrorModel)

    def _createSimulatedDeformableMirror(self, mirrorDeviceSection):
        dmSerialNumber = self.configuration.getValue(
            mirrorDeviceSection, 'serial_number')
        self._mirror = SimulatedDeformableMirror(dmSerialNumber)

    def _createAlpaoMirror(self, mirrorDeviceSection):
        serialNumber = str(self.configuration.getValue(mirrorDeviceSection,
                                                       'serial_number'))
        self._logger.notice("Creating ALPAO device SN %s" % serialNumber)
        libFolder = self.configuration.getValue(mirrorDeviceSection,
                                                'lib_folder')
        sys.path.append(libFolder)
        from asdk import DM
        alpaoDm = DM(serialNumber)
        self._mirror = AlpaoDeformableMirror(alpaoDm, serialNumber)
        self._logger.notice("ALPAO device SN %s created" % serialNumber)

    def _createBmcDeformableMirror(self, mirrorDeviceSection):
        serialNumber = self.configuration.getValue(mirrorDeviceSection,
                                                   'serial_number')
        self._logger.notice("Creating BMC device SN %s" % serialNumber)
        import bmc
        bmcDm = bmc.BmcDm()
        self._logger.notice("BMC version <%s>" % bmcDm.version_string())
        self._mirror = BmcDeformableMirror(bmcDm, serialNumber)

    def _createMeadowlarkSlm(self, mirrorDeviceSection):
        # serialNumber = self.configuration.getValue(mirrorDeviceSection,
        #                                           'serial_number')
        self._logger.notice("Creating  Meadowlark SLM 1920 device")
        self._logger.notice("Reading from configuration file")
        blink_dir_root = str(self.configuration.getValue(
            mirrorDeviceSection, 'blink_dir_root'))
        self._logger.notice(
            "blink_dir_root has been read from configuration file: %s" %
            blink_dir_root)
        lut_filename = self.configuration.getValue(
            mirrorDeviceSection, 'lut_filename')
        self._logger.notice(
            "lut_filename has been read from configuration file: %s" %
            lut_filename)
        wfc_filename = self.configuration.getValue(
            mirrorDeviceSection, 'wfc_filename')
        self._logger.notice(
            "wfc_filename has been read from configuration file: %s" %
            wfc_filename)
        wl_calibration = self.configuration.getValue(
            mirrorDeviceSection, 'wl_calibration', getfloat=True)
        self._logger.notice(
            "wl_calibration has been read from configuration file: %g [m]" %
            wl_calibration)
        # wl_calibration = 635e-9 #meters
        slm_lib, image_lib = initialize_meadowlark_sdk(blink_dir_root)
        self._logger.notice("slm_lib and image_lib returned")
        self._mirror = MeadowlarkSlm1920(
            slm_lib, image_lib, lut_filename, wfc_filename, wl_calibration)
        self._logger.notice("MeadowlarkSlm1920 object created")

    def _createPITipTiltMirror(self, mirrorDeviceSection):
        from plico_dm_server.controller.pi_tip_tilt_mirror \
            import PhysikInstrumenteTipTiltMirror
        from pi_gcs.gcs2 import GeneralCommandSet2
        from pi_gcs.tip_tilt_2_axes import TipTilt2Axis

        hostname = self.configuration.getValue(
            mirrorDeviceSection, 'ip_address')
        serialNumber = self.configuration.getValue(mirrorDeviceSection,
                                                   'serial_number')
        cfg = self._calibrationManager.loadPiTipTiltCalibration(
            serialNumber)
        cfg.hostname = hostname
        gcs = GeneralCommandSet2()
        tt = TipTilt2Axis(gcs, cfg)
        tt.setUp()
        self._mirror = PhysikInstrumenteTipTiltMirror(
            serialNumber, tt)

    def _createSPLATTMirror(self, mirrorDeviceSection):
        from plico_dm_server.controller.splatt_dm import SPLATTDeformableMirror
        self._mirror = SPLATTDeformableMirror()

    def _createCalibrationManager(self):
        calibrationRootDir = self.configuration.calibrationRootDir()
        self._calibrationManager = CalibrationManager(calibrationRootDir)

    @logFailureAndRaise
    def _setUp(self):
        self._logger = Logger.of("Deformable Mirror Controller runner")

        self._zmqPorts = ZmqPorts.fromConfiguration(
            self.configuration, self.getConfigurationSection())
        self._replySocket = self.rpc().replySocket(
            self._zmqPorts.SERVER_REPLY_PORT)
        self._statusSocket = self.rpc().publisherSocket(
            self._zmqPorts.SERVER_STATUS_PORT)

        self._logger.notice('reply socket on port %d' %
                            self._zmqPorts.SERVER_REPLY_PORT)
        self._logger.notice('status socket on port %d' %
                            self._zmqPorts.SERVER_STATUS_PORT)

        self._createCalibrationManager()

        self._createDeformableMirrorDevice()

        flatFileTag = self._tryGetDefaultFlatTag()

        self._logger.notice("Creating DeformableMirrorController")
        self._controller = DeformableMirrorController(
            self.name,
            self._zmqPorts,
            self._mirror,
            self._replySocket,
            self._statusSocket,
            self.rpc(),
            self._calibrationManager,
            flatFileTag)
        self._configureDiscoveryServer('plico_dm', self._mirror.__class__.__name__)

    def _runLoop(self):
        self._logRunning()

        FaultTolerantControlLoop(
            self._controller,
            Logger.of("Deformable Mirror Controller control loop"),
            time,
            0.001).start()
        self._logger.notice("Terminated")

    @override
    def run(self):
        # try:
        #     self._setUp()
        # except Exception as e:
        #     #traceback.print_exc()
        #     self._logger.error(str(e))
        #     raise(e)
        self._setUp()
        self._runLoop()
        return os.EX_OK

    @override
    def terminate(self, signal, frame):
        self._controller.terminate()
