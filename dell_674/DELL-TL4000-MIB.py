# SNMP MIB module (DELL-TL4000-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/dell_674/DELL-TL4000-MIB.mib
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
_TL4000_ObjectIdentity = ObjectIdentity
TL4000 = _TL4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102)
)
_TL4000Id_ObjectIdentity = ObjectIdentity
TL4000Id = _TL4000Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 1)
)
_TL4000IdDisplayName_Type = DisplayString
_TL4000IdDisplayName_Object = MibScalar
tL4000IdDisplayName = _TL4000IdDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 1, 1),
    _TL4000IdDisplayName_Type()
)
tL4000IdDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tL4000IdDisplayName.setStatus("mandatory")
_TL4000IdDescription_Type = DisplayString
_TL4000IdDescription_Object = MibScalar
tL4000IdDescription = _TL4000IdDescription_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 1, 2),
    _TL4000IdDescription_Type()
)
tL4000IdDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tL4000IdDescription.setStatus("mandatory")
_TL4000AgentVendor_Type = DisplayString
_TL4000AgentVendor_Object = MibScalar
tL4000AgentVendor = _TL4000AgentVendor_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 1, 3),
    _TL4000AgentVendor_Type()
)
tL4000AgentVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tL4000AgentVendor.setStatus("mandatory")
_TL4000IdAgentVersion_Type = DisplayString
_TL4000IdAgentVersion_Object = MibScalar
tL4000IdAgentVersion = _TL4000IdAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 1, 4),
    _TL4000IdAgentVersion_Type()
)
tL4000IdAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tL4000IdAgentVersion.setStatus("mandatory")
_TL4000IdBuildNumber_Type = DisplayString
_TL4000IdBuildNumber_Object = MibScalar
tL4000IdBuildNumber = _TL4000IdBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 1, 5),
    _TL4000IdBuildNumber_Type()
)
tL4000IdBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tL4000IdBuildNumber.setStatus("mandatory")
_TL4000IdURL_Type = DisplayString
_TL4000IdURL_Object = MibScalar
tL4000IdURL = _TL4000IdURL_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 1, 6),
    _TL4000IdURL_Type()
)
tL4000IdURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tL4000IdURL.setStatus("mandatory")
_TL4000Status_ObjectIdentity = ObjectIdentity
TL4000Status = _TL4000Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 2)
)


class _TL4000StatusGlobalStatus_Type(Integer32):
    """Custom type tL4000StatusGlobalStatus based on Integer32"""
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


_TL4000StatusGlobalStatus_Type.__name__ = "Integer32"
_TL4000StatusGlobalStatus_Object = MibScalar
tL4000StatusGlobalStatus = _TL4000StatusGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 2, 1),
    _TL4000StatusGlobalStatus_Type()
)
tL4000StatusGlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tL4000StatusGlobalStatus.setStatus("mandatory")


class _TL4000StatusLastGlobalStatus_Type(Integer32):
    """Custom type tL4000StatusLastGlobalStatus based on Integer32"""
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


_TL4000StatusLastGlobalStatus_Type.__name__ = "Integer32"
_TL4000StatusLastGlobalStatus_Object = MibScalar
tL4000StatusLastGlobalStatus = _TL4000StatusLastGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 2, 2),
    _TL4000StatusLastGlobalStatus_Type()
)
tL4000StatusLastGlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tL4000StatusLastGlobalStatus.setStatus("mandatory")
_TL4000StatusTimeStamp_Type = Integer32
_TL4000StatusTimeStamp_Object = MibScalar
tL4000StatusTimeStamp = _TL4000StatusTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 2, 3),
    _TL4000StatusTimeStamp_Type()
)
tL4000StatusTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tL4000StatusTimeStamp.setStatus("mandatory")


class _TL4000StatusGetTimeOut_Type(Integer32):
    """Custom type tL4000StatusGetTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_TL4000StatusGetTimeOut_Type.__name__ = "Integer32"
_TL4000StatusGetTimeOut_Object = MibScalar
tL4000StatusGetTimeOut = _TL4000StatusGetTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 2, 4),
    _TL4000StatusGetTimeOut_Type()
)
tL4000StatusGetTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tL4000StatusGetTimeOut.setStatus("mandatory")


class _TL4000StatusRefreshRate_Type(Integer32):
    """Custom type tL4000StatusRefreshRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000000000),
    )


