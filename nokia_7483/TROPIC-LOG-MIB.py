# SNMP MIB module (TROPIC-LOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TROPIC-LOG-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:04:12 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(dot1agCfmMaIndex,
 dot1agCfmMdIndex,
 dot1agCfmMepIdentifier) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "dot1agCfmMaIndex",
    "dot1agCfmMdIndex",
    "dot1agCfmMepIdentifier")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(tnEthRingIndex,) = mibBuilder.importSymbols(
    "TN-ETH-RING-MIB",
    "tnEthRingIndex")

(tnOamSaaCtlTestIndex,) = mibBuilder.importSymbols(
    "TN-OAM-TEST-MIB",
    "tnOamSaaCtlTestIndex")

(tnRmdCfmMepNumber,) = mibBuilder.importSymbols(
    "TN-RMD-CFM-MIB",
    "tnRmdCfmMepNumber")

(TnRmdNimDirection,
 tnRmdIfIndex,
 tnRmdIfMauIndex) = mibBuilder.importSymbols(
    "TN-RMD-IF-MIB",
    "TnRmdNimDirection",
    "tnRmdIfIndex",
    "tnRmdIfMauIndex")

(tnRmdSystemId,) = mibBuilder.importSymbols(
    "TN-RMD-SYSTEM-MIB",
    "tnRmdSystemId")

(tnRmdTsopIwfChannelNumber,) = mibBuilder.importSymbols(
    "TN-RMD-TSOP-MIB",
    "tnRmdTsopIwfChannelNumber")

(tnSapEncapValue,
 tnSapPortId) = mibBuilder.importSymbols(
    "TN-SAP-MIB",
    "tnSapEncapValue",
    "tnSapPortId")

(tnSvcId,) = mibBuilder.importSymbols(
    "TN-SERV-MIB",
    "tnSvcId")

(tnLogMIB,
 tnSystemModules) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnLogMIB",
    "tnSystemModules")

(tnSysSwitchId,) = mibBuilder.importSymbols(
    "TROPIC-SYSTEM-MIB",
    "tnSysSwitchId")

(TnCondition,
 TnEntityType,
 TnTrapCategory) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "TnCondition",
    "TnEntityType",
    "TnTrapCategory")


# MODULE-IDENTITY

tnLogMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    tnLogMIBModule.setRevisions(
        ("2009-07-17 12:00",
         "2010-04-16 12:00",
         "2010-06-16 12:00",
         "2010-07-29 12:00",
         "2010-08-09 12:00",
         "2010-10-04 12:00",
         "2010-12-06 12:00",
         "2011-01-21 12:00",
         "2011-02-25 12:00",
         "2011-04-08 12:00",
         "2011-05-02 12:00",
         "2012-04-09 12:00",
         "2012-05-09 12:00",
         "2012-05-25 12:00",
         "2012-11-06 12:00",
         "2012-12-05 12:00",
         "2013-01-07 12:00",
         "2013-04-16 12:00",
         "2013-04-19 12:00",
         "2013-08-02 12:00",
         "2013-09-16 12:00",
         "2013-09-25 12:00",
         "2013-10-14 12:00",
         "2014-02-27 12:00",
         "2014-02-28 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AluWdmAlarmCategoryDirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("tx", 2),
          ("rx", 3))
    )



# MIB Managed Objects in the order of their OIDs

_TnLogConf_ObjectIdentity = ObjectIdentity
tnLogConf = _TnLogConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1)
)
_TnLogGroups_ObjectIdentity = ObjectIdentity
tnLogGroups = _TnLogGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1)
)
_TnLogCompliances_ObjectIdentity = ObjectIdentity
tnLogCompliances = _TnLogCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 2)
)
_TnLogObjs_ObjectIdentity = ObjectIdentity
tnLogObjs = _TnLogObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2)
)
_TnLogs_ObjectIdentity = ObjectIdentity
tnLogs = _TnLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1)
)
_TnSystemLogs_ObjectIdentity = ObjectIdentity
tnSystemLogs = _TnSystemLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 1)
)
_TnUserActionLog_ObjectIdentity = ObjectIdentity
tnUserActionLog = _TnUserActionLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tnUserActionLog.setStatus("current")
_TnApplicationProcessStartFailureLog_ObjectIdentity = ObjectIdentity
tnApplicationProcessStartFailureLog = _TnApplicationProcessStartFailureLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tnApplicationProcessStartFailureLog.setStatus("current")
_TnDiscardedEventsLog_ObjectIdentity = ObjectIdentity
tnDiscardedEventsLog = _TnDiscardedEventsLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tnDiscardedEventsLog.setStatus("current")
_TnExceededSystemLimitLog_ObjectIdentity = ObjectIdentity
tnExceededSystemLimitLog = _TnExceededSystemLimitLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    tnExceededSystemLimitLog.setStatus("current")
_TnInvalidDatabaseRecordLog_ObjectIdentity = ObjectIdentity
tnInvalidDatabaseRecordLog = _TnInvalidDatabaseRecordLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    tnInvalidDatabaseRecordLog.setStatus("current")
_TnAlarmEventCategoryChangeEventidLog_ObjectIdentity = ObjectIdentity
tnAlarmEventCategoryChangeEventidLog = _TnAlarmEventCategoryChangeEventidLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 1, 6)
)
if mibBuilder.loadTexts:
    tnAlarmEventCategoryChangeEventidLog.setStatus("current")
_TnProgrammedPortTypeChangeLog_ObjectIdentity = ObjectIdentity
tnProgrammedPortTypeChangeLog = _TnProgrammedPortTypeChangeLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 1, 7)
)
if mibBuilder.loadTexts:
    tnProgrammedPortTypeChangeLog.setStatus("current")
_TnPtchgOkLog_ObjectIdentity = ObjectIdentity
tnPtchgOkLog = _TnPtchgOkLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 1, 8)
)
if mibBuilder.loadTexts:
    tnPtchgOkLog.setStatus("current")
_TnPtchgUnknownPortTypeLog_ObjectIdentity = ObjectIdentity
tnPtchgUnknownPortTypeLog = _TnPtchgUnknownPortTypeLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 1, 9)
)
if mibBuilder.loadTexts:
    tnPtchgUnknownPortTypeLog.setStatus("current")
_TnPtchgNoSlotCorrLog_ObjectIdentity = ObjectIdentity
tnPtchgNoSlotCorrLog = _TnPtchgNoSlotCorrLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 1, 10)
)
if mibBuilder.loadTexts:
    tnPtchgNoSlotCorrLog.setStatus("current")
_TnPtchgNotAllowedLog_ObjectIdentity = ObjectIdentity
tnPtchgNotAllowedLog = _TnPtchgNotAllowedLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 1, 11)
)
if mibBuilder.loadTexts:
    tnPtchgNotAllowedLog.setStatus("current")
_TnPtchgNoPortCorrLog_ObjectIdentity = ObjectIdentity
tnPtchgNoPortCorrLog = _TnPtchgNoPortCorrLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 1, 12)
)
if mibBuilder.loadTexts:
    tnPtchgNoPortCorrLog.setStatus("current")
_TnDatabaseLogs_ObjectIdentity = ObjectIdentity
tnDatabaseLogs = _TnDatabaseLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 2)
)
_TnDatabaseConvertLog_ObjectIdentity = ObjectIdentity
tnDatabaseConvertLog = _TnDatabaseConvertLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tnDatabaseConvertLog.setStatus("current")
_TnDatabaseRestoreLog_ObjectIdentity = ObjectIdentity
tnDatabaseRestoreLog = _TnDatabaseRestoreLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tnDatabaseRestoreLog.setStatus("current")
_TnDatabaseClearPersistentRepositoryLog_ObjectIdentity = ObjectIdentity
tnDatabaseClearPersistentRepositoryLog = _TnDatabaseClearPersistentRepositoryLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 2, 6)
)
if mibBuilder.loadTexts:
    tnDatabaseClearPersistentRepositoryLog.setStatus("current")
_TnDatabaseBackupFailedLog_ObjectIdentity = ObjectIdentity
tnDatabaseBackupFailedLog = _TnDatabaseBackupFailedLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 2, 7)
)
if mibBuilder.loadTexts:
    tnDatabaseBackupFailedLog.setStatus("current")
_TnDatabaseRestoreFailedLog_ObjectIdentity = ObjectIdentity
tnDatabaseRestoreFailedLog = _TnDatabaseRestoreFailedLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 2, 8)
)
if mibBuilder.loadTexts:
    tnDatabaseRestoreFailedLog.setStatus("current")
_TnDiagnosticsLogs_ObjectIdentity = ObjectIdentity
tnDiagnosticsLogs = _TnDiagnosticsLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 3)
)
_TnEquipmentLogs_ObjectIdentity = ObjectIdentity
tnEquipmentLogs = _TnEquipmentLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 4)
)
_TnSlotMonitorCardPulledLog_ObjectIdentity = ObjectIdentity
tnSlotMonitorCardPulledLog = _TnSlotMonitorCardPulledLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tnSlotMonitorCardPulledLog.setStatus("current")
_TnSlotMonitorCardInsertedLog_ObjectIdentity = ObjectIdentity
tnSlotMonitorCardInsertedLog = _TnSlotMonitorCardInsertedLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    tnSlotMonitorCardInsertedLog.setStatus("current")
_TnI2CReadErrorLog_ObjectIdentity = ObjectIdentity
tnI2CReadErrorLog = _TnI2CReadErrorLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 4, 3)
)
if mibBuilder.loadTexts:
    tnI2CReadErrorLog.setStatus("current")
_TnI2CWriteErrorLog_ObjectIdentity = ObjectIdentity
tnI2CWriteErrorLog = _TnI2CWriteErrorLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 4, 4)
)
if mibBuilder.loadTexts:
    tnI2CWriteErrorLog.setStatus("current")
_TnSandiskATAReadErrorLog_ObjectIdentity = ObjectIdentity
tnSandiskATAReadErrorLog = _TnSandiskATAReadErrorLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 4, 5)
)
if mibBuilder.loadTexts:
    tnSandiskATAReadErrorLog.setStatus("current")
_TnSandiskATAWriteErrorLog_ObjectIdentity = ObjectIdentity
tnSandiskATAWriteErrorLog = _TnSandiskATAWriteErrorLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 4, 6)
)
if mibBuilder.loadTexts:
    tnSandiskATAWriteErrorLog.setStatus("current")
_TnAutoTopologyConfigFailedLog_ObjectIdentity = ObjectIdentity
tnAutoTopologyConfigFailedLog = _TnAutoTopologyConfigFailedLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 4, 7)
)
if mibBuilder.loadTexts:
    tnAutoTopologyConfigFailedLog.setStatus("current")
_TnAutoTopologyConfigFailedROADMCardMissingLog_ObjectIdentity = ObjectIdentity
tnAutoTopologyConfigFailedROADMCardMissingLog = _TnAutoTopologyConfigFailedROADMCardMissingLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 4, 8)
)
if mibBuilder.loadTexts:
    tnAutoTopologyConfigFailedROADMCardMissingLog.setStatus("current")
_TnAutoTopologyConfigFailedMateCADCardMissingLog_ObjectIdentity = ObjectIdentity
tnAutoTopologyConfigFailedMateCADCardMissingLog = _TnAutoTopologyConfigFailedMateCADCardMissingLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 4, 9)
)
if mibBuilder.loadTexts:
    tnAutoTopologyConfigFailedMateCADCardMissingLog.setStatus("current")
_TnAutoTopologyConfigFailedPortAlreadyConnectedLog_ObjectIdentity = ObjectIdentity
tnAutoTopologyConfigFailedPortAlreadyConnectedLog = _TnAutoTopologyConfigFailedPortAlreadyConnectedLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 4, 10)
)
if mibBuilder.loadTexts:
    tnAutoTopologyConfigFailedPortAlreadyConnectedLog.setStatus("current")
_TnAutoTopologyConfigFailedFarEndPortAlreadyConnectedLog_ObjectIdentity = ObjectIdentity
tnAutoTopologyConfigFailedFarEndPortAlreadyConnectedLog = _TnAutoTopologyConfigFailedFarEndPortAlreadyConnectedLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 4, 11)
)
if mibBuilder.loadTexts:
    tnAutoTopologyConfigFailedFarEndPortAlreadyConnectedLog.setStatus("current")
_TnSoftwareDownloadingLogs_ObjectIdentity = ObjectIdentity
tnSoftwareDownloadingLogs = _TnSoftwareDownloadingLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 5)
)
_TnSwdlResultLog_ObjectIdentity = ObjectIdentity
tnSwdlResultLog = _TnSwdlResultLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tnSwdlResultLog.setStatus("current")
_TnSwdlTransferStartedLog_ObjectIdentity = ObjectIdentity
tnSwdlTransferStartedLog = _TnSwdlTransferStartedLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 5, 2)
)
if mibBuilder.loadTexts:
    tnSwdlTransferStartedLog.setStatus("current")
_TnSwdlTransferCompleteLog_ObjectIdentity = ObjectIdentity
tnSwdlTransferCompleteLog = _TnSwdlTransferCompleteLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 5, 3)
)
if mibBuilder.loadTexts:
    tnSwdlTransferCompleteLog.setStatus("current")
_TnSwdlSwitchBankLog_ObjectIdentity = ObjectIdentity
tnSwdlSwitchBankLog = _TnSwdlSwitchBankLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 5, 4)
)
if mibBuilder.loadTexts:
    tnSwdlSwitchBankLog.setStatus("current")
_TnSwdlSwitchActivityLog_ObjectIdentity = ObjectIdentity
tnSwdlSwitchActivityLog = _TnSwdlSwitchActivityLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 5, 5)
)
if mibBuilder.loadTexts:
    tnSwdlSwitchActivityLog.setStatus("current")
_TnSwdlDatabaseBackupLog_ObjectIdentity = ObjectIdentity
tnSwdlDatabaseBackupLog = _TnSwdlDatabaseBackupLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 5, 6)
)
if mibBuilder.loadTexts:
    tnSwdlDatabaseBackupLog.setStatus("current")
_TnSwdlDatabaseRestoreLog_ObjectIdentity = ObjectIdentity
tnSwdlDatabaseRestoreLog = _TnSwdlDatabaseRestoreLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 5, 7)
)
if mibBuilder.loadTexts:
    tnSwdlDatabaseRestoreLog.setStatus("current")
_TnSwdlResetCardLog_ObjectIdentity = ObjectIdentity
tnSwdlResetCardLog = _TnSwdlResetCardLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 5, 8)
)
if mibBuilder.loadTexts:
    tnSwdlResetCardLog.setStatus("current")
_TnSwdlDatabaseClearLog_ObjectIdentity = ObjectIdentity
tnSwdlDatabaseClearLog = _TnSwdlDatabaseClearLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 5, 9)
)
if mibBuilder.loadTexts:
    tnSwdlDatabaseClearLog.setStatus("current")
_TnL1APSLogs_ObjectIdentity = ObjectIdentity
tnL1APSLogs = _TnL1APSLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 6)
)
_TnProtectionSwitchToWorkingChannelLog_ObjectIdentity = ObjectIdentity
tnProtectionSwitchToWorkingChannelLog = _TnProtectionSwitchToWorkingChannelLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    tnProtectionSwitchToWorkingChannelLog.setStatus("current")
_TnProtectionSwitchToProtectionChannelLog_ObjectIdentity = ObjectIdentity
tnProtectionSwitchToProtectionChannelLog = _TnProtectionSwitchToProtectionChannelLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 6, 2)
)
if mibBuilder.loadTexts:
    tnProtectionSwitchToProtectionChannelLog.setStatus("current")
_TnProtectionSwitchFailedLog_ObjectIdentity = ObjectIdentity
tnProtectionSwitchFailedLog = _TnProtectionSwitchFailedLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 6, 3)
)
if mibBuilder.loadTexts:
    tnProtectionSwitchFailedLog.setStatus("current")
_TnOspfLogs_ObjectIdentity = ObjectIdentity
tnOspfLogs = _TnOspfLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 7)
)
_TnOspfLsdbOverflowLog_ObjectIdentity = ObjectIdentity
tnOspfLsdbOverflowLog = _TnOspfLsdbOverflowLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    tnOspfLsdbOverflowLog.setStatus("current")
_TnOchXcLogs_ObjectIdentity = ObjectIdentity
tnOchXcLogs = _TnOchXcLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 8)
)
_TnExceededSystemLimitForConnectionsLog_ObjectIdentity = ObjectIdentity
tnExceededSystemLimitForConnectionsLog = _TnExceededSystemLimitForConnectionsLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 8, 1)
)
if mibBuilder.loadTexts:
    tnExceededSystemLimitForConnectionsLog.setStatus("current")
_TnChangedWaveKeysOfConnectionLog_ObjectIdentity = ObjectIdentity
tnChangedWaveKeysOfConnectionLog = _TnChangedWaveKeysOfConnectionLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 8, 2)
)
if mibBuilder.loadTexts:
    tnChangedWaveKeysOfConnectionLog.setStatus("current")
_TnPowerMgmtLogs_ObjectIdentity = ObjectIdentity
tnPowerMgmtLogs = _TnPowerMgmtLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 9)
)
_TnPowerMgmtAdjustStartedLog_ObjectIdentity = ObjectIdentity
tnPowerMgmtAdjustStartedLog = _TnPowerMgmtAdjustStartedLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 9, 1)
)
if mibBuilder.loadTexts:
    tnPowerMgmtAdjustStartedLog.setStatus("current")
_TnPowerMgmtAdjustCompletedLog_ObjectIdentity = ObjectIdentity
tnPowerMgmtAdjustCompletedLog = _TnPowerMgmtAdjustCompletedLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 9, 2)
)
if mibBuilder.loadTexts:
    tnPowerMgmtAdjustCompletedLog.setStatus("current")
_TnPowerControlReinitializedLog_ObjectIdentity = ObjectIdentity
tnPowerControlReinitializedLog = _TnPowerControlReinitializedLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 9, 3)
)
if mibBuilder.loadTexts:
    tnPowerControlReinitializedLog.setStatus("current")
_TnPowerMgmtAutoAdjustRequestedLog_ObjectIdentity = ObjectIdentity
tnPowerMgmtAutoAdjustRequestedLog = _TnPowerMgmtAutoAdjustRequestedLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 9, 4)
)
if mibBuilder.loadTexts:
    tnPowerMgmtAutoAdjustRequestedLog.setStatus("current")
_TnPowerMgmtCommissioningRequiredLog_ObjectIdentity = ObjectIdentity
tnPowerMgmtCommissioningRequiredLog = _TnPowerMgmtCommissioningRequiredLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 9, 5)
)
if mibBuilder.loadTexts:
    tnPowerMgmtCommissioningRequiredLog.setStatus("current")
_TnPowerMgmtVectoredAddDropFailureLog_ObjectIdentity = ObjectIdentity
tnPowerMgmtVectoredAddDropFailureLog = _TnPowerMgmtVectoredAddDropFailureLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 9, 6)
)
if mibBuilder.loadTexts:
    tnPowerMgmtVectoredAddDropFailureLog.setStatus("current")
_TnPowerMgmtTiltAdjustStartedLog_ObjectIdentity = ObjectIdentity
tnPowerMgmtTiltAdjustStartedLog = _TnPowerMgmtTiltAdjustStartedLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 9, 7)
)
if mibBuilder.loadTexts:
    tnPowerMgmtTiltAdjustStartedLog.setStatus("current")
_TnPowerMgmtTiltAdjustCompleteLog_ObjectIdentity = ObjectIdentity
tnPowerMgmtTiltAdjustCompleteLog = _TnPowerMgmtTiltAdjustCompleteLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 9, 8)
)
if mibBuilder.loadTexts:
    tnPowerMgmtTiltAdjustCompleteLog.setStatus("current")
_TnPowerMgmtTiltAdjustRequestLog_ObjectIdentity = ObjectIdentity
tnPowerMgmtTiltAdjustRequestLog = _TnPowerMgmtTiltAdjustRequestLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 9, 9)
)
if mibBuilder.loadTexts:
    tnPowerMgmtTiltAdjustRequestLog.setStatus("current")
_TnPowerMgmtTiltAdjustRequestClearedLog_ObjectIdentity = ObjectIdentity
tnPowerMgmtTiltAdjustRequestClearedLog = _TnPowerMgmtTiltAdjustRequestClearedLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 9, 10)
)
if mibBuilder.loadTexts:
    tnPowerMgmtTiltAdjustRequestClearedLog.setStatus("current")
_TnPowerMgmtExpressThruPathLossTooHighLog_ObjectIdentity = ObjectIdentity
tnPowerMgmtExpressThruPathLossTooHighLog = _TnPowerMgmtExpressThruPathLossTooHighLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 1, 9, 11)
)
if mibBuilder.loadTexts:
    tnPowerMgmtExpressThruPathLossTooHighLog.setStatus("current")
_TnLogBasics_ObjectIdentity = ObjectIdentity
tnLogBasics = _TnLogBasics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 2)
)
_TnCriticalAlarmLogTotal_Type = Unsigned32
_TnCriticalAlarmLogTotal_Object = MibScalar
tnCriticalAlarmLogTotal = _TnCriticalAlarmLogTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 2, 1),
    _TnCriticalAlarmLogTotal_Type()
)
tnCriticalAlarmLogTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCriticalAlarmLogTotal.setStatus("current")
_TnMajorAlarmLogTotal_Type = Unsigned32
_TnMajorAlarmLogTotal_Object = MibScalar
tnMajorAlarmLogTotal = _TnMajorAlarmLogTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 2, 2),
    _TnMajorAlarmLogTotal_Type()
)
tnMajorAlarmLogTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMajorAlarmLogTotal.setStatus("current")
_TnMinorAlarmLogTotal_Type = Unsigned32
_TnMinorAlarmLogTotal_Object = MibScalar
tnMinorAlarmLogTotal = _TnMinorAlarmLogTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 2, 3),
    _TnMinorAlarmLogTotal_Type()
)
tnMinorAlarmLogTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMinorAlarmLogTotal.setStatus("current")
_TnStateChangeLogTotal_Type = Unsigned32
_TnStateChangeLogTotal_Object = MibScalar
tnStateChangeLogTotal = _TnStateChangeLogTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 2, 4),
    _TnStateChangeLogTotal_Type()
)
tnStateChangeLogTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStateChangeLogTotal.setStatus("current")
_TnUserActionLogTotal_Type = Unsigned32
_TnUserActionLogTotal_Object = MibScalar
tnUserActionLogTotal = _TnUserActionLogTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 2, 5),
    _TnUserActionLogTotal_Type()
)
tnUserActionLogTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserActionLogTotal.setStatus("current")
_TnGeneralEventLogTotal_Type = Unsigned32
_TnGeneralEventLogTotal_Object = MibScalar
tnGeneralEventLogTotal = _TnGeneralEventLogTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 2, 6),
    _TnGeneralEventLogTotal_Type()
)
tnGeneralEventLogTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGeneralEventLogTotal.setStatus("current")
_TnLogTotal_Type = Unsigned32
_TnLogTotal_Object = MibScalar
tnLogTotal = _TnLogTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 2, 7),
    _TnLogTotal_Type()
)
tnLogTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLogTotal.setStatus("current")
_TnActiveAlarmTotal_Type = Unsigned32
_TnActiveAlarmTotal_Object = MibScalar
tnActiveAlarmTotal = _TnActiveAlarmTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 2, 8),
    _TnActiveAlarmTotal_Type()
)
tnActiveAlarmTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnActiveAlarmTotal.setStatus("current")
_TnPersistentLogTotal_Type = Unsigned32
_TnPersistentLogTotal_Object = MibScalar
tnPersistentLogTotal = _TnPersistentLogTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 2, 9),
    _TnPersistentLogTotal_Type()
)
tnPersistentLogTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPersistentLogTotal.setStatus("current")
_TnActiveCriticalAlarmTotal_Type = Unsigned32
_TnActiveCriticalAlarmTotal_Object = MibScalar
tnActiveCriticalAlarmTotal = _TnActiveCriticalAlarmTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 2, 10),
    _TnActiveCriticalAlarmTotal_Type()
)
tnActiveCriticalAlarmTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnActiveCriticalAlarmTotal.setStatus("current")
_TnActiveMajorAlarmTotal_Type = Unsigned32
_TnActiveMajorAlarmTotal_Object = MibScalar
tnActiveMajorAlarmTotal = _TnActiveMajorAlarmTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 2, 11),
    _TnActiveMajorAlarmTotal_Type()
)
tnActiveMajorAlarmTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnActiveMajorAlarmTotal.setStatus("current")
_TnActiveMinorAlarmTotal_Type = Unsigned32
_TnActiveMinorAlarmTotal_Object = MibScalar
tnActiveMinorAlarmTotal = _TnActiveMinorAlarmTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 2, 12),
    _TnActiveMinorAlarmTotal_Type()
)
tnActiveMinorAlarmTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnActiveMinorAlarmTotal.setStatus("current")
_TnActiveOrMaskedAlarmTotal_Type = Unsigned32
_TnActiveOrMaskedAlarmTotal_Object = MibScalar
tnActiveOrMaskedAlarmTotal = _TnActiveOrMaskedAlarmTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 2, 13),
    _TnActiveOrMaskedAlarmTotal_Type()
)
tnActiveOrMaskedAlarmTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnActiveOrMaskedAlarmTotal.setStatus("current")
_TnNotAlarmedLogTotal_Type = Unsigned32
_TnNotAlarmedLogTotal_Object = MibScalar
tnNotAlarmedLogTotal = _TnNotAlarmedLogTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 2, 14),
    _TnNotAlarmedLogTotal_Type()
)
tnNotAlarmedLogTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNotAlarmedLogTotal.setStatus("current")
_TnSecurityLogTotal_Type = Unsigned32
_TnSecurityLogTotal_Object = MibScalar
tnSecurityLogTotal = _TnSecurityLogTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 2, 15),
    _TnSecurityLogTotal_Type()
)
tnSecurityLogTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSecurityLogTotal.setStatus("current")
_TnWarningAlarmLogTotal_Type = Unsigned32
_TnWarningAlarmLogTotal_Object = MibScalar
tnWarningAlarmLogTotal = _TnWarningAlarmLogTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 2, 16),
    _TnWarningAlarmLogTotal_Type()
)
tnWarningAlarmLogTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWarningAlarmLogTotal.setStatus("current")
_TnActiveWarningAlarmTotal_Type = Unsigned32
_TnActiveWarningAlarmTotal_Object = MibScalar
tnActiveWarningAlarmTotal = _TnActiveWarningAlarmTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 2, 17),
    _TnActiveWarningAlarmTotal_Type()
)
tnActiveWarningAlarmTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnActiveWarningAlarmTotal.setStatus("current")
_TnLogQueues_ObjectIdentity = ObjectIdentity
tnLogQueues = _TnLogQueues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3)
)
_TnCriticalAlarmLogBufferTable_Object = MibTable
tnCriticalAlarmLogBufferTable = _TnCriticalAlarmLogBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    tnCriticalAlarmLogBufferTable.setStatus("current")
_TnCriticalAlarmLogBufferEntry_Object = MibTableRow
tnCriticalAlarmLogBufferEntry = _TnCriticalAlarmLogBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 1, 1)
)
tnCriticalAlarmLogBufferEntry.setIndexNames(
    (0, "TROPIC-LOG-MIB", "tnCriticalAlarmLogSerialNumber"),
)
if mibBuilder.loadTexts:
    tnCriticalAlarmLogBufferEntry.setStatus("current")


class _TnCriticalAlarmLogSerialNumber_Type(Unsigned32):
    """Custom type tnCriticalAlarmLogSerialNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TnCriticalAlarmLogSerialNumber_Type.__name__ = "Unsigned32"
_TnCriticalAlarmLogSerialNumber_Object = MibTableColumn
tnCriticalAlarmLogSerialNumber = _TnCriticalAlarmLogSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 1, 1, 1),
    _TnCriticalAlarmLogSerialNumber_Type()
)
tnCriticalAlarmLogSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCriticalAlarmLogSerialNumber.setStatus("current")
_TnCriticalAlarmLogType_Type = ObjectIdentifier
_TnCriticalAlarmLogType_Object = MibTableColumn
tnCriticalAlarmLogType = _TnCriticalAlarmLogType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 1, 1, 2),
    _TnCriticalAlarmLogType_Type()
)
tnCriticalAlarmLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCriticalAlarmLogType.setStatus("current")
_TnCriticalAlarmLogTime_Type = Unsigned32
_TnCriticalAlarmLogTime_Object = MibTableColumn
tnCriticalAlarmLogTime = _TnCriticalAlarmLogTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 1, 1, 3),
    _TnCriticalAlarmLogTime_Type()
)
tnCriticalAlarmLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCriticalAlarmLogTime.setStatus("current")
_TnCriticalAlarmLogObjectIDType_Type = Unsigned32
_TnCriticalAlarmLogObjectIDType_Object = MibTableColumn
tnCriticalAlarmLogObjectIDType = _TnCriticalAlarmLogObjectIDType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 1, 1, 4),
    _TnCriticalAlarmLogObjectIDType_Type()
)
tnCriticalAlarmLogObjectIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCriticalAlarmLogObjectIDType.setStatus("current")
_TnCriticalAlarmLogObjectID_Type = Unsigned32
_TnCriticalAlarmLogObjectID_Object = MibTableColumn
tnCriticalAlarmLogObjectID = _TnCriticalAlarmLogObjectID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 1, 1, 5),
    _TnCriticalAlarmLogObjectID_Type()
)
tnCriticalAlarmLogObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCriticalAlarmLogObjectID.setStatus("current")


class _TnCriticalAlarmLogDescr_Type(SnmpAdminString):
    """Custom type tnCriticalAlarmLogDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnCriticalAlarmLogDescr_Type.__name__ = "SnmpAdminString"
_TnCriticalAlarmLogDescr_Object = MibTableColumn
tnCriticalAlarmLogDescr = _TnCriticalAlarmLogDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 1, 1, 6),
    _TnCriticalAlarmLogDescr_Type()
)
tnCriticalAlarmLogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCriticalAlarmLogDescr.setStatus("current")


class _TnCriticalAlarmLogData_Type(SnmpAdminString):
    """Custom type tnCriticalAlarmLogData based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnCriticalAlarmLogData_Type.__name__ = "SnmpAdminString"
_TnCriticalAlarmLogData_Object = MibTableColumn
tnCriticalAlarmLogData = _TnCriticalAlarmLogData_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 1, 1, 7),
    _TnCriticalAlarmLogData_Type()
)
tnCriticalAlarmLogData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCriticalAlarmLogData.setStatus("current")
_TnCriticalAlarmLogServiceAffecting_Type = TruthValue
_TnCriticalAlarmLogServiceAffecting_Object = MibTableColumn
tnCriticalAlarmLogServiceAffecting = _TnCriticalAlarmLogServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 1, 1, 8),
    _TnCriticalAlarmLogServiceAffecting_Type()
)
tnCriticalAlarmLogServiceAffecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCriticalAlarmLogServiceAffecting.setStatus("current")
_TnCriticalAlarmLogSlotProgrammedType_Type = ObjectIdentifier
_TnCriticalAlarmLogSlotProgrammedType_Object = MibTableColumn
tnCriticalAlarmLogSlotProgrammedType = _TnCriticalAlarmLogSlotProgrammedType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 1, 1, 9),
    _TnCriticalAlarmLogSlotProgrammedType_Type()
)
tnCriticalAlarmLogSlotProgrammedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCriticalAlarmLogSlotProgrammedType.setStatus("current")
_TnCriticalAlarmLogEntityType_Type = TnEntityType
_TnCriticalAlarmLogEntityType_Object = MibTableColumn
tnCriticalAlarmLogEntityType = _TnCriticalAlarmLogEntityType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 1, 1, 10),
    _TnCriticalAlarmLogEntityType_Type()
)
tnCriticalAlarmLogEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCriticalAlarmLogEntityType.setStatus("current")
_TnCriticalAlarmLogCondition_Type = TnCondition
_TnCriticalAlarmLogCondition_Object = MibTableColumn
tnCriticalAlarmLogCondition = _TnCriticalAlarmLogCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 1, 1, 11),
    _TnCriticalAlarmLogCondition_Type()
)
tnCriticalAlarmLogCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCriticalAlarmLogCondition.setStatus("current")
_TnMajorAlarmLogBufferTable_Object = MibTable
tnMajorAlarmLogBufferTable = _TnMajorAlarmLogBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 2)
)
if mibBuilder.loadTexts:
    tnMajorAlarmLogBufferTable.setStatus("current")
_TnMajorAlarmLogBufferEntry_Object = MibTableRow
tnMajorAlarmLogBufferEntry = _TnMajorAlarmLogBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 2, 1)
)
tnMajorAlarmLogBufferEntry.setIndexNames(
    (0, "TROPIC-LOG-MIB", "tnMajorAlarmLogSerialNumber"),
)
if mibBuilder.loadTexts:
    tnMajorAlarmLogBufferEntry.setStatus("current")


class _TnMajorAlarmLogSerialNumber_Type(Unsigned32):
    """Custom type tnMajorAlarmLogSerialNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TnMajorAlarmLogSerialNumber_Type.__name__ = "Unsigned32"
