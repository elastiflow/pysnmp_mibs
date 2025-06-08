# SNMP MIB module (CISCO-OPTICAL-PATCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-OPTICAL-PATCH-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:13:24 2025
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoOpticalPatchMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 67)
)
if mibBuilder.loadTexts:
    ciscoOpticalPatchMIB.setRevisions(
        ("2002-03-18 00:00",
         "2001-09-05 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_COPatchMIBObjects_ObjectIdentity = ObjectIdentity
cOPatchMIBObjects = _COPatchMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 1)
)
_COPatchInterfaceTable_Object = MibTable
cOPatchInterfaceTable = _COPatchInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 1)
)
if mibBuilder.loadTexts:
    cOPatchInterfaceTable.setStatus("deprecated")
_COPatchInterfaceEntry_Object = MibTableRow
cOPatchInterfaceEntry = _COPatchInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 1, 1)
)
cOPatchInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cOPatchInterfaceEntry.setStatus("deprecated")


class _COPatchIdentifier_Type(Integer32):
    """Custom type cOPatchIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483547),
    )


_COPatchIdentifier_Type.__name__ = "Integer32"
_COPatchIdentifier_Object = MibTableColumn
cOPatchIdentifier = _COPatchIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 1, 1, 1),
    _COPatchIdentifier_Type()
)
cOPatchIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOPatchIdentifier.setStatus("deprecated")


class _COPatchIndexNext_Type(Integer32):
    """Custom type cOPatchIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_COPatchIndexNext_Type.__name__ = "Integer32"
_COPatchIndexNext_Object = MibScalar
cOPatchIndexNext = _COPatchIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 2),
    _COPatchIndexNext_Type()
)
cOPatchIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOPatchIndexNext.setStatus("current")
_COPatchLastChange_Type = TimeStamp
_COPatchLastChange_Object = MibScalar
cOPatchLastChange = _COPatchLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 3),
    _COPatchLastChange_Type()
)
cOPatchLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOPatchLastChange.setStatus("current")


class _COPatchEventType_Type(Integer32):
    """Custom type cOPatchEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2),
          ("modify", 3))
    )


_COPatchEventType_Type.__name__ = "Integer32"
_COPatchEventType_Object = MibScalar
cOPatchEventType = _COPatchEventType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 4),
    _COPatchEventType_Type()
)
cOPatchEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cOPatchEventType.setStatus("current")
_COPatchTable_Object = MibTable
cOPatchTable = _COPatchTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 5)
)
if mibBuilder.loadTexts:
    cOPatchTable.setStatus("current")
_COPatchEntry_Object = MibTableRow
cOPatchEntry = _COPatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 5, 1)
)
cOPatchEntry.setIndexNames(
    (0, "CISCO-OPTICAL-PATCH-MIB", "cOPatchIndex"),
)
if mibBuilder.loadTexts:
    cOPatchEntry.setStatus("current")


class _COPatchIndex_Type(Integer32):
    """Custom type cOPatchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_COPatchIndex_Type.__name__ = "Integer32"
_COPatchIndex_Object = MibTableColumn
cOPatchIndex = _COPatchIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 5, 1, 1),
    _COPatchIndex_Type()
)
cOPatchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cOPatchIndex.setStatus("current")
_COPatchLowIfIndex_Type = InterfaceIndex
_COPatchLowIfIndex_Object = MibTableColumn
cOPatchLowIfIndex = _COPatchLowIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 5, 1, 2),
    _COPatchLowIfIndex_Type()
)
cOPatchLowIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cOPatchLowIfIndex.setStatus("current")
_COPatchHighIfIndex_Type = InterfaceIndex
_COPatchHighIfIndex_Object = MibTableColumn
cOPatchHighIfIndex = _COPatchHighIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 5, 1, 3),
    _COPatchHighIfIndex_Type()
)
cOPatchHighIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cOPatchHighIfIndex.setStatus("current")


class _COPatchType_Type(Integer32):
    """Custom type cOPatchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("provisioned", 1),
          ("automatic", 2),
          ("other", 3))
    )


_COPatchType_Type.__name__ = "Integer32"
_COPatchType_Object = MibTableColumn
cOPatchType = _COPatchType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 5, 1, 4),
    _COPatchType_Type()
)
cOPatchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOPatchType.setStatus("current")


class _COPatchStatus_Type(Integer32):
    """Custom type cOPatchStatus based on Integer32"""
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
        *(("noError", 1),
          ("otherError", 2),
          ("interfaceError", 3),
          ("interfaceChannelError", 4))
    )


_COPatchStatus_Type.__name__ = "Integer32"
_COPatchStatus_Object = MibTableColumn
cOPatchStatus = _COPatchStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 5, 1, 5),
    _COPatchStatus_Type()
)
cOPatchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOPatchStatus.setStatus("current")
_COPatchCreationTime_Type = TimeStamp
_COPatchCreationTime_Object = MibTableColumn
cOPatchCreationTime = _COPatchCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 5, 1, 6),
    _COPatchCreationTime_Type()
)
cOPatchCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOPatchCreationTime.setStatus("current")
_COPatchRowStatus_Type = RowStatus
_COPatchRowStatus_Object = MibTableColumn
cOPatchRowStatus = _COPatchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 5, 1, 7),
    _COPatchRowStatus_Type()
)
cOPatchRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cOPatchRowStatus.setStatus("current")


class _COPatchDirOnLowIf_Type(Integer32):
    """Custom type cOPatchDirOnLowIf based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lowIfDirReceive", 1),
          ("lowIfDirTransmit", 2),
          ("lowIfDirBoth", 3))
    )


