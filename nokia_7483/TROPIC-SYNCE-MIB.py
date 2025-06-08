# SNMP MIB module (TROPIC-SYNCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TROPIC-SYNCE-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:59:16 2025
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

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(tnPortModules,
 tnSyncEMIB) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnPortModules",
    "tnSyncEMIB")

(tnShelfIndex,) = mibBuilder.importSymbols(
    "TROPIC-SHELF-MIB",
    "tnShelfIndex")

(tnSlotIndex,) = mibBuilder.importSymbols(
    "TROPIC-SLOT-MIB",
    "tnSlotIndex")


# MODULE-IDENTITY

tnSyncEMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 4, 6)
)
if mibBuilder.loadTexts:
    tnSyncEMibModule.setRevisions(
        ("2010-11-22 12:00",
         "2010-11-30 12:00",
         "2011-07-22 12:00",
         "2011-08-19 12:00",
         "2011-12-21 12:00",
         "2012-05-08 12:00",
         "2012-09-01 12:00",
         "2012-12-20 12:00",
         "2013-06-01 12:00",
         "2013-07-12 12:00",
         "2013-08-26 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnSyncEConf_ObjectIdentity = ObjectIdentity
tnSyncEConf = _TnSyncEConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 1)
)
_TnSyncEGroups_ObjectIdentity = ObjectIdentity
tnSyncEGroups = _TnSyncEGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 1, 1)
)
_TnSyncECompliances_ObjectIdentity = ObjectIdentity
tnSyncECompliances = _TnSyncECompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 1, 2)
)
_TnSyncEObjs_ObjectIdentity = ObjectIdentity
tnSyncEObjs = _TnSyncEObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2)
)
_TnSyncEBasics_ObjectIdentity = ObjectIdentity
tnSyncEBasics = _TnSyncEBasics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1)
)
_TnSyncETable_Object = MibTable
tnSyncETable = _TnSyncETable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tnSyncETable.setStatus("current")
_TnSyncEEntry_Object = MibTableRow
tnSyncEEntry = _TnSyncEEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 1, 1)
)
tnSyncEEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnSyncEEntry.setStatus("current")


class _TnSyncESyncMsg_Type(TruthValue):
    """Custom type tnSyncESyncMsg based on TruthValue"""
    defaultValue = 2


_TnSyncESyncMsg_Type.__name__ = "TruthValue"
_TnSyncESyncMsg_Object = MibTableColumn
tnSyncESyncMsg = _TnSyncESyncMsg_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 1, 1, 1),
    _TnSyncESyncMsg_Type()
)
tnSyncESyncMsg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSyncESyncMsg.setStatus("current")


class _TnSyncEActiveRef_Type(Integer32):
    """Custom type tnSyncEActiveRef based on Integer32"""
    defaultValue = 1

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
          ("lineRef0", 2),
          ("lineRef1", 3),
          ("lineRef2", 4),
          ("lineRef3", 5),
          ("lineRef4", 6),
          ("lineRef5", 7))
    )


_TnSyncEActiveRef_Type.__name__ = "Integer32"
_TnSyncEActiveRef_Object = MibTableColumn
tnSyncEActiveRef = _TnSyncEActiveRef_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 1, 1, 2),
    _TnSyncEActiveRef_Type()
)
tnSyncEActiveRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSyncEActiveRef.setStatus("current")


class _TnSyncEWTR_Type(Unsigned32):
    """Custom type tnSyncEWTR based on Unsigned32"""
    defaultValue = 5


_TnSyncEWTR_Type.__name__ = "Unsigned32"
_TnSyncEWTR_Object = MibTableColumn
tnSyncEWTR = _TnSyncEWTR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 1, 1, 3),
    _TnSyncEWTR_Type()
)
tnSyncEWTR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSyncEWTR.setStatus("current")
_TnSyncESwCmdLineRef_Type = Unsigned32
_TnSyncESwCmdLineRef_Object = MibTableColumn
tnSyncESwCmdLineRef = _TnSyncESwCmdLineRef_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 1, 1, 4),
    _TnSyncESwCmdLineRef_Type()
)
tnSyncESwCmdLineRef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSyncESwCmdLineRef.setStatus("current")


class _TnSyncEClkModState_Type(Integer32):
    """Custom type tnSyncEClkModState based on Integer32"""
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
        *(("unknown", 1),
          ("locked", 2),
          ("autonomousHoldOver", 3),
          ("autonomousFreeRunning", 4),
          ("forcedFreeRunning", 5))
    )


