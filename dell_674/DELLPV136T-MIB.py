# SNMP MIB module (DELLPV136T-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/dell_674/DELLPV136T-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 16:02:30 2025
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
 NotificationType,
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
    "NotificationType",
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

_Dell_ObjectIdentity = ObjectIdentity
dell = _Dell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674)
)
_Storage_ObjectIdentity = ObjectIdentity
storage = _Storage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10893)
)
_Hardware_ObjectIdentity = ObjectIdentity
hardware = _Hardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2)
)
_PV136Tagent_ObjectIdentity = ObjectIdentity
pV136Tagent = _PV136Tagent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100)
)
_PV136TAgentInfo_ObjectIdentity = ObjectIdentity
pV136TAgentInfo = _PV136TAgentInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 1)
)
_PV136TDisplayName_Type = DisplayString
_PV136TDisplayName_Object = MibScalar
pV136TDisplayName = _PV136TDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 1, 1),
    _PV136TDisplayName_Type()
)
pV136TDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pV136TDisplayName.setStatus("mandatory")
_PV136Description_Type = DisplayString
_PV136Description_Object = MibScalar
pV136Description = _PV136Description_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 1, 2),
    _PV136Description_Type()
)
pV136Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pV136Description.setStatus("mandatory")
_PV136AgentVendor_Type = DisplayString
_PV136AgentVendor_Object = MibScalar
pV136AgentVendor = _PV136AgentVendor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 1, 3),
    _PV136AgentVendor_Type()
)
pV136AgentVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pV136AgentVendor.setStatus("mandatory")
_PV136AgentVersion_Type = DisplayString
_PV136AgentVersion_Object = MibScalar
pV136AgentVersion = _PV136AgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 1, 4),
    _PV136AgentVersion_Type()
)
pV136AgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pV136AgentVersion.setStatus("mandatory")
_GlobalData_ObjectIdentity = ObjectIdentity
globalData = _GlobalData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 2)
)


class _PV136GlobalStatus_Type(Integer32):
    """Custom type pV136GlobalStatus based on Integer32"""
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
        *(("other", 1),
          ("unknown", 2),
          ("ok", 3),
          ("non-critical", 4),
          ("critical", 5),
          ("non-Recoverable", 6))
    )


_PV136GlobalStatus_Type.__name__ = "Integer32"
_PV136GlobalStatus_Object = MibScalar
pV136GlobalStatus = _PV136GlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 2, 1),
    _PV136GlobalStatus_Type()
)
pV136GlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pV136GlobalStatus.setStatus("mandatory")


class _PV136LastGlobalStatus_Type(Integer32):
    """Custom type pV136LastGlobalStatus based on Integer32"""
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
        *(("other", 1),
          ("unknown", 2),
          ("ok", 3),
          ("non-critical", 4),
          ("critical", 5),
          ("non-recoverable", 6))
    )


_PV136LastGlobalStatus_Type.__name__ = "Integer32"
_PV136LastGlobalStatus_Object = MibScalar
pV136LastGlobalStatus = _PV136LastGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 2, 2),
    _PV136LastGlobalStatus_Type()
)
pV136LastGlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pV136LastGlobalStatus.setStatus("mandatory")
_PV136TimeStamp_Type = Integer32
_PV136TimeStamp_Object = MibScalar
pV136TimeStamp = _PV136TimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 2, 3),
    _PV136TimeStamp_Type()
)
pV136TimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pV136TimeStamp.setStatus("mandatory")


class _PV136GetTimeOut_Type(Integer32):
    """Custom type pV136GetTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_PV136GetTimeOut_Type.__name__ = "Integer32"
_PV136GetTimeOut_Object = MibScalar
pV136GetTimeOut = _PV136GetTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 2, 4),
    _PV136GetTimeOut_Type()
)
pV136GetTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pV136GetTimeOut.setStatus("mandatory")


class _PV136Modifiers_Type(Integer32):
    """Custom type pV136Modifiers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_PV136Modifiers_Type.__name__ = "Integer32"
_PV136Modifiers_Object = MibScalar
pV136Modifiers = _PV136Modifiers_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 2, 5),
    _PV136Modifiers_Type()
)
pV136Modifiers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pV136Modifiers.setStatus("mandatory")