_COPatchDirOnLowIf_Type.__name__ = "Integer32"
_COPatchDirOnLowIf_Object = MibTableColumn
cOPatchDirOnLowIf = _COPatchDirOnLowIf_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 5, 1, 8),
    _COPatchDirOnLowIf_Type()
)
cOPatchDirOnLowIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cOPatchDirOnLowIf.setStatus("current")
_COPatchLastConVerChange_Type = TimeStamp
_COPatchLastConVerChange_Object = MibTableColumn
cOPatchLastConVerChange = _COPatchLastConVerChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 5, 1, 9),
    _COPatchLastConVerChange_Type()
)
cOPatchLastConVerChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOPatchLastConVerChange.setStatus("current")


class _COPatchConVer_Type(Integer32):
    """Custom type cOPatchConVer based on Integer32"""
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
        *(("cvNotVerified", 0),
          ("cvNotMeasurable", 1),
          ("cvConnected", 2),
          ("cvDisconnected", 3),
          ("cvDisabled", 4))
    )


_COPatchConVer_Type.__name__ = "Integer32"
_COPatchConVer_Object = MibTableColumn
cOPatchConVer = _COPatchConVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 5, 1, 10),
    _COPatchConVer_Type()
)
cOPatchConVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOPatchConVer.setStatus("current")
_COPatchLastILVerChange_Type = TimeStamp
_COPatchLastILVerChange_Object = MibTableColumn
cOPatchLastILVerChange = _COPatchLastILVerChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 5, 1, 11),
    _COPatchLastILVerChange_Type()
)
cOPatchLastILVerChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOPatchLastILVerChange.setStatus("current")


class _COPatchILVer_Type(Integer32):
    """Custom type cOPatchILVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ilvNotVerified", 0),
          ("ilvNotMeasurable", 1),
          ("ilvLossOk", 2),
          ("ilvLossMinDeg", 3),
          ("ilvLossMajDeg", 4),
          ("ilvDisabled", 5))
    )


_COPatchILVer_Type.__name__ = "Integer32"
_COPatchILVer_Object = MibTableColumn
cOPatchILVer = _COPatchILVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 5, 1, 12),
    _COPatchILVer_Type()
)
cOPatchILVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOPatchILVer.setStatus("current")
_COPatchLastILVer_Type = Integer32
_COPatchLastILVer_Object = MibTableColumn
cOPatchLastILVer = _COPatchLastILVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 5, 1, 13),
    _COPatchLastILVer_Type()
)
cOPatchLastILVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOPatchLastILVer.setStatus("current")
_COPatchExcessIL_Type = Integer32
_COPatchExcessIL_Object = MibTableColumn
cOPatchExcessIL = _COPatchExcessIL_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 5, 1, 14),
    _COPatchExcessIL_Type()
)
cOPatchExcessIL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOPatchExcessIL.setStatus("current")


class _COPatchEventEnabled_Type(TruthValue):
    """Custom type cOPatchEventEnabled based on TruthValue"""
    defaultValue = 2


_COPatchEventEnabled_Type.__name__ = "TruthValue"
_COPatchEventEnabled_Object = MibScalar
cOPatchEventEnabled = _COPatchEventEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 6),
    _COPatchEventEnabled_Type()
)
cOPatchEventEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cOPatchEventEnabled.setStatus("current")
_COPatchIntfTable_Object = MibTable
cOPatchIntfTable = _COPatchIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 7)
)
if mibBuilder.loadTexts:
    cOPatchIntfTable.setStatus("current")
_COPatchIntfEntry_Object = MibTableRow
cOPatchIntfEntry = _COPatchIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 7, 1)
)
cOPatchIntfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-OPTICAL-PATCH-MIB", "cOPatchIntfDirection"),
)
if mibBuilder.loadTexts:
    cOPatchIntfEntry.setStatus("current")


class _COPatchIntfDirection_Type(Integer32):
    """Custom type cOPatchIntfDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("receive", 1),
          ("transmit", 2),
          ("both", 3))
    )