_TnMajorAlarmLogSerialNumber_Object = MibTableColumn
tnMajorAlarmLogSerialNumber = _TnMajorAlarmLogSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 2, 1, 1),
    _TnMajorAlarmLogSerialNumber_Type()
)
tnMajorAlarmLogSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMajorAlarmLogSerialNumber.setStatus("current")
_TnMajorAlarmLogType_Type = ObjectIdentifier
_TnMajorAlarmLogType_Object = MibTableColumn
tnMajorAlarmLogType = _TnMajorAlarmLogType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 2, 1, 2),
    _TnMajorAlarmLogType_Type()
)
tnMajorAlarmLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMajorAlarmLogType.setStatus("current")
_TnMajorAlarmLogTime_Type = Unsigned32
_TnMajorAlarmLogTime_Object = MibTableColumn
tnMajorAlarmLogTime = _TnMajorAlarmLogTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 2, 1, 3),
    _TnMajorAlarmLogTime_Type()
)
tnMajorAlarmLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMajorAlarmLogTime.setStatus("current")
_TnMajorAlarmLogObjectIDType_Type = Unsigned32
_TnMajorAlarmLogObjectIDType_Object = MibTableColumn
tnMajorAlarmLogObjectIDType = _TnMajorAlarmLogObjectIDType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 2, 1, 4),
    _TnMajorAlarmLogObjectIDType_Type()
)
tnMajorAlarmLogObjectIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMajorAlarmLogObjectIDType.setStatus("current")
_TnMajorAlarmLogObjectID_Type = Unsigned32
_TnMajorAlarmLogObjectID_Object = MibTableColumn
tnMajorAlarmLogObjectID = _TnMajorAlarmLogObjectID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 2, 1, 5),
    _TnMajorAlarmLogObjectID_Type()
)
tnMajorAlarmLogObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMajorAlarmLogObjectID.setStatus("current")


class _TnMajorAlarmLogDescr_Type(SnmpAdminString):
    """Custom type tnMajorAlarmLogDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnMajorAlarmLogDescr_Type.__name__ = "SnmpAdminString"
_TnMajorAlarmLogDescr_Object = MibTableColumn
tnMajorAlarmLogDescr = _TnMajorAlarmLogDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 2, 1, 6),
    _TnMajorAlarmLogDescr_Type()
)
tnMajorAlarmLogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMajorAlarmLogDescr.setStatus("current")


class _TnMajorAlarmLogData_Type(SnmpAdminString):
    """Custom type tnMajorAlarmLogData based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnMajorAlarmLogData_Type.__name__ = "SnmpAdminString"
_TnMajorAlarmLogData_Object = MibTableColumn
tnMajorAlarmLogData = _TnMajorAlarmLogData_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 2, 1, 7),
    _TnMajorAlarmLogData_Type()
)
tnMajorAlarmLogData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMajorAlarmLogData.setStatus("current")
_TnMajorAlarmLogServiceAffecting_Type = TruthValue
_TnMajorAlarmLogServiceAffecting_Object = MibTableColumn
tnMajorAlarmLogServiceAffecting = _TnMajorAlarmLogServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 2, 1, 8),
    _TnMajorAlarmLogServiceAffecting_Type()
)
tnMajorAlarmLogServiceAffecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMajorAlarmLogServiceAffecting.setStatus("current")
_TnMajorAlarmLogSlotProgrammedType_Type = ObjectIdentifier
_TnMajorAlarmLogSlotProgrammedType_Object = MibTableColumn
tnMajorAlarmLogSlotProgrammedType = _TnMajorAlarmLogSlotProgrammedType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 2, 1, 9),
    _TnMajorAlarmLogSlotProgrammedType_Type()
)
tnMajorAlarmLogSlotProgrammedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMajorAlarmLogSlotProgrammedType.setStatus("current")
_TnMajorAlarmLogEntityType_Type = TnEntityType
_TnMajorAlarmLogEntityType_Object = MibTableColumn
tnMajorAlarmLogEntityType = _TnMajorAlarmLogEntityType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 2, 1, 10),
    _TnMajorAlarmLogEntityType_Type()
)
tnMajorAlarmLogEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMajorAlarmLogEntityType.setStatus("current")
_TnMajorAlarmLogCondition_Type = TnCondition
_TnMajorAlarmLogCondition_Object = MibTableColumn
tnMajorAlarmLogCondition = _TnMajorAlarmLogCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 2, 1, 11),
    _TnMajorAlarmLogCondition_Type()
)
tnMajorAlarmLogCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMajorAlarmLogCondition.setStatus("current")
_TnMinorAlarmLogBufferTable_Object = MibTable
tnMinorAlarmLogBufferTable = _TnMinorAlarmLogBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 3)
)
if mibBuilder.loadTexts:
    tnMinorAlarmLogBufferTable.setStatus("current")
_TnMinorAlarmLogBufferEntry_Object = MibTableRow
tnMinorAlarmLogBufferEntry = _TnMinorAlarmLogBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 3, 1)
)
tnMinorAlarmLogBufferEntry.setIndexNames(
    (0, "TROPIC-LOG-MIB", "tnMinorAlarmLogSerialNumber"),
)
if mibBuilder.loadTexts:
    tnMinorAlarmLogBufferEntry.setStatus("current")


class _TnMinorAlarmLogSerialNumber_Type(Unsigned32):
    """Custom type tnMinorAlarmLogSerialNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TnMinorAlarmLogSerialNumber_Type.__name__ = "Unsigned32"
_TnMinorAlarmLogSerialNumber_Object = MibTableColumn
tnMinorAlarmLogSerialNumber = _TnMinorAlarmLogSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 3, 1, 1),
    _TnMinorAlarmLogSerialNumber_Type()
)
tnMinorAlarmLogSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnMinorAlarmLogSerialNumber.setStatus("current")
_TnMinorAlarmLogType_Type = ObjectIdentifier
_TnMinorAlarmLogType_Object = MibTableColumn
tnMinorAlarmLogType = _TnMinorAlarmLogType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 3, 1, 2),
    _TnMinorAlarmLogType_Type()
)
tnMinorAlarmLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMinorAlarmLogType.setStatus("current")
_TnMinorAlarmLogTime_Type = Unsigned32
_TnMinorAlarmLogTime_Object = MibTableColumn
tnMinorAlarmLogTime = _TnMinorAlarmLogTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 3, 1, 3),
    _TnMinorAlarmLogTime_Type()
)
tnMinorAlarmLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMinorAlarmLogTime.setStatus("current")
_TnMinorAlarmLogObjectIDType_Type = Unsigned32
_TnMinorAlarmLogObjectIDType_Object = MibTableColumn
tnMinorAlarmLogObjectIDType = _TnMinorAlarmLogObjectIDType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 3, 1, 4),
    _TnMinorAlarmLogObjectIDType_Type()
)
tnMinorAlarmLogObjectIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMinorAlarmLogObjectIDType.setStatus("current")
_TnMinorAlarmLogObjectID_Type = Unsigned32
_TnMinorAlarmLogObjectID_Object = MibTableColumn
tnMinorAlarmLogObjectID = _TnMinorAlarmLogObjectID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 3, 1, 5),
    _TnMinorAlarmLogObjectID_Type()
)
tnMinorAlarmLogObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMinorAlarmLogObjectID.setStatus("current")


class _TnMinorAlarmLogDescr_Type(SnmpAdminString):
    """Custom type tnMinorAlarmLogDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnMinorAlarmLogDescr_Type.__name__ = "SnmpAdminString"
_TnMinorAlarmLogDescr_Object = MibTableColumn
tnMinorAlarmLogDescr = _TnMinorAlarmLogDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 3, 1, 6),
    _TnMinorAlarmLogDescr_Type()
)
tnMinorAlarmLogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMinorAlarmLogDescr.setStatus("current")


class _TnMinorAlarmLogData_Type(SnmpAdminString):
    """Custom type tnMinorAlarmLogData based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnMinorAlarmLogData_Type.__name__ = "SnmpAdminString"
_TnMinorAlarmLogData_Object = MibTableColumn
tnMinorAlarmLogData = _TnMinorAlarmLogData_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 3, 1, 7),
    _TnMinorAlarmLogData_Type()
)
tnMinorAlarmLogData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMinorAlarmLogData.setStatus("current")
_TnMinorAlarmLogServiceAffecting_Type = TruthValue
_TnMinorAlarmLogServiceAffecting_Object = MibTableColumn
tnMinorAlarmLogServiceAffecting = _TnMinorAlarmLogServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 3, 1, 8),
    _TnMinorAlarmLogServiceAffecting_Type()
)
tnMinorAlarmLogServiceAffecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMinorAlarmLogServiceAffecting.setStatus("current")
_TnMinorAlarmLogSlotProgrammedType_Type = ObjectIdentifier
_TnMinorAlarmLogSlotProgrammedType_Object = MibTableColumn
tnMinorAlarmLogSlotProgrammedType = _TnMinorAlarmLogSlotProgrammedType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 3, 1, 9),
    _TnMinorAlarmLogSlotProgrammedType_Type()
)
tnMinorAlarmLogSlotProgrammedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMinorAlarmLogSlotProgrammedType.setStatus("current")
_TnMinorAlarmLogEntityType_Type = TnEntityType
_TnMinorAlarmLogEntityType_Object = MibTableColumn
tnMinorAlarmLogEntityType = _TnMinorAlarmLogEntityType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 3, 1, 10),
    _TnMinorAlarmLogEntityType_Type()
)
tnMinorAlarmLogEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMinorAlarmLogEntityType.setStatus("current")
_TnMinorAlarmLogCondition_Type = TnCondition
_TnMinorAlarmLogCondition_Object = MibTableColumn
tnMinorAlarmLogCondition = _TnMinorAlarmLogCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 3, 1, 11),
    _TnMinorAlarmLogCondition_Type()
)
tnMinorAlarmLogCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnMinorAlarmLogCondition.setStatus("current")
_TnStateChangeLogBufferTable_Object = MibTable
tnStateChangeLogBufferTable = _TnStateChangeLogBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 4)
)
if mibBuilder.loadTexts:
    tnStateChangeLogBufferTable.setStatus("current")
_TnStateChangeLogBufferEntry_Object = MibTableRow
tnStateChangeLogBufferEntry = _TnStateChangeLogBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 4, 1)
)
tnStateChangeLogBufferEntry.setIndexNames(
    (0, "TROPIC-LOG-MIB", "tnStateChangeLogSerialNumber"),
)
if mibBuilder.loadTexts:
    tnStateChangeLogBufferEntry.setStatus("current")


class _TnStateChangeLogSerialNumber_Type(Unsigned32):
    """Custom type tnStateChangeLogSerialNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TnStateChangeLogSerialNumber_Type.__name__ = "Unsigned32"
_TnStateChangeLogSerialNumber_Object = MibTableColumn
tnStateChangeLogSerialNumber = _TnStateChangeLogSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 4, 1, 1),
    _TnStateChangeLogSerialNumber_Type()
)
tnStateChangeLogSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnStateChangeLogSerialNumber.setStatus("current")
_TnStateChangeLogType_Type = ObjectIdentifier
_TnStateChangeLogType_Object = MibTableColumn
tnStateChangeLogType = _TnStateChangeLogType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 4, 1, 2),
    _TnStateChangeLogType_Type()
)
tnStateChangeLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStateChangeLogType.setStatus("current")
_TnStateChangeLogTime_Type = Unsigned32
_TnStateChangeLogTime_Object = MibTableColumn
tnStateChangeLogTime = _TnStateChangeLogTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 4, 1, 3),
    _TnStateChangeLogTime_Type()
)
tnStateChangeLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStateChangeLogTime.setStatus("current")
_TnStateChangeLogObjectIDType_Type = Unsigned32
_TnStateChangeLogObjectIDType_Object = MibTableColumn
tnStateChangeLogObjectIDType = _TnStateChangeLogObjectIDType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 4, 1, 4),
    _TnStateChangeLogObjectIDType_Type()
)
tnStateChangeLogObjectIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStateChangeLogObjectIDType.setStatus("current")
_TnStateChangeLogObjectID_Type = Unsigned32
_TnStateChangeLogObjectID_Object = MibTableColumn
tnStateChangeLogObjectID = _TnStateChangeLogObjectID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 4, 1, 5),
    _TnStateChangeLogObjectID_Type()
)
tnStateChangeLogObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStateChangeLogObjectID.setStatus("current")


class _TnStateChangeLogDescr_Type(SnmpAdminString):
    """Custom type tnStateChangeLogDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnStateChangeLogDescr_Type.__name__ = "SnmpAdminString"
_TnStateChangeLogDescr_Object = MibTableColumn
tnStateChangeLogDescr = _TnStateChangeLogDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 4, 1, 6),
    _TnStateChangeLogDescr_Type()
)
tnStateChangeLogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStateChangeLogDescr.setStatus("current")


class _TnStateChangeLogData_Type(SnmpAdminString):
    """Custom type tnStateChangeLogData based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnStateChangeLogData_Type.__name__ = "SnmpAdminString"
_TnStateChangeLogData_Object = MibTableColumn
tnStateChangeLogData = _TnStateChangeLogData_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 4, 1, 7),
    _TnStateChangeLogData_Type()
)
tnStateChangeLogData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStateChangeLogData.setStatus("current")
_TnStateChangeLogSlotProgrammedType_Type = ObjectIdentifier
_TnStateChangeLogSlotProgrammedType_Object = MibTableColumn
tnStateChangeLogSlotProgrammedType = _TnStateChangeLogSlotProgrammedType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 4, 1, 8),
    _TnStateChangeLogSlotProgrammedType_Type()
)
tnStateChangeLogSlotProgrammedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnStateChangeLogSlotProgrammedType.setStatus("current")
_TnUserActionLogBufferTable_Object = MibTable
tnUserActionLogBufferTable = _TnUserActionLogBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 5)
)
if mibBuilder.loadTexts:
    tnUserActionLogBufferTable.setStatus("current")
_TnUserActionLogBufferEntry_Object = MibTableRow
tnUserActionLogBufferEntry = _TnUserActionLogBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 5, 1)
)
tnUserActionLogBufferEntry.setIndexNames(
    (0, "TROPIC-LOG-MIB", "tnUserActionLogSerialNumber"),
)
if mibBuilder.loadTexts:
    tnUserActionLogBufferEntry.setStatus("current")


class _TnUserActionLogSerialNumber_Type(Unsigned32):
    """Custom type tnUserActionLogSerialNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TnUserActionLogSerialNumber_Type.__name__ = "Unsigned32"
_TnUserActionLogSerialNumber_Object = MibTableColumn
tnUserActionLogSerialNumber = _TnUserActionLogSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 5, 1, 1),
    _TnUserActionLogSerialNumber_Type()
)
tnUserActionLogSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnUserActionLogSerialNumber.setStatus("current")
_TnUserActionLogType_Type = ObjectIdentifier
_TnUserActionLogType_Object = MibTableColumn
tnUserActionLogType = _TnUserActionLogType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 5, 1, 2),
    _TnUserActionLogType_Type()
)
tnUserActionLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserActionLogType.setStatus("current")
_TnUserActionLogTime_Type = Unsigned32
_TnUserActionLogTime_Object = MibTableColumn
tnUserActionLogTime = _TnUserActionLogTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 5, 1, 3),
    _TnUserActionLogTime_Type()
)
tnUserActionLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserActionLogTime.setStatus("current")
_TnUserActionLogObjectIDType_Type = Unsigned32
_TnUserActionLogObjectIDType_Object = MibTableColumn
tnUserActionLogObjectIDType = _TnUserActionLogObjectIDType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 5, 1, 4),
    _TnUserActionLogObjectIDType_Type()
)
tnUserActionLogObjectIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserActionLogObjectIDType.setStatus("current")
_TnUserActionLogObjectID_Type = Unsigned32
_TnUserActionLogObjectID_Object = MibTableColumn
tnUserActionLogObjectID = _TnUserActionLogObjectID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 5, 1, 5),
    _TnUserActionLogObjectID_Type()
)
tnUserActionLogObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserActionLogObjectID.setStatus("current")


class _TnUserActionLogDescr_Type(SnmpAdminString):
    """Custom type tnUserActionLogDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnUserActionLogDescr_Type.__name__ = "SnmpAdminString"
_TnUserActionLogDescr_Object = MibTableColumn
tnUserActionLogDescr = _TnUserActionLogDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 5, 1, 6),
    _TnUserActionLogDescr_Type()
)
tnUserActionLogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserActionLogDescr.setStatus("current")
_TnUserActionLogChangedObject_Type = ObjectIdentifier
_TnUserActionLogChangedObject_Object = MibTableColumn
tnUserActionLogChangedObject = _TnUserActionLogChangedObject_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 5, 1, 7),
    _TnUserActionLogChangedObject_Type()
)
tnUserActionLogChangedObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserActionLogChangedObject.setStatus("current")


class _TnUserActionLogData_Type(SnmpAdminString):
    """Custom type tnUserActionLogData based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnUserActionLogData_Type.__name__ = "SnmpAdminString"
_TnUserActionLogData_Object = MibTableColumn
tnUserActionLogData = _TnUserActionLogData_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 5, 1, 8),
    _TnUserActionLogData_Type()
)
tnUserActionLogData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserActionLogData.setStatus("current")
_TnGeneralEventLogBufferTable_Object = MibTable
tnGeneralEventLogBufferTable = _TnGeneralEventLogBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 6)
)
if mibBuilder.loadTexts:
    tnGeneralEventLogBufferTable.setStatus("current")
_TnGeneralEventLogBufferEntry_Object = MibTableRow
tnGeneralEventLogBufferEntry = _TnGeneralEventLogBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 6, 1)
)
tnGeneralEventLogBufferEntry.setIndexNames(
    (0, "TROPIC-LOG-MIB", "tnGeneralEventLogSerialNumber"),
)
if mibBuilder.loadTexts:
    tnGeneralEventLogBufferEntry.setStatus("current")


class _TnGeneralEventLogSerialNumber_Type(Unsigned32):
    """Custom type tnGeneralEventLogSerialNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TnGeneralEventLogSerialNumber_Type.__name__ = "Unsigned32"
_TnGeneralEventLogSerialNumber_Object = MibTableColumn
tnGeneralEventLogSerialNumber = _TnGeneralEventLogSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 6, 1, 1),
    _TnGeneralEventLogSerialNumber_Type()
)
tnGeneralEventLogSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGeneralEventLogSerialNumber.setStatus("current")
_TnGeneralEventLogType_Type = ObjectIdentifier
_TnGeneralEventLogType_Object = MibTableColumn
tnGeneralEventLogType = _TnGeneralEventLogType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 6, 1, 2),
    _TnGeneralEventLogType_Type()
)
tnGeneralEventLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGeneralEventLogType.setStatus("current")
_TnGeneralEventLogTime_Type = Unsigned32
_TnGeneralEventLogTime_Object = MibTableColumn
tnGeneralEventLogTime = _TnGeneralEventLogTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 6, 1, 3),
    _TnGeneralEventLogTime_Type()
)
tnGeneralEventLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGeneralEventLogTime.setStatus("current")
_TnGeneralEventLogObjectIDType_Type = Unsigned32
_TnGeneralEventLogObjectIDType_Object = MibTableColumn
tnGeneralEventLogObjectIDType = _TnGeneralEventLogObjectIDType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 6, 1, 4),
    _TnGeneralEventLogObjectIDType_Type()
)
tnGeneralEventLogObjectIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGeneralEventLogObjectIDType.setStatus("current")
_TnGeneralEventLogObjectID_Type = Unsigned32
_TnGeneralEventLogObjectID_Object = MibTableColumn
tnGeneralEventLogObjectID = _TnGeneralEventLogObjectID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 6, 1, 5),
    _TnGeneralEventLogObjectID_Type()
)
tnGeneralEventLogObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGeneralEventLogObjectID.setStatus("current")


class _TnGeneralEventLogDescr_Type(SnmpAdminString):
    """Custom type tnGeneralEventLogDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnGeneralEventLogDescr_Type.__name__ = "SnmpAdminString"
_TnGeneralEventLogDescr_Object = MibTableColumn
tnGeneralEventLogDescr = _TnGeneralEventLogDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 6, 1, 6),
    _TnGeneralEventLogDescr_Type()
)
tnGeneralEventLogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGeneralEventLogDescr.setStatus("current")
_TnGeneralEventLogChangedObject_Type = ObjectIdentifier
_TnGeneralEventLogChangedObject_Object = MibTableColumn
tnGeneralEventLogChangedObject = _TnGeneralEventLogChangedObject_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 6, 1, 7),
    _TnGeneralEventLogChangedObject_Type()
)
tnGeneralEventLogChangedObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGeneralEventLogChangedObject.setStatus("current")


class _TnGeneralEventLogData_Type(SnmpAdminString):
    """Custom type tnGeneralEventLogData based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnGeneralEventLogData_Type.__name__ = "SnmpAdminString"
_TnGeneralEventLogData_Object = MibTableColumn
tnGeneralEventLogData = _TnGeneralEventLogData_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 6, 1, 8),
    _TnGeneralEventLogData_Type()
)
tnGeneralEventLogData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGeneralEventLogData.setStatus("current")
_TnGeneralEventLogSlotProgrammedType_Type = ObjectIdentifier
_TnGeneralEventLogSlotProgrammedType_Object = MibTableColumn
tnGeneralEventLogSlotProgrammedType = _TnGeneralEventLogSlotProgrammedType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 6, 1, 9),
    _TnGeneralEventLogSlotProgrammedType_Type()
)
tnGeneralEventLogSlotProgrammedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGeneralEventLogSlotProgrammedType.setStatus("current")
_TnLogBufferTable_Object = MibTable
tnLogBufferTable = _TnLogBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 7)
)
if mibBuilder.loadTexts:
    tnLogBufferTable.setStatus("current")
_TnLogBufferEntry_Object = MibTableRow
tnLogBufferEntry = _TnLogBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 7, 1)
)
tnLogBufferEntry.setIndexNames(
    (0, "TROPIC-LOG-MIB", "tnLogSerialNumber"),
)
if mibBuilder.loadTexts:
    tnLogBufferEntry.setStatus("current")


class _TnLogSerialNumber_Type(Unsigned32):
    """Custom type tnLogSerialNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TnLogSerialNumber_Type.__name__ = "Unsigned32"
_TnLogSerialNumber_Object = MibTableColumn
tnLogSerialNumber = _TnLogSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 7, 1, 1),
    _TnLogSerialNumber_Type()
)
tnLogSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLogSerialNumber.setStatus("current")
_TnLogType_Type = ObjectIdentifier
_TnLogType_Object = MibTableColumn
tnLogType = _TnLogType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 7, 1, 2),
    _TnLogType_Type()
)
tnLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLogType.setStatus("current")
_TnLogTime_Type = Unsigned32
_TnLogTime_Object = MibTableColumn
tnLogTime = _TnLogTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 7, 1, 3),
    _TnLogTime_Type()
)
tnLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLogTime.setStatus("current")
_TnLogObjectIDType_Type = Unsigned32
_TnLogObjectIDType_Object = MibTableColumn
tnLogObjectIDType = _TnLogObjectIDType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 7, 1, 4),
    _TnLogObjectIDType_Type()
)
tnLogObjectIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLogObjectIDType.setStatus("current")
_TnLogObjectID_Type = Unsigned32
_TnLogObjectID_Object = MibTableColumn
tnLogObjectID = _TnLogObjectID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 7, 1, 5),
    _TnLogObjectID_Type()
)
tnLogObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLogObjectID.setStatus("current")
_TnLogCategory_Type = TnTrapCategory
_TnLogCategory_Object = MibTableColumn
tnLogCategory = _TnLogCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 7, 1, 6),
    _TnLogCategory_Type()
)
tnLogCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLogCategory.setStatus("current")


class _TnLogDescr_Type(SnmpAdminString):
    """Custom type tnLogDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnLogDescr_Type.__name__ = "SnmpAdminString"
_TnLogDescr_Object = MibTableColumn
tnLogDescr = _TnLogDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 7, 1, 7),
    _TnLogDescr_Type()
)
tnLogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLogDescr.setStatus("current")
_TnLogChangedObject_Type = ObjectIdentifier
_TnLogChangedObject_Object = MibTableColumn
tnLogChangedObject = _TnLogChangedObject_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 7, 1, 8),
    _TnLogChangedObject_Type()
)
tnLogChangedObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLogChangedObject.setStatus("current")


class _TnLogData_Type(SnmpAdminString):
    """Custom type tnLogData based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnLogData_Type.__name__ = "SnmpAdminString"
_TnLogData_Object = MibTableColumn
tnLogData = _TnLogData_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 7, 1, 9),
    _TnLogData_Type()
)
tnLogData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLogData.setStatus("current")
_TnLogServiceAffecting_Type = TruthValue
_TnLogServiceAffecting_Object = MibTableColumn
tnLogServiceAffecting = _TnLogServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 7, 1, 10),
    _TnLogServiceAffecting_Type()
)
tnLogServiceAffecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLogServiceAffecting.setStatus("current")
_TnLogSlotProgrammedType_Type = ObjectIdentifier
_TnLogSlotProgrammedType_Object = MibTableColumn
tnLogSlotProgrammedType = _TnLogSlotProgrammedType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 7, 1, 11),
    _TnLogSlotProgrammedType_Type()
)
tnLogSlotProgrammedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLogSlotProgrammedType.setStatus("current")
_TnLogEntityType_Type = TnEntityType
_TnLogEntityType_Object = MibTableColumn
tnLogEntityType = _TnLogEntityType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 7, 1, 12),
    _TnLogEntityType_Type()
)
tnLogEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLogEntityType.setStatus("current")
_TnLogCondition_Type = TnCondition
_TnLogCondition_Object = MibTableColumn
tnLogCondition = _TnLogCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 7, 1, 13),
    _TnLogCondition_Type()
)
tnLogCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLogCondition.setStatus("current")
_TnActiveAlarmTable_Object = MibTable
tnActiveAlarmTable = _TnActiveAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 8)
)
if mibBuilder.loadTexts:
    tnActiveAlarmTable.setStatus("current")
_TnActiveAlarmEntry_Object = MibTableRow
tnActiveAlarmEntry = _TnActiveAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 8, 1)
)
tnActiveAlarmEntry.setIndexNames(
    (0, "TROPIC-LOG-MIB", "tnActiveAlarmSerialNumber"),
)
if mibBuilder.loadTexts:
    tnActiveAlarmEntry.setStatus("current")


class _TnActiveAlarmSerialNumber_Type(Unsigned32):
    """Custom type tnActiveAlarmSerialNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TnActiveAlarmSerialNumber_Type.__name__ = "Unsigned32"
_TnActiveAlarmSerialNumber_Object = MibTableColumn
tnActiveAlarmSerialNumber = _TnActiveAlarmSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 8, 1, 1),
    _TnActiveAlarmSerialNumber_Type()
)
tnActiveAlarmSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnActiveAlarmSerialNumber.setStatus("current")
_TnActiveAlarmType_Type = ObjectIdentifier
_TnActiveAlarmType_Object = MibTableColumn
tnActiveAlarmType = _TnActiveAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 8, 1, 2),
    _TnActiveAlarmType_Type()
)
tnActiveAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnActiveAlarmType.setStatus("current")
_TnActiveAlarmTime_Type = Unsigned32
_TnActiveAlarmTime_Object = MibTableColumn
tnActiveAlarmTime = _TnActiveAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 8, 1, 3),
    _TnActiveAlarmTime_Type()
)
tnActiveAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnActiveAlarmTime.setStatus("current")
_TnActiveAlarmObjectIDType_Type = Unsigned32
_TnActiveAlarmObjectIDType_Object = MibTableColumn
tnActiveAlarmObjectIDType = _TnActiveAlarmObjectIDType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 8, 1, 4),
    _TnActiveAlarmObjectIDType_Type()
)
tnActiveAlarmObjectIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnActiveAlarmObjectIDType.setStatus("current")
_TnActiveAlarmObjectID_Type = Unsigned32
_TnActiveAlarmObjectID_Object = MibTableColumn
tnActiveAlarmObjectID = _TnActiveAlarmObjectID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 8, 1, 5),
    _TnActiveAlarmObjectID_Type()
)
tnActiveAlarmObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnActiveAlarmObjectID.setStatus("current")
_TnActiveAlarmCategory_Type = TnTrapCategory
_TnActiveAlarmCategory_Object = MibTableColumn
tnActiveAlarmCategory = _TnActiveAlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 8, 1, 6),
    _TnActiveAlarmCategory_Type()
)
tnActiveAlarmCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnActiveAlarmCategory.setStatus("current")


class _TnActiveAlarmDescr_Type(SnmpAdminString):
    """Custom type tnActiveAlarmDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnActiveAlarmDescr_Type.__name__ = "SnmpAdminString"
_TnActiveAlarmDescr_Object = MibTableColumn
tnActiveAlarmDescr = _TnActiveAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 8, 1, 7),
    _TnActiveAlarmDescr_Type()
)
tnActiveAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnActiveAlarmDescr.setStatus("current")


class _TnActiveAlarmData_Type(SnmpAdminString):
    """Custom type tnActiveAlarmData based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnActiveAlarmData_Type.__name__ = "SnmpAdminString"
_TnActiveAlarmData_Object = MibTableColumn
tnActiveAlarmData = _TnActiveAlarmData_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 8, 1, 8),
    _TnActiveAlarmData_Type()
)
tnActiveAlarmData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnActiveAlarmData.setStatus("current")
_TnActiveAlarmServiceAffecting_Type = TruthValue
_TnActiveAlarmServiceAffecting_Object = MibTableColumn
tnActiveAlarmServiceAffecting = _TnActiveAlarmServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 8, 1, 9),
    _TnActiveAlarmServiceAffecting_Type()
)
tnActiveAlarmServiceAffecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnActiveAlarmServiceAffecting.setStatus("current")
_TnActiveAlarmSlotProgrammedType_Type = ObjectIdentifier
_TnActiveAlarmSlotProgrammedType_Object = MibTableColumn
tnActiveAlarmSlotProgrammedType = _TnActiveAlarmSlotProgrammedType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 8, 1, 10),
    _TnActiveAlarmSlotProgrammedType_Type()
)
tnActiveAlarmSlotProgrammedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnActiveAlarmSlotProgrammedType.setStatus("current")
_TnActiveAlarmEntityType_Type = TnEntityType
_TnActiveAlarmEntityType_Object = MibTableColumn
tnActiveAlarmEntityType = _TnActiveAlarmEntityType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 8, 1, 11),
    _TnActiveAlarmEntityType_Type()
)
tnActiveAlarmEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnActiveAlarmEntityType.setStatus("current")
_TnActiveAlarmCondition_Type = TnCondition
_TnActiveAlarmCondition_Object = MibTableColumn
tnActiveAlarmCondition = _TnActiveAlarmCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 8, 1, 12),
    _TnActiveAlarmCondition_Type()
)
tnActiveAlarmCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnActiveAlarmCondition.setStatus("current")
_TnPersistentLogBufferTable_Object = MibTable
tnPersistentLogBufferTable = _TnPersistentLogBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 9)
)
if mibBuilder.loadTexts:
    tnPersistentLogBufferTable.setStatus("current")
_TnPersistentLogBufferEntry_Object = MibTableRow
tnPersistentLogBufferEntry = _TnPersistentLogBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 9, 1)
)
tnPersistentLogBufferEntry.setIndexNames(
    (0, "TROPIC-LOG-MIB", "tnPersistentLogSerialNumber"),
)
if mibBuilder.loadTexts:
    tnPersistentLogBufferEntry.setStatus("current")


class _TnPersistentLogSerialNumber_Type(Unsigned32):
    """Custom type tnPersistentLogSerialNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TnPersistentLogSerialNumber_Type.__name__ = "Unsigned32"
_TnPersistentLogSerialNumber_Object = MibTableColumn
tnPersistentLogSerialNumber = _TnPersistentLogSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 9, 1, 1),
    _TnPersistentLogSerialNumber_Type()
)
tnPersistentLogSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPersistentLogSerialNumber.setStatus("current")
_TnPersistentLogType_Type = ObjectIdentifier
_TnPersistentLogType_Object = MibTableColumn
tnPersistentLogType = _TnPersistentLogType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 9, 1, 2),
    _TnPersistentLogType_Type()
)
tnPersistentLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPersistentLogType.setStatus("current")
_TnPersistentLogTime_Type = Unsigned32
_TnPersistentLogTime_Object = MibTableColumn
tnPersistentLogTime = _TnPersistentLogTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 9, 1, 3),
    _TnPersistentLogTime_Type()
)
tnPersistentLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPersistentLogTime.setStatus("current")
_TnPersistentLogObjectIDType_Type = Unsigned32
_TnPersistentLogObjectIDType_Object = MibTableColumn
tnPersistentLogObjectIDType = _TnPersistentLogObjectIDType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 9, 1, 4),
    _TnPersistentLogObjectIDType_Type()
)
tnPersistentLogObjectIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPersistentLogObjectIDType.setStatus("current")
_TnPersistentLogObjectID_Type = Unsigned32
_TnPersistentLogObjectID_Object = MibTableColumn
tnPersistentLogObjectID = _TnPersistentLogObjectID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 9, 1, 5),
    _TnPersistentLogObjectID_Type()
)
tnPersistentLogObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPersistentLogObjectID.setStatus("current")
_TnPersistentLogCategory_Type = TnTrapCategory
_TnPersistentLogCategory_Object = MibTableColumn
tnPersistentLogCategory = _TnPersistentLogCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 9, 1, 6),
    _TnPersistentLogCategory_Type()
)
tnPersistentLogCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPersistentLogCategory.setStatus("current")


class _TnPersistentLogDescr_Type(SnmpAdminString):
    """Custom type tnPersistentLogDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnPersistentLogDescr_Type.__name__ = "SnmpAdminString"
_TnPersistentLogDescr_Object = MibTableColumn
tnPersistentLogDescr = _TnPersistentLogDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 9, 1, 7),
    _TnPersistentLogDescr_Type()
)
tnPersistentLogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPersistentLogDescr.setStatus("current")
_TnPersistentLogChangedObject_Type = ObjectIdentifier
_TnPersistentLogChangedObject_Object = MibTableColumn
tnPersistentLogChangedObject = _TnPersistentLogChangedObject_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 9, 1, 8),
    _TnPersistentLogChangedObject_Type()
)
tnPersistentLogChangedObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPersistentLogChangedObject.setStatus("current")


