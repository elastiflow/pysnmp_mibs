# SNMP MIB module (RUIJIE-GVRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-GVRP-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:21 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "IfIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ruijieGvrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25)
)
if mibBuilder.loadTexts:
    ruijieGvrpMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieGvrpMIBObjects_ObjectIdentity = ObjectIdentity
ruijieGvrpMIBObjects = _RuijieGvrpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1)
)


class _RuijieGvrpStatus_Type(EnabledStatus):
    """Custom type ruijieGvrpStatus based on EnabledStatus"""
    defaultValue = 2


_RuijieGvrpStatus_Type.__name__ = "EnabledStatus"
_RuijieGvrpStatus_Object = MibScalar
ruijieGvrpStatus = _RuijieGvrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 1),
    _RuijieGvrpStatus_Type()
)
ruijieGvrpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieGvrpStatus.setStatus("current")


class _RuijieGvrpDynamicVlanCreateStauts_Type(EnabledStatus):
    """Custom type ruijieGvrpDynamicVlanCreateStauts based on EnabledStatus"""
    defaultValue = 2


_RuijieGvrpDynamicVlanCreateStauts_Type.__name__ = "EnabledStatus"
_RuijieGvrpDynamicVlanCreateStauts_Object = MibScalar
ruijieGvrpDynamicVlanCreateStauts = _RuijieGvrpDynamicVlanCreateStauts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 2),
    _RuijieGvrpDynamicVlanCreateStauts_Type()
)
ruijieGvrpDynamicVlanCreateStauts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieGvrpDynamicVlanCreateStauts.setStatus("current")


class _RuijieGvrpJoinTimer_Type(Integer32):
    """Custom type ruijieGvrpJoinTimer based on Integer32"""
    defaultValue = 200


_RuijieGvrpJoinTimer_Type.__name__ = "Integer32"
_RuijieGvrpJoinTimer_Object = MibScalar
ruijieGvrpJoinTimer = _RuijieGvrpJoinTimer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 3),
    _RuijieGvrpJoinTimer_Type()
)
ruijieGvrpJoinTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieGvrpJoinTimer.setStatus("current")


class _RuijieGvrpLeaveTimer_Type(Integer32):
    """Custom type ruijieGvrpLeaveTimer based on Integer32"""
    defaultValue = 600


_RuijieGvrpLeaveTimer_Type.__name__ = "Integer32"
_RuijieGvrpLeaveTimer_Object = MibScalar
ruijieGvrpLeaveTimer = _RuijieGvrpLeaveTimer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 4),
    _RuijieGvrpLeaveTimer_Type()
)
ruijieGvrpLeaveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieGvrpLeaveTimer.setStatus("current")


class _RuijieGvrpLeaveAllTimer_Type(Integer32):
    """Custom type ruijieGvrpLeaveAllTimer based on Integer32"""
    defaultValue = 10000


_RuijieGvrpLeaveAllTimer_Type.__name__ = "Integer32"
_RuijieGvrpLeaveAllTimer_Object = MibScalar
ruijieGvrpLeaveAllTimer = _RuijieGvrpLeaveAllTimer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 5),
    _RuijieGvrpLeaveAllTimer_Type()
)
ruijieGvrpLeaveAllTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieGvrpLeaveAllTimer.setStatus("current")
_RuijieGvrpTable_Object = MibTable
ruijieGvrpTable = _RuijieGvrpTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 6)
)
if mibBuilder.loadTexts:
    ruijieGvrpTable.setStatus("current")
_RuijieGvrpEntry_Object = MibTableRow
ruijieGvrpEntry = _RuijieGvrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 6, 1)
)
ruijieGvrpEntry.setIndexNames(
    (0, "RUIJIE-GVRP-MIB", "ruijieGvrpIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieGvrpEntry.setStatus("current")
_RuijieGvrpIfIndex_Type = IfIndex
_RuijieGvrpIfIndex_Object = MibTableColumn
ruijieGvrpIfIndex = _RuijieGvrpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 6, 1, 1),
    _RuijieGvrpIfIndex_Type()
)
ruijieGvrpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieGvrpIfIndex.setStatus("current")


class _RuijieGvrpRegistrationMode_Type(EnabledStatus):
    """Custom type ruijieGvrpRegistrationMode based on EnabledStatus"""
    defaultValue = 1


_RuijieGvrpRegistrationMode_Type.__name__ = "EnabledStatus"
_RuijieGvrpRegistrationMode_Object = MibTableColumn
ruijieGvrpRegistrationMode = _RuijieGvrpRegistrationMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 6, 1, 2),
    _RuijieGvrpRegistrationMode_Type()
)
ruijieGvrpRegistrationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieGvrpRegistrationMode.setStatus("current")