_TnSyncEClkModState_Type.__name__ = "Integer32"
_TnSyncEClkModState_Object = MibTableColumn
tnSyncEClkModState = _TnSyncEClkModState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 1, 1, 5),
    _TnSyncEClkModState_Type()
)
tnSyncEClkModState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSyncEClkModState.setStatus("current")
_TnSyncESystemQL_Type = Integer32
_TnSyncESystemQL_Object = MibTableColumn
tnSyncESystemQL = _TnSyncESystemQL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 1, 1, 6),
    _TnSyncESystemQL_Type()
)
tnSyncESystemQL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSyncESystemQL.setStatus("current")
_TnSyncELineRefTable_Object = MibTable
tnSyncELineRefTable = _TnSyncELineRefTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tnSyncELineRefTable.setStatus("current")
_TnSyncELineRefEntry_Object = MibTableRow
tnSyncELineRefEntry = _TnSyncELineRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 2, 1)
)
tnSyncELineRefEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
    (0, "TROPIC-SYNCE-MIB", "tnSyncELineRefIndex"),
)
if mibBuilder.loadTexts:
    tnSyncELineRefEntry.setStatus("current")
_TnSyncELineRefIndex_Type = Unsigned32
_TnSyncELineRefIndex_Object = MibTableColumn
tnSyncELineRefIndex = _TnSyncELineRefIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 2, 1, 1),
    _TnSyncELineRefIndex_Type()
)
tnSyncELineRefIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSyncELineRefIndex.setStatus("current")


class _TnSyncELineRefAssignedPort_Type(Integer32):
    """Custom type tnSyncELineRefAssignedPort based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              34,
              35,
              36,
              37)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("l1", 2),
          ("l2", 3),
          ("c1", 4),
          ("c2", 5),
          ("c3", 6),
          ("c4", 7),
          ("c5", 8),
          ("c6", 9),
          ("c7", 10),
          ("c8", 11),
          ("c9", 12),
          ("c10", 13),
          ("c11", 14),
          ("c12", 15),
          ("c13", 16),
          ("c14", 17),
          ("c15", 18),
          ("c16", 19),
          ("c17", 20),
          ("c18", 21),
          ("c19", 22),
          ("c20", 23),
          ("c21", 24),
          ("c22", 25),
          ("c23", 26),
          ("c24", 27),
          ("x1", 28),
          ("x2", 29),
          ("x3", 30),
          ("x4", 31),
          ("x5", 32),
          ("x6", 33),
          ("m1", 34),
          ("m2", 35),
          ("m3", 36),
          ("m4", 37))
    )


_TnSyncELineRefAssignedPort_Type.__name__ = "Integer32"
_TnSyncELineRefAssignedPort_Object = MibTableColumn
tnSyncELineRefAssignedPort = _TnSyncELineRefAssignedPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 2, 1, 2),
    _TnSyncELineRefAssignedPort_Type()
)
tnSyncELineRefAssignedPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSyncELineRefAssignedPort.setStatus("current")


class _TnSyncELineRefPriority_Type(Unsigned32):
    """Custom type tnSyncELineRefPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_TnSyncELineRefPriority_Type.__name__ = "Unsigned32"
_TnSyncELineRefPriority_Object = MibTableColumn
tnSyncELineRefPriority = _TnSyncELineRefPriority_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 2, 1, 3),
    _TnSyncELineRefPriority_Type()
)
tnSyncELineRefPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSyncELineRefPriority.setStatus("current")


class _TnSyncELineRefAdminState_Type(Integer32):
    """Custom type tnSyncELineRefAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_TnSyncELineRefAdminState_Type.__name__ = "Integer32"
_TnSyncELineRefAdminState_Object = MibTableColumn
tnSyncELineRefAdminState = _TnSyncELineRefAdminState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 2, 1, 4),
    _TnSyncELineRefAdminState_Type()
)
tnSyncELineRefAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSyncELineRefAdminState.setStatus("current")


class _TnSyncELineRefOperState_Type(Integer32):
    """Custom type tnSyncELineRefOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_TnSyncELineRefOperState_Type.__name__ = "Integer32"
_TnSyncELineRefOperState_Object = MibTableColumn
tnSyncELineRefOperState = _TnSyncELineRefOperState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 2, 1, 5),
    _TnSyncELineRefOperState_Type()
)
tnSyncELineRefOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSyncELineRefOperState.setStatus("current")
_TnSyncELineLockOut_Type = TruthValue
_TnSyncELineLockOut_Object = MibTableColumn
tnSyncELineLockOut = _TnSyncELineLockOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 2, 1, 6),
    _TnSyncELineLockOut_Type()
)
tnSyncELineLockOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSyncELineLockOut.setStatus("current")


class _TnSyncELineRefState_Type(Integer32):
    """Custom type tnSyncELineRefState based on Integer32"""
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
        *(("notAssigned", 1),
          ("normal", 2),
          ("signalFailure", 3),
          ("wtr", 4))
    )


_TnSyncELineRefState_Type.__name__ = "Integer32"
_TnSyncELineRefState_Object = MibTableColumn
tnSyncELineRefState = _TnSyncELineRefState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 2, 1, 7),
    _TnSyncELineRefState_Type()
)
tnSyncELineRefState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSyncELineRefState.setStatus("current")