_TL4000StatusRefreshRate_Type.__name__ = "Integer32"
_TL4000StatusRefreshRate_Object = MibScalar
tL4000StatusRefreshRate = _TL4000StatusRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 2, 5),
    _TL4000StatusRefreshRate_Type()
)
tL4000StatusRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tL4000StatusRefreshRate.setStatus("mandatory")


class _TL4000StatusGeneratingTrapFlag_Type(Integer32):
    """Custom type tL4000StatusGeneratingTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("disabled", 3))
    )


_TL4000StatusGeneratingTrapFlag_Type.__name__ = "Integer32"
_TL4000StatusGeneratingTrapFlag_Object = MibScalar
tL4000StatusGeneratingTrapFlag = _TL4000StatusGeneratingTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 2, 6),
    _TL4000StatusGeneratingTrapFlag_Type()
)
tL4000StatusGeneratingTrapFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tL4000StatusGeneratingTrapFlag.setStatus("mandatory")
_TL4000Physical_ObjectIdentity = ObjectIdentity
TL4000Physical = _TL4000Physical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3)
)
_LibraryTable_Object = MibTable
libraryTable = _LibraryTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 1)
)
if mibBuilder.loadTexts:
    libraryTable.setStatus("mandatory")
_LibraryEntry_Object = MibTableRow
libraryEntry = _LibraryEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 1, 1)
)
libraryEntry.setIndexNames(
    (0, "DELL-TL4000-MIB", "libraryEntryId"),
)
if mibBuilder.loadTexts:
    libraryEntry.setStatus("mandatory")


class _LibraryEntryId_Type(Integer32):
    """Custom type libraryEntryId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_LibraryEntryId_Type.__name__ = "Integer32"
