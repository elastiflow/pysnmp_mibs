# SNMP MIB module (CISCO-FIREPOWER-TRIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-TRIG-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:24:13 2025
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

(CfprManagedObjectDn,
 CfprManagedObjectId,
 ciscoFirepowerMIBObjects) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-MIB",
    "CfprManagedObjectDn",
    "CfprManagedObjectId",
    "ciscoFirepowerMIBObjects")

(CfprPolicyPolicyOwner,
 CfprTrigAdminState,
 CfprTrigDay,
 CfprTrigOperState,
 CfprTrigTokenOperState,
 CfprTrigTrigOperState,
 CfprTrigTriggeredState) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprPolicyPolicyOwner",
    "CfprTrigAdminState",
    "CfprTrigDay",
    "CfprTrigOperState",
    "CfprTrigTokenOperState",
    "CfprTrigTrigOperState",
    "CfprTrigTriggeredState")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoAlarmSeverity,
 CiscoInetAddressMask,
 CiscoNetworkAddress,
 TimeIntervalSec,
 Unsigned64) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoAlarmSeverity",
    "CiscoInetAddressMask",
    "CiscoNetworkAddress",
    "TimeIntervalSec",
    "Unsigned64")

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowPointer,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowPointer",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cfprTrigObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprTrigAbsWindowTable_Object = MibTable
cfprTrigAbsWindowTable = _CfprTrigAbsWindowTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 1)
)
if mibBuilder.loadTexts:
    cfprTrigAbsWindowTable.setStatus("current")
_CfprTrigAbsWindowEntry_Object = MibTableRow
cfprTrigAbsWindowEntry = _CfprTrigAbsWindowEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 1, 1)
)
cfprTrigAbsWindowEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-TRIG-MIB", "cfprTrigAbsWindowInstanceId"),
)
if mibBuilder.loadTexts:
    cfprTrigAbsWindowEntry.setStatus("current")
_CfprTrigAbsWindowInstanceId_Type = CfprManagedObjectId
_CfprTrigAbsWindowInstanceId_Object = MibTableColumn
cfprTrigAbsWindowInstanceId = _CfprTrigAbsWindowInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 1, 1, 1),
    _CfprTrigAbsWindowInstanceId_Type()
)
cfprTrigAbsWindowInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprTrigAbsWindowInstanceId.setStatus("current")
_CfprTrigAbsWindowDn_Type = CfprManagedObjectDn
_CfprTrigAbsWindowDn_Object = MibTableColumn
cfprTrigAbsWindowDn = _CfprTrigAbsWindowDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 1, 1, 2),
    _CfprTrigAbsWindowDn_Type()
)
cfprTrigAbsWindowDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigAbsWindowDn.setStatus("current")
_CfprTrigAbsWindowRn_Type = SnmpAdminString
_CfprTrigAbsWindowRn_Object = MibTableColumn
cfprTrigAbsWindowRn = _CfprTrigAbsWindowRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 1, 1, 3),
    _CfprTrigAbsWindowRn_Type()
)
cfprTrigAbsWindowRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigAbsWindowRn.setStatus("current")
_CfprTrigAbsWindowConcurCap_Type = Gauge32
_CfprTrigAbsWindowConcurCap_Object = MibTableColumn
cfprTrigAbsWindowConcurCap = _CfprTrigAbsWindowConcurCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 1, 1, 4),
    _CfprTrigAbsWindowConcurCap_Type()
)
cfprTrigAbsWindowConcurCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigAbsWindowConcurCap.setStatus("current")
_CfprTrigAbsWindowDate_Type = DateAndTime
_CfprTrigAbsWindowDate_Object = MibTableColumn
cfprTrigAbsWindowDate = _CfprTrigAbsWindowDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 1, 1, 5),
    _CfprTrigAbsWindowDate_Type()
)
cfprTrigAbsWindowDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigAbsWindowDate.setStatus("current")
_CfprTrigAbsWindowJobCount_Type = Gauge32
_CfprTrigAbsWindowJobCount_Object = MibTableColumn
cfprTrigAbsWindowJobCount = _CfprTrigAbsWindowJobCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 1, 1, 6),
    _CfprTrigAbsWindowJobCount_Type()
)
cfprTrigAbsWindowJobCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigAbsWindowJobCount.setStatus("current")
_CfprTrigAbsWindowName_Type = SnmpAdminString
_CfprTrigAbsWindowName_Object = MibTableColumn
cfprTrigAbsWindowName = _CfprTrigAbsWindowName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 1, 1, 7),
    _CfprTrigAbsWindowName_Type()
)
cfprTrigAbsWindowName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigAbsWindowName.setStatus("current")
_CfprTrigAbsWindowProcBreak_Type = SnmpAdminString
_CfprTrigAbsWindowProcBreak_Object = MibTableColumn
cfprTrigAbsWindowProcBreak = _CfprTrigAbsWindowProcBreak_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 1, 1, 8),
    _CfprTrigAbsWindowProcBreak_Type()
)
cfprTrigAbsWindowProcBreak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigAbsWindowProcBreak.setStatus("current")
_CfprTrigAbsWindowProcCap_Type = Gauge32
_CfprTrigAbsWindowProcCap_Object = MibTableColumn
cfprTrigAbsWindowProcCap = _CfprTrigAbsWindowProcCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 1, 1, 9),
    _CfprTrigAbsWindowProcCap_Type()
)
cfprTrigAbsWindowProcCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigAbsWindowProcCap.setStatus("current")
_CfprTrigAbsWindowTimeCap_Type = SnmpAdminString
_CfprTrigAbsWindowTimeCap_Object = MibTableColumn
cfprTrigAbsWindowTimeCap = _CfprTrigAbsWindowTimeCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 1, 1, 10),
    _CfprTrigAbsWindowTimeCap_Type()
)
cfprTrigAbsWindowTimeCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigAbsWindowTimeCap.setStatus("current")
_CfprTrigAbsWindowStart_Type = TruthValue
_CfprTrigAbsWindowStart_Object = MibTableColumn
cfprTrigAbsWindowStart = _CfprTrigAbsWindowStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 1, 1, 11),
    _CfprTrigAbsWindowStart_Type()
)
cfprTrigAbsWindowStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigAbsWindowStart.setStatus("current")
_CfprTrigClientTokenTable_Object = MibTable
cfprTrigClientTokenTable = _CfprTrigClientTokenTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 2)
)
if mibBuilder.loadTexts:
    cfprTrigClientTokenTable.setStatus("current")
_CfprTrigClientTokenEntry_Object = MibTableRow
cfprTrigClientTokenEntry = _CfprTrigClientTokenEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 2, 1)
)
cfprTrigClientTokenEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-TRIG-MIB", "cfprTrigClientTokenInstanceId"),
)
if mibBuilder.loadTexts:
    cfprTrigClientTokenEntry.setStatus("current")