class _TnSyncELineRefSwState_Type(Integer32):
    """Custom type tnSyncELineRefSwState based on Integer32"""
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
        *(("nocmd", 1),
          ("forced", 2),
          ("mansw", 3),
          ("lockout", 4),
          ("wtr", 5))
    )


_TnSyncELineRefSwState_Type.__name__ = "Integer32"
_TnSyncELineRefSwState_Object = MibTableColumn
tnSyncELineRefSwState = _TnSyncELineRefSwState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 2, 1, 8),
    _TnSyncELineRefSwState_Type()
)
tnSyncELineRefSwState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSyncELineRefSwState.setStatus("current")
_TnSyncELineRefIncSSMMsg_Type = Integer32
_TnSyncELineRefIncSSMMsg_Object = MibTableColumn
tnSyncELineRefIncSSMMsg = _TnSyncELineRefIncSSMMsg_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 2, 1, 9),
    _TnSyncELineRefIncSSMMsg_Type()
)
tnSyncELineRefIncSSMMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSyncELineRefIncSSMMsg.setStatus("current")
_TnSyncELineRefIncSSMStatus_Type = Integer32
_TnSyncELineRefIncSSMStatus_Object = MibTableColumn
tnSyncELineRefIncSSMStatus = _TnSyncELineRefIncSSMStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 2, 1, 10),
    _TnSyncELineRefIncSSMStatus_Type()
)
tnSyncELineRefIncSSMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSyncELineRefIncSSMStatus.setStatus("current")


class _TnSyncELineRefIncSSMSupp_Type(Integer32):
    """Custom type tnSyncELineRefIncSSMSupp based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TnSyncELineRefIncSSMSupp_Type.__name__ = "Integer32"
_TnSyncELineRefIncSSMSupp_Object = MibTableColumn
tnSyncELineRefIncSSMSupp = _TnSyncELineRefIncSSMSupp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 2, 1, 11),
    _TnSyncELineRefIncSSMSupp_Type()
)
tnSyncELineRefIncSSMSupp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSyncELineRefIncSSMSupp.setStatus("current")


class _TnSyncELineRefProvQL_Type(Integer32):
    """Custom type tnSyncELineRefProvQL based on Integer32"""
    defaultValue = 0


_TnSyncELineRefProvQL_Type.__name__ = "Integer32"
_TnSyncELineRefProvQL_Object = MibTableColumn
tnSyncELineRefProvQL = _TnSyncELineRefProvQL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 2, 1, 12),
    _TnSyncELineRefProvQL_Type()
)
tnSyncELineRefProvQL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSyncELineRefProvQL.setStatus("current")


class _TnSyncELineRefAssociatedPort_Type(InterfaceIndexOrZero):
    """Custom type tnSyncELineRefAssociatedPort based on InterfaceIndexOrZero"""
    defaultValue = 0


_TnSyncELineRefAssociatedPort_Type.__name__ = "InterfaceIndexOrZero"
_TnSyncELineRefAssociatedPort_Object = MibTableColumn
tnSyncELineRefAssociatedPort = _TnSyncELineRefAssociatedPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 2, 1, 13),
    _TnSyncELineRefAssociatedPort_Type()
)
tnSyncELineRefAssociatedPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSyncELineRefAssociatedPort.setStatus("current")


class _TnSyncELineRefPriorityOfStationClock_Type(Unsigned32):
    """Custom type tnSyncELineRefPriorityOfStationClock based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_TnSyncELineRefPriorityOfStationClock_Type.__name__ = "Unsigned32"
_TnSyncELineRefPriorityOfStationClock_Object = MibTableColumn
tnSyncELineRefPriorityOfStationClock = _TnSyncELineRefPriorityOfStationClock_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 2, 1, 14),
    _TnSyncELineRefPriorityOfStationClock_Type()
)
tnSyncELineRefPriorityOfStationClock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSyncELineRefPriorityOfStationClock.setStatus("current")
_TnSyncELineRefLockOutOfStationClock_Type = TruthValue
_TnSyncELineRefLockOutOfStationClock_Object = MibTableColumn
tnSyncELineRefLockOutOfStationClock = _TnSyncELineRefLockOutOfStationClock_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 2, 1, 15),
    _TnSyncELineRefLockOutOfStationClock_Type()
)
tnSyncELineRefLockOutOfStationClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSyncELineRefLockOutOfStationClock.setStatus("current")


class _TnSyncELineRefSwStateOfStationClock_Type(Integer32):
    """Custom type tnSyncELineRefSwStateOfStationClock based on Integer32"""
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
        *(("nocmd", 1),
          ("forced", 2),
          ("mansw", 3),
          ("lockout", 4),
          ("wtr", 5))
    )