class _PV136RefreshRate_Type(Integer32):
    """Custom type pV136RefreshRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000000000),
    )


_PV136RefreshRate_Type.__name__ = "Integer32"
_PV136RefreshRate_Object = MibScalar
pV136RefreshRate = _PV136RefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 2, 6),
    _PV136RefreshRate_Type()
)
pV136RefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pV136RefreshRate.setStatus("mandatory")
_PV136IPAddress_Type = DisplayString
_PV136IPAddress_Object = MibScalar
pV136IPAddress = _PV136IPAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 2, 7),
    _PV136IPAddress_Type()
)
pV136IPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pV136IPAddress.setStatus("optional")
_PV136HostName_Type = DisplayString
_PV136HostName_Object = MibScalar
pV136HostName = _PV136HostName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 2, 8),
    _PV136HostName_Type()
)
pV136HostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pV136HostName.setStatus("optional")
_PV136RMUVersion_Type = DisplayString
_PV136RMUVersion_Object = MibScalar
pV136RMUVersion = _PV136RMUVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 2, 9),
    _PV136RMUVersion_Type()
)
pV136RMUVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pV136RMUVersion.setStatus("optional")


class _PV136ShutdownState_Type(Integer32):
    """Custom type pV136ShutdownState based on Integer32"""
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
        *(("other", 1),
          ("unknown", 2),
          ("normal", 3),
          ("abnormal", 4))
    )


_PV136ShutdownState_Type.__name__ = "Integer32"
_PV136ShutdownState_Object = MibScalar
pV136ShutdownState = _PV136ShutdownState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 2, 10),
    _PV136ShutdownState_Type()
)
pV136ShutdownState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pV136ShutdownState.setStatus("mandatory")


class _PV136PreviousShutdownState_Type(Integer32):
    """Custom type pV136PreviousShutdownState based on Integer32"""
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
        *(("other", 1),
          ("unknown", 2),
          ("normal", 3),
          ("abnormal", 4))
    )


_PV136PreviousShutdownState_Type.__name__ = "Integer32"
_PV136PreviousShutdownState_Object = MibScalar
pV136PreviousShutdownState = _PV136PreviousShutdownState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 2, 11),
    _PV136PreviousShutdownState_Type()
)
pV136PreviousShutdownState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pV136PreviousShutdownState.setStatus("mandatory")
_PV136ErrorCode_Type = Integer32
_PV136ErrorCode_Object = MibScalar
pV136ErrorCode = _PV136ErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 2, 12),
    _PV136ErrorCode_Type()
)
pV136ErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pV136ErrorCode.setStatus("mandatory")
_PV136ErrorData_Type = Integer32
_PV136ErrorData_Object = MibScalar
pV136ErrorData = _PV136ErrorData_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 2, 13),
    _PV136ErrorData_Type()
)
pV136ErrorData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pV136ErrorData.setStatus("mandatory")
_PV136ServiceActionCode_Type = Integer32
_PV136ServiceActionCode_Object = MibScalar
pV136ServiceActionCode = _PV136ServiceActionCode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 2, 14),
    _PV136ServiceActionCode_Type()
)
pV136ServiceActionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pV136ServiceActionCode.setStatus("mandatory")
_Pv136ServiceTag_Type = DisplayString
_Pv136ServiceTag_Object = MibScalar
pv136ServiceTag = _Pv136ServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 2, 15),
    _Pv136ServiceTag_Type()
)
pv136ServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pv136ServiceTag.setStatus("mandatory")
_PhysicalDevices_ObjectIdentity = ObjectIdentity
physicalDevices = _PhysicalDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3)
)
_MoverTable_Object = MibTable
moverTable = _MoverTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 1)
)
if mibBuilder.loadTexts:
    moverTable.setStatus("mandatory")
_MoverEntry_Object = MibTableRow
moverEntry = _MoverEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 1, 1)
)
moverEntry.setIndexNames(
    (0, "DELLPV136T-MIB", "moverEntryId"),
)
if mibBuilder.loadTexts:
    moverEntry.setStatus("mandatory")


class _MoverEntryId_Type(Integer32):
    """Custom type moverEntryId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_MoverEntryId_Type.__name__ = "Integer32"