_CfprTrigClientTokenInstanceId_Type = CfprManagedObjectId
_CfprTrigClientTokenInstanceId_Object = MibTableColumn
cfprTrigClientTokenInstanceId = _CfprTrigClientTokenInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 2, 1, 1),
    _CfprTrigClientTokenInstanceId_Type()
)
cfprTrigClientTokenInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprTrigClientTokenInstanceId.setStatus("current")
_CfprTrigClientTokenDn_Type = CfprManagedObjectDn
_CfprTrigClientTokenDn_Object = MibTableColumn
cfprTrigClientTokenDn = _CfprTrigClientTokenDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 2, 1, 2),
    _CfprTrigClientTokenDn_Type()
)
cfprTrigClientTokenDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigClientTokenDn.setStatus("current")
_CfprTrigClientTokenRn_Type = SnmpAdminString
_CfprTrigClientTokenRn_Object = MibTableColumn
cfprTrigClientTokenRn = _CfprTrigClientTokenRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 2, 1, 3),
    _CfprTrigClientTokenRn_Type()
)
cfprTrigClientTokenRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigClientTokenRn.setStatus("current")
_CfprTrigClientTokenActivityTs_Type = DateAndTime
_CfprTrigClientTokenActivityTs_Object = MibTableColumn
cfprTrigClientTokenActivityTs = _CfprTrigClientTokenActivityTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 2, 1, 4),
    _CfprTrigClientTokenActivityTs_Type()
)
cfprTrigClientTokenActivityTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigClientTokenActivityTs.setStatus("current")
_CfprTrigClientTokenId_Type = Unsigned64
_CfprTrigClientTokenId_Object = MibTableColumn
cfprTrigClientTokenId = _CfprTrigClientTokenId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 2, 1, 5),
    _CfprTrigClientTokenId_Type()
)
cfprTrigClientTokenId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigClientTokenId.setStatus("current")
_CfprTrigClientTokenOperState_Type = CfprTrigTokenOperState
_CfprTrigClientTokenOperState_Object = MibTableColumn
cfprTrigClientTokenOperState = _CfprTrigClientTokenOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 2, 1, 6),
    _CfprTrigClientTokenOperState_Type()
)
cfprTrigClientTokenOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigClientTokenOperState.setStatus("current")
_CfprTrigLocalAbsWindowTable_Object = MibTable
cfprTrigLocalAbsWindowTable = _CfprTrigLocalAbsWindowTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 3)
)
if mibBuilder.loadTexts:
    cfprTrigLocalAbsWindowTable.setStatus("current")
_CfprTrigLocalAbsWindowEntry_Object = MibTableRow
cfprTrigLocalAbsWindowEntry = _CfprTrigLocalAbsWindowEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 3, 1)
)
cfprTrigLocalAbsWindowEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-TRIG-MIB", "cfprTrigLocalAbsWindowInstanceId"),
)
if mibBuilder.loadTexts:
    cfprTrigLocalAbsWindowEntry.setStatus("current")
_CfprTrigLocalAbsWindowInstanceId_Type = CfprManagedObjectId
_CfprTrigLocalAbsWindowInstanceId_Object = MibTableColumn
cfprTrigLocalAbsWindowInstanceId = _CfprTrigLocalAbsWindowInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 3, 1, 1),
    _CfprTrigLocalAbsWindowInstanceId_Type()
)
cfprTrigLocalAbsWindowInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprTrigLocalAbsWindowInstanceId.setStatus("current")
_CfprTrigLocalAbsWindowDn_Type = CfprManagedObjectDn
_CfprTrigLocalAbsWindowDn_Object = MibTableColumn
cfprTrigLocalAbsWindowDn = _CfprTrigLocalAbsWindowDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 3, 1, 2),
    _CfprTrigLocalAbsWindowDn_Type()
)
cfprTrigLocalAbsWindowDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigLocalAbsWindowDn.setStatus("current")
_CfprTrigLocalAbsWindowRn_Type = SnmpAdminString
_CfprTrigLocalAbsWindowRn_Object = MibTableColumn
cfprTrigLocalAbsWindowRn = _CfprTrigLocalAbsWindowRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 3, 1, 3),
    _CfprTrigLocalAbsWindowRn_Type()
)
cfprTrigLocalAbsWindowRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigLocalAbsWindowRn.setStatus("current")
_CfprTrigLocalAbsWindowConcurCap_Type = Gauge32
_CfprTrigLocalAbsWindowConcurCap_Object = MibTableColumn
cfprTrigLocalAbsWindowConcurCap = _CfprTrigLocalAbsWindowConcurCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 3, 1, 4),
    _CfprTrigLocalAbsWindowConcurCap_Type()
)
cfprTrigLocalAbsWindowConcurCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigLocalAbsWindowConcurCap.setStatus("current")
_CfprTrigLocalAbsWindowDate_Type = DateAndTime
_CfprTrigLocalAbsWindowDate_Object = MibTableColumn
cfprTrigLocalAbsWindowDate = _CfprTrigLocalAbsWindowDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 3, 1, 5),
    _CfprTrigLocalAbsWindowDate_Type()
)
cfprTrigLocalAbsWindowDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigLocalAbsWindowDate.setStatus("current")
_CfprTrigLocalAbsWindowJobCount_Type = Gauge32
_CfprTrigLocalAbsWindowJobCount_Object = MibTableColumn
cfprTrigLocalAbsWindowJobCount = _CfprTrigLocalAbsWindowJobCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 3, 1, 6),
    _CfprTrigLocalAbsWindowJobCount_Type()
)
cfprTrigLocalAbsWindowJobCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigLocalAbsWindowJobCount.setStatus("current")
_CfprTrigLocalAbsWindowName_Type = SnmpAdminString
_CfprTrigLocalAbsWindowName_Object = MibTableColumn
cfprTrigLocalAbsWindowName = _CfprTrigLocalAbsWindowName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 3, 1, 7),
    _CfprTrigLocalAbsWindowName_Type()
)
cfprTrigLocalAbsWindowName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigLocalAbsWindowName.setStatus("current")
_CfprTrigLocalAbsWindowProcBreak_Type = SnmpAdminString
_CfprTrigLocalAbsWindowProcBreak_Object = MibTableColumn
cfprTrigLocalAbsWindowProcBreak = _CfprTrigLocalAbsWindowProcBreak_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 3, 1, 8),
    _CfprTrigLocalAbsWindowProcBreak_Type()
)
cfprTrigLocalAbsWindowProcBreak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigLocalAbsWindowProcBreak.setStatus("current")
_CfprTrigLocalAbsWindowProcCap_Type = Gauge32
_CfprTrigLocalAbsWindowProcCap_Object = MibTableColumn
cfprTrigLocalAbsWindowProcCap = _CfprTrigLocalAbsWindowProcCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 3, 1, 9),
    _CfprTrigLocalAbsWindowProcCap_Type()
)
cfprTrigLocalAbsWindowProcCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigLocalAbsWindowProcCap.setStatus("current")
_CfprTrigLocalAbsWindowTimeCap_Type = SnmpAdminString
_CfprTrigLocalAbsWindowTimeCap_Object = MibTableColumn
cfprTrigLocalAbsWindowTimeCap = _CfprTrigLocalAbsWindowTimeCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 3, 1, 10),
    _CfprTrigLocalAbsWindowTimeCap_Type()
)
cfprTrigLocalAbsWindowTimeCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigLocalAbsWindowTimeCap.setStatus("current")
_CfprTrigLocalAbsWindowStart_Type = TruthValue
_CfprTrigLocalAbsWindowStart_Object = MibTableColumn
cfprTrigLocalAbsWindowStart = _CfprTrigLocalAbsWindowStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 3, 1, 11),
    _CfprTrigLocalAbsWindowStart_Type()
)
cfprTrigLocalAbsWindowStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigLocalAbsWindowStart.setStatus("current")
_CfprTrigLocalSchedTable_Object = MibTable
cfprTrigLocalSchedTable = _CfprTrigLocalSchedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 4)
)
if mibBuilder.loadTexts:
    cfprTrigLocalSchedTable.setStatus("current")
