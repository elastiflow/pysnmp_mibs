# SNMP MIB module (EKT-CORE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/elkomtech_44730/EKT-CORE-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 12:06:13 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Elkomtech_ObjectIdentity = ObjectIdentity
elkomtech = _Elkomtech_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44730)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44730, 0)
)
_TrapMsg_ObjectIdentity = ObjectIdentity
trapMsg = _TrapMsg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44730, 0, 12)
)
_SubDeviceId_Type = OctetString
_SubDeviceId_Object = MibScalar
subDeviceId = _SubDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 44730, 0, 12, 1),
    _SubDeviceId_Type()
)
subDeviceId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    subDeviceId.setStatus("current")
_DateTimeString_Type = OctetString
_DateTimeString_Object = MibScalar
dateTimeString = _DateTimeString_Object(
    (1, 3, 6, 1, 4, 1, 44730, 0, 12, 2),
    _DateTimeString_Type()
)
dateTimeString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dateTimeString.setStatus("current")
_LogMessage_Type = OctetString
_LogMessage_Object = MibScalar
logMessage = _LogMessage_Object(
    (1, 3, 6, 1, 4, 1, 44730, 0, 12, 3),
    _LogMessage_Type()
)
logMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    logMessage.setStatus("current")


class _CommState_Type(Integer32):
    """Custom type commState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("lost", 1))
    )


_CommState_Type.__name__ = "Integer32"
_CommState_Object = MibScalar
commState = _CommState_Object(
    (1, 3, 6, 1, 4, 1, 44730, 0, 12, 4),
    _CommState_Type()
)
commState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commState.setStatus("current")
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44730, 1)
)
_ExWinApp_ObjectIdentity = ObjectIdentity
exWinApp = _ExWinApp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44730, 1, 1)
)
_ExMST2_ObjectIdentity = ObjectIdentity
exMST2 = _ExMST2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44730, 1, 2)
)
_ExBRG2_ObjectIdentity = ObjectIdentity
exBRG2 = _ExBRG2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44730, 1, 3)
)
_ExRSU_ObjectIdentity = ObjectIdentity
exRSU = _ExRSU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44730, 1, 4)
)
_Info_ObjectIdentity = ObjectIdentity
info = _Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44730, 2)
)
_InfoType_Type = OctetString
_InfoType_Object = MibScalar
infoType = _InfoType_Object(
    (1, 3, 6, 1, 4, 1, 44730, 2, 1),
    _InfoType_Type()
)
infoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoType.setStatus("current")
_InfoSN_Type = OctetString
_InfoSN_Object = MibScalar
infoSN = _InfoSN_Object(
    (1, 3, 6, 1, 4, 1, 44730, 2, 2),
    _InfoSN_Type()
)
infoSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSN.setStatus("current")
_InfoFwVer_Type = OctetString
_InfoFwVer_Object = MibScalar
infoFwVer = _InfoFwVer_Object(
    (1, 3, 6, 1, 4, 1, 44730, 2, 3),
    _InfoFwVer_Type()
)
infoFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoFwVer.setStatus("current")
_InfoCurrTime_Type = OctetString
_InfoCurrTime_Object = MibScalar
infoCurrTime = _InfoCurrTime_Object(
    (1, 3, 6, 1, 4, 1, 44730, 2, 4),
    _InfoCurrTime_Type()
)
infoCurrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoCurrTime.setStatus("current")
_DeviceIO_ObjectIdentity = ObjectIdentity
deviceIO = _DeviceIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44730, 4)
)
_BiTable_Object = MibTable
biTable = _BiTable_Object(
    (1, 3, 6, 1, 4, 1, 44730, 4, 1)
)
if mibBuilder.loadTexts:
    biTable.setStatus("current")
_SgnEntry_Object = MibTableRow
sgnEntry = _SgnEntry_Object(
    (1, 3, 6, 1, 4, 1, 44730, 4, 1, 1)
)
sgnEntry.setIndexNames(
    (0, "EKT-CORE-MIB", "sgnIndex"),
)
if mibBuilder.loadTexts:
    sgnEntry.setStatus("current")
_SgnIndex_Type = Integer32
_SgnIndex_Object = MibTableColumn
sgnIndex = _SgnIndex_Object(
    (1, 3, 6, 1, 4, 1, 44730, 4, 1, 1, 1),
    _SgnIndex_Type()
)
sgnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgnIndex.setStatus("current")
_SgnValue_Type = Integer32
_SgnValue_Object = MibTableColumn
sgnValue = _SgnValue_Object(
    (1, 3, 6, 1, 4, 1, 44730, 4, 1, 1, 2),
    _SgnValue_Type()
)
sgnValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgnValue.setStatus("current")
_AiTable_Object = MibTable
aiTable = _AiTable_Object(
    (1, 3, 6, 1, 4, 1, 44730, 4, 2)
)
if mibBuilder.loadTexts:
    aiTable.setStatus("current")
_MsrEntry_Object = MibTableRow
msrEntry = _MsrEntry_Object(
    (1, 3, 6, 1, 4, 1, 44730, 4, 2, 1)
)
msrEntry.setIndexNames(
    (0, "EKT-CORE-MIB", "msrIndex"),
)
if mibBuilder.loadTexts:
    msrEntry.setStatus("current")
_MsrIndex_Type = Integer32
_MsrIndex_Object = MibTableColumn
msrIndex = _MsrIndex_Object(
    (1, 3, 6, 1, 4, 1, 44730, 4, 2, 1, 1),
    _MsrIndex_Type()
)
msrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msrIndex.setStatus("current")
_MsrValue_Type = Integer32
_MsrValue_Object = MibTableColumn
msrValue = _MsrValue_Object(
    (1, 3, 6, 1, 4, 1, 44730, 4, 2, 1, 2),
    _MsrValue_Type()
)
msrValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msrValue.setStatus("current")
_Protocols_ObjectIdentity = ObjectIdentity
protocols = _Protocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44730, 5)
)
_PrStatusTable_Object = MibTable
prStatusTable = _PrStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 44730, 5, 1)
)
if mibBuilder.loadTexts:
    prStatusTable.setStatus("current")
_PrStatusEntry_Object = MibTableRow
prStatusEntry = _PrStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 44730, 5, 1, 1)
)
prStatusEntry.setIndexNames(
    (0, "EKT-CORE-MIB", "prIndex"),
)
if mibBuilder.loadTexts:
    prStatusEntry.setStatus("current")
_PrIndex_Type = Integer32
_PrIndex_Object = MibTableColumn
prIndex = _PrIndex_Object(
    (1, 3, 6, 1, 4, 1, 44730, 5, 1, 1, 1),
    _PrIndex_Type()
)
prIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prIndex.setStatus("current")
_PrIdent_Type = OctetString
_PrIdent_Object = MibTableColumn
prIdent = _PrIdent_Object(
    (1, 3, 6, 1, 4, 1, 44730, 5, 1, 1, 2),
    _PrIdent_Type()
)
prIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prIdent.setStatus("current")
_PrDesc_Type = OctetString
_PrDesc_Object = MibTableColumn
prDesc = _PrDesc_Object(
    (1, 3, 6, 1, 4, 1, 44730, 5, 1, 1, 3),
    _PrDesc_Type()
)
prDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prDesc.setStatus("current")


class _PrEnabled_Type(Integer32):
    """Custom type prEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_PrEnabled_Type.__name__ = "Integer32"