class _TnPersistentLogData_Type(SnmpAdminString):
    """Custom type tnPersistentLogData based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnPersistentLogData_Type.__name__ = "SnmpAdminString"
_TnPersistentLogData_Object = MibTableColumn
tnPersistentLogData = _TnPersistentLogData_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 9, 1, 9),
    _TnPersistentLogData_Type()
)
tnPersistentLogData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPersistentLogData.setStatus("current")
_TnPersistentLogServiceAffecting_Type = TruthValue
_TnPersistentLogServiceAffecting_Object = MibTableColumn
tnPersistentLogServiceAffecting = _TnPersistentLogServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 9, 1, 10),
    _TnPersistentLogServiceAffecting_Type()
)
tnPersistentLogServiceAffecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPersistentLogServiceAffecting.setStatus("current")
_TnPersistentLogSlotProgrammedType_Type = ObjectIdentifier
_TnPersistentLogSlotProgrammedType_Object = MibTableColumn
tnPersistentLogSlotProgrammedType = _TnPersistentLogSlotProgrammedType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 9, 1, 11),
    _TnPersistentLogSlotProgrammedType_Type()
)
tnPersistentLogSlotProgrammedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPersistentLogSlotProgrammedType.setStatus("current")
_TnActiveOrMaskedAlarmTable_Object = MibTable
tnActiveOrMaskedAlarmTable = _TnActiveOrMaskedAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 10)
)
if mibBuilder.loadTexts:
    tnActiveOrMaskedAlarmTable.setStatus("current")
_TnActiveOrMaskedAlarmEntry_Object = MibTableRow
tnActiveOrMaskedAlarmEntry = _TnActiveOrMaskedAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 10, 1)
)
tnActiveOrMaskedAlarmEntry.setIndexNames(
    (0, "TROPIC-LOG-MIB", "tnActiveOrMaskedAlarmSerialNumber"),
)
if mibBuilder.loadTexts:
    tnActiveOrMaskedAlarmEntry.setStatus("current")


class _TnActiveOrMaskedAlarmSerialNumber_Type(Unsigned32):
    """Custom type tnActiveOrMaskedAlarmSerialNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TnActiveOrMaskedAlarmSerialNumber_Type.__name__ = "Unsigned32"
_TnActiveOrMaskedAlarmSerialNumber_Object = MibTableColumn
tnActiveOrMaskedAlarmSerialNumber = _TnActiveOrMaskedAlarmSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 10, 1, 1),
    _TnActiveOrMaskedAlarmSerialNumber_Type()
)
tnActiveOrMaskedAlarmSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnActiveOrMaskedAlarmSerialNumber.setStatus("current")
_TnActiveOrMaskedAlarmType_Type = ObjectIdentifier
_TnActiveOrMaskedAlarmType_Object = MibTableColumn
tnActiveOrMaskedAlarmType = _TnActiveOrMaskedAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 10, 1, 2),
    _TnActiveOrMaskedAlarmType_Type()
)
tnActiveOrMaskedAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnActiveOrMaskedAlarmType.setStatus("current")
_TnActiveOrMaskedAlarmTime_Type = Unsigned32
_TnActiveOrMaskedAlarmTime_Object = MibTableColumn
tnActiveOrMaskedAlarmTime = _TnActiveOrMaskedAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 10, 1, 3),
    _TnActiveOrMaskedAlarmTime_Type()
)
tnActiveOrMaskedAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnActiveOrMaskedAlarmTime.setStatus("current")
_TnActiveOrMaskedAlarmObjectIDType_Type = Unsigned32
_TnActiveOrMaskedAlarmObjectIDType_Object = MibTableColumn
tnActiveOrMaskedAlarmObjectIDType = _TnActiveOrMaskedAlarmObjectIDType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 10, 1, 4),
    _TnActiveOrMaskedAlarmObjectIDType_Type()
)
tnActiveOrMaskedAlarmObjectIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnActiveOrMaskedAlarmObjectIDType.setStatus("current")
_TnActiveOrMaskedAlarmObjectID_Type = Unsigned32
_TnActiveOrMaskedAlarmObjectID_Object = MibTableColumn
tnActiveOrMaskedAlarmObjectID = _TnActiveOrMaskedAlarmObjectID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 10, 1, 5),
    _TnActiveOrMaskedAlarmObjectID_Type()
)
tnActiveOrMaskedAlarmObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnActiveOrMaskedAlarmObjectID.setStatus("current")
_TnActiveOrMaskedAlarmCategory_Type = TnTrapCategory
_TnActiveOrMaskedAlarmCategory_Object = MibTableColumn
tnActiveOrMaskedAlarmCategory = _TnActiveOrMaskedAlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 10, 1, 6),
    _TnActiveOrMaskedAlarmCategory_Type()
)
tnActiveOrMaskedAlarmCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnActiveOrMaskedAlarmCategory.setStatus("current")


class _TnActiveOrMaskedAlarmDescr_Type(SnmpAdminString):
    """Custom type tnActiveOrMaskedAlarmDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnActiveOrMaskedAlarmDescr_Type.__name__ = "SnmpAdminString"
_TnActiveOrMaskedAlarmDescr_Object = MibTableColumn
tnActiveOrMaskedAlarmDescr = _TnActiveOrMaskedAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 10, 1, 7),
    _TnActiveOrMaskedAlarmDescr_Type()
)
tnActiveOrMaskedAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnActiveOrMaskedAlarmDescr.setStatus("current")


class _TnActiveOrMaskedAlarmData_Type(SnmpAdminString):
    """Custom type tnActiveOrMaskedAlarmData based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnActiveOrMaskedAlarmData_Type.__name__ = "SnmpAdminString"
_TnActiveOrMaskedAlarmData_Object = MibTableColumn
tnActiveOrMaskedAlarmData = _TnActiveOrMaskedAlarmData_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 10, 1, 8),
    _TnActiveOrMaskedAlarmData_Type()
)
tnActiveOrMaskedAlarmData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnActiveOrMaskedAlarmData.setStatus("current")
_TnActiveOrMaskedAlarmServiceAffecting_Type = TruthValue
_TnActiveOrMaskedAlarmServiceAffecting_Object = MibTableColumn
tnActiveOrMaskedAlarmServiceAffecting = _TnActiveOrMaskedAlarmServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 10, 1, 9),
    _TnActiveOrMaskedAlarmServiceAffecting_Type()
)
tnActiveOrMaskedAlarmServiceAffecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnActiveOrMaskedAlarmServiceAffecting.setStatus("current")
_TnActiveOrMaskedAlarmSlotProgrammedType_Type = ObjectIdentifier
_TnActiveOrMaskedAlarmSlotProgrammedType_Object = MibTableColumn
tnActiveOrMaskedAlarmSlotProgrammedType = _TnActiveOrMaskedAlarmSlotProgrammedType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 10, 1, 10),
    _TnActiveOrMaskedAlarmSlotProgrammedType_Type()
)
tnActiveOrMaskedAlarmSlotProgrammedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnActiveOrMaskedAlarmSlotProgrammedType.setStatus("current")
_TnActiveOrMaskedAlarmIsMasked_Type = TruthValue
_TnActiveOrMaskedAlarmIsMasked_Object = MibTableColumn
tnActiveOrMaskedAlarmIsMasked = _TnActiveOrMaskedAlarmIsMasked_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 10, 1, 11),
    _TnActiveOrMaskedAlarmIsMasked_Type()
)
tnActiveOrMaskedAlarmIsMasked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnActiveOrMaskedAlarmIsMasked.setStatus("current")
_TnActiveOrMaskedAlarmEntityType_Type = TnEntityType
_TnActiveOrMaskedAlarmEntityType_Object = MibTableColumn
tnActiveOrMaskedAlarmEntityType = _TnActiveOrMaskedAlarmEntityType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 10, 1, 12),
    _TnActiveOrMaskedAlarmEntityType_Type()
)
tnActiveOrMaskedAlarmEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnActiveOrMaskedAlarmEntityType.setStatus("current")
_TnActiveOrMaskedAlarmCondition_Type = TnCondition
_TnActiveOrMaskedAlarmCondition_Object = MibTableColumn
tnActiveOrMaskedAlarmCondition = _TnActiveOrMaskedAlarmCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 10, 1, 13),
    _TnActiveOrMaskedAlarmCondition_Type()
)
tnActiveOrMaskedAlarmCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnActiveOrMaskedAlarmCondition.setStatus("current")
_TnNotAlarmedLogBufferTable_Object = MibTable
tnNotAlarmedLogBufferTable = _TnNotAlarmedLogBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 11)
)
if mibBuilder.loadTexts:
    tnNotAlarmedLogBufferTable.setStatus("current")
_TnNotAlarmedLogBufferEntry_Object = MibTableRow
tnNotAlarmedLogBufferEntry = _TnNotAlarmedLogBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 11, 1)
)
tnNotAlarmedLogBufferEntry.setIndexNames(
    (0, "TROPIC-LOG-MIB", "tnNotAlarmedLogSerialNumber"),
)
if mibBuilder.loadTexts:
    tnNotAlarmedLogBufferEntry.setStatus("current")


class _TnNotAlarmedLogSerialNumber_Type(Unsigned32):
    """Custom type tnNotAlarmedLogSerialNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TnNotAlarmedLogSerialNumber_Type.__name__ = "Unsigned32"
_TnNotAlarmedLogSerialNumber_Object = MibTableColumn
tnNotAlarmedLogSerialNumber = _TnNotAlarmedLogSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 11, 1, 1),
    _TnNotAlarmedLogSerialNumber_Type()
)
tnNotAlarmedLogSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnNotAlarmedLogSerialNumber.setStatus("current")
_TnNotAlarmedLogType_Type = ObjectIdentifier
_TnNotAlarmedLogType_Object = MibTableColumn
tnNotAlarmedLogType = _TnNotAlarmedLogType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 11, 1, 2),
    _TnNotAlarmedLogType_Type()
)
tnNotAlarmedLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNotAlarmedLogType.setStatus("current")
_TnNotAlarmedLogTime_Type = Unsigned32
_TnNotAlarmedLogTime_Object = MibTableColumn
tnNotAlarmedLogTime = _TnNotAlarmedLogTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 11, 1, 3),
    _TnNotAlarmedLogTime_Type()
)
tnNotAlarmedLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNotAlarmedLogTime.setStatus("current")
_TnNotAlarmedLogObjectIDType_Type = Unsigned32
_TnNotAlarmedLogObjectIDType_Object = MibTableColumn
tnNotAlarmedLogObjectIDType = _TnNotAlarmedLogObjectIDType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 11, 1, 4),
    _TnNotAlarmedLogObjectIDType_Type()
)
tnNotAlarmedLogObjectIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNotAlarmedLogObjectIDType.setStatus("current")
_TnNotAlarmedLogObjectID_Type = Unsigned32
_TnNotAlarmedLogObjectID_Object = MibTableColumn
tnNotAlarmedLogObjectID = _TnNotAlarmedLogObjectID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 11, 1, 5),
    _TnNotAlarmedLogObjectID_Type()
)
tnNotAlarmedLogObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNotAlarmedLogObjectID.setStatus("current")


class _TnNotAlarmedLogDescr_Type(SnmpAdminString):
    """Custom type tnNotAlarmedLogDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnNotAlarmedLogDescr_Type.__name__ = "SnmpAdminString"
_TnNotAlarmedLogDescr_Object = MibTableColumn
tnNotAlarmedLogDescr = _TnNotAlarmedLogDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 11, 1, 6),
    _TnNotAlarmedLogDescr_Type()
)
tnNotAlarmedLogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNotAlarmedLogDescr.setStatus("current")


class _TnNotAlarmedLogData_Type(SnmpAdminString):
    """Custom type tnNotAlarmedLogData based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnNotAlarmedLogData_Type.__name__ = "SnmpAdminString"
_TnNotAlarmedLogData_Object = MibTableColumn
tnNotAlarmedLogData = _TnNotAlarmedLogData_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 11, 1, 7),
    _TnNotAlarmedLogData_Type()
)
tnNotAlarmedLogData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNotAlarmedLogData.setStatus("current")
_TnNotAlarmedLogServiceAffecting_Type = TruthValue
_TnNotAlarmedLogServiceAffecting_Object = MibTableColumn
tnNotAlarmedLogServiceAffecting = _TnNotAlarmedLogServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 11, 1, 8),
    _TnNotAlarmedLogServiceAffecting_Type()
)
tnNotAlarmedLogServiceAffecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNotAlarmedLogServiceAffecting.setStatus("current")
_TnNotAlarmedLogSlotProgrammedType_Type = ObjectIdentifier
_TnNotAlarmedLogSlotProgrammedType_Object = MibTableColumn
tnNotAlarmedLogSlotProgrammedType = _TnNotAlarmedLogSlotProgrammedType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 11, 1, 9),
    _TnNotAlarmedLogSlotProgrammedType_Type()
)
tnNotAlarmedLogSlotProgrammedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNotAlarmedLogSlotProgrammedType.setStatus("current")
_TnNotAlarmedLogEntityType_Type = TnEntityType
_TnNotAlarmedLogEntityType_Object = MibTableColumn
tnNotAlarmedLogEntityType = _TnNotAlarmedLogEntityType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 11, 1, 10),
    _TnNotAlarmedLogEntityType_Type()
)
tnNotAlarmedLogEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNotAlarmedLogEntityType.setStatus("current")
_TnNotAlarmedLogCondition_Type = TnCondition
_TnNotAlarmedLogCondition_Object = MibTableColumn
tnNotAlarmedLogCondition = _TnNotAlarmedLogCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 11, 1, 11),
    _TnNotAlarmedLogCondition_Type()
)
tnNotAlarmedLogCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNotAlarmedLogCondition.setStatus("current")
_TnSecurityLogBufferTable_Object = MibTable
tnSecurityLogBufferTable = _TnSecurityLogBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 12)
)
if mibBuilder.loadTexts:
    tnSecurityLogBufferTable.setStatus("current")
_TnSecurityLogBufferEntry_Object = MibTableRow
tnSecurityLogBufferEntry = _TnSecurityLogBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 12, 1)
)
tnSecurityLogBufferEntry.setIndexNames(
    (0, "TROPIC-LOG-MIB", "tnSecurityLogSerialNumber"),
)
if mibBuilder.loadTexts:
    tnSecurityLogBufferEntry.setStatus("current")


class _TnSecurityLogSerialNumber_Type(Unsigned32):
    """Custom type tnSecurityLogSerialNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TnSecurityLogSerialNumber_Type.__name__ = "Unsigned32"
_TnSecurityLogSerialNumber_Object = MibTableColumn
tnSecurityLogSerialNumber = _TnSecurityLogSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 12, 1, 1),
    _TnSecurityLogSerialNumber_Type()
)
tnSecurityLogSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSecurityLogSerialNumber.setStatus("current")
_TnSecurityLogType_Type = ObjectIdentifier
_TnSecurityLogType_Object = MibTableColumn
tnSecurityLogType = _TnSecurityLogType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 12, 1, 2),
    _TnSecurityLogType_Type()
)
tnSecurityLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSecurityLogType.setStatus("current")
_TnSecurityLogTime_Type = Unsigned32
_TnSecurityLogTime_Object = MibTableColumn
tnSecurityLogTime = _TnSecurityLogTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 12, 1, 3),
    _TnSecurityLogTime_Type()
)
tnSecurityLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSecurityLogTime.setStatus("current")
_TnSecurityLogObjectIDType_Type = Unsigned32
_TnSecurityLogObjectIDType_Object = MibTableColumn
tnSecurityLogObjectIDType = _TnSecurityLogObjectIDType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 12, 1, 4),
    _TnSecurityLogObjectIDType_Type()
)
tnSecurityLogObjectIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSecurityLogObjectIDType.setStatus("current")
_TnSecurityLogObjectID_Type = Unsigned32
_TnSecurityLogObjectID_Object = MibTableColumn
tnSecurityLogObjectID = _TnSecurityLogObjectID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 12, 1, 5),
    _TnSecurityLogObjectID_Type()
)
tnSecurityLogObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSecurityLogObjectID.setStatus("current")


class _TnSecurityLogDescr_Type(SnmpAdminString):
    """Custom type tnSecurityLogDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSecurityLogDescr_Type.__name__ = "SnmpAdminString"
_TnSecurityLogDescr_Object = MibTableColumn
tnSecurityLogDescr = _TnSecurityLogDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 12, 1, 6),
    _TnSecurityLogDescr_Type()
)
tnSecurityLogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSecurityLogDescr.setStatus("current")


class _TnSecurityLogData_Type(SnmpAdminString):
    """Custom type tnSecurityLogData based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSecurityLogData_Type.__name__ = "SnmpAdminString"
_TnSecurityLogData_Object = MibTableColumn
tnSecurityLogData = _TnSecurityLogData_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 12, 1, 7),
    _TnSecurityLogData_Type()
)
tnSecurityLogData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSecurityLogData.setStatus("current")


class _TnSecurityLogUserID_Type(SnmpAdminString):
    """Custom type tnSecurityLogUserID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_TnSecurityLogUserID_Type.__name__ = "SnmpAdminString"
_TnSecurityLogUserID_Object = MibTableColumn
tnSecurityLogUserID = _TnSecurityLogUserID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 12, 1, 8),
    _TnSecurityLogUserID_Type()
)
tnSecurityLogUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSecurityLogUserID.setStatus("current")
_TnSecurityLogUserSessionNumber_Type = Unsigned32
_TnSecurityLogUserSessionNumber_Object = MibTableColumn
tnSecurityLogUserSessionNumber = _TnSecurityLogUserSessionNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 12, 1, 9),
    _TnSecurityLogUserSessionNumber_Type()
)
tnSecurityLogUserSessionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSecurityLogUserSessionNumber.setStatus("current")


class _TnSecurityLogHeaderType_Type(SnmpAdminString):
    """Custom type tnSecurityLogHeaderType based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_TnSecurityLogHeaderType_Type.__name__ = "SnmpAdminString"
_TnSecurityLogHeaderType_Object = MibTableColumn
tnSecurityLogHeaderType = _TnSecurityLogHeaderType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 12, 1, 10),
    _TnSecurityLogHeaderType_Type()
)
tnSecurityLogHeaderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSecurityLogHeaderType.setStatus("current")


class _TnSecurityLogUserPrivilege_Type(Integer32):
    """Custom type tnSecurityLogUserPrivilege based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("service", 1),
          ("administrator", 2),
          ("provisioner", 3),
          ("observer", 4),
          ("null", 5),
          ("crypto", 6))
    )


_TnSecurityLogUserPrivilege_Type.__name__ = "Integer32"
_TnSecurityLogUserPrivilege_Object = MibTableColumn
tnSecurityLogUserPrivilege = _TnSecurityLogUserPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 12, 1, 11),
    _TnSecurityLogUserPrivilege_Type()
)
tnSecurityLogUserPrivilege.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSecurityLogUserPrivilege.setStatus("current")
_TnSecurityLogUserDestinationAddress_Type = IpAddress
_TnSecurityLogUserDestinationAddress_Object = MibTableColumn
tnSecurityLogUserDestinationAddress = _TnSecurityLogUserDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 12, 1, 12),
    _TnSecurityLogUserDestinationAddress_Type()
)
tnSecurityLogUserDestinationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSecurityLogUserDestinationAddress.setStatus("current")


class _TnSecurityLogResult_Type(Integer32):
    """Custom type tnSecurityLogResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("compld", 1),
          ("prtl", 2),
          ("deny", 3),
          ("other", 4))
    )


_TnSecurityLogResult_Type.__name__ = "Integer32"
_TnSecurityLogResult_Object = MibTableColumn
tnSecurityLogResult = _TnSecurityLogResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 12, 1, 13),
    _TnSecurityLogResult_Type()
)
tnSecurityLogResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSecurityLogResult.setStatus("current")
_TnWarningAlarmLogBufferTable_Object = MibTable
tnWarningAlarmLogBufferTable = _TnWarningAlarmLogBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 13)
)
if mibBuilder.loadTexts:
    tnWarningAlarmLogBufferTable.setStatus("current")
_TnWarningAlarmLogBufferEntry_Object = MibTableRow
tnWarningAlarmLogBufferEntry = _TnWarningAlarmLogBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 13, 1)
)
tnWarningAlarmLogBufferEntry.setIndexNames(
    (0, "TROPIC-LOG-MIB", "tnWarningAlarmLogSerialNumber"),
)
if mibBuilder.loadTexts:
    tnWarningAlarmLogBufferEntry.setStatus("current")


class _TnWarningAlarmLogSerialNumber_Type(Unsigned32):
    """Custom type tnWarningAlarmLogSerialNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TnWarningAlarmLogSerialNumber_Type.__name__ = "Unsigned32"
_TnWarningAlarmLogSerialNumber_Object = MibTableColumn
tnWarningAlarmLogSerialNumber = _TnWarningAlarmLogSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 13, 1, 1),
    _TnWarningAlarmLogSerialNumber_Type()
)
tnWarningAlarmLogSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnWarningAlarmLogSerialNumber.setStatus("current")
_TnWarningAlarmLogType_Type = ObjectIdentifier
_TnWarningAlarmLogType_Object = MibTableColumn
tnWarningAlarmLogType = _TnWarningAlarmLogType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 13, 1, 2),
    _TnWarningAlarmLogType_Type()
)
tnWarningAlarmLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWarningAlarmLogType.setStatus("current")
_TnWarningAlarmLogTime_Type = Unsigned32
_TnWarningAlarmLogTime_Object = MibTableColumn
tnWarningAlarmLogTime = _TnWarningAlarmLogTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 13, 1, 3),
    _TnWarningAlarmLogTime_Type()
)
tnWarningAlarmLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWarningAlarmLogTime.setStatus("current")
_TnWarningAlarmLogObjectIDType_Type = Unsigned32
_TnWarningAlarmLogObjectIDType_Object = MibTableColumn
tnWarningAlarmLogObjectIDType = _TnWarningAlarmLogObjectIDType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 13, 1, 4),
    _TnWarningAlarmLogObjectIDType_Type()
)
tnWarningAlarmLogObjectIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWarningAlarmLogObjectIDType.setStatus("current")
_TnWarningAlarmLogObjectID_Type = Unsigned32
_TnWarningAlarmLogObjectID_Object = MibTableColumn
tnWarningAlarmLogObjectID = _TnWarningAlarmLogObjectID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 13, 1, 5),
    _TnWarningAlarmLogObjectID_Type()
)
tnWarningAlarmLogObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWarningAlarmLogObjectID.setStatus("current")


class _TnWarningAlarmLogDescr_Type(SnmpAdminString):
    """Custom type tnWarningAlarmLogDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnWarningAlarmLogDescr_Type.__name__ = "SnmpAdminString"
_TnWarningAlarmLogDescr_Object = MibTableColumn
tnWarningAlarmLogDescr = _TnWarningAlarmLogDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 13, 1, 6),
    _TnWarningAlarmLogDescr_Type()
)
tnWarningAlarmLogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWarningAlarmLogDescr.setStatus("current")


class _TnWarningAlarmLogData_Type(SnmpAdminString):
    """Custom type tnWarningAlarmLogData based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnWarningAlarmLogData_Type.__name__ = "SnmpAdminString"
_TnWarningAlarmLogData_Object = MibTableColumn
tnWarningAlarmLogData = _TnWarningAlarmLogData_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 13, 1, 7),
    _TnWarningAlarmLogData_Type()
)
tnWarningAlarmLogData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWarningAlarmLogData.setStatus("current")
_TnWarningAlarmLogServiceAffecting_Type = TruthValue
_TnWarningAlarmLogServiceAffecting_Object = MibTableColumn
tnWarningAlarmLogServiceAffecting = _TnWarningAlarmLogServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 13, 1, 8),
    _TnWarningAlarmLogServiceAffecting_Type()
)
tnWarningAlarmLogServiceAffecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWarningAlarmLogServiceAffecting.setStatus("current")
_TnWarningAlarmLogSlotProgrammedType_Type = ObjectIdentifier
_TnWarningAlarmLogSlotProgrammedType_Object = MibTableColumn
tnWarningAlarmLogSlotProgrammedType = _TnWarningAlarmLogSlotProgrammedType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 13, 1, 9),
    _TnWarningAlarmLogSlotProgrammedType_Type()
)
tnWarningAlarmLogSlotProgrammedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWarningAlarmLogSlotProgrammedType.setStatus("current")
_TnWarningAlarmLogEntityType_Type = TnEntityType
_TnWarningAlarmLogEntityType_Object = MibTableColumn
tnWarningAlarmLogEntityType = _TnWarningAlarmLogEntityType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 13, 1, 10),
    _TnWarningAlarmLogEntityType_Type()
)
tnWarningAlarmLogEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWarningAlarmLogEntityType.setStatus("current")
_TnWarningAlarmLogCondition_Type = TnCondition
_TnWarningAlarmLogCondition_Object = MibTableColumn
tnWarningAlarmLogCondition = _TnWarningAlarmLogCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 3, 13, 1, 11),
    _TnWarningAlarmLogCondition_Type()
)
tnWarningAlarmLogCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnWarningAlarmLogCondition.setStatus("current")
_TnLogAlarmCategoryConfig_ObjectIdentity = ObjectIdentity
tnLogAlarmCategoryConfig = _TnLogAlarmCategoryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4)
)
_TnPerObjectAlarmCategoryConfigTable_Object = MibTable
tnPerObjectAlarmCategoryConfigTable = _TnPerObjectAlarmCategoryConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 1)
)
if mibBuilder.loadTexts:
    tnPerObjectAlarmCategoryConfigTable.setStatus("current")
_TnPerObjectAlarmCategoryConfigEntry_Object = MibTableRow
tnPerObjectAlarmCategoryConfigEntry = _TnPerObjectAlarmCategoryConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 1, 1)
)
tnPerObjectAlarmCategoryConfigEntry.setIndexNames(
    (0, "TROPIC-LOG-MIB", "tnAlarmCategoryObjectId"),
    (0, "TROPIC-LOG-MIB", "tnAlarmCategoryEntityType"),
    (0, "TROPIC-LOG-MIB", "tnAlarmCategoryCondition"),
)
if mibBuilder.loadTexts:
    tnPerObjectAlarmCategoryConfigEntry.setStatus("current")
_TnAlarmCategoryObjectId_Type = Unsigned32
_TnAlarmCategoryObjectId_Object = MibTableColumn
tnAlarmCategoryObjectId = _TnAlarmCategoryObjectId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 1, 1, 1),
    _TnAlarmCategoryObjectId_Type()
)
tnAlarmCategoryObjectId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnAlarmCategoryObjectId.setStatus("current")
_TnAlarmCategoryEntityType_Type = TnEntityType
_TnAlarmCategoryEntityType_Object = MibTableColumn
tnAlarmCategoryEntityType = _TnAlarmCategoryEntityType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 1, 1, 2),
    _TnAlarmCategoryEntityType_Type()
)
tnAlarmCategoryEntityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnAlarmCategoryEntityType.setStatus("current")
_TnAlarmCategoryCondition_Type = TnCondition
_TnAlarmCategoryCondition_Object = MibTableColumn
tnAlarmCategoryCondition = _TnAlarmCategoryCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 1, 1, 3),
    _TnAlarmCategoryCondition_Type()
)
tnAlarmCategoryCondition.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnAlarmCategoryCondition.setStatus("current")
_TnPerObjectAlarmCategory_Type = TnTrapCategory
_TnPerObjectAlarmCategory_Object = MibTableColumn
tnPerObjectAlarmCategory = _TnPerObjectAlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 1, 1, 4),
    _TnPerObjectAlarmCategory_Type()
)
tnPerObjectAlarmCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPerObjectAlarmCategory.setStatus("current")
_TnPerObjectAlarmEntityTypeCategory_Type = TnTrapCategory
_TnPerObjectAlarmEntityTypeCategory_Object = MibTableColumn
tnPerObjectAlarmEntityTypeCategory = _TnPerObjectAlarmEntityTypeCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 1, 1, 5),
    _TnPerObjectAlarmEntityTypeCategory_Type()
)
tnPerObjectAlarmEntityTypeCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerObjectAlarmEntityTypeCategory.setStatus("current")
_TnPerObjectAlarmDefaultCategory_Type = TnTrapCategory
_TnPerObjectAlarmDefaultCategory_Object = MibTableColumn
tnPerObjectAlarmDefaultCategory = _TnPerObjectAlarmDefaultCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 1, 1, 6),
    _TnPerObjectAlarmDefaultCategory_Type()
)
tnPerObjectAlarmDefaultCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerObjectAlarmDefaultCategory.setStatus("current")
_TnAlarmProfileConfigTable_Object = MibTable
tnAlarmProfileConfigTable = _TnAlarmProfileConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 2)
)
if mibBuilder.loadTexts:
    tnAlarmProfileConfigTable.setStatus("current")
_TnAlarmProfileConfigEntry_Object = MibTableRow
tnAlarmProfileConfigEntry = _TnAlarmProfileConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 2, 1)
)
tnAlarmProfileConfigEntry.setIndexNames(
    (0, "TROPIC-LOG-MIB", "tnAlarmCategoryEntityType"),
    (0, "TROPIC-LOG-MIB", "tnAlarmCategoryCondition"),
    (0, "TROPIC-LOG-MIB", "tnAlarmCategoryDirection"),
)
if mibBuilder.loadTexts:
    tnAlarmProfileConfigEntry.setStatus("current")
_TnAlarmCategoryDirection_Type = AluWdmAlarmCategoryDirection
_TnAlarmCategoryDirection_Object = MibTableColumn
tnAlarmCategoryDirection = _TnAlarmCategoryDirection_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 2, 1, 1),
    _TnAlarmCategoryDirection_Type()
)
tnAlarmCategoryDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnAlarmCategoryDirection.setStatus("current")
_TnAlarmProfileConfigCategory_Type = TnTrapCategory
_TnAlarmProfileConfigCategory_Object = MibTableColumn
tnAlarmProfileConfigCategory = _TnAlarmProfileConfigCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 2, 1, 2),
    _TnAlarmProfileConfigCategory_Type()
)
tnAlarmProfileConfigCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAlarmProfileConfigCategory.setStatus("current")
_TnAlarmProfileConfigDefaultCategory_Type = TnTrapCategory
_TnAlarmProfileConfigDefaultCategory_Object = MibTableColumn
tnAlarmProfileConfigDefaultCategory = _TnAlarmProfileConfigDefaultCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 2, 1, 3),
    _TnAlarmProfileConfigDefaultCategory_Type()
)
tnAlarmProfileConfigDefaultCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAlarmProfileConfigDefaultCategory.setStatus("current")


class _TnAlarmProfileConfigDescr_Type(SnmpAdminString):
    """Custom type tnAlarmProfileConfigDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnAlarmProfileConfigDescr_Type.__name__ = "SnmpAdminString"
_TnAlarmProfileConfigDescr_Object = MibTableColumn
tnAlarmProfileConfigDescr = _TnAlarmProfileConfigDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 2, 1, 4),
    _TnAlarmProfileConfigDescr_Type()
)
tnAlarmProfileConfigDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAlarmProfileConfigDescr.setStatus("current")
_TnPerSyncObjectAlarmCategoryConfigTable_Object = MibTable
tnPerSyncObjectAlarmCategoryConfigTable = _TnPerSyncObjectAlarmCategoryConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 4)
)
if mibBuilder.loadTexts:
    tnPerSyncObjectAlarmCategoryConfigTable.setStatus("current")
_TnPerSyncObjectAlarmCategoryConfigEntry_Object = MibTableRow
tnPerSyncObjectAlarmCategoryConfigEntry = _TnPerSyncObjectAlarmCategoryConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 4, 1)
)
tnPerSyncObjectAlarmCategoryConfigEntry.setIndexNames(
    (0, "TROPIC-LOG-MIB", "tnSyncAlarmCategoryObjectId"),
    (0, "TROPIC-LOG-MIB", "tnSyncAlarmCategoryEntityType"),
    (0, "TROPIC-LOG-MIB", "tnSyncAlarmCategoryCondition"),
)
if mibBuilder.loadTexts:
    tnPerSyncObjectAlarmCategoryConfigEntry.setStatus("current")
_TnSyncAlarmCategoryObjectId_Type = Unsigned32
_TnSyncAlarmCategoryObjectId_Object = MibTableColumn
tnSyncAlarmCategoryObjectId = _TnSyncAlarmCategoryObjectId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 4, 1, 1),
    _TnSyncAlarmCategoryObjectId_Type()
)
tnSyncAlarmCategoryObjectId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSyncAlarmCategoryObjectId.setStatus("current")
_TnSyncAlarmCategoryEntityType_Type = TnEntityType
_TnSyncAlarmCategoryEntityType_Object = MibTableColumn
tnSyncAlarmCategoryEntityType = _TnSyncAlarmCategoryEntityType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 4, 1, 2),
    _TnSyncAlarmCategoryEntityType_Type()
)
tnSyncAlarmCategoryEntityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSyncAlarmCategoryEntityType.setStatus("current")
_TnSyncAlarmCategoryCondition_Type = TnCondition
_TnSyncAlarmCategoryCondition_Object = MibTableColumn
tnSyncAlarmCategoryCondition = _TnSyncAlarmCategoryCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 4, 1, 3),
    _TnSyncAlarmCategoryCondition_Type()
)
tnSyncAlarmCategoryCondition.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSyncAlarmCategoryCondition.setStatus("current")
_TnPerSyncObjectAlarmCategory_Type = TnTrapCategory
_TnPerSyncObjectAlarmCategory_Object = MibTableColumn
tnPerSyncObjectAlarmCategory = _TnPerSyncObjectAlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 4, 1, 4),
    _TnPerSyncObjectAlarmCategory_Type()
)
tnPerSyncObjectAlarmCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPerSyncObjectAlarmCategory.setStatus("current")
_TnPerSyncObjectAlarmEntityTypeCategory_Type = TnTrapCategory
_TnPerSyncObjectAlarmEntityTypeCategory_Object = MibTableColumn
tnPerSyncObjectAlarmEntityTypeCategory = _TnPerSyncObjectAlarmEntityTypeCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 4, 1, 5),
    _TnPerSyncObjectAlarmEntityTypeCategory_Type()
)
tnPerSyncObjectAlarmEntityTypeCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerSyncObjectAlarmEntityTypeCategory.setStatus("current")
_TnPerSyncObjectAlarmDefaultCategory_Type = TnTrapCategory
_TnPerSyncObjectAlarmDefaultCategory_Object = MibTableColumn
tnPerSyncObjectAlarmDefaultCategory = _TnPerSyncObjectAlarmDefaultCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 4, 1, 6),
    _TnPerSyncObjectAlarmDefaultCategory_Type()
)
tnPerSyncObjectAlarmDefaultCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerSyncObjectAlarmDefaultCategory.setStatus("current")
_TnPerVtsObjectAlarmCategoryConfigAttributeTotal_Type = Integer32
_TnPerVtsObjectAlarmCategoryConfigAttributeTotal_Object = MibScalar
tnPerVtsObjectAlarmCategoryConfigAttributeTotal = _TnPerVtsObjectAlarmCategoryConfigAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 5),
    _TnPerVtsObjectAlarmCategoryConfigAttributeTotal_Type()
)
tnPerVtsObjectAlarmCategoryConfigAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerVtsObjectAlarmCategoryConfigAttributeTotal.setStatus("current")
_TnPerVtsObjectAlarmCategoryConfigTable_Object = MibTable
tnPerVtsObjectAlarmCategoryConfigTable = _TnPerVtsObjectAlarmCategoryConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 6)
)
if mibBuilder.loadTexts:
    tnPerVtsObjectAlarmCategoryConfigTable.setStatus("current")