_CfprTrigLocalSchedEntry_Object = MibTableRow
cfprTrigLocalSchedEntry = _CfprTrigLocalSchedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 4, 1)
)
cfprTrigLocalSchedEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-TRIG-MIB", "cfprTrigLocalSchedInstanceId"),
)
if mibBuilder.loadTexts:
    cfprTrigLocalSchedEntry.setStatus("current")
_CfprTrigLocalSchedInstanceId_Type = CfprManagedObjectId
_CfprTrigLocalSchedInstanceId_Object = MibTableColumn
cfprTrigLocalSchedInstanceId = _CfprTrigLocalSchedInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 4, 1, 1),
    _CfprTrigLocalSchedInstanceId_Type()
)
cfprTrigLocalSchedInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprTrigLocalSchedInstanceId.setStatus("current")
_CfprTrigLocalSchedDn_Type = CfprManagedObjectDn
_CfprTrigLocalSchedDn_Object = MibTableColumn
cfprTrigLocalSchedDn = _CfprTrigLocalSchedDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 4, 1, 2),
    _CfprTrigLocalSchedDn_Type()
)
cfprTrigLocalSchedDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigLocalSchedDn.setStatus("current")
_CfprTrigLocalSchedRn_Type = SnmpAdminString
_CfprTrigLocalSchedRn_Object = MibTableColumn
cfprTrigLocalSchedRn = _CfprTrigLocalSchedRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 4, 1, 3),
    _CfprTrigLocalSchedRn_Type()
)
cfprTrigLocalSchedRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigLocalSchedRn.setStatus("current")
_CfprTrigLocalSchedAdminState_Type = CfprTrigAdminState
_CfprTrigLocalSchedAdminState_Object = MibTableColumn
cfprTrigLocalSchedAdminState = _CfprTrigLocalSchedAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 4, 1, 4),
    _CfprTrigLocalSchedAdminState_Type()
)
cfprTrigLocalSchedAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigLocalSchedAdminState.setStatus("current")
_CfprTrigLocalSchedDescr_Type = SnmpAdminString
_CfprTrigLocalSchedDescr_Object = MibTableColumn
cfprTrigLocalSchedDescr = _CfprTrigLocalSchedDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 4, 1, 5),
    _CfprTrigLocalSchedDescr_Type()
)
cfprTrigLocalSchedDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigLocalSchedDescr.setStatus("current")
_CfprTrigLocalSchedFlgInitialActive_Type = TruthValue
_CfprTrigLocalSchedFlgInitialActive_Object = MibTableColumn
cfprTrigLocalSchedFlgInitialActive = _CfprTrigLocalSchedFlgInitialActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 4, 1, 6),
    _CfprTrigLocalSchedFlgInitialActive_Type()
)
cfprTrigLocalSchedFlgInitialActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigLocalSchedFlgInitialActive.setStatus("current")
_CfprTrigLocalSchedIntId_Type = SnmpAdminString
_CfprTrigLocalSchedIntId_Object = MibTableColumn
cfprTrigLocalSchedIntId = _CfprTrigLocalSchedIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 4, 1, 7),
    _CfprTrigLocalSchedIntId_Type()
)
cfprTrigLocalSchedIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigLocalSchedIntId.setStatus("current")
_CfprTrigLocalSchedName_Type = SnmpAdminString
_CfprTrigLocalSchedName_Object = MibTableColumn
cfprTrigLocalSchedName = _CfprTrigLocalSchedName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 4, 1, 8),
    _CfprTrigLocalSchedName_Type()
)
cfprTrigLocalSchedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigLocalSchedName.setStatus("current")
_CfprTrigLocalSchedOperState_Type = CfprTrigOperState
_CfprTrigLocalSchedOperState_Object = MibTableColumn
cfprTrigLocalSchedOperState = _CfprTrigLocalSchedOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 4, 1, 9),
    _CfprTrigLocalSchedOperState_Type()
)
cfprTrigLocalSchedOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigLocalSchedOperState.setStatus("current")
_CfprTrigLocalSchedPolicyLevel_Type = Gauge32
_CfprTrigLocalSchedPolicyLevel_Object = MibTableColumn
cfprTrigLocalSchedPolicyLevel = _CfprTrigLocalSchedPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 4, 1, 10),
    _CfprTrigLocalSchedPolicyLevel_Type()
)
cfprTrigLocalSchedPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigLocalSchedPolicyLevel.setStatus("current")
_CfprTrigLocalSchedPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprTrigLocalSchedPolicyOwner_Object = MibTableColumn
cfprTrigLocalSchedPolicyOwner = _CfprTrigLocalSchedPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 4, 1, 11),
    _CfprTrigLocalSchedPolicyOwner_Type()
)
cfprTrigLocalSchedPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigLocalSchedPolicyOwner.setStatus("current")
_CfprTrigMetaTable_Object = MibTable
cfprTrigMetaTable = _CfprTrigMetaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 5)
)
if mibBuilder.loadTexts:
    cfprTrigMetaTable.setStatus("current")
_CfprTrigMetaEntry_Object = MibTableRow
cfprTrigMetaEntry = _CfprTrigMetaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 5, 1)
)
cfprTrigMetaEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-TRIG-MIB", "cfprTrigMetaInstanceId"),
)
if mibBuilder.loadTexts:
    cfprTrigMetaEntry.setStatus("current")