_TnSyncELineRefSwStateOfStationClock_Type.__name__ = "Integer32"
_TnSyncELineRefSwStateOfStationClock_Object = MibTableColumn
tnSyncELineRefSwStateOfStationClock = _TnSyncELineRefSwStateOfStationClock_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 2, 1, 16),
    _TnSyncELineRefSwStateOfStationClock_Type()
)
tnSyncELineRefSwStateOfStationClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSyncELineRefSwStateOfStationClock.setStatus("current")
_TnSyncEControlTable_Object = MibTable
tnSyncEControlTable = _TnSyncEControlTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 3)
)
if mibBuilder.loadTexts:
    tnSyncEControlTable.setStatus("current")
_TnSyncEControlEntry_Object = MibTableRow
tnSyncEControlEntry = _TnSyncEControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 3, 1)
)
tnSyncEControlEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnSyncEControlEntry.setStatus("current")


class _TnSyncEControlEECEnable_Type(Integer32):
    """Custom type tnSyncEControlEECEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TnSyncEControlEECEnable_Type.__name__ = "Integer32"
_TnSyncEControlEECEnable_Object = MibTableColumn
tnSyncEControlEECEnable = _TnSyncEControlEECEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 3, 1, 1),
    _TnSyncEControlEECEnable_Type()
)
tnSyncEControlEECEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSyncEControlEECEnable.setStatus("current")
_TnSyncEPortTable_Object = MibTable
tnSyncEPortTable = _TnSyncEPortTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 4)
)
if mibBuilder.loadTexts:
    tnSyncEPortTable.setStatus("current")
_TnSyncEPortEntry_Object = MibTableRow
tnSyncEPortEntry = _TnSyncEPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 4, 1)
)
tnSyncEPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnSyncEPortEntry.setStatus("current")


class _TnSyncEOprMode_Type(Integer32):
    """Custom type tnSyncEOprMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sync", 1),
          ("non-sync", 2))
    )


_TnSyncEOprMode_Type.__name__ = "Integer32"
_TnSyncEOprMode_Object = MibTableColumn
tnSyncEOprMode = _TnSyncEOprMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 4, 1, 1),
    _TnSyncEOprMode_Type()
)
tnSyncEOprMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSyncEOprMode.setStatus("current")


class _TnSyncEOutgoingForceSsmTrans_Type(Integer32):
    """Custom type tnSyncEOutgoingForceSsmTrans based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("act", 1),
          ("prc", 2),
          ("ssua", 3),
          ("ssub", 4),
          ("sec", 5),
          ("dnu", 6),
          ("stu", 7),
          ("prs", 8),
          ("st2", 9),
          ("sts3e", 10),
          ("st3", 11),
          ("none", 12),
          ("dus", 13))
    )


_TnSyncEOutgoingForceSsmTrans_Type.__name__ = "Integer32"
_TnSyncEOutgoingForceSsmTrans_Object = MibTableColumn
tnSyncEOutgoingForceSsmTrans = _TnSyncEOutgoingForceSsmTrans_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 4, 1, 2),
    _TnSyncEOutgoingForceSsmTrans_Type()
)
tnSyncEOutgoingForceSsmTrans.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSyncEOutgoingForceSsmTrans.setStatus("current")
_TnSyncEStationClockTable_Object = MibTable
tnSyncEStationClockTable = _TnSyncEStationClockTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 5)
)
if mibBuilder.loadTexts:
    tnSyncEStationClockTable.setStatus("current")
_TnSyncEStationClockEntry_Object = MibTableRow
tnSyncEStationClockEntry = _TnSyncEStationClockEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 5, 1)
)
tnSyncEStationClockEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnSyncEStationClockEntry.setStatus("current")
_TnSyncEStationClockSyncMsg_Type = TruthValue
_TnSyncEStationClockSyncMsg_Object = MibTableColumn
tnSyncEStationClockSyncMsg = _TnSyncEStationClockSyncMsg_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 5, 1, 1),
    _TnSyncEStationClockSyncMsg_Type()
)
tnSyncEStationClockSyncMsg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSyncEStationClockSyncMsg.setStatus("current")


class _TnSyncEStationClockActiveRef_Type(Integer32):
    """Custom type tnSyncEStationClockActiveRef based on Integer32"""
    defaultValue = 1

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
          ("lineRef0", 2),
          ("lineRef1", 3),
          ("lineRef2", 4),
          ("lineRef3", 5),
          ("lineRef4", 6),
          ("lineRef5", 7))
    )


_TnSyncEStationClockActiveRef_Type.__name__ = "Integer32"
_TnSyncEStationClockActiveRef_Object = MibTableColumn
tnSyncEStationClockActiveRef = _TnSyncEStationClockActiveRef_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 5, 1, 2),
    _TnSyncEStationClockActiveRef_Type()
)
tnSyncEStationClockActiveRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSyncEStationClockActiveRef.setStatus("current")


class _TnSyncEStationClockWTR_Type(Unsigned32):
    """Custom type tnSyncEStationClockWTR based on Unsigned32"""
    defaultValue = 5


_TnSyncEStationClockWTR_Type.__name__ = "Unsigned32"
_TnSyncEStationClockWTR_Object = MibTableColumn
tnSyncEStationClockWTR = _TnSyncEStationClockWTR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 5, 1, 3),
    _TnSyncEStationClockWTR_Type()
)
tnSyncEStationClockWTR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSyncEStationClockWTR.setStatus("current")
_TnSyncEStationClockSwCmdLineRef_Type = Unsigned32
_TnSyncEStationClockSwCmdLineRef_Object = MibTableColumn
tnSyncEStationClockSwCmdLineRef = _TnSyncEStationClockSwCmdLineRef_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 5, 1, 4),
    _TnSyncEStationClockSwCmdLineRef_Type()
)
tnSyncEStationClockSwCmdLineRef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSyncEStationClockSwCmdLineRef.setStatus("current")
_TnSyncEStationClockSystemQL_Type = Integer32
_TnSyncEStationClockSystemQL_Object = MibTableColumn
tnSyncEStationClockSystemQL = _TnSyncEStationClockSystemQL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 5, 1, 5),
    _TnSyncEStationClockSystemQL_Type()
)
tnSyncEStationClockSystemQL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSyncEStationClockSystemQL.setStatus("current")


class _TnSyncEStationClockQLThreshold_Type(Integer32):
    """Custom type tnSyncEStationClockQLThreshold based on Integer32"""
    defaultValue = 4


_TnSyncEStationClockQLThreshold_Type.__name__ = "Integer32"
_TnSyncEStationClockQLThreshold_Object = MibTableColumn
tnSyncEStationClockQLThreshold = _TnSyncEStationClockQLThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 5, 1, 6),
    _TnSyncEStationClockQLThreshold_Type()
)
tnSyncEStationClockQLThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSyncEStationClockQLThreshold.setStatus("current")


class _TnSyncEStationClockOutSel_Type(Integer32):
    """Custom type tnSyncEStationClockOutSel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("outtim", 1),
          ("setg", 2))
    )