_TnPerVtsObjectAlarmCategoryConfigEntry_Object = MibTableRow
tnPerVtsObjectAlarmCategoryConfigEntry = _TnPerVtsObjectAlarmCategoryConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 6, 1)
)
tnPerVtsObjectAlarmCategoryConfigEntry.setIndexNames(
    (0, "TROPIC-LOG-MIB", "tnVtsAlarmCategoryObjectId"),
    (0, "TROPIC-LOG-MIB", "tnVtsAlarmCategoryDirection"),
    (0, "TROPIC-LOG-MIB", "tnVtsAlarmCategoryEntityType"),
    (0, "TROPIC-LOG-MIB", "tnVtsAlarmCategoryCondition"),
)
if mibBuilder.loadTexts:
    tnPerVtsObjectAlarmCategoryConfigEntry.setStatus("current")
_TnVtsAlarmCategoryObjectId_Type = Unsigned32
_TnVtsAlarmCategoryObjectId_Object = MibTableColumn
tnVtsAlarmCategoryObjectId = _TnVtsAlarmCategoryObjectId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 6, 1, 1),
    _TnVtsAlarmCategoryObjectId_Type()
)
tnVtsAlarmCategoryObjectId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVtsAlarmCategoryObjectId.setStatus("current")
_TnVtsAlarmCategoryDirection_Type = AluWdmAlarmCategoryDirection
_TnVtsAlarmCategoryDirection_Object = MibTableColumn
tnVtsAlarmCategoryDirection = _TnVtsAlarmCategoryDirection_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 6, 1, 2),
    _TnVtsAlarmCategoryDirection_Type()
)
tnVtsAlarmCategoryDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVtsAlarmCategoryDirection.setStatus("current")
_TnVtsAlarmCategoryEntityType_Type = TnEntityType
_TnVtsAlarmCategoryEntityType_Object = MibTableColumn
tnVtsAlarmCategoryEntityType = _TnVtsAlarmCategoryEntityType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 6, 1, 3),
    _TnVtsAlarmCategoryEntityType_Type()
)
tnVtsAlarmCategoryEntityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVtsAlarmCategoryEntityType.setStatus("current")
_TnVtsAlarmCategoryCondition_Type = TnCondition
_TnVtsAlarmCategoryCondition_Object = MibTableColumn
tnVtsAlarmCategoryCondition = _TnVtsAlarmCategoryCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 6, 1, 4),
    _TnVtsAlarmCategoryCondition_Type()
)
tnVtsAlarmCategoryCondition.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVtsAlarmCategoryCondition.setStatus("current")
_TnPerVtsObjectAlarmCategory_Type = TnTrapCategory
_TnPerVtsObjectAlarmCategory_Object = MibTableColumn
tnPerVtsObjectAlarmCategory = _TnPerVtsObjectAlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 6, 1, 5),
    _TnPerVtsObjectAlarmCategory_Type()
)
tnPerVtsObjectAlarmCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPerVtsObjectAlarmCategory.setStatus("current")
_TnPerVtsObjectAlarmEntityTypeCategory_Type = TnTrapCategory
_TnPerVtsObjectAlarmEntityTypeCategory_Object = MibTableColumn
tnPerVtsObjectAlarmEntityTypeCategory = _TnPerVtsObjectAlarmEntityTypeCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 6, 1, 6),
    _TnPerVtsObjectAlarmEntityTypeCategory_Type()
)
tnPerVtsObjectAlarmEntityTypeCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerVtsObjectAlarmEntityTypeCategory.setStatus("current")
_TnPerVtsObjectAlarmDefaultCategory_Type = TnTrapCategory
_TnPerVtsObjectAlarmDefaultCategory_Object = MibTableColumn
tnPerVtsObjectAlarmDefaultCategory = _TnPerVtsObjectAlarmDefaultCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 6, 1, 7),
    _TnPerVtsObjectAlarmDefaultCategory_Type()
)
tnPerVtsObjectAlarmDefaultCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerVtsObjectAlarmDefaultCategory.setStatus("current")
_TnPerCcmObjectAlarmCategoryConfigAttributeTotal_Type = Integer32
_TnPerCcmObjectAlarmCategoryConfigAttributeTotal_Object = MibScalar
tnPerCcmObjectAlarmCategoryConfigAttributeTotal = _TnPerCcmObjectAlarmCategoryConfigAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 7),
    _TnPerCcmObjectAlarmCategoryConfigAttributeTotal_Type()
)
tnPerCcmObjectAlarmCategoryConfigAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerCcmObjectAlarmCategoryConfigAttributeTotal.setStatus("current")
_TnPerCcmObjectAlarmCategoryConfigTable_Object = MibTable
tnPerCcmObjectAlarmCategoryConfigTable = _TnPerCcmObjectAlarmCategoryConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 8)
)
if mibBuilder.loadTexts:
    tnPerCcmObjectAlarmCategoryConfigTable.setStatus("current")
_TnPerCcmObjectAlarmCategoryConfigEntry_Object = MibTableRow
tnPerCcmObjectAlarmCategoryConfigEntry = _TnPerCcmObjectAlarmCategoryConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 8, 1)
)
tnPerCcmObjectAlarmCategoryConfigEntry.setIndexNames(
    (0, "TROPIC-LOG-MIB", "tnCcmAlarmCategoryObjectId"),
    (0, "TROPIC-LOG-MIB", "tnCcmAlarmCategoryTribObjectId"),
    (0, "TROPIC-LOG-MIB", "tnCcmAlarmCategoryEntityType"),
    (0, "TROPIC-LOG-MIB", "tnCcmAlarmCategoryCondition"),
)
if mibBuilder.loadTexts:
    tnPerCcmObjectAlarmCategoryConfigEntry.setStatus("current")
_TnCcmAlarmCategoryObjectId_Type = Unsigned32
_TnCcmAlarmCategoryObjectId_Object = MibTableColumn
tnCcmAlarmCategoryObjectId = _TnCcmAlarmCategoryObjectId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 8, 1, 1),
    _TnCcmAlarmCategoryObjectId_Type()
)
tnCcmAlarmCategoryObjectId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCcmAlarmCategoryObjectId.setStatus("current")
_TnCcmAlarmCategoryTribObjectId_Type = Unsigned32
_TnCcmAlarmCategoryTribObjectId_Object = MibTableColumn
tnCcmAlarmCategoryTribObjectId = _TnCcmAlarmCategoryTribObjectId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 8, 1, 2),
    _TnCcmAlarmCategoryTribObjectId_Type()
)
tnCcmAlarmCategoryTribObjectId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCcmAlarmCategoryTribObjectId.setStatus("current")
_TnCcmAlarmCategoryEntityType_Type = TnEntityType
_TnCcmAlarmCategoryEntityType_Object = MibTableColumn
tnCcmAlarmCategoryEntityType = _TnCcmAlarmCategoryEntityType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 8, 1, 3),
    _TnCcmAlarmCategoryEntityType_Type()
)
tnCcmAlarmCategoryEntityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCcmAlarmCategoryEntityType.setStatus("current")
_TnCcmAlarmCategoryCondition_Type = TnCondition
_TnCcmAlarmCategoryCondition_Object = MibTableColumn
tnCcmAlarmCategoryCondition = _TnCcmAlarmCategoryCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 8, 1, 4),
    _TnCcmAlarmCategoryCondition_Type()
)
tnCcmAlarmCategoryCondition.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnCcmAlarmCategoryCondition.setStatus("current")
_TnPerCcmObjectAlarmCategory_Type = TnTrapCategory
_TnPerCcmObjectAlarmCategory_Object = MibTableColumn
tnPerCcmObjectAlarmCategory = _TnPerCcmObjectAlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 8, 1, 5),
    _TnPerCcmObjectAlarmCategory_Type()
)
tnPerCcmObjectAlarmCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPerCcmObjectAlarmCategory.setStatus("current")
_TnPerCcmObjectAlarmEntityTypeCategory_Type = TnTrapCategory
_TnPerCcmObjectAlarmEntityTypeCategory_Object = MibTableColumn
tnPerCcmObjectAlarmEntityTypeCategory = _TnPerCcmObjectAlarmEntityTypeCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 8, 1, 6),
    _TnPerCcmObjectAlarmEntityTypeCategory_Type()
)
tnPerCcmObjectAlarmEntityTypeCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerCcmObjectAlarmEntityTypeCategory.setStatus("current")
_TnPerCcmObjectAlarmDefaultCategory_Type = TnTrapCategory
_TnPerCcmObjectAlarmDefaultCategory_Object = MibTableColumn
tnPerCcmObjectAlarmDefaultCategory = _TnPerCcmObjectAlarmDefaultCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 8, 1, 7),
    _TnPerCcmObjectAlarmDefaultCategory_Type()
)
tnPerCcmObjectAlarmDefaultCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerCcmObjectAlarmDefaultCategory.setStatus("current")
_TnPerTcmObjectAlarmCategoryConfigAttributeTotal_Type = Integer32
_TnPerTcmObjectAlarmCategoryConfigAttributeTotal_Object = MibScalar
tnPerTcmObjectAlarmCategoryConfigAttributeTotal = _TnPerTcmObjectAlarmCategoryConfigAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 9),
    _TnPerTcmObjectAlarmCategoryConfigAttributeTotal_Type()
)
tnPerTcmObjectAlarmCategoryConfigAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerTcmObjectAlarmCategoryConfigAttributeTotal.setStatus("current")
_TnPerTcmObjectAlarmCategoryConfigTable_Object = MibTable
tnPerTcmObjectAlarmCategoryConfigTable = _TnPerTcmObjectAlarmCategoryConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 10)
)
if mibBuilder.loadTexts:
    tnPerTcmObjectAlarmCategoryConfigTable.setStatus("current")
_TnPerTcmObjectAlarmCategoryConfigEntry_Object = MibTableRow
tnPerTcmObjectAlarmCategoryConfigEntry = _TnPerTcmObjectAlarmCategoryConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 10, 1)
)
tnPerTcmObjectAlarmCategoryConfigEntry.setIndexNames(
    (0, "TROPIC-LOG-MIB", "tnTcmAlarmCategoryObjectId"),
    (0, "TROPIC-LOG-MIB", "tnTcmAlarmCategoryTribObjectId"),
    (0, "TROPIC-LOG-MIB", "tnTcmAlarmCategoryEntityType"),
    (0, "TROPIC-LOG-MIB", "tnTcmAlarmCategoryCondition"),
)
if mibBuilder.loadTexts:
    tnPerTcmObjectAlarmCategoryConfigEntry.setStatus("current")
_TnTcmAlarmCategoryObjectId_Type = Unsigned32
_TnTcmAlarmCategoryObjectId_Object = MibTableColumn
tnTcmAlarmCategoryObjectId = _TnTcmAlarmCategoryObjectId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 10, 1, 1),
    _TnTcmAlarmCategoryObjectId_Type()
)
tnTcmAlarmCategoryObjectId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnTcmAlarmCategoryObjectId.setStatus("current")
_TnTcmAlarmCategoryTribObjectId_Type = Unsigned32
_TnTcmAlarmCategoryTribObjectId_Object = MibTableColumn
tnTcmAlarmCategoryTribObjectId = _TnTcmAlarmCategoryTribObjectId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 10, 1, 2),
    _TnTcmAlarmCategoryTribObjectId_Type()
)
tnTcmAlarmCategoryTribObjectId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnTcmAlarmCategoryTribObjectId.setStatus("current")
_TnTcmAlarmCategoryEntityType_Type = TnEntityType
_TnTcmAlarmCategoryEntityType_Object = MibTableColumn
tnTcmAlarmCategoryEntityType = _TnTcmAlarmCategoryEntityType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 10, 1, 3),
    _TnTcmAlarmCategoryEntityType_Type()
)
tnTcmAlarmCategoryEntityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnTcmAlarmCategoryEntityType.setStatus("current")
_TnTcmAlarmCategoryCondition_Type = TnCondition
_TnTcmAlarmCategoryCondition_Object = MibTableColumn
tnTcmAlarmCategoryCondition = _TnTcmAlarmCategoryCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 10, 1, 4),
    _TnTcmAlarmCategoryCondition_Type()
)
tnTcmAlarmCategoryCondition.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnTcmAlarmCategoryCondition.setStatus("current")
_TnPerTcmObjectAlarmCategory_Type = TnTrapCategory
_TnPerTcmObjectAlarmCategory_Object = MibTableColumn
tnPerTcmObjectAlarmCategory = _TnPerTcmObjectAlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 10, 1, 5),
    _TnPerTcmObjectAlarmCategory_Type()
)
tnPerTcmObjectAlarmCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPerTcmObjectAlarmCategory.setStatus("current")
_TnPerTcmObjectAlarmEntityTypeCategory_Type = TnTrapCategory
_TnPerTcmObjectAlarmEntityTypeCategory_Object = MibTableColumn
tnPerTcmObjectAlarmEntityTypeCategory = _TnPerTcmObjectAlarmEntityTypeCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 10, 1, 6),
    _TnPerTcmObjectAlarmEntityTypeCategory_Type()
)
tnPerTcmObjectAlarmEntityTypeCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerTcmObjectAlarmEntityTypeCategory.setStatus("current")
_TnPerTcmObjectAlarmDefaultCategory_Type = TnTrapCategory
_TnPerTcmObjectAlarmDefaultCategory_Object = MibTableColumn
tnPerTcmObjectAlarmDefaultCategory = _TnPerTcmObjectAlarmDefaultCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 10, 1, 7),
    _TnPerTcmObjectAlarmDefaultCategory_Type()
)
tnPerTcmObjectAlarmDefaultCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerTcmObjectAlarmDefaultCategory.setStatus("current")
_TnPerPtpObjectAlarmCategoryConfigAttributeTotal_Type = Integer32
_TnPerPtpObjectAlarmCategoryConfigAttributeTotal_Object = MibScalar
tnPerPtpObjectAlarmCategoryConfigAttributeTotal = _TnPerPtpObjectAlarmCategoryConfigAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 11),
    _TnPerPtpObjectAlarmCategoryConfigAttributeTotal_Type()
)
tnPerPtpObjectAlarmCategoryConfigAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerPtpObjectAlarmCategoryConfigAttributeTotal.setStatus("current")
_TnPerPtpObjectAlarmCategoryConfigTable_Object = MibTable
tnPerPtpObjectAlarmCategoryConfigTable = _TnPerPtpObjectAlarmCategoryConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 12)
)
if mibBuilder.loadTexts:
    tnPerPtpObjectAlarmCategoryConfigTable.setStatus("current")
_TnPerPtpObjectAlarmCategoryConfigEntry_Object = MibTableRow
tnPerPtpObjectAlarmCategoryConfigEntry = _TnPerPtpObjectAlarmCategoryConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 12, 1)
)
tnPerPtpObjectAlarmCategoryConfigEntry.setIndexNames(
    (0, "TROPIC-LOG-MIB", "tnPtpAlarmCategoryObjectId"),
    (0, "TROPIC-LOG-MIB", "tnPtpAlarmCategoryDirection"),
    (0, "TROPIC-LOG-MIB", "tnPtpAlarmCategoryEntityType"),
    (0, "TROPIC-LOG-MIB", "tnPtpAlarmCategoryCondition"),
)
if mibBuilder.loadTexts:
    tnPerPtpObjectAlarmCategoryConfigEntry.setStatus("current")
_TnPtpAlarmCategoryObjectId_Type = Unsigned32
_TnPtpAlarmCategoryObjectId_Object = MibTableColumn
tnPtpAlarmCategoryObjectId = _TnPtpAlarmCategoryObjectId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 12, 1, 1),
    _TnPtpAlarmCategoryObjectId_Type()
)
tnPtpAlarmCategoryObjectId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPtpAlarmCategoryObjectId.setStatus("current")
_TnPtpAlarmCategoryDirection_Type = AluWdmAlarmCategoryDirection
_TnPtpAlarmCategoryDirection_Object = MibTableColumn
tnPtpAlarmCategoryDirection = _TnPtpAlarmCategoryDirection_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 12, 1, 2),
    _TnPtpAlarmCategoryDirection_Type()
)
tnPtpAlarmCategoryDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPtpAlarmCategoryDirection.setStatus("current")
_TnPtpAlarmCategoryEntityType_Type = TnEntityType
_TnPtpAlarmCategoryEntityType_Object = MibTableColumn
tnPtpAlarmCategoryEntityType = _TnPtpAlarmCategoryEntityType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 12, 1, 3),
    _TnPtpAlarmCategoryEntityType_Type()
)
tnPtpAlarmCategoryEntityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPtpAlarmCategoryEntityType.setStatus("current")
_TnPtpAlarmCategoryCondition_Type = TnCondition
_TnPtpAlarmCategoryCondition_Object = MibTableColumn
tnPtpAlarmCategoryCondition = _TnPtpAlarmCategoryCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 12, 1, 4),
    _TnPtpAlarmCategoryCondition_Type()
)
tnPtpAlarmCategoryCondition.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPtpAlarmCategoryCondition.setStatus("current")
_TnPerPtpObjectAlarmCategory_Type = TnTrapCategory
_TnPerPtpObjectAlarmCategory_Object = MibTableColumn
tnPerPtpObjectAlarmCategory = _TnPerPtpObjectAlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 12, 1, 5),
    _TnPerPtpObjectAlarmCategory_Type()
)
tnPerPtpObjectAlarmCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPerPtpObjectAlarmCategory.setStatus("current")
_TnPerPtpObjectAlarmEntityTypeCategory_Type = TnTrapCategory
_TnPerPtpObjectAlarmEntityTypeCategory_Object = MibTableColumn
tnPerPtpObjectAlarmEntityTypeCategory = _TnPerPtpObjectAlarmEntityTypeCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 12, 1, 6),
    _TnPerPtpObjectAlarmEntityTypeCategory_Type()
)
tnPerPtpObjectAlarmEntityTypeCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerPtpObjectAlarmEntityTypeCategory.setStatus("current")
_TnPerPtpObjectAlarmDefaultCategory_Type = TnTrapCategory
_TnPerPtpObjectAlarmDefaultCategory_Object = MibTableColumn
tnPerPtpObjectAlarmDefaultCategory = _TnPerPtpObjectAlarmDefaultCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 12, 1, 7),
    _TnPerPtpObjectAlarmDefaultCategory_Type()
)
tnPerPtpObjectAlarmDefaultCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerPtpObjectAlarmDefaultCategory.setStatus("current")
_TnPerLagObjectAlarmCategoryConfigAttributeTotal_Type = Integer32
_TnPerLagObjectAlarmCategoryConfigAttributeTotal_Object = MibScalar
tnPerLagObjectAlarmCategoryConfigAttributeTotal = _TnPerLagObjectAlarmCategoryConfigAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 13),
    _TnPerLagObjectAlarmCategoryConfigAttributeTotal_Type()
)
tnPerLagObjectAlarmCategoryConfigAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerLagObjectAlarmCategoryConfigAttributeTotal.setStatus("current")
_TnPerLagObjectAlarmCategoryConfigTable_Object = MibTable
tnPerLagObjectAlarmCategoryConfigTable = _TnPerLagObjectAlarmCategoryConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 14)
)
if mibBuilder.loadTexts:
    tnPerLagObjectAlarmCategoryConfigTable.setStatus("current")
_TnPerLagObjectAlarmCategoryConfigEntry_Object = MibTableRow
tnPerLagObjectAlarmCategoryConfigEntry = _TnPerLagObjectAlarmCategoryConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 14, 1)
)
tnPerLagObjectAlarmCategoryConfigEntry.setIndexNames(
    (0, "TROPIC-LOG-MIB", "tnLagAlarmCategoryObjectId"),
    (0, "TROPIC-LOG-MIB", "tnLagAlarmCategoryDirection"),
    (0, "TROPIC-LOG-MIB", "tnLagAlarmCategoryEntityType"),
    (0, "TROPIC-LOG-MIB", "tnLagAlarmCategoryCondition"),
)
if mibBuilder.loadTexts:
    tnPerLagObjectAlarmCategoryConfigEntry.setStatus("current")
_TnLagAlarmCategoryObjectId_Type = Unsigned32
_TnLagAlarmCategoryObjectId_Object = MibTableColumn
tnLagAlarmCategoryObjectId = _TnLagAlarmCategoryObjectId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 14, 1, 1),
    _TnLagAlarmCategoryObjectId_Type()
)
tnLagAlarmCategoryObjectId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLagAlarmCategoryObjectId.setStatus("current")
_TnLagAlarmCategoryDirection_Type = AluWdmAlarmCategoryDirection
_TnLagAlarmCategoryDirection_Object = MibTableColumn
tnLagAlarmCategoryDirection = _TnLagAlarmCategoryDirection_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 14, 1, 2),
    _TnLagAlarmCategoryDirection_Type()
)
tnLagAlarmCategoryDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLagAlarmCategoryDirection.setStatus("current")
_TnLagAlarmCategoryEntityType_Type = TnEntityType
_TnLagAlarmCategoryEntityType_Object = MibTableColumn
tnLagAlarmCategoryEntityType = _TnLagAlarmCategoryEntityType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 14, 1, 3),
    _TnLagAlarmCategoryEntityType_Type()
)
tnLagAlarmCategoryEntityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLagAlarmCategoryEntityType.setStatus("current")
_TnLagAlarmCategoryCondition_Type = TnCondition
_TnLagAlarmCategoryCondition_Object = MibTableColumn
tnLagAlarmCategoryCondition = _TnLagAlarmCategoryCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 14, 1, 4),
    _TnLagAlarmCategoryCondition_Type()
)
tnLagAlarmCategoryCondition.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLagAlarmCategoryCondition.setStatus("current")
_TnPerLagObjectAlarmCategory_Type = TnTrapCategory
_TnPerLagObjectAlarmCategory_Object = MibTableColumn
tnPerLagObjectAlarmCategory = _TnPerLagObjectAlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 14, 1, 5),
    _TnPerLagObjectAlarmCategory_Type()
)
tnPerLagObjectAlarmCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPerLagObjectAlarmCategory.setStatus("current")
_TnPerLagObjectAlarmEntityTypeCategory_Type = TnTrapCategory
_TnPerLagObjectAlarmEntityTypeCategory_Object = MibTableColumn
tnPerLagObjectAlarmEntityTypeCategory = _TnPerLagObjectAlarmEntityTypeCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 14, 1, 6),
    _TnPerLagObjectAlarmEntityTypeCategory_Type()
)
tnPerLagObjectAlarmEntityTypeCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerLagObjectAlarmEntityTypeCategory.setStatus("current")
_TnPerLagObjectAlarmDefaultCategory_Type = TnTrapCategory
_TnPerLagObjectAlarmDefaultCategory_Object = MibTableColumn
tnPerLagObjectAlarmDefaultCategory = _TnPerLagObjectAlarmDefaultCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 14, 1, 7),
    _TnPerLagObjectAlarmDefaultCategory_Type()
)
tnPerLagObjectAlarmDefaultCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerLagObjectAlarmDefaultCategory.setStatus("current")
_TnPerOtnObjectAlarmCategoryConfigAttributeTotal_Type = Integer32
_TnPerOtnObjectAlarmCategoryConfigAttributeTotal_Object = MibScalar
tnPerOtnObjectAlarmCategoryConfigAttributeTotal = _TnPerOtnObjectAlarmCategoryConfigAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 15),
    _TnPerOtnObjectAlarmCategoryConfigAttributeTotal_Type()
)
tnPerOtnObjectAlarmCategoryConfigAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerOtnObjectAlarmCategoryConfigAttributeTotal.setStatus("deprecated")
_TnPerOtnObjectAlarmCategoryConfigTable_Object = MibTable
tnPerOtnObjectAlarmCategoryConfigTable = _TnPerOtnObjectAlarmCategoryConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 16)
)
if mibBuilder.loadTexts:
    tnPerOtnObjectAlarmCategoryConfigTable.setStatus("deprecated")
_TnPerOtnObjectAlarmCategoryConfigEntry_Object = MibTableRow
tnPerOtnObjectAlarmCategoryConfigEntry = _TnPerOtnObjectAlarmCategoryConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 16, 1)
)
tnPerOtnObjectAlarmCategoryConfigEntry.setIndexNames(
    (0, "TROPIC-LOG-MIB", "tnOtnAlarmCategoryObjectId"),
    (0, "TROPIC-LOG-MIB", "tnOtnAlarmCategoryTribObjectId"),
    (0, "TROPIC-LOG-MIB", "tnOtnAlarmCategoryEntityType"),
    (0, "TROPIC-LOG-MIB", "tnOtnAlarmCategoryCondition"),
)
if mibBuilder.loadTexts:
    tnPerOtnObjectAlarmCategoryConfigEntry.setStatus("deprecated")
_TnOtnAlarmCategoryObjectId_Type = Unsigned32
_TnOtnAlarmCategoryObjectId_Object = MibTableColumn
tnOtnAlarmCategoryObjectId = _TnOtnAlarmCategoryObjectId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 16, 1, 1),
    _TnOtnAlarmCategoryObjectId_Type()
)
tnOtnAlarmCategoryObjectId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOtnAlarmCategoryObjectId.setStatus("deprecated")
_TnOtnAlarmCategoryTribObjectId_Type = Unsigned32
_TnOtnAlarmCategoryTribObjectId_Object = MibTableColumn
tnOtnAlarmCategoryTribObjectId = _TnOtnAlarmCategoryTribObjectId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 16, 1, 2),
    _TnOtnAlarmCategoryTribObjectId_Type()
)
tnOtnAlarmCategoryTribObjectId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOtnAlarmCategoryTribObjectId.setStatus("deprecated")
_TnOtnAlarmCategoryEntityType_Type = TnEntityType
_TnOtnAlarmCategoryEntityType_Object = MibTableColumn
tnOtnAlarmCategoryEntityType = _TnOtnAlarmCategoryEntityType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 16, 1, 3),
    _TnOtnAlarmCategoryEntityType_Type()
)
tnOtnAlarmCategoryEntityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOtnAlarmCategoryEntityType.setStatus("deprecated")
_TnOtnAlarmCategoryCondition_Type = TnCondition
_TnOtnAlarmCategoryCondition_Object = MibTableColumn
tnOtnAlarmCategoryCondition = _TnOtnAlarmCategoryCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 16, 1, 4),
    _TnOtnAlarmCategoryCondition_Type()
)
tnOtnAlarmCategoryCondition.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOtnAlarmCategoryCondition.setStatus("deprecated")
_TnPerOtnObjectAlarmCategory_Type = TnTrapCategory
_TnPerOtnObjectAlarmCategory_Object = MibTableColumn
tnPerOtnObjectAlarmCategory = _TnPerOtnObjectAlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 16, 1, 5),
    _TnPerOtnObjectAlarmCategory_Type()
)
tnPerOtnObjectAlarmCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPerOtnObjectAlarmCategory.setStatus("deprecated")
_TnPerOtnObjectAlarmEntityTypeCategory_Type = TnTrapCategory
_TnPerOtnObjectAlarmEntityTypeCategory_Object = MibTableColumn
tnPerOtnObjectAlarmEntityTypeCategory = _TnPerOtnObjectAlarmEntityTypeCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 16, 1, 6),
    _TnPerOtnObjectAlarmEntityTypeCategory_Type()
)
tnPerOtnObjectAlarmEntityTypeCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerOtnObjectAlarmEntityTypeCategory.setStatus("deprecated")
_TnPerOtnObjectAlarmDefaultCategory_Type = TnTrapCategory
_TnPerOtnObjectAlarmDefaultCategory_Object = MibTableColumn
tnPerOtnObjectAlarmDefaultCategory = _TnPerOtnObjectAlarmDefaultCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 16, 1, 7),
    _TnPerOtnObjectAlarmDefaultCategory_Type()
)
tnPerOtnObjectAlarmDefaultCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerOtnObjectAlarmDefaultCategory.setStatus("deprecated")
_TnPerSrSvcObjectAlarmCategoryConfigAttributeTotal_Type = Integer32
_TnPerSrSvcObjectAlarmCategoryConfigAttributeTotal_Object = MibScalar
tnPerSrSvcObjectAlarmCategoryConfigAttributeTotal = _TnPerSrSvcObjectAlarmCategoryConfigAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 17),
    _TnPerSrSvcObjectAlarmCategoryConfigAttributeTotal_Type()
)
tnPerSrSvcObjectAlarmCategoryConfigAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerSrSvcObjectAlarmCategoryConfigAttributeTotal.setStatus("current")
_TnPerSrSvcObjectAlarmCategoryConfigTable_Object = MibTable
tnPerSrSvcObjectAlarmCategoryConfigTable = _TnPerSrSvcObjectAlarmCategoryConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 18)
)
if mibBuilder.loadTexts:
    tnPerSrSvcObjectAlarmCategoryConfigTable.setStatus("current")
_TnPerSrSvcObjectAlarmCategoryConfigEntry_Object = MibTableRow
tnPerSrSvcObjectAlarmCategoryConfigEntry = _TnPerSrSvcObjectAlarmCategoryConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 18, 1)
)
tnPerSrSvcObjectAlarmCategoryConfigEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (0, "TROPIC-LOG-MIB", "tnSrSvcAlarmCategoryEntityType"),
    (0, "TROPIC-LOG-MIB", "tnSrSvcAlarmCategoryCondition"),
)
if mibBuilder.loadTexts:
    tnPerSrSvcObjectAlarmCategoryConfigEntry.setStatus("current")
_TnSrSvcAlarmCategoryEntityType_Type = TnEntityType
_TnSrSvcAlarmCategoryEntityType_Object = MibTableColumn
tnSrSvcAlarmCategoryEntityType = _TnSrSvcAlarmCategoryEntityType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 18, 1, 1),
    _TnSrSvcAlarmCategoryEntityType_Type()
)
tnSrSvcAlarmCategoryEntityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSrSvcAlarmCategoryEntityType.setStatus("current")
_TnSrSvcAlarmCategoryCondition_Type = TnCondition
_TnSrSvcAlarmCategoryCondition_Object = MibTableColumn
tnSrSvcAlarmCategoryCondition = _TnSrSvcAlarmCategoryCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 18, 1, 2),
    _TnSrSvcAlarmCategoryCondition_Type()
)
tnSrSvcAlarmCategoryCondition.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSrSvcAlarmCategoryCondition.setStatus("current")
_TnPerSrSvcObjectAlarmCategory_Type = TnTrapCategory
_TnPerSrSvcObjectAlarmCategory_Object = MibTableColumn
tnPerSrSvcObjectAlarmCategory = _TnPerSrSvcObjectAlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 18, 1, 3),
    _TnPerSrSvcObjectAlarmCategory_Type()
)
tnPerSrSvcObjectAlarmCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPerSrSvcObjectAlarmCategory.setStatus("current")
_TnPerSrSvcObjectAlarmEntityTypeCategory_Type = TnTrapCategory
_TnPerSrSvcObjectAlarmEntityTypeCategory_Object = MibTableColumn
tnPerSrSvcObjectAlarmEntityTypeCategory = _TnPerSrSvcObjectAlarmEntityTypeCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 18, 1, 4),
    _TnPerSrSvcObjectAlarmEntityTypeCategory_Type()
)
tnPerSrSvcObjectAlarmEntityTypeCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerSrSvcObjectAlarmEntityTypeCategory.setStatus("current")
_TnPerSrSvcObjectAlarmDefaultCategory_Type = TnTrapCategory
_TnPerSrSvcObjectAlarmDefaultCategory_Object = MibTableColumn
tnPerSrSvcObjectAlarmDefaultCategory = _TnPerSrSvcObjectAlarmDefaultCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 18, 1, 5),
    _TnPerSrSvcObjectAlarmDefaultCategory_Type()
)
tnPerSrSvcObjectAlarmDefaultCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerSrSvcObjectAlarmDefaultCategory.setStatus("current")
_TnPerSrSapObjectAlarmCategoryConfigAttributeTotal_Type = Integer32
_TnPerSrSapObjectAlarmCategoryConfigAttributeTotal_Object = MibScalar
tnPerSrSapObjectAlarmCategoryConfigAttributeTotal = _TnPerSrSapObjectAlarmCategoryConfigAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 19),
    _TnPerSrSapObjectAlarmCategoryConfigAttributeTotal_Type()
)
tnPerSrSapObjectAlarmCategoryConfigAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerSrSapObjectAlarmCategoryConfigAttributeTotal.setStatus("current")
_TnPerSrSapObjectAlarmCategoryConfigTable_Object = MibTable
tnPerSrSapObjectAlarmCategoryConfigTable = _TnPerSrSapObjectAlarmCategoryConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 20)
)
if mibBuilder.loadTexts:
    tnPerSrSapObjectAlarmCategoryConfigTable.setStatus("current")