_CfprTrigMetaInstanceId_Type = CfprManagedObjectId
_CfprTrigMetaInstanceId_Object = MibTableColumn
cfprTrigMetaInstanceId = _CfprTrigMetaInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 5, 1, 1),
    _CfprTrigMetaInstanceId_Type()
)
cfprTrigMetaInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprTrigMetaInstanceId.setStatus("current")
_CfprTrigMetaDn_Type = CfprManagedObjectDn
_CfprTrigMetaDn_Object = MibTableColumn
cfprTrigMetaDn = _CfprTrigMetaDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 5, 1, 2),
    _CfprTrigMetaDn_Type()
)
cfprTrigMetaDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigMetaDn.setStatus("current")
_CfprTrigMetaRn_Type = SnmpAdminString
_CfprTrigMetaRn_Object = MibTableColumn
cfprTrigMetaRn = _CfprTrigMetaRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 5, 1, 3),
    _CfprTrigMetaRn_Type()
)
cfprTrigMetaRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigMetaRn.setStatus("current")
_CfprTrigMetaAdminState_Type = CfprTrigAdminState
_CfprTrigMetaAdminState_Object = MibTableColumn
cfprTrigMetaAdminState = _CfprTrigMetaAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 5, 1, 4),
    _CfprTrigMetaAdminState_Type()
)
cfprTrigMetaAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigMetaAdminState.setStatus("current")
_CfprTrigMetaDescr_Type = SnmpAdminString
_CfprTrigMetaDescr_Object = MibTableColumn
cfprTrigMetaDescr = _CfprTrigMetaDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 5, 1, 5),
    _CfprTrigMetaDescr_Type()
)
cfprTrigMetaDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigMetaDescr.setStatus("current")
_CfprTrigMetaIntId_Type = SnmpAdminString
_CfprTrigMetaIntId_Object = MibTableColumn
cfprTrigMetaIntId = _CfprTrigMetaIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 5, 1, 6),
    _CfprTrigMetaIntId_Type()
)
cfprTrigMetaIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigMetaIntId.setStatus("current")
_CfprTrigMetaJobCount_Type = Gauge32
_CfprTrigMetaJobCount_Object = MibTableColumn
cfprTrigMetaJobCount = _CfprTrigMetaJobCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 5, 1, 7),
    _CfprTrigMetaJobCount_Type()
)
cfprTrigMetaJobCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigMetaJobCount.setStatus("current")
_CfprTrigMetaName_Type = SnmpAdminString
_CfprTrigMetaName_Object = MibTableColumn
cfprTrigMetaName = _CfprTrigMetaName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 5, 1, 8),
    _CfprTrigMetaName_Type()
)
cfprTrigMetaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigMetaName.setStatus("current")
_CfprTrigMetaOperState_Type = CfprTrigOperState
_CfprTrigMetaOperState_Object = MibTableColumn
cfprTrigMetaOperState = _CfprTrigMetaOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 5, 1, 9),
    _CfprTrigMetaOperState_Type()
)
cfprTrigMetaOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigMetaOperState.setStatus("current")
_CfprTrigMetaPolicyLevel_Type = Gauge32
_CfprTrigMetaPolicyLevel_Object = MibTableColumn
cfprTrigMetaPolicyLevel = _CfprTrigMetaPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 5, 1, 10),
    _CfprTrigMetaPolicyLevel_Type()
)
cfprTrigMetaPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigMetaPolicyLevel.setStatus("current")
_CfprTrigMetaPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprTrigMetaPolicyOwner_Object = MibTableColumn
cfprTrigMetaPolicyOwner = _CfprTrigMetaPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 5, 1, 11),
    _CfprTrigMetaPolicyOwner_Type()
)
cfprTrigMetaPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigMetaPolicyOwner.setStatus("current")
_CfprTrigMetaSchedName_Type = SnmpAdminString
_CfprTrigMetaSchedName_Object = MibTableColumn
cfprTrigMetaSchedName = _CfprTrigMetaSchedName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 5, 1, 12),
    _CfprTrigMetaSchedName_Type()
)
cfprTrigMetaSchedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigMetaSchedName.setStatus("current")
_CfprTrigMetaTrigTime_Type = DateAndTime
_CfprTrigMetaTrigTime_Object = MibTableColumn
cfprTrigMetaTrigTime = _CfprTrigMetaTrigTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 5, 1, 13),
    _CfprTrigMetaTrigTime_Type()
)
cfprTrigMetaTrigTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigMetaTrigTime.setStatus("current")
_CfprTrigMetaWindowDn_Type = SnmpAdminString
_CfprTrigMetaWindowDn_Object = MibTableColumn
cfprTrigMetaWindowDn = _CfprTrigMetaWindowDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 5, 1, 14),
    _CfprTrigMetaWindowDn_Type()
)
cfprTrigMetaWindowDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigMetaWindowDn.setStatus("current")
_CfprTrigRecurrWindowTable_Object = MibTable
cfprTrigRecurrWindowTable = _CfprTrigRecurrWindowTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 6)
)
if mibBuilder.loadTexts:
    cfprTrigRecurrWindowTable.setStatus("current")
_CfprTrigRecurrWindowEntry_Object = MibTableRow
cfprTrigRecurrWindowEntry = _CfprTrigRecurrWindowEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 6, 1)
)
cfprTrigRecurrWindowEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-TRIG-MIB", "cfprTrigRecurrWindowInstanceId"),
)
if mibBuilder.loadTexts:
    cfprTrigRecurrWindowEntry.setStatus("current")
