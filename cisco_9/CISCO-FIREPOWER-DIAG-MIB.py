# SNMP MIB module (CISCO-FIREPOWER-DIAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-DIAG-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:24:10 2025
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

(CfprDiagAdminState,
 CfprDiagBladeTestType,
 CfprDiagFailureAction,
 CfprDiagNetworkTestType,
 CfprDiagSrvCtrlType,
 CfprDiagStatus,
 CfprDiagStatusIssues,
 CfprDiagSuccessAction,
 CfprDiagTestOrder,
 CfprNetworkSwitchId,
 CfprPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprDiagAdminState",
    "CfprDiagBladeTestType",
    "CfprDiagFailureAction",
    "CfprDiagNetworkTestType",
    "CfprDiagSrvCtrlType",
    "CfprDiagStatus",
    "CfprDiagStatusIssues",
    "CfprDiagSuccessAction",
    "CfprDiagTestOrder",
    "CfprNetworkSwitchId",
    "CfprPolicyPolicyOwner")

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

cfprDiagObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprDiagBladeTestTable_Object = MibTable
cfprDiagBladeTestTable = _CfprDiagBladeTestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 1)
)
if mibBuilder.loadTexts:
    cfprDiagBladeTestTable.setStatus("current")
_CfprDiagBladeTestEntry_Object = MibTableRow
cfprDiagBladeTestEntry = _CfprDiagBladeTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 1, 1)
)
cfprDiagBladeTestEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-DIAG-MIB", "cfprDiagBladeTestInstanceId"),
)
if mibBuilder.loadTexts:
    cfprDiagBladeTestEntry.setStatus("current")
_CfprDiagBladeTestInstanceId_Type = CfprManagedObjectId
_CfprDiagBladeTestInstanceId_Object = MibTableColumn
cfprDiagBladeTestInstanceId = _CfprDiagBladeTestInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 1, 1, 1),
    _CfprDiagBladeTestInstanceId_Type()
)
cfprDiagBladeTestInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprDiagBladeTestInstanceId.setStatus("current")
_CfprDiagBladeTestDn_Type = CfprManagedObjectDn
_CfprDiagBladeTestDn_Object = MibTableColumn
cfprDiagBladeTestDn = _CfprDiagBladeTestDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 1, 1, 2),
    _CfprDiagBladeTestDn_Type()
)
cfprDiagBladeTestDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagBladeTestDn.setStatus("current")
_CfprDiagBladeTestRn_Type = SnmpAdminString
_CfprDiagBladeTestRn_Object = MibTableColumn
cfprDiagBladeTestRn = _CfprDiagBladeTestRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 1, 1, 3),
    _CfprDiagBladeTestRn_Type()
)
cfprDiagBladeTestRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagBladeTestRn.setStatus("current")
_CfprDiagBladeTestLength_Type = Gauge32
_CfprDiagBladeTestLength_Object = MibTableColumn
cfprDiagBladeTestLength = _CfprDiagBladeTestLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 1, 1, 4),
    _CfprDiagBladeTestLength_Type()
)
cfprDiagBladeTestLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagBladeTestLength.setStatus("current")
_CfprDiagBladeTestOrder_Type = CfprDiagTestOrder
_CfprDiagBladeTestOrder_Object = MibTableColumn
cfprDiagBladeTestOrder = _CfprDiagBladeTestOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 1, 1, 5),
    _CfprDiagBladeTestOrder_Type()
)
cfprDiagBladeTestOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagBladeTestOrder.setStatus("current")
_CfprDiagBladeTestType_Type = CfprDiagBladeTestType
_CfprDiagBladeTestType_Object = MibTableColumn
cfprDiagBladeTestType = _CfprDiagBladeTestType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 1, 1, 6),
    _CfprDiagBladeTestType_Type()
)
cfprDiagBladeTestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagBladeTestType.setStatus("current")
_CfprDiagNetworkTestTable_Object = MibTable
cfprDiagNetworkTestTable = _CfprDiagNetworkTestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 2)
)
if mibBuilder.loadTexts:
    cfprDiagNetworkTestTable.setStatus("current")
_CfprDiagNetworkTestEntry_Object = MibTableRow
cfprDiagNetworkTestEntry = _CfprDiagNetworkTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 2, 1)
)
cfprDiagNetworkTestEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-DIAG-MIB", "cfprDiagNetworkTestInstanceId"),
)
if mibBuilder.loadTexts:
    cfprDiagNetworkTestEntry.setStatus("current")