_TnSyncEStationClockOutSel_Type.__name__ = "Integer32"
_TnSyncEStationClockOutSel_Object = MibTableColumn
tnSyncEStationClockOutSel = _TnSyncEStationClockOutSel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 5, 1, 7),
    _TnSyncEStationClockOutSel_Type()
)
tnSyncEStationClockOutSel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSyncEStationClockOutSel.setStatus("current")
_TnSyncEBITSPortTable_Object = MibTable
tnSyncEBITSPortTable = _TnSyncEBITSPortTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 6)
)
if mibBuilder.loadTexts:
    tnSyncEBITSPortTable.setStatus("current")
_TnSyncEBITSPortEntry_Object = MibTableRow
tnSyncEBITSPortEntry = _TnSyncEBITSPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 6, 1)
)
tnSyncEBITSPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnSyncEBITSPortEntry.setStatus("current")


class _TnSyncEBITSPortDirection_Type(Integer32):
    """Custom type tnSyncEBITSPortDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_TnSyncEBITSPortDirection_Type.__name__ = "Integer32"
_TnSyncEBITSPortDirection_Object = MibTableColumn
tnSyncEBITSPortDirection = _TnSyncEBITSPortDirection_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 6, 1, 1),
    _TnSyncEBITSPortDirection_Type()
)
tnSyncEBITSPortDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSyncEBITSPortDirection.setStatus("current")


class _TnSyncEBITSPortSignalType_Type(Integer32):
    """Custom type tnSyncEBITSPortSignalType based on Integer32"""
    defaultValue = 0


_TnSyncEBITSPortSignalType_Type.__name__ = "Integer32"
_TnSyncEBITSPortSignalType_Object = MibTableColumn
tnSyncEBITSPortSignalType = _TnSyncEBITSPortSignalType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 6, 1, 2),
    _TnSyncEBITSPortSignalType_Type()
)
tnSyncEBITSPortSignalType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSyncEBITSPortSignalType.setStatus("current")


class _TnSyncEBITSPortSaBit_Type(Integer32):
    """Custom type tnSyncEBITSPortSaBit based on Integer32"""
    defaultValue = 1

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
        *(("sa4", 1),
          ("sa5", 2),
          ("sa6", 3),
          ("sa7", 4),
          ("sa8", 5))
    )


_TnSyncEBITSPortSaBit_Type.__name__ = "Integer32"
_TnSyncEBITSPortSaBit_Object = MibTableColumn
tnSyncEBITSPortSaBit = _TnSyncEBITSPortSaBit_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 6, 1, 3),
    _TnSyncEBITSPortSaBit_Type()
)
tnSyncEBITSPortSaBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSyncEBITSPortSaBit.setStatus("current")


class _TnSyncEBITSPortOutputSSMTrans_Type(Integer32):
    """Custom type tnSyncEBITSPortOutputSSMTrans based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("act", 1),
          ("prc", 2),
          ("ssua", 3),
          ("ssub", 4),
          ("sec", 5),
          ("dnu", 6),
          ("stu", 7),
          ("prs", 8),
          ("st2", 9),
          ("sts3e", 10),
          ("st3", 11),
          ("none", 12),
          ("dus", 13))
    )