_CfprTrigRecurrWindowInstanceId_Type = CfprManagedObjectId
_CfprTrigRecurrWindowInstanceId_Object = MibTableColumn
cfprTrigRecurrWindowInstanceId = _CfprTrigRecurrWindowInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 6, 1, 1),
    _CfprTrigRecurrWindowInstanceId_Type()
)
cfprTrigRecurrWindowInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprTrigRecurrWindowInstanceId.setStatus("current")
_CfprTrigRecurrWindowDn_Type = CfprManagedObjectDn
_CfprTrigRecurrWindowDn_Object = MibTableColumn
cfprTrigRecurrWindowDn = _CfprTrigRecurrWindowDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 6, 1, 2),
    _CfprTrigRecurrWindowDn_Type()
)
cfprTrigRecurrWindowDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigRecurrWindowDn.setStatus("current")
_CfprTrigRecurrWindowRn_Type = SnmpAdminString
_CfprTrigRecurrWindowRn_Object = MibTableColumn
cfprTrigRecurrWindowRn = _CfprTrigRecurrWindowRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 6, 1, 3),
    _CfprTrigRecurrWindowRn_Type()
)
cfprTrigRecurrWindowRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigRecurrWindowRn.setStatus("current")
_CfprTrigRecurrWindowConcurCap_Type = Gauge32
_CfprTrigRecurrWindowConcurCap_Object = MibTableColumn
cfprTrigRecurrWindowConcurCap = _CfprTrigRecurrWindowConcurCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 6, 1, 4),
    _CfprTrigRecurrWindowConcurCap_Type()
)
cfprTrigRecurrWindowConcurCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigRecurrWindowConcurCap.setStatus("current")
_CfprTrigRecurrWindowDay_Type = CfprTrigDay
_CfprTrigRecurrWindowDay_Object = MibTableColumn
cfprTrigRecurrWindowDay = _CfprTrigRecurrWindowDay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 6, 1, 5),
    _CfprTrigRecurrWindowDay_Type()
)
cfprTrigRecurrWindowDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigRecurrWindowDay.setStatus("current")
_CfprTrigRecurrWindowHour_Type = Gauge32
_CfprTrigRecurrWindowHour_Object = MibTableColumn
cfprTrigRecurrWindowHour = _CfprTrigRecurrWindowHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 6, 1, 6),
    _CfprTrigRecurrWindowHour_Type()
)
cfprTrigRecurrWindowHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigRecurrWindowHour.setStatus("current")
_CfprTrigRecurrWindowJobCount_Type = Gauge32
_CfprTrigRecurrWindowJobCount_Object = MibTableColumn
cfprTrigRecurrWindowJobCount = _CfprTrigRecurrWindowJobCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 6, 1, 7),
    _CfprTrigRecurrWindowJobCount_Type()
)
cfprTrigRecurrWindowJobCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigRecurrWindowJobCount.setStatus("current")
_CfprTrigRecurrWindowMinute_Type = Gauge32
_CfprTrigRecurrWindowMinute_Object = MibTableColumn
cfprTrigRecurrWindowMinute = _CfprTrigRecurrWindowMinute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 6, 1, 8),
    _CfprTrigRecurrWindowMinute_Type()
)
cfprTrigRecurrWindowMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigRecurrWindowMinute.setStatus("current")
_CfprTrigRecurrWindowName_Type = SnmpAdminString
_CfprTrigRecurrWindowName_Object = MibTableColumn
cfprTrigRecurrWindowName = _CfprTrigRecurrWindowName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 6, 1, 9),
    _CfprTrigRecurrWindowName_Type()
)
cfprTrigRecurrWindowName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigRecurrWindowName.setStatus("current")
_CfprTrigRecurrWindowProcBreak_Type = SnmpAdminString
_CfprTrigRecurrWindowProcBreak_Object = MibTableColumn
cfprTrigRecurrWindowProcBreak = _CfprTrigRecurrWindowProcBreak_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 6, 1, 10),
    _CfprTrigRecurrWindowProcBreak_Type()
)
cfprTrigRecurrWindowProcBreak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigRecurrWindowProcBreak.setStatus("current")
_CfprTrigRecurrWindowProcCap_Type = Gauge32
_CfprTrigRecurrWindowProcCap_Object = MibTableColumn
cfprTrigRecurrWindowProcCap = _CfprTrigRecurrWindowProcCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 6, 1, 11),
    _CfprTrigRecurrWindowProcCap_Type()
)
cfprTrigRecurrWindowProcCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigRecurrWindowProcCap.setStatus("current")
_CfprTrigRecurrWindowTimeCap_Type = SnmpAdminString
_CfprTrigRecurrWindowTimeCap_Object = MibTableColumn
cfprTrigRecurrWindowTimeCap = _CfprTrigRecurrWindowTimeCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 6, 1, 12),
    _CfprTrigRecurrWindowTimeCap_Type()
)
cfprTrigRecurrWindowTimeCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigRecurrWindowTimeCap.setStatus("current")
_CfprTrigSchedTable_Object = MibTable
cfprTrigSchedTable = _CfprTrigSchedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 7)
)
if mibBuilder.loadTexts:
    cfprTrigSchedTable.setStatus("current")
_CfprTrigSchedEntry_Object = MibTableRow
cfprTrigSchedEntry = _CfprTrigSchedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 7, 1)
)
cfprTrigSchedEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-TRIG-MIB", "cfprTrigSchedInstanceId"),
)
if mibBuilder.loadTexts:
    cfprTrigSchedEntry.setStatus("current")
_CfprTrigSchedInstanceId_Type = CfprManagedObjectId
_CfprTrigSchedInstanceId_Object = MibTableColumn
cfprTrigSchedInstanceId = _CfprTrigSchedInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 7, 1, 1),
    _CfprTrigSchedInstanceId_Type()
)
cfprTrigSchedInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprTrigSchedInstanceId.setStatus("current")
_CfprTrigSchedDn_Type = CfprManagedObjectDn
_CfprTrigSchedDn_Object = MibTableColumn
cfprTrigSchedDn = _CfprTrigSchedDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 7, 1, 2),
    _CfprTrigSchedDn_Type()
)
cfprTrigSchedDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigSchedDn.setStatus("current")
_CfprTrigSchedRn_Type = SnmpAdminString
_CfprTrigSchedRn_Object = MibTableColumn
cfprTrigSchedRn = _CfprTrigSchedRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 7, 1, 3),
    _CfprTrigSchedRn_Type()
)
cfprTrigSchedRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigSchedRn.setStatus("current")
_CfprTrigSchedAdminState_Type = CfprTrigAdminState
_CfprTrigSchedAdminState_Object = MibTableColumn
cfprTrigSchedAdminState = _CfprTrigSchedAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 7, 1, 4),
    _CfprTrigSchedAdminState_Type()
)
cfprTrigSchedAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigSchedAdminState.setStatus("current")
_CfprTrigSchedDescr_Type = SnmpAdminString
_CfprTrigSchedDescr_Object = MibTableColumn
cfprTrigSchedDescr = _CfprTrigSchedDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 7, 1, 5),
    _CfprTrigSchedDescr_Type()
)
cfprTrigSchedDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigSchedDescr.setStatus("current")
_CfprTrigSchedFlgInitialActive_Type = TruthValue
_CfprTrigSchedFlgInitialActive_Object = MibTableColumn
cfprTrigSchedFlgInitialActive = _CfprTrigSchedFlgInitialActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 7, 1, 6),
    _CfprTrigSchedFlgInitialActive_Type()
)
cfprTrigSchedFlgInitialActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigSchedFlgInitialActive.setStatus("current")
_CfprTrigSchedIntId_Type = SnmpAdminString
_CfprTrigSchedIntId_Object = MibTableColumn
cfprTrigSchedIntId = _CfprTrigSchedIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 7, 1, 7),
    _CfprTrigSchedIntId_Type()
)
cfprTrigSchedIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigSchedIntId.setStatus("current")
_CfprTrigSchedName_Type = SnmpAdminString
_CfprTrigSchedName_Object = MibTableColumn
cfprTrigSchedName = _CfprTrigSchedName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 7, 1, 8),
    _CfprTrigSchedName_Type()
)
cfprTrigSchedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigSchedName.setStatus("current")
_CfprTrigSchedOperState_Type = CfprTrigOperState
_CfprTrigSchedOperState_Object = MibTableColumn
cfprTrigSchedOperState = _CfprTrigSchedOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 7, 1, 9),
    _CfprTrigSchedOperState_Type()
)
cfprTrigSchedOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigSchedOperState.setStatus("current")
_CfprTrigSchedPolicyLevel_Type = Gauge32
_CfprTrigSchedPolicyLevel_Object = MibTableColumn
cfprTrigSchedPolicyLevel = _CfprTrigSchedPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 7, 1, 10),
    _CfprTrigSchedPolicyLevel_Type()
)
cfprTrigSchedPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigSchedPolicyLevel.setStatus("current")
_CfprTrigSchedPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprTrigSchedPolicyOwner_Object = MibTableColumn
cfprTrigSchedPolicyOwner = _CfprTrigSchedPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 7, 1, 11),
    _CfprTrigSchedPolicyOwner_Type()
)
cfprTrigSchedPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigSchedPolicyOwner.setStatus("current")
_CfprTrigTestTable_Object = MibTable
cfprTrigTestTable = _CfprTrigTestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 8)
)
if mibBuilder.loadTexts:
    cfprTrigTestTable.setStatus("current")