class _RuijieGvrpApplicantState_Type(EnabledStatus):
    """Custom type ruijieGvrpApplicantState based on EnabledStatus"""
    defaultValue = 1


_RuijieGvrpApplicantState_Type.__name__ = "EnabledStatus"
_RuijieGvrpApplicantState_Object = MibTableColumn
ruijieGvrpApplicantState = _RuijieGvrpApplicantState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 6, 1, 3),
    _RuijieGvrpApplicantState_Type()
)
ruijieGvrpApplicantState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieGvrpApplicantState.setStatus("current")
_RuijieGvrpStatsTable_Object = MibTable
ruijieGvrpStatsTable = _RuijieGvrpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7)
)
if mibBuilder.loadTexts:
    ruijieGvrpStatsTable.setStatus("current")
_RuijieGvrpStatsEntry_Object = MibTableRow
ruijieGvrpStatsEntry = _RuijieGvrpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1)
)
ruijieGvrpStatsEntry.setIndexNames(
    (0, "RUIJIE-GVRP-MIB", "ruijieGvrpStatsIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieGvrpStatsEntry.setStatus("current")
_RuijieGvrpStatsIfIndex_Type = IfIndex
_RuijieGvrpStatsIfIndex_Object = MibTableColumn
ruijieGvrpStatsIfIndex = _RuijieGvrpStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 1),
    _RuijieGvrpStatsIfIndex_Type()
)
ruijieGvrpStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieGvrpStatsIfIndex.setStatus("current")
_RuijieGvrpRecValidGvrpPdu_Type = Counter32
_RuijieGvrpRecValidGvrpPdu_Object = MibTableColumn
ruijieGvrpRecValidGvrpPdu = _RuijieGvrpRecValidGvrpPdu_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 2),
    _RuijieGvrpRecValidGvrpPdu_Type()
)
ruijieGvrpRecValidGvrpPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieGvrpRecValidGvrpPdu.setStatus("current")
_RuijieGvrpRecInvalidGvrpPdu_Type = Counter32
_RuijieGvrpRecInvalidGvrpPdu_Object = MibTableColumn
ruijieGvrpRecInvalidGvrpPdu = _RuijieGvrpRecInvalidGvrpPdu_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 3),
    _RuijieGvrpRecInvalidGvrpPdu_Type()
)
ruijieGvrpRecInvalidGvrpPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieGvrpRecInvalidGvrpPdu.setStatus("current")
_RuijieGvrpRecJoin_Type = Counter32
_RuijieGvrpRecJoin_Object = MibTableColumn
ruijieGvrpRecJoin = _RuijieGvrpRecJoin_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 4),
    _RuijieGvrpRecJoin_Type()
)
ruijieGvrpRecJoin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieGvrpRecJoin.setStatus("current")
_RuijieGvrpRecJoinIn_Type = Counter32
_RuijieGvrpRecJoinIn_Object = MibTableColumn
ruijieGvrpRecJoinIn = _RuijieGvrpRecJoinIn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 5),
    _RuijieGvrpRecJoinIn_Type()
)
ruijieGvrpRecJoinIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieGvrpRecJoinIn.setStatus("current")
_RuijieGvrpRecEmpty_Type = Counter32
_RuijieGvrpRecEmpty_Object = MibTableColumn
ruijieGvrpRecEmpty = _RuijieGvrpRecEmpty_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 6),
    _RuijieGvrpRecEmpty_Type()
)
ruijieGvrpRecEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieGvrpRecEmpty.setStatus("current")
_RuijieGvrpRecLeaveEmpty_Type = Counter32
_RuijieGvrpRecLeaveEmpty_Object = MibTableColumn
ruijieGvrpRecLeaveEmpty = _RuijieGvrpRecLeaveEmpty_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 7),
    _RuijieGvrpRecLeaveEmpty_Type()
)
ruijieGvrpRecLeaveEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieGvrpRecLeaveEmpty.setStatus("current")
_RuijieGvrpRecLeaveIn_Type = Counter32
_RuijieGvrpRecLeaveIn_Object = MibTableColumn
ruijieGvrpRecLeaveIn = _RuijieGvrpRecLeaveIn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 8),
    _RuijieGvrpRecLeaveIn_Type()
)
ruijieGvrpRecLeaveIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieGvrpRecLeaveIn.setStatus("current")
_RuijieGvrpRecLeaveAll_Type = Counter32
_RuijieGvrpRecLeaveAll_Object = MibTableColumn
ruijieGvrpRecLeaveAll = _RuijieGvrpRecLeaveAll_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 9),
    _RuijieGvrpRecLeaveAll_Type()
)
ruijieGvrpRecLeaveAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieGvrpRecLeaveAll.setStatus("current")
_RuijieGvrpSentGvrpPdu_Type = Counter32
_RuijieGvrpSentGvrpPdu_Object = MibTableColumn
ruijieGvrpSentGvrpPdu = _RuijieGvrpSentGvrpPdu_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 10),
    _RuijieGvrpSentGvrpPdu_Type()
)
ruijieGvrpSentGvrpPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieGvrpSentGvrpPdu.setStatus("current")
_RuijieGvrpSentJoin_Type = Counter32
_RuijieGvrpSentJoin_Object = MibTableColumn
ruijieGvrpSentJoin = _RuijieGvrpSentJoin_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 11),
    _RuijieGvrpSentJoin_Type()
)
ruijieGvrpSentJoin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieGvrpSentJoin.setStatus("current")
_RuijieGvrpSentJoinIn_Type = Counter32
_RuijieGvrpSentJoinIn_Object = MibTableColumn
ruijieGvrpSentJoinIn = _RuijieGvrpSentJoinIn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 12),
    _RuijieGvrpSentJoinIn_Type()
)
ruijieGvrpSentJoinIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieGvrpSentJoinIn.setStatus("current")
_RuijieGvrpSentEmpty_Type = Counter32
_RuijieGvrpSentEmpty_Object = MibTableColumn
ruijieGvrpSentEmpty = _RuijieGvrpSentEmpty_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 13),
    _RuijieGvrpSentEmpty_Type()
)
ruijieGvrpSentEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieGvrpSentEmpty.setStatus("current")
_RuijieGvrpSentLeaveEmpty_Type = Counter32
_RuijieGvrpSentLeaveEmpty_Object = MibTableColumn
ruijieGvrpSentLeaveEmpty = _RuijieGvrpSentLeaveEmpty_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 14),
    _RuijieGvrpSentLeaveEmpty_Type()
)
ruijieGvrpSentLeaveEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieGvrpSentLeaveEmpty.setStatus("current")
_RuijieGvrpSentLeaveIn_Type = Counter32
_RuijieGvrpSentLeaveIn_Object = MibTableColumn
ruijieGvrpSentLeaveIn = _RuijieGvrpSentLeaveIn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 15),
    _RuijieGvrpSentLeaveIn_Type()
)
ruijieGvrpSentLeaveIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieGvrpSentLeaveIn.setStatus("current")
_RuijieGvrpSentLeaveAll_Type = Counter32
_RuijieGvrpSentLeaveAll_Object = MibTableColumn
ruijieGvrpSentLeaveAll = _RuijieGvrpSentLeaveAll_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 16),
    _RuijieGvrpSentLeaveAll_Type()
)
ruijieGvrpSentLeaveAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieGvrpSentLeaveAll.setStatus("current")
_RuijieGvrpJoinIndicated_Type = Counter32
_RuijieGvrpJoinIndicated_Object = MibTableColumn
ruijieGvrpJoinIndicated = _RuijieGvrpJoinIndicated_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 17),
    _RuijieGvrpJoinIndicated_Type()
)
ruijieGvrpJoinIndicated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieGvrpJoinIndicated.setStatus("current")
_RuijieGvrpLeaveIndicated_Type = Counter32
_RuijieGvrpLeaveIndicated_Object = MibTableColumn
ruijieGvrpLeaveIndicated = _RuijieGvrpLeaveIndicated_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 18),
    _RuijieGvrpLeaveIndicated_Type()
)
ruijieGvrpLeaveIndicated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieGvrpLeaveIndicated.setStatus("current")
_RuijieGvrpJoinPropagated_Type = Counter32
_RuijieGvrpJoinPropagated_Object = MibTableColumn
ruijieGvrpJoinPropagated = _RuijieGvrpJoinPropagated_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 19),
    _RuijieGvrpJoinPropagated_Type()
)
ruijieGvrpJoinPropagated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieGvrpJoinPropagated.setStatus("current")
_RuijieGvrpLeavePropagated_Type = Counter32
_RuijieGvrpLeavePropagated_Object = MibTableColumn
ruijieGvrpLeavePropagated = _RuijieGvrpLeavePropagated_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 20),
    _RuijieGvrpLeavePropagated_Type()
)
ruijieGvrpLeavePropagated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieGvrpLeavePropagated.setStatus("current")
_RuijieGvrpStatisticsPortClear_Type = Integer32
_RuijieGvrpStatisticsPortClear_Object = MibTableColumn
ruijieGvrpStatisticsPortClear = _RuijieGvrpStatisticsPortClear_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 7, 1, 21),
    _RuijieGvrpStatisticsPortClear_Type()
)
ruijieGvrpStatisticsPortClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieGvrpStatisticsPortClear.setStatus("current")