_MoverEntryId_Object = MibTableColumn
moverEntryId = _MoverEntryId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 1, 1, 1),
    _MoverEntryId_Type()
)
moverEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moverEntryId.setStatus("mandatory")
_MoverState_Type = Integer32
_MoverState_Object = MibTableColumn
moverState = _MoverState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 1, 1, 2),
    _MoverState_Type()
)
moverState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moverState.setStatus("mandatory")
_MoverTimeStamp_Type = Integer32
_MoverTimeStamp_Object = MibTableColumn
moverTimeStamp = _MoverTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 1, 1, 3),
    _MoverTimeStamp_Type()
)
moverTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moverTimeStamp.setStatus("mandatory")
_MoverType_Type = Integer32
_MoverType_Object = MibTableColumn
moverType = _MoverType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 1, 1, 4),
    _MoverType_Type()
)
moverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moverType.setStatus("mandatory")
_MoverVendor_Type = DisplayString
_MoverVendor_Object = MibTableColumn
moverVendor = _MoverVendor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 1, 1, 5),
    _MoverVendor_Type()
)
moverVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moverVendor.setStatus("mandatory")
_MoverModel_Type = DisplayString
_MoverModel_Object = MibTableColumn
moverModel = _MoverModel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 1, 1, 6),
    _MoverModel_Type()
)
moverModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moverModel.setStatus("mandatory")
_MoverFwlevel_Type = DisplayString
_MoverFwlevel_Object = MibTableColumn
moverFwlevel = _MoverFwlevel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 1, 1, 7),
    _MoverFwlevel_Type()
)
moverFwlevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moverFwlevel.setStatus("mandatory")
_MoveraltVendor_Type = DisplayString
_MoveraltVendor_Object = MibTableColumn
moveraltVendor = _MoveraltVendor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 1, 1, 8),
    _MoveraltVendor_Type()
)
moveraltVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moveraltVendor.setStatus("mandatory")
_MoveraltModel_Type = DisplayString
_MoveraltModel_Object = MibTableColumn
moveraltModel = _MoveraltModel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 1, 1, 9),
    _MoveraltModel_Type()
)
moveraltModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moveraltModel.setStatus("mandatory")
_MoveraltFwlevel_Type = DisplayString
_MoveraltFwlevel_Object = MibTableColumn
moveraltFwlevel = _MoveraltFwlevel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 1, 1, 10),
    _MoveraltFwlevel_Type()
)
moveraltFwlevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moveraltFwlevel.setStatus("mandatory")
_MoverSerNum_Type = DisplayString
_MoverSerNum_Object = MibTableColumn
moverSerNum = _MoverSerNum_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 1, 1, 11),
    _MoverSerNum_Type()
)
moverSerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moverSerNum.setStatus("mandatory")
_MoverScsiId_Type = Integer32
_MoverScsiId_Object = MibTableColumn
moverScsiId = _MoverScsiId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 1, 1, 12),
    _MoverScsiId_Type()
)
moverScsiId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moverScsiId.setStatus("mandatory")
_MoverScsiLun_Type = Integer32
_MoverScsiLun_Object = MibTableColumn
moverScsiLun = _MoverScsiLun_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 1, 1, 13),
    _MoverScsiLun_Type()
)
moverScsiLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moverScsiLun.setStatus("mandatory")
_MoverDrvCnt_Type = Integer32
_MoverDrvCnt_Object = MibTableColumn
moverDrvCnt = _MoverDrvCnt_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 1, 1, 14),
    _MoverDrvCnt_Type()
)
moverDrvCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moverDrvCnt.setStatus("mandatory")
_MoverSlotCnt_Type = Integer32
_MoverSlotCnt_Object = MibTableColumn
moverSlotCnt = _MoverSlotCnt_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 1, 1, 15),
    _MoverSlotCnt_Type()
)
moverSlotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moverSlotCnt.setStatus("mandatory")
_MoverCAPCnt_Type = Integer32
_MoverCAPCnt_Object = MibTableColumn
moverCAPCnt = _MoverCAPCnt_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 1, 1, 16),
    _MoverCAPCnt_Type()
)
moverCAPCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moverCAPCnt.setStatus("mandatory")
_MoverPickerCnt_Type = Integer32
_MoverPickerCnt_Object = MibTableColumn
moverPickerCnt = _MoverPickerCnt_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 1, 1, 17),
    _MoverPickerCnt_Type()
)
moverPickerCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moverPickerCnt.setStatus("mandatory")
_MoverPicks_Type = Integer32
_MoverPicks_Object = MibTableColumn
moverPicks = _MoverPicks_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 1, 1, 18),
    _MoverPicks_Type()
)
moverPicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moverPicks.setStatus("mandatory")
_MoverPickRetries_Type = Integer32
_MoverPickRetries_Object = MibTableColumn
moverPickRetries = _MoverPickRetries_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 1, 1, 19),
    _MoverPickRetries_Type()
)
moverPickRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moverPickRetries.setStatus("optional")
_MoverPlaceRetries_Type = Integer32
_MoverPlaceRetries_Object = MibTableColumn
moverPlaceRetries = _MoverPlaceRetries_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 1, 1, 20),
    _MoverPlaceRetries_Type()
)
moverPlaceRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moverPlaceRetries.setStatus("optional")
_MoverLoadRetries_Type = Integer32
_MoverLoadRetries_Object = MibTableColumn
moverLoadRetries = _MoverLoadRetries_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 1, 1, 21),
    _MoverLoadRetries_Type()
)
moverLoadRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moverLoadRetries.setStatus("optional")
_MoverScanRetries_Type = Integer32
_MoverScanRetries_Object = MibTableColumn
moverScanRetries = _MoverScanRetries_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 1, 1, 22),
    _MoverScanRetries_Type()
)
moverScanRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moverScanRetries.setStatus("optional")