_CfprTrigTestEntry_Object = MibTableRow
cfprTrigTestEntry = _CfprTrigTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 8, 1)
)
cfprTrigTestEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-TRIG-MIB", "cfprTrigTestInstanceId"),
)
if mibBuilder.loadTexts:
    cfprTrigTestEntry.setStatus("current")
_CfprTrigTestInstanceId_Type = CfprManagedObjectId
_CfprTrigTestInstanceId_Object = MibTableColumn
cfprTrigTestInstanceId = _CfprTrigTestInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 8, 1, 1),
    _CfprTrigTestInstanceId_Type()
)
cfprTrigTestInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprTrigTestInstanceId.setStatus("current")
_CfprTrigTestDn_Type = CfprManagedObjectDn
_CfprTrigTestDn_Object = MibTableColumn
cfprTrigTestDn = _CfprTrigTestDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 8, 1, 2),
    _CfprTrigTestDn_Type()
)
cfprTrigTestDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigTestDn.setStatus("current")
_CfprTrigTestRn_Type = SnmpAdminString
_CfprTrigTestRn_Object = MibTableColumn
cfprTrigTestRn = _CfprTrigTestRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 8, 1, 3),
    _CfprTrigTestRn_Type()
)
cfprTrigTestRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigTestRn.setStatus("current")
_CfprTrigTestAdminState_Type = CfprTrigAdminState
_CfprTrigTestAdminState_Object = MibTableColumn
cfprTrigTestAdminState = _CfprTrigTestAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 8, 1, 4),
    _CfprTrigTestAdminState_Type()
)
cfprTrigTestAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigTestAdminState.setStatus("current")
_CfprTrigTestAutoDelete_Type = TruthValue
_CfprTrigTestAutoDelete_Object = MibTableColumn
cfprTrigTestAutoDelete = _CfprTrigTestAutoDelete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 8, 1, 5),
    _CfprTrigTestAutoDelete_Type()
)
cfprTrigTestAutoDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigTestAutoDelete.setStatus("current")
_CfprTrigTestCreationDate_Type = DateAndTime
_CfprTrigTestCreationDate_Object = MibTableColumn
cfprTrigTestCreationDate = _CfprTrigTestCreationDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 8, 1, 6),
    _CfprTrigTestCreationDate_Type()
)
cfprTrigTestCreationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigTestCreationDate.setStatus("current")
_CfprTrigTestDescr_Type = SnmpAdminString
_CfprTrigTestDescr_Object = MibTableColumn
cfprTrigTestDescr = _CfprTrigTestDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 8, 1, 7),
    _CfprTrigTestDescr_Type()
)
cfprTrigTestDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigTestDescr.setStatus("current")
_CfprTrigTestIgnoreCap_Type = TruthValue
_CfprTrigTestIgnoreCap_Object = MibTableColumn
cfprTrigTestIgnoreCap = _CfprTrigTestIgnoreCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 8, 1, 8),
    _CfprTrigTestIgnoreCap_Type()
)
cfprTrigTestIgnoreCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigTestIgnoreCap.setStatus("current")
_CfprTrigTestIntId_Type = SnmpAdminString
_CfprTrigTestIntId_Object = MibTableColumn
cfprTrigTestIntId = _CfprTrigTestIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 8, 1, 9),
    _CfprTrigTestIntId_Type()
)
cfprTrigTestIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigTestIntId.setStatus("current")
_CfprTrigTestName_Type = SnmpAdminString
_CfprTrigTestName_Object = MibTableColumn
cfprTrigTestName = _CfprTrigTestName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 8, 1, 10),
    _CfprTrigTestName_Type()
)
cfprTrigTestName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigTestName.setStatus("current")
_CfprTrigTestOperScheduler_Type = SnmpAdminString
_CfprTrigTestOperScheduler_Object = MibTableColumn
cfprTrigTestOperScheduler = _CfprTrigTestOperScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 8, 1, 11),
    _CfprTrigTestOperScheduler_Type()
)
cfprTrigTestOperScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigTestOperScheduler.setStatus("current")
_CfprTrigTestOperState_Type = CfprTrigTrigOperState
_CfprTrigTestOperState_Object = MibTableColumn
cfprTrigTestOperState = _CfprTrigTestOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 8, 1, 12),
    _CfprTrigTestOperState_Type()
)
cfprTrigTestOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigTestOperState.setStatus("current")
_CfprTrigTestPolicyLevel_Type = Gauge32
_CfprTrigTestPolicyLevel_Object = MibTableColumn
cfprTrigTestPolicyLevel = _CfprTrigTestPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 8, 1, 13),
    _CfprTrigTestPolicyLevel_Type()
)
cfprTrigTestPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigTestPolicyLevel.setStatus("current")
_CfprTrigTestPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprTrigTestPolicyOwner_Object = MibTableColumn
cfprTrigTestPolicyOwner = _CfprTrigTestPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 8, 1, 14),
    _CfprTrigTestPolicyOwner_Type()
)
cfprTrigTestPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigTestPolicyOwner.setStatus("current")
_CfprTrigTestScheduler_Type = SnmpAdminString
_CfprTrigTestScheduler_Object = MibTableColumn
cfprTrigTestScheduler = _CfprTrigTestScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 8, 1, 15),
    _CfprTrigTestScheduler_Type()
)
cfprTrigTestScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigTestScheduler.setStatus("current")
_CfprTrigTriggeredTable_Object = MibTable
cfprTrigTriggeredTable = _CfprTrigTriggeredTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 9)
)
if mibBuilder.loadTexts:
    cfprTrigTriggeredTable.setStatus("current")