_LibraryEntryId_Object = MibTableColumn
libraryEntryId = _LibraryEntryId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 1, 1, 1),
    _LibraryEntryId_Type()
)
libraryEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    libraryEntryId.setStatus("mandatory")
_LibraryState_Type = Integer32
_LibraryState_Object = MibTableColumn
libraryState = _LibraryState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 1, 1, 2),
    _LibraryState_Type()
)
libraryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    libraryState.setStatus("mandatory")
_LibraryTimeStamp_Type = Integer32
_LibraryTimeStamp_Object = MibTableColumn
libraryTimeStamp = _LibraryTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 1, 1, 3),
    _LibraryTimeStamp_Type()
)
libraryTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    libraryTimeStamp.setStatus("mandatory")
_LibraryType_Type = Integer32
_LibraryType_Object = MibTableColumn
libraryType = _LibraryType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 1, 1, 4),
    _LibraryType_Type()
)
libraryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    libraryType.setStatus("mandatory")
_LibraryScsiId_Type = Integer32
_LibraryScsiId_Object = MibTableColumn
libraryScsiId = _LibraryScsiId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 1, 1, 5),
    _LibraryScsiId_Type()
)
libraryScsiId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    libraryScsiId.setStatus("mandatory")
_LibraryScsiLun_Type = Integer32
_LibraryScsiLun_Object = MibTableColumn
libraryScsiLun = _LibraryScsiLun_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 1, 1, 6),
    _LibraryScsiLun_Type()
)
libraryScsiLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    libraryScsiLun.setStatus("mandatory")
_LibraryVendorId_Type = DisplayString
_LibraryVendorId_Object = MibTableColumn
libraryVendorId = _LibraryVendorId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 1, 1, 7),
    _LibraryVendorId_Type()
)
libraryVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    libraryVendorId.setStatus("mandatory")
_LibraryProductId_Type = DisplayString
_LibraryProductId_Object = MibTableColumn
libraryProductId = _LibraryProductId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 1, 1, 8),
    _LibraryProductId_Type()
)
libraryProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    libraryProductId.setStatus("mandatory")
_LibraryFwLevel_Type = DisplayString
_LibraryFwLevel_Object = MibTableColumn
libraryFwLevel = _LibraryFwLevel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 1, 1, 9),
    _LibraryFwLevel_Type()
)
libraryFwLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    libraryFwLevel.setStatus("mandatory")
_LibrarySerNum_Type = DisplayString
_LibrarySerNum_Object = MibTableColumn
librarySerNum = _LibrarySerNum_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 1, 1, 10),
    _LibrarySerNum_Type()
)
librarySerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    librarySerNum.setStatus("mandatory")
_LibraryDrvCnt_Type = Integer32
_LibraryDrvCnt_Object = MibTableColumn
libraryDrvCnt = _LibraryDrvCnt_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 1, 1, 11),
    _LibraryDrvCnt_Type()
)
libraryDrvCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    libraryDrvCnt.setStatus("mandatory")
_LibrarySlotCnt_Type = Integer32
_LibrarySlotCnt_Object = MibTableColumn
librarySlotCnt = _LibrarySlotCnt_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 1, 1, 12),
    _LibrarySlotCnt_Type()
)
librarySlotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    librarySlotCnt.setStatus("mandatory")
_LibraryImpExpCnt_Type = Integer32
_LibraryImpExpCnt_Object = MibTableColumn
libraryImpExpCnt = _LibraryImpExpCnt_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 1, 1, 13),
    _LibraryImpExpCnt_Type()
)
libraryImpExpCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    libraryImpExpCnt.setStatus("mandatory")
_LibraryTranspCnt_Type = Integer32
_LibraryTranspCnt_Object = MibTableColumn
libraryTranspCnt = _LibraryTranspCnt_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 1, 1, 14),
    _LibraryTranspCnt_Type()
)
libraryTranspCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    libraryTranspCnt.setStatus("mandatory")
_LibraryMoves_Type = Integer32
_LibraryMoves_Object = MibTableColumn
libraryMoves = _LibraryMoves_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 1, 1, 15),
    _LibraryMoves_Type()
)
libraryMoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    libraryMoves.setStatus("mandatory")
_LibrarySlotFetchRetries_Type = Integer32
_LibrarySlotFetchRetries_Object = MibTableColumn
librarySlotFetchRetries = _LibrarySlotFetchRetries_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 1, 1, 16),
    _LibrarySlotFetchRetries_Type()
)
librarySlotFetchRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    librarySlotFetchRetries.setStatus("optional")
_LibrarySlotStowRetries_Type = Integer32
_LibrarySlotStowRetries_Object = MibTableColumn
librarySlotStowRetries = _LibrarySlotStowRetries_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 1, 1, 17),
    _LibrarySlotStowRetries_Type()
)
librarySlotStowRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    librarySlotStowRetries.setStatus("optional")
_LibraryDrvFetchRetries_Type = Integer32
_LibraryDrvFetchRetries_Object = MibTableColumn
libraryDrvFetchRetries = _LibraryDrvFetchRetries_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 1, 1, 18),
    _LibraryDrvFetchRetries_Type()
)
libraryDrvFetchRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    libraryDrvFetchRetries.setStatus("optional")
_LibraryDrvStowRetries_Type = Integer32
_LibraryDrvStowRetries_Object = MibTableColumn
libraryDrvStowRetries = _LibraryDrvStowRetries_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 1, 1, 19),
    _LibraryDrvStowRetries_Type()
)
libraryDrvStowRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    libraryDrvStowRetries.setStatus("optional")


class _LibraryDoorState_Type(Integer32):
    """Custom type libraryDoorState based on Integer32"""
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


_LibraryDoorState_Type.__name__ = "Integer32"
_LibraryDoorState_Object = MibTableColumn
libraryDoorState = _LibraryDoorState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 1, 1, 20),
    _LibraryDoorState_Type()
)
libraryDoorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    libraryDoorState.setStatus("mandatory")


class _LibraryImpExpState_Type(Integer32):
    """Custom type libraryImpExpState based on Integer32"""
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


_LibraryImpExpState_Type.__name__ = "Integer32"
_LibraryImpExpState_Object = MibTableColumn
libraryImpExpState = _LibraryImpExpState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 1, 1, 21),
    _LibraryImpExpState_Type()
)
libraryImpExpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    libraryImpExpState.setStatus("mandatory")
_LibraryFaultFSC_Type = Integer32
_LibraryFaultFSC_Object = MibTableColumn
libraryFaultFSC = _LibraryFaultFSC_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 1, 1, 22),
    _LibraryFaultFSC_Type()
)
libraryFaultFSC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    libraryFaultFSC.setStatus("optional")


class _LibraryFaultSev_Type(Integer32):
    """Custom type libraryFaultSev based on Integer32"""
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
        *(("informational", 1),
          ("minor", 2),
          ("major", 3),
          ("critical", 4))
    )