_CfprDiagNetworkTestInstanceId_Type = CfprManagedObjectId
_CfprDiagNetworkTestInstanceId_Object = MibTableColumn
cfprDiagNetworkTestInstanceId = _CfprDiagNetworkTestInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 2, 1, 1),
    _CfprDiagNetworkTestInstanceId_Type()
)
cfprDiagNetworkTestInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprDiagNetworkTestInstanceId.setStatus("current")
_CfprDiagNetworkTestDn_Type = CfprManagedObjectDn
_CfprDiagNetworkTestDn_Object = MibTableColumn
cfprDiagNetworkTestDn = _CfprDiagNetworkTestDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 2, 1, 2),
    _CfprDiagNetworkTestDn_Type()
)
cfprDiagNetworkTestDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagNetworkTestDn.setStatus("current")
_CfprDiagNetworkTestRn_Type = SnmpAdminString
_CfprDiagNetworkTestRn_Object = MibTableColumn
cfprDiagNetworkTestRn = _CfprDiagNetworkTestRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 2, 1, 3),
    _CfprDiagNetworkTestRn_Type()
)
cfprDiagNetworkTestRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagNetworkTestRn.setStatus("current")
_CfprDiagNetworkTestLength_Type = Gauge32
_CfprDiagNetworkTestLength_Object = MibTableColumn
cfprDiagNetworkTestLength = _CfprDiagNetworkTestLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 2, 1, 4),
    _CfprDiagNetworkTestLength_Type()
)
cfprDiagNetworkTestLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagNetworkTestLength.setStatus("current")
_CfprDiagNetworkTestOrder_Type = CfprDiagTestOrder
_CfprDiagNetworkTestOrder_Object = MibTableColumn
cfprDiagNetworkTestOrder = _CfprDiagNetworkTestOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 2, 1, 5),
    _CfprDiagNetworkTestOrder_Type()
)
cfprDiagNetworkTestOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagNetworkTestOrder.setStatus("current")
_CfprDiagNetworkTestSwitchId_Type = CfprNetworkSwitchId
_CfprDiagNetworkTestSwitchId_Object = MibTableColumn
cfprDiagNetworkTestSwitchId = _CfprDiagNetworkTestSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 2, 1, 6),
    _CfprDiagNetworkTestSwitchId_Type()
)
cfprDiagNetworkTestSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagNetworkTestSwitchId.setStatus("current")
_CfprDiagNetworkTestType_Type = CfprDiagNetworkTestType
_CfprDiagNetworkTestType_Object = MibTableColumn
cfprDiagNetworkTestType = _CfprDiagNetworkTestType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 2, 1, 7),
    _CfprDiagNetworkTestType_Type()
)
cfprDiagNetworkTestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagNetworkTestType.setStatus("current")
_CfprDiagRsltTable_Object = MibTable
cfprDiagRsltTable = _CfprDiagRsltTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 3)
)
if mibBuilder.loadTexts:
    cfprDiagRsltTable.setStatus("current")
_CfprDiagRsltEntry_Object = MibTableRow
cfprDiagRsltEntry = _CfprDiagRsltEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 3, 1)
)
cfprDiagRsltEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-DIAG-MIB", "cfprDiagRsltInstanceId"),
)
if mibBuilder.loadTexts:
    cfprDiagRsltEntry.setStatus("current")
