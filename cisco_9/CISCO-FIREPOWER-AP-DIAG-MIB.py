# SNMP MIB module (CISCO-FIREPOWER-AP-DIAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-DIAG-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:15:14 2025
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

(CfprApManagedObjectDn,
 CfprApManagedObjectId,
 ciscoFirepowerApMIBObjects) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-MIB",
    "CfprApManagedObjectDn",
    "CfprApManagedObjectId",
    "ciscoFirepowerApMIBObjects")

(CfprApDiagAdminState,
 CfprApDiagBladeTestType,
 CfprApDiagFailureAction,
 CfprApDiagNetworkTestType,
 CfprApDiagSrvCtrlType,
 CfprApDiagStatus,
 CfprApDiagStatusIssues,
 CfprApDiagSuccessAction,
 CfprApDiagTestOrder,
 CfprApNetworkSwitchId,
 CfprApPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApDiagAdminState",
    "CfprApDiagBladeTestType",
    "CfprApDiagFailureAction",
    "CfprApDiagNetworkTestType",
    "CfprApDiagSrvCtrlType",
    "CfprApDiagStatus",
    "CfprApDiagStatusIssues",
    "CfprApDiagSuccessAction",
    "CfprApDiagTestOrder",
    "CfprApNetworkSwitchId",
    "CfprApPolicyPolicyOwner")

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

cfprApDiagObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApDiagBladeTestTable_Object = MibTable
cfprApDiagBladeTestTable = _CfprApDiagBladeTestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 1)
)
if mibBuilder.loadTexts:
    cfprApDiagBladeTestTable.setStatus("current")
_CfprApDiagBladeTestEntry_Object = MibTableRow
cfprApDiagBladeTestEntry = _CfprApDiagBladeTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 1, 1)
)
cfprApDiagBladeTestEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-DIAG-MIB", "cfprApDiagBladeTestInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApDiagBladeTestEntry.setStatus("current")
_CfprApDiagBladeTestInstanceId_Type = CfprApManagedObjectId
_CfprApDiagBladeTestInstanceId_Object = MibTableColumn
cfprApDiagBladeTestInstanceId = _CfprApDiagBladeTestInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 1, 1, 1),
    _CfprApDiagBladeTestInstanceId_Type()
)
cfprApDiagBladeTestInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApDiagBladeTestInstanceId.setStatus("current")
_CfprApDiagBladeTestDn_Type = CfprApManagedObjectDn
_CfprApDiagBladeTestDn_Object = MibTableColumn
cfprApDiagBladeTestDn = _CfprApDiagBladeTestDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 1, 1, 2),
    _CfprApDiagBladeTestDn_Type()
)
cfprApDiagBladeTestDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagBladeTestDn.setStatus("current")
_CfprApDiagBladeTestRn_Type = SnmpAdminString
_CfprApDiagBladeTestRn_Object = MibTableColumn
cfprApDiagBladeTestRn = _CfprApDiagBladeTestRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 1, 1, 3),
    _CfprApDiagBladeTestRn_Type()
)
cfprApDiagBladeTestRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagBladeTestRn.setStatus("current")
_CfprApDiagBladeTestLength_Type = Gauge32
_CfprApDiagBladeTestLength_Object = MibTableColumn
cfprApDiagBladeTestLength = _CfprApDiagBladeTestLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 1, 1, 4),
    _CfprApDiagBladeTestLength_Type()
)
cfprApDiagBladeTestLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagBladeTestLength.setStatus("current")
_CfprApDiagBladeTestOrder_Type = CfprApDiagTestOrder
_CfprApDiagBladeTestOrder_Object = MibTableColumn
cfprApDiagBladeTestOrder = _CfprApDiagBladeTestOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 1, 1, 5),
    _CfprApDiagBladeTestOrder_Type()
)
cfprApDiagBladeTestOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagBladeTestOrder.setStatus("current")
_CfprApDiagBladeTestType_Type = CfprApDiagBladeTestType
_CfprApDiagBladeTestType_Object = MibTableColumn
cfprApDiagBladeTestType = _CfprApDiagBladeTestType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 1, 1, 6),
    _CfprApDiagBladeTestType_Type()
)
cfprApDiagBladeTestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagBladeTestType.setStatus("current")
_CfprApDiagNetworkTestTable_Object = MibTable
cfprApDiagNetworkTestTable = _CfprApDiagNetworkTestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 2)
)
if mibBuilder.loadTexts:
    cfprApDiagNetworkTestTable.setStatus("current")