_LibraryFaultSev_Type.__name__ = "Integer32"
_LibraryFaultSev_Object = MibTableColumn
libraryFaultSev = _LibraryFaultSev_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 1, 1, 23),
    _LibraryFaultSev_Type()
)
libraryFaultSev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    libraryFaultSev.setStatus("optional")
_LibraryFaultDescr_Type = DisplayString
_LibraryFaultDescr_Object = MibTableColumn
libraryFaultDescr = _LibraryFaultDescr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 1, 1, 24),
    _LibraryFaultDescr_Type()
)
libraryFaultDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    libraryFaultDescr.setStatus("optional")
_DriveTable_Object = MibTable
driveTable = _DriveTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 2)
)
if mibBuilder.loadTexts:
    driveTable.setStatus("mandatory")
_DriveEntry_Object = MibTableRow
driveEntry = _DriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 2, 1)
)
driveEntry.setIndexNames(
    (0, "DELL-TL4000-MIB", "driveEntryId"),
)
if mibBuilder.loadTexts:
    driveEntry.setStatus("mandatory")


class _DriveEntryId_Type(Integer32):
    """Custom type driveEntryId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_DriveEntryId_Type.__name__ = "Integer32"
_DriveEntryId_Object = MibTableColumn
driveEntryId = _DriveEntryId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 2, 1, 1),
    _DriveEntryId_Type()
)
driveEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveEntryId.setStatus("mandatory")
_DriveState_Type = Integer32
_DriveState_Object = MibTableColumn
driveState = _DriveState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 2, 1, 2),
    _DriveState_Type()
)
driveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveState.setStatus("mandatory")
_DriveTimeStamp_Type = Integer32
_DriveTimeStamp_Object = MibTableColumn
driveTimeStamp = _DriveTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 2, 1, 3),
    _DriveTimeStamp_Type()
)
driveTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveTimeStamp.setStatus("mandatory")
_DriveType_Type = Integer32
_DriveType_Object = MibTableColumn
driveType = _DriveType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 2, 1, 4),
    _DriveType_Type()
)
driveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveType.setStatus("mandatory")
_DriveScsiId_Type = Integer32
_DriveScsiId_Object = MibTableColumn
driveScsiId = _DriveScsiId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 2, 1, 5),
    _DriveScsiId_Type()
)
driveScsiId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveScsiId.setStatus("mandatory")
_DriveScsiLun_Type = Integer32
_DriveScsiLun_Object = MibTableColumn
driveScsiLun = _DriveScsiLun_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 2, 1, 6),
    _DriveScsiLun_Type()
)
driveScsiLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveScsiLun.setStatus("mandatory")
_DriveVendorId_Type = DisplayString
_DriveVendorId_Object = MibTableColumn
driveVendorId = _DriveVendorId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 2, 1, 7),
    _DriveVendorId_Type()
)
driveVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveVendorId.setStatus("mandatory")
_DriveProductId_Type = DisplayString
_DriveProductId_Object = MibTableColumn
driveProductId = _DriveProductId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 2, 1, 8),
    _DriveProductId_Type()
)
driveProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveProductId.setStatus("mandatory")
_DriveFwlevel_Type = DisplayString
_DriveFwlevel_Object = MibTableColumn
driveFwlevel = _DriveFwlevel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 2, 1, 9),
    _DriveFwlevel_Type()
)
driveFwlevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveFwlevel.setStatus("mandatory")
_DriveSerNum_Type = DisplayString
_DriveSerNum_Object = MibTableColumn
driveSerNum = _DriveSerNum_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 2, 1, 10),
    _DriveSerNum_Type()
)
driveSerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveSerNum.setStatus("mandatory")
_DriveLibrarySN_Type = DisplayString
_DriveLibrarySN_Object = MibTableColumn
driveLibrarySN = _DriveLibrarySN_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 2, 1, 11),
    _DriveLibrarySN_Type()
)
driveLibrarySN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveLibrarySN.setStatus("mandatory")
_DriveTpHrs_Type = Integer32
_DriveTpHrs_Object = MibTableColumn
driveTpHrs = _DriveTpHrs_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 2, 1, 12),
    _DriveTpHrs_Type()
)
driveTpHrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveTpHrs.setStatus("mandatory")
_DriveClean_Type = Integer32
_DriveClean_Object = MibTableColumn
driveClean = _DriveClean_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 2, 1, 13),
    _DriveClean_Type()
)
driveClean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveClean.setStatus("mandatory")
_DriveLoads_Type = Integer32
_DriveLoads_Object = MibTableColumn
driveLoads = _DriveLoads_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 2, 1, 14),
    _DriveLoads_Type()
)
driveLoads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveLoads.setStatus("mandatory")
_DriveSoftWrtErrors_Type = Integer32
_DriveSoftWrtErrors_Object = MibTableColumn
driveSoftWrtErrors = _DriveSoftWrtErrors_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 2, 1, 15),
    _DriveSoftWrtErrors_Type()
)
driveSoftWrtErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveSoftWrtErrors.setStatus("mandatory")
_DriveHardWrtErrors_Type = Integer32
_DriveHardWrtErrors_Object = MibTableColumn
driveHardWrtErrors = _DriveHardWrtErrors_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 2, 1, 16),
    _DriveHardWrtErrors_Type()
)
driveHardWrtErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveHardWrtErrors.setStatus("mandatory")
_DriveSoftReadErrors_Type = Integer32
_DriveSoftReadErrors_Object = MibTableColumn
driveSoftReadErrors = _DriveSoftReadErrors_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 2, 1, 17),
    _DriveSoftReadErrors_Type()
)
driveSoftReadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveSoftReadErrors.setStatus("mandatory")
_DriveHardReadErrors_Type = Integer32
_DriveHardReadErrors_Object = MibTableColumn
driveHardReadErrors = _DriveHardReadErrors_Object(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 3, 2, 1, 18),
    _DriveHardReadErrors_Type()
)
driveHardReadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveHardReadErrors.setStatus("mandatory")
_TL4000Event_ObjectIdentity = ObjectIdentity
TL4000Event = _TL4000Event_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 4)
)

# Managed Objects groups


# Notification objects

eventStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 4, 0, 1)
)
eventStatusChange.setObjects(
      *(("DELL-TL4000-MIB", "libraryProductId"),
        ("DELL-TL4000-MIB", "librarySerNum"),
        ("DELL-TL4000-MIB", "TL4000StatusLastGlobalStatus"),
        ("DELL-TL4000-MIB", "TL4000StatusGlobalStatus"))
)
if mibBuilder.loadTexts:
    eventStatusChange.setStatus(
        ""
    )

eventDoorOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 4, 0, 2)
)
eventDoorOpen.setObjects(
      *(("DELL-TL4000-MIB", "libraryProductId"),
        ("DELL-TL4000-MIB", "librarySerNum"))
)
if mibBuilder.loadTexts:
    eventDoorOpen.setStatus(
        ""
    )

eventMailSlotAccessed = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 4, 0, 3)
)
eventMailSlotAccessed.setObjects(
      *(("DELL-TL4000-MIB", "libraryProductId"),
        ("DELL-TL4000-MIB", "librarySerNum"))
)
if mibBuilder.loadTexts:
    eventMailSlotAccessed.setStatus(
        ""
    )

eventFaultPosted = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 4, 0, 4)
)
eventFaultPosted.setObjects(
      *(("DELL-TL4000-MIB", "libraryProductId"),
        ("DELL-TL4000-MIB", "librarySerNum"),
        ("DELL-TL4000-MIB", "libraryFaultSev"),
        ("DELL-TL4000-MIB", "libraryFaultFSC"),
        ("DELL-TL4000-MIB", "libraryFaultDescr"))
)
if mibBuilder.loadTexts:
    eventFaultPosted.setStatus(
        ""
    )

eventRequestDriveClean = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 4, 0, 5)
)
eventRequestDriveClean.setObjects(
      *(("DELL-TL4000-MIB", "libraryProductId"),
        ("DELL-TL4000-MIB", "librarySerNum"))
)
if mibBuilder.loadTexts:
    eventRequestDriveClean.setStatus(
        ""
    )

eventDriveError = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 4, 0, 6)
)
eventDriveError.setObjects(
      *(("DELL-TL4000-MIB", "libraryProductId"),
        ("DELL-TL4000-MIB", "librarySerNum"))
)
if mibBuilder.loadTexts:
    eventDriveError.setStatus(
        ""
    )

eventLoaderRetriesExcessive = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 4, 0, 7)
)
eventLoaderRetriesExcessive.setObjects(
      *(("DELL-TL4000-MIB", "libraryProductId"),
        ("DELL-TL4000-MIB", "librarySerNum"))
)
if mibBuilder.loadTexts:
    eventLoaderRetriesExcessive.setStatus(
        ""
    )

eventLoaderOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10893, 2, 102, 4, 0, 8)
)
eventLoaderOK.setObjects(
      *(("DELL-TL4000-MIB", "libraryProductId"),
        ("DELL-TL4000-MIB", "librarySerNum"))
)
if mibBuilder.loadTexts:
    eventLoaderOK.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELL-TL4000-MIB",
    **{"dell": dell,
       "storage": storage,
       "hardware": hardware,
       "TL4000": TL4000,
       "TL4000Id": TL4000Id,
       "tL4000IdDisplayName": tL4000IdDisplayName,
       "tL4000IdDescription": tL4000IdDescription,
       "tL4000AgentVendor": tL4000AgentVendor,
       "tL4000IdAgentVersion": tL4000IdAgentVersion,
       "tL4000IdBuildNumber": tL4000IdBuildNumber,
       "tL4000IdURL": tL4000IdURL,
       "TL4000Status": TL4000Status,
       "tL4000StatusGlobalStatus": tL4000StatusGlobalStatus,
       "tL4000StatusLastGlobalStatus": tL4000StatusLastGlobalStatus,
       "tL4000StatusTimeStamp": tL4000StatusTimeStamp,
       "tL4000StatusGetTimeOut": tL4000StatusGetTimeOut,
       "tL4000StatusRefreshRate": tL4000StatusRefreshRate,
       "tL4000StatusGeneratingTrapFlag": tL4000StatusGeneratingTrapFlag,
       "TL4000Physical": TL4000Physical,
       "libraryTable": libraryTable,
       "libraryEntry": libraryEntry,
       "libraryEntryId": libraryEntryId,
       "libraryState": libraryState,
       "libraryTimeStamp": libraryTimeStamp,
       "libraryType": libraryType,
       "libraryScsiId": libraryScsiId,
       "libraryScsiLun": libraryScsiLun,
       "libraryVendorId": libraryVendorId,
       "libraryProductId": libraryProductId,
       "libraryFwLevel": libraryFwLevel,
       "librarySerNum": librarySerNum,
       "libraryDrvCnt": libraryDrvCnt,
       "librarySlotCnt": librarySlotCnt,
       "libraryImpExpCnt": libraryImpExpCnt,
       "libraryTranspCnt": libraryTranspCnt,
       "libraryMoves": libraryMoves,
       "librarySlotFetchRetries": librarySlotFetchRetries,
       "librarySlotStowRetries": librarySlotStowRetries,
       "libraryDrvFetchRetries": libraryDrvFetchRetries,
       "libraryDrvStowRetries": libraryDrvStowRetries,
       "libraryDoorState": libraryDoorState,
       "libraryImpExpState": libraryImpExpState,
       "libraryFaultFSC": libraryFaultFSC,
       "libraryFaultSev": libraryFaultSev,
       "libraryFaultDescr": libraryFaultDescr,
       "driveTable": driveTable,
       "driveEntry": driveEntry,
       "driveEntryId": driveEntryId,
       "driveState": driveState,
       "driveTimeStamp": driveTimeStamp,
       "driveType": driveType,
       "driveScsiId": driveScsiId,
       "driveScsiLun": driveScsiLun,
       "driveVendorId": driveVendorId,
       "driveProductId": driveProductId,
       "driveFwlevel": driveFwlevel,
       "driveSerNum": driveSerNum,
       "driveLibrarySN": driveLibrarySN,
       "driveTpHrs": driveTpHrs,
       "driveClean": driveClean,
       "driveLoads": driveLoads,
       "driveSoftWrtErrors": driveSoftWrtErrors,
       "driveHardWrtErrors": driveHardWrtErrors,
       "driveSoftReadErrors": driveSoftReadErrors,
       "driveHardReadErrors": driveHardReadErrors,
       "TL4000Event": TL4000Event,
       "eventStatusChange": eventStatusChange,
       "eventDoorOpen": eventDoorOpen,
       "eventMailSlotAccessed": eventMailSlotAccessed,
       "eventFaultPosted": eventFaultPosted,
       "eventRequestDriveClean": eventRequestDriveClean,
       "eventDriveError": eventDriveError,
       "eventLoaderRetriesExcessive": eventLoaderRetriesExcessive,
       "eventLoaderOK": eventLoaderOK}
)