_CfprDiagRsltInstanceId_Type = CfprManagedObjectId
_CfprDiagRsltInstanceId_Object = MibTableColumn
cfprDiagRsltInstanceId = _CfprDiagRsltInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 3, 1, 1),
    _CfprDiagRsltInstanceId_Type()
)
cfprDiagRsltInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprDiagRsltInstanceId.setStatus("current")
_CfprDiagRsltDn_Type = CfprManagedObjectDn
_CfprDiagRsltDn_Object = MibTableColumn
cfprDiagRsltDn = _CfprDiagRsltDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 3, 1, 2),
    _CfprDiagRsltDn_Type()
)
cfprDiagRsltDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagRsltDn.setStatus("current")
_CfprDiagRsltRn_Type = SnmpAdminString
_CfprDiagRsltRn_Object = MibTableColumn
cfprDiagRsltRn = _CfprDiagRsltRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 3, 1, 3),
    _CfprDiagRsltRn_Type()
)
cfprDiagRsltRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagRsltRn.setStatus("current")
_CfprDiagRsltDescr_Type = SnmpAdminString
_CfprDiagRsltDescr_Object = MibTableColumn
cfprDiagRsltDescr = _CfprDiagRsltDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 3, 1, 4),
    _CfprDiagRsltDescr_Type()
)
cfprDiagRsltDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagRsltDescr.setStatus("current")
_CfprDiagRsltEndTs_Type = DateAndTime
_CfprDiagRsltEndTs_Object = MibTableColumn
cfprDiagRsltEndTs = _CfprDiagRsltEndTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 3, 1, 5),
    _CfprDiagRsltEndTs_Type()
)
cfprDiagRsltEndTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagRsltEndTs.setStatus("current")
_CfprDiagRsltId_Type = Gauge32
_CfprDiagRsltId_Object = MibTableColumn
cfprDiagRsltId = _CfprDiagRsltId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 3, 1, 6),
    _CfprDiagRsltId_Type()
)
cfprDiagRsltId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagRsltId.setStatus("current")
_CfprDiagRsltResult_Type = Gauge32
_CfprDiagRsltResult_Object = MibTableColumn
cfprDiagRsltResult = _CfprDiagRsltResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 3, 1, 7),
    _CfprDiagRsltResult_Type()
)
cfprDiagRsltResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagRsltResult.setStatus("current")
_CfprDiagRsltRsltStatus_Type = CfprDiagStatus
_CfprDiagRsltRsltStatus_Object = MibTableColumn
cfprDiagRsltRsltStatus = _CfprDiagRsltRsltStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 3, 1, 8),
    _CfprDiagRsltRsltStatus_Type()
)
cfprDiagRsltRsltStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagRsltRsltStatus.setStatus("current")
_CfprDiagRsltStartTs_Type = DateAndTime
_CfprDiagRsltStartTs_Object = MibTableColumn
cfprDiagRsltStartTs = _CfprDiagRsltStartTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 3, 1, 9),
    _CfprDiagRsltStartTs_Type()
)
cfprDiagRsltStartTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagRsltStartTs.setStatus("current")
_CfprDiagRunPolicyTable_Object = MibTable
cfprDiagRunPolicyTable = _CfprDiagRunPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 4)
)
if mibBuilder.loadTexts:
    cfprDiagRunPolicyTable.setStatus("current")
_CfprDiagRunPolicyEntry_Object = MibTableRow
cfprDiagRunPolicyEntry = _CfprDiagRunPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 4, 1)
)
cfprDiagRunPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-DIAG-MIB", "cfprDiagRunPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprDiagRunPolicyEntry.setStatus("current")
_CfprDiagRunPolicyInstanceId_Type = CfprManagedObjectId
_CfprDiagRunPolicyInstanceId_Object = MibTableColumn
cfprDiagRunPolicyInstanceId = _CfprDiagRunPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 4, 1, 1),
    _CfprDiagRunPolicyInstanceId_Type()
)
cfprDiagRunPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprDiagRunPolicyInstanceId.setStatus("current")
_CfprDiagRunPolicyDn_Type = CfprManagedObjectDn
_CfprDiagRunPolicyDn_Object = MibTableColumn
cfprDiagRunPolicyDn = _CfprDiagRunPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 4, 1, 2),
    _CfprDiagRunPolicyDn_Type()
)
cfprDiagRunPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagRunPolicyDn.setStatus("current")
_CfprDiagRunPolicyRn_Type = SnmpAdminString
_CfprDiagRunPolicyRn_Object = MibTableColumn
cfprDiagRunPolicyRn = _CfprDiagRunPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 4, 1, 3),
    _CfprDiagRunPolicyRn_Type()
)
cfprDiagRunPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagRunPolicyRn.setStatus("current")
_CfprDiagRunPolicyDescr_Type = SnmpAdminString
_CfprDiagRunPolicyDescr_Object = MibTableColumn
cfprDiagRunPolicyDescr = _CfprDiagRunPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 4, 1, 4),
    _CfprDiagRunPolicyDescr_Type()
)
cfprDiagRunPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagRunPolicyDescr.setStatus("current")
_CfprDiagRunPolicyFailureAction_Type = CfprDiagFailureAction
_CfprDiagRunPolicyFailureAction_Object = MibTableColumn
cfprDiagRunPolicyFailureAction = _CfprDiagRunPolicyFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 4, 1, 5),
    _CfprDiagRunPolicyFailureAction_Type()
)
cfprDiagRunPolicyFailureAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagRunPolicyFailureAction.setStatus("current")
_CfprDiagRunPolicyIntId_Type = SnmpAdminString
_CfprDiagRunPolicyIntId_Object = MibTableColumn
cfprDiagRunPolicyIntId = _CfprDiagRunPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 4, 1, 6),
    _CfprDiagRunPolicyIntId_Type()
)
cfprDiagRunPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagRunPolicyIntId.setStatus("current")
_CfprDiagRunPolicyName_Type = SnmpAdminString
_CfprDiagRunPolicyName_Object = MibTableColumn
cfprDiagRunPolicyName = _CfprDiagRunPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 4, 1, 7),
    _CfprDiagRunPolicyName_Type()
)
cfprDiagRunPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagRunPolicyName.setStatus("current")
_CfprDiagRunPolicyPolicyLevel_Type = Gauge32
_CfprDiagRunPolicyPolicyLevel_Object = MibTableColumn
cfprDiagRunPolicyPolicyLevel = _CfprDiagRunPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 4, 1, 8),
    _CfprDiagRunPolicyPolicyLevel_Type()
)
cfprDiagRunPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagRunPolicyPolicyLevel.setStatus("current")
_CfprDiagRunPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprDiagRunPolicyPolicyOwner_Object = MibTableColumn
cfprDiagRunPolicyPolicyOwner = _CfprDiagRunPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 4, 1, 9),
    _CfprDiagRunPolicyPolicyOwner_Type()
)
cfprDiagRunPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagRunPolicyPolicyOwner.setStatus("current")
_CfprDiagRunPolicySuccessAction_Type = CfprDiagSuccessAction
_CfprDiagRunPolicySuccessAction_Object = MibTableColumn
cfprDiagRunPolicySuccessAction = _CfprDiagRunPolicySuccessAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 4, 1, 10),
    _CfprDiagRunPolicySuccessAction_Type()
)
cfprDiagRunPolicySuccessAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagRunPolicySuccessAction.setStatus("current")
_CfprDiagSrvCapProviderTable_Object = MibTable
cfprDiagSrvCapProviderTable = _CfprDiagSrvCapProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 5)
)
if mibBuilder.loadTexts:
    cfprDiagSrvCapProviderTable.setStatus("current")