_TnSyncEBITSPortOutputSSMTrans_Type.__name__ = "Integer32"
_TnSyncEBITSPortOutputSSMTrans_Object = MibTableColumn
tnSyncEBITSPortOutputSSMTrans = _TnSyncEBITSPortOutputSSMTrans_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 6, 1, 4),
    _TnSyncEBITSPortOutputSSMTrans_Type()
)
tnSyncEBITSPortOutputSSMTrans.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSyncEBITSPortOutputSSMTrans.setStatus("current")


class _TnSyncEBITSPortOutputAISMode_Type(Integer32):
    """Custom type tnSyncEBITSPortOutputAISMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aismode", 1),
          ("qlmode", 2))
    )


_TnSyncEBITSPortOutputAISMode_Type.__name__ = "Integer32"
_TnSyncEBITSPortOutputAISMode_Object = MibTableColumn
tnSyncEBITSPortOutputAISMode = _TnSyncEBITSPortOutputAISMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 6, 1, 5),
    _TnSyncEBITSPortOutputAISMode_Type()
)
tnSyncEBITSPortOutputAISMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSyncEBITSPortOutputAISMode.setStatus("current")


class _TnSyncEBITSPortLineImpedance_Type(Integer32):
    """Custom type tnSyncEBITSPortLineImpedance based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("imp75ohms", 1),
          ("imp120ohms", 2),
          ("imp100ohms", 3))
    )


_TnSyncEBITSPortLineImpedance_Type.__name__ = "Integer32"
_TnSyncEBITSPortLineImpedance_Object = MibTableColumn
tnSyncEBITSPortLineImpedance = _TnSyncEBITSPortLineImpedance_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 6, 1, 6),
    _TnSyncEBITSPortLineImpedance_Type()
)
tnSyncEBITSPortLineImpedance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSyncEBITSPortLineImpedance.setStatus("current")