_CfprApDiagNetworkTestEntry_Object = MibTableRow
cfprApDiagNetworkTestEntry = _CfprApDiagNetworkTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 2, 1)
)
cfprApDiagNetworkTestEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-DIAG-MIB", "cfprApDiagNetworkTestInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApDiagNetworkTestEntry.setStatus("current")
_CfprApDiagNetworkTestInstanceId_Type = CfprApManagedObjectId
_CfprApDiagNetworkTestInstanceId_Object = MibTableColumn
cfprApDiagNetworkTestInstanceId = _CfprApDiagNetworkTestInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 2, 1, 1),
    _CfprApDiagNetworkTestInstanceId_Type()
)
cfprApDiagNetworkTestInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApDiagNetworkTestInstanceId.setStatus("current")
_CfprApDiagNetworkTestDn_Type = CfprApManagedObjectDn
_CfprApDiagNetworkTestDn_Object = MibTableColumn
cfprApDiagNetworkTestDn = _CfprApDiagNetworkTestDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 2, 1, 2),
    _CfprApDiagNetworkTestDn_Type()
)
cfprApDiagNetworkTestDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagNetworkTestDn.setStatus("current")
_CfprApDiagNetworkTestRn_Type = SnmpAdminString
_CfprApDiagNetworkTestRn_Object = MibTableColumn
cfprApDiagNetworkTestRn = _CfprApDiagNetworkTestRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 2, 1, 3),
    _CfprApDiagNetworkTestRn_Type()
)
cfprApDiagNetworkTestRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagNetworkTestRn.setStatus("current")
_CfprApDiagNetworkTestLength_Type = Gauge32
_CfprApDiagNetworkTestLength_Object = MibTableColumn
cfprApDiagNetworkTestLength = _CfprApDiagNetworkTestLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 2, 1, 4),
    _CfprApDiagNetworkTestLength_Type()
)
cfprApDiagNetworkTestLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagNetworkTestLength.setStatus("current")
_CfprApDiagNetworkTestOrder_Type = CfprApDiagTestOrder
_CfprApDiagNetworkTestOrder_Object = MibTableColumn
cfprApDiagNetworkTestOrder = _CfprApDiagNetworkTestOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 2, 1, 5),
    _CfprApDiagNetworkTestOrder_Type()
)
cfprApDiagNetworkTestOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagNetworkTestOrder.setStatus("current")
_CfprApDiagNetworkTestSwitchId_Type = CfprApNetworkSwitchId
_CfprApDiagNetworkTestSwitchId_Object = MibTableColumn
cfprApDiagNetworkTestSwitchId = _CfprApDiagNetworkTestSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 2, 1, 6),
    _CfprApDiagNetworkTestSwitchId_Type()
)
cfprApDiagNetworkTestSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagNetworkTestSwitchId.setStatus("current")
_CfprApDiagNetworkTestType_Type = CfprApDiagNetworkTestType
_CfprApDiagNetworkTestType_Object = MibTableColumn
cfprApDiagNetworkTestType = _CfprApDiagNetworkTestType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 2, 1, 7),
    _CfprApDiagNetworkTestType_Type()
)
cfprApDiagNetworkTestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagNetworkTestType.setStatus("current")
_CfprApDiagRsltTable_Object = MibTable
cfprApDiagRsltTable = _CfprApDiagRsltTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 3)
)
if mibBuilder.loadTexts:
    cfprApDiagRsltTable.setStatus("current")