_CfprTrigTriggeredEntry_Object = MibTableRow
cfprTrigTriggeredEntry = _CfprTrigTriggeredEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 9, 1)
)
cfprTrigTriggeredEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-TRIG-MIB", "cfprTrigTriggeredInstanceId"),
)
if mibBuilder.loadTexts:
    cfprTrigTriggeredEntry.setStatus("current")
_CfprTrigTriggeredInstanceId_Type = CfprManagedObjectId
_CfprTrigTriggeredInstanceId_Object = MibTableColumn
cfprTrigTriggeredInstanceId = _CfprTrigTriggeredInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 9, 1, 1),
    _CfprTrigTriggeredInstanceId_Type()
)
cfprTrigTriggeredInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprTrigTriggeredInstanceId.setStatus("current")
_CfprTrigTriggeredDn_Type = CfprManagedObjectDn
_CfprTrigTriggeredDn_Object = MibTableColumn
cfprTrigTriggeredDn = _CfprTrigTriggeredDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 9, 1, 2),
    _CfprTrigTriggeredDn_Type()
)
cfprTrigTriggeredDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigTriggeredDn.setStatus("current")
_CfprTrigTriggeredRn_Type = SnmpAdminString
_CfprTrigTriggeredRn_Object = MibTableColumn
cfprTrigTriggeredRn = _CfprTrigTriggeredRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 9, 1, 3),
    _CfprTrigTriggeredRn_Type()
)
cfprTrigTriggeredRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigTriggeredRn.setStatus("current")
_CfprTrigTriggeredJobCount_Type = Gauge32
_CfprTrigTriggeredJobCount_Object = MibTableColumn
cfprTrigTriggeredJobCount = _CfprTrigTriggeredJobCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 9, 1, 4),
    _CfprTrigTriggeredJobCount_Type()
)
cfprTrigTriggeredJobCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigTriggeredJobCount.setStatus("current")
_CfprTrigTriggeredOperState_Type = CfprTrigTriggeredState
_CfprTrigTriggeredOperState_Object = MibTableColumn
cfprTrigTriggeredOperState = _CfprTrigTriggeredOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 9, 1, 5),
    _CfprTrigTriggeredOperState_Type()
)
cfprTrigTriggeredOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigTriggeredOperState.setStatus("current")
_CfprTrigTriggeredOrder_Type = Gauge32
_CfprTrigTriggeredOrder_Object = MibTableColumn
cfprTrigTriggeredOrder = _CfprTrigTriggeredOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 9, 1, 6),
    _CfprTrigTriggeredOrder_Type()
)
cfprTrigTriggeredOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigTriggeredOrder.setStatus("current")
_CfprTrigTriggeredTrDn_Type = SnmpAdminString
_CfprTrigTriggeredTrDn_Object = MibTableColumn
cfprTrigTriggeredTrDn = _CfprTrigTriggeredTrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 9, 1, 7),
    _CfprTrigTriggeredTrDn_Type()
)
cfprTrigTriggeredTrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigTriggeredTrDn.setStatus("current")
_CfprTrigTriggeredTrId_Type = Gauge32
_CfprTrigTriggeredTrId_Object = MibTableColumn
cfprTrigTriggeredTrId = _CfprTrigTriggeredTrId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 79, 9, 1, 8),
    _CfprTrigTriggeredTrId_Type()
)
cfprTrigTriggeredTrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprTrigTriggeredTrId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-TRIG-MIB",
    **{"cfprTrigObjects": cfprTrigObjects,
       "cfprTrigAbsWindowTable": cfprTrigAbsWindowTable,
       "cfprTrigAbsWindowEntry": cfprTrigAbsWindowEntry,
       "cfprTrigAbsWindowInstanceId": cfprTrigAbsWindowInstanceId,
       "cfprTrigAbsWindowDn": cfprTrigAbsWindowDn,
       "cfprTrigAbsWindowRn": cfprTrigAbsWindowRn,
       "cfprTrigAbsWindowConcurCap": cfprTrigAbsWindowConcurCap,
       "cfprTrigAbsWindowDate": cfprTrigAbsWindowDate,
       "cfprTrigAbsWindowJobCount": cfprTrigAbsWindowJobCount,
       "cfprTrigAbsWindowName": cfprTrigAbsWindowName,
       "cfprTrigAbsWindowProcBreak": cfprTrigAbsWindowProcBreak,
       "cfprTrigAbsWindowProcCap": cfprTrigAbsWindowProcCap,
       "cfprTrigAbsWindowTimeCap": cfprTrigAbsWindowTimeCap,
       "cfprTrigAbsWindowStart": cfprTrigAbsWindowStart,
       "cfprTrigClientTokenTable": cfprTrigClientTokenTable,
       "cfprTrigClientTokenEntry": cfprTrigClientTokenEntry,
       "cfprTrigClientTokenInstanceId": cfprTrigClientTokenInstanceId,
       "cfprTrigClientTokenDn": cfprTrigClientTokenDn,
       "cfprTrigClientTokenRn": cfprTrigClientTokenRn,
       "cfprTrigClientTokenActivityTs": cfprTrigClientTokenActivityTs,
       "cfprTrigClientTokenId": cfprTrigClientTokenId,
       "cfprTrigClientTokenOperState": cfprTrigClientTokenOperState,
       "cfprTrigLocalAbsWindowTable": cfprTrigLocalAbsWindowTable,
       "cfprTrigLocalAbsWindowEntry": cfprTrigLocalAbsWindowEntry,
       "cfprTrigLocalAbsWindowInstanceId": cfprTrigLocalAbsWindowInstanceId,
       "cfprTrigLocalAbsWindowDn": cfprTrigLocalAbsWindowDn,
       "cfprTrigLocalAbsWindowRn": cfprTrigLocalAbsWindowRn,
       "cfprTrigLocalAbsWindowConcurCap": cfprTrigLocalAbsWindowConcurCap,
       "cfprTrigLocalAbsWindowDate": cfprTrigLocalAbsWindowDate,
       "cfprTrigLocalAbsWindowJobCount": cfprTrigLocalAbsWindowJobCount,
       "cfprTrigLocalAbsWindowName": cfprTrigLocalAbsWindowName,
       "cfprTrigLocalAbsWindowProcBreak": cfprTrigLocalAbsWindowProcBreak,
       "cfprTrigLocalAbsWindowProcCap": cfprTrigLocalAbsWindowProcCap,
       "cfprTrigLocalAbsWindowTimeCap": cfprTrigLocalAbsWindowTimeCap,
       "cfprTrigLocalAbsWindowStart": cfprTrigLocalAbsWindowStart,
       "cfprTrigLocalSchedTable": cfprTrigLocalSchedTable,
       "cfprTrigLocalSchedEntry": cfprTrigLocalSchedEntry,
       "cfprTrigLocalSchedInstanceId": cfprTrigLocalSchedInstanceId,
       "cfprTrigLocalSchedDn": cfprTrigLocalSchedDn,
       "cfprTrigLocalSchedRn": cfprTrigLocalSchedRn,
       "cfprTrigLocalSchedAdminState": cfprTrigLocalSchedAdminState,
       "cfprTrigLocalSchedDescr": cfprTrigLocalSchedDescr,
       "cfprTrigLocalSchedFlgInitialActive": cfprTrigLocalSchedFlgInitialActive,
       "cfprTrigLocalSchedIntId": cfprTrigLocalSchedIntId,
       "cfprTrigLocalSchedName": cfprTrigLocalSchedName,
       "cfprTrigLocalSchedOperState": cfprTrigLocalSchedOperState,
       "cfprTrigLocalSchedPolicyLevel": cfprTrigLocalSchedPolicyLevel,
       "cfprTrigLocalSchedPolicyOwner": cfprTrigLocalSchedPolicyOwner,
       "cfprTrigMetaTable": cfprTrigMetaTable,
       "cfprTrigMetaEntry": cfprTrigMetaEntry,
       "cfprTrigMetaInstanceId": cfprTrigMetaInstanceId,
       "cfprTrigMetaDn": cfprTrigMetaDn,
       "cfprTrigMetaRn": cfprTrigMetaRn,
       "cfprTrigMetaAdminState": cfprTrigMetaAdminState,
       "cfprTrigMetaDescr": cfprTrigMetaDescr,
       "cfprTrigMetaIntId": cfprTrigMetaIntId,
       "cfprTrigMetaJobCount": cfprTrigMetaJobCount,
       "cfprTrigMetaName": cfprTrigMetaName,
       "cfprTrigMetaOperState": cfprTrigMetaOperState,
       "cfprTrigMetaPolicyLevel": cfprTrigMetaPolicyLevel,
       "cfprTrigMetaPolicyOwner": cfprTrigMetaPolicyOwner,
       "cfprTrigMetaSchedName": cfprTrigMetaSchedName,
       "cfprTrigMetaTrigTime": cfprTrigMetaTrigTime,
       "cfprTrigMetaWindowDn": cfprTrigMetaWindowDn,
       "cfprTrigRecurrWindowTable": cfprTrigRecurrWindowTable,
       "cfprTrigRecurrWindowEntry": cfprTrigRecurrWindowEntry,
       "cfprTrigRecurrWindowInstanceId": cfprTrigRecurrWindowInstanceId,
       "cfprTrigRecurrWindowDn": cfprTrigRecurrWindowDn,
       "cfprTrigRecurrWindowRn": cfprTrigRecurrWindowRn,
       "cfprTrigRecurrWindowConcurCap": cfprTrigRecurrWindowConcurCap,
       "cfprTrigRecurrWindowDay": cfprTrigRecurrWindowDay,
       "cfprTrigRecurrWindowHour": cfprTrigRecurrWindowHour,
       "cfprTrigRecurrWindowJobCount": cfprTrigRecurrWindowJobCount,
       "cfprTrigRecurrWindowMinute": cfprTrigRecurrWindowMinute,
       "cfprTrigRecurrWindowName": cfprTrigRecurrWindowName,
       "cfprTrigRecurrWindowProcBreak": cfprTrigRecurrWindowProcBreak,
       "cfprTrigRecurrWindowProcCap": cfprTrigRecurrWindowProcCap,
       "cfprTrigRecurrWindowTimeCap": cfprTrigRecurrWindowTimeCap,
       "cfprTrigSchedTable": cfprTrigSchedTable,
       "cfprTrigSchedEntry": cfprTrigSchedEntry,
       "cfprTrigSchedInstanceId": cfprTrigSchedInstanceId,
       "cfprTrigSchedDn": cfprTrigSchedDn,
       "cfprTrigSchedRn": cfprTrigSchedRn,
       "cfprTrigSchedAdminState": cfprTrigSchedAdminState,
       "cfprTrigSchedDescr": cfprTrigSchedDescr,
       "cfprTrigSchedFlgInitialActive": cfprTrigSchedFlgInitialActive,
       "cfprTrigSchedIntId": cfprTrigSchedIntId,
       "cfprTrigSchedName": cfprTrigSchedName,
       "cfprTrigSchedOperState": cfprTrigSchedOperState,
       "cfprTrigSchedPolicyLevel": cfprTrigSchedPolicyLevel,
       "cfprTrigSchedPolicyOwner": cfprTrigSchedPolicyOwner,
       "cfprTrigTestTable": cfprTrigTestTable,
       "cfprTrigTestEntry": cfprTrigTestEntry,
       "cfprTrigTestInstanceId": cfprTrigTestInstanceId,
       "cfprTrigTestDn": cfprTrigTestDn,
       "cfprTrigTestRn": cfprTrigTestRn,
       "cfprTrigTestAdminState": cfprTrigTestAdminState,
       "cfprTrigTestAutoDelete": cfprTrigTestAutoDelete,
       "cfprTrigTestCreationDate": cfprTrigTestCreationDate,
       "cfprTrigTestDescr": cfprTrigTestDescr,
       "cfprTrigTestIgnoreCap": cfprTrigTestIgnoreCap,
       "cfprTrigTestIntId": cfprTrigTestIntId,
       "cfprTrigTestName": cfprTrigTestName,
       "cfprTrigTestOperScheduler": cfprTrigTestOperScheduler,
       "cfprTrigTestOperState": cfprTrigTestOperState,
       "cfprTrigTestPolicyLevel": cfprTrigTestPolicyLevel,
       "cfprTrigTestPolicyOwner": cfprTrigTestPolicyOwner,
       "cfprTrigTestScheduler": cfprTrigTestScheduler,
       "cfprTrigTriggeredTable": cfprTrigTriggeredTable,
       "cfprTrigTriggeredEntry": cfprTrigTriggeredEntry,
       "cfprTrigTriggeredInstanceId": cfprTrigTriggeredInstanceId,
       "cfprTrigTriggeredDn": cfprTrigTriggeredDn,
       "cfprTrigTriggeredRn": cfprTrigTriggeredRn,
       "cfprTrigTriggeredJobCount": cfprTrigTriggeredJobCount,
       "cfprTrigTriggeredOperState": cfprTrigTriggeredOperState,
       "cfprTrigTriggeredOrder": cfprTrigTriggeredOrder,
       "cfprTrigTriggeredTrDn": cfprTrigTriggeredTrDn,
       "cfprTrigTriggeredTrId": cfprTrigTriggeredTrId}
)