_PrEnabled_Object = MibTableColumn
prEnabled = _PrEnabled_Object(
    (1, 3, 6, 1, 4, 1, 44730, 5, 1, 1, 4),
    _PrEnabled_Type()
)
prEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prEnabled.setStatus("current")


class _PrState_Type(Integer32):
    """Custom type prState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("disabled", 1),
          ("dead", 2),
          ("alive", 3),
          ("lost", 4))
    )


_PrState_Type.__name__ = "Integer32"
_PrState_Object = MibTableColumn
prState = _PrState_Object(
    (1, 3, 6, 1, 4, 1, 44730, 5, 1, 1, 5),
    _PrState_Type()
)
prState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prState.setStatus("current")
_PrRequests_Type = Counter32
_PrRequests_Object = MibTableColumn
prRequests = _PrRequests_Object(
    (1, 3, 6, 1, 4, 1, 44730, 5, 1, 1, 6),
    _PrRequests_Type()
)
prRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prRequests.setStatus("current")
_PrResponses_Type = Counter32
_PrResponses_Object = MibTableColumn
prResponses = _PrResponses_Object(
    (1, 3, 6, 1, 4, 1, 44730, 5, 1, 1, 7),
    _PrResponses_Type()
)
prResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prResponses.setStatus("current")
_PrSendErr_Type = Counter32
_PrSendErr_Object = MibTableColumn
prSendErr = _PrSendErr_Object(
    (1, 3, 6, 1, 4, 1, 44730, 5, 1, 1, 8),
    _PrSendErr_Type()
)
prSendErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prSendErr.setStatus("current")
_PrRespErr_Type = Counter32
_PrRespErr_Object = MibTableColumn
prRespErr = _PrRespErr_Object(
    (1, 3, 6, 1, 4, 1, 44730, 5, 1, 1, 9),
    _PrRespErr_Type()
)
prRespErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prRespErr.setStatus("current")
_SysMsr_ObjectIdentity = ObjectIdentity
sysMsr = _SysMsr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44730, 7)
)
_SysBattVoltage_Type = OctetString
_SysBattVoltage_Object = MibScalar
sysBattVoltage = _SysBattVoltage_Object(
    (1, 3, 6, 1, 4, 1, 44730, 7, 1),
    _SysBattVoltage_Type()
)
sysBattVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBattVoltage.setStatus("current")
_SysTempValue_Type = OctetString
_SysTempValue_Object = MibScalar
sysTempValue = _SysTempValue_Object(
    (1, 3, 6, 1, 4, 1, 44730, 7, 2),
    _SysTempValue_Type()
)
sysTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTempValue.setStatus("current")
_SysCpuUsage_Type = Integer32
_SysCpuUsage_Object = MibScalar
sysCpuUsage = _SysCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 44730, 7, 3),
    _SysCpuUsage_Type()
)
sysCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCpuUsage.setStatus("current")
_SysMemUsage_Type = Integer32
_SysMemUsage_Object = MibScalar
sysMemUsage = _SysMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 44730, 7, 4),
    _SysMemUsage_Type()
)
sysMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMemUsage.setStatus("current")
_SysRamUsage_Type = Integer32
_SysRamUsage_Object = MibScalar
sysRamUsage = _SysRamUsage_Object(
    (1, 3, 6, 1, 4, 1, 44730, 7, 5),
    _SysRamUsage_Type()
)
sysRamUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysRamUsage.setStatus("current")
_SysDiagn_ObjectIdentity = ObjectIdentity
sysDiagn = _SysDiagn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44730, 8)
)


class _SysTimeState_Type(Integer32):
    """Custom type sysTimeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("set", 0),
          ("notSet", 1))
    )


