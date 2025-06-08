# SNMP MIB module (F3-SYNC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/adva_2544/F3-SYNC-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 00:07:58 2025
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

(fsp150cm,) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "fsp150cm")

(AdminState,
 F3DisplayString,
 OperationalState,
 SecondaryState) = mibBuilder.importSymbols(
    "CM-COMMON-MIB",
    "AdminState",
    "F3DisplayString",
    "OperationalState",
    "SecondaryState")

(neIndex,
 shelfIndex,
 slotIndex) = mibBuilder.importSymbols(
    "CM-ENTITY-MIB",
    "neIndex",
    "shelfIndex",
    "slotIndex")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

f3SyncMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12)
)
if mibBuilder.loadTexts:
    f3SyncMIB.setRevisions(
        ("2010-03-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class NetworkClockType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("option1", 1),
          ("option2", 2))
    )



class ClockMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("freerun", 1),
          ("holdover", 2),
          ("tracking", 3),
          ("lossoflock", 4),
          ("locked", 5),
          ("bypass", 6))
    )



class SSMQualityLevel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("ql-dnu", 1),
          ("ql-eec1", 2),
          ("ql-eec2", 3),
          ("ql-inv", 4),
          ("ql-inv0", 5),
          ("ql-inv1", 6),
          ("ql-inv2", 7),
          ("ql-inv3", 8),
          ("ql-inv5", 9),
          ("ql-inv7", 10),
          ("ql-inv8", 11),
          ("ql-inv9", 12),
          ("ql-inv10", 13),
          ("ql-inv11", 14),
          ("ql-inv12", 15),
          ("ql-none", 16),
          ("ql-nsupp", 17),
          ("ql-prc", 18),
          ("ql-prov", 19),
          ("ql-prs", 20),
          ("ql-smc", 21),
          ("ql-ssu-a", 22),
          ("ql-ssu-b", 23),
          ("ql-st2", 24),
          ("ql-st3e", 25),
          ("ql-stu", 26),
          ("ql-tnc", 27),
          ("ql-unc", 28),
          ("ql-failed", 29),
          ("ql-inv6", 30),
          ("ql-inv13", 31),
          ("ql-inv14", 32),
          ("ql-dus", 33),
          ("ql-na", 34))
    )



class SyncRefStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("ref-ok", 1),
          ("ref-failed", 2),
          ("ref-freq-ok", 3))
    )



class SyncRefState(TextualConvention, Integer32):
    status = "current"
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
        *(("not-applicable", 0),
          ("active", 1),
          ("standby", 2),
          ("unavailable", 3),
          ("lockedout", 4))
    )



class SyncDomainType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chassis", 1),
          ("linecard", 2))
    )



class SyncOperationType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("forcedswitch", 2),
          ("manualswitch", 3),
          ("lockout", 4),
          ("clearwtr", 5),
          ("clearlockout", 6),
          ("clearswitch", 7))
    )



class SyncSelectionMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ql-mode", 1),
          ("priority-mode", 2))
    )



class SquelchControl(TextualConvention, Integer32):
    status = "current"
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
        *(("never", 1),
          ("holdover", 2),
          ("lock", 3),
          ("squelch-ql", 4))
    )



class TimeClockMode(TextualConvention, Integer32):
    status = "current"
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
        *(("freerun", 1),
          ("warmup", 2),
          ("tracking", 3),
          ("transition", 4),
          ("holdover", 5),
          ("locked", 6))
    )



class TimeTraceAbilityStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("notTraceAble", 1),
          ("timeLocked", 2),
          ("timeFreqLock", 3),
          ("timeHoldover", 4))
    )



class HoldoverAccuracy(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("time-500ns", 1),
          ("time-1000ns", 2),
          ("time-1500ns", 3),
          ("time-5000ns", 4),
          ("time-10000ns", 5))
    )



class TimeHoldoverPerformance(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("time-500ns", 1),
          ("time-1000ns", 2),
          ("time-1500ns", 3),
          ("time-5000ns", 4),
          ("time-10000ns", 5),
          ("time-0ns", 6),
          ("time-100ns", 7))
    )



class TimeSource(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("atomic", 1),
          ("gps", 2),
          ("ptp", 3),
          ("internal", 4),
          ("other", 5))
    )



# MIB Managed Objects in the order of their OIDs

_F3SyncObjects_ObjectIdentity = ObjectIdentity
f3SyncObjects = _F3SyncObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1)
)
_F3SyncTable_Object = MibTable
f3SyncTable = _F3SyncTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 1)
)
if mibBuilder.loadTexts:
    f3SyncTable.setStatus("current")
_F3SyncEntry_Object = MibTableRow
f3SyncEntry = _F3SyncEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 1, 1)
)
f3SyncEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-SYNC-MIB", "f3SyncIndex"),
)
if mibBuilder.loadTexts:
    f3SyncEntry.setStatus("current")