_CfprApDiagRsltEntry_Object = MibTableRow
cfprApDiagRsltEntry = _CfprApDiagRsltEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 3, 1)
)
cfprApDiagRsltEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-DIAG-MIB", "cfprApDiagRsltInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApDiagRsltEntry.setStatus("current")
_CfprApDiagRsltInstanceId_Type = CfprApManagedObjectId
_CfprApDiagRsltInstanceId_Object = MibTableColumn
cfprApDiagRsltInstanceId = _CfprApDiagRsltInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 3, 1, 1),
    _CfprApDiagRsltInstanceId_Type()
)
cfprApDiagRsltInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApDiagRsltInstanceId.setStatus("current")
_CfprApDiagRsltDn_Type = CfprApManagedObjectDn
_CfprApDiagRsltDn_Object = MibTableColumn
cfprApDiagRsltDn = _CfprApDiagRsltDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 3, 1, 2),
    _CfprApDiagRsltDn_Type()
)
cfprApDiagRsltDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagRsltDn.setStatus("current")
_CfprApDiagRsltRn_Type = SnmpAdminString
_CfprApDiagRsltRn_Object = MibTableColumn
cfprApDiagRsltRn = _CfprApDiagRsltRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 3, 1, 3),
    _CfprApDiagRsltRn_Type()
)
cfprApDiagRsltRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagRsltRn.setStatus("current")
_CfprApDiagRsltDescr_Type = SnmpAdminString
_CfprApDiagRsltDescr_Object = MibTableColumn
cfprApDiagRsltDescr = _CfprApDiagRsltDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 3, 1, 4),
    _CfprApDiagRsltDescr_Type()
)
cfprApDiagRsltDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagRsltDescr.setStatus("current")
_CfprApDiagRsltEndTs_Type = DateAndTime
_CfprApDiagRsltEndTs_Object = MibTableColumn
cfprApDiagRsltEndTs = _CfprApDiagRsltEndTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 3, 1, 5),
    _CfprApDiagRsltEndTs_Type()
)
cfprApDiagRsltEndTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagRsltEndTs.setStatus("current")
_CfprApDiagRsltId_Type = Gauge32
_CfprApDiagRsltId_Object = MibTableColumn
cfprApDiagRsltId = _CfprApDiagRsltId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 3, 1, 6),
    _CfprApDiagRsltId_Type()
)
cfprApDiagRsltId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagRsltId.setStatus("current")
_CfprApDiagRsltResult_Type = Gauge32
_CfprApDiagRsltResult_Object = MibTableColumn
cfprApDiagRsltResult = _CfprApDiagRsltResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 3, 1, 7),
    _CfprApDiagRsltResult_Type()
)
cfprApDiagRsltResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagRsltResult.setStatus("current")
_CfprApDiagRsltRsltStatus_Type = CfprApDiagStatus
_CfprApDiagRsltRsltStatus_Object = MibTableColumn
cfprApDiagRsltRsltStatus = _CfprApDiagRsltRsltStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 3, 1, 8),
    _CfprApDiagRsltRsltStatus_Type()
)
cfprApDiagRsltRsltStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagRsltRsltStatus.setStatus("current")
_CfprApDiagRsltStartTs_Type = DateAndTime
_CfprApDiagRsltStartTs_Object = MibTableColumn
cfprApDiagRsltStartTs = _CfprApDiagRsltStartTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 3, 1, 9),
    _CfprApDiagRsltStartTs_Type()
)
cfprApDiagRsltStartTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagRsltStartTs.setStatus("current")
_CfprApDiagRunPolicyTable_Object = MibTable
cfprApDiagRunPolicyTable = _CfprApDiagRunPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 4)
)
if mibBuilder.loadTexts:
    cfprApDiagRunPolicyTable.setStatus("current")
_CfprApDiagRunPolicyEntry_Object = MibTableRow
cfprApDiagRunPolicyEntry = _CfprApDiagRunPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 4, 1)
)
cfprApDiagRunPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-DIAG-MIB", "cfprApDiagRunPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApDiagRunPolicyEntry.setStatus("current")
_CfprApDiagRunPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApDiagRunPolicyInstanceId_Object = MibTableColumn
cfprApDiagRunPolicyInstanceId = _CfprApDiagRunPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 4, 1, 1),
    _CfprApDiagRunPolicyInstanceId_Type()
)
cfprApDiagRunPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApDiagRunPolicyInstanceId.setStatus("current")
_CfprApDiagRunPolicyDn_Type = CfprApManagedObjectDn
_CfprApDiagRunPolicyDn_Object = MibTableColumn
cfprApDiagRunPolicyDn = _CfprApDiagRunPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 4, 1, 2),
    _CfprApDiagRunPolicyDn_Type()
)
cfprApDiagRunPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagRunPolicyDn.setStatus("current")
_CfprApDiagRunPolicyRn_Type = SnmpAdminString
_CfprApDiagRunPolicyRn_Object = MibTableColumn
cfprApDiagRunPolicyRn = _CfprApDiagRunPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 4, 1, 3),
    _CfprApDiagRunPolicyRn_Type()
)
cfprApDiagRunPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagRunPolicyRn.setStatus("current")
_CfprApDiagRunPolicyDescr_Type = SnmpAdminString
_CfprApDiagRunPolicyDescr_Object = MibTableColumn
cfprApDiagRunPolicyDescr = _CfprApDiagRunPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 4, 1, 4),
    _CfprApDiagRunPolicyDescr_Type()
)
cfprApDiagRunPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagRunPolicyDescr.setStatus("current")
_CfprApDiagRunPolicyFailureAction_Type = CfprApDiagFailureAction
_CfprApDiagRunPolicyFailureAction_Object = MibTableColumn
cfprApDiagRunPolicyFailureAction = _CfprApDiagRunPolicyFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 4, 1, 5),
    _CfprApDiagRunPolicyFailureAction_Type()
)
cfprApDiagRunPolicyFailureAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagRunPolicyFailureAction.setStatus("current")
_CfprApDiagRunPolicyIntId_Type = SnmpAdminString
_CfprApDiagRunPolicyIntId_Object = MibTableColumn
cfprApDiagRunPolicyIntId = _CfprApDiagRunPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 4, 1, 6),
    _CfprApDiagRunPolicyIntId_Type()
)
cfprApDiagRunPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagRunPolicyIntId.setStatus("current")
_CfprApDiagRunPolicyName_Type = SnmpAdminString
_CfprApDiagRunPolicyName_Object = MibTableColumn
cfprApDiagRunPolicyName = _CfprApDiagRunPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 4, 1, 7),
    _CfprApDiagRunPolicyName_Type()
)
cfprApDiagRunPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagRunPolicyName.setStatus("current")
_CfprApDiagRunPolicyPolicyLevel_Type = Gauge32
_CfprApDiagRunPolicyPolicyLevel_Object = MibTableColumn
cfprApDiagRunPolicyPolicyLevel = _CfprApDiagRunPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 4, 1, 8),
    _CfprApDiagRunPolicyPolicyLevel_Type()
)
cfprApDiagRunPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagRunPolicyPolicyLevel.setStatus("current")
_CfprApDiagRunPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApDiagRunPolicyPolicyOwner_Object = MibTableColumn
cfprApDiagRunPolicyPolicyOwner = _CfprApDiagRunPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 4, 1, 9),
    _CfprApDiagRunPolicyPolicyOwner_Type()
)
cfprApDiagRunPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagRunPolicyPolicyOwner.setStatus("current")
_CfprApDiagRunPolicySuccessAction_Type = CfprApDiagSuccessAction
_CfprApDiagRunPolicySuccessAction_Object = MibTableColumn
cfprApDiagRunPolicySuccessAction = _CfprApDiagRunPolicySuccessAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 4, 1, 10),
    _CfprApDiagRunPolicySuccessAction_Type()
)
cfprApDiagRunPolicySuccessAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagRunPolicySuccessAction.setStatus("current")
_CfprApDiagSrvCapProviderTable_Object = MibTable
cfprApDiagSrvCapProviderTable = _CfprApDiagSrvCapProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 5)
)
if mibBuilder.loadTexts:
    cfprApDiagSrvCapProviderTable.setStatus("current")