class _MoverDoorState_Type(Integer32):
    """Custom type moverDoorState based on Integer32"""
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
        *(("unknown", 1),
          ("open", 2),
          ("closed", 3),
          ("locked", 4))
    )


_MoverDoorState_Type.__name__ = "Integer32"
_MoverDoorState_Object = MibTableColumn
moverDoorState = _MoverDoorState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 1, 1, 23),
    _MoverDoorState_Type()
)
moverDoorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moverDoorState.setStatus("mandatory")


class _MoverMaillboxState_Type(Integer32):
    """Custom type moverMaillboxState based on Integer32"""
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
        *(("unknown", 1),
          ("open", 2),
          ("closed", 3),
          ("locked", 4))
    )


_MoverMaillboxState_Type.__name__ = "Integer32"
_MoverMaillboxState_Object = MibTableColumn
moverMaillboxState = _MoverMaillboxState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 1, 1, 24),
    _MoverMaillboxState_Type()
)
moverMaillboxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moverMaillboxState.setStatus("mandatory")
_TapeTable_Object = MibTable
tapeTable = _TapeTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 2)
)
if mibBuilder.loadTexts:
    tapeTable.setStatus("mandatory")
_TapeEntry_Object = MibTableRow
tapeEntry = _TapeEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 2, 1)
)
tapeEntry.setIndexNames(
    (0, "DELLPV136T-MIB", "tapeEntryId"),
)
if mibBuilder.loadTexts:
    tapeEntry.setStatus("mandatory")