_F3SyncIndex_Type = Integer32
_F3SyncIndex_Object = MibTableColumn
f3SyncIndex = _F3SyncIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 1, 1, 1),
    _F3SyncIndex_Type()
)
f3SyncIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncIndex.setStatus("current")
_F3SyncAdminState_Type = AdminState
_F3SyncAdminState_Object = MibTableColumn
f3SyncAdminState = _F3SyncAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 1, 1, 2),
    _F3SyncAdminState_Type()
)
f3SyncAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncAdminState.setStatus("current")
_F3SyncOperationalState_Type = OperationalState
_F3SyncOperationalState_Object = MibTableColumn
f3SyncOperationalState = _F3SyncOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 1, 1, 3),
    _F3SyncOperationalState_Type()
)
f3SyncOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncOperationalState.setStatus("current")
_F3SyncSecondaryState_Type = SecondaryState
_F3SyncSecondaryState_Object = MibTableColumn
f3SyncSecondaryState = _F3SyncSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 1, 1, 4),
    _F3SyncSecondaryState_Type()
)
f3SyncSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncSecondaryState.setStatus("current")
_F3SyncNetworkClockType_Type = NetworkClockType
_F3SyncNetworkClockType_Object = MibTableColumn
f3SyncNetworkClockType = _F3SyncNetworkClockType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 1, 1, 5),
    _F3SyncNetworkClockType_Type()
)
f3SyncNetworkClockType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncNetworkClockType.setStatus("current")
_F3SyncSelectedReference_Type = VariablePointer
_F3SyncSelectedReference_Object = MibTableColumn
f3SyncSelectedReference = _F3SyncSelectedReference_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 1, 1, 6),
    _F3SyncSelectedReference_Type()
)
f3SyncSelectedReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncSelectedReference.setStatus("current")
_F3SyncClockMode_Type = ClockMode
_F3SyncClockMode_Object = MibTableColumn
f3SyncClockMode = _F3SyncClockMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 1, 1, 7),
    _F3SyncClockMode_Type()
)
f3SyncClockMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncClockMode.setStatus("current")
_F3SyncQL_Type = SSMQualityLevel
_F3SyncQL_Object = MibTableColumn
f3SyncQL = _F3SyncQL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 1, 1, 8),
    _F3SyncQL_Type()
)
f3SyncQL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncQL.setStatus("current")


class _F3SyncAlias_Type(DisplayString):
    """Custom type f3SyncAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3SyncAlias_Type.__name__ = "DisplayString"
_F3SyncAlias_Object = MibTableColumn
f3SyncAlias = _F3SyncAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 1, 1, 9),
    _F3SyncAlias_Type()
)
f3SyncAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3SyncAlias.setStatus("current")
_F3SyncDomain_Type = SyncDomainType
_F3SyncDomain_Object = MibTableColumn
f3SyncDomain = _F3SyncDomain_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 1, 1, 10),
    _F3SyncDomain_Type()
)
f3SyncDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncDomain.setStatus("current")
_F3SyncSelectionMode_Type = SyncSelectionMode
_F3SyncSelectionMode_Object = MibTableColumn
f3SyncSelectionMode = _F3SyncSelectionMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 1, 1, 11),
    _F3SyncSelectionMode_Type()
)
f3SyncSelectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncSelectionMode.setStatus("current")


class _F3SyncWaitToRestoreTime_Type(Integer32):
    """Custom type f3SyncWaitToRestoreTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_F3SyncWaitToRestoreTime_Type.__name__ = "Integer32"
_F3SyncWaitToRestoreTime_Object = MibTableColumn
f3SyncWaitToRestoreTime = _F3SyncWaitToRestoreTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 1, 1, 12),
    _F3SyncWaitToRestoreTime_Type()
)
f3SyncWaitToRestoreTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncWaitToRestoreTime.setStatus("current")
_F3SyncOperationSyncRef_Type = VariablePointer
_F3SyncOperationSyncRef_Object = MibTableColumn
f3SyncOperationSyncRef = _F3SyncOperationSyncRef_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 1, 1, 13),
    _F3SyncOperationSyncRef_Type()
)
f3SyncOperationSyncRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncOperationSyncRef.setStatus("current")
_F3SyncOperationType_Type = SyncOperationType
_F3SyncOperationType_Object = MibTableColumn
f3SyncOperationType = _F3SyncOperationType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 1, 1, 14),
    _F3SyncOperationType_Type()
)
f3SyncOperationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SyncOperationType.setStatus("current")
_F3SyncRefTable_Object = MibTable
f3SyncRefTable = _F3SyncRefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 2)
)
if mibBuilder.loadTexts:
    f3SyncRefTable.setStatus("current")