_COPatchIntfDirection_Type.__name__ = "Integer32"
_COPatchIntfDirection_Object = MibTableColumn
cOPatchIntfDirection = _COPatchIntfDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 7, 1, 1),
    _COPatchIntfDirection_Type()
)
cOPatchIntfDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cOPatchIntfDirection.setStatus("current")


class _COPatchIntfPatchId_Type(Integer32):
    """Custom type cOPatchIntfPatchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483547),
    )


_COPatchIntfPatchId_Type.__name__ = "Integer32"
_COPatchIntfPatchId_Object = MibTableColumn
cOPatchIntfPatchId = _COPatchIntfPatchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 7, 1, 2),
    _COPatchIntfPatchId_Type()
)
cOPatchIntfPatchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOPatchIntfPatchId.setStatus("current")
_COCVDefaultThresTable_Object = MibTable
cOCVDefaultThresTable = _COCVDefaultThresTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 8)
)
if mibBuilder.loadTexts:
    cOCVDefaultThresTable.setStatus("current")
_COCVDefaultThresEntry_Object = MibTableRow
cOCVDefaultThresEntry = _COCVDefaultThresEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 8, 1)
)
cOCVDefaultThresEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cOCVDefaultThresEntry.setStatus("current")


class _CODegILThreshold_Type(Integer32):
    """Custom type cODegILThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483547),
    )


_CODegILThreshold_Type.__name__ = "Integer32"
_CODegILThreshold_Object = MibTableColumn
cODegILThreshold = _CODegILThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 8, 1, 1),
    _CODegILThreshold_Type()
)
cODegILThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cODegILThreshold.setStatus("current")


class _COFailILThreshold_Type(Integer32):
    """Custom type cOFailILThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483547),
    )


_COFailILThreshold_Type.__name__ = "Integer32"
_COFailILThreshold_Object = MibTableColumn
cOFailILThreshold = _COFailILThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 8, 1, 2),
    _COFailILThreshold_Type()
)
cOFailILThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOFailILThreshold.setStatus("current")


class _COConnVerifStatus_Type(Integer32):
    """Custom type cOConnVerifStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cVNotRunning", 0),
          ("cVRunning", 1),
          ("iLRunning", 2))
    )


_COConnVerifStatus_Type.__name__ = "Integer32"
_COConnVerifStatus_Object = MibScalar
cOConnVerifStatus = _COConnVerifStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 1, 9),
    _COConnVerifStatus_Type()
)
cOConnVerifStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cOConnVerifStatus.setStatus("current")
_COPatchMIBNotifications_ObjectIdentity = ObjectIdentity
cOPatchMIBNotifications = _COPatchMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 2)
)
_COPatchMIBConformance_ObjectIdentity = ObjectIdentity
cOPatchMIBConformance = _COPatchMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 3)
)
_COPatchMIBCompliances_ObjectIdentity = ObjectIdentity
cOPatchMIBCompliances = _COPatchMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 3, 1)
)
_COPatchMIBGroups_ObjectIdentity = ObjectIdentity
cOPatchMIBGroups = _COPatchMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 3, 2)
)

# Managed Objects groups

cOPatchInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 3, 2, 1)
)
cOPatchInterfaceGroup.setObjects(
    ("CISCO-OPTICAL-PATCH-MIB", "cOPatchIdentifier")
)
if mibBuilder.loadTexts:
    cOPatchInterfaceGroup.setStatus("deprecated")

cOPatchGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 3, 2, 2)
)
cOPatchGroup.setObjects(
      *(("CISCO-OPTICAL-PATCH-MIB", "cOPatchIndexNext"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchLastChange"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchEventType"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchEventEnabled"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchLowIfIndex"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchHighIfIndex"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchType"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchStatus"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchCreationTime"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchRowStatus"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchLastConVerChange"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchConVer"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchLastILVerChange"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchILVer"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchLastILVer"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchExcessIL"))
)
if mibBuilder.loadTexts:
    cOPatchGroup.setStatus("deprecated")

cOPatchIntfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 3, 2, 4)
)
cOPatchIntfGroup.setObjects(
    ("CISCO-OPTICAL-PATCH-MIB", "cOPatchIntfPatchId")
)
if mibBuilder.loadTexts:
    cOPatchIntfGroup.setStatus("current")

cOPatchGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 3, 2, 5)
)
cOPatchGroup1.setObjects(
      *(("CISCO-OPTICAL-PATCH-MIB", "cOPatchIndexNext"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchLastChange"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchEventType"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchEventEnabled"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchLowIfIndex"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchHighIfIndex"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchType"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchStatus"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchCreationTime"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchRowStatus"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchDirOnLowIf"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchLastConVerChange"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchConVer"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchLastILVerChange"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchILVer"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchLastILVer"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchExcessIL"))
)
if mibBuilder.loadTexts:
    cOPatchGroup1.setStatus("current")