class _TapeEntryId_Type(Integer32):
    """Custom type tapeEntryId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_TapeEntryId_Type.__name__ = "Integer32"
_TapeEntryId_Object = MibTableColumn
tapeEntryId = _TapeEntryId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 2, 1, 1),
    _TapeEntryId_Type()
)
tapeEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeEntryId.setStatus("mandatory")
_TapeState_Type = Integer32
_TapeState_Object = MibTableColumn
tapeState = _TapeState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 2, 1, 2),
    _TapeState_Type()
)
tapeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeState.setStatus("mandatory")
_TapeTimeStamp_Type = Integer32
_TapeTimeStamp_Object = MibTableColumn
tapeTimeStamp = _TapeTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 2, 1, 3),
    _TapeTimeStamp_Type()
)
tapeTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeTimeStamp.setStatus("mandatory")
_TapeType_Type = Integer32
_TapeType_Object = MibTableColumn
tapeType = _TapeType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 2, 1, 4),
    _TapeType_Type()
)
tapeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeType.setStatus("mandatory")
_TapeVendor_Type = DisplayString
_TapeVendor_Object = MibTableColumn
tapeVendor = _TapeVendor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 2, 1, 5),
    _TapeVendor_Type()
)
tapeVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeVendor.setStatus("mandatory")
_TapeModel_Type = DisplayString
_TapeModel_Object = MibTableColumn
tapeModel = _TapeModel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 2, 1, 6),
    _TapeModel_Type()
)
tapeModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeModel.setStatus("mandatory")
_TapeFwlevel_Type = DisplayString
_TapeFwlevel_Object = MibTableColumn
tapeFwlevel = _TapeFwlevel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 2, 1, 7),
    _TapeFwlevel_Type()
)
tapeFwlevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeFwlevel.setStatus("mandatory")
_TapealtVendor_Type = DisplayString
_TapealtVendor_Object = MibTableColumn
tapealtVendor = _TapealtVendor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 2, 1, 8),
    _TapealtVendor_Type()
)
tapealtVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapealtVendor.setStatus("mandatory")
_TapealtModel_Type = DisplayString
_TapealtModel_Object = MibTableColumn
tapealtModel = _TapealtModel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 2, 1, 9),
    _TapealtModel_Type()
)
tapealtModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapealtModel.setStatus("mandatory")
_TapealtFwlevel_Type = DisplayString
_TapealtFwlevel_Object = MibTableColumn
tapealtFwlevel = _TapealtFwlevel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 2, 1, 10),
    _TapealtFwlevel_Type()
)
tapealtFwlevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapealtFwlevel.setStatus("mandatory")
_TapeSerNum_Type = DisplayString
_TapeSerNum_Object = MibTableColumn
tapeSerNum = _TapeSerNum_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 2, 1, 11),
    _TapeSerNum_Type()
)
tapeSerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeSerNum.setStatus("mandatory")
_TapeScsiId_Type = Integer32
_TapeScsiId_Object = MibTableColumn
tapeScsiId = _TapeScsiId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 2, 1, 12),
    _TapeScsiId_Type()
)
tapeScsiId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeScsiId.setStatus("mandatory")
_TapeScsiLun_Type = Integer32
_TapeScsiLun_Object = MibTableColumn
tapeScsiLun = _TapeScsiLun_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 2, 1, 13),
    _TapeScsiLun_Type()
)
tapeScsiLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeScsiLun.setStatus("mandatory")
_TapeLibrarySN_Type = DisplayString
_TapeLibrarySN_Object = MibTableColumn
tapeLibrarySN = _TapeLibrarySN_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 2, 1, 14),
    _TapeLibrarySN_Type()
)
tapeLibrarySN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeLibrarySN.setStatus("mandatory")
_TapeTpHrs_Type = Integer32
_TapeTpHrs_Object = MibTableColumn
tapeTpHrs = _TapeTpHrs_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 2, 1, 15),
    _TapeTpHrs_Type()
)
tapeTpHrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeTpHrs.setStatus("mandatory")
_TapeClean_Type = Integer32
_TapeClean_Object = MibTableColumn
tapeClean = _TapeClean_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 2, 1, 16),
    _TapeClean_Type()
)
tapeClean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeClean.setStatus("mandatory")
_TapeLoads_Type = Integer32
_TapeLoads_Object = MibTableColumn
tapeLoads = _TapeLoads_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 2, 1, 17),
    _TapeLoads_Type()
)
tapeLoads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeLoads.setStatus("mandatory")
_TapeSoftWrtErrors_Type = Integer32
_TapeSoftWrtErrors_Object = MibTableColumn
tapeSoftWrtErrors = _TapeSoftWrtErrors_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 2, 1, 18),
    _TapeSoftWrtErrors_Type()
)
tapeSoftWrtErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeSoftWrtErrors.setStatus("mandatory")
_TapeHardWrtErrors_Type = Integer32
_TapeHardWrtErrors_Object = MibTableColumn
tapeHardWrtErrors = _TapeHardWrtErrors_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 2, 1, 19),
    _TapeHardWrtErrors_Type()
)
tapeHardWrtErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeHardWrtErrors.setStatus("mandatory")
_TapeSoftReadErrors_Type = Integer32
_TapeSoftReadErrors_Object = MibTableColumn
tapeSoftReadErrors = _TapeSoftReadErrors_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 2, 1, 20),
    _TapeSoftReadErrors_Type()
)
tapeSoftReadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeSoftReadErrors.setStatus("mandatory")
_TapeHardReadErrors_Type = Integer32
_TapeHardReadErrors_Object = MibTableColumn
tapeHardReadErrors = _TapeHardReadErrors_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 2, 1, 21),
    _TapeHardReadErrors_Type()
)
tapeHardReadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeHardReadErrors.setStatus("mandatory")
_RmuTable_Object = MibTable
rmuTable = _RmuTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 3)
)
if mibBuilder.loadTexts:
    rmuTable.setStatus("mandatory")
_RmuEntry_Object = MibTableRow
rmuEntry = _RmuEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 3, 1)
)
rmuEntry.setIndexNames(
    (0, "DELLPV136T-MIB", "rmuEntryID"),
)
if mibBuilder.loadTexts:
    rmuEntry.setStatus("mandatory")
_RmuEntryID_Type = Integer32
_RmuEntryID_Object = MibTableColumn
rmuEntryID = _RmuEntryID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 3, 1, 1),
    _RmuEntryID_Type()
)
rmuEntryID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmuEntryID.setStatus("mandatory")
_RmuMACAddress_Type = DisplayString
_RmuMACAddress_Object = MibTableColumn
rmuMACAddress = _RmuMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 3, 1, 2),
    _RmuMACAddress_Type()
)
rmuMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmuMACAddress.setStatus("mandatory")
_RmuIPAddress_Type = DisplayString
_RmuIPAddress_Object = MibTableColumn
rmuIPAddress = _RmuIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 3, 3, 1, 3),
    _RmuIPAddress_Type()
)
rmuIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmuIPAddress.setStatus("mandatory")
_LogicalDevices_ObjectIdentity = ObjectIdentity
logicalDevices = _LogicalDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 7)
)

# Managed Objects groups


# Notification objects

pV136TAgentStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 0, 1)
)
pV136TAgentStatusChange.setObjects(
      *(("DELLPV136T-MIB", "pV136TDisplayName"),
        ("DELLPV136T-MIB", "moverSerNum"),
        ("DELLPV136T-MIB", "pV136GlobalStatus"),
        ("DELLPV136T-MIB", "pV136LastGlobalStatus"))
)
if mibBuilder.loadTexts:
    pV136TAgentStatusChange.setStatus(
        ""
    )

pV136TDoorStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 0, 2)
)
pV136TDoorStateChange.setObjects(
      *(("DELLPV136T-MIB", "pV136TDisplayName"),
        ("DELLPV136T-MIB", "moverSerNum"),
        ("DELLPV136T-MIB", "moverDoorState"))
)
if mibBuilder.loadTexts:
    pV136TDoorStateChange.setStatus(
        ""
    )

pV136TMailboxStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 0, 3)
)
pV136TMailboxStateChange.setObjects(
      *(("DELLPV136T-MIB", "pV136TDisplayName"),
        ("DELLPV136T-MIB", "moverSerNum"),
        ("DELLPV136T-MIB", "moverMaillboxState"))
)
if mibBuilder.loadTexts:
    pV136TMailboxStateChange.setStatus(
        ""
    )

pV136TPowerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 0, 4)
)
pV136TPowerUp.setObjects(
      *(("DELLPV136T-MIB", "pV136TDisplayName"),
        ("DELLPV136T-MIB", "moverSerNum"),
        ("DELLPV136T-MIB", "pV136PreviousShutdownState"))
)
if mibBuilder.loadTexts:
    pV136TPowerUp.setStatus(
        ""
    )

pV136TShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 0, 5)
)
pV136TShutdown.setObjects(
      *(("DELLPV136T-MIB", "pV136TDisplayName"),
        ("DELLPV136T-MIB", "moverSerNum"),
        ("DELLPV136T-MIB", "pV136ShutdownState"))
)
if mibBuilder.loadTexts:
    pV136TShutdown.setStatus(
        ""
    )

pV136TError = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 0, 6)
)
pV136TError.setObjects(
      *(("DELLPV136T-MIB", "pV136TDisplayName"),
        ("DELLPV136T-MIB", "moverSerNum"),
        ("DELLPV136T-MIB", "pV136ErrorCode"),
        ("DELLPV136T-MIB", "pV136ErrorData"))
)
if mibBuilder.loadTexts:
    pV136TError.setStatus(
        ""
    )

pV136TSeriveActionCode = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 100, 0, 7)
)
pV136TSeriveActionCode.setObjects(
      *(("DELLPV136T-MIB", "pV136TDisplayName"),
        ("DELLPV136T-MIB", "moverSerNum"),
        ("DELLPV136T-MIB", "pV136ServiceActionCode"))
)
if mibBuilder.loadTexts:
    pV136TSeriveActionCode.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELLPV136T-MIB",
    **{"dell": dell,
       "storage": storage,
       "hardware": hardware,
       "pV136Tagent": pV136Tagent,
       "pV136TAgentStatusChange": pV136TAgentStatusChange,
       "pV136TDoorStateChange": pV136TDoorStateChange,
       "pV136TMailboxStateChange": pV136TMailboxStateChange,
       "pV136TPowerUp": pV136TPowerUp,
       "pV136TShutdown": pV136TShutdown,
       "pV136TError": pV136TError,
       "pV136TSeriveActionCode": pV136TSeriveActionCode,
       "pV136TAgentInfo": pV136TAgentInfo,
       "pV136TDisplayName": pV136TDisplayName,
       "pV136Description": pV136Description,
       "pV136AgentVendor": pV136AgentVendor,
       "pV136AgentVersion": pV136AgentVersion,
       "globalData": globalData,
       "pV136GlobalStatus": pV136GlobalStatus,
       "pV136LastGlobalStatus": pV136LastGlobalStatus,
       "pV136TimeStamp": pV136TimeStamp,
       "pV136GetTimeOut": pV136GetTimeOut,
       "pV136Modifiers": pV136Modifiers,
       "pV136RefreshRate": pV136RefreshRate,
       "pV136IPAddress": pV136IPAddress,
       "pV136HostName": pV136HostName,
       "pV136RMUVersion": pV136RMUVersion,
       "pV136ShutdownState": pV136ShutdownState,
       "pV136PreviousShutdownState": pV136PreviousShutdownState,
       "pV136ErrorCode": pV136ErrorCode,
       "pV136ErrorData": pV136ErrorData,
       "pV136ServiceActionCode": pV136ServiceActionCode,
       "pv136ServiceTag": pv136ServiceTag,
       "physicalDevices": physicalDevices,
       "moverTable": moverTable,
       "moverEntry": moverEntry,
       "moverEntryId": moverEntryId,
       "moverState": moverState,
       "moverTimeStamp": moverTimeStamp,
       "moverType": moverType,
       "moverVendor": moverVendor,
       "moverModel": moverModel,
       "moverFwlevel": moverFwlevel,
       "moveraltVendor": moveraltVendor,
       "moveraltModel": moveraltModel,
       "moveraltFwlevel": moveraltFwlevel,
       "moverSerNum": moverSerNum,
       "moverScsiId": moverScsiId,
       "moverScsiLun": moverScsiLun,
       "moverDrvCnt": moverDrvCnt,
       "moverSlotCnt": moverSlotCnt,
       "moverCAPCnt": moverCAPCnt,
       "moverPickerCnt": moverPickerCnt,
       "moverPicks": moverPicks,
       "moverPickRetries": moverPickRetries,
       "moverPlaceRetries": moverPlaceRetries,
       "moverLoadRetries": moverLoadRetries,
       "moverScanRetries": moverScanRetries,
       "moverDoorState": moverDoorState,
       "moverMaillboxState": moverMaillboxState,
       "tapeTable": tapeTable,
       "tapeEntry": tapeEntry,
       "tapeEntryId": tapeEntryId,
       "tapeState": tapeState,
       "tapeTimeStamp": tapeTimeStamp,
       "tapeType": tapeType,
       "tapeVendor": tapeVendor,
       "tapeModel": tapeModel,
       "tapeFwlevel": tapeFwlevel,
       "tapealtVendor": tapealtVendor,
       "tapealtModel": tapealtModel,
       "tapealtFwlevel": tapealtFwlevel,
       "tapeSerNum": tapeSerNum,
       "tapeScsiId": tapeScsiId,
       "tapeScsiLun": tapeScsiLun,
       "tapeLibrarySN": tapeLibrarySN,
       "tapeTpHrs": tapeTpHrs,
       "tapeClean": tapeClean,
       "tapeLoads": tapeLoads,
       "tapeSoftWrtErrors": tapeSoftWrtErrors,
       "tapeHardWrtErrors": tapeHardWrtErrors,
       "tapeSoftReadErrors": tapeSoftReadErrors,
       "tapeHardReadErrors": tapeHardReadErrors,
       "rmuTable": rmuTable,
       "rmuEntry": rmuEntry,
       "rmuEntryID": rmuEntryID,
       "rmuMACAddress": rmuMACAddress,
       "rmuIPAddress": rmuIPAddress,
       "logicalDevices": logicalDevices}
)