_F3SyncRefEntry_Object = MibTableRow
f3SyncRefEntry = _F3SyncRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 2, 1)
)
f3SyncRefEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-SYNC-MIB", "f3SyncIndex"),
    (0, "F3-SYNC-MIB", "f3SyncRefIndex"),
)
if mibBuilder.loadTexts:
    f3SyncRefEntry.setStatus("current")
_F3SyncRefIndex_Type = Integer32
_F3SyncRefIndex_Object = MibTableColumn
f3SyncRefIndex = _F3SyncRefIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 2, 1, 1),
    _F3SyncRefIndex_Type()
)
f3SyncRefIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncRefIndex.setStatus("current")
_F3SyncRefReference_Type = VariablePointer
_F3SyncRefReference_Object = MibTableColumn
f3SyncRefReference = _F3SyncRefReference_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 2, 1, 2),
    _F3SyncRefReference_Type()
)
f3SyncRefReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3SyncRefReference.setStatus("current")


class _F3SyncRefPriority_Type(Integer32):
    """Custom type f3SyncRefPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_F3SyncRefPriority_Type.__name__ = "Integer32"
_F3SyncRefPriority_Object = MibTableColumn
f3SyncRefPriority = _F3SyncRefPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 2, 1, 3),
    _F3SyncRefPriority_Type()
)
f3SyncRefPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3SyncRefPriority.setStatus("current")
_F3SyncRefStatus_Type = SyncRefStatus
_F3SyncRefStatus_Object = MibTableColumn
f3SyncRefStatus = _F3SyncRefStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 2, 1, 4),
    _F3SyncRefStatus_Type()
)
f3SyncRefStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncRefStatus.setStatus("current")
_F3SyncRefState_Type = SyncRefState
_F3SyncRefState_Object = MibTableColumn
f3SyncRefState = _F3SyncRefState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 2, 1, 5),
    _F3SyncRefState_Type()
)
f3SyncRefState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncRefState.setStatus("current")
_F3SyncRefReceivedQL_Type = SSMQualityLevel
_F3SyncRefReceivedQL_Object = MibTableColumn
f3SyncRefReceivedQL = _F3SyncRefReceivedQL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 2, 1, 6),
    _F3SyncRefReceivedQL_Type()
)
f3SyncRefReceivedQL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncRefReceivedQL.setStatus("current")
_F3SyncRefStorageType_Type = StorageType
_F3SyncRefStorageType_Object = MibTableColumn
f3SyncRefStorageType = _F3SyncRefStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 2, 1, 7),
    _F3SyncRefStorageType_Type()
)
f3SyncRefStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3SyncRefStorageType.setStatus("current")
_F3SyncRefRowStatus_Type = RowStatus
_F3SyncRefRowStatus_Object = MibTableColumn
f3SyncRefRowStatus = _F3SyncRefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 2, 1, 8),
    _F3SyncRefRowStatus_Type()
)
f3SyncRefRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3SyncRefRowStatus.setStatus("current")


class _F3SyncRefAlias_Type(DisplayString):
    """Custom type f3SyncRefAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3SyncRefAlias_Type.__name__ = "DisplayString"
_F3SyncRefAlias_Object = MibTableColumn
f3SyncRefAlias = _F3SyncRefAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 2, 1, 9),
    _F3SyncRefAlias_Type()
)
f3SyncRefAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3SyncRefAlias.setStatus("current")
_F3SyncRefEffectiveQL_Type = SSMQualityLevel
_F3SyncRefEffectiveQL_Object = MibTableColumn
f3SyncRefEffectiveQL = _F3SyncRefEffectiveQL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 2, 1, 10),
    _F3SyncRefEffectiveQL_Type()
)
f3SyncRefEffectiveQL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncRefEffectiveQL.setStatus("current")
_F3SyncRefOperationType_Type = SyncOperationType
_F3SyncRefOperationType_Object = MibTableColumn
f3SyncRefOperationType = _F3SyncRefOperationType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 2, 1, 11),
    _F3SyncRefOperationType_Type()
)
f3SyncRefOperationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SyncRefOperationType.setStatus("current")
_F3TimeClockTable_Object = MibTable
f3TimeClockTable = _F3TimeClockTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 3)
)
if mibBuilder.loadTexts:
    f3TimeClockTable.setStatus("current")
_F3TimeClockEntry_Object = MibTableRow
f3TimeClockEntry = _F3TimeClockEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 3, 1)
)
f3TimeClockEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-SYNC-MIB", "f3TimeClockIndex"),
)
if mibBuilder.loadTexts:
    f3TimeClockEntry.setStatus("current")
_F3TimeClockIndex_Type = Integer32
_F3TimeClockIndex_Object = MibTableColumn
f3TimeClockIndex = _F3TimeClockIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 3, 1, 1),
    _F3TimeClockIndex_Type()
)
f3TimeClockIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3TimeClockIndex.setStatus("current")