class _TnSyncEBITSPortLineCode_Type(Integer32):
    """Custom type tnSyncEBITSPortLineCode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("b8zs", 1),
          ("ami", 2))
    )


_TnSyncEBITSPortLineCode_Type.__name__ = "Integer32"
_TnSyncEBITSPortLineCode_Object = MibTableColumn
tnSyncEBITSPortLineCode = _TnSyncEBITSPortLineCode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 6, 1, 7),
    _TnSyncEBITSPortLineCode_Type()
)
tnSyncEBITSPortLineCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSyncEBITSPortLineCode.setStatus("current")


class _TnSyncEBITSPortLbo_Type(Integer32):
    """Custom type tnSyncEBITSPortLbo based on Integer32"""
    defaultValue = 2

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
        *(("lbo", 1),
          ("lbo1", 2),
          ("lbo2", 3),
          ("lbo3", 4),
          ("lbo4", 5),
          ("lbo5", 6))
    )


_TnSyncEBITSPortLbo_Type.__name__ = "Integer32"
_TnSyncEBITSPortLbo_Object = MibTableColumn
tnSyncEBITSPortLbo = _TnSyncEBITSPortLbo_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 2, 1, 6, 1, 8),
    _TnSyncEBITSPortLbo_Type()
)
tnSyncEBITSPortLbo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSyncEBITSPortLbo.setStatus("current")

# Managed Objects groups

tnSyncEGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 1, 1, 1)
)
tnSyncEGroup.setObjects(
      *(("TROPIC-SYNCE-MIB", "tnSyncESyncMsg"),
        ("TROPIC-SYNCE-MIB", "tnSyncEActiveRef"),
        ("TROPIC-SYNCE-MIB", "tnSyncEWTR"),
        ("TROPIC-SYNCE-MIB", "tnSyncESwCmdLineRef"),
        ("TROPIC-SYNCE-MIB", "tnSyncEClkModState"),
        ("TROPIC-SYNCE-MIB", "tnSyncESystemQL"))
)
if mibBuilder.loadTexts:
    tnSyncEGroup.setStatus("current")

tnSyncELineRefGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 1, 1, 2)
)
tnSyncELineRefGroup.setObjects(
      *(("TROPIC-SYNCE-MIB", "tnSyncELineRefAssignedPort"),
        ("TROPIC-SYNCE-MIB", "tnSyncELineRefPriority"),
        ("TROPIC-SYNCE-MIB", "tnSyncELineRefAdminState"),
        ("TROPIC-SYNCE-MIB", "tnSyncELineRefOperState"),
        ("TROPIC-SYNCE-MIB", "tnSyncELineLockOut"),
        ("TROPIC-SYNCE-MIB", "tnSyncELineRefState"),
        ("TROPIC-SYNCE-MIB", "tnSyncELineRefSwState"),
        ("TROPIC-SYNCE-MIB", "tnSyncELineRefIncSSMMsg"),
        ("TROPIC-SYNCE-MIB", "tnSyncELineRefIncSSMStatus"),
        ("TROPIC-SYNCE-MIB", "tnSyncELineRefIncSSMSupp"),
        ("TROPIC-SYNCE-MIB", "tnSyncELineRefProvQL"),
        ("TROPIC-SYNCE-MIB", "tnSyncELineRefAssociatedPort"),
        ("TROPIC-SYNCE-MIB", "tnSyncELineRefPriorityOfStationClock"),
        ("TROPIC-SYNCE-MIB", "tnSyncELineRefLockOutOfStationClock"),
        ("TROPIC-SYNCE-MIB", "tnSyncELineRefSwStateOfStationClock"))
)
if mibBuilder.loadTexts:
    tnSyncELineRefGroup.setStatus("current")

tnSyncEControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 1, 1, 3)
)
tnSyncEControlGroup.setObjects(
    ("TROPIC-SYNCE-MIB", "tnSyncEControlEECEnable")
)
if mibBuilder.loadTexts:
    tnSyncEControlGroup.setStatus("current")

tnSyncEPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 1, 1, 4)
)
tnSyncEPortGroup.setObjects(
      *(("TROPIC-SYNCE-MIB", "tnSyncEOprMode"),
        ("TROPIC-SYNCE-MIB", "tnSyncEOutgoingForceSsmTrans"))
)
if mibBuilder.loadTexts:
    tnSyncEPortGroup.setStatus("current")

tnSyncEStationClockGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 1, 1, 5)
)
tnSyncEStationClockGroup.setObjects(
      *(("TROPIC-SYNCE-MIB", "tnSyncEStationClockSyncMsg"),
        ("TROPIC-SYNCE-MIB", "tnSyncEStationClockActiveRef"),
        ("TROPIC-SYNCE-MIB", "tnSyncEStationClockWTR"),
        ("TROPIC-SYNCE-MIB", "tnSyncEStationClockSwCmdLineRef"),
        ("TROPIC-SYNCE-MIB", "tnSyncEStationClockSystemQL"),
        ("TROPIC-SYNCE-MIB", "tnSyncEStationClockQLThreshold"),
        ("TROPIC-SYNCE-MIB", "tnSyncEStationClockOutSel"))
)
if mibBuilder.loadTexts:
    tnSyncEStationClockGroup.setStatus("current")

tnSyncEBITSPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 1, 1, 6)
)
tnSyncEBITSPortGroup.setObjects(
      *(("TROPIC-SYNCE-MIB", "tnSyncEBITSPortDirection"),
        ("TROPIC-SYNCE-MIB", "tnSyncEBITSPortSignalType"),
        ("TROPIC-SYNCE-MIB", "tnSyncEBITSPortSaBit"),
        ("TROPIC-SYNCE-MIB", "tnSyncEBITSPortOutputSSMTrans"),
        ("TROPIC-SYNCE-MIB", "tnSyncEBITSPortOutputAISMode"),
        ("TROPIC-SYNCE-MIB", "tnSyncEBITSPortLineImpedance"),
        ("TROPIC-SYNCE-MIB", "tnSyncEBITSPortLineCode"),
        ("TROPIC-SYNCE-MIB", "tnSyncEBITSPortLbo"))
)
if mibBuilder.loadTexts:
    tnSyncEBITSPortGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnSyncECompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 8, 1, 2, 1)
)
tnSyncECompliance.setObjects(
      *(("TROPIC-SYNCE-MIB", "tnSyncEGroup"),
        ("TROPIC-SYNCE-MIB", "tnSyncELineRefGroup"),
        ("TROPIC-SYNCE-MIB", "tnSyncEControlGroup"),
        ("TROPIC-SYNCE-MIB", "tnSyncEPortGroup"),
        ("TROPIC-SYNCE-MIB", "tnSyncEStationClockGroup"),
        ("TROPIC-SYNCE-MIB", "tnSyncEBITSPortGroup"))
)
if mibBuilder.loadTexts:
    tnSyncECompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-SYNCE-MIB",
    **{"tnSyncEMibModule": tnSyncEMibModule,
       "tnSyncEConf": tnSyncEConf,
       "tnSyncEGroups": tnSyncEGroups,
       "tnSyncEGroup": tnSyncEGroup,
       "tnSyncELineRefGroup": tnSyncELineRefGroup,
       "tnSyncEControlGroup": tnSyncEControlGroup,
       "tnSyncEPortGroup": tnSyncEPortGroup,
       "tnSyncEStationClockGroup": tnSyncEStationClockGroup,
       "tnSyncEBITSPortGroup": tnSyncEBITSPortGroup,
       "tnSyncECompliances": tnSyncECompliances,
       "tnSyncECompliance": tnSyncECompliance,
       "tnSyncEObjs": tnSyncEObjs,
       "tnSyncEBasics": tnSyncEBasics,
       "tnSyncETable": tnSyncETable,
       "tnSyncEEntry": tnSyncEEntry,
       "tnSyncESyncMsg": tnSyncESyncMsg,
       "tnSyncEActiveRef": tnSyncEActiveRef,
       "tnSyncEWTR": tnSyncEWTR,
       "tnSyncESwCmdLineRef": tnSyncESwCmdLineRef,
       "tnSyncEClkModState": tnSyncEClkModState,
       "tnSyncESystemQL": tnSyncESystemQL,
       "tnSyncELineRefTable": tnSyncELineRefTable,
       "tnSyncELineRefEntry": tnSyncELineRefEntry,
       "tnSyncELineRefIndex": tnSyncELineRefIndex,
       "tnSyncELineRefAssignedPort": tnSyncELineRefAssignedPort,
       "tnSyncELineRefPriority": tnSyncELineRefPriority,
       "tnSyncELineRefAdminState": tnSyncELineRefAdminState,
       "tnSyncELineRefOperState": tnSyncELineRefOperState,
       "tnSyncELineLockOut": tnSyncELineLockOut,
       "tnSyncELineRefState": tnSyncELineRefState,
       "tnSyncELineRefSwState": tnSyncELineRefSwState,
       "tnSyncELineRefIncSSMMsg": tnSyncELineRefIncSSMMsg,
       "tnSyncELineRefIncSSMStatus": tnSyncELineRefIncSSMStatus,
       "tnSyncELineRefIncSSMSupp": tnSyncELineRefIncSSMSupp,
       "tnSyncELineRefProvQL": tnSyncELineRefProvQL,
       "tnSyncELineRefAssociatedPort": tnSyncELineRefAssociatedPort,
       "tnSyncELineRefPriorityOfStationClock": tnSyncELineRefPriorityOfStationClock,
       "tnSyncELineRefLockOutOfStationClock": tnSyncELineRefLockOutOfStationClock,
       "tnSyncELineRefSwStateOfStationClock": tnSyncELineRefSwStateOfStationClock,
       "tnSyncEControlTable": tnSyncEControlTable,
       "tnSyncEControlEntry": tnSyncEControlEntry,
       "tnSyncEControlEECEnable": tnSyncEControlEECEnable,
       "tnSyncEPortTable": tnSyncEPortTable,
       "tnSyncEPortEntry": tnSyncEPortEntry,
       "tnSyncEOprMode": tnSyncEOprMode,
       "tnSyncEOutgoingForceSsmTrans": tnSyncEOutgoingForceSsmTrans,
       "tnSyncEStationClockTable": tnSyncEStationClockTable,
       "tnSyncEStationClockEntry": tnSyncEStationClockEntry,
       "tnSyncEStationClockSyncMsg": tnSyncEStationClockSyncMsg,
       "tnSyncEStationClockActiveRef": tnSyncEStationClockActiveRef,
       "tnSyncEStationClockWTR": tnSyncEStationClockWTR,
       "tnSyncEStationClockSwCmdLineRef": tnSyncEStationClockSwCmdLineRef,
       "tnSyncEStationClockSystemQL": tnSyncEStationClockSystemQL,
       "tnSyncEStationClockQLThreshold": tnSyncEStationClockQLThreshold,
       "tnSyncEStationClockOutSel": tnSyncEStationClockOutSel,
       "tnSyncEBITSPortTable": tnSyncEBITSPortTable,
       "tnSyncEBITSPortEntry": tnSyncEBITSPortEntry,
       "tnSyncEBITSPortDirection": tnSyncEBITSPortDirection,
       "tnSyncEBITSPortSignalType": tnSyncEBITSPortSignalType,
       "tnSyncEBITSPortSaBit": tnSyncEBITSPortSaBit,
       "tnSyncEBITSPortOutputSSMTrans": tnSyncEBITSPortOutputSSMTrans,
       "tnSyncEBITSPortOutputAISMode": tnSyncEBITSPortOutputAISMode,
       "tnSyncEBITSPortLineImpedance": tnSyncEBITSPortLineImpedance,
       "tnSyncEBITSPortLineCode": tnSyncEBITSPortLineCode,
       "tnSyncEBITSPortLbo": tnSyncEBITSPortLbo}
)