_CfprApDiagSrvCapProviderEntry_Object = MibTableRow
cfprApDiagSrvCapProviderEntry = _CfprApDiagSrvCapProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 5, 1)
)
cfprApDiagSrvCapProviderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-DIAG-MIB", "cfprApDiagSrvCapProviderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApDiagSrvCapProviderEntry.setStatus("current")
_CfprApDiagSrvCapProviderInstanceId_Type = CfprApManagedObjectId
_CfprApDiagSrvCapProviderInstanceId_Object = MibTableColumn
cfprApDiagSrvCapProviderInstanceId = _CfprApDiagSrvCapProviderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 5, 1, 1),
    _CfprApDiagSrvCapProviderInstanceId_Type()
)
cfprApDiagSrvCapProviderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApDiagSrvCapProviderInstanceId.setStatus("current")
_CfprApDiagSrvCapProviderDn_Type = CfprApManagedObjectDn
_CfprApDiagSrvCapProviderDn_Object = MibTableColumn
cfprApDiagSrvCapProviderDn = _CfprApDiagSrvCapProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 5, 1, 2),
    _CfprApDiagSrvCapProviderDn_Type()
)
cfprApDiagSrvCapProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagSrvCapProviderDn.setStatus("current")
_CfprApDiagSrvCapProviderRn_Type = SnmpAdminString
_CfprApDiagSrvCapProviderRn_Object = MibTableColumn
cfprApDiagSrvCapProviderRn = _CfprApDiagSrvCapProviderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 5, 1, 3),
    _CfprApDiagSrvCapProviderRn_Type()
)
cfprApDiagSrvCapProviderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagSrvCapProviderRn.setStatus("current")
_CfprApDiagSrvCapProviderDeleted_Type = TruthValue
_CfprApDiagSrvCapProviderDeleted_Object = MibTableColumn
cfprApDiagSrvCapProviderDeleted = _CfprApDiagSrvCapProviderDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 5, 1, 4),
    _CfprApDiagSrvCapProviderDeleted_Type()
)
cfprApDiagSrvCapProviderDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagSrvCapProviderDeleted.setStatus("current")
_CfprApDiagSrvCapProviderDeprecated_Type = TruthValue
_CfprApDiagSrvCapProviderDeprecated_Object = MibTableColumn
cfprApDiagSrvCapProviderDeprecated = _CfprApDiagSrvCapProviderDeprecated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 5, 1, 5),
    _CfprApDiagSrvCapProviderDeprecated_Type()
)
cfprApDiagSrvCapProviderDeprecated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagSrvCapProviderDeprecated.setStatus("current")
_CfprApDiagSrvCapProviderElementLoadFailures_Type = Gauge32
_CfprApDiagSrvCapProviderElementLoadFailures_Object = MibTableColumn
cfprApDiagSrvCapProviderElementLoadFailures = _CfprApDiagSrvCapProviderElementLoadFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 5, 1, 6),
    _CfprApDiagSrvCapProviderElementLoadFailures_Type()
)
cfprApDiagSrvCapProviderElementLoadFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagSrvCapProviderElementLoadFailures.setStatus("current")
_CfprApDiagSrvCapProviderElementsLoaded_Type = Gauge32
_CfprApDiagSrvCapProviderElementsLoaded_Object = MibTableColumn
cfprApDiagSrvCapProviderElementsLoaded = _CfprApDiagSrvCapProviderElementsLoaded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 5, 1, 7),
    _CfprApDiagSrvCapProviderElementsLoaded_Type()
)
cfprApDiagSrvCapProviderElementsLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagSrvCapProviderElementsLoaded.setStatus("current")
_CfprApDiagSrvCapProviderGencount_Type = Gauge32
_CfprApDiagSrvCapProviderGencount_Object = MibTableColumn
cfprApDiagSrvCapProviderGencount = _CfprApDiagSrvCapProviderGencount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 5, 1, 8),
    _CfprApDiagSrvCapProviderGencount_Type()
)
cfprApDiagSrvCapProviderGencount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagSrvCapProviderGencount.setStatus("current")
_CfprApDiagSrvCapProviderLoadErrors_Type = Gauge32
_CfprApDiagSrvCapProviderLoadErrors_Object = MibTableColumn
cfprApDiagSrvCapProviderLoadErrors = _CfprApDiagSrvCapProviderLoadErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 5, 1, 9),
    _CfprApDiagSrvCapProviderLoadErrors_Type()
)
cfprApDiagSrvCapProviderLoadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagSrvCapProviderLoadErrors.setStatus("current")
_CfprApDiagSrvCapProviderLoadWarnings_Type = Gauge32
_CfprApDiagSrvCapProviderLoadWarnings_Object = MibTableColumn
cfprApDiagSrvCapProviderLoadWarnings = _CfprApDiagSrvCapProviderLoadWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 5, 1, 10),
    _CfprApDiagSrvCapProviderLoadWarnings_Type()
)
cfprApDiagSrvCapProviderLoadWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagSrvCapProviderLoadWarnings.setStatus("current")
_CfprApDiagSrvCapProviderMgmtPlaneVer_Type = SnmpAdminString
_CfprApDiagSrvCapProviderMgmtPlaneVer_Object = MibTableColumn
cfprApDiagSrvCapProviderMgmtPlaneVer = _CfprApDiagSrvCapProviderMgmtPlaneVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 5, 1, 11),
    _CfprApDiagSrvCapProviderMgmtPlaneVer_Type()
)
cfprApDiagSrvCapProviderMgmtPlaneVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagSrvCapProviderMgmtPlaneVer.setStatus("current")
_CfprApDiagSrvCapProviderModel_Type = SnmpAdminString
_CfprApDiagSrvCapProviderModel_Object = MibTableColumn
cfprApDiagSrvCapProviderModel = _CfprApDiagSrvCapProviderModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 5, 1, 12),
    _CfprApDiagSrvCapProviderModel_Type()
)
cfprApDiagSrvCapProviderModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagSrvCapProviderModel.setStatus("current")
_CfprApDiagSrvCapProviderPromCardType_Type = Gauge32
_CfprApDiagSrvCapProviderPromCardType_Object = MibTableColumn
cfprApDiagSrvCapProviderPromCardType = _CfprApDiagSrvCapProviderPromCardType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 5, 1, 13),
    _CfprApDiagSrvCapProviderPromCardType_Type()
)
cfprApDiagSrvCapProviderPromCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagSrvCapProviderPromCardType.setStatus("current")
_CfprApDiagSrvCapProviderRevision_Type = SnmpAdminString
_CfprApDiagSrvCapProviderRevision_Object = MibTableColumn
cfprApDiagSrvCapProviderRevision = _CfprApDiagSrvCapProviderRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 5, 1, 14),
    _CfprApDiagSrvCapProviderRevision_Type()
)
cfprApDiagSrvCapProviderRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagSrvCapProviderRevision.setStatus("current")
_CfprApDiagSrvCapProviderVendor_Type = SnmpAdminString
_CfprApDiagSrvCapProviderVendor_Object = MibTableColumn
cfprApDiagSrvCapProviderVendor = _CfprApDiagSrvCapProviderVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 5, 1, 15),
    _CfprApDiagSrvCapProviderVendor_Type()
)
cfprApDiagSrvCapProviderVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagSrvCapProviderVendor.setStatus("current")
_CfprApDiagSrvCtrlTable_Object = MibTable
cfprApDiagSrvCtrlTable = _CfprApDiagSrvCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 6)
)
if mibBuilder.loadTexts:
    cfprApDiagSrvCtrlTable.setStatus("current")