class _F3TimeClockAlias_Type(F3DisplayString):
    """Custom type f3TimeClockAlias based on F3DisplayString"""
    subtypeSpec = F3DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3TimeClockAlias_Type.__name__ = "F3DisplayString"
_F3TimeClockAlias_Object = MibTableColumn
f3TimeClockAlias = _F3TimeClockAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 3, 1, 2),
    _F3TimeClockAlias_Type()
)
f3TimeClockAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3TimeClockAlias.setStatus("current")
_F3TimeClockAdminState_Type = AdminState
_F3TimeClockAdminState_Object = MibTableColumn
f3TimeClockAdminState = _F3TimeClockAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 3, 1, 3),
    _F3TimeClockAdminState_Type()
)
f3TimeClockAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3TimeClockAdminState.setStatus("current")
_F3TimeClockOperationalState_Type = OperationalState
_F3TimeClockOperationalState_Object = MibTableColumn
f3TimeClockOperationalState = _F3TimeClockOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 3, 1, 4),
    _F3TimeClockOperationalState_Type()
)
f3TimeClockOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TimeClockOperationalState.setStatus("current")
_F3TimeClockSecondaryState_Type = SecondaryState
_F3TimeClockSecondaryState_Object = MibTableColumn
f3TimeClockSecondaryState = _F3TimeClockSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 3, 1, 5),
    _F3TimeClockSecondaryState_Type()
)
f3TimeClockSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TimeClockSecondaryState.setStatus("current")
_F3TimeClockSelectedReference_Type = VariablePointer
_F3TimeClockSelectedReference_Object = MibTableColumn
f3TimeClockSelectedReference = _F3TimeClockSelectedReference_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 3, 1, 6),
    _F3TimeClockSelectedReference_Type()
)
f3TimeClockSelectedReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TimeClockSelectedReference.setStatus("current")
_F3TimeClockClockMode_Type = TimeClockMode
_F3TimeClockClockMode_Object = MibTableColumn
f3TimeClockClockMode = _F3TimeClockClockMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 3, 1, 7),
    _F3TimeClockClockMode_Type()
)
f3TimeClockClockMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TimeClockClockMode.setStatus("current")
_F3TimeClockClockClass_Type = Unsigned32
_F3TimeClockClockClass_Object = MibTableColumn
f3TimeClockClockClass = _F3TimeClockClockClass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 3, 1, 8),
    _F3TimeClockClockClass_Type()
)
f3TimeClockClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TimeClockClockClass.setStatus("deprecated")
_F3TimeClockSelectionMode_Type = SyncSelectionMode
_F3TimeClockSelectionMode_Object = MibTableColumn
f3TimeClockSelectionMode = _F3TimeClockSelectionMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 3, 1, 9),
    _F3TimeClockSelectionMode_Type()
)
f3TimeClockSelectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3TimeClockSelectionMode.setStatus("current")