_CfprDiagSrvCapProviderEntry_Object = MibTableRow
cfprDiagSrvCapProviderEntry = _CfprDiagSrvCapProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 5, 1)
)
cfprDiagSrvCapProviderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-DIAG-MIB", "cfprDiagSrvCapProviderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprDiagSrvCapProviderEntry.setStatus("current")
_CfprDiagSrvCapProviderInstanceId_Type = CfprManagedObjectId
_CfprDiagSrvCapProviderInstanceId_Object = MibTableColumn
cfprDiagSrvCapProviderInstanceId = _CfprDiagSrvCapProviderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 5, 1, 1),
    _CfprDiagSrvCapProviderInstanceId_Type()
)
cfprDiagSrvCapProviderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprDiagSrvCapProviderInstanceId.setStatus("current")
_CfprDiagSrvCapProviderDn_Type = CfprManagedObjectDn
_CfprDiagSrvCapProviderDn_Object = MibTableColumn
cfprDiagSrvCapProviderDn = _CfprDiagSrvCapProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 5, 1, 2),
    _CfprDiagSrvCapProviderDn_Type()
)
cfprDiagSrvCapProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagSrvCapProviderDn.setStatus("current")
_CfprDiagSrvCapProviderRn_Type = SnmpAdminString
_CfprDiagSrvCapProviderRn_Object = MibTableColumn
cfprDiagSrvCapProviderRn = _CfprDiagSrvCapProviderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 5, 1, 3),
    _CfprDiagSrvCapProviderRn_Type()
)
cfprDiagSrvCapProviderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagSrvCapProviderRn.setStatus("current")
_CfprDiagSrvCapProviderDeleted_Type = TruthValue
_CfprDiagSrvCapProviderDeleted_Object = MibTableColumn
cfprDiagSrvCapProviderDeleted = _CfprDiagSrvCapProviderDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 5, 1, 4),
    _CfprDiagSrvCapProviderDeleted_Type()
)
cfprDiagSrvCapProviderDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagSrvCapProviderDeleted.setStatus("current")
_CfprDiagSrvCapProviderDeprecated_Type = TruthValue
_CfprDiagSrvCapProviderDeprecated_Object = MibTableColumn
cfprDiagSrvCapProviderDeprecated = _CfprDiagSrvCapProviderDeprecated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 5, 1, 5),
    _CfprDiagSrvCapProviderDeprecated_Type()
)
cfprDiagSrvCapProviderDeprecated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagSrvCapProviderDeprecated.setStatus("current")
_CfprDiagSrvCapProviderElementLoadFailures_Type = Gauge32
_CfprDiagSrvCapProviderElementLoadFailures_Object = MibTableColumn
cfprDiagSrvCapProviderElementLoadFailures = _CfprDiagSrvCapProviderElementLoadFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 5, 1, 6),
    _CfprDiagSrvCapProviderElementLoadFailures_Type()
)
cfprDiagSrvCapProviderElementLoadFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagSrvCapProviderElementLoadFailures.setStatus("current")
_CfprDiagSrvCapProviderElementsLoaded_Type = Gauge32
_CfprDiagSrvCapProviderElementsLoaded_Object = MibTableColumn
cfprDiagSrvCapProviderElementsLoaded = _CfprDiagSrvCapProviderElementsLoaded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 5, 1, 7),
    _CfprDiagSrvCapProviderElementsLoaded_Type()
)
cfprDiagSrvCapProviderElementsLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagSrvCapProviderElementsLoaded.setStatus("current")
_CfprDiagSrvCapProviderGencount_Type = Gauge32
_CfprDiagSrvCapProviderGencount_Object = MibTableColumn
cfprDiagSrvCapProviderGencount = _CfprDiagSrvCapProviderGencount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 5, 1, 8),
    _CfprDiagSrvCapProviderGencount_Type()
)
cfprDiagSrvCapProviderGencount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagSrvCapProviderGencount.setStatus("current")
_CfprDiagSrvCapProviderLoadErrors_Type = Gauge32
_CfprDiagSrvCapProviderLoadErrors_Object = MibTableColumn
cfprDiagSrvCapProviderLoadErrors = _CfprDiagSrvCapProviderLoadErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 5, 1, 9),
    _CfprDiagSrvCapProviderLoadErrors_Type()
)
cfprDiagSrvCapProviderLoadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagSrvCapProviderLoadErrors.setStatus("current")
_CfprDiagSrvCapProviderLoadWarnings_Type = Gauge32
_CfprDiagSrvCapProviderLoadWarnings_Object = MibTableColumn
cfprDiagSrvCapProviderLoadWarnings = _CfprDiagSrvCapProviderLoadWarnings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 5, 1, 10),
    _CfprDiagSrvCapProviderLoadWarnings_Type()
)
cfprDiagSrvCapProviderLoadWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagSrvCapProviderLoadWarnings.setStatus("current")
_CfprDiagSrvCapProviderMgmtPlaneVer_Type = SnmpAdminString
_CfprDiagSrvCapProviderMgmtPlaneVer_Object = MibTableColumn
cfprDiagSrvCapProviderMgmtPlaneVer = _CfprDiagSrvCapProviderMgmtPlaneVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 5, 1, 11),
    _CfprDiagSrvCapProviderMgmtPlaneVer_Type()
)
cfprDiagSrvCapProviderMgmtPlaneVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagSrvCapProviderMgmtPlaneVer.setStatus("current")
_CfprDiagSrvCapProviderModel_Type = SnmpAdminString
_CfprDiagSrvCapProviderModel_Object = MibTableColumn
cfprDiagSrvCapProviderModel = _CfprDiagSrvCapProviderModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 5, 1, 12),
    _CfprDiagSrvCapProviderModel_Type()
)
cfprDiagSrvCapProviderModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagSrvCapProviderModel.setStatus("current")
_CfprDiagSrvCapProviderPromCardType_Type = Gauge32
_CfprDiagSrvCapProviderPromCardType_Object = MibTableColumn
cfprDiagSrvCapProviderPromCardType = _CfprDiagSrvCapProviderPromCardType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 5, 1, 13),
    _CfprDiagSrvCapProviderPromCardType_Type()
)
cfprDiagSrvCapProviderPromCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagSrvCapProviderPromCardType.setStatus("current")
_CfprDiagSrvCapProviderRevision_Type = SnmpAdminString
_CfprDiagSrvCapProviderRevision_Object = MibTableColumn
cfprDiagSrvCapProviderRevision = _CfprDiagSrvCapProviderRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 5, 1, 14),
    _CfprDiagSrvCapProviderRevision_Type()
)
cfprDiagSrvCapProviderRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagSrvCapProviderRevision.setStatus("current")
_CfprDiagSrvCapProviderVendor_Type = SnmpAdminString
_CfprDiagSrvCapProviderVendor_Object = MibTableColumn
cfprDiagSrvCapProviderVendor = _CfprDiagSrvCapProviderVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 5, 1, 15),
    _CfprDiagSrvCapProviderVendor_Type()
)
cfprDiagSrvCapProviderVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagSrvCapProviderVendor.setStatus("current")
_CfprDiagSrvCtrlTable_Object = MibTable
cfprDiagSrvCtrlTable = _CfprDiagSrvCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 6)
)
if mibBuilder.loadTexts:
    cfprDiagSrvCtrlTable.setStatus("current")