_TnPerSrSapObjectAlarmCategoryConfigEntry_Object = MibTableRow
tnPerSrSapObjectAlarmCategoryConfigEntry = _TnPerSrSapObjectAlarmCategoryConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 20, 1)
)
tnPerSrSapObjectAlarmCategoryConfigEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (0, "TN-SAP-MIB", "tnSapPortId"),
    (0, "TN-SAP-MIB", "tnSapEncapValue"),
    (0, "TROPIC-LOG-MIB", "tnSrSapAlarmCategoryEntityType"),
    (0, "TROPIC-LOG-MIB", "tnSrSapAlarmCategoryCondition"),
)
if mibBuilder.loadTexts:
    tnPerSrSapObjectAlarmCategoryConfigEntry.setStatus("current")
_TnSrSapAlarmCategoryEntityType_Type = TnEntityType
_TnSrSapAlarmCategoryEntityType_Object = MibTableColumn
tnSrSapAlarmCategoryEntityType = _TnSrSapAlarmCategoryEntityType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 20, 1, 1),
    _TnSrSapAlarmCategoryEntityType_Type()
)
tnSrSapAlarmCategoryEntityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSrSapAlarmCategoryEntityType.setStatus("current")
_TnSrSapAlarmCategoryCondition_Type = TnCondition
_TnSrSapAlarmCategoryCondition_Object = MibTableColumn
tnSrSapAlarmCategoryCondition = _TnSrSapAlarmCategoryCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 20, 1, 2),
    _TnSrSapAlarmCategoryCondition_Type()
)
tnSrSapAlarmCategoryCondition.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSrSapAlarmCategoryCondition.setStatus("current")
_TnPerSrSapObjectAlarmCategory_Type = TnTrapCategory
_TnPerSrSapObjectAlarmCategory_Object = MibTableColumn
tnPerSrSapObjectAlarmCategory = _TnPerSrSapObjectAlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 20, 1, 3),
    _TnPerSrSapObjectAlarmCategory_Type()
)
tnPerSrSapObjectAlarmCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPerSrSapObjectAlarmCategory.setStatus("current")
_TnPerSrSapObjectAlarmEntityTypeCategory_Type = TnTrapCategory
_TnPerSrSapObjectAlarmEntityTypeCategory_Object = MibTableColumn
tnPerSrSapObjectAlarmEntityTypeCategory = _TnPerSrSapObjectAlarmEntityTypeCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 20, 1, 4),
    _TnPerSrSapObjectAlarmEntityTypeCategory_Type()
)
tnPerSrSapObjectAlarmEntityTypeCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerSrSapObjectAlarmEntityTypeCategory.setStatus("current")
_TnPerSrSapObjectAlarmDefaultCategory_Type = TnTrapCategory
_TnPerSrSapObjectAlarmDefaultCategory_Object = MibTableColumn
tnPerSrSapObjectAlarmDefaultCategory = _TnPerSrSapObjectAlarmDefaultCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 20, 1, 5),
    _TnPerSrSapObjectAlarmDefaultCategory_Type()
)
tnPerSrSapObjectAlarmDefaultCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerSrSapObjectAlarmDefaultCategory.setStatus("current")
_TnPerSrErpObjectAlarmCategoryConfigAttributeTotal_Type = Integer32
_TnPerSrErpObjectAlarmCategoryConfigAttributeTotal_Object = MibScalar
tnPerSrErpObjectAlarmCategoryConfigAttributeTotal = _TnPerSrErpObjectAlarmCategoryConfigAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 21),
    _TnPerSrErpObjectAlarmCategoryConfigAttributeTotal_Type()
)
tnPerSrErpObjectAlarmCategoryConfigAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerSrErpObjectAlarmCategoryConfigAttributeTotal.setStatus("current")
_TnPerSrErpObjectAlarmCategoryConfigTable_Object = MibTable
tnPerSrErpObjectAlarmCategoryConfigTable = _TnPerSrErpObjectAlarmCategoryConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 22)
)
if mibBuilder.loadTexts:
    tnPerSrErpObjectAlarmCategoryConfigTable.setStatus("current")
_TnPerSrErpObjectAlarmCategoryConfigEntry_Object = MibTableRow
tnPerSrErpObjectAlarmCategoryConfigEntry = _TnPerSrErpObjectAlarmCategoryConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 22, 1)
)
tnPerSrErpObjectAlarmCategoryConfigEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-ETH-RING-MIB", "tnEthRingIndex"),
    (0, "TROPIC-LOG-MIB", "tnSrErpAlarmCategoryEntityType"),
    (0, "TROPIC-LOG-MIB", "tnSrErpAlarmCategoryCondition"),
)
if mibBuilder.loadTexts:
    tnPerSrErpObjectAlarmCategoryConfigEntry.setStatus("current")
_TnSrErpAlarmCategoryEntityType_Type = TnEntityType
_TnSrErpAlarmCategoryEntityType_Object = MibTableColumn
tnSrErpAlarmCategoryEntityType = _TnSrErpAlarmCategoryEntityType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 22, 1, 1),
    _TnSrErpAlarmCategoryEntityType_Type()
)
tnSrErpAlarmCategoryEntityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSrErpAlarmCategoryEntityType.setStatus("current")
_TnSrErpAlarmCategoryCondition_Type = TnCondition
_TnSrErpAlarmCategoryCondition_Object = MibTableColumn
tnSrErpAlarmCategoryCondition = _TnSrErpAlarmCategoryCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 22, 1, 2),
    _TnSrErpAlarmCategoryCondition_Type()
)
tnSrErpAlarmCategoryCondition.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSrErpAlarmCategoryCondition.setStatus("current")
_TnPerSrErpObjectAlarmCategory_Type = TnTrapCategory
_TnPerSrErpObjectAlarmCategory_Object = MibTableColumn
tnPerSrErpObjectAlarmCategory = _TnPerSrErpObjectAlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 22, 1, 3),
    _TnPerSrErpObjectAlarmCategory_Type()
)
tnPerSrErpObjectAlarmCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPerSrErpObjectAlarmCategory.setStatus("current")
_TnPerSrErpObjectAlarmEntityTypeCategory_Type = TnTrapCategory
_TnPerSrErpObjectAlarmEntityTypeCategory_Object = MibTableColumn
tnPerSrErpObjectAlarmEntityTypeCategory = _TnPerSrErpObjectAlarmEntityTypeCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 22, 1, 4),
    _TnPerSrErpObjectAlarmEntityTypeCategory_Type()
)
tnPerSrErpObjectAlarmEntityTypeCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerSrErpObjectAlarmEntityTypeCategory.setStatus("current")
_TnPerSrErpObjectAlarmDefaultCategory_Type = TnTrapCategory
_TnPerSrErpObjectAlarmDefaultCategory_Object = MibTableColumn
tnPerSrErpObjectAlarmDefaultCategory = _TnPerSrErpObjectAlarmDefaultCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 22, 1, 5),
    _TnPerSrErpObjectAlarmDefaultCategory_Type()
)
tnPerSrErpObjectAlarmDefaultCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerSrErpObjectAlarmDefaultCategory.setStatus("current")
_TnPerSrMepObjectAlarmCategoryConfigAttributeTotal_Type = Integer32
_TnPerSrMepObjectAlarmCategoryConfigAttributeTotal_Object = MibScalar
tnPerSrMepObjectAlarmCategoryConfigAttributeTotal = _TnPerSrMepObjectAlarmCategoryConfigAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 23),
    _TnPerSrMepObjectAlarmCategoryConfigAttributeTotal_Type()
)
tnPerSrMepObjectAlarmCategoryConfigAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerSrMepObjectAlarmCategoryConfigAttributeTotal.setStatus("current")
_TnPerSrMepObjectAlarmCategoryConfigTable_Object = MibTable
tnPerSrMepObjectAlarmCategoryConfigTable = _TnPerSrMepObjectAlarmCategoryConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 24)
)
if mibBuilder.loadTexts:
    tnPerSrMepObjectAlarmCategoryConfigTable.setStatus("current")
_TnPerSrMepObjectAlarmCategoryConfigEntry_Object = MibTableRow
tnPerSrMepObjectAlarmCategoryConfigEntry = _TnPerSrMepObjectAlarmCategoryConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 24, 1)
)
tnPerSrMepObjectAlarmCategoryConfigEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "TROPIC-LOG-MIB", "tnSrMepAlarmCategoryEntityType"),
    (0, "TROPIC-LOG-MIB", "tnSrMepAlarmCategoryCondition"),
)
if mibBuilder.loadTexts:
    tnPerSrMepObjectAlarmCategoryConfigEntry.setStatus("current")
_TnSrMepAlarmCategoryEntityType_Type = TnEntityType
_TnSrMepAlarmCategoryEntityType_Object = MibTableColumn
tnSrMepAlarmCategoryEntityType = _TnSrMepAlarmCategoryEntityType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 24, 1, 1),
    _TnSrMepAlarmCategoryEntityType_Type()
)
tnSrMepAlarmCategoryEntityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSrMepAlarmCategoryEntityType.setStatus("current")
_TnSrMepAlarmCategoryCondition_Type = TnCondition
_TnSrMepAlarmCategoryCondition_Object = MibTableColumn
tnSrMepAlarmCategoryCondition = _TnSrMepAlarmCategoryCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 24, 1, 2),
    _TnSrMepAlarmCategoryCondition_Type()
)
tnSrMepAlarmCategoryCondition.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSrMepAlarmCategoryCondition.setStatus("current")
_TnPerSrMepObjectAlarmCategory_Type = TnTrapCategory
_TnPerSrMepObjectAlarmCategory_Object = MibTableColumn
tnPerSrMepObjectAlarmCategory = _TnPerSrMepObjectAlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 24, 1, 3),
    _TnPerSrMepObjectAlarmCategory_Type()
)
tnPerSrMepObjectAlarmCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPerSrMepObjectAlarmCategory.setStatus("current")
_TnPerSrMepObjectAlarmEntityTypeCategory_Type = TnTrapCategory
_TnPerSrMepObjectAlarmEntityTypeCategory_Object = MibTableColumn
tnPerSrMepObjectAlarmEntityTypeCategory = _TnPerSrMepObjectAlarmEntityTypeCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 24, 1, 4),
    _TnPerSrMepObjectAlarmEntityTypeCategory_Type()
)
tnPerSrMepObjectAlarmEntityTypeCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerSrMepObjectAlarmEntityTypeCategory.setStatus("current")
_TnPerSrMepObjectAlarmDefaultCategory_Type = TnTrapCategory
_TnPerSrMepObjectAlarmDefaultCategory_Object = MibTableColumn
tnPerSrMepObjectAlarmDefaultCategory = _TnPerSrMepObjectAlarmDefaultCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 24, 1, 5),
    _TnPerSrMepObjectAlarmDefaultCategory_Type()
)
tnPerSrMepObjectAlarmDefaultCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerSrMepObjectAlarmDefaultCategory.setStatus("current")
_TnPerSrOamTestObjectAlarmCategoryConfigAttributeTotal_Type = Integer32
_TnPerSrOamTestObjectAlarmCategoryConfigAttributeTotal_Object = MibScalar
tnPerSrOamTestObjectAlarmCategoryConfigAttributeTotal = _TnPerSrOamTestObjectAlarmCategoryConfigAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 25),
    _TnPerSrOamTestObjectAlarmCategoryConfigAttributeTotal_Type()
)
tnPerSrOamTestObjectAlarmCategoryConfigAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerSrOamTestObjectAlarmCategoryConfigAttributeTotal.setStatus("current")
_TnPerSrOamTestObjectAlarmCategoryConfigTable_Object = MibTable
tnPerSrOamTestObjectAlarmCategoryConfigTable = _TnPerSrOamTestObjectAlarmCategoryConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 26)
)
if mibBuilder.loadTexts:
    tnPerSrOamTestObjectAlarmCategoryConfigTable.setStatus("current")
_TnPerSrOamTestObjectAlarmCategoryConfigEntry_Object = MibTableRow
tnPerSrOamTestObjectAlarmCategoryConfigEntry = _TnPerSrOamTestObjectAlarmCategoryConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 26, 1)
)
tnPerSrOamTestObjectAlarmCategoryConfigEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-OAM-TEST-MIB", "tnOamSaaCtlTestIndex"),
    (0, "TROPIC-LOG-MIB", "tnSrOamTestAlarmCategoryEntityType"),
    (0, "TROPIC-LOG-MIB", "tnSrOamTestAlarmCategoryCondition"),
)
if mibBuilder.loadTexts:
    tnPerSrOamTestObjectAlarmCategoryConfigEntry.setStatus("current")
_TnSrOamTestAlarmCategoryEntityType_Type = TnEntityType
_TnSrOamTestAlarmCategoryEntityType_Object = MibTableColumn
tnSrOamTestAlarmCategoryEntityType = _TnSrOamTestAlarmCategoryEntityType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 26, 1, 1),
    _TnSrOamTestAlarmCategoryEntityType_Type()
)
tnSrOamTestAlarmCategoryEntityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSrOamTestAlarmCategoryEntityType.setStatus("current")
_TnSrOamTestAlarmCategoryCondition_Type = TnCondition
_TnSrOamTestAlarmCategoryCondition_Object = MibTableColumn
tnSrOamTestAlarmCategoryCondition = _TnSrOamTestAlarmCategoryCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 26, 1, 2),
    _TnSrOamTestAlarmCategoryCondition_Type()
)
tnSrOamTestAlarmCategoryCondition.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSrOamTestAlarmCategoryCondition.setStatus("current")
_TnPerSrOamTestObjectAlarmCategory_Type = TnTrapCategory
_TnPerSrOamTestObjectAlarmCategory_Object = MibTableColumn
tnPerSrOamTestObjectAlarmCategory = _TnPerSrOamTestObjectAlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 26, 1, 3),
    _TnPerSrOamTestObjectAlarmCategory_Type()
)
tnPerSrOamTestObjectAlarmCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPerSrOamTestObjectAlarmCategory.setStatus("current")
_TnPerSrOamTestObjectAlarmEntityTypeCategory_Type = TnTrapCategory
_TnPerSrOamTestObjectAlarmEntityTypeCategory_Object = MibTableColumn
tnPerSrOamTestObjectAlarmEntityTypeCategory = _TnPerSrOamTestObjectAlarmEntityTypeCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 26, 1, 4),
    _TnPerSrOamTestObjectAlarmEntityTypeCategory_Type()
)
tnPerSrOamTestObjectAlarmEntityTypeCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerSrOamTestObjectAlarmEntityTypeCategory.setStatus("current")
_TnPerSrOamTestObjectAlarmDefaultCategory_Type = TnTrapCategory
_TnPerSrOamTestObjectAlarmDefaultCategory_Object = MibTableColumn
tnPerSrOamTestObjectAlarmDefaultCategory = _TnPerSrOamTestObjectAlarmDefaultCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 26, 1, 5),
    _TnPerSrOamTestObjectAlarmDefaultCategory_Type()
)
tnPerSrOamTestObjectAlarmDefaultCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerSrOamTestObjectAlarmDefaultCategory.setStatus("current")
_TnPerRmdObjectAlarmCategoryConfigAttributeTotal_Type = Integer32
_TnPerRmdObjectAlarmCategoryConfigAttributeTotal_Object = MibScalar
tnPerRmdObjectAlarmCategoryConfigAttributeTotal = _TnPerRmdObjectAlarmCategoryConfigAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 27),
    _TnPerRmdObjectAlarmCategoryConfigAttributeTotal_Type()
)
tnPerRmdObjectAlarmCategoryConfigAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerRmdObjectAlarmCategoryConfigAttributeTotal.setStatus("current")
_TnPerRmdObjectAlarmCategoryConfigTable_Object = MibTable
tnPerRmdObjectAlarmCategoryConfigTable = _TnPerRmdObjectAlarmCategoryConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 28)
)
if mibBuilder.loadTexts:
    tnPerRmdObjectAlarmCategoryConfigTable.setStatus("current")
_TnPerRmdObjectAlarmCategoryConfigEntry_Object = MibTableRow
tnPerRmdObjectAlarmCategoryConfigEntry = _TnPerRmdObjectAlarmCategoryConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 28, 1)
)
tnPerRmdObjectAlarmCategoryConfigEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-RMD-SYSTEM-MIB", "tnRmdSystemId"),
    (0, "TROPIC-LOG-MIB", "tnRmdAlarmCategoryEntityType"),
    (0, "TROPIC-LOG-MIB", "tnRmdAlarmCategoryCondition"),
)
if mibBuilder.loadTexts:
    tnPerRmdObjectAlarmCategoryConfigEntry.setStatus("current")
_TnRmdAlarmCategoryEntityType_Type = TnEntityType
_TnRmdAlarmCategoryEntityType_Object = MibTableColumn
tnRmdAlarmCategoryEntityType = _TnRmdAlarmCategoryEntityType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 28, 1, 1),
    _TnRmdAlarmCategoryEntityType_Type()
)
tnRmdAlarmCategoryEntityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRmdAlarmCategoryEntityType.setStatus("current")
_TnRmdAlarmCategoryCondition_Type = TnCondition
_TnRmdAlarmCategoryCondition_Object = MibTableColumn
tnRmdAlarmCategoryCondition = _TnRmdAlarmCategoryCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 28, 1, 2),
    _TnRmdAlarmCategoryCondition_Type()
)
tnRmdAlarmCategoryCondition.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRmdAlarmCategoryCondition.setStatus("current")
_TnPerRmdObjectAlarmCategory_Type = TnTrapCategory
_TnPerRmdObjectAlarmCategory_Object = MibTableColumn
tnPerRmdObjectAlarmCategory = _TnPerRmdObjectAlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 28, 1, 3),
    _TnPerRmdObjectAlarmCategory_Type()
)
tnPerRmdObjectAlarmCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPerRmdObjectAlarmCategory.setStatus("current")
_TnPerRmdObjectAlarmEntityTypeCategory_Type = TnTrapCategory
_TnPerRmdObjectAlarmEntityTypeCategory_Object = MibTableColumn
tnPerRmdObjectAlarmEntityTypeCategory = _TnPerRmdObjectAlarmEntityTypeCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 28, 1, 4),
    _TnPerRmdObjectAlarmEntityTypeCategory_Type()
)
tnPerRmdObjectAlarmEntityTypeCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerRmdObjectAlarmEntityTypeCategory.setStatus("current")
_TnPerRmdObjectAlarmDefaultCategory_Type = TnTrapCategory
_TnPerRmdObjectAlarmDefaultCategory_Object = MibTableColumn
tnPerRmdObjectAlarmDefaultCategory = _TnPerRmdObjectAlarmDefaultCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 28, 1, 5),
    _TnPerRmdObjectAlarmDefaultCategory_Type()
)
tnPerRmdObjectAlarmDefaultCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerRmdObjectAlarmDefaultCategory.setStatus("current")
_TnPerRmdMepObjectAlarmCategoryConfigAttributeTotal_Type = Integer32
_TnPerRmdMepObjectAlarmCategoryConfigAttributeTotal_Object = MibScalar
tnPerRmdMepObjectAlarmCategoryConfigAttributeTotal = _TnPerRmdMepObjectAlarmCategoryConfigAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 29),
    _TnPerRmdMepObjectAlarmCategoryConfigAttributeTotal_Type()
)
tnPerRmdMepObjectAlarmCategoryConfigAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerRmdMepObjectAlarmCategoryConfigAttributeTotal.setStatus("current")
_TnPerRmdMepObjectAlarmCategoryConfigTable_Object = MibTable
tnPerRmdMepObjectAlarmCategoryConfigTable = _TnPerRmdMepObjectAlarmCategoryConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 30)
)
if mibBuilder.loadTexts:
    tnPerRmdMepObjectAlarmCategoryConfigTable.setStatus("current")
_TnPerRmdMepObjectAlarmCategoryConfigEntry_Object = MibTableRow
tnPerRmdMepObjectAlarmCategoryConfigEntry = _TnPerRmdMepObjectAlarmCategoryConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 30, 1)
)
tnPerRmdMepObjectAlarmCategoryConfigEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-RMD-SYSTEM-MIB", "tnRmdSystemId"),
    (0, "TN-RMD-CFM-MIB", "tnRmdCfmMepNumber"),
    (0, "TROPIC-LOG-MIB", "tnRmdMepAlarmCategoryEntityType"),
    (0, "TROPIC-LOG-MIB", "tnRmdMepAlarmCategoryCondition"),
)
if mibBuilder.loadTexts:
    tnPerRmdMepObjectAlarmCategoryConfigEntry.setStatus("current")
_TnRmdMepAlarmCategoryEntityType_Type = TnEntityType
_TnRmdMepAlarmCategoryEntityType_Object = MibTableColumn
tnRmdMepAlarmCategoryEntityType = _TnRmdMepAlarmCategoryEntityType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 30, 1, 1),
    _TnRmdMepAlarmCategoryEntityType_Type()
)
tnRmdMepAlarmCategoryEntityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRmdMepAlarmCategoryEntityType.setStatus("current")
_TnRmdMepAlarmCategoryCondition_Type = TnCondition
_TnRmdMepAlarmCategoryCondition_Object = MibTableColumn
tnRmdMepAlarmCategoryCondition = _TnRmdMepAlarmCategoryCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 30, 1, 2),
    _TnRmdMepAlarmCategoryCondition_Type()
)
tnRmdMepAlarmCategoryCondition.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRmdMepAlarmCategoryCondition.setStatus("current")
_TnPerRmdMepObjectAlarmCategory_Type = TnTrapCategory
_TnPerRmdMepObjectAlarmCategory_Object = MibTableColumn
tnPerRmdMepObjectAlarmCategory = _TnPerRmdMepObjectAlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 30, 1, 3),
    _TnPerRmdMepObjectAlarmCategory_Type()
)
tnPerRmdMepObjectAlarmCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPerRmdMepObjectAlarmCategory.setStatus("current")
_TnPerRmdMepObjectAlarmEntityTypeCategory_Type = TnTrapCategory
_TnPerRmdMepObjectAlarmEntityTypeCategory_Object = MibTableColumn
tnPerRmdMepObjectAlarmEntityTypeCategory = _TnPerRmdMepObjectAlarmEntityTypeCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 30, 1, 4),
    _TnPerRmdMepObjectAlarmEntityTypeCategory_Type()
)
tnPerRmdMepObjectAlarmEntityTypeCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerRmdMepObjectAlarmEntityTypeCategory.setStatus("current")
_TnPerRmdMepObjectAlarmDefaultCategory_Type = TnTrapCategory
_TnPerRmdMepObjectAlarmDefaultCategory_Object = MibTableColumn
tnPerRmdMepObjectAlarmDefaultCategory = _TnPerRmdMepObjectAlarmDefaultCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 30, 1, 5),
    _TnPerRmdMepObjectAlarmDefaultCategory_Type()
)
tnPerRmdMepObjectAlarmDefaultCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerRmdMepObjectAlarmDefaultCategory.setStatus("current")
_TnPerRmdIfObjectAlarmCategoryConfigAttributeTotal_Type = Integer32
_TnPerRmdIfObjectAlarmCategoryConfigAttributeTotal_Object = MibScalar
tnPerRmdIfObjectAlarmCategoryConfigAttributeTotal = _TnPerRmdIfObjectAlarmCategoryConfigAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 31),
    _TnPerRmdIfObjectAlarmCategoryConfigAttributeTotal_Type()
)
tnPerRmdIfObjectAlarmCategoryConfigAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerRmdIfObjectAlarmCategoryConfigAttributeTotal.setStatus("current")
_TnPerRmdIfObjectAlarmCategoryConfigTable_Object = MibTable
tnPerRmdIfObjectAlarmCategoryConfigTable = _TnPerRmdIfObjectAlarmCategoryConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 32)
)
if mibBuilder.loadTexts:
    tnPerRmdIfObjectAlarmCategoryConfigTable.setStatus("current")
_TnPerRmdIfObjectAlarmCategoryConfigEntry_Object = MibTableRow
tnPerRmdIfObjectAlarmCategoryConfigEntry = _TnPerRmdIfObjectAlarmCategoryConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 32, 1)
)
tnPerRmdIfObjectAlarmCategoryConfigEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-RMD-SYSTEM-MIB", "tnRmdSystemId"),
    (0, "TN-RMD-IF-MIB", "tnRmdIfIndex"),
    (0, "TROPIC-LOG-MIB", "tnRmdIfAlarmCategoryEntityType"),
    (0, "TROPIC-LOG-MIB", "tnRmdIfAlarmCategoryCondition"),
)
if mibBuilder.loadTexts:
    tnPerRmdIfObjectAlarmCategoryConfigEntry.setStatus("current")
_TnRmdIfAlarmCategoryEntityType_Type = TnEntityType
_TnRmdIfAlarmCategoryEntityType_Object = MibTableColumn
tnRmdIfAlarmCategoryEntityType = _TnRmdIfAlarmCategoryEntityType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 32, 1, 1),
    _TnRmdIfAlarmCategoryEntityType_Type()
)
tnRmdIfAlarmCategoryEntityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRmdIfAlarmCategoryEntityType.setStatus("current")
_TnRmdIfAlarmCategoryCondition_Type = TnCondition
_TnRmdIfAlarmCategoryCondition_Object = MibTableColumn
tnRmdIfAlarmCategoryCondition = _TnRmdIfAlarmCategoryCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 32, 1, 2),
    _TnRmdIfAlarmCategoryCondition_Type()
)
tnRmdIfAlarmCategoryCondition.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRmdIfAlarmCategoryCondition.setStatus("current")
_TnPerRmdIfObjectAlarmCategory_Type = TnTrapCategory
_TnPerRmdIfObjectAlarmCategory_Object = MibTableColumn
tnPerRmdIfObjectAlarmCategory = _TnPerRmdIfObjectAlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 32, 1, 3),
    _TnPerRmdIfObjectAlarmCategory_Type()
)
tnPerRmdIfObjectAlarmCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPerRmdIfObjectAlarmCategory.setStatus("current")
_TnPerRmdIfObjectAlarmEntityTypeCategory_Type = TnTrapCategory
_TnPerRmdIfObjectAlarmEntityTypeCategory_Object = MibTableColumn
tnPerRmdIfObjectAlarmEntityTypeCategory = _TnPerRmdIfObjectAlarmEntityTypeCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 32, 1, 4),
    _TnPerRmdIfObjectAlarmEntityTypeCategory_Type()
)
tnPerRmdIfObjectAlarmEntityTypeCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerRmdIfObjectAlarmEntityTypeCategory.setStatus("current")
_TnPerRmdIfObjectAlarmDefaultCategory_Type = TnTrapCategory
_TnPerRmdIfObjectAlarmDefaultCategory_Object = MibTableColumn
tnPerRmdIfObjectAlarmDefaultCategory = _TnPerRmdIfObjectAlarmDefaultCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 32, 1, 5),
    _TnPerRmdIfObjectAlarmDefaultCategory_Type()
)
tnPerRmdIfObjectAlarmDefaultCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerRmdIfObjectAlarmDefaultCategory.setStatus("current")
_TnPerRmdIfMauObjectAlarmCategoryConfigAttributeTotal_Type = Integer32
_TnPerRmdIfMauObjectAlarmCategoryConfigAttributeTotal_Object = MibScalar
tnPerRmdIfMauObjectAlarmCategoryConfigAttributeTotal = _TnPerRmdIfMauObjectAlarmCategoryConfigAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 33),
    _TnPerRmdIfMauObjectAlarmCategoryConfigAttributeTotal_Type()
)
tnPerRmdIfMauObjectAlarmCategoryConfigAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerRmdIfMauObjectAlarmCategoryConfigAttributeTotal.setStatus("current")
_TnPerRmdIfMauObjectAlarmCategoryConfigTable_Object = MibTable
tnPerRmdIfMauObjectAlarmCategoryConfigTable = _TnPerRmdIfMauObjectAlarmCategoryConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 34)
)
if mibBuilder.loadTexts:
    tnPerRmdIfMauObjectAlarmCategoryConfigTable.setStatus("current")
_TnPerRmdIfMauObjectAlarmCategoryConfigEntry_Object = MibTableRow
tnPerRmdIfMauObjectAlarmCategoryConfigEntry = _TnPerRmdIfMauObjectAlarmCategoryConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 34, 1)
)
tnPerRmdIfMauObjectAlarmCategoryConfigEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-RMD-SYSTEM-MIB", "tnRmdSystemId"),
    (0, "TN-RMD-IF-MIB", "tnRmdIfIndex"),
    (0, "TN-RMD-IF-MIB", "tnRmdIfMauIndex"),
    (0, "TROPIC-LOG-MIB", "tnRmdIfMauAlarmCategoryEntityType"),
    (0, "TROPIC-LOG-MIB", "tnRmdIfMauAlarmCategoryCondition"),
)
if mibBuilder.loadTexts:
    tnPerRmdIfMauObjectAlarmCategoryConfigEntry.setStatus("current")
_TnRmdIfMauAlarmCategoryEntityType_Type = TnEntityType
_TnRmdIfMauAlarmCategoryEntityType_Object = MibTableColumn
tnRmdIfMauAlarmCategoryEntityType = _TnRmdIfMauAlarmCategoryEntityType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 34, 1, 1),
    _TnRmdIfMauAlarmCategoryEntityType_Type()
)
tnRmdIfMauAlarmCategoryEntityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRmdIfMauAlarmCategoryEntityType.setStatus("current")
_TnRmdIfMauAlarmCategoryCondition_Type = TnCondition
_TnRmdIfMauAlarmCategoryCondition_Object = MibTableColumn
tnRmdIfMauAlarmCategoryCondition = _TnRmdIfMauAlarmCategoryCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 34, 1, 2),
    _TnRmdIfMauAlarmCategoryCondition_Type()
)
tnRmdIfMauAlarmCategoryCondition.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRmdIfMauAlarmCategoryCondition.setStatus("current")
_TnPerRmdIfMauObjectAlarmCategory_Type = TnTrapCategory
_TnPerRmdIfMauObjectAlarmCategory_Object = MibTableColumn
tnPerRmdIfMauObjectAlarmCategory = _TnPerRmdIfMauObjectAlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 34, 1, 3),
    _TnPerRmdIfMauObjectAlarmCategory_Type()
)
tnPerRmdIfMauObjectAlarmCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPerRmdIfMauObjectAlarmCategory.setStatus("current")
_TnPerRmdIfMauObjectAlarmEntityTypeCategory_Type = TnTrapCategory
_TnPerRmdIfMauObjectAlarmEntityTypeCategory_Object = MibTableColumn
tnPerRmdIfMauObjectAlarmEntityTypeCategory = _TnPerRmdIfMauObjectAlarmEntityTypeCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 34, 1, 4),
    _TnPerRmdIfMauObjectAlarmEntityTypeCategory_Type()
)
tnPerRmdIfMauObjectAlarmEntityTypeCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerRmdIfMauObjectAlarmEntityTypeCategory.setStatus("current")
_TnPerRmdIfMauObjectAlarmDefaultCategory_Type = TnTrapCategory
_TnPerRmdIfMauObjectAlarmDefaultCategory_Object = MibTableColumn
tnPerRmdIfMauObjectAlarmDefaultCategory = _TnPerRmdIfMauObjectAlarmDefaultCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 34, 1, 5),
    _TnPerRmdIfMauObjectAlarmDefaultCategory_Type()
)
tnPerRmdIfMauObjectAlarmDefaultCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerRmdIfMauObjectAlarmDefaultCategory.setStatus("current")
_TnPerRmdCesChannelObjectAlarmCategoryConfigAttributeTotal_Type = Integer32
_TnPerRmdCesChannelObjectAlarmCategoryConfigAttributeTotal_Object = MibScalar
tnPerRmdCesChannelObjectAlarmCategoryConfigAttributeTotal = _TnPerRmdCesChannelObjectAlarmCategoryConfigAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 35),
    _TnPerRmdCesChannelObjectAlarmCategoryConfigAttributeTotal_Type()
)
tnPerRmdCesChannelObjectAlarmCategoryConfigAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerRmdCesChannelObjectAlarmCategoryConfigAttributeTotal.setStatus("current")
_TnPerRmdCesChannelObjectAlarmCategoryConfigTable_Object = MibTable
tnPerRmdCesChannelObjectAlarmCategoryConfigTable = _TnPerRmdCesChannelObjectAlarmCategoryConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 36)
)
if mibBuilder.loadTexts:
    tnPerRmdCesChannelObjectAlarmCategoryConfigTable.setStatus("current")
_TnPerRmdCesChannelObjectAlarmCategoryConfigEntry_Object = MibTableRow
tnPerRmdCesChannelObjectAlarmCategoryConfigEntry = _TnPerRmdCesChannelObjectAlarmCategoryConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 36, 1)
)
tnPerRmdCesChannelObjectAlarmCategoryConfigEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-RMD-SYSTEM-MIB", "tnRmdSystemId"),
    (0, "TN-RMD-TSOP-MIB", "tnRmdTsopIwfChannelNumber"),
    (0, "TROPIC-LOG-MIB", "tnRmdCesChannelAlarmCategoryEntityType"),
    (0, "TROPIC-LOG-MIB", "tnRmdCesChannelAlarmCategoryCondition"),
)
if mibBuilder.loadTexts:
    tnPerRmdCesChannelObjectAlarmCategoryConfigEntry.setStatus("current")