class _F3TimeClockWaitToRestoreTime_Type(Integer32):
    """Custom type f3TimeClockWaitToRestoreTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_F3TimeClockWaitToRestoreTime_Type.__name__ = "Integer32"
_F3TimeClockWaitToRestoreTime_Object = MibTableColumn
f3TimeClockWaitToRestoreTime = _F3TimeClockWaitToRestoreTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 3, 1, 10),
    _F3TimeClockWaitToRestoreTime_Type()
)
f3TimeClockWaitToRestoreTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3TimeClockWaitToRestoreTime.setStatus("current")
_F3TimeClockOperationTimeClockRef_Type = VariablePointer
_F3TimeClockOperationTimeClockRef_Object = MibTableColumn
f3TimeClockOperationTimeClockRef = _F3TimeClockOperationTimeClockRef_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 3, 1, 11),
    _F3TimeClockOperationTimeClockRef_Type()
)
f3TimeClockOperationTimeClockRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3TimeClockOperationTimeClockRef.setStatus("current")
_F3TimeClockOperationType_Type = SyncOperationType
_F3TimeClockOperationType_Object = MibTableColumn
f3TimeClockOperationType = _F3TimeClockOperationType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 3, 1, 12),
    _F3TimeClockOperationType_Type()
)
f3TimeClockOperationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3TimeClockOperationType.setStatus("current")
_F3TimeClockLeap59_Type = TruthValue
_F3TimeClockLeap59_Object = MibTableColumn
f3TimeClockLeap59 = _F3TimeClockLeap59_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 3, 1, 13),
    _F3TimeClockLeap59_Type()
)
f3TimeClockLeap59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TimeClockLeap59.setStatus("current")
_F3TimeClockLeap61_Type = TruthValue
_F3TimeClockLeap61_Object = MibTableColumn
f3TimeClockLeap61 = _F3TimeClockLeap61_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 3, 1, 14),
    _F3TimeClockLeap61_Type()
)
f3TimeClockLeap61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TimeClockLeap61.setStatus("current")
_F3TimeClockTimeTraceAbilityStatus_Type = TimeTraceAbilityStatus
_F3TimeClockTimeTraceAbilityStatus_Object = MibTableColumn
f3TimeClockTimeTraceAbilityStatus = _F3TimeClockTimeTraceAbilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 3, 1, 15),
    _F3TimeClockTimeTraceAbilityStatus_Type()
)
f3TimeClockTimeTraceAbilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TimeClockTimeTraceAbilityStatus.setStatus("current")
_F3TimeClockExpectedQL_Type = SSMQualityLevel
_F3TimeClockExpectedQL_Object = MibTableColumn
f3TimeClockExpectedQL = _F3TimeClockExpectedQL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 3, 1, 16),
    _F3TimeClockExpectedQL_Type()
)
f3TimeClockExpectedQL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3TimeClockExpectedQL.setStatus("current")
_F3TimeClockCurrentQL_Type = SSMQualityLevel
_F3TimeClockCurrentQL_Object = MibTableColumn
f3TimeClockCurrentQL = _F3TimeClockCurrentQL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 3, 1, 17),
    _F3TimeClockCurrentQL_Type()
)
f3TimeClockCurrentQL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TimeClockCurrentQL.setStatus("current")
_F3TimeClockSyncRefCandidate_Type = TruthValue
_F3TimeClockSyncRefCandidate_Object = MibTableColumn
f3TimeClockSyncRefCandidate = _F3TimeClockSyncRefCandidate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 3, 1, 18),
    _F3TimeClockSyncRefCandidate_Type()
)
f3TimeClockSyncRefCandidate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3TimeClockSyncRefCandidate.setStatus("current")
_F3TimeClockTimeHoldoverPerformance_Type = TimeHoldoverPerformance
_F3TimeClockTimeHoldoverPerformance_Object = MibTableColumn
f3TimeClockTimeHoldoverPerformance = _F3TimeClockTimeHoldoverPerformance_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 3, 1, 19),
    _F3TimeClockTimeHoldoverPerformance_Type()
)
f3TimeClockTimeHoldoverPerformance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3TimeClockTimeHoldoverPerformance.setStatus("current")
_F3TimeClockUtcOffset_Type = Unsigned32
_F3TimeClockUtcOffset_Object = MibTableColumn
f3TimeClockUtcOffset = _F3TimeClockUtcOffset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 3, 1, 20),
    _F3TimeClockUtcOffset_Type()
)
f3TimeClockUtcOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TimeClockUtcOffset.setStatus("current")
_F3TimeClockCurrentTimeOfDay_Type = DateAndTime
_F3TimeClockCurrentTimeOfDay_Object = MibTableColumn
f3TimeClockCurrentTimeOfDay = _F3TimeClockCurrentTimeOfDay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 3, 1, 21),
    _F3TimeClockCurrentTimeOfDay_Type()
)
f3TimeClockCurrentTimeOfDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TimeClockCurrentTimeOfDay.setStatus("current")
_F3TimeClockFrequencyReference_Type = VariablePointer
_F3TimeClockFrequencyReference_Object = MibTableColumn
f3TimeClockFrequencyReference = _F3TimeClockFrequencyReference_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 3, 1, 22),
    _F3TimeClockFrequencyReference_Type()
)
f3TimeClockFrequencyReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3TimeClockFrequencyReference.setStatus("current")
_F3TimeClockFrequencyClockMode_Type = TimeClockMode
_F3TimeClockFrequencyClockMode_Object = MibTableColumn
f3TimeClockFrequencyClockMode = _F3TimeClockFrequencyClockMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 3, 1, 23),
    _F3TimeClockFrequencyClockMode_Type()
)
f3TimeClockFrequencyClockMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TimeClockFrequencyClockMode.setStatus("current")
_F3TimeClockRefTable_Object = MibTable
f3TimeClockRefTable = _F3TimeClockRefTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 4)
)
if mibBuilder.loadTexts:
    f3TimeClockRefTable.setStatus("current")
_F3TimeClockRefEntry_Object = MibTableRow
f3TimeClockRefEntry = _F3TimeClockRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 4, 1)
)
f3TimeClockRefEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-SYNC-MIB", "f3TimeClockIndex"),
    (0, "F3-SYNC-MIB", "f3TimeClockRefIndex"),
)
if mibBuilder.loadTexts:
    f3TimeClockRefEntry.setStatus("current")
_F3TimeClockRefIndex_Type = Integer32
_F3TimeClockRefIndex_Object = MibTableColumn
f3TimeClockRefIndex = _F3TimeClockRefIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 4, 1, 1),
    _F3TimeClockRefIndex_Type()
)
f3TimeClockRefIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3TimeClockRefIndex.setStatus("current")


class _F3TimeClockRefAlias_Type(F3DisplayString):
    """Custom type f3TimeClockRefAlias based on F3DisplayString"""
    subtypeSpec = F3DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3TimeClockRefAlias_Type.__name__ = "F3DisplayString"
_F3TimeClockRefAlias_Object = MibTableColumn
f3TimeClockRefAlias = _F3TimeClockRefAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 4, 1, 2),
    _F3TimeClockRefAlias_Type()
)
f3TimeClockRefAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TimeClockRefAlias.setStatus("current")
_F3TimeClockRefReference_Type = VariablePointer
_F3TimeClockRefReference_Object = MibTableColumn
f3TimeClockRefReference = _F3TimeClockRefReference_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 4, 1, 3),
    _F3TimeClockRefReference_Type()
)
f3TimeClockRefReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TimeClockRefReference.setStatus("current")


class _F3TimeClockRefPriority_Type(Integer32):
    """Custom type f3TimeClockRefPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_F3TimeClockRefPriority_Type.__name__ = "Integer32"