_CfprApDiagSrvCtrlEntry_Object = MibTableRow
cfprApDiagSrvCtrlEntry = _CfprApDiagSrvCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 6, 1)
)
cfprApDiagSrvCtrlEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-DIAG-MIB", "cfprApDiagSrvCtrlInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApDiagSrvCtrlEntry.setStatus("current")
_CfprApDiagSrvCtrlInstanceId_Type = CfprApManagedObjectId
_CfprApDiagSrvCtrlInstanceId_Object = MibTableColumn
cfprApDiagSrvCtrlInstanceId = _CfprApDiagSrvCtrlInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 6, 1, 1),
    _CfprApDiagSrvCtrlInstanceId_Type()
)
cfprApDiagSrvCtrlInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApDiagSrvCtrlInstanceId.setStatus("current")
_CfprApDiagSrvCtrlDn_Type = CfprApManagedObjectDn
_CfprApDiagSrvCtrlDn_Object = MibTableColumn
cfprApDiagSrvCtrlDn = _CfprApDiagSrvCtrlDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 6, 1, 2),
    _CfprApDiagSrvCtrlDn_Type()
)
cfprApDiagSrvCtrlDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagSrvCtrlDn.setStatus("current")
_CfprApDiagSrvCtrlRn_Type = SnmpAdminString
_CfprApDiagSrvCtrlRn_Object = MibTableColumn
cfprApDiagSrvCtrlRn = _CfprApDiagSrvCtrlRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 6, 1, 3),
    _CfprApDiagSrvCtrlRn_Type()
)
cfprApDiagSrvCtrlRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagSrvCtrlRn.setStatus("current")
_CfprApDiagSrvCtrlAdminState_Type = CfprApDiagAdminState
_CfprApDiagSrvCtrlAdminState_Object = MibTableColumn
cfprApDiagSrvCtrlAdminState = _CfprApDiagSrvCtrlAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 6, 1, 4),
    _CfprApDiagSrvCtrlAdminState_Type()
)
cfprApDiagSrvCtrlAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagSrvCtrlAdminState.setStatus("current")
_CfprApDiagSrvCtrlEndTs_Type = DateAndTime
_CfprApDiagSrvCtrlEndTs_Object = MibTableColumn
cfprApDiagSrvCtrlEndTs = _CfprApDiagSrvCtrlEndTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 6, 1, 5),
    _CfprApDiagSrvCtrlEndTs_Type()
)
cfprApDiagSrvCtrlEndTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagSrvCtrlEndTs.setStatus("current")
_CfprApDiagSrvCtrlEndTsM_Type = Unsigned64
_CfprApDiagSrvCtrlEndTsM_Object = MibTableColumn
cfprApDiagSrvCtrlEndTsM = _CfprApDiagSrvCtrlEndTsM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 6, 1, 6),
    _CfprApDiagSrvCtrlEndTsM_Type()
)
cfprApDiagSrvCtrlEndTsM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagSrvCtrlEndTsM.setStatus("current")
_CfprApDiagSrvCtrlErrorDescr_Type = SnmpAdminString
_CfprApDiagSrvCtrlErrorDescr_Object = MibTableColumn
cfprApDiagSrvCtrlErrorDescr = _CfprApDiagSrvCtrlErrorDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 6, 1, 7),
    _CfprApDiagSrvCtrlErrorDescr_Type()
)
cfprApDiagSrvCtrlErrorDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagSrvCtrlErrorDescr.setStatus("current")
_CfprApDiagSrvCtrlImgLoc_Type = SnmpAdminString
_CfprApDiagSrvCtrlImgLoc_Object = MibTableColumn
cfprApDiagSrvCtrlImgLoc = _CfprApDiagSrvCtrlImgLoc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 6, 1, 8),
    _CfprApDiagSrvCtrlImgLoc_Type()
)
cfprApDiagSrvCtrlImgLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagSrvCtrlImgLoc.setStatus("current")
_CfprApDiagSrvCtrlImgName_Type = SnmpAdminString
_CfprApDiagSrvCtrlImgName_Object = MibTableColumn
cfprApDiagSrvCtrlImgName = _CfprApDiagSrvCtrlImgName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 6, 1, 9),
    _CfprApDiagSrvCtrlImgName_Type()
)
cfprApDiagSrvCtrlImgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagSrvCtrlImgName.setStatus("current")
_CfprApDiagSrvCtrlOperQualifier_Type = CfprApDiagStatusIssues
_CfprApDiagSrvCtrlOperQualifier_Object = MibTableColumn
cfprApDiagSrvCtrlOperQualifier = _CfprApDiagSrvCtrlOperQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 6, 1, 10),
    _CfprApDiagSrvCtrlOperQualifier_Type()
)
cfprApDiagSrvCtrlOperQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagSrvCtrlOperQualifier.setStatus("current")
_CfprApDiagSrvCtrlOperState_Type = CfprApDiagStatus
_CfprApDiagSrvCtrlOperState_Object = MibTableColumn
cfprApDiagSrvCtrlOperState = _CfprApDiagSrvCtrlOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 6, 1, 11),
    _CfprApDiagSrvCtrlOperState_Type()
)
cfprApDiagSrvCtrlOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagSrvCtrlOperState.setStatus("current")
_CfprApDiagSrvCtrlRunPolicyName_Type = SnmpAdminString
_CfprApDiagSrvCtrlRunPolicyName_Object = MibTableColumn
cfprApDiagSrvCtrlRunPolicyName = _CfprApDiagSrvCtrlRunPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 6, 1, 12),
    _CfprApDiagSrvCtrlRunPolicyName_Type()
)
cfprApDiagSrvCtrlRunPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagSrvCtrlRunPolicyName.setStatus("current")
_CfprApDiagSrvCtrlStartTs_Type = DateAndTime
_CfprApDiagSrvCtrlStartTs_Object = MibTableColumn
cfprApDiagSrvCtrlStartTs = _CfprApDiagSrvCtrlStartTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 6, 1, 13),
    _CfprApDiagSrvCtrlStartTs_Type()
)
cfprApDiagSrvCtrlStartTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagSrvCtrlStartTs.setStatus("current")
_CfprApDiagSrvCtrlStartTsM_Type = Unsigned64
_CfprApDiagSrvCtrlStartTsM_Object = MibTableColumn
cfprApDiagSrvCtrlStartTsM = _CfprApDiagSrvCtrlStartTsM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 6, 1, 14),
    _CfprApDiagSrvCtrlStartTsM_Type()
)
cfprApDiagSrvCtrlStartTsM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagSrvCtrlStartTsM.setStatus("current")
_CfprApDiagSrvCtrlType_Type = CfprApDiagSrvCtrlType
_CfprApDiagSrvCtrlType_Object = MibTableColumn
cfprApDiagSrvCtrlType = _CfprApDiagSrvCtrlType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 16, 6, 1, 15),
    _CfprApDiagSrvCtrlType_Type()
)
cfprApDiagSrvCtrlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDiagSrvCtrlType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-DIAG-MIB",
    **{"cfprApDiagObjects": cfprApDiagObjects,
       "cfprApDiagBladeTestTable": cfprApDiagBladeTestTable,
       "cfprApDiagBladeTestEntry": cfprApDiagBladeTestEntry,
       "cfprApDiagBladeTestInstanceId": cfprApDiagBladeTestInstanceId,
       "cfprApDiagBladeTestDn": cfprApDiagBladeTestDn,
       "cfprApDiagBladeTestRn": cfprApDiagBladeTestRn,
       "cfprApDiagBladeTestLength": cfprApDiagBladeTestLength,
       "cfprApDiagBladeTestOrder": cfprApDiagBladeTestOrder,
       "cfprApDiagBladeTestType": cfprApDiagBladeTestType,
       "cfprApDiagNetworkTestTable": cfprApDiagNetworkTestTable,
       "cfprApDiagNetworkTestEntry": cfprApDiagNetworkTestEntry,
       "cfprApDiagNetworkTestInstanceId": cfprApDiagNetworkTestInstanceId,
       "cfprApDiagNetworkTestDn": cfprApDiagNetworkTestDn,
       "cfprApDiagNetworkTestRn": cfprApDiagNetworkTestRn,
       "cfprApDiagNetworkTestLength": cfprApDiagNetworkTestLength,
       "cfprApDiagNetworkTestOrder": cfprApDiagNetworkTestOrder,
       "cfprApDiagNetworkTestSwitchId": cfprApDiagNetworkTestSwitchId,
       "cfprApDiagNetworkTestType": cfprApDiagNetworkTestType,
       "cfprApDiagRsltTable": cfprApDiagRsltTable,
       "cfprApDiagRsltEntry": cfprApDiagRsltEntry,
       "cfprApDiagRsltInstanceId": cfprApDiagRsltInstanceId,
       "cfprApDiagRsltDn": cfprApDiagRsltDn,
       "cfprApDiagRsltRn": cfprApDiagRsltRn,
       "cfprApDiagRsltDescr": cfprApDiagRsltDescr,
       "cfprApDiagRsltEndTs": cfprApDiagRsltEndTs,
       "cfprApDiagRsltId": cfprApDiagRsltId,
       "cfprApDiagRsltResult": cfprApDiagRsltResult,
       "cfprApDiagRsltRsltStatus": cfprApDiagRsltRsltStatus,
       "cfprApDiagRsltStartTs": cfprApDiagRsltStartTs,
       "cfprApDiagRunPolicyTable": cfprApDiagRunPolicyTable,
       "cfprApDiagRunPolicyEntry": cfprApDiagRunPolicyEntry,
       "cfprApDiagRunPolicyInstanceId": cfprApDiagRunPolicyInstanceId,
       "cfprApDiagRunPolicyDn": cfprApDiagRunPolicyDn,
       "cfprApDiagRunPolicyRn": cfprApDiagRunPolicyRn,
       "cfprApDiagRunPolicyDescr": cfprApDiagRunPolicyDescr,
       "cfprApDiagRunPolicyFailureAction": cfprApDiagRunPolicyFailureAction,
       "cfprApDiagRunPolicyIntId": cfprApDiagRunPolicyIntId,
       "cfprApDiagRunPolicyName": cfprApDiagRunPolicyName,
       "cfprApDiagRunPolicyPolicyLevel": cfprApDiagRunPolicyPolicyLevel,
       "cfprApDiagRunPolicyPolicyOwner": cfprApDiagRunPolicyPolicyOwner,
       "cfprApDiagRunPolicySuccessAction": cfprApDiagRunPolicySuccessAction,
       "cfprApDiagSrvCapProviderTable": cfprApDiagSrvCapProviderTable,
       "cfprApDiagSrvCapProviderEntry": cfprApDiagSrvCapProviderEntry,
       "cfprApDiagSrvCapProviderInstanceId": cfprApDiagSrvCapProviderInstanceId,
       "cfprApDiagSrvCapProviderDn": cfprApDiagSrvCapProviderDn,
       "cfprApDiagSrvCapProviderRn": cfprApDiagSrvCapProviderRn,
       "cfprApDiagSrvCapProviderDeleted": cfprApDiagSrvCapProviderDeleted,
       "cfprApDiagSrvCapProviderDeprecated": cfprApDiagSrvCapProviderDeprecated,
       "cfprApDiagSrvCapProviderElementLoadFailures": cfprApDiagSrvCapProviderElementLoadFailures,
       "cfprApDiagSrvCapProviderElementsLoaded": cfprApDiagSrvCapProviderElementsLoaded,
       "cfprApDiagSrvCapProviderGencount": cfprApDiagSrvCapProviderGencount,
       "cfprApDiagSrvCapProviderLoadErrors": cfprApDiagSrvCapProviderLoadErrors,
       "cfprApDiagSrvCapProviderLoadWarnings": cfprApDiagSrvCapProviderLoadWarnings,
       "cfprApDiagSrvCapProviderMgmtPlaneVer": cfprApDiagSrvCapProviderMgmtPlaneVer,
       "cfprApDiagSrvCapProviderModel": cfprApDiagSrvCapProviderModel,
       "cfprApDiagSrvCapProviderPromCardType": cfprApDiagSrvCapProviderPromCardType,
       "cfprApDiagSrvCapProviderRevision": cfprApDiagSrvCapProviderRevision,
       "cfprApDiagSrvCapProviderVendor": cfprApDiagSrvCapProviderVendor,
       "cfprApDiagSrvCtrlTable": cfprApDiagSrvCtrlTable,
       "cfprApDiagSrvCtrlEntry": cfprApDiagSrvCtrlEntry,
       "cfprApDiagSrvCtrlInstanceId": cfprApDiagSrvCtrlInstanceId,
       "cfprApDiagSrvCtrlDn": cfprApDiagSrvCtrlDn,
       "cfprApDiagSrvCtrlRn": cfprApDiagSrvCtrlRn,
       "cfprApDiagSrvCtrlAdminState": cfprApDiagSrvCtrlAdminState,
       "cfprApDiagSrvCtrlEndTs": cfprApDiagSrvCtrlEndTs,
       "cfprApDiagSrvCtrlEndTsM": cfprApDiagSrvCtrlEndTsM,
       "cfprApDiagSrvCtrlErrorDescr": cfprApDiagSrvCtrlErrorDescr,
       "cfprApDiagSrvCtrlImgLoc": cfprApDiagSrvCtrlImgLoc,
       "cfprApDiagSrvCtrlImgName": cfprApDiagSrvCtrlImgName,
       "cfprApDiagSrvCtrlOperQualifier": cfprApDiagSrvCtrlOperQualifier,
       "cfprApDiagSrvCtrlOperState": cfprApDiagSrvCtrlOperState,
       "cfprApDiagSrvCtrlRunPolicyName": cfprApDiagSrvCtrlRunPolicyName,
       "cfprApDiagSrvCtrlStartTs": cfprApDiagSrvCtrlStartTs,
       "cfprApDiagSrvCtrlStartTsM": cfprApDiagSrvCtrlStartTsM,
       "cfprApDiagSrvCtrlType": cfprApDiagSrvCtrlType}
)