_SysTimeState_Type.__name__ = "Integer32"
_SysTimeState_Object = MibScalar
sysTimeState = _SysTimeState_Object(
    (1, 3, 6, 1, 4, 1, 44730, 8, 1),
    _SysTimeState_Type()
)
sysTimeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTimeState.setStatus("current")


class _SysTimeSyncState_Type(Integer32):
    """Custom type sysTimeSyncState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("valid", 0),
          ("obsolete", 1))
    )


_SysTimeSyncState_Type.__name__ = "Integer32"
_SysTimeSyncState_Object = MibScalar
sysTimeSyncState = _SysTimeSyncState_Object(
    (1, 3, 6, 1, 4, 1, 44730, 8, 2),
    _SysTimeSyncState_Type()
)
sysTimeSyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTimeSyncState.setStatus("current")

# Managed Objects groups


# Notification objects

sysTimeStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 100)
)
sysTimeStateTrap.setObjects(
    ("EKT-CORE-MIB", "logMessage")
)
if mibBuilder.loadTexts:
    sysTimeStateTrap.setStatus(
        "current"
    )

sysTimeSyncStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 101)
)
sysTimeSyncStateTrap.setObjects(
    ("EKT-CORE-MIB", "logMessage")
)
if mibBuilder.loadTexts:
    sysTimeSyncStateTrap.setStatus(
        "current"
    )

sysBattLevelFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 104)
)
sysBattLevelFailure.setObjects(
    ("EKT-CORE-MIB", "sysBattVoltage")
)
if mibBuilder.loadTexts:
    sysBattLevelFailure.setStatus(
        "current"
    )

sysTempIncorrect = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 105)
)
sysTempIncorrect.setObjects(
    ("EKT-CORE-MIB", "sysTempValue")
)
if mibBuilder.loadTexts:
    sysTempIncorrect.setStatus(
        "current"
    )

sysCpuUsageAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 106)
)
sysCpuUsageAbnormal.setObjects(
    ("EKT-CORE-MIB", "sysCpuUsage")
)
if mibBuilder.loadTexts:
    sysCpuUsageAbnormal.setStatus(
        "current"
    )

sysMemAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 107)
)
sysMemAlarm.setObjects(
    ("EKT-CORE-MIB", "sysMemUsage")
)
if mibBuilder.loadTexts:
    sysMemAlarm.setStatus(
        "current"
    )

sysRamUsageAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 108)
)
sysRamUsageAlarm.setObjects(
    ("EKT-CORE-MIB", "systemRamUsage")
)
if mibBuilder.loadTexts:
    sysRamUsageAlarm.setStatus(
        "current"
    )

sysSomeCertsWillExpire = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 109)
)
sysSomeCertsWillExpire.setObjects(
    ("EKT-CORE-MIB", "logMessage")
)
if mibBuilder.loadTexts:
    sysSomeCertsWillExpire.setStatus(
        "current"
    )

sysBattLevelCorrect = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 154)
)
sysBattLevelCorrect.setObjects(
    ("EKT-CORE-MIB", "sysBattVoltage")
)
if mibBuilder.loadTexts:
    sysBattLevelCorrect.setStatus(
        "current"
    )

sTempCorrect = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 155)
)
sTempCorrect.setObjects(
    ("EKT-CORE-MIB", "sysTempValue")
)
if mibBuilder.loadTexts:
    sTempCorrect.setStatus(
        "current"
    )

sysCpuUsageNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 156)
)
sysCpuUsageNormal.setObjects(
    ("EKT-CORE-MIB", "sysCpuUsage")
)
if mibBuilder.loadTexts:
    sysCpuUsageNormal.setStatus(
        "current"
    )

sysMemUsageNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 157)
)
sysMemUsageNormal.setObjects(
    ("EKT-CORE-MIB", "sysMemUsage")
)
if mibBuilder.loadTexts:
    sysMemUsageNormal.setStatus(
        "current"
    )

intSysRamUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 158)
)
intSysRamUsage.setObjects(
    ("EKT-CORE-MIB", "sysRamUsage")
)
if mibBuilder.loadTexts:
    intSysRamUsage.setStatus(
        "current"
    )

intSubDeviceRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 201)
)
intSubDeviceRestart.setObjects(
    ("EKT-CORE-MIB", "subDeviceId")
)
if mibBuilder.loadTexts:
    intSubDeviceRestart.setStatus(
        "current"
    )

intCommLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 204)
)
intCommLost.setObjects(
    ("EKT-CORE-MIB", "subDeviceId")
)
if mibBuilder.loadTexts:
    intCommLost.setStatus(
        "current"
    )

intCommRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 205)
)
intCommRestored.setObjects(
    ("EKT-CORE-MIB", "subDeviceId")
)
if mibBuilder.loadTexts:
    intCommRestored.setStatus(
        "current"
    )

intNewProgLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 214)
)
intNewProgLoad.setObjects(
    ("EKT-CORE-MIB", "dateTimeString")
)
if mibBuilder.loadTexts:
    intNewProgLoad.setStatus(
        "current"
    )

intNewBaseCfgLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 215)
)
intNewBaseCfgLoad.setObjects(
    ("EKT-CORE-MIB", "dateTimeString")
)
if mibBuilder.loadTexts:
    intNewBaseCfgLoad.setStatus(
        "current"
    )

intBattFailureDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 221)
)
intBattFailureDetected.setObjects(
    ("EKT-CORE-MIB", "battLevel")
)
if mibBuilder.loadTexts:
    intBattFailureDetected.setStatus(
        "current"
    )

intUserLogon = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 222)
)
intUserLogon.setObjects(
    ("EKT-CORE-MIB", "logMessage")
)
if mibBuilder.loadTexts:
    intUserLogon.setStatus(
        "current"
    )

intUserLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 223)
)
intUserLogout.setObjects(
    ("EKT-CORE-MIB", "logMessage")
)
if mibBuilder.loadTexts:
    intUserLogout.setStatus(
        "current"
    )

intUserLogonFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 224)
)
intUserLogonFailure.setObjects(
    ("EKT-CORE-MIB", "logMessage")
)
if mibBuilder.loadTexts:
    intUserLogonFailure.setStatus(
        "current"
    )

intCfgUdpated = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 225)
)
intCfgUdpated.setObjects(
    ("EKT-CORE-MIB", "logMessage")
)
if mibBuilder.loadTexts:
    intCfgUdpated.setStatus(
        "current"
    )

intprogramUdpated = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 226)
)
intprogramUdpated.setObjects(
    ("EKT-CORE-MIB", "logMessage")
)
if mibBuilder.loadTexts:
    intprogramUdpated.setStatus(
        "current"
    )

binInputChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 44730, 0, 401)
)
binInputChanged.setObjects(
    ("EKT-CORE-MIB", "sgnValue")
)
if mibBuilder.loadTexts:
    binInputChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKT-CORE-MIB",
    **{"elkomtech": elkomtech,
       "traps": traps,
       "trapMsg": trapMsg,
       "subDeviceId": subDeviceId,
       "dateTimeString": dateTimeString,
       "logMessage": logMessage,
       "commState": commState,
       "sysTimeStateTrap": sysTimeStateTrap,
       "sysTimeSyncStateTrap": sysTimeSyncStateTrap,
       "sysBattLevelFailure": sysBattLevelFailure,
       "sysTempIncorrect": sysTempIncorrect,
       "sysCpuUsageAbnormal": sysCpuUsageAbnormal,
       "sysMemAlarm": sysMemAlarm,
       "sysRamUsageAlarm": sysRamUsageAlarm,
       "sysSomeCertsWillExpire": sysSomeCertsWillExpire,
       "sysBattLevelCorrect": sysBattLevelCorrect,
       "sTempCorrect": sTempCorrect,
       "sysCpuUsageNormal": sysCpuUsageNormal,
       "sysMemUsageNormal": sysMemUsageNormal,
       "intSysRamUsage": intSysRamUsage,
       "intSubDeviceRestart": intSubDeviceRestart,
       "intCommLost": intCommLost,
       "intCommRestored": intCommRestored,
       "intNewProgLoad": intNewProgLoad,
       "intNewBaseCfgLoad": intNewBaseCfgLoad,
       "intBattFailureDetected": intBattFailureDetected,
       "intUserLogon": intUserLogon,
       "intUserLogout": intUserLogout,
       "intUserLogonFailure": intUserLogonFailure,
       "intCfgUdpated": intCfgUdpated,
       "intprogramUdpated": intprogramUdpated,
       "binInputChanged": binInputChanged,
       "products": products,
       "exWinApp": exWinApp,
       "exMST2": exMST2,
       "exBRG2": exBRG2,
       "exRSU": exRSU,
       "info": info,
       "infoType": infoType,
       "infoSN": infoSN,
       "infoFwVer": infoFwVer,
       "infoCurrTime": infoCurrTime,
       "deviceIO": deviceIO,
       "biTable": biTable,
       "sgnEntry": sgnEntry,
       "sgnIndex": sgnIndex,
       "sgnValue": sgnValue,
       "aiTable": aiTable,
       "msrEntry": msrEntry,
       "msrIndex": msrIndex,
       "msrValue": msrValue,
       "protocols": protocols,
       "prStatusTable": prStatusTable,
       "prStatusEntry": prStatusEntry,
       "prIndex": prIndex,
       "prIdent": prIdent,
       "prDesc": prDesc,
       "prEnabled": prEnabled,
       "prState": prState,
       "prRequests": prRequests,
       "prResponses": prResponses,
       "prSendErr": prSendErr,
       "prRespErr": prRespErr,
       "sysMsr": sysMsr,
       "sysBattVoltage": sysBattVoltage,
       "sysTempValue": sysTempValue,
       "sysCpuUsage": sysCpuUsage,
       "sysMemUsage": sysMemUsage,
       "sysRamUsage": sysRamUsage,
       "sysDiagn": sysDiagn,
       "sysTimeState": sysTimeState,
       "sysTimeSyncState": sysTimeSyncState}
)