_F3TimeClockRefPriority_Object = MibTableColumn
f3TimeClockRefPriority = _F3TimeClockRefPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 4, 1, 4),
    _F3TimeClockRefPriority_Type()
)
f3TimeClockRefPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TimeClockRefPriority.setStatus("current")
_F3TimeClockRefStatus_Type = SyncRefStatus
_F3TimeClockRefStatus_Object = MibTableColumn
f3TimeClockRefStatus = _F3TimeClockRefStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 4, 1, 5),
    _F3TimeClockRefStatus_Type()
)
f3TimeClockRefStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TimeClockRefStatus.setStatus("current")
_F3TimeClockRefState_Type = SyncRefState
_F3TimeClockRefState_Object = MibTableColumn
f3TimeClockRefState = _F3TimeClockRefState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 4, 1, 6),
    _F3TimeClockRefState_Type()
)
f3TimeClockRefState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TimeClockRefState.setStatus("current")
_F3TimeClockRefOperationType_Type = SyncOperationType
_F3TimeClockRefOperationType_Object = MibTableColumn
f3TimeClockRefOperationType = _F3TimeClockRefOperationType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 4, 1, 7),
    _F3TimeClockRefOperationType_Type()
)
f3TimeClockRefOperationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3TimeClockRefOperationType.setStatus("current")
_F3TimeClockRefStorageType_Type = StorageType
_F3TimeClockRefStorageType_Object = MibTableColumn
f3TimeClockRefStorageType = _F3TimeClockRefStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 4, 1, 8),
    _F3TimeClockRefStorageType_Type()
)
f3TimeClockRefStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TimeClockRefStorageType.setStatus("current")
_F3TimeClockRefRowStatus_Type = RowStatus
_F3TimeClockRefRowStatus_Object = MibTableColumn
f3TimeClockRefRowStatus = _F3TimeClockRefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 1, 4, 1, 9),
    _F3TimeClockRefRowStatus_Type()
)
f3TimeClockRefRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3TimeClockRefRowStatus.setStatus("current")
_F3SyncConformance_ObjectIdentity = ObjectIdentity
f3SyncConformance = _F3SyncConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 2)
)
_F3SyncCompliances_ObjectIdentity = ObjectIdentity
f3SyncCompliances = _F3SyncCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 2, 1)
)
_F3SyncGroups_ObjectIdentity = ObjectIdentity
f3SyncGroups = _F3SyncGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 2, 2)
)

# Managed Objects groups

f3SyncObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 2, 2, 1)
)
f3SyncObjectGroup.setObjects(
      *(("F3-SYNC-MIB", "f3SyncIndex"),
        ("F3-SYNC-MIB", "f3SyncAdminState"),
        ("F3-SYNC-MIB", "f3SyncOperationalState"),
        ("F3-SYNC-MIB", "f3SyncSecondaryState"),
        ("F3-SYNC-MIB", "f3SyncNetworkClockType"),
        ("F3-SYNC-MIB", "f3SyncSelectedReference"),
        ("F3-SYNC-MIB", "f3SyncClockMode"),
        ("F3-SYNC-MIB", "f3SyncQL"),
        ("F3-SYNC-MIB", "f3SyncAlias"),
        ("F3-SYNC-MIB", "f3SyncDomain"),
        ("F3-SYNC-MIB", "f3SyncSelectionMode"),
        ("F3-SYNC-MIB", "f3SyncWaitToRestoreTime"),
        ("F3-SYNC-MIB", "f3SyncOperationSyncRef"),
        ("F3-SYNC-MIB", "f3SyncOperationType"),
        ("F3-SYNC-MIB", "f3SyncRefIndex"),
        ("F3-SYNC-MIB", "f3SyncRefReference"),
        ("F3-SYNC-MIB", "f3SyncRefPriority"),
        ("F3-SYNC-MIB", "f3SyncRefStatus"),
        ("F3-SYNC-MIB", "f3SyncRefState"),
        ("F3-SYNC-MIB", "f3SyncRefReceivedQL"),
        ("F3-SYNC-MIB", "f3SyncRefStorageType"),
        ("F3-SYNC-MIB", "f3SyncRefRowStatus"),
        ("F3-SYNC-MIB", "f3SyncRefAlias"),
        ("F3-SYNC-MIB", "f3SyncRefEffectiveQL"),
        ("F3-SYNC-MIB", "f3SyncRefOperationType"))
)
if mibBuilder.loadTexts:
    f3SyncObjectGroup.setStatus("current")