_CfprDiagSrvCtrlEntry_Object = MibTableRow
cfprDiagSrvCtrlEntry = _CfprDiagSrvCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 6, 1)
)
cfprDiagSrvCtrlEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-DIAG-MIB", "cfprDiagSrvCtrlInstanceId"),
)
if mibBuilder.loadTexts:
    cfprDiagSrvCtrlEntry.setStatus("current")
_CfprDiagSrvCtrlInstanceId_Type = CfprManagedObjectId
_CfprDiagSrvCtrlInstanceId_Object = MibTableColumn
cfprDiagSrvCtrlInstanceId = _CfprDiagSrvCtrlInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 6, 1, 1),
    _CfprDiagSrvCtrlInstanceId_Type()
)
cfprDiagSrvCtrlInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprDiagSrvCtrlInstanceId.setStatus("current")
_CfprDiagSrvCtrlDn_Type = CfprManagedObjectDn
_CfprDiagSrvCtrlDn_Object = MibTableColumn
cfprDiagSrvCtrlDn = _CfprDiagSrvCtrlDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 6, 1, 2),
    _CfprDiagSrvCtrlDn_Type()
)
cfprDiagSrvCtrlDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagSrvCtrlDn.setStatus("current")
_CfprDiagSrvCtrlRn_Type = SnmpAdminString
_CfprDiagSrvCtrlRn_Object = MibTableColumn
cfprDiagSrvCtrlRn = _CfprDiagSrvCtrlRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 6, 1, 3),
    _CfprDiagSrvCtrlRn_Type()
)
cfprDiagSrvCtrlRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagSrvCtrlRn.setStatus("current")
_CfprDiagSrvCtrlAdminState_Type = CfprDiagAdminState
_CfprDiagSrvCtrlAdminState_Object = MibTableColumn
cfprDiagSrvCtrlAdminState = _CfprDiagSrvCtrlAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 6, 1, 4),
    _CfprDiagSrvCtrlAdminState_Type()
)
cfprDiagSrvCtrlAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagSrvCtrlAdminState.setStatus("current")
_CfprDiagSrvCtrlEndTs_Type = DateAndTime
_CfprDiagSrvCtrlEndTs_Object = MibTableColumn
cfprDiagSrvCtrlEndTs = _CfprDiagSrvCtrlEndTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 6, 1, 5),
    _CfprDiagSrvCtrlEndTs_Type()
)
cfprDiagSrvCtrlEndTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagSrvCtrlEndTs.setStatus("current")
_CfprDiagSrvCtrlEndTsM_Type = Unsigned64
_CfprDiagSrvCtrlEndTsM_Object = MibTableColumn
cfprDiagSrvCtrlEndTsM = _CfprDiagSrvCtrlEndTsM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 6, 1, 6),
    _CfprDiagSrvCtrlEndTsM_Type()
)
cfprDiagSrvCtrlEndTsM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagSrvCtrlEndTsM.setStatus("current")
_CfprDiagSrvCtrlErrorDescr_Type = SnmpAdminString
_CfprDiagSrvCtrlErrorDescr_Object = MibTableColumn
cfprDiagSrvCtrlErrorDescr = _CfprDiagSrvCtrlErrorDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 6, 1, 7),
    _CfprDiagSrvCtrlErrorDescr_Type()
)
cfprDiagSrvCtrlErrorDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagSrvCtrlErrorDescr.setStatus("current")
_CfprDiagSrvCtrlImgLoc_Type = SnmpAdminString
_CfprDiagSrvCtrlImgLoc_Object = MibTableColumn
cfprDiagSrvCtrlImgLoc = _CfprDiagSrvCtrlImgLoc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 6, 1, 8),
    _CfprDiagSrvCtrlImgLoc_Type()
)
cfprDiagSrvCtrlImgLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagSrvCtrlImgLoc.setStatus("current")
_CfprDiagSrvCtrlImgName_Type = SnmpAdminString
_CfprDiagSrvCtrlImgName_Object = MibTableColumn
cfprDiagSrvCtrlImgName = _CfprDiagSrvCtrlImgName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 6, 1, 9),
    _CfprDiagSrvCtrlImgName_Type()
)
cfprDiagSrvCtrlImgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagSrvCtrlImgName.setStatus("current")
_CfprDiagSrvCtrlOperQualifier_Type = CfprDiagStatusIssues
_CfprDiagSrvCtrlOperQualifier_Object = MibTableColumn
cfprDiagSrvCtrlOperQualifier = _CfprDiagSrvCtrlOperQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 6, 1, 10),
    _CfprDiagSrvCtrlOperQualifier_Type()
)
cfprDiagSrvCtrlOperQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagSrvCtrlOperQualifier.setStatus("current")
_CfprDiagSrvCtrlOperState_Type = CfprDiagStatus
_CfprDiagSrvCtrlOperState_Object = MibTableColumn
cfprDiagSrvCtrlOperState = _CfprDiagSrvCtrlOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 6, 1, 11),
    _CfprDiagSrvCtrlOperState_Type()
)
cfprDiagSrvCtrlOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagSrvCtrlOperState.setStatus("current")
_CfprDiagSrvCtrlRunPolicyName_Type = SnmpAdminString
_CfprDiagSrvCtrlRunPolicyName_Object = MibTableColumn
cfprDiagSrvCtrlRunPolicyName = _CfprDiagSrvCtrlRunPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 6, 1, 12),
    _CfprDiagSrvCtrlRunPolicyName_Type()
)
cfprDiagSrvCtrlRunPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagSrvCtrlRunPolicyName.setStatus("current")
_CfprDiagSrvCtrlStartTs_Type = DateAndTime
_CfprDiagSrvCtrlStartTs_Object = MibTableColumn
cfprDiagSrvCtrlStartTs = _CfprDiagSrvCtrlStartTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 6, 1, 13),
    _CfprDiagSrvCtrlStartTs_Type()
)
cfprDiagSrvCtrlStartTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagSrvCtrlStartTs.setStatus("current")
_CfprDiagSrvCtrlStartTsM_Type = Unsigned64
_CfprDiagSrvCtrlStartTsM_Object = MibTableColumn
cfprDiagSrvCtrlStartTsM = _CfprDiagSrvCtrlStartTsM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 6, 1, 14),
    _CfprDiagSrvCtrlStartTsM_Type()
)
cfprDiagSrvCtrlStartTsM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagSrvCtrlStartTsM.setStatus("current")
_CfprDiagSrvCtrlType_Type = CfprDiagSrvCtrlType
_CfprDiagSrvCtrlType_Object = MibTableColumn
cfprDiagSrvCtrlType = _CfprDiagSrvCtrlType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 16, 6, 1, 15),
    _CfprDiagSrvCtrlType_Type()
)
cfprDiagSrvCtrlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDiagSrvCtrlType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-DIAG-MIB",
    **{"cfprDiagObjects": cfprDiagObjects,
       "cfprDiagBladeTestTable": cfprDiagBladeTestTable,
       "cfprDiagBladeTestEntry": cfprDiagBladeTestEntry,
       "cfprDiagBladeTestInstanceId": cfprDiagBladeTestInstanceId,
       "cfprDiagBladeTestDn": cfprDiagBladeTestDn,
       "cfprDiagBladeTestRn": cfprDiagBladeTestRn,
       "cfprDiagBladeTestLength": cfprDiagBladeTestLength,
       "cfprDiagBladeTestOrder": cfprDiagBladeTestOrder,
       "cfprDiagBladeTestType": cfprDiagBladeTestType,
       "cfprDiagNetworkTestTable": cfprDiagNetworkTestTable,
       "cfprDiagNetworkTestEntry": cfprDiagNetworkTestEntry,
       "cfprDiagNetworkTestInstanceId": cfprDiagNetworkTestInstanceId,
       "cfprDiagNetworkTestDn": cfprDiagNetworkTestDn,
       "cfprDiagNetworkTestRn": cfprDiagNetworkTestRn,
       "cfprDiagNetworkTestLength": cfprDiagNetworkTestLength,
       "cfprDiagNetworkTestOrder": cfprDiagNetworkTestOrder,
       "cfprDiagNetworkTestSwitchId": cfprDiagNetworkTestSwitchId,
       "cfprDiagNetworkTestType": cfprDiagNetworkTestType,
       "cfprDiagRsltTable": cfprDiagRsltTable,
       "cfprDiagRsltEntry": cfprDiagRsltEntry,
       "cfprDiagRsltInstanceId": cfprDiagRsltInstanceId,
       "cfprDiagRsltDn": cfprDiagRsltDn,
       "cfprDiagRsltRn": cfprDiagRsltRn,
       "cfprDiagRsltDescr": cfprDiagRsltDescr,
       "cfprDiagRsltEndTs": cfprDiagRsltEndTs,
       "cfprDiagRsltId": cfprDiagRsltId,
       "cfprDiagRsltResult": cfprDiagRsltResult,
       "cfprDiagRsltRsltStatus": cfprDiagRsltRsltStatus,
       "cfprDiagRsltStartTs": cfprDiagRsltStartTs,
       "cfprDiagRunPolicyTable": cfprDiagRunPolicyTable,
       "cfprDiagRunPolicyEntry": cfprDiagRunPolicyEntry,
       "cfprDiagRunPolicyInstanceId": cfprDiagRunPolicyInstanceId,
       "cfprDiagRunPolicyDn": cfprDiagRunPolicyDn,
       "cfprDiagRunPolicyRn": cfprDiagRunPolicyRn,
       "cfprDiagRunPolicyDescr": cfprDiagRunPolicyDescr,
       "cfprDiagRunPolicyFailureAction": cfprDiagRunPolicyFailureAction,
       "cfprDiagRunPolicyIntId": cfprDiagRunPolicyIntId,
       "cfprDiagRunPolicyName": cfprDiagRunPolicyName,
       "cfprDiagRunPolicyPolicyLevel": cfprDiagRunPolicyPolicyLevel,
       "cfprDiagRunPolicyPolicyOwner": cfprDiagRunPolicyPolicyOwner,
       "cfprDiagRunPolicySuccessAction": cfprDiagRunPolicySuccessAction,
       "cfprDiagSrvCapProviderTable": cfprDiagSrvCapProviderTable,
       "cfprDiagSrvCapProviderEntry": cfprDiagSrvCapProviderEntry,
       "cfprDiagSrvCapProviderInstanceId": cfprDiagSrvCapProviderInstanceId,
       "cfprDiagSrvCapProviderDn": cfprDiagSrvCapProviderDn,
       "cfprDiagSrvCapProviderRn": cfprDiagSrvCapProviderRn,
       "cfprDiagSrvCapProviderDeleted": cfprDiagSrvCapProviderDeleted,
       "cfprDiagSrvCapProviderDeprecated": cfprDiagSrvCapProviderDeprecated,
       "cfprDiagSrvCapProviderElementLoadFailures": cfprDiagSrvCapProviderElementLoadFailures,
       "cfprDiagSrvCapProviderElementsLoaded": cfprDiagSrvCapProviderElementsLoaded,
       "cfprDiagSrvCapProviderGencount": cfprDiagSrvCapProviderGencount,
       "cfprDiagSrvCapProviderLoadErrors": cfprDiagSrvCapProviderLoadErrors,
       "cfprDiagSrvCapProviderLoadWarnings": cfprDiagSrvCapProviderLoadWarnings,
       "cfprDiagSrvCapProviderMgmtPlaneVer": cfprDiagSrvCapProviderMgmtPlaneVer,
       "cfprDiagSrvCapProviderModel": cfprDiagSrvCapProviderModel,
       "cfprDiagSrvCapProviderPromCardType": cfprDiagSrvCapProviderPromCardType,
       "cfprDiagSrvCapProviderRevision": cfprDiagSrvCapProviderRevision,
       "cfprDiagSrvCapProviderVendor": cfprDiagSrvCapProviderVendor,
       "cfprDiagSrvCtrlTable": cfprDiagSrvCtrlTable,
       "cfprDiagSrvCtrlEntry": cfprDiagSrvCtrlEntry,
       "cfprDiagSrvCtrlInstanceId": cfprDiagSrvCtrlInstanceId,
       "cfprDiagSrvCtrlDn": cfprDiagSrvCtrlDn,
       "cfprDiagSrvCtrlRn": cfprDiagSrvCtrlRn,
       "cfprDiagSrvCtrlAdminState": cfprDiagSrvCtrlAdminState,
       "cfprDiagSrvCtrlEndTs": cfprDiagSrvCtrlEndTs,
       "cfprDiagSrvCtrlEndTsM": cfprDiagSrvCtrlEndTsM,
       "cfprDiagSrvCtrlErrorDescr": cfprDiagSrvCtrlErrorDescr,
       "cfprDiagSrvCtrlImgLoc": cfprDiagSrvCtrlImgLoc,
       "cfprDiagSrvCtrlImgName": cfprDiagSrvCtrlImgName,
       "cfprDiagSrvCtrlOperQualifier": cfprDiagSrvCtrlOperQualifier,
       "cfprDiagSrvCtrlOperState": cfprDiagSrvCtrlOperState,
       "cfprDiagSrvCtrlRunPolicyName": cfprDiagSrvCtrlRunPolicyName,
       "cfprDiagSrvCtrlStartTs": cfprDiagSrvCtrlStartTs,
       "cfprDiagSrvCtrlStartTsM": cfprDiagSrvCtrlStartTsM,
       "cfprDiagSrvCtrlType": cfprDiagSrvCtrlType}
)