_TnRmdCesChannelAlarmCategoryEntityType_Type = TnEntityType
_TnRmdCesChannelAlarmCategoryEntityType_Object = MibTableColumn
tnRmdCesChannelAlarmCategoryEntityType = _TnRmdCesChannelAlarmCategoryEntityType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 36, 1, 1),
    _TnRmdCesChannelAlarmCategoryEntityType_Type()
)
tnRmdCesChannelAlarmCategoryEntityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRmdCesChannelAlarmCategoryEntityType.setStatus("current")
_TnRmdCesChannelAlarmCategoryCondition_Type = TnCondition
_TnRmdCesChannelAlarmCategoryCondition_Object = MibTableColumn
tnRmdCesChannelAlarmCategoryCondition = _TnRmdCesChannelAlarmCategoryCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 36, 1, 2),
    _TnRmdCesChannelAlarmCategoryCondition_Type()
)
tnRmdCesChannelAlarmCategoryCondition.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRmdCesChannelAlarmCategoryCondition.setStatus("current")
_TnPerRmdCesChannelObjectAlarmCategory_Type = TnTrapCategory
_TnPerRmdCesChannelObjectAlarmCategory_Object = MibTableColumn
tnPerRmdCesChannelObjectAlarmCategory = _TnPerRmdCesChannelObjectAlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 36, 1, 3),
    _TnPerRmdCesChannelObjectAlarmCategory_Type()
)
tnPerRmdCesChannelObjectAlarmCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPerRmdCesChannelObjectAlarmCategory.setStatus("current")
_TnPerRmdCesChannelObjectAlarmEntityTypeCategory_Type = TnTrapCategory
_TnPerRmdCesChannelObjectAlarmEntityTypeCategory_Object = MibTableColumn
tnPerRmdCesChannelObjectAlarmEntityTypeCategory = _TnPerRmdCesChannelObjectAlarmEntityTypeCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 36, 1, 4),
    _TnPerRmdCesChannelObjectAlarmEntityTypeCategory_Type()
)
tnPerRmdCesChannelObjectAlarmEntityTypeCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerRmdCesChannelObjectAlarmEntityTypeCategory.setStatus("current")
_TnPerRmdCesChannelObjectAlarmDefaultCategory_Type = TnTrapCategory
_TnPerRmdCesChannelObjectAlarmDefaultCategory_Object = MibTableColumn
tnPerRmdCesChannelObjectAlarmDefaultCategory = _TnPerRmdCesChannelObjectAlarmDefaultCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 36, 1, 5),
    _TnPerRmdCesChannelObjectAlarmDefaultCategory_Type()
)
tnPerRmdCesChannelObjectAlarmDefaultCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerRmdCesChannelObjectAlarmDefaultCategory.setStatus("current")
_TnPerOthObjectAlarmCategoryConfigAttributeTotal_Type = Integer32
_TnPerOthObjectAlarmCategoryConfigAttributeTotal_Object = MibScalar
tnPerOthObjectAlarmCategoryConfigAttributeTotal = _TnPerOthObjectAlarmCategoryConfigAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 37),
    _TnPerOthObjectAlarmCategoryConfigAttributeTotal_Type()
)
tnPerOthObjectAlarmCategoryConfigAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerOthObjectAlarmCategoryConfigAttributeTotal.setStatus("current")
_TnPerOthObjectAlarmCategoryConfigTable_Object = MibTable
tnPerOthObjectAlarmCategoryConfigTable = _TnPerOthObjectAlarmCategoryConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 38)
)
if mibBuilder.loadTexts:
    tnPerOthObjectAlarmCategoryConfigTable.setStatus("current")
_TnPerOthObjectAlarmCategoryConfigEntry_Object = MibTableRow
tnPerOthObjectAlarmCategoryConfigEntry = _TnPerOthObjectAlarmCategoryConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 38, 1)
)
tnPerOthObjectAlarmCategoryConfigEntry.setIndexNames(
    (0, "TROPIC-LOG-MIB", "tnOthAlarmCategoryObjectId"),
    (0, "TROPIC-LOG-MIB", "tnOthAlarmCategoryTribObjectId"),
    (0, "TROPIC-LOG-MIB", "tnOthAlarmCategoryDirection"),
    (0, "TROPIC-LOG-MIB", "tnOthAlarmCategoryEntityType"),
    (0, "TROPIC-LOG-MIB", "tnOthAlarmCategoryCondition"),
)
if mibBuilder.loadTexts:
    tnPerOthObjectAlarmCategoryConfigEntry.setStatus("current")
_TnOthAlarmCategoryObjectId_Type = Unsigned32
_TnOthAlarmCategoryObjectId_Object = MibTableColumn
tnOthAlarmCategoryObjectId = _TnOthAlarmCategoryObjectId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 38, 1, 1),
    _TnOthAlarmCategoryObjectId_Type()
)
tnOthAlarmCategoryObjectId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOthAlarmCategoryObjectId.setStatus("current")
_TnOthAlarmCategoryTribObjectId_Type = Unsigned32
_TnOthAlarmCategoryTribObjectId_Object = MibTableColumn
tnOthAlarmCategoryTribObjectId = _TnOthAlarmCategoryTribObjectId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 38, 1, 2),
    _TnOthAlarmCategoryTribObjectId_Type()
)
tnOthAlarmCategoryTribObjectId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOthAlarmCategoryTribObjectId.setStatus("current")
_TnOthAlarmCategoryDirection_Type = AluWdmAlarmCategoryDirection
_TnOthAlarmCategoryDirection_Object = MibTableColumn
tnOthAlarmCategoryDirection = _TnOthAlarmCategoryDirection_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 38, 1, 3),
    _TnOthAlarmCategoryDirection_Type()
)
tnOthAlarmCategoryDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOthAlarmCategoryDirection.setStatus("current")
_TnOthAlarmCategoryEntityType_Type = TnEntityType
_TnOthAlarmCategoryEntityType_Object = MibTableColumn
tnOthAlarmCategoryEntityType = _TnOthAlarmCategoryEntityType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 38, 1, 4),
    _TnOthAlarmCategoryEntityType_Type()
)
tnOthAlarmCategoryEntityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOthAlarmCategoryEntityType.setStatus("current")
_TnOthAlarmCategoryCondition_Type = TnCondition
_TnOthAlarmCategoryCondition_Object = MibTableColumn
tnOthAlarmCategoryCondition = _TnOthAlarmCategoryCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 38, 1, 5),
    _TnOthAlarmCategoryCondition_Type()
)
tnOthAlarmCategoryCondition.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnOthAlarmCategoryCondition.setStatus("current")
_TnPerOthObjectAlarmCategory_Type = TnTrapCategory
_TnPerOthObjectAlarmCategory_Object = MibTableColumn
tnPerOthObjectAlarmCategory = _TnPerOthObjectAlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 38, 1, 6),
    _TnPerOthObjectAlarmCategory_Type()
)
tnPerOthObjectAlarmCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPerOthObjectAlarmCategory.setStatus("current")
_TnPerOthObjectAlarmEntityTypeCategory_Type = TnTrapCategory
_TnPerOthObjectAlarmEntityTypeCategory_Object = MibTableColumn
tnPerOthObjectAlarmEntityTypeCategory = _TnPerOthObjectAlarmEntityTypeCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 38, 1, 7),
    _TnPerOthObjectAlarmEntityTypeCategory_Type()
)
tnPerOthObjectAlarmEntityTypeCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerOthObjectAlarmEntityTypeCategory.setStatus("current")
_TnPerOthObjectAlarmDefaultCategory_Type = TnTrapCategory
_TnPerOthObjectAlarmDefaultCategory_Object = MibTableColumn
tnPerOthObjectAlarmDefaultCategory = _TnPerOthObjectAlarmDefaultCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 38, 1, 8),
    _TnPerOthObjectAlarmDefaultCategory_Type()
)
tnPerOthObjectAlarmDefaultCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerOthObjectAlarmDefaultCategory.setStatus("current")
_TnPerRmdNimObjectAlarmCategoryConfigAttributeTotal_Type = Integer32
_TnPerRmdNimObjectAlarmCategoryConfigAttributeTotal_Object = MibScalar
tnPerRmdNimObjectAlarmCategoryConfigAttributeTotal = _TnPerRmdNimObjectAlarmCategoryConfigAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 39),
    _TnPerRmdNimObjectAlarmCategoryConfigAttributeTotal_Type()
)
tnPerRmdNimObjectAlarmCategoryConfigAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerRmdNimObjectAlarmCategoryConfigAttributeTotal.setStatus("current")
_TnPerRmdNimObjectAlarmCategoryConfigTable_Object = MibTable
tnPerRmdNimObjectAlarmCategoryConfigTable = _TnPerRmdNimObjectAlarmCategoryConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 40)
)
if mibBuilder.loadTexts:
    tnPerRmdNimObjectAlarmCategoryConfigTable.setStatus("current")
_TnPerRmdNimObjectAlarmCategoryConfigEntry_Object = MibTableRow
tnPerRmdNimObjectAlarmCategoryConfigEntry = _TnPerRmdNimObjectAlarmCategoryConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 40, 1)
)
tnPerRmdNimObjectAlarmCategoryConfigEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-RMD-SYSTEM-MIB", "tnRmdSystemId"),
    (0, "TN-RMD-IF-MIB", "tnRmdIfIndex"),
    (0, "TROPIC-LOG-MIB", "tnRmdIfNimDirection"),
    (0, "TROPIC-LOG-MIB", "tnRmdNimAlarmCategoryEntityType"),
    (0, "TROPIC-LOG-MIB", "tnRmdNimAlarmCategoryCondition"),
)
if mibBuilder.loadTexts:
    tnPerRmdNimObjectAlarmCategoryConfigEntry.setStatus("current")
_TnRmdIfNimDirection_Type = TnRmdNimDirection
_TnRmdIfNimDirection_Object = MibTableColumn
tnRmdIfNimDirection = _TnRmdIfNimDirection_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 40, 1, 1),
    _TnRmdIfNimDirection_Type()
)
tnRmdIfNimDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRmdIfNimDirection.setStatus("current")
_TnRmdNimAlarmCategoryEntityType_Type = TnEntityType
_TnRmdNimAlarmCategoryEntityType_Object = MibTableColumn
tnRmdNimAlarmCategoryEntityType = _TnRmdNimAlarmCategoryEntityType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 40, 1, 2),
    _TnRmdNimAlarmCategoryEntityType_Type()
)
tnRmdNimAlarmCategoryEntityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRmdNimAlarmCategoryEntityType.setStatus("current")
_TnRmdNimAlarmCategoryCondition_Type = TnCondition
_TnRmdNimAlarmCategoryCondition_Object = MibTableColumn
tnRmdNimAlarmCategoryCondition = _TnRmdNimAlarmCategoryCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 40, 1, 3),
    _TnRmdNimAlarmCategoryCondition_Type()
)
tnRmdNimAlarmCategoryCondition.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRmdNimAlarmCategoryCondition.setStatus("current")
_TnPerRmdNimObjectAlarmCategory_Type = TnTrapCategory
_TnPerRmdNimObjectAlarmCategory_Object = MibTableColumn
tnPerRmdNimObjectAlarmCategory = _TnPerRmdNimObjectAlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 40, 1, 4),
    _TnPerRmdNimObjectAlarmCategory_Type()
)
tnPerRmdNimObjectAlarmCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPerRmdNimObjectAlarmCategory.setStatus("current")
_TnPerRmdNimObjectAlarmEntityTypeCategory_Type = TnTrapCategory
_TnPerRmdNimObjectAlarmEntityTypeCategory_Object = MibTableColumn
tnPerRmdNimObjectAlarmEntityTypeCategory = _TnPerRmdNimObjectAlarmEntityTypeCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 40, 1, 5),
    _TnPerRmdNimObjectAlarmEntityTypeCategory_Type()
)
tnPerRmdNimObjectAlarmEntityTypeCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerRmdNimObjectAlarmEntityTypeCategory.setStatus("current")
_TnPerRmdNimObjectAlarmDefaultCategory_Type = TnTrapCategory
_TnPerRmdNimObjectAlarmDefaultCategory_Object = MibTableColumn
tnPerRmdNimObjectAlarmDefaultCategory = _TnPerRmdNimObjectAlarmDefaultCategory_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 2, 4, 40, 1, 6),
    _TnPerRmdNimObjectAlarmDefaultCategory_Type()
)
tnPerRmdNimObjectAlarmDefaultCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPerRmdNimObjectAlarmDefaultCategory.setStatus("current")

# Managed Objects groups

tnLogScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 1)
)
tnLogScalarsGroup.setObjects(
      *(("TROPIC-LOG-MIB", "tnCriticalAlarmLogTotal"),
        ("TROPIC-LOG-MIB", "tnMajorAlarmLogTotal"),
        ("TROPIC-LOG-MIB", "tnMinorAlarmLogTotal"),
        ("TROPIC-LOG-MIB", "tnStateChangeLogTotal"),
        ("TROPIC-LOG-MIB", "tnUserActionLogTotal"),
        ("TROPIC-LOG-MIB", "tnGeneralEventLogTotal"),
        ("TROPIC-LOG-MIB", "tnLogTotal"),
        ("TROPIC-LOG-MIB", "tnActiveAlarmTotal"),
        ("TROPIC-LOG-MIB", "tnPersistentLogTotal"),
        ("TROPIC-LOG-MIB", "tnActiveCriticalAlarmTotal"),
        ("TROPIC-LOG-MIB", "tnActiveMajorAlarmTotal"),
        ("TROPIC-LOG-MIB", "tnActiveMinorAlarmTotal"),
        ("TROPIC-LOG-MIB", "tnActiveOrMaskedAlarmTotal"),
        ("TROPIC-LOG-MIB", "tnNotAlarmedLogTotal"),
        ("TROPIC-LOG-MIB", "tnSecurityLogTotal"),
        ("TROPIC-LOG-MIB", "tnWarningAlarmLogTotal"),
        ("TROPIC-LOG-MIB", "tnActiveWarningAlarmTotal"))
)
if mibBuilder.loadTexts:
    tnLogScalarsGroup.setStatus("current")

tnCriticalAlarmLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 2)
)
tnCriticalAlarmLogGroup.setObjects(
      *(("TROPIC-LOG-MIB", "tnCriticalAlarmLogType"),
        ("TROPIC-LOG-MIB", "tnCriticalAlarmLogTime"),
        ("TROPIC-LOG-MIB", "tnCriticalAlarmLogObjectIDType"),
        ("TROPIC-LOG-MIB", "tnCriticalAlarmLogObjectID"),
        ("TROPIC-LOG-MIB", "tnCriticalAlarmLogDescr"),
        ("TROPIC-LOG-MIB", "tnCriticalAlarmLogData"),
        ("TROPIC-LOG-MIB", "tnCriticalAlarmLogServiceAffecting"),
        ("TROPIC-LOG-MIB", "tnCriticalAlarmLogSlotProgrammedType"),
        ("TROPIC-LOG-MIB", "tnCriticalAlarmLogEntityType"),
        ("TROPIC-LOG-MIB", "tnCriticalAlarmLogCondition"))
)
if mibBuilder.loadTexts:
    tnCriticalAlarmLogGroup.setStatus("current")

tnMajorAlarmLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 3)
)
tnMajorAlarmLogGroup.setObjects(
      *(("TROPIC-LOG-MIB", "tnMajorAlarmLogType"),
        ("TROPIC-LOG-MIB", "tnMajorAlarmLogTime"),
        ("TROPIC-LOG-MIB", "tnMajorAlarmLogObjectIDType"),
        ("TROPIC-LOG-MIB", "tnMajorAlarmLogObjectID"),
        ("TROPIC-LOG-MIB", "tnMajorAlarmLogDescr"),
        ("TROPIC-LOG-MIB", "tnMajorAlarmLogData"),
        ("TROPIC-LOG-MIB", "tnMajorAlarmLogServiceAffecting"),
        ("TROPIC-LOG-MIB", "tnMajorAlarmLogSlotProgrammedType"),
        ("TROPIC-LOG-MIB", "tnMajorAlarmLogEntityType"),
        ("TROPIC-LOG-MIB", "tnMajorAlarmLogCondition"))
)
if mibBuilder.loadTexts:
    tnMajorAlarmLogGroup.setStatus("current")

tnMinorAlarmLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 4)
)
tnMinorAlarmLogGroup.setObjects(
      *(("TROPIC-LOG-MIB", "tnMinorAlarmLogType"),
        ("TROPIC-LOG-MIB", "tnMinorAlarmLogTime"),
        ("TROPIC-LOG-MIB", "tnMinorAlarmLogObjectIDType"),
        ("TROPIC-LOG-MIB", "tnMinorAlarmLogObjectID"),
        ("TROPIC-LOG-MIB", "tnMinorAlarmLogDescr"),
        ("TROPIC-LOG-MIB", "tnMinorAlarmLogData"),
        ("TROPIC-LOG-MIB", "tnMinorAlarmLogServiceAffecting"),
        ("TROPIC-LOG-MIB", "tnMinorAlarmLogSlotProgrammedType"),
        ("TROPIC-LOG-MIB", "tnMinorAlarmLogEntityType"),
        ("TROPIC-LOG-MIB", "tnMinorAlarmLogCondition"))
)
if mibBuilder.loadTexts:
    tnMinorAlarmLogGroup.setStatus("current")

tnStateChangeLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 5)
)
tnStateChangeLogGroup.setObjects(
      *(("TROPIC-LOG-MIB", "tnStateChangeLogType"),
        ("TROPIC-LOG-MIB", "tnStateChangeLogTime"),
        ("TROPIC-LOG-MIB", "tnStateChangeLogObjectIDType"),
        ("TROPIC-LOG-MIB", "tnStateChangeLogObjectID"),
        ("TROPIC-LOG-MIB", "tnStateChangeLogDescr"),
        ("TROPIC-LOG-MIB", "tnStateChangeLogData"),
        ("TROPIC-LOG-MIB", "tnStateChangeLogSlotProgrammedType"))
)
if mibBuilder.loadTexts:
    tnStateChangeLogGroup.setStatus("current")

tnUserActionLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 6)
)
tnUserActionLogGroup.setObjects(
      *(("TROPIC-LOG-MIB", "tnUserActionLogType"),
        ("TROPIC-LOG-MIB", "tnUserActionLogTime"),
        ("TROPIC-LOG-MIB", "tnUserActionLogObjectIDType"),
        ("TROPIC-LOG-MIB", "tnUserActionLogObjectID"),
        ("TROPIC-LOG-MIB", "tnUserActionLogDescr"),
        ("TROPIC-LOG-MIB", "tnUserActionLogChangedObject"),
        ("TROPIC-LOG-MIB", "tnUserActionLogData"))
)
if mibBuilder.loadTexts:
    tnUserActionLogGroup.setStatus("current")

tnGeneralEventLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 7)
)
tnGeneralEventLogGroup.setObjects(
      *(("TROPIC-LOG-MIB", "tnGeneralEventLogType"),
        ("TROPIC-LOG-MIB", "tnGeneralEventLogTime"),
        ("TROPIC-LOG-MIB", "tnGeneralEventLogObjectIDType"),
        ("TROPIC-LOG-MIB", "tnGeneralEventLogObjectID"),
        ("TROPIC-LOG-MIB", "tnGeneralEventLogDescr"),
        ("TROPIC-LOG-MIB", "tnGeneralEventLogChangedObject"),
        ("TROPIC-LOG-MIB", "tnGeneralEventLogData"),
        ("TROPIC-LOG-MIB", "tnGeneralEventLogSlotProgrammedType"))
)
if mibBuilder.loadTexts:
    tnGeneralEventLogGroup.setStatus("current")

tnLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 8)
)
tnLogGroup.setObjects(
      *(("TROPIC-LOG-MIB", "tnLogType"),
        ("TROPIC-LOG-MIB", "tnLogTime"),
        ("TROPIC-LOG-MIB", "tnLogObjectIDType"),
        ("TROPIC-LOG-MIB", "tnLogObjectID"),
        ("TROPIC-LOG-MIB", "tnLogCategory"),
        ("TROPIC-LOG-MIB", "tnLogDescr"),
        ("TROPIC-LOG-MIB", "tnLogChangedObject"),
        ("TROPIC-LOG-MIB", "tnLogData"),
        ("TROPIC-LOG-MIB", "tnLogServiceAffecting"),
        ("TROPIC-LOG-MIB", "tnLogSlotProgrammedType"),
        ("TROPIC-LOG-MIB", "tnLogEntityType"),
        ("TROPIC-LOG-MIB", "tnLogCondition"))
)
if mibBuilder.loadTexts:
    tnLogGroup.setStatus("current")

tnActiveAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 9)
)
tnActiveAlarmGroup.setObjects(
      *(("TROPIC-LOG-MIB", "tnActiveAlarmSerialNumber"),
        ("TROPIC-LOG-MIB", "tnActiveAlarmType"),
        ("TROPIC-LOG-MIB", "tnActiveAlarmTime"),
        ("TROPIC-LOG-MIB", "tnActiveAlarmObjectIDType"),
        ("TROPIC-LOG-MIB", "tnActiveAlarmObjectID"),
        ("TROPIC-LOG-MIB", "tnActiveAlarmCategory"),
        ("TROPIC-LOG-MIB", "tnActiveAlarmDescr"),
        ("TROPIC-LOG-MIB", "tnActiveAlarmData"),
        ("TROPIC-LOG-MIB", "tnActiveAlarmServiceAffecting"),
        ("TROPIC-LOG-MIB", "tnActiveAlarmSlotProgrammedType"),
        ("TROPIC-LOG-MIB", "tnActiveAlarmEntityType"),
        ("TROPIC-LOG-MIB", "tnActiveAlarmCondition"))
)
if mibBuilder.loadTexts:
    tnActiveAlarmGroup.setStatus("current")

tnPersistentLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 10)
)
tnPersistentLogGroup.setObjects(
      *(("TROPIC-LOG-MIB", "tnPersistentLogType"),
        ("TROPIC-LOG-MIB", "tnPersistentLogTime"),
        ("TROPIC-LOG-MIB", "tnPersistentLogObjectIDType"),
        ("TROPIC-LOG-MIB", "tnPersistentLogObjectID"),
        ("TROPIC-LOG-MIB", "tnPersistentLogCategory"),
        ("TROPIC-LOG-MIB", "tnPersistentLogDescr"),
        ("TROPIC-LOG-MIB", "tnPersistentLogChangedObject"),
        ("TROPIC-LOG-MIB", "tnPersistentLogData"),
        ("TROPIC-LOG-MIB", "tnPersistentLogServiceAffecting"),
        ("TROPIC-LOG-MIB", "tnPersistentLogSlotProgrammedType"))
)
if mibBuilder.loadTexts:
    tnPersistentLogGroup.setStatus("current")

tnActiveOrMaskedAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 11)
)
tnActiveOrMaskedAlarmGroup.setObjects(
      *(("TROPIC-LOG-MIB", "tnActiveOrMaskedAlarmSerialNumber"),
        ("TROPIC-LOG-MIB", "tnActiveOrMaskedAlarmType"),
        ("TROPIC-LOG-MIB", "tnActiveOrMaskedAlarmTime"),
        ("TROPIC-LOG-MIB", "tnActiveOrMaskedAlarmObjectIDType"),
        ("TROPIC-LOG-MIB", "tnActiveOrMaskedAlarmObjectID"),
        ("TROPIC-LOG-MIB", "tnActiveOrMaskedAlarmCategory"),
        ("TROPIC-LOG-MIB", "tnActiveOrMaskedAlarmDescr"),
        ("TROPIC-LOG-MIB", "tnActiveOrMaskedAlarmData"),
        ("TROPIC-LOG-MIB", "tnActiveOrMaskedAlarmServiceAffecting"),
        ("TROPIC-LOG-MIB", "tnActiveOrMaskedAlarmSlotProgrammedType"),
        ("TROPIC-LOG-MIB", "tnActiveOrMaskedAlarmIsMasked"),
        ("TROPIC-LOG-MIB", "tnActiveOrMaskedAlarmEntityType"),
        ("TROPIC-LOG-MIB", "tnActiveOrMaskedAlarmCondition"))
)
if mibBuilder.loadTexts:
    tnActiveOrMaskedAlarmGroup.setStatus("current")

tnNotAlarmedLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 12)
)
tnNotAlarmedLogGroup.setObjects(
      *(("TROPIC-LOG-MIB", "tnNotAlarmedLogType"),
        ("TROPIC-LOG-MIB", "tnNotAlarmedLogTime"),
        ("TROPIC-LOG-MIB", "tnNotAlarmedLogObjectIDType"),
        ("TROPIC-LOG-MIB", "tnNotAlarmedLogObjectID"),
        ("TROPIC-LOG-MIB", "tnNotAlarmedLogDescr"),
        ("TROPIC-LOG-MIB", "tnNotAlarmedLogData"),
        ("TROPIC-LOG-MIB", "tnNotAlarmedLogServiceAffecting"),
        ("TROPIC-LOG-MIB", "tnNotAlarmedLogSlotProgrammedType"),
        ("TROPIC-LOG-MIB", "tnNotAlarmedLogEntityType"),
        ("TROPIC-LOG-MIB", "tnNotAlarmedLogCondition"))
)
if mibBuilder.loadTexts:
    tnNotAlarmedLogGroup.setStatus("current")

tnPerObjectAlarmCategoryConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 13)
)
tnPerObjectAlarmCategoryConfigGroup.setObjects(
      *(("TROPIC-LOG-MIB", "tnPerObjectAlarmCategory"),
        ("TROPIC-LOG-MIB", "tnPerObjectAlarmEntityTypeCategory"),
        ("TROPIC-LOG-MIB", "tnPerObjectAlarmDefaultCategory"))
)
if mibBuilder.loadTexts:
    tnPerObjectAlarmCategoryConfigGroup.setStatus("current")

tnAlarmProfileConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 14)
)
tnAlarmProfileConfigGroup.setObjects(
      *(("TROPIC-LOG-MIB", "tnAlarmProfileConfigCategory"),
        ("TROPIC-LOG-MIB", "tnAlarmProfileConfigDefaultCategory"),
        ("TROPIC-LOG-MIB", "tnAlarmProfileConfigDescr"))
)
if mibBuilder.loadTexts:
    tnAlarmProfileConfigGroup.setStatus("current")

tnSecurityLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 15)
)
tnSecurityLogGroup.setObjects(
      *(("TROPIC-LOG-MIB", "tnSecurityLogType"),
        ("TROPIC-LOG-MIB", "tnSecurityLogTime"),
        ("TROPIC-LOG-MIB", "tnSecurityLogObjectIDType"),
        ("TROPIC-LOG-MIB", "tnSecurityLogObjectID"),
        ("TROPIC-LOG-MIB", "tnSecurityLogDescr"),
        ("TROPIC-LOG-MIB", "tnSecurityLogData"),
        ("TROPIC-LOG-MIB", "tnSecurityLogUserID"),
        ("TROPIC-LOG-MIB", "tnSecurityLogUserSessionNumber"),
        ("TROPIC-LOG-MIB", "tnSecurityLogHeaderType"),
        ("TROPIC-LOG-MIB", "tnSecurityLogUserPrivilege"),
        ("TROPIC-LOG-MIB", "tnSecurityLogUserDestinationAddress"),
        ("TROPIC-LOG-MIB", "tnSecurityLogResult"))
)
if mibBuilder.loadTexts:
    tnSecurityLogGroup.setStatus("current")

tnWarningAlarmLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 16)
)
tnWarningAlarmLogGroup.setObjects(
      *(("TROPIC-LOG-MIB", "tnWarningAlarmLogType"),
        ("TROPIC-LOG-MIB", "tnWarningAlarmLogTime"),
        ("TROPIC-LOG-MIB", "tnWarningAlarmLogObjectIDType"),
        ("TROPIC-LOG-MIB", "tnWarningAlarmLogObjectID"),
        ("TROPIC-LOG-MIB", "tnWarningAlarmLogDescr"),
        ("TROPIC-LOG-MIB", "tnWarningAlarmLogData"),
        ("TROPIC-LOG-MIB", "tnWarningAlarmLogServiceAffecting"),
        ("TROPIC-LOG-MIB", "tnWarningAlarmLogSlotProgrammedType"),
        ("TROPIC-LOG-MIB", "tnWarningAlarmLogEntityType"),
        ("TROPIC-LOG-MIB", "tnWarningAlarmLogCondition"))
)
if mibBuilder.loadTexts:
    tnWarningAlarmLogGroup.setStatus("current")

tnPerSyncObjectAlarmCategoryConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 18)
)
tnPerSyncObjectAlarmCategoryConfigGroup.setObjects(
      *(("TROPIC-LOG-MIB", "tnPerSyncObjectAlarmCategory"),
        ("TROPIC-LOG-MIB", "tnPerSyncObjectAlarmEntityTypeCategory"),
        ("TROPIC-LOG-MIB", "tnPerSyncObjectAlarmDefaultCategory"))
)
if mibBuilder.loadTexts:
    tnPerSyncObjectAlarmCategoryConfigGroup.setStatus("current")

tnPerVtsObjectAlarmCategoryConfigScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 19)
)
tnPerVtsObjectAlarmCategoryConfigScalarsGroup.setObjects(
    ("TROPIC-LOG-MIB", "tnPerVtsObjectAlarmCategoryConfigAttributeTotal")
)
if mibBuilder.loadTexts:
    tnPerVtsObjectAlarmCategoryConfigScalarsGroup.setStatus("current")

tnPerVtsObjectAlarmCategoryConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 20)
)
tnPerVtsObjectAlarmCategoryConfigGroup.setObjects(
      *(("TROPIC-LOG-MIB", "tnPerVtsObjectAlarmCategory"),
        ("TROPIC-LOG-MIB", "tnPerVtsObjectAlarmEntityTypeCategory"),
        ("TROPIC-LOG-MIB", "tnPerVtsObjectAlarmDefaultCategory"))
)
if mibBuilder.loadTexts:
    tnPerVtsObjectAlarmCategoryConfigGroup.setStatus("current")

tnPerCcmObjectAlarmCategoryConfigScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 21)
)
tnPerCcmObjectAlarmCategoryConfigScalarsGroup.setObjects(
    ("TROPIC-LOG-MIB", "tnPerCcmObjectAlarmCategoryConfigAttributeTotal")
)
if mibBuilder.loadTexts:
    tnPerCcmObjectAlarmCategoryConfigScalarsGroup.setStatus("current")

tnPerCcmObjectAlarmCategoryConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 22)
)
tnPerCcmObjectAlarmCategoryConfigGroup.setObjects(
      *(("TROPIC-LOG-MIB", "tnPerCcmObjectAlarmCategory"),
        ("TROPIC-LOG-MIB", "tnPerCcmObjectAlarmEntityTypeCategory"),
        ("TROPIC-LOG-MIB", "tnPerCcmObjectAlarmDefaultCategory"))
)
if mibBuilder.loadTexts:
    tnPerCcmObjectAlarmCategoryConfigGroup.setStatus("current")

tnPerTcmObjectAlarmCategoryConfigScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 23)
)
tnPerTcmObjectAlarmCategoryConfigScalarsGroup.setObjects(
    ("TROPIC-LOG-MIB", "tnPerTcmObjectAlarmCategoryConfigAttributeTotal")
)
if mibBuilder.loadTexts:
    tnPerTcmObjectAlarmCategoryConfigScalarsGroup.setStatus("current")

tnPerTcmObjectAlarmCategoryConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 24)
)
tnPerTcmObjectAlarmCategoryConfigGroup.setObjects(
      *(("TROPIC-LOG-MIB", "tnPerTcmObjectAlarmCategory"),
        ("TROPIC-LOG-MIB", "tnPerTcmObjectAlarmEntityTypeCategory"),
        ("TROPIC-LOG-MIB", "tnPerTcmObjectAlarmDefaultCategory"))
)
if mibBuilder.loadTexts:
    tnPerTcmObjectAlarmCategoryConfigGroup.setStatus("current")

tnPerPtpObjectAlarmCategoryConfigScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 25)
)
tnPerPtpObjectAlarmCategoryConfigScalarsGroup.setObjects(
    ("TROPIC-LOG-MIB", "tnPerPtpObjectAlarmCategoryConfigAttributeTotal")
)
if mibBuilder.loadTexts:
    tnPerPtpObjectAlarmCategoryConfigScalarsGroup.setStatus("current")

tnPerPtpObjectAlarmCategoryConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 26)
)
tnPerPtpObjectAlarmCategoryConfigGroup.setObjects(
      *(("TROPIC-LOG-MIB", "tnPerPtpObjectAlarmCategory"),
        ("TROPIC-LOG-MIB", "tnPerPtpObjectAlarmEntityTypeCategory"),
        ("TROPIC-LOG-MIB", "tnPerPtpObjectAlarmDefaultCategory"))
)
if mibBuilder.loadTexts:
    tnPerPtpObjectAlarmCategoryConfigGroup.setStatus("current")

tnPerLagObjectAlarmCategoryConfigScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 27)
)
tnPerLagObjectAlarmCategoryConfigScalarsGroup.setObjects(
    ("TROPIC-LOG-MIB", "tnPerLagObjectAlarmCategoryConfigAttributeTotal")
)
if mibBuilder.loadTexts:
    tnPerLagObjectAlarmCategoryConfigScalarsGroup.setStatus("current")

tnPerLagObjectAlarmCategoryConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 28)
)
tnPerLagObjectAlarmCategoryConfigGroup.setObjects(
      *(("TROPIC-LOG-MIB", "tnPerLagObjectAlarmCategory"),
        ("TROPIC-LOG-MIB", "tnPerLagObjectAlarmEntityTypeCategory"),
        ("TROPIC-LOG-MIB", "tnPerLagObjectAlarmDefaultCategory"))
)
if mibBuilder.loadTexts:
    tnPerLagObjectAlarmCategoryConfigGroup.setStatus("current")

tnPerOtnObjectAlarmCategoryConfigScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 29)
)
tnPerOtnObjectAlarmCategoryConfigScalarsGroup.setObjects(
    ("TROPIC-LOG-MIB", "tnPerOtnObjectAlarmCategoryConfigAttributeTotal")
)
if mibBuilder.loadTexts:
    tnPerOtnObjectAlarmCategoryConfigScalarsGroup.setStatus("deprecated")

tnPerOtnObjectAlarmCategoryConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 30)
)
tnPerOtnObjectAlarmCategoryConfigGroup.setObjects(
      *(("TROPIC-LOG-MIB", "tnPerOtnObjectAlarmCategory"),
        ("TROPIC-LOG-MIB", "tnPerOtnObjectAlarmEntityTypeCategory"),
        ("TROPIC-LOG-MIB", "tnPerOtnObjectAlarmDefaultCategory"))
)
if mibBuilder.loadTexts:
    tnPerOtnObjectAlarmCategoryConfigGroup.setStatus("deprecated")

tnPerSrSvcObjectAlarmCategoryConfigScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 31)
)
tnPerSrSvcObjectAlarmCategoryConfigScalarsGroup.setObjects(
    ("TROPIC-LOG-MIB", "tnPerSrSvcObjectAlarmCategoryConfigAttributeTotal")
)
if mibBuilder.loadTexts:
    tnPerSrSvcObjectAlarmCategoryConfigScalarsGroup.setStatus("current")

tnPerSrSvcObjectAlarmCategoryConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 32)
)
tnPerSrSvcObjectAlarmCategoryConfigGroup.setObjects(
      *(("TROPIC-LOG-MIB", "tnPerSrSvcObjectAlarmCategory"),
        ("TROPIC-LOG-MIB", "tnPerSrSvcObjectAlarmEntityTypeCategory"),
        ("TROPIC-LOG-MIB", "tnPerSrSvcObjectAlarmDefaultCategory"))
)
if mibBuilder.loadTexts:
    tnPerSrSvcObjectAlarmCategoryConfigGroup.setStatus("current")

tnPerSrSapObjectAlarmCategoryConfigScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 33)
)
tnPerSrSapObjectAlarmCategoryConfigScalarsGroup.setObjects(
    ("TROPIC-LOG-MIB", "tnPerSrSapObjectAlarmCategoryConfigAttributeTotal")
)
if mibBuilder.loadTexts:
    tnPerSrSapObjectAlarmCategoryConfigScalarsGroup.setStatus("current")

tnPerSrSapObjectAlarmCategoryConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 34)
)
tnPerSrSapObjectAlarmCategoryConfigGroup.setObjects(
      *(("TROPIC-LOG-MIB", "tnPerSrSapObjectAlarmCategory"),
        ("TROPIC-LOG-MIB", "tnPerSrSapObjectAlarmEntityTypeCategory"),
        ("TROPIC-LOG-MIB", "tnPerSrSapObjectAlarmDefaultCategory"))
)
if mibBuilder.loadTexts:
    tnPerSrSapObjectAlarmCategoryConfigGroup.setStatus("current")

tnPerSrErpObjectAlarmCategoryConfigScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 35)
)
tnPerSrErpObjectAlarmCategoryConfigScalarsGroup.setObjects(
    ("TROPIC-LOG-MIB", "tnPerSrErpObjectAlarmCategoryConfigAttributeTotal")
)
if mibBuilder.loadTexts:
    tnPerSrErpObjectAlarmCategoryConfigScalarsGroup.setStatus("current")

tnPerSrErpObjectAlarmCategoryConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 36)
)
tnPerSrErpObjectAlarmCategoryConfigGroup.setObjects(
      *(("TROPIC-LOG-MIB", "tnPerSrErpObjectAlarmCategory"),
        ("TROPIC-LOG-MIB", "tnPerSrErpObjectAlarmEntityTypeCategory"),
        ("TROPIC-LOG-MIB", "tnPerSrErpObjectAlarmDefaultCategory"))
)
if mibBuilder.loadTexts:
    tnPerSrErpObjectAlarmCategoryConfigGroup.setStatus("current")

tnPerSrMepObjectAlarmCategoryConfigScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 37)
)
tnPerSrMepObjectAlarmCategoryConfigScalarsGroup.setObjects(
    ("TROPIC-LOG-MIB", "tnPerSrMepObjectAlarmCategoryConfigAttributeTotal")
)
if mibBuilder.loadTexts:
    tnPerSrMepObjectAlarmCategoryConfigScalarsGroup.setStatus("current")

tnPerSrMepObjectAlarmCategoryConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 38)
)
tnPerSrMepObjectAlarmCategoryConfigGroup.setObjects(
      *(("TROPIC-LOG-MIB", "tnPerSrMepObjectAlarmCategory"),
        ("TROPIC-LOG-MIB", "tnPerSrMepObjectAlarmEntityTypeCategory"),
        ("TROPIC-LOG-MIB", "tnPerSrMepObjectAlarmDefaultCategory"))
)
if mibBuilder.loadTexts:
    tnPerSrMepObjectAlarmCategoryConfigGroup.setStatus("current")

tnPerSrOamTestObjectAlarmCategoryConfigScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 39)
)
tnPerSrOamTestObjectAlarmCategoryConfigScalarsGroup.setObjects(
    ("TROPIC-LOG-MIB", "tnPerSrOamTestObjectAlarmCategoryConfigAttributeTotal")
)
if mibBuilder.loadTexts:
    tnPerSrOamTestObjectAlarmCategoryConfigScalarsGroup.setStatus("current")

tnPerSrOamTestObjectAlarmCategoryConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 40)
)
tnPerSrOamTestObjectAlarmCategoryConfigGroup.setObjects(
      *(("TROPIC-LOG-MIB", "tnPerSrOamTestObjectAlarmCategory"),
        ("TROPIC-LOG-MIB", "tnPerSrOamTestObjectAlarmEntityTypeCategory"),
        ("TROPIC-LOG-MIB", "tnPerSrOamTestObjectAlarmDefaultCategory"))
)
if mibBuilder.loadTexts:
    tnPerSrOamTestObjectAlarmCategoryConfigGroup.setStatus("current")

tnPerRmdObjectAlarmCategoryConfigScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 41)
)
tnPerRmdObjectAlarmCategoryConfigScalarsGroup.setObjects(
    ("TROPIC-LOG-MIB", "tnPerRmdObjectAlarmCategoryConfigAttributeTotal")
)
if mibBuilder.loadTexts:
    tnPerRmdObjectAlarmCategoryConfigScalarsGroup.setStatus("current")

tnPerRmdObjectAlarmCategoryConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 42)
)
tnPerRmdObjectAlarmCategoryConfigGroup.setObjects(
      *(("TROPIC-LOG-MIB", "tnPerRmdObjectAlarmCategory"),
        ("TROPIC-LOG-MIB", "tnPerRmdObjectAlarmEntityTypeCategory"),
        ("TROPIC-LOG-MIB", "tnPerRmdObjectAlarmDefaultCategory"))
)
if mibBuilder.loadTexts:
    tnPerRmdObjectAlarmCategoryConfigGroup.setStatus("current")

tnPerRmdMepObjectAlarmCategoryConfigScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 43)
)
tnPerRmdMepObjectAlarmCategoryConfigScalarsGroup.setObjects(
    ("TROPIC-LOG-MIB", "tnPerRmdMepObjectAlarmCategoryConfigAttributeTotal")
)
if mibBuilder.loadTexts:
    tnPerRmdMepObjectAlarmCategoryConfigScalarsGroup.setStatus("current")

tnPerRmdMepObjectAlarmCategoryConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 44)
)
tnPerRmdMepObjectAlarmCategoryConfigGroup.setObjects(
      *(("TROPIC-LOG-MIB", "tnPerRmdMepObjectAlarmCategory"),
        ("TROPIC-LOG-MIB", "tnPerRmdMepObjectAlarmEntityTypeCategory"),
        ("TROPIC-LOG-MIB", "tnPerRmdMepObjectAlarmDefaultCategory"))
)
if mibBuilder.loadTexts:
    tnPerRmdMepObjectAlarmCategoryConfigGroup.setStatus("current")

tnPerRmdIfObjectAlarmCategoryConfigScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 45)
)
tnPerRmdIfObjectAlarmCategoryConfigScalarsGroup.setObjects(
    ("TROPIC-LOG-MIB", "tnPerRmdIfObjectAlarmCategoryConfigAttributeTotal")
)
if mibBuilder.loadTexts:
    tnPerRmdIfObjectAlarmCategoryConfigScalarsGroup.setStatus("current")

tnPerRmdIfObjectAlarmCategoryConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 46)
)
tnPerRmdIfObjectAlarmCategoryConfigGroup.setObjects(
      *(("TROPIC-LOG-MIB", "tnPerRmdIfObjectAlarmCategory"),
        ("TROPIC-LOG-MIB", "tnPerRmdIfObjectAlarmEntityTypeCategory"),
        ("TROPIC-LOG-MIB", "tnPerRmdIfObjectAlarmDefaultCategory"))
)
if mibBuilder.loadTexts:
    tnPerRmdIfObjectAlarmCategoryConfigGroup.setStatus("current")

tnPerRmdIfMauObjectAlarmCategoryConfigScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 47)
)
tnPerRmdIfMauObjectAlarmCategoryConfigScalarsGroup.setObjects(
    ("TROPIC-LOG-MIB", "tnPerRmdIfMauObjectAlarmCategoryConfigAttributeTotal")
)
if mibBuilder.loadTexts:
    tnPerRmdIfMauObjectAlarmCategoryConfigScalarsGroup.setStatus("current")

tnPerRmdIfMauObjectAlarmCategoryConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 48)
)
tnPerRmdIfMauObjectAlarmCategoryConfigGroup.setObjects(
      *(("TROPIC-LOG-MIB", "tnPerRmdIfMauObjectAlarmCategory"),
        ("TROPIC-LOG-MIB", "tnPerRmdIfMauObjectAlarmEntityTypeCategory"),
        ("TROPIC-LOG-MIB", "tnPerRmdIfMauObjectAlarmDefaultCategory"))
)
if mibBuilder.loadTexts:
    tnPerRmdIfMauObjectAlarmCategoryConfigGroup.setStatus("current")

tnPerRmdCesChannelObjectAlarmCategoryConfigScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 49)
)
tnPerRmdCesChannelObjectAlarmCategoryConfigScalarsGroup.setObjects(
    ("TROPIC-LOG-MIB", "tnPerRmdCesChannelObjectAlarmCategoryConfigAttributeTotal")
)
if mibBuilder.loadTexts:
    tnPerRmdCesChannelObjectAlarmCategoryConfigScalarsGroup.setStatus("current")

tnPerRmdCesChannelObjectAlarmCategoryConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 50)
)
tnPerRmdCesChannelObjectAlarmCategoryConfigGroup.setObjects(
      *(("TROPIC-LOG-MIB", "tnPerRmdCesChannelObjectAlarmCategory"),
        ("TROPIC-LOG-MIB", "tnPerRmdCesChannelObjectAlarmEntityTypeCategory"),
        ("TROPIC-LOG-MIB", "tnPerRmdCesChannelObjectAlarmDefaultCategory"))
)
if mibBuilder.loadTexts:
    tnPerRmdCesChannelObjectAlarmCategoryConfigGroup.setStatus("current")

tnPerOthObjectAlarmCategoryConfigScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 51)
)
tnPerOthObjectAlarmCategoryConfigScalarsGroup.setObjects(
    ("TROPIC-LOG-MIB", "tnPerOthObjectAlarmCategoryConfigAttributeTotal")
)
if mibBuilder.loadTexts:
    tnPerOthObjectAlarmCategoryConfigScalarsGroup.setStatus("current")

tnPerOthObjectAlarmCategoryConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 52)
)
tnPerOthObjectAlarmCategoryConfigGroup.setObjects(
      *(("TROPIC-LOG-MIB", "tnPerOthObjectAlarmCategory"),
        ("TROPIC-LOG-MIB", "tnPerOthObjectAlarmEntityTypeCategory"),
        ("TROPIC-LOG-MIB", "tnPerOthObjectAlarmDefaultCategory"))
)
if mibBuilder.loadTexts:
    tnPerOthObjectAlarmCategoryConfigGroup.setStatus("current")

tnPerRmdNimObjectAlarmCategoryConfigScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 53)
)
tnPerRmdNimObjectAlarmCategoryConfigScalarsGroup.setObjects(
    ("TROPIC-LOG-MIB", "tnPerRmdNimObjectAlarmCategoryConfigAttributeTotal")
)
if mibBuilder.loadTexts:
    tnPerRmdNimObjectAlarmCategoryConfigScalarsGroup.setStatus("current")

tnPerRmdNimObjectAlarmCategoryConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 1, 54)
)
tnPerRmdNimObjectAlarmCategoryConfigGroup.setObjects(
      *(("TROPIC-LOG-MIB", "tnPerRmdNimObjectAlarmCategory"),
        ("TROPIC-LOG-MIB", "tnPerRmdNimObjectAlarmEntityTypeCategory"),
        ("TROPIC-LOG-MIB", "tnPerRmdNimObjectAlarmDefaultCategory"))
)
if mibBuilder.loadTexts:
    tnPerRmdNimObjectAlarmCategoryConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnLogCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 3, 1, 2, 1)
)
tnLogCompliance.setObjects(
      *(("TROPIC-LOG-MIB", "tnLogScalarsGroup"),
        ("TROPIC-LOG-MIB", "tnCriticalAlarmLogGroup"),
        ("TROPIC-LOG-MIB", "tnMajorAlarmLogGroup"),
        ("TROPIC-LOG-MIB", "tnMinorAlarmLogGroup"),
        ("TROPIC-LOG-MIB", "tnStateChangeLogGroup"),
        ("TROPIC-LOG-MIB", "tnUserActionLogGroup"),
        ("TROPIC-LOG-MIB", "tnGeneralEventLogGroup"),
        ("TROPIC-LOG-MIB", "tnLogGroup"),
        ("TROPIC-LOG-MIB", "tnActiveAlarmGroup"),
        ("TROPIC-LOG-MIB", "tnPersistentLogGroup"),
        ("TROPIC-LOG-MIB", "tnActiveOrMaskedAlarmGroup"),
        ("TROPIC-LOG-MIB", "tnNotAlarmedLogGroup"),
        ("TROPIC-LOG-MIB", "tnPerObjectAlarmCategoryConfigGroup"),
        ("TROPIC-LOG-MIB", "tnAlarmProfileConfigGroup"),
        ("TROPIC-LOG-MIB", "tnSecurityLogGroup"),
        ("TROPIC-LOG-MIB", "tnWarningAlarmLogGroup"),
        ("TROPIC-LOG-MIB", "tnPerSyncObjectAlarmCategoryConfigGroup"),
        ("TROPIC-LOG-MIB", "tnPerVtsObjectAlarmCategoryConfigScalarsGroup"),
        ("TROPIC-LOG-MIB", "tnPerVtsObjectAlarmCategoryConfigGroup"),
        ("TROPIC-LOG-MIB", "tnPerCcmObjectAlarmCategoryConfigScalarsGroup"),
        ("TROPIC-LOG-MIB", "tnPerCcmObjectAlarmCategoryConfigGroup"),
        ("TROPIC-LOG-MIB", "tnPerTcmObjectAlarmCategoryConfigScalarsGroup"),
        ("TROPIC-LOG-MIB", "tnPerTcmObjectAlarmCategoryConfigGroup"),
        ("TROPIC-LOG-MIB", "tnPerPtpObjectAlarmCategoryConfigScalarsGroup"),
        ("TROPIC-LOG-MIB", "tnPerPtpObjectAlarmCategoryConfigGroup"),
        ("TROPIC-LOG-MIB", "tnPerLagObjectAlarmCategoryConfigScalarsGroup"),
        ("TROPIC-LOG-MIB", "tnPerLagObjectAlarmCategoryConfigGroup"),
        ("TROPIC-LOG-MIB", "tnPerOtnObjectAlarmCategoryConfigScalarsGroup"),
        ("TROPIC-LOG-MIB", "tnPerOtnObjectAlarmCategoryConfigGroup"),
        ("TROPIC-LOG-MIB", "tnPerSrSvcObjectAlarmCategoryConfigScalarsGroup"),
        ("TROPIC-LOG-MIB", "tnPerSrSvcObjectAlarmCategoryConfigGroup"),
        ("TROPIC-LOG-MIB", "tnPerSrSapObjectAlarmCategoryConfigScalarsGroup"),
        ("TROPIC-LOG-MIB", "tnPerSrSapObjectAlarmCategoryConfigGroup"),
        ("TROPIC-LOG-MIB", "tnPerSrErpObjectAlarmCategoryConfigScalarsGroup"),
        ("TROPIC-LOG-MIB", "tnPerSrErpObjectAlarmCategoryConfigGroup"),
        ("TROPIC-LOG-MIB", "tnPerSrMepObjectAlarmCategoryConfigScalarsGroup"),
        ("TROPIC-LOG-MIB", "tnPerSrMepObjectAlarmCategoryConfigGroup"),
        ("TROPIC-LOG-MIB", "tnPerSrOamTestObjectAlarmCategoryConfigScalarsGroup"),
        ("TROPIC-LOG-MIB", "tnPerSrOamTestObjectAlarmCategoryConfigGroup"),
        ("TROPIC-LOG-MIB", "tnPerRmdObjectAlarmCategoryConfigScalarsGroup"),
        ("TROPIC-LOG-MIB", "tnPerRmdObjectAlarmCategoryConfigGroup"),
        ("TROPIC-LOG-MIB", "tnPerRmdMepObjectAlarmCategoryConfigScalarsGroup"),
        ("TROPIC-LOG-MIB", "tnPerRmdMepObjectAlarmCategoryConfigGroup"),
        ("TROPIC-LOG-MIB", "tnPerRmdIfObjectAlarmCategoryConfigScalarsGroup"),
        ("TROPIC-LOG-MIB", "tnPerRmdIfObjectAlarmCategoryConfigGroup"),
        ("TROPIC-LOG-MIB", "tnPerRmdIfMauObjectAlarmCategoryConfigScalarsGroup"),
        ("TROPIC-LOG-MIB", "tnPerRmdIfMauObjectAlarmCategoryConfigGroup"),
        ("TROPIC-LOG-MIB", "tnPerRmdCesChannelObjectAlarmCategoryConfigScalarsGroup"),
        ("TROPIC-LOG-MIB", "tnPerRmdCesChannelObjectAlarmCategoryConfigGroup"),
        ("TROPIC-LOG-MIB", "tnPerOthObjectAlarmCategoryConfigScalarsGroup"),
        ("TROPIC-LOG-MIB", "tnPerOthObjectAlarmCategoryConfigGroup"),
        ("TROPIC-LOG-MIB", "tnPerRmdNimObjectAlarmCategoryConfigScalarsGroup"),
        ("TROPIC-LOG-MIB", "tnPerRmdNimObjectAlarmCategoryConfigGroup"))
)
if mibBuilder.loadTexts:
    tnLogCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-LOG-MIB",
    **{"AluWdmAlarmCategoryDirection": AluWdmAlarmCategoryDirection,
       "tnLogMIBModule": tnLogMIBModule,
       "tnLogConf": tnLogConf,
       "tnLogGroups": tnLogGroups,
       "tnLogScalarsGroup": tnLogScalarsGroup,
       "tnCriticalAlarmLogGroup": tnCriticalAlarmLogGroup,
       "tnMajorAlarmLogGroup": tnMajorAlarmLogGroup,
       "tnMinorAlarmLogGroup": tnMinorAlarmLogGroup,
       "tnStateChangeLogGroup": tnStateChangeLogGroup,
       "tnUserActionLogGroup": tnUserActionLogGroup,
       "tnGeneralEventLogGroup": tnGeneralEventLogGroup,
       "tnLogGroup": tnLogGroup,
       "tnActiveAlarmGroup": tnActiveAlarmGroup,
       "tnPersistentLogGroup": tnPersistentLogGroup,
       "tnActiveOrMaskedAlarmGroup": tnActiveOrMaskedAlarmGroup,
       "tnNotAlarmedLogGroup": tnNotAlarmedLogGroup,
       "tnPerObjectAlarmCategoryConfigGroup": tnPerObjectAlarmCategoryConfigGroup,
       "tnAlarmProfileConfigGroup": tnAlarmProfileConfigGroup,
       "tnSecurityLogGroup": tnSecurityLogGroup,
       "tnWarningAlarmLogGroup": tnWarningAlarmLogGroup,
       "tnPerSyncObjectAlarmCategoryConfigGroup": tnPerSyncObjectAlarmCategoryConfigGroup,
       "tnPerVtsObjectAlarmCategoryConfigScalarsGroup": tnPerVtsObjectAlarmCategoryConfigScalarsGroup,
       "tnPerVtsObjectAlarmCategoryConfigGroup": tnPerVtsObjectAlarmCategoryConfigGroup,
       "tnPerCcmObjectAlarmCategoryConfigScalarsGroup": tnPerCcmObjectAlarmCategoryConfigScalarsGroup,
       "tnPerCcmObjectAlarmCategoryConfigGroup": tnPerCcmObjectAlarmCategoryConfigGroup,
       "tnPerTcmObjectAlarmCategoryConfigScalarsGroup": tnPerTcmObjectAlarmCategoryConfigScalarsGroup,
       "tnPerTcmObjectAlarmCategoryConfigGroup": tnPerTcmObjectAlarmCategoryConfigGroup,
       "tnPerPtpObjectAlarmCategoryConfigScalarsGroup": tnPerPtpObjectAlarmCategoryConfigScalarsGroup,
       "tnPerPtpObjectAlarmCategoryConfigGroup": tnPerPtpObjectAlarmCategoryConfigGroup,
       "tnPerLagObjectAlarmCategoryConfigScalarsGroup": tnPerLagObjectAlarmCategoryConfigScalarsGroup,
       "tnPerLagObjectAlarmCategoryConfigGroup": tnPerLagObjectAlarmCategoryConfigGroup,
       "tnPerOtnObjectAlarmCategoryConfigScalarsGroup": tnPerOtnObjectAlarmCategoryConfigScalarsGroup,
       "tnPerOtnObjectAlarmCategoryConfigGroup": tnPerOtnObjectAlarmCategoryConfigGroup,
       "tnPerSrSvcObjectAlarmCategoryConfigScalarsGroup": tnPerSrSvcObjectAlarmCategoryConfigScalarsGroup,
       "tnPerSrSvcObjectAlarmCategoryConfigGroup": tnPerSrSvcObjectAlarmCategoryConfigGroup,
       "tnPerSrSapObjectAlarmCategoryConfigScalarsGroup": tnPerSrSapObjectAlarmCategoryConfigScalarsGroup,
       "tnPerSrSapObjectAlarmCategoryConfigGroup": tnPerSrSapObjectAlarmCategoryConfigGroup,
       "tnPerSrErpObjectAlarmCategoryConfigScalarsGroup": tnPerSrErpObjectAlarmCategoryConfigScalarsGroup,
       "tnPerSrErpObjectAlarmCategoryConfigGroup": tnPerSrErpObjectAlarmCategoryConfigGroup,
       "tnPerSrMepObjectAlarmCategoryConfigScalarsGroup": tnPerSrMepObjectAlarmCategoryConfigScalarsGroup,
       "tnPerSrMepObjectAlarmCategoryConfigGroup": tnPerSrMepObjectAlarmCategoryConfigGroup,
       "tnPerSrOamTestObjectAlarmCategoryConfigScalarsGroup": tnPerSrOamTestObjectAlarmCategoryConfigScalarsGroup,
       "tnPerSrOamTestObjectAlarmCategoryConfigGroup": tnPerSrOamTestObjectAlarmCategoryConfigGroup,
       "tnPerRmdObjectAlarmCategoryConfigScalarsGroup": tnPerRmdObjectAlarmCategoryConfigScalarsGroup,
       "tnPerRmdObjectAlarmCategoryConfigGroup": tnPerRmdObjectAlarmCategoryConfigGroup,
       "tnPerRmdMepObjectAlarmCategoryConfigScalarsGroup": tnPerRmdMepObjectAlarmCategoryConfigScalarsGroup,
       "tnPerRmdMepObjectAlarmCategoryConfigGroup": tnPerRmdMepObjectAlarmCategoryConfigGroup,
       "tnPerRmdIfObjectAlarmCategoryConfigScalarsGroup": tnPerRmdIfObjectAlarmCategoryConfigScalarsGroup,
       "tnPerRmdIfObjectAlarmCategoryConfigGroup": tnPerRmdIfObjectAlarmCategoryConfigGroup,
       "tnPerRmdIfMauObjectAlarmCategoryConfigScalarsGroup": tnPerRmdIfMauObjectAlarmCategoryConfigScalarsGroup,
       "tnPerRmdIfMauObjectAlarmCategoryConfigGroup": tnPerRmdIfMauObjectAlarmCategoryConfigGroup,
       "tnPerRmdCesChannelObjectAlarmCategoryConfigScalarsGroup": tnPerRmdCesChannelObjectAlarmCategoryConfigScalarsGroup,
       "tnPerRmdCesChannelObjectAlarmCategoryConfigGroup": tnPerRmdCesChannelObjectAlarmCategoryConfigGroup,
       "tnPerOthObjectAlarmCategoryConfigScalarsGroup": tnPerOthObjectAlarmCategoryConfigScalarsGroup,
       "tnPerOthObjectAlarmCategoryConfigGroup": tnPerOthObjectAlarmCategoryConfigGroup,
       "tnPerRmdNimObjectAlarmCategoryConfigScalarsGroup": tnPerRmdNimObjectAlarmCategoryConfigScalarsGroup,
       "tnPerRmdNimObjectAlarmCategoryConfigGroup": tnPerRmdNimObjectAlarmCategoryConfigGroup,
       "tnLogCompliances": tnLogCompliances,
       "tnLogCompliance": tnLogCompliance,
       "tnLogObjs": tnLogObjs,
       "tnLogs": tnLogs,
       "tnSystemLogs": tnSystemLogs,
       "tnUserActionLog": tnUserActionLog,
       "tnApplicationProcessStartFailureLog": tnApplicationProcessStartFailureLog,
       "tnDiscardedEventsLog": tnDiscardedEventsLog,
       "tnExceededSystemLimitLog": tnExceededSystemLimitLog,
       "tnInvalidDatabaseRecordLog": tnInvalidDatabaseRecordLog,
       "tnAlarmEventCategoryChangeEventidLog": tnAlarmEventCategoryChangeEventidLog,
       "tnProgrammedPortTypeChangeLog": tnProgrammedPortTypeChangeLog,
       "tnPtchgOkLog": tnPtchgOkLog,
       "tnPtchgUnknownPortTypeLog": tnPtchgUnknownPortTypeLog,
       "tnPtchgNoSlotCorrLog": tnPtchgNoSlotCorrLog,
       "tnPtchgNotAllowedLog": tnPtchgNotAllowedLog,
       "tnPtchgNoPortCorrLog": tnPtchgNoPortCorrLog,
       "tnDatabaseLogs": tnDatabaseLogs,
       "tnDatabaseConvertLog": tnDatabaseConvertLog,
       "tnDatabaseRestoreLog": tnDatabaseRestoreLog,
       "tnDatabaseClearPersistentRepositoryLog": tnDatabaseClearPersistentRepositoryLog,
       "tnDatabaseBackupFailedLog": tnDatabaseBackupFailedLog,
       "tnDatabaseRestoreFailedLog": tnDatabaseRestoreFailedLog,
       "tnDiagnosticsLogs": tnDiagnosticsLogs,
       "tnEquipmentLogs": tnEquipmentLogs,
       "tnSlotMonitorCardPulledLog": tnSlotMonitorCardPulledLog,
       "tnSlotMonitorCardInsertedLog": tnSlotMonitorCardInsertedLog,
       "tnI2CReadErrorLog": tnI2CReadErrorLog,
       "tnI2CWriteErrorLog": tnI2CWriteErrorLog,
       "tnSandiskATAReadErrorLog": tnSandiskATAReadErrorLog,
       "tnSandiskATAWriteErrorLog": tnSandiskATAWriteErrorLog,
       "tnAutoTopologyConfigFailedLog": tnAutoTopologyConfigFailedLog,
       "tnAutoTopologyConfigFailedROADMCardMissingLog": tnAutoTopologyConfigFailedROADMCardMissingLog,
       "tnAutoTopologyConfigFailedMateCADCardMissingLog": tnAutoTopologyConfigFailedMateCADCardMissingLog,
       "tnAutoTopologyConfigFailedPortAlreadyConnectedLog": tnAutoTopologyConfigFailedPortAlreadyConnectedLog,
       "tnAutoTopologyConfigFailedFarEndPortAlreadyConnectedLog": tnAutoTopologyConfigFailedFarEndPortAlreadyConnectedLog,
       "tnSoftwareDownloadingLogs": tnSoftwareDownloadingLogs,
       "tnSwdlResultLog": tnSwdlResultLog,
       "tnSwdlTransferStartedLog": tnSwdlTransferStartedLog,
       "tnSwdlTransferCompleteLog": tnSwdlTransferCompleteLog,
       "tnSwdlSwitchBankLog": tnSwdlSwitchBankLog,
       "tnSwdlSwitchActivityLog": tnSwdlSwitchActivityLog,
       "tnSwdlDatabaseBackupLog": tnSwdlDatabaseBackupLog,
       "tnSwdlDatabaseRestoreLog": tnSwdlDatabaseRestoreLog,
       "tnSwdlResetCardLog": tnSwdlResetCardLog,
       "tnSwdlDatabaseClearLog": tnSwdlDatabaseClearLog,
       "tnL1APSLogs": tnL1APSLogs,
       "tnProtectionSwitchToWorkingChannelLog": tnProtectionSwitchToWorkingChannelLog,
       "tnProtectionSwitchToProtectionChannelLog": tnProtectionSwitchToProtectionChannelLog,
       "tnProtectionSwitchFailedLog": tnProtectionSwitchFailedLog,
       "tnOspfLogs": tnOspfLogs,
       "tnOspfLsdbOverflowLog": tnOspfLsdbOverflowLog,
       "tnOchXcLogs": tnOchXcLogs,
       "tnExceededSystemLimitForConnectionsLog": tnExceededSystemLimitForConnectionsLog,
       "tnChangedWaveKeysOfConnectionLog": tnChangedWaveKeysOfConnectionLog,
       "tnPowerMgmtLogs": tnPowerMgmtLogs,
       "tnPowerMgmtAdjustStartedLog": tnPowerMgmtAdjustStartedLog,
       "tnPowerMgmtAdjustCompletedLog": tnPowerMgmtAdjustCompletedLog,
       "tnPowerControlReinitializedLog": tnPowerControlReinitializedLog,
       "tnPowerMgmtAutoAdjustRequestedLog": tnPowerMgmtAutoAdjustRequestedLog,
       "tnPowerMgmtCommissioningRequiredLog": tnPowerMgmtCommissioningRequiredLog,
       "tnPowerMgmtVectoredAddDropFailureLog": tnPowerMgmtVectoredAddDropFailureLog,
       "tnPowerMgmtTiltAdjustStartedLog": tnPowerMgmtTiltAdjustStartedLog,
       "tnPowerMgmtTiltAdjustCompleteLog": tnPowerMgmtTiltAdjustCompleteLog,
       "tnPowerMgmtTiltAdjustRequestLog": tnPowerMgmtTiltAdjustRequestLog,
       "tnPowerMgmtTiltAdjustRequestClearedLog": tnPowerMgmtTiltAdjustRequestClearedLog,
       "tnPowerMgmtExpressThruPathLossTooHighLog": tnPowerMgmtExpressThruPathLossTooHighLog,
       "tnLogBasics": tnLogBasics,
       "tnCriticalAlarmLogTotal": tnCriticalAlarmLogTotal,
       "tnMajorAlarmLogTotal": tnMajorAlarmLogTotal,
       "tnMinorAlarmLogTotal": tnMinorAlarmLogTotal,
       "tnStateChangeLogTotal": tnStateChangeLogTotal,
       "tnUserActionLogTotal": tnUserActionLogTotal,
       "tnGeneralEventLogTotal": tnGeneralEventLogTotal,
       "tnLogTotal": tnLogTotal,
       "tnActiveAlarmTotal": tnActiveAlarmTotal,
       "tnPersistentLogTotal": tnPersistentLogTotal,
       "tnActiveCriticalAlarmTotal": tnActiveCriticalAlarmTotal,
       "tnActiveMajorAlarmTotal": tnActiveMajorAlarmTotal,
       "tnActiveMinorAlarmTotal": tnActiveMinorAlarmTotal,
       "tnActiveOrMaskedAlarmTotal": tnActiveOrMaskedAlarmTotal,
       "tnNotAlarmedLogTotal": tnNotAlarmedLogTotal,
       "tnSecurityLogTotal": tnSecurityLogTotal,
       "tnWarningAlarmLogTotal": tnWarningAlarmLogTotal,
       "tnActiveWarningAlarmTotal": tnActiveWarningAlarmTotal,
       "tnLogQueues": tnLogQueues,
       "tnCriticalAlarmLogBufferTable": tnCriticalAlarmLogBufferTable,
       "tnCriticalAlarmLogBufferEntry": tnCriticalAlarmLogBufferEntry,
       "tnCriticalAlarmLogSerialNumber": tnCriticalAlarmLogSerialNumber,
       "tnCriticalAlarmLogType": tnCriticalAlarmLogType,
       "tnCriticalAlarmLogTime": tnCriticalAlarmLogTime,
       "tnCriticalAlarmLogObjectIDType": tnCriticalAlarmLogObjectIDType,
       "tnCriticalAlarmLogObjectID": tnCriticalAlarmLogObjectID,
       "tnCriticalAlarmLogDescr": tnCriticalAlarmLogDescr,
       "tnCriticalAlarmLogData": tnCriticalAlarmLogData,
       "tnCriticalAlarmLogServiceAffecting": tnCriticalAlarmLogServiceAffecting,
       "tnCriticalAlarmLogSlotProgrammedType": tnCriticalAlarmLogSlotProgrammedType,
       "tnCriticalAlarmLogEntityType": tnCriticalAlarmLogEntityType,
       "tnCriticalAlarmLogCondition": tnCriticalAlarmLogCondition,
       "tnMajorAlarmLogBufferTable": tnMajorAlarmLogBufferTable,
       "tnMajorAlarmLogBufferEntry": tnMajorAlarmLogBufferEntry,
       "tnMajorAlarmLogSerialNumber": tnMajorAlarmLogSerialNumber,
       "tnMajorAlarmLogType": tnMajorAlarmLogType,
       "tnMajorAlarmLogTime": tnMajorAlarmLogTime,
       "tnMajorAlarmLogObjectIDType": tnMajorAlarmLogObjectIDType,
       "tnMajorAlarmLogObjectID": tnMajorAlarmLogObjectID,
       "tnMajorAlarmLogDescr": tnMajorAlarmLogDescr,
       "tnMajorAlarmLogData": tnMajorAlarmLogData,
       "tnMajorAlarmLogServiceAffecting": tnMajorAlarmLogServiceAffecting,
       "tnMajorAlarmLogSlotProgrammedType": tnMajorAlarmLogSlotProgrammedType,
       "tnMajorAlarmLogEntityType": tnMajorAlarmLogEntityType,
       "tnMajorAlarmLogCondition": tnMajorAlarmLogCondition,
       "tnMinorAlarmLogBufferTable": tnMinorAlarmLogBufferTable,
       "tnMinorAlarmLogBufferEntry": tnMinorAlarmLogBufferEntry,
       "tnMinorAlarmLogSerialNumber": tnMinorAlarmLogSerialNumber,
       "tnMinorAlarmLogType": tnMinorAlarmLogType,
       "tnMinorAlarmLogTime": tnMinorAlarmLogTime,
       "tnMinorAlarmLogObjectIDType": tnMinorAlarmLogObjectIDType,
       "tnMinorAlarmLogObjectID": tnMinorAlarmLogObjectID,
       "tnMinorAlarmLogDescr": tnMinorAlarmLogDescr,
       "tnMinorAlarmLogData": tnMinorAlarmLogData,
       "tnMinorAlarmLogServiceAffecting": tnMinorAlarmLogServiceAffecting,
       "tnMinorAlarmLogSlotProgrammedType": tnMinorAlarmLogSlotProgrammedType,
       "tnMinorAlarmLogEntityType": tnMinorAlarmLogEntityType,
       "tnMinorAlarmLogCondition": tnMinorAlarmLogCondition,
       "tnStateChangeLogBufferTable": tnStateChangeLogBufferTable,
       "tnStateChangeLogBufferEntry": tnStateChangeLogBufferEntry,
       "tnStateChangeLogSerialNumber": tnStateChangeLogSerialNumber,
       "tnStateChangeLogType": tnStateChangeLogType,
       "tnStateChangeLogTime": tnStateChangeLogTime,
       "tnStateChangeLogObjectIDType": tnStateChangeLogObjectIDType,
       "tnStateChangeLogObjectID": tnStateChangeLogObjectID,
       "tnStateChangeLogDescr": tnStateChangeLogDescr,
       "tnStateChangeLogData": tnStateChangeLogData,
       "tnStateChangeLogSlotProgrammedType": tnStateChangeLogSlotProgrammedType,
       "tnUserActionLogBufferTable": tnUserActionLogBufferTable,
       "tnUserActionLogBufferEntry": tnUserActionLogBufferEntry,
       "tnUserActionLogSerialNumber": tnUserActionLogSerialNumber,
       "tnUserActionLogType": tnUserActionLogType,
       "tnUserActionLogTime": tnUserActionLogTime,
       "tnUserActionLogObjectIDType": tnUserActionLogObjectIDType,
       "tnUserActionLogObjectID": tnUserActionLogObjectID,
       "tnUserActionLogDescr": tnUserActionLogDescr,
       "tnUserActionLogChangedObject": tnUserActionLogChangedObject,
       "tnUserActionLogData": tnUserActionLogData,
       "tnGeneralEventLogBufferTable": tnGeneralEventLogBufferTable,
       "tnGeneralEventLogBufferEntry": tnGeneralEventLogBufferEntry,
       "tnGeneralEventLogSerialNumber": tnGeneralEventLogSerialNumber,
       "tnGeneralEventLogType": tnGeneralEventLogType,
       "tnGeneralEventLogTime": tnGeneralEventLogTime,
       "tnGeneralEventLogObjectIDType": tnGeneralEventLogObjectIDType,
       "tnGeneralEventLogObjectID": tnGeneralEventLogObjectID,
       "tnGeneralEventLogDescr": tnGeneralEventLogDescr,
       "tnGeneralEventLogChangedObject": tnGeneralEventLogChangedObject,
       "tnGeneralEventLogData": tnGeneralEventLogData,
       "tnGeneralEventLogSlotProgrammedType": tnGeneralEventLogSlotProgrammedType,
       "tnLogBufferTable": tnLogBufferTable,
       "tnLogBufferEntry": tnLogBufferEntry,
       "tnLogSerialNumber": tnLogSerialNumber,
       "tnLogType": tnLogType,
       "tnLogTime": tnLogTime,
       "tnLogObjectIDType": tnLogObjectIDType,
       "tnLogObjectID": tnLogObjectID,
       "tnLogCategory": tnLogCategory,
       "tnLogDescr": tnLogDescr,
       "tnLogChangedObject": tnLogChangedObject,
       "tnLogData": tnLogData,
       "tnLogServiceAffecting": tnLogServiceAffecting,
       "tnLogSlotProgrammedType": tnLogSlotProgrammedType,
       "tnLogEntityType": tnLogEntityType,
       "tnLogCondition": tnLogCondition,
       "tnActiveAlarmTable": tnActiveAlarmTable,
       "tnActiveAlarmEntry": tnActiveAlarmEntry,
       "tnActiveAlarmSerialNumber": tnActiveAlarmSerialNumber,
       "tnActiveAlarmType": tnActiveAlarmType,
       "tnActiveAlarmTime": tnActiveAlarmTime,
       "tnActiveAlarmObjectIDType": tnActiveAlarmObjectIDType,
       "tnActiveAlarmObjectID": tnActiveAlarmObjectID,
       "tnActiveAlarmCategory": tnActiveAlarmCategory,
       "tnActiveAlarmDescr": tnActiveAlarmDescr,
       "tnActiveAlarmData": tnActiveAlarmData,
       "tnActiveAlarmServiceAffecting": tnActiveAlarmServiceAffecting,
       "tnActiveAlarmSlotProgrammedType": tnActiveAlarmSlotProgrammedType,
       "tnActiveAlarmEntityType": tnActiveAlarmEntityType,
       "tnActiveAlarmCondition": tnActiveAlarmCondition,
       "tnPersistentLogBufferTable": tnPersistentLogBufferTable,
       "tnPersistentLogBufferEntry": tnPersistentLogBufferEntry,
       "tnPersistentLogSerialNumber": tnPersistentLogSerialNumber,
       "tnPersistentLogType": tnPersistentLogType,
       "tnPersistentLogTime": tnPersistentLogTime,
       "tnPersistentLogObjectIDType": tnPersistentLogObjectIDType,
       "tnPersistentLogObjectID": tnPersistentLogObjectID,
       "tnPersistentLogCategory": tnPersistentLogCategory,
       "tnPersistentLogDescr": tnPersistentLogDescr,
       "tnPersistentLogChangedObject": tnPersistentLogChangedObject,
       "tnPersistentLogData": tnPersistentLogData,
       "tnPersistentLogServiceAffecting": tnPersistentLogServiceAffecting,
       "tnPersistentLogSlotProgrammedType": tnPersistentLogSlotProgrammedType,
       "tnActiveOrMaskedAlarmTable": tnActiveOrMaskedAlarmTable,
       "tnActiveOrMaskedAlarmEntry": tnActiveOrMaskedAlarmEntry,
       "tnActiveOrMaskedAlarmSerialNumber": tnActiveOrMaskedAlarmSerialNumber,
       "tnActiveOrMaskedAlarmType": tnActiveOrMaskedAlarmType,
       "tnActiveOrMaskedAlarmTime": tnActiveOrMaskedAlarmTime,
       "tnActiveOrMaskedAlarmObjectIDType": tnActiveOrMaskedAlarmObjectIDType,
       "tnActiveOrMaskedAlarmObjectID": tnActiveOrMaskedAlarmObjectID,
       "tnActiveOrMaskedAlarmCategory": tnActiveOrMaskedAlarmCategory,
       "tnActiveOrMaskedAlarmDescr": tnActiveOrMaskedAlarmDescr,
       "tnActiveOrMaskedAlarmData": tnActiveOrMaskedAlarmData,
       "tnActiveOrMaskedAlarmServiceAffecting": tnActiveOrMaskedAlarmServiceAffecting,
       "tnActiveOrMaskedAlarmSlotProgrammedType": tnActiveOrMaskedAlarmSlotProgrammedType,
       "tnActiveOrMaskedAlarmIsMasked": tnActiveOrMaskedAlarmIsMasked,
       "tnActiveOrMaskedAlarmEntityType": tnActiveOrMaskedAlarmEntityType,
       "tnActiveOrMaskedAlarmCondition": tnActiveOrMaskedAlarmCondition,
       "tnNotAlarmedLogBufferTable": tnNotAlarmedLogBufferTable,
       "tnNotAlarmedLogBufferEntry": tnNotAlarmedLogBufferEntry,
       "tnNotAlarmedLogSerialNumber": tnNotAlarmedLogSerialNumber,
       "tnNotAlarmedLogType": tnNotAlarmedLogType,
       "tnNotAlarmedLogTime": tnNotAlarmedLogTime,
       "tnNotAlarmedLogObjectIDType": tnNotAlarmedLogObjectIDType,
       "tnNotAlarmedLogObjectID": tnNotAlarmedLogObjectID,
       "tnNotAlarmedLogDescr": tnNotAlarmedLogDescr,
       "tnNotAlarmedLogData": tnNotAlarmedLogData,
       "tnNotAlarmedLogServiceAffecting": tnNotAlarmedLogServiceAffecting,
       "tnNotAlarmedLogSlotProgrammedType": tnNotAlarmedLogSlotProgrammedType,
       "tnNotAlarmedLogEntityType": tnNotAlarmedLogEntityType,
       "tnNotAlarmedLogCondition": tnNotAlarmedLogCondition,
       "tnSecurityLogBufferTable": tnSecurityLogBufferTable,
       "tnSecurityLogBufferEntry": tnSecurityLogBufferEntry,
       "tnSecurityLogSerialNumber": tnSecurityLogSerialNumber,
       "tnSecurityLogType": tnSecurityLogType,
       "tnSecurityLogTime": tnSecurityLogTime,
       "tnSecurityLogObjectIDType": tnSecurityLogObjectIDType,
       "tnSecurityLogObjectID": tnSecurityLogObjectID,
       "tnSecurityLogDescr": tnSecurityLogDescr,
       "tnSecurityLogData": tnSecurityLogData,
       "tnSecurityLogUserID": tnSecurityLogUserID,
       "tnSecurityLogUserSessionNumber": tnSecurityLogUserSessionNumber,
       "tnSecurityLogHeaderType": tnSecurityLogHeaderType,
       "tnSecurityLogUserPrivilege": tnSecurityLogUserPrivilege,
       "tnSecurityLogUserDestinationAddress": tnSecurityLogUserDestinationAddress,
       "tnSecurityLogResult": tnSecurityLogResult,
       "tnWarningAlarmLogBufferTable": tnWarningAlarmLogBufferTable,
       "tnWarningAlarmLogBufferEntry": tnWarningAlarmLogBufferEntry,
       "tnWarningAlarmLogSerialNumber": tnWarningAlarmLogSerialNumber,
       "tnWarningAlarmLogType": tnWarningAlarmLogType,
       "tnWarningAlarmLogTime": tnWarningAlarmLogTime,
       "tnWarningAlarmLogObjectIDType": tnWarningAlarmLogObjectIDType,
       "tnWarningAlarmLogObjectID": tnWarningAlarmLogObjectID,
       "tnWarningAlarmLogDescr": tnWarningAlarmLogDescr,
       "tnWarningAlarmLogData": tnWarningAlarmLogData,
       "tnWarningAlarmLogServiceAffecting": tnWarningAlarmLogServiceAffecting,
       "tnWarningAlarmLogSlotProgrammedType": tnWarningAlarmLogSlotProgrammedType,
       "tnWarningAlarmLogEntityType": tnWarningAlarmLogEntityType,
       "tnWarningAlarmLogCondition": tnWarningAlarmLogCondition,
       "tnLogAlarmCategoryConfig": tnLogAlarmCategoryConfig,
       "tnPerObjectAlarmCategoryConfigTable": tnPerObjectAlarmCategoryConfigTable,
       "tnPerObjectAlarmCategoryConfigEntry": tnPerObjectAlarmCategoryConfigEntry,
       "tnAlarmCategoryObjectId": tnAlarmCategoryObjectId,
       "tnAlarmCategoryEntityType": tnAlarmCategoryEntityType,
       "tnAlarmCategoryCondition": tnAlarmCategoryCondition,
       "tnPerObjectAlarmCategory": tnPerObjectAlarmCategory,
       "tnPerObjectAlarmEntityTypeCategory": tnPerObjectAlarmEntityTypeCategory,
       "tnPerObjectAlarmDefaultCategory": tnPerObjectAlarmDefaultCategory,
       "tnAlarmProfileConfigTable": tnAlarmProfileConfigTable,
       "tnAlarmProfileConfigEntry": tnAlarmProfileConfigEntry,
       "tnAlarmCategoryDirection": tnAlarmCategoryDirection,
       "tnAlarmProfileConfigCategory": tnAlarmProfileConfigCategory,
       "tnAlarmProfileConfigDefaultCategory": tnAlarmProfileConfigDefaultCategory,
       "tnAlarmProfileConfigDescr": tnAlarmProfileConfigDescr,
       "tnPerSyncObjectAlarmCategoryConfigTable": tnPerSyncObjectAlarmCategoryConfigTable,
       "tnPerSyncObjectAlarmCategoryConfigEntry": tnPerSyncObjectAlarmCategoryConfigEntry,
       "tnSyncAlarmCategoryObjectId": tnSyncAlarmCategoryObjectId,
       "tnSyncAlarmCategoryEntityType": tnSyncAlarmCategoryEntityType,
       "tnSyncAlarmCategoryCondition": tnSyncAlarmCategoryCondition,
       "tnPerSyncObjectAlarmCategory": tnPerSyncObjectAlarmCategory,
       "tnPerSyncObjectAlarmEntityTypeCategory": tnPerSyncObjectAlarmEntityTypeCategory,
       "tnPerSyncObjectAlarmDefaultCategory": tnPerSyncObjectAlarmDefaultCategory,
       "tnPerVtsObjectAlarmCategoryConfigAttributeTotal": tnPerVtsObjectAlarmCategoryConfigAttributeTotal,
       "tnPerVtsObjectAlarmCategoryConfigTable": tnPerVtsObjectAlarmCategoryConfigTable,
       "tnPerVtsObjectAlarmCategoryConfigEntry": tnPerVtsObjectAlarmCategoryConfigEntry,
       "tnVtsAlarmCategoryObjectId": tnVtsAlarmCategoryObjectId,
       "tnVtsAlarmCategoryDirection": tnVtsAlarmCategoryDirection,
       "tnVtsAlarmCategoryEntityType": tnVtsAlarmCategoryEntityType,
       "tnVtsAlarmCategoryCondition": tnVtsAlarmCategoryCondition,
       "tnPerVtsObjectAlarmCategory": tnPerVtsObjectAlarmCategory,
       "tnPerVtsObjectAlarmEntityTypeCategory": tnPerVtsObjectAlarmEntityTypeCategory,
       "tnPerVtsObjectAlarmDefaultCategory": tnPerVtsObjectAlarmDefaultCategory,
       "tnPerCcmObjectAlarmCategoryConfigAttributeTotal": tnPerCcmObjectAlarmCategoryConfigAttributeTotal,
       "tnPerCcmObjectAlarmCategoryConfigTable": tnPerCcmObjectAlarmCategoryConfigTable,
       "tnPerCcmObjectAlarmCategoryConfigEntry": tnPerCcmObjectAlarmCategoryConfigEntry,
       "tnCcmAlarmCategoryObjectId": tnCcmAlarmCategoryObjectId,
       "tnCcmAlarmCategoryTribObjectId": tnCcmAlarmCategoryTribObjectId,
       "tnCcmAlarmCategoryEntityType": tnCcmAlarmCategoryEntityType,
       "tnCcmAlarmCategoryCondition": tnCcmAlarmCategoryCondition,
       "tnPerCcmObjectAlarmCategory": tnPerCcmObjectAlarmCategory,
       "tnPerCcmObjectAlarmEntityTypeCategory": tnPerCcmObjectAlarmEntityTypeCategory,
       "tnPerCcmObjectAlarmDefaultCategory": tnPerCcmObjectAlarmDefaultCategory,
       "tnPerTcmObjectAlarmCategoryConfigAttributeTotal": tnPerTcmObjectAlarmCategoryConfigAttributeTotal,
       "tnPerTcmObjectAlarmCategoryConfigTable": tnPerTcmObjectAlarmCategoryConfigTable,
       "tnPerTcmObjectAlarmCategoryConfigEntry": tnPerTcmObjectAlarmCategoryConfigEntry,
       "tnTcmAlarmCategoryObjectId": tnTcmAlarmCategoryObjectId,
       "tnTcmAlarmCategoryTribObjectId": tnTcmAlarmCategoryTribObjectId,
       "tnTcmAlarmCategoryEntityType": tnTcmAlarmCategoryEntityType,
       "tnTcmAlarmCategoryCondition": tnTcmAlarmCategoryCondition,
       "tnPerTcmObjectAlarmCategory": tnPerTcmObjectAlarmCategory,
       "tnPerTcmObjectAlarmEntityTypeCategory": tnPerTcmObjectAlarmEntityTypeCategory,
       "tnPerTcmObjectAlarmDefaultCategory": tnPerTcmObjectAlarmDefaultCategory,
       "tnPerPtpObjectAlarmCategoryConfigAttributeTotal": tnPerPtpObjectAlarmCategoryConfigAttributeTotal,
       "tnPerPtpObjectAlarmCategoryConfigTable": tnPerPtpObjectAlarmCategoryConfigTable,
       "tnPerPtpObjectAlarmCategoryConfigEntry": tnPerPtpObjectAlarmCategoryConfigEntry,
       "tnPtpAlarmCategoryObjectId": tnPtpAlarmCategoryObjectId,
       "tnPtpAlarmCategoryDirection": tnPtpAlarmCategoryDirection,
       "tnPtpAlarmCategoryEntityType": tnPtpAlarmCategoryEntityType,
       "tnPtpAlarmCategoryCondition": tnPtpAlarmCategoryCondition,
       "tnPerPtpObjectAlarmCategory": tnPerPtpObjectAlarmCategory,
       "tnPerPtpObjectAlarmEntityTypeCategory": tnPerPtpObjectAlarmEntityTypeCategory,
       "tnPerPtpObjectAlarmDefaultCategory": tnPerPtpObjectAlarmDefaultCategory,
       "tnPerLagObjectAlarmCategoryConfigAttributeTotal": tnPerLagObjectAlarmCategoryConfigAttributeTotal,
       "tnPerLagObjectAlarmCategoryConfigTable": tnPerLagObjectAlarmCategoryConfigTable,
       "tnPerLagObjectAlarmCategoryConfigEntry": tnPerLagObjectAlarmCategoryConfigEntry,
       "tnLagAlarmCategoryObjectId": tnLagAlarmCategoryObjectId,
       "tnLagAlarmCategoryDirection": tnLagAlarmCategoryDirection,
       "tnLagAlarmCategoryEntityType": tnLagAlarmCategoryEntityType,
       "tnLagAlarmCategoryCondition": tnLagAlarmCategoryCondition,
       "tnPerLagObjectAlarmCategory": tnPerLagObjectAlarmCategory,
       "tnPerLagObjectAlarmEntityTypeCategory": tnPerLagObjectAlarmEntityTypeCategory,
       "tnPerLagObjectAlarmDefaultCategory": tnPerLagObjectAlarmDefaultCategory,
       "tnPerOtnObjectAlarmCategoryConfigAttributeTotal": tnPerOtnObjectAlarmCategoryConfigAttributeTotal,
       "tnPerOtnObjectAlarmCategoryConfigTable": tnPerOtnObjectAlarmCategoryConfigTable,
       "tnPerOtnObjectAlarmCategoryConfigEntry": tnPerOtnObjectAlarmCategoryConfigEntry,
       "tnOtnAlarmCategoryObjectId": tnOtnAlarmCategoryObjectId,
       "tnOtnAlarmCategoryTribObjectId": tnOtnAlarmCategoryTribObjectId,
       "tnOtnAlarmCategoryEntityType": tnOtnAlarmCategoryEntityType,
       "tnOtnAlarmCategoryCondition": tnOtnAlarmCategoryCondition,
       "tnPerOtnObjectAlarmCategory": tnPerOtnObjectAlarmCategory,
       "tnPerOtnObjectAlarmEntityTypeCategory": tnPerOtnObjectAlarmEntityTypeCategory,
       "tnPerOtnObjectAlarmDefaultCategory": tnPerOtnObjectAlarmDefaultCategory,
       "tnPerSrSvcObjectAlarmCategoryConfigAttributeTotal": tnPerSrSvcObjectAlarmCategoryConfigAttributeTotal,
       "tnPerSrSvcObjectAlarmCategoryConfigTable": tnPerSrSvcObjectAlarmCategoryConfigTable,
       "tnPerSrSvcObjectAlarmCategoryConfigEntry": tnPerSrSvcObjectAlarmCategoryConfigEntry,
       "tnSrSvcAlarmCategoryEntityType": tnSrSvcAlarmCategoryEntityType,
       "tnSrSvcAlarmCategoryCondition": tnSrSvcAlarmCategoryCondition,
       "tnPerSrSvcObjectAlarmCategory": tnPerSrSvcObjectAlarmCategory,
       "tnPerSrSvcObjectAlarmEntityTypeCategory": tnPerSrSvcObjectAlarmEntityTypeCategory,
       "tnPerSrSvcObjectAlarmDefaultCategory": tnPerSrSvcObjectAlarmDefaultCategory,
       "tnPerSrSapObjectAlarmCategoryConfigAttributeTotal": tnPerSrSapObjectAlarmCategoryConfigAttributeTotal,
       "tnPerSrSapObjectAlarmCategoryConfigTable": tnPerSrSapObjectAlarmCategoryConfigTable,
       "tnPerSrSapObjectAlarmCategoryConfigEntry": tnPerSrSapObjectAlarmCategoryConfigEntry,
       "tnSrSapAlarmCategoryEntityType": tnSrSapAlarmCategoryEntityType,
       "tnSrSapAlarmCategoryCondition": tnSrSapAlarmCategoryCondition,
       "tnPerSrSapObjectAlarmCategory": tnPerSrSapObjectAlarmCategory,
       "tnPerSrSapObjectAlarmEntityTypeCategory": tnPerSrSapObjectAlarmEntityTypeCategory,
       "tnPerSrSapObjectAlarmDefaultCategory": tnPerSrSapObjectAlarmDefaultCategory,
       "tnPerSrErpObjectAlarmCategoryConfigAttributeTotal": tnPerSrErpObjectAlarmCategoryConfigAttributeTotal,
       "tnPerSrErpObjectAlarmCategoryConfigTable": tnPerSrErpObjectAlarmCategoryConfigTable,
       "tnPerSrErpObjectAlarmCategoryConfigEntry": tnPerSrErpObjectAlarmCategoryConfigEntry,
       "tnSrErpAlarmCategoryEntityType": tnSrErpAlarmCategoryEntityType,
       "tnSrErpAlarmCategoryCondition": tnSrErpAlarmCategoryCondition,
       "tnPerSrErpObjectAlarmCategory": tnPerSrErpObjectAlarmCategory,
       "tnPerSrErpObjectAlarmEntityTypeCategory": tnPerSrErpObjectAlarmEntityTypeCategory,
       "tnPerSrErpObjectAlarmDefaultCategory": tnPerSrErpObjectAlarmDefaultCategory,
       "tnPerSrMepObjectAlarmCategoryConfigAttributeTotal": tnPerSrMepObjectAlarmCategoryConfigAttributeTotal,
       "tnPerSrMepObjectAlarmCategoryConfigTable": tnPerSrMepObjectAlarmCategoryConfigTable,
       "tnPerSrMepObjectAlarmCategoryConfigEntry": tnPerSrMepObjectAlarmCategoryConfigEntry,
       "tnSrMepAlarmCategoryEntityType": tnSrMepAlarmCategoryEntityType,
       "tnSrMepAlarmCategoryCondition": tnSrMepAlarmCategoryCondition,
       "tnPerSrMepObjectAlarmCategory": tnPerSrMepObjectAlarmCategory,
       "tnPerSrMepObjectAlarmEntityTypeCategory": tnPerSrMepObjectAlarmEntityTypeCategory,
       "tnPerSrMepObjectAlarmDefaultCategory": tnPerSrMepObjectAlarmDefaultCategory,
       "tnPerSrOamTestObjectAlarmCategoryConfigAttributeTotal": tnPerSrOamTestObjectAlarmCategoryConfigAttributeTotal,
       "tnPerSrOamTestObjectAlarmCategoryConfigTable": tnPerSrOamTestObjectAlarmCategoryConfigTable,
       "tnPerSrOamTestObjectAlarmCategoryConfigEntry": tnPerSrOamTestObjectAlarmCategoryConfigEntry,
       "tnSrOamTestAlarmCategoryEntityType": tnSrOamTestAlarmCategoryEntityType,
       "tnSrOamTestAlarmCategoryCondition": tnSrOamTestAlarmCategoryCondition,
       "tnPerSrOamTestObjectAlarmCategory": tnPerSrOamTestObjectAlarmCategory,
       "tnPerSrOamTestObjectAlarmEntityTypeCategory": tnPerSrOamTestObjectAlarmEntityTypeCategory,
       "tnPerSrOamTestObjectAlarmDefaultCategory": tnPerSrOamTestObjectAlarmDefaultCategory,
       "tnPerRmdObjectAlarmCategoryConfigAttributeTotal": tnPerRmdObjectAlarmCategoryConfigAttributeTotal,
       "tnPerRmdObjectAlarmCategoryConfigTable": tnPerRmdObjectAlarmCategoryConfigTable,
       "tnPerRmdObjectAlarmCategoryConfigEntry": tnPerRmdObjectAlarmCategoryConfigEntry,
       "tnRmdAlarmCategoryEntityType": tnRmdAlarmCategoryEntityType,
       "tnRmdAlarmCategoryCondition": tnRmdAlarmCategoryCondition,
       "tnPerRmdObjectAlarmCategory": tnPerRmdObjectAlarmCategory,
       "tnPerRmdObjectAlarmEntityTypeCategory": tnPerRmdObjectAlarmEntityTypeCategory,
       "tnPerRmdObjectAlarmDefaultCategory": tnPerRmdObjectAlarmDefaultCategory,
       "tnPerRmdMepObjectAlarmCategoryConfigAttributeTotal": tnPerRmdMepObjectAlarmCategoryConfigAttributeTotal,
       "tnPerRmdMepObjectAlarmCategoryConfigTable": tnPerRmdMepObjectAlarmCategoryConfigTable,
       "tnPerRmdMepObjectAlarmCategoryConfigEntry": tnPerRmdMepObjectAlarmCategoryConfigEntry,
       "tnRmdMepAlarmCategoryEntityType": tnRmdMepAlarmCategoryEntityType,
       "tnRmdMepAlarmCategoryCondition": tnRmdMepAlarmCategoryCondition,
       "tnPerRmdMepObjectAlarmCategory": tnPerRmdMepObjectAlarmCategory,
       "tnPerRmdMepObjectAlarmEntityTypeCategory": tnPerRmdMepObjectAlarmEntityTypeCategory,
       "tnPerRmdMepObjectAlarmDefaultCategory": tnPerRmdMepObjectAlarmDefaultCategory,
       "tnPerRmdIfObjectAlarmCategoryConfigAttributeTotal": tnPerRmdIfObjectAlarmCategoryConfigAttributeTotal,
       "tnPerRmdIfObjectAlarmCategoryConfigTable": tnPerRmdIfObjectAlarmCategoryConfigTable,
       "tnPerRmdIfObjectAlarmCategoryConfigEntry": tnPerRmdIfObjectAlarmCategoryConfigEntry,
       "tnRmdIfAlarmCategoryEntityType": tnRmdIfAlarmCategoryEntityType,
       "tnRmdIfAlarmCategoryCondition": tnRmdIfAlarmCategoryCondition,
       "tnPerRmdIfObjectAlarmCategory": tnPerRmdIfObjectAlarmCategory,
       "tnPerRmdIfObjectAlarmEntityTypeCategory": tnPerRmdIfObjectAlarmEntityTypeCategory,
       "tnPerRmdIfObjectAlarmDefaultCategory": tnPerRmdIfObjectAlarmDefaultCategory,
       "tnPerRmdIfMauObjectAlarmCategoryConfigAttributeTotal": tnPerRmdIfMauObjectAlarmCategoryConfigAttributeTotal,
       "tnPerRmdIfMauObjectAlarmCategoryConfigTable": tnPerRmdIfMauObjectAlarmCategoryConfigTable,
       "tnPerRmdIfMauObjectAlarmCategoryConfigEntry": tnPerRmdIfMauObjectAlarmCategoryConfigEntry,
       "tnRmdIfMauAlarmCategoryEntityType": tnRmdIfMauAlarmCategoryEntityType,
       "tnRmdIfMauAlarmCategoryCondition": tnRmdIfMauAlarmCategoryCondition,
       "tnPerRmdIfMauObjectAlarmCategory": tnPerRmdIfMauObjectAlarmCategory,
       "tnPerRmdIfMauObjectAlarmEntityTypeCategory": tnPerRmdIfMauObjectAlarmEntityTypeCategory,
       "tnPerRmdIfMauObjectAlarmDefaultCategory": tnPerRmdIfMauObjectAlarmDefaultCategory,
       "tnPerRmdCesChannelObjectAlarmCategoryConfigAttributeTotal": tnPerRmdCesChannelObjectAlarmCategoryConfigAttributeTotal,
       "tnPerRmdCesChannelObjectAlarmCategoryConfigTable": tnPerRmdCesChannelObjectAlarmCategoryConfigTable,
       "tnPerRmdCesChannelObjectAlarmCategoryConfigEntry": tnPerRmdCesChannelObjectAlarmCategoryConfigEntry,
       "tnRmdCesChannelAlarmCategoryEntityType": tnRmdCesChannelAlarmCategoryEntityType,
       "tnRmdCesChannelAlarmCategoryCondition": tnRmdCesChannelAlarmCategoryCondition,
       "tnPerRmdCesChannelObjectAlarmCategory": tnPerRmdCesChannelObjectAlarmCategory,
       "tnPerRmdCesChannelObjectAlarmEntityTypeCategory": tnPerRmdCesChannelObjectAlarmEntityTypeCategory,
       "tnPerRmdCesChannelObjectAlarmDefaultCategory": tnPerRmdCesChannelObjectAlarmDefaultCategory,
       "tnPerOthObjectAlarmCategoryConfigAttributeTotal": tnPerOthObjectAlarmCategoryConfigAttributeTotal,
       "tnPerOthObjectAlarmCategoryConfigTable": tnPerOthObjectAlarmCategoryConfigTable,
       "tnPerOthObjectAlarmCategoryConfigEntry": tnPerOthObjectAlarmCategoryConfigEntry,
       "tnOthAlarmCategoryObjectId": tnOthAlarmCategoryObjectId,
       "tnOthAlarmCategoryTribObjectId": tnOthAlarmCategoryTribObjectId,
       "tnOthAlarmCategoryDirection": tnOthAlarmCategoryDirection,
       "tnOthAlarmCategoryEntityType": tnOthAlarmCategoryEntityType,
       "tnOthAlarmCategoryCondition": tnOthAlarmCategoryCondition,
       "tnPerOthObjectAlarmCategory": tnPerOthObjectAlarmCategory,
       "tnPerOthObjectAlarmEntityTypeCategory": tnPerOthObjectAlarmEntityTypeCategory,
       "tnPerOthObjectAlarmDefaultCategory": tnPerOthObjectAlarmDefaultCategory,
       "tnPerRmdNimObjectAlarmCategoryConfigAttributeTotal": tnPerRmdNimObjectAlarmCategoryConfigAttributeTotal,
       "tnPerRmdNimObjectAlarmCategoryConfigTable": tnPerRmdNimObjectAlarmCategoryConfigTable,
       "tnPerRmdNimObjectAlarmCategoryConfigEntry": tnPerRmdNimObjectAlarmCategoryConfigEntry,
       "tnRmdIfNimDirection": tnRmdIfNimDirection,
       "tnRmdNimAlarmCategoryEntityType": tnRmdNimAlarmCategoryEntityType,
       "tnRmdNimAlarmCategoryCondition": tnRmdNimAlarmCategoryCondition,
       "tnPerRmdNimObjectAlarmCategory": tnPerRmdNimObjectAlarmCategory,
       "tnPerRmdNimObjectAlarmEntityTypeCategory": tnPerRmdNimObjectAlarmEntityTypeCategory,
       "tnPerRmdNimObjectAlarmDefaultCategory": tnPerRmdNimObjectAlarmDefaultCategory}
)