f3TimeClockObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 2, 2, 2)
)
f3TimeClockObjectGroup.setObjects(
      *(("F3-SYNC-MIB", "f3TimeClockIndex"),
        ("F3-SYNC-MIB", "f3TimeClockAlias"),
        ("F3-SYNC-MIB", "f3TimeClockAdminState"),
        ("F3-SYNC-MIB", "f3TimeClockOperationalState"),
        ("F3-SYNC-MIB", "f3TimeClockSecondaryState"),
        ("F3-SYNC-MIB", "f3TimeClockSelectedReference"),
        ("F3-SYNC-MIB", "f3TimeClockClockMode"),
        ("F3-SYNC-MIB", "f3TimeClockClockClass"),
        ("F3-SYNC-MIB", "f3TimeClockSelectionMode"),
        ("F3-SYNC-MIB", "f3TimeClockWaitToRestoreTime"),
        ("F3-SYNC-MIB", "f3TimeClockOperationTimeClockRef"),
        ("F3-SYNC-MIB", "f3TimeClockOperationType"),
        ("F3-SYNC-MIB", "f3TimeClockLeap59"),
        ("F3-SYNC-MIB", "f3TimeClockLeap61"),
        ("F3-SYNC-MIB", "f3TimeClockTimeTraceAbilityStatus"),
        ("F3-SYNC-MIB", "f3TimeClockExpectedQL"),
        ("F3-SYNC-MIB", "f3TimeClockCurrentQL"),
        ("F3-SYNC-MIB", "f3TimeClockSyncRefCandidate"),
        ("F3-SYNC-MIB", "f3TimeClockTimeHoldoverPerformance"),
        ("F3-SYNC-MIB", "f3TimeClockUtcOffset"),
        ("F3-SYNC-MIB", "f3TimeClockCurrentTimeOfDay"),
        ("F3-SYNC-MIB", "f3TimeClockRefIndex"),
        ("F3-SYNC-MIB", "f3TimeClockRefAlias"),
        ("F3-SYNC-MIB", "f3TimeClockRefReference"),
        ("F3-SYNC-MIB", "f3TimeClockRefPriority"),
        ("F3-SYNC-MIB", "f3TimeClockRefStatus"),
        ("F3-SYNC-MIB", "f3TimeClockRefState"),
        ("F3-SYNC-MIB", "f3TimeClockRefOperationType"),
        ("F3-SYNC-MIB", "f3TimeClockRefStorageType"),
        ("F3-SYNC-MIB", "f3TimeClockRefRowStatus"))
)
if mibBuilder.loadTexts:
    f3TimeClockObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