class _RuijieGvrpOperVid_Type(VlanId):
    """Custom type ruijieGvrpOperVid based on VlanId"""
    defaultValue = 1


_RuijieGvrpOperVid_Type.__name__ = "VlanId"
_RuijieGvrpOperVid_Object = MibScalar
ruijieGvrpOperVid = _RuijieGvrpOperVid_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 8),
    _RuijieGvrpOperVid_Type()
)
ruijieGvrpOperVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieGvrpOperVid.setStatus("current")
_RuijieGvrpStatisticsClear_Type = Integer32
_RuijieGvrpStatisticsClear_Object = MibScalar
ruijieGvrpStatisticsClear = _RuijieGvrpStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 9),
    _RuijieGvrpStatisticsClear_Type()
)
ruijieGvrpStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieGvrpStatisticsClear.setStatus("current")
_RuijieGvrpResetTimer_Type = VlanId
_RuijieGvrpResetTimer_Object = MibScalar
ruijieGvrpResetTimer = _RuijieGvrpResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 1, 10),
    _RuijieGvrpResetTimer_Type()
)
ruijieGvrpResetTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieGvrpResetTimer.setStatus("current")
_RuijieGvrpMIBConformance_ObjectIdentity = ObjectIdentity
ruijieGvrpMIBConformance = _RuijieGvrpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 2)
)
_RuijieGvrpMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieGvrpMIBCompliances = _RuijieGvrpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 2, 1)
)
_RuijieGvrpMIBGroups_ObjectIdentity = ObjectIdentity
ruijieGvrpMIBGroups = _RuijieGvrpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 2, 2)
)