# Notification objects

cOPatchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 2, 1)
)
cOPatchEvent.setObjects(
      *(("CISCO-OPTICAL-PATCH-MIB", "cOPatchLowIfIndex"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchHighIfIndex"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchType"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchStatus"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchEventType"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchLastConVerChange"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchConVer"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchLastILVerChange"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchILVer"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchLastILVer"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchExcessIL"))
)
if mibBuilder.loadTexts:
    cOPatchEvent.setStatus(
        "current"
    )


# Notifications groups

cOPatchNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 3, 2, 3)
)
cOPatchNotifyGroup.setObjects(
    ("CISCO-OPTICAL-PATCH-MIB", "cOPatchEvent")
)
if mibBuilder.loadTexts:
    cOPatchNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cOPatchMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 3, 1, 1)
)
cOPatchMIBCompliance.setObjects(
      *(("CISCO-OPTICAL-PATCH-MIB", "cOPatchInterfaceGroup"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchGroup"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchNotifyGroup"))
)
if mibBuilder.loadTexts:
    cOPatchMIBCompliance.setStatus(
        "deprecated"
    )

cOPatchMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 67, 3, 1, 2)
)
cOPatchMIBCompliance1.setObjects(
      *(("CISCO-OPTICAL-PATCH-MIB", "cOPatchIntfGroup"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchGroup1"),
        ("CISCO-OPTICAL-PATCH-MIB", "cOPatchNotifyGroup"))
)
if mibBuilder.loadTexts:
    cOPatchMIBCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-OPTICAL-PATCH-MIB",
    **{"ciscoOpticalPatchMIB": ciscoOpticalPatchMIB,
       "cOPatchMIBObjects": cOPatchMIBObjects,
       "cOPatchInterfaceTable": cOPatchInterfaceTable,
       "cOPatchInterfaceEntry": cOPatchInterfaceEntry,
       "cOPatchIdentifier": cOPatchIdentifier,
       "cOPatchIndexNext": cOPatchIndexNext,
       "cOPatchLastChange": cOPatchLastChange,
       "cOPatchEventType": cOPatchEventType,
       "cOPatchTable": cOPatchTable,
       "cOPatchEntry": cOPatchEntry,
       "cOPatchIndex": cOPatchIndex,
       "cOPatchLowIfIndex": cOPatchLowIfIndex,
       "cOPatchHighIfIndex": cOPatchHighIfIndex,
       "cOPatchType": cOPatchType,
       "cOPatchStatus": cOPatchStatus,
       "cOPatchCreationTime": cOPatchCreationTime,
       "cOPatchRowStatus": cOPatchRowStatus,
       "cOPatchDirOnLowIf": cOPatchDirOnLowIf,
       "cOPatchLastConVerChange": cOPatchLastConVerChange,
       "cOPatchConVer": cOPatchConVer,
       "cOPatchLastILVerChange": cOPatchLastILVerChange,
       "cOPatchILVer": cOPatchILVer,
       "cOPatchLastILVer": cOPatchLastILVer,
       "cOPatchExcessIL": cOPatchExcessIL,
       "cOPatchEventEnabled": cOPatchEventEnabled,
       "cOPatchIntfTable": cOPatchIntfTable,
       "cOPatchIntfEntry": cOPatchIntfEntry,
       "cOPatchIntfDirection": cOPatchIntfDirection,
       "cOPatchIntfPatchId": cOPatchIntfPatchId,
       "cOCVDefaultThresTable": cOCVDefaultThresTable,
       "cOCVDefaultThresEntry": cOCVDefaultThresEntry,
       "cODegILThreshold": cODegILThreshold,
       "cOFailILThreshold": cOFailILThreshold,
       "cOConnVerifStatus": cOConnVerifStatus,
       "cOPatchMIBNotifications": cOPatchMIBNotifications,
       "cOPatchEvent": cOPatchEvent,
       "cOPatchMIBConformance": cOPatchMIBConformance,
       "cOPatchMIBCompliances": cOPatchMIBCompliances,
       "cOPatchMIBCompliance": cOPatchMIBCompliance,
       "cOPatchMIBCompliance1": cOPatchMIBCompliance1,
       "cOPatchMIBGroups": cOPatchMIBGroups,
       "cOPatchInterfaceGroup": cOPatchInterfaceGroup,
       "cOPatchGroup": cOPatchGroup,
       "cOPatchNotifyGroup": cOPatchNotifyGroup,
       "cOPatchIntfGroup": cOPatchIntfGroup,
       "cOPatchGroup1": cOPatchGroup1}
)