f3SyncCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 12, 2, 1, 1)
)
f3SyncCompliance.setObjects(
    ("F3-SYNC-MIB", "f3SyncObjectGroup")
)
if mibBuilder.loadTexts:
    f3SyncCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F3-SYNC-MIB",
    **{"NetworkClockType": NetworkClockType,
       "ClockMode": ClockMode,
       "SSMQualityLevel": SSMQualityLevel,
       "SyncRefStatus": SyncRefStatus,
       "SyncRefState": SyncRefState,
       "SyncDomainType": SyncDomainType,
       "SyncOperationType": SyncOperationType,
       "SyncSelectionMode": SyncSelectionMode,
       "SquelchControl": SquelchControl,
       "TimeClockMode": TimeClockMode,
       "TimeTraceAbilityStatus": TimeTraceAbilityStatus,
       "HoldoverAccuracy": HoldoverAccuracy,
       "TimeHoldoverPerformance": TimeHoldoverPerformance,
       "TimeSource": TimeSource,
       "f3SyncMIB": f3SyncMIB,
       "f3SyncObjects": f3SyncObjects,
       "f3SyncTable": f3SyncTable,
       "f3SyncEntry": f3SyncEntry,
       "f3SyncIndex": f3SyncIndex,
       "f3SyncAdminState": f3SyncAdminState,
       "f3SyncOperationalState": f3SyncOperationalState,
       "f3SyncSecondaryState": f3SyncSecondaryState,
       "f3SyncNetworkClockType": f3SyncNetworkClockType,
       "f3SyncSelectedReference": f3SyncSelectedReference,
       "f3SyncClockMode": f3SyncClockMode,
       "f3SyncQL": f3SyncQL,
       "f3SyncAlias": f3SyncAlias,
       "f3SyncDomain": f3SyncDomain,
       "f3SyncSelectionMode": f3SyncSelectionMode,
       "f3SyncWaitToRestoreTime": f3SyncWaitToRestoreTime,
       "f3SyncOperationSyncRef": f3SyncOperationSyncRef,
       "f3SyncOperationType": f3SyncOperationType,
       "f3SyncRefTable": f3SyncRefTable,
       "f3SyncRefEntry": f3SyncRefEntry,
       "f3SyncRefIndex": f3SyncRefIndex,
       "f3SyncRefReference": f3SyncRefReference,
       "f3SyncRefPriority": f3SyncRefPriority,
       "f3SyncRefStatus": f3SyncRefStatus,
       "f3SyncRefState": f3SyncRefState,
       "f3SyncRefReceivedQL": f3SyncRefReceivedQL,
       "f3SyncRefStorageType": f3SyncRefStorageType,
       "f3SyncRefRowStatus": f3SyncRefRowStatus,
       "f3SyncRefAlias": f3SyncRefAlias,
       "f3SyncRefEffectiveQL": f3SyncRefEffectiveQL,
       "f3SyncRefOperationType": f3SyncRefOperationType,
       "f3TimeClockTable": f3TimeClockTable,
       "f3TimeClockEntry": f3TimeClockEntry,
       "f3TimeClockIndex": f3TimeClockIndex,
       "f3TimeClockAlias": f3TimeClockAlias,
       "f3TimeClockAdminState": f3TimeClockAdminState,
       "f3TimeClockOperationalState": f3TimeClockOperationalState,
       "f3TimeClockSecondaryState": f3TimeClockSecondaryState,
       "f3TimeClockSelectedReference": f3TimeClockSelectedReference,
       "f3TimeClockClockMode": f3TimeClockClockMode,
       "f3TimeClockClockClass": f3TimeClockClockClass,
       "f3TimeClockSelectionMode": f3TimeClockSelectionMode,
       "f3TimeClockWaitToRestoreTime": f3TimeClockWaitToRestoreTime,
       "f3TimeClockOperationTimeClockRef": f3TimeClockOperationTimeClockRef,
       "f3TimeClockOperationType": f3TimeClockOperationType,
       "f3TimeClockLeap59": f3TimeClockLeap59,
       "f3TimeClockLeap61": f3TimeClockLeap61,
       "f3TimeClockTimeTraceAbilityStatus": f3TimeClockTimeTraceAbilityStatus,
       "f3TimeClockExpectedQL": f3TimeClockExpectedQL,
       "f3TimeClockCurrentQL": f3TimeClockCurrentQL,
       "f3TimeClockSyncRefCandidate": f3TimeClockSyncRefCandidate,
       "f3TimeClockTimeHoldoverPerformance": f3TimeClockTimeHoldoverPerformance,
       "f3TimeClockUtcOffset": f3TimeClockUtcOffset,
       "f3TimeClockCurrentTimeOfDay": f3TimeClockCurrentTimeOfDay,
       "f3TimeClockFrequencyReference": f3TimeClockFrequencyReference,
       "f3TimeClockFrequencyClockMode": f3TimeClockFrequencyClockMode,
       "f3TimeClockRefTable": f3TimeClockRefTable,
       "f3TimeClockRefEntry": f3TimeClockRefEntry,
       "f3TimeClockRefIndex": f3TimeClockRefIndex,
       "f3TimeClockRefAlias": f3TimeClockRefAlias,
       "f3TimeClockRefReference": f3TimeClockRefReference,
       "f3TimeClockRefPriority": f3TimeClockRefPriority,
       "f3TimeClockRefStatus": f3TimeClockRefStatus,
       "f3TimeClockRefState": f3TimeClockRefState,
       "f3TimeClockRefOperationType": f3TimeClockRefOperationType,
       "f3TimeClockRefStorageType": f3TimeClockRefStorageType,
       "f3TimeClockRefRowStatus": f3TimeClockRefRowStatus,
       "f3SyncConformance": f3SyncConformance,
       "f3SyncCompliances": f3SyncCompliances,
       "f3SyncCompliance": f3SyncCompliance,
       "f3SyncGroups": f3SyncGroups,
       "f3SyncObjectGroup": f3SyncObjectGroup,
       "f3TimeClockObjectGroup": f3TimeClockObjectGroup}
)