# Managed Objects groups

ruijieGvrpMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 2, 2, 1)
)
ruijieGvrpMIBGroup.setObjects(
      *(("RUIJIE-GVRP-MIB", "ruijieGvrpStatus"),
        ("RUIJIE-GVRP-MIB", "ruijieGvrpDynamicVlanCreateStauts"),
        ("RUIJIE-GVRP-MIB", "ruijieGvrpJoinTimer"),
        ("RUIJIE-GVRP-MIB", "ruijieGvrpLeaveTimer"),
        ("RUIJIE-GVRP-MIB", "ruijieGvrpLeaveAllTimer"),
        ("RUIJIE-GVRP-MIB", "ruijieGvrpRegistrationMode"),
        ("RUIJIE-GVRP-MIB", "ruijieGvrpApplicantState"))
)
if mibBuilder.loadTexts:
    ruijieGvrpMIBGroup.setStatus("current")

ruijieGvrpStatsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 2, 2, 2)
)
ruijieGvrpStatsMIBGroup.setObjects(
      *(("RUIJIE-GVRP-MIB", "ruijieGvrpRecValidGvrpPdu"),
        ("RUIJIE-GVRP-MIB", "ruijieGvrpRecInvalidGvrpPdu"),
        ("RUIJIE-GVRP-MIB", "ruijieGvrpRecJoin"),
        ("RUIJIE-GVRP-MIB", "ruijieGvrpRecJoinIn"),
        ("RUIJIE-GVRP-MIB", "ruijieGvrpRecEmpty"),
        ("RUIJIE-GVRP-MIB", "ruijieGvrpRecLeaveEmpty"),
        ("RUIJIE-GVRP-MIB", "ruijieGvrpRecLeaveIn"),
        ("RUIJIE-GVRP-MIB", "ruijieGvrpRecLeaveAll"),
        ("RUIJIE-GVRP-MIB", "ruijieGvrpSentGvrpPdu"),
        ("RUIJIE-GVRP-MIB", "ruijieGvrpSentJoin"),
        ("RUIJIE-GVRP-MIB", "ruijieGvrpSentJoinIn"),
        ("RUIJIE-GVRP-MIB", "ruijieGvrpSentEmpty"),
        ("RUIJIE-GVRP-MIB", "ruijieGvrpSentLeaveEmpty"),
        ("RUIJIE-GVRP-MIB", "ruijieGvrpSentLeaveIn"),
        ("RUIJIE-GVRP-MIB", "ruijieGvrpSentLeaveAll"),
        ("RUIJIE-GVRP-MIB", "ruijieGvrpJoinIndicated"),
        ("RUIJIE-GVRP-MIB", "ruijieGvrpLeaveIndicated"),
        ("RUIJIE-GVRP-MIB", "ruijieGvrpJoinPropagated"),
        ("RUIJIE-GVRP-MIB", "ruijieGvrpLeavePropagated"),
        ("RUIJIE-GVRP-MIB", "ruijieGvrpStatisticsPortClear"))
)
if mibBuilder.loadTexts:
    ruijieGvrpStatsMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieGvrpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 25, 2, 1, 1)
)
ruijieGvrpMIBCompliance.setObjects(
      *(("RUIJIE-GVRP-MIB", "ruijieGvrpMIBGroup"),
        ("RUIJIE-GVRP-MIB", "ruijieGvrpStatsMIBGroup"))
)
if mibBuilder.loadTexts:
    ruijieGvrpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-GVRP-MIB",
    **{"ruijieGvrpMIB": ruijieGvrpMIB,
       "ruijieGvrpMIBObjects": ruijieGvrpMIBObjects,
       "ruijieGvrpStatus": ruijieGvrpStatus,
       "ruijieGvrpDynamicVlanCreateStauts": ruijieGvrpDynamicVlanCreateStauts,
       "ruijieGvrpJoinTimer": ruijieGvrpJoinTimer,
       "ruijieGvrpLeaveTimer": ruijieGvrpLeaveTimer,
       "ruijieGvrpLeaveAllTimer": ruijieGvrpLeaveAllTimer,
       "ruijieGvrpTable": ruijieGvrpTable,
       "ruijieGvrpEntry": ruijieGvrpEntry,
       "ruijieGvrpIfIndex": ruijieGvrpIfIndex,
       "ruijieGvrpRegistrationMode": ruijieGvrpRegistrationMode,
       "ruijieGvrpApplicantState": ruijieGvrpApplicantState,
       "ruijieGvrpStatsTable": ruijieGvrpStatsTable,
       "ruijieGvrpStatsEntry": ruijieGvrpStatsEntry,
       "ruijieGvrpStatsIfIndex": ruijieGvrpStatsIfIndex,
       "ruijieGvrpRecValidGvrpPdu": ruijieGvrpRecValidGvrpPdu,
       "ruijieGvrpRecInvalidGvrpPdu": ruijieGvrpRecInvalidGvrpPdu,
       "ruijieGvrpRecJoin": ruijieGvrpRecJoin,
       "ruijieGvrpRecJoinIn": ruijieGvrpRecJoinIn,
       "ruijieGvrpRecEmpty": ruijieGvrpRecEmpty,
       "ruijieGvrpRecLeaveEmpty": ruijieGvrpRecLeaveEmpty,
       "ruijieGvrpRecLeaveIn": ruijieGvrpRecLeaveIn,
       "ruijieGvrpRecLeaveAll": ruijieGvrpRecLeaveAll,
       "ruijieGvrpSentGvrpPdu": ruijieGvrpSentGvrpPdu,
       "ruijieGvrpSentJoin": ruijieGvrpSentJoin,
       "ruijieGvrpSentJoinIn": ruijieGvrpSentJoinIn,
       "ruijieGvrpSentEmpty": ruijieGvrpSentEmpty,
       "ruijieGvrpSentLeaveEmpty": ruijieGvrpSentLeaveEmpty,
       "ruijieGvrpSentLeaveIn": ruijieGvrpSentLeaveIn,
       "ruijieGvrpSentLeaveAll": ruijieGvrpSentLeaveAll,
       "ruijieGvrpJoinIndicated": ruijieGvrpJoinIndicated,
       "ruijieGvrpLeaveIndicated": ruijieGvrpLeaveIndicated,
       "ruijieGvrpJoinPropagated": ruijieGvrpJoinPropagated,
       "ruijieGvrpLeavePropagated": ruijieGvrpLeavePropagated,
       "ruijieGvrpStatisticsPortClear": ruijieGvrpStatisticsPortClear,
       "ruijieGvrpOperVid": ruijieGvrpOperVid,
       "ruijieGvrpStatisticsClear": ruijieGvrpStatisticsClear,
       "ruijieGvrpResetTimer": ruijieGvrpResetTimer,
       "ruijieGvrpMIBConformance": ruijieGvrpMIBConformance,
       "ruijieGvrpMIBCompliances": ruijieGvrpMIBCompliances,
       "ruijieGvrpMIBCompliance": ruijieGvrpMIBCompliance,
       "ruijieGvrpMIBGroups": ruijieGvrpMIBGroups,
       "ruijieGvrpMIBGroup": ruijieGvrpMIBGroup,
       "ruijieGvrpStatsMIBGroup": ruijieGvrpStatsMIBGroup}
)
