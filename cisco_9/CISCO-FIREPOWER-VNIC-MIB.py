# SNMP MIB module (CISCO-FIREPOWER-VNIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-VNIC-MIB.mib
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

(CfprConditionRemoteInvRslt,
 CfprDpsecForgedTransmit,
 CfprFabricHostPortId,
 CfprFabricSSAPortType,
 CfprFabricVlanSharingType,
 CfprFsmCompletion,
 CfprFsmFlags,
 CfprFsmFsmStageStatus,
 CfprLsConfigState,
 CfprNetworkSwitchId,
 CfprNwctrlAdminState,
 CfprNwctrlLinkFailAction,
 CfprNwctrlRegistrationMode,
 CfprPolicyPolicyOwner,
 CfprVmMgmtPlane,
 CfprVnicAEtherIfType,
 CfprVnicAFcIfType,
 CfprVnicAIpcIfType,
 CfprVnicAScsiIfType,
 CfprVnicAppRole,
 CfprVnicConfigIssues,
 CfprVnicConnectionOwner,
 CfprVnicConnectionType,
 CfprVnicDefBehType,
 CfprVnicDefaultAction,
 CfprVnicDynamicConReqProtection,
 CfprVnicEtherBaseSwitchId,
 CfprVnicEtherType,
 CfprVnicExternalMgmtIPMode,
 CfprVnicFcBasePersBind,
 CfprVnicFcBaseType,
 CfprVnicFcNodeOwner,
 CfprVnicHostNwIOPerfPref,
 CfprVnicIPv4DnsPref,
 CfprVnicIScsiIfDefType,
 CfprVnicIScsiNodeOwner,
 CfprVnicIfOperState,
 CfprVnicInstantiation,
 CfprVnicIpcType,
 CfprVnicL2IfSwitchId,
 CfprVnicLanConnTemplSwitchId,
 CfprVnicLunId,
 CfprVnicPortProfileType,
 CfprVnicProfileConfigQualifier,
 CfprVnicProfileSetFsmCurrentFsm,
 CfprVnicProfileSetFsmStageName,
 CfprVnicProfileSetFsmTaskItem,
 CfprVnicSanConnTemplTarget,
 CfprVnicScsiType,
 CfprVnicTemplateTarget,
 CfprVnicTemplateType,
 CfprVnicVhbaBehPolicyType,
 CfprVnicVirtualizationPreferenceType,
 CfprVnicVnicBehPolicyType,
 CfprVnicVnicBootDev,
 CfprVnicVnicOperHostPort) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprConditionRemoteInvRslt",
    "CfprDpsecForgedTransmit",
    "CfprFabricHostPortId",
    "CfprFabricSSAPortType",
    "CfprFabricVlanSharingType",
    "CfprFsmCompletion",
    "CfprFsmFlags",
    "CfprFsmFsmStageStatus",
    "CfprLsConfigState",
    "CfprNetworkSwitchId",
    "CfprNwctrlAdminState",
    "CfprNwctrlLinkFailAction",
    "CfprNwctrlRegistrationMode",
    "CfprPolicyPolicyOwner",
    "CfprVmMgmtPlane",
    "CfprVnicAEtherIfType",
    "CfprVnicAFcIfType",
    "CfprVnicAIpcIfType",
    "CfprVnicAScsiIfType",
    "CfprVnicAppRole",
    "CfprVnicConfigIssues",
    "CfprVnicConnectionOwner",
    "CfprVnicConnectionType",
    "CfprVnicDefBehType",
    "CfprVnicDefaultAction",
    "CfprVnicDynamicConReqProtection",
    "CfprVnicEtherBaseSwitchId",
    "CfprVnicEtherType",
    "CfprVnicExternalMgmtIPMode",
    "CfprVnicFcBasePersBind",
    "CfprVnicFcBaseType",
    "CfprVnicFcNodeOwner",
    "CfprVnicHostNwIOPerfPref",
    "CfprVnicIPv4DnsPref",
    "CfprVnicIScsiIfDefType",
    "CfprVnicIScsiNodeOwner",
    "CfprVnicIfOperState",
    "CfprVnicInstantiation",
    "CfprVnicIpcType",
    "CfprVnicL2IfSwitchId",
    "CfprVnicLanConnTemplSwitchId",
    "CfprVnicLunId",
    "CfprVnicPortProfileType",
    "CfprVnicProfileConfigQualifier",
    "CfprVnicProfileSetFsmCurrentFsm",
    "CfprVnicProfileSetFsmStageName",
    "CfprVnicProfileSetFsmTaskItem",
    "CfprVnicSanConnTemplTarget",
    "CfprVnicScsiType",
    "CfprVnicTemplateTarget",
    "CfprVnicTemplateType",
    "CfprVnicVhbaBehPolicyType",
    "CfprVnicVirtualizationPreferenceType",
    "CfprVnicVnicBehPolicyType",
    "CfprVnicVnicBootDev",
    "CfprVnicVnicOperHostPort")

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

cfprVnicObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprVnicBootIpPolicyTable_Object = MibTable
cfprVnicBootIpPolicyTable = _CfprVnicBootIpPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 1)
)
if mibBuilder.loadTexts:
    cfprVnicBootIpPolicyTable.setStatus("current")
_CfprVnicBootIpPolicyEntry_Object = MibTableRow
cfprVnicBootIpPolicyEntry = _CfprVnicBootIpPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 1, 1)
)
cfprVnicBootIpPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicBootIpPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicBootIpPolicyEntry.setStatus("current")
_CfprVnicBootIpPolicyInstanceId_Type = CfprManagedObjectId
_CfprVnicBootIpPolicyInstanceId_Object = MibTableColumn
cfprVnicBootIpPolicyInstanceId = _CfprVnicBootIpPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 1, 1, 1),
    _CfprVnicBootIpPolicyInstanceId_Type()
)
cfprVnicBootIpPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicBootIpPolicyInstanceId.setStatus("current")
_CfprVnicBootIpPolicyDn_Type = CfprManagedObjectDn
_CfprVnicBootIpPolicyDn_Object = MibTableColumn
cfprVnicBootIpPolicyDn = _CfprVnicBootIpPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 1, 1, 2),
    _CfprVnicBootIpPolicyDn_Type()
)
cfprVnicBootIpPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicBootIpPolicyDn.setStatus("current")
_CfprVnicBootIpPolicyRn_Type = SnmpAdminString
_CfprVnicBootIpPolicyRn_Object = MibTableColumn
cfprVnicBootIpPolicyRn = _CfprVnicBootIpPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 1, 1, 3),
    _CfprVnicBootIpPolicyRn_Type()
)
cfprVnicBootIpPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicBootIpPolicyRn.setStatus("current")
_CfprVnicBootIpPolicyDescr_Type = SnmpAdminString
_CfprVnicBootIpPolicyDescr_Object = MibTableColumn
cfprVnicBootIpPolicyDescr = _CfprVnicBootIpPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 1, 1, 4),
    _CfprVnicBootIpPolicyDescr_Type()
)
cfprVnicBootIpPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicBootIpPolicyDescr.setStatus("current")
_CfprVnicBootIpPolicyIntId_Type = SnmpAdminString
_CfprVnicBootIpPolicyIntId_Object = MibTableColumn
cfprVnicBootIpPolicyIntId = _CfprVnicBootIpPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 1, 1, 5),
    _CfprVnicBootIpPolicyIntId_Type()
)
cfprVnicBootIpPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicBootIpPolicyIntId.setStatus("current")
_CfprVnicBootIpPolicyName_Type = SnmpAdminString
_CfprVnicBootIpPolicyName_Object = MibTableColumn
cfprVnicBootIpPolicyName = _CfprVnicBootIpPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 1, 1, 6),
    _CfprVnicBootIpPolicyName_Type()
)
cfprVnicBootIpPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicBootIpPolicyName.setStatus("current")
_CfprVnicBootIpPolicyPolicyLevel_Type = Gauge32
_CfprVnicBootIpPolicyPolicyLevel_Object = MibTableColumn
cfprVnicBootIpPolicyPolicyLevel = _CfprVnicBootIpPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 1, 1, 7),
    _CfprVnicBootIpPolicyPolicyLevel_Type()
)
cfprVnicBootIpPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicBootIpPolicyPolicyLevel.setStatus("current")
_CfprVnicBootIpPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprVnicBootIpPolicyPolicyOwner_Object = MibTableColumn
cfprVnicBootIpPolicyPolicyOwner = _CfprVnicBootIpPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 1, 1, 8),
    _CfprVnicBootIpPolicyPolicyOwner_Type()
)
cfprVnicBootIpPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicBootIpPolicyPolicyOwner.setStatus("current")
_CfprVnicBootIpPolicyPoolName_Type = SnmpAdminString
_CfprVnicBootIpPolicyPoolName_Object = MibTableColumn
cfprVnicBootIpPolicyPoolName = _CfprVnicBootIpPolicyPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 1, 1, 9),
    _CfprVnicBootIpPolicyPoolName_Type()
)
cfprVnicBootIpPolicyPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicBootIpPolicyPoolName.setStatus("current")
_CfprVnicBootTargetTable_Object = MibTable
cfprVnicBootTargetTable = _CfprVnicBootTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 2)
)
if mibBuilder.loadTexts:
    cfprVnicBootTargetTable.setStatus("current")
_CfprVnicBootTargetEntry_Object = MibTableRow
cfprVnicBootTargetEntry = _CfprVnicBootTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 2, 1)
)
cfprVnicBootTargetEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicBootTargetInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicBootTargetEntry.setStatus("current")
_CfprVnicBootTargetInstanceId_Type = CfprManagedObjectId
_CfprVnicBootTargetInstanceId_Object = MibTableColumn
cfprVnicBootTargetInstanceId = _CfprVnicBootTargetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 2, 1, 1),
    _CfprVnicBootTargetInstanceId_Type()
)
cfprVnicBootTargetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicBootTargetInstanceId.setStatus("current")
_CfprVnicBootTargetDn_Type = CfprManagedObjectDn
_CfprVnicBootTargetDn_Object = MibTableColumn
cfprVnicBootTargetDn = _CfprVnicBootTargetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 2, 1, 2),
    _CfprVnicBootTargetDn_Type()
)
cfprVnicBootTargetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicBootTargetDn.setStatus("current")
_CfprVnicBootTargetRn_Type = SnmpAdminString
_CfprVnicBootTargetRn_Object = MibTableColumn
cfprVnicBootTargetRn = _CfprVnicBootTargetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 2, 1, 3),
    _CfprVnicBootTargetRn_Type()
)
cfprVnicBootTargetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicBootTargetRn.setStatus("current")
_CfprVnicBootTargetLun_Type = SnmpAdminString
_CfprVnicBootTargetLun_Object = MibTableColumn
cfprVnicBootTargetLun = _CfprVnicBootTargetLun_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 2, 1, 4),
    _CfprVnicBootTargetLun_Type()
)
cfprVnicBootTargetLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicBootTargetLun.setStatus("current")
_CfprVnicBootTargetWwn_Type = Unsigned64
_CfprVnicBootTargetWwn_Object = MibTableColumn
cfprVnicBootTargetWwn = _CfprVnicBootTargetWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 2, 1, 5),
    _CfprVnicBootTargetWwn_Type()
)
cfprVnicBootTargetWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicBootTargetWwn.setStatus("current")
_CfprVnicConnDefTable_Object = MibTable
cfprVnicConnDefTable = _CfprVnicConnDefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 3)
)
if mibBuilder.loadTexts:
    cfprVnicConnDefTable.setStatus("current")
_CfprVnicConnDefEntry_Object = MibTableRow
cfprVnicConnDefEntry = _CfprVnicConnDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 3, 1)
)
cfprVnicConnDefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicConnDefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicConnDefEntry.setStatus("current")
_CfprVnicConnDefInstanceId_Type = CfprManagedObjectId
_CfprVnicConnDefInstanceId_Object = MibTableColumn
cfprVnicConnDefInstanceId = _CfprVnicConnDefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 3, 1, 1),
    _CfprVnicConnDefInstanceId_Type()
)
cfprVnicConnDefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicConnDefInstanceId.setStatus("current")
_CfprVnicConnDefDn_Type = CfprManagedObjectDn
_CfprVnicConnDefDn_Object = MibTableColumn
cfprVnicConnDefDn = _CfprVnicConnDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 3, 1, 2),
    _CfprVnicConnDefDn_Type()
)
cfprVnicConnDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicConnDefDn.setStatus("current")
_CfprVnicConnDefRn_Type = SnmpAdminString
_CfprVnicConnDefRn_Object = MibTableColumn
cfprVnicConnDefRn = _CfprVnicConnDefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 3, 1, 3),
    _CfprVnicConnDefRn_Type()
)
cfprVnicConnDefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicConnDefRn.setStatus("current")
_CfprVnicConnDefFltAggr_Type = Unsigned64
_CfprVnicConnDefFltAggr_Object = MibTableColumn
cfprVnicConnDefFltAggr = _CfprVnicConnDefFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 3, 1, 4),
    _CfprVnicConnDefFltAggr_Type()
)
cfprVnicConnDefFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicConnDefFltAggr.setStatus("current")
_CfprVnicConnDefLanConnPolicyName_Type = SnmpAdminString
_CfprVnicConnDefLanConnPolicyName_Object = MibTableColumn
cfprVnicConnDefLanConnPolicyName = _CfprVnicConnDefLanConnPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 3, 1, 5),
    _CfprVnicConnDefLanConnPolicyName_Type()
)
cfprVnicConnDefLanConnPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicConnDefLanConnPolicyName.setStatus("current")
_CfprVnicConnDefOperLanConnPolicyName_Type = SnmpAdminString
_CfprVnicConnDefOperLanConnPolicyName_Object = MibTableColumn
cfprVnicConnDefOperLanConnPolicyName = _CfprVnicConnDefOperLanConnPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 3, 1, 6),
    _CfprVnicConnDefOperLanConnPolicyName_Type()
)
cfprVnicConnDefOperLanConnPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicConnDefOperLanConnPolicyName.setStatus("current")
_CfprVnicConnDefOperSanConnPolicyName_Type = SnmpAdminString
_CfprVnicConnDefOperSanConnPolicyName_Object = MibTableColumn
cfprVnicConnDefOperSanConnPolicyName = _CfprVnicConnDefOperSanConnPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 3, 1, 7),
    _CfprVnicConnDefOperSanConnPolicyName_Type()
)
cfprVnicConnDefOperSanConnPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicConnDefOperSanConnPolicyName.setStatus("current")
_CfprVnicConnDefSanConnPolicyName_Type = SnmpAdminString
_CfprVnicConnDefSanConnPolicyName_Object = MibTableColumn
cfprVnicConnDefSanConnPolicyName = _CfprVnicConnDefSanConnPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 3, 1, 8),
    _CfprVnicConnDefSanConnPolicyName_Type()
)
cfprVnicConnDefSanConnPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicConnDefSanConnPolicyName.setStatus("current")
_CfprVnicDefBehTable_Object = MibTable
cfprVnicDefBehTable = _CfprVnicDefBehTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 4)
)
if mibBuilder.loadTexts:
    cfprVnicDefBehTable.setStatus("current")
_CfprVnicDefBehEntry_Object = MibTableRow
cfprVnicDefBehEntry = _CfprVnicDefBehEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 4, 1)
)
cfprVnicDefBehEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicDefBehInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicDefBehEntry.setStatus("current")
_CfprVnicDefBehInstanceId_Type = CfprManagedObjectId
_CfprVnicDefBehInstanceId_Object = MibTableColumn
cfprVnicDefBehInstanceId = _CfprVnicDefBehInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 4, 1, 1),
    _CfprVnicDefBehInstanceId_Type()
)
cfprVnicDefBehInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicDefBehInstanceId.setStatus("current")
_CfprVnicDefBehDn_Type = CfprManagedObjectDn
_CfprVnicDefBehDn_Object = MibTableColumn
cfprVnicDefBehDn = _CfprVnicDefBehDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 4, 1, 2),
    _CfprVnicDefBehDn_Type()
)
cfprVnicDefBehDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDefBehDn.setStatus("current")
_CfprVnicDefBehRn_Type = SnmpAdminString
_CfprVnicDefBehRn_Object = MibTableColumn
cfprVnicDefBehRn = _CfprVnicDefBehRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 4, 1, 3),
    _CfprVnicDefBehRn_Type()
)
cfprVnicDefBehRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDefBehRn.setStatus("current")
_CfprVnicDefBehAction_Type = CfprVnicDefaultAction
_CfprVnicDefBehAction_Object = MibTableColumn
cfprVnicDefBehAction = _CfprVnicDefBehAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 4, 1, 4),
    _CfprVnicDefBehAction_Type()
)
cfprVnicDefBehAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDefBehAction.setStatus("current")
_CfprVnicDefBehDescr_Type = SnmpAdminString
_CfprVnicDefBehDescr_Object = MibTableColumn
cfprVnicDefBehDescr = _CfprVnicDefBehDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 4, 1, 5),
    _CfprVnicDefBehDescr_Type()
)
cfprVnicDefBehDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDefBehDescr.setStatus("current")
_CfprVnicDefBehIntId_Type = SnmpAdminString
_CfprVnicDefBehIntId_Object = MibTableColumn
cfprVnicDefBehIntId = _CfprVnicDefBehIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 4, 1, 6),
    _CfprVnicDefBehIntId_Type()
)
cfprVnicDefBehIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDefBehIntId.setStatus("current")
_CfprVnicDefBehName_Type = SnmpAdminString
_CfprVnicDefBehName_Object = MibTableColumn
cfprVnicDefBehName = _CfprVnicDefBehName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 4, 1, 7),
    _CfprVnicDefBehName_Type()
)
cfprVnicDefBehName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDefBehName.setStatus("current")
_CfprVnicDefBehNwTemplName_Type = SnmpAdminString
_CfprVnicDefBehNwTemplName_Object = MibTableColumn
cfprVnicDefBehNwTemplName = _CfprVnicDefBehNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 4, 1, 8),
    _CfprVnicDefBehNwTemplName_Type()
)
cfprVnicDefBehNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDefBehNwTemplName.setStatus("current")
_CfprVnicDefBehPolicyLevel_Type = Gauge32
_CfprVnicDefBehPolicyLevel_Object = MibTableColumn
cfprVnicDefBehPolicyLevel = _CfprVnicDefBehPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 4, 1, 9),
    _CfprVnicDefBehPolicyLevel_Type()
)
cfprVnicDefBehPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDefBehPolicyLevel.setStatus("current")
_CfprVnicDefBehPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprVnicDefBehPolicyOwner_Object = MibTableColumn
cfprVnicDefBehPolicyOwner = _CfprVnicDefBehPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 4, 1, 10),
    _CfprVnicDefBehPolicyOwner_Type()
)
cfprVnicDefBehPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDefBehPolicyOwner.setStatus("current")
_CfprVnicDefBehType_Type = CfprVnicDefBehType
_CfprVnicDefBehType_Object = MibTableColumn
cfprVnicDefBehType = _CfprVnicDefBehType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 4, 1, 11),
    _CfprVnicDefBehType_Type()
)
cfprVnicDefBehType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDefBehType.setStatus("current")
_CfprVnicDynamicConTable_Object = MibTable
cfprVnicDynamicConTable = _CfprVnicDynamicConTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 5)
)
if mibBuilder.loadTexts:
    cfprVnicDynamicConTable.setStatus("current")
_CfprVnicDynamicConEntry_Object = MibTableRow
cfprVnicDynamicConEntry = _CfprVnicDynamicConEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 5, 1)
)
cfprVnicDynamicConEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicDynamicConInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicDynamicConEntry.setStatus("current")
_CfprVnicDynamicConInstanceId_Type = CfprManagedObjectId
_CfprVnicDynamicConInstanceId_Object = MibTableColumn
cfprVnicDynamicConInstanceId = _CfprVnicDynamicConInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 5, 1, 1),
    _CfprVnicDynamicConInstanceId_Type()
)
cfprVnicDynamicConInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicDynamicConInstanceId.setStatus("current")
_CfprVnicDynamicConDn_Type = CfprManagedObjectDn
_CfprVnicDynamicConDn_Object = MibTableColumn
cfprVnicDynamicConDn = _CfprVnicDynamicConDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 5, 1, 2),
    _CfprVnicDynamicConDn_Type()
)
cfprVnicDynamicConDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicConDn.setStatus("current")
_CfprVnicDynamicConRn_Type = SnmpAdminString
_CfprVnicDynamicConRn_Object = MibTableColumn
cfprVnicDynamicConRn = _CfprVnicDynamicConRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 5, 1, 3),
    _CfprVnicDynamicConRn_Type()
)
cfprVnicDynamicConRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicConRn.setStatus("current")
_CfprVnicDynamicConAdaptorProfileName_Type = SnmpAdminString
_CfprVnicDynamicConAdaptorProfileName_Object = MibTableColumn
cfprVnicDynamicConAdaptorProfileName = _CfprVnicDynamicConAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 5, 1, 4),
    _CfprVnicDynamicConAdaptorProfileName_Type()
)
cfprVnicDynamicConAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicConAdaptorProfileName.setStatus("current")
_CfprVnicDynamicConDescr_Type = SnmpAdminString
_CfprVnicDynamicConDescr_Object = MibTableColumn
cfprVnicDynamicConDescr = _CfprVnicDynamicConDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 5, 1, 5),
    _CfprVnicDynamicConDescr_Type()
)
cfprVnicDynamicConDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicConDescr.setStatus("current")
_CfprVnicDynamicConDynamicEth_Type = Gauge32
_CfprVnicDynamicConDynamicEth_Object = MibTableColumn
cfprVnicDynamicConDynamicEth = _CfprVnicDynamicConDynamicEth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 5, 1, 6),
    _CfprVnicDynamicConDynamicEth_Type()
)
cfprVnicDynamicConDynamicEth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicConDynamicEth.setStatus("current")
_CfprVnicDynamicConIntId_Type = SnmpAdminString
_CfprVnicDynamicConIntId_Object = MibTableColumn
cfprVnicDynamicConIntId = _CfprVnicDynamicConIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 5, 1, 7),
    _CfprVnicDynamicConIntId_Type()
)
cfprVnicDynamicConIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicConIntId.setStatus("current")
_CfprVnicDynamicConMtu_Type = Gauge32
_CfprVnicDynamicConMtu_Object = MibTableColumn
cfprVnicDynamicConMtu = _CfprVnicDynamicConMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 5, 1, 8),
    _CfprVnicDynamicConMtu_Type()
)
cfprVnicDynamicConMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicConMtu.setStatus("current")
_CfprVnicDynamicConName_Type = SnmpAdminString
_CfprVnicDynamicConName_Object = MibTableColumn
cfprVnicDynamicConName = _CfprVnicDynamicConName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 5, 1, 9),
    _CfprVnicDynamicConName_Type()
)
cfprVnicDynamicConName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicConName.setStatus("current")
_CfprVnicDynamicConNamingPrefix_Type = SnmpAdminString
_CfprVnicDynamicConNamingPrefix_Object = MibTableColumn
cfprVnicDynamicConNamingPrefix = _CfprVnicDynamicConNamingPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 5, 1, 10),
    _CfprVnicDynamicConNamingPrefix_Type()
)
cfprVnicDynamicConNamingPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicConNamingPrefix.setStatus("current")
_CfprVnicDynamicConPolicyLevel_Type = Gauge32
_CfprVnicDynamicConPolicyLevel_Object = MibTableColumn
cfprVnicDynamicConPolicyLevel = _CfprVnicDynamicConPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 5, 1, 11),
    _CfprVnicDynamicConPolicyLevel_Type()
)
cfprVnicDynamicConPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicConPolicyLevel.setStatus("current")
_CfprVnicDynamicConPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprVnicDynamicConPolicyOwner_Object = MibTableColumn
cfprVnicDynamicConPolicyOwner = _CfprVnicDynamicConPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 5, 1, 12),
    _CfprVnicDynamicConPolicyOwner_Type()
)
cfprVnicDynamicConPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicConPolicyOwner.setStatus("current")
_CfprVnicDynamicConProtection_Type = CfprVnicDynamicConReqProtection
_CfprVnicDynamicConProtection_Object = MibTableColumn
cfprVnicDynamicConProtection = _CfprVnicDynamicConProtection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 5, 1, 13),
    _CfprVnicDynamicConProtection_Type()
)
cfprVnicDynamicConProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicConProtection.setStatus("current")
_CfprVnicDynamicConPolicyTable_Object = MibTable
cfprVnicDynamicConPolicyTable = _CfprVnicDynamicConPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 6)
)
if mibBuilder.loadTexts:
    cfprVnicDynamicConPolicyTable.setStatus("current")
_CfprVnicDynamicConPolicyEntry_Object = MibTableRow
cfprVnicDynamicConPolicyEntry = _CfprVnicDynamicConPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 6, 1)
)
cfprVnicDynamicConPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicDynamicConPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicDynamicConPolicyEntry.setStatus("current")
_CfprVnicDynamicConPolicyInstanceId_Type = CfprManagedObjectId
_CfprVnicDynamicConPolicyInstanceId_Object = MibTableColumn
cfprVnicDynamicConPolicyInstanceId = _CfprVnicDynamicConPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 6, 1, 1),
    _CfprVnicDynamicConPolicyInstanceId_Type()
)
cfprVnicDynamicConPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicDynamicConPolicyInstanceId.setStatus("current")
_CfprVnicDynamicConPolicyDn_Type = CfprManagedObjectDn
_CfprVnicDynamicConPolicyDn_Object = MibTableColumn
cfprVnicDynamicConPolicyDn = _CfprVnicDynamicConPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 6, 1, 2),
    _CfprVnicDynamicConPolicyDn_Type()
)
cfprVnicDynamicConPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicConPolicyDn.setStatus("current")
_CfprVnicDynamicConPolicyRn_Type = SnmpAdminString
_CfprVnicDynamicConPolicyRn_Object = MibTableColumn
cfprVnicDynamicConPolicyRn = _CfprVnicDynamicConPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 6, 1, 3),
    _CfprVnicDynamicConPolicyRn_Type()
)
cfprVnicDynamicConPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicConPolicyRn.setStatus("current")
_CfprVnicDynamicConPolicyAdaptorProfileName_Type = SnmpAdminString
_CfprVnicDynamicConPolicyAdaptorProfileName_Object = MibTableColumn
cfprVnicDynamicConPolicyAdaptorProfileName = _CfprVnicDynamicConPolicyAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 6, 1, 4),
    _CfprVnicDynamicConPolicyAdaptorProfileName_Type()
)
cfprVnicDynamicConPolicyAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicConPolicyAdaptorProfileName.setStatus("current")
_CfprVnicDynamicConPolicyDescr_Type = SnmpAdminString
_CfprVnicDynamicConPolicyDescr_Object = MibTableColumn
cfprVnicDynamicConPolicyDescr = _CfprVnicDynamicConPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 6, 1, 5),
    _CfprVnicDynamicConPolicyDescr_Type()
)
cfprVnicDynamicConPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicConPolicyDescr.setStatus("current")
_CfprVnicDynamicConPolicyDynamicEth_Type = Gauge32
_CfprVnicDynamicConPolicyDynamicEth_Object = MibTableColumn
cfprVnicDynamicConPolicyDynamicEth = _CfprVnicDynamicConPolicyDynamicEth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 6, 1, 6),
    _CfprVnicDynamicConPolicyDynamicEth_Type()
)
cfprVnicDynamicConPolicyDynamicEth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicConPolicyDynamicEth.setStatus("current")
_CfprVnicDynamicConPolicyIntId_Type = SnmpAdminString
_CfprVnicDynamicConPolicyIntId_Object = MibTableColumn
cfprVnicDynamicConPolicyIntId = _CfprVnicDynamicConPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 6, 1, 7),
    _CfprVnicDynamicConPolicyIntId_Type()
)
cfprVnicDynamicConPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicConPolicyIntId.setStatus("current")
_CfprVnicDynamicConPolicyMtu_Type = Gauge32
_CfprVnicDynamicConPolicyMtu_Object = MibTableColumn
cfprVnicDynamicConPolicyMtu = _CfprVnicDynamicConPolicyMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 6, 1, 8),
    _CfprVnicDynamicConPolicyMtu_Type()
)
cfprVnicDynamicConPolicyMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicConPolicyMtu.setStatus("current")
_CfprVnicDynamicConPolicyName_Type = SnmpAdminString
_CfprVnicDynamicConPolicyName_Object = MibTableColumn
cfprVnicDynamicConPolicyName = _CfprVnicDynamicConPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 6, 1, 9),
    _CfprVnicDynamicConPolicyName_Type()
)
cfprVnicDynamicConPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicConPolicyName.setStatus("current")
_CfprVnicDynamicConPolicyNamingPrefix_Type = SnmpAdminString
_CfprVnicDynamicConPolicyNamingPrefix_Object = MibTableColumn
cfprVnicDynamicConPolicyNamingPrefix = _CfprVnicDynamicConPolicyNamingPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 6, 1, 10),
    _CfprVnicDynamicConPolicyNamingPrefix_Type()
)
cfprVnicDynamicConPolicyNamingPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicConPolicyNamingPrefix.setStatus("current")
_CfprVnicDynamicConPolicyPolicyLevel_Type = Gauge32
_CfprVnicDynamicConPolicyPolicyLevel_Object = MibTableColumn
cfprVnicDynamicConPolicyPolicyLevel = _CfprVnicDynamicConPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 6, 1, 11),
    _CfprVnicDynamicConPolicyPolicyLevel_Type()
)
cfprVnicDynamicConPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicConPolicyPolicyLevel.setStatus("current")
_CfprVnicDynamicConPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprVnicDynamicConPolicyPolicyOwner_Object = MibTableColumn
cfprVnicDynamicConPolicyPolicyOwner = _CfprVnicDynamicConPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 6, 1, 12),
    _CfprVnicDynamicConPolicyPolicyOwner_Type()
)
cfprVnicDynamicConPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicConPolicyPolicyOwner.setStatus("current")
_CfprVnicDynamicConPolicyProtection_Type = CfprVnicDynamicConReqProtection
_CfprVnicDynamicConPolicyProtection_Object = MibTableColumn
cfprVnicDynamicConPolicyProtection = _CfprVnicDynamicConPolicyProtection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 6, 1, 13),
    _CfprVnicDynamicConPolicyProtection_Type()
)
cfprVnicDynamicConPolicyProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicConPolicyProtection.setStatus("current")
_CfprVnicDynamicConPolicyRefTable_Object = MibTable
cfprVnicDynamicConPolicyRefTable = _CfprVnicDynamicConPolicyRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 7)
)
if mibBuilder.loadTexts:
    cfprVnicDynamicConPolicyRefTable.setStatus("current")
_CfprVnicDynamicConPolicyRefEntry_Object = MibTableRow
cfprVnicDynamicConPolicyRefEntry = _CfprVnicDynamicConPolicyRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 7, 1)
)
cfprVnicDynamicConPolicyRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicDynamicConPolicyRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicDynamicConPolicyRefEntry.setStatus("current")
_CfprVnicDynamicConPolicyRefInstanceId_Type = CfprManagedObjectId
_CfprVnicDynamicConPolicyRefInstanceId_Object = MibTableColumn
cfprVnicDynamicConPolicyRefInstanceId = _CfprVnicDynamicConPolicyRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 7, 1, 1),
    _CfprVnicDynamicConPolicyRefInstanceId_Type()
)
cfprVnicDynamicConPolicyRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicDynamicConPolicyRefInstanceId.setStatus("current")
_CfprVnicDynamicConPolicyRefDn_Type = CfprManagedObjectDn
_CfprVnicDynamicConPolicyRefDn_Object = MibTableColumn
cfprVnicDynamicConPolicyRefDn = _CfprVnicDynamicConPolicyRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 7, 1, 2),
    _CfprVnicDynamicConPolicyRefDn_Type()
)
cfprVnicDynamicConPolicyRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicConPolicyRefDn.setStatus("current")
_CfprVnicDynamicConPolicyRefRn_Type = SnmpAdminString
_CfprVnicDynamicConPolicyRefRn_Object = MibTableColumn
cfprVnicDynamicConPolicyRefRn = _CfprVnicDynamicConPolicyRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 7, 1, 3),
    _CfprVnicDynamicConPolicyRefRn_Type()
)
cfprVnicDynamicConPolicyRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicConPolicyRefRn.setStatus("current")
_CfprVnicDynamicConPolicyRefConPolicyName_Type = SnmpAdminString
_CfprVnicDynamicConPolicyRefConPolicyName_Object = MibTableColumn
cfprVnicDynamicConPolicyRefConPolicyName = _CfprVnicDynamicConPolicyRefConPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 7, 1, 4),
    _CfprVnicDynamicConPolicyRefConPolicyName_Type()
)
cfprVnicDynamicConPolicyRefConPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicConPolicyRefConPolicyName.setStatus("current")
_CfprVnicDynamicConPolicyRefOperConPolicyName_Type = SnmpAdminString
_CfprVnicDynamicConPolicyRefOperConPolicyName_Object = MibTableColumn
cfprVnicDynamicConPolicyRefOperConPolicyName = _CfprVnicDynamicConPolicyRefOperConPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 7, 1, 5),
    _CfprVnicDynamicConPolicyRefOperConPolicyName_Type()
)
cfprVnicDynamicConPolicyRefOperConPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicConPolicyRefOperConPolicyName.setStatus("current")
_CfprVnicDynamicIdUniverseTable_Object = MibTable
cfprVnicDynamicIdUniverseTable = _CfprVnicDynamicIdUniverseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 8)
)
if mibBuilder.loadTexts:
    cfprVnicDynamicIdUniverseTable.setStatus("current")
_CfprVnicDynamicIdUniverseEntry_Object = MibTableRow
cfprVnicDynamicIdUniverseEntry = _CfprVnicDynamicIdUniverseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 8, 1)
)
cfprVnicDynamicIdUniverseEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicDynamicIdUniverseInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicDynamicIdUniverseEntry.setStatus("current")
_CfprVnicDynamicIdUniverseInstanceId_Type = CfprManagedObjectId
_CfprVnicDynamicIdUniverseInstanceId_Object = MibTableColumn
cfprVnicDynamicIdUniverseInstanceId = _CfprVnicDynamicIdUniverseInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 8, 1, 1),
    _CfprVnicDynamicIdUniverseInstanceId_Type()
)
cfprVnicDynamicIdUniverseInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicDynamicIdUniverseInstanceId.setStatus("current")
_CfprVnicDynamicIdUniverseDn_Type = CfprManagedObjectDn
_CfprVnicDynamicIdUniverseDn_Object = MibTableColumn
cfprVnicDynamicIdUniverseDn = _CfprVnicDynamicIdUniverseDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 8, 1, 2),
    _CfprVnicDynamicIdUniverseDn_Type()
)
cfprVnicDynamicIdUniverseDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicIdUniverseDn.setStatus("current")
_CfprVnicDynamicIdUniverseRn_Type = SnmpAdminString
_CfprVnicDynamicIdUniverseRn_Object = MibTableColumn
cfprVnicDynamicIdUniverseRn = _CfprVnicDynamicIdUniverseRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 8, 1, 3),
    _CfprVnicDynamicIdUniverseRn_Type()
)
cfprVnicDynamicIdUniverseRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicIdUniverseRn.setStatus("current")
_CfprVnicDynamicIdUniverseDescr_Type = SnmpAdminString
_CfprVnicDynamicIdUniverseDescr_Object = MibTableColumn
cfprVnicDynamicIdUniverseDescr = _CfprVnicDynamicIdUniverseDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 8, 1, 4),
    _CfprVnicDynamicIdUniverseDescr_Type()
)
cfprVnicDynamicIdUniverseDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicIdUniverseDescr.setStatus("current")
_CfprVnicDynamicIdUniverseIntId_Type = SnmpAdminString
_CfprVnicDynamicIdUniverseIntId_Object = MibTableColumn
cfprVnicDynamicIdUniverseIntId = _CfprVnicDynamicIdUniverseIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 8, 1, 5),
    _CfprVnicDynamicIdUniverseIntId_Type()
)
cfprVnicDynamicIdUniverseIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicIdUniverseIntId.setStatus("current")
_CfprVnicDynamicIdUniverseName_Type = SnmpAdminString
_CfprVnicDynamicIdUniverseName_Object = MibTableColumn
cfprVnicDynamicIdUniverseName = _CfprVnicDynamicIdUniverseName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 8, 1, 6),
    _CfprVnicDynamicIdUniverseName_Type()
)
cfprVnicDynamicIdUniverseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicIdUniverseName.setStatus("current")
_CfprVnicDynamicIdUniversePolicyLevel_Type = Gauge32
_CfprVnicDynamicIdUniversePolicyLevel_Object = MibTableColumn
cfprVnicDynamicIdUniversePolicyLevel = _CfprVnicDynamicIdUniversePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 8, 1, 7),
    _CfprVnicDynamicIdUniversePolicyLevel_Type()
)
cfprVnicDynamicIdUniversePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicIdUniversePolicyLevel.setStatus("current")
_CfprVnicDynamicIdUniversePolicyOwner_Type = CfprPolicyPolicyOwner
_CfprVnicDynamicIdUniversePolicyOwner_Object = MibTableColumn
cfprVnicDynamicIdUniversePolicyOwner = _CfprVnicDynamicIdUniversePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 8, 1, 8),
    _CfprVnicDynamicIdUniversePolicyOwner_Type()
)
cfprVnicDynamicIdUniversePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicIdUniversePolicyOwner.setStatus("current")
_CfprVnicDynamicProviderTable_Object = MibTable
cfprVnicDynamicProviderTable = _CfprVnicDynamicProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 9)
)
if mibBuilder.loadTexts:
    cfprVnicDynamicProviderTable.setStatus("current")
_CfprVnicDynamicProviderEntry_Object = MibTableRow
cfprVnicDynamicProviderEntry = _CfprVnicDynamicProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 9, 1)
)
cfprVnicDynamicProviderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicDynamicProviderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicDynamicProviderEntry.setStatus("current")
_CfprVnicDynamicProviderInstanceId_Type = CfprManagedObjectId
_CfprVnicDynamicProviderInstanceId_Object = MibTableColumn
cfprVnicDynamicProviderInstanceId = _CfprVnicDynamicProviderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 9, 1, 1),
    _CfprVnicDynamicProviderInstanceId_Type()
)
cfprVnicDynamicProviderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicDynamicProviderInstanceId.setStatus("current")
_CfprVnicDynamicProviderDn_Type = CfprManagedObjectDn
_CfprVnicDynamicProviderDn_Object = MibTableColumn
cfprVnicDynamicProviderDn = _CfprVnicDynamicProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 9, 1, 2),
    _CfprVnicDynamicProviderDn_Type()
)
cfprVnicDynamicProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicProviderDn.setStatus("current")
_CfprVnicDynamicProviderRn_Type = SnmpAdminString
_CfprVnicDynamicProviderRn_Object = MibTableColumn
cfprVnicDynamicProviderRn = _CfprVnicDynamicProviderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 9, 1, 3),
    _CfprVnicDynamicProviderRn_Type()
)
cfprVnicDynamicProviderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicProviderRn.setStatus("current")
_CfprVnicDynamicProviderName_Type = SnmpAdminString
_CfprVnicDynamicProviderName_Object = MibTableColumn
cfprVnicDynamicProviderName = _CfprVnicDynamicProviderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 9, 1, 4),
    _CfprVnicDynamicProviderName_Type()
)
cfprVnicDynamicProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicProviderName.setStatus("current")
_CfprVnicDynamicProviderEpTable_Object = MibTable
cfprVnicDynamicProviderEpTable = _CfprVnicDynamicProviderEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 10)
)
if mibBuilder.loadTexts:
    cfprVnicDynamicProviderEpTable.setStatus("current")
_CfprVnicDynamicProviderEpEntry_Object = MibTableRow
cfprVnicDynamicProviderEpEntry = _CfprVnicDynamicProviderEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 10, 1)
)
cfprVnicDynamicProviderEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicDynamicProviderEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicDynamicProviderEpEntry.setStatus("current")
_CfprVnicDynamicProviderEpInstanceId_Type = CfprManagedObjectId
_CfprVnicDynamicProviderEpInstanceId_Object = MibTableColumn
cfprVnicDynamicProviderEpInstanceId = _CfprVnicDynamicProviderEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 10, 1, 1),
    _CfprVnicDynamicProviderEpInstanceId_Type()
)
cfprVnicDynamicProviderEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicDynamicProviderEpInstanceId.setStatus("current")
_CfprVnicDynamicProviderEpDn_Type = CfprManagedObjectDn
_CfprVnicDynamicProviderEpDn_Object = MibTableColumn
cfprVnicDynamicProviderEpDn = _CfprVnicDynamicProviderEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 10, 1, 2),
    _CfprVnicDynamicProviderEpDn_Type()
)
cfprVnicDynamicProviderEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicProviderEpDn.setStatus("current")
_CfprVnicDynamicProviderEpRn_Type = SnmpAdminString
_CfprVnicDynamicProviderEpRn_Object = MibTableColumn
cfprVnicDynamicProviderEpRn = _CfprVnicDynamicProviderEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 10, 1, 3),
    _CfprVnicDynamicProviderEpRn_Type()
)
cfprVnicDynamicProviderEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicProviderEpRn.setStatus("current")
_CfprVnicDynamicProviderEpChassisId_Type = Gauge32
_CfprVnicDynamicProviderEpChassisId_Object = MibTableColumn
cfprVnicDynamicProviderEpChassisId = _CfprVnicDynamicProviderEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 10, 1, 4),
    _CfprVnicDynamicProviderEpChassisId_Type()
)
cfprVnicDynamicProviderEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicProviderEpChassisId.setStatus("current")
_CfprVnicDynamicProviderEpPortId_Type = Gauge32
_CfprVnicDynamicProviderEpPortId_Object = MibTableColumn
cfprVnicDynamicProviderEpPortId = _CfprVnicDynamicProviderEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 10, 1, 5),
    _CfprVnicDynamicProviderEpPortId_Type()
)
cfprVnicDynamicProviderEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicProviderEpPortId.setStatus("current")
_CfprVnicDynamicProviderEpSlotId_Type = Gauge32
_CfprVnicDynamicProviderEpSlotId_Object = MibTableColumn
cfprVnicDynamicProviderEpSlotId = _CfprVnicDynamicProviderEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 10, 1, 6),
    _CfprVnicDynamicProviderEpSlotId_Type()
)
cfprVnicDynamicProviderEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicProviderEpSlotId.setStatus("current")
_CfprVnicDynamicProviderEpSwitchId_Type = CfprNetworkSwitchId
_CfprVnicDynamicProviderEpSwitchId_Object = MibTableColumn
cfprVnicDynamicProviderEpSwitchId = _CfprVnicDynamicProviderEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 10, 1, 7),
    _CfprVnicDynamicProviderEpSwitchId_Type()
)
cfprVnicDynamicProviderEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicDynamicProviderEpSwitchId.setStatus("current")
_CfprVnicEthLifTable_Object = MibTable
cfprVnicEthLifTable = _CfprVnicEthLifTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 11)
)
if mibBuilder.loadTexts:
    cfprVnicEthLifTable.setStatus("current")
_CfprVnicEthLifEntry_Object = MibTableRow
cfprVnicEthLifEntry = _CfprVnicEthLifEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 11, 1)
)
cfprVnicEthLifEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicEthLifInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicEthLifEntry.setStatus("current")
_CfprVnicEthLifInstanceId_Type = CfprManagedObjectId
_CfprVnicEthLifInstanceId_Object = MibTableColumn
cfprVnicEthLifInstanceId = _CfprVnicEthLifInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 11, 1, 1),
    _CfprVnicEthLifInstanceId_Type()
)
cfprVnicEthLifInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicEthLifInstanceId.setStatus("current")
_CfprVnicEthLifDn_Type = CfprManagedObjectDn
_CfprVnicEthLifDn_Object = MibTableColumn
cfprVnicEthLifDn = _CfprVnicEthLifDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 11, 1, 2),
    _CfprVnicEthLifDn_Type()
)
cfprVnicEthLifDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEthLifDn.setStatus("current")
_CfprVnicEthLifRn_Type = SnmpAdminString
_CfprVnicEthLifRn_Object = MibTableColumn
cfprVnicEthLifRn = _CfprVnicEthLifRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 11, 1, 3),
    _CfprVnicEthLifRn_Type()
)
cfprVnicEthLifRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEthLifRn.setStatus("current")
_CfprVnicEthLifAddr_Type = MacAddress
_CfprVnicEthLifAddr_Object = MibTableColumn
cfprVnicEthLifAddr = _CfprVnicEthLifAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 11, 1, 4),
    _CfprVnicEthLifAddr_Type()
)
cfprVnicEthLifAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEthLifAddr.setStatus("current")
_CfprVnicEthLifName_Type = SnmpAdminString
_CfprVnicEthLifName_Object = MibTableColumn
cfprVnicEthLifName = _CfprVnicEthLifName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 11, 1, 5),
    _CfprVnicEthLifName_Type()
)
cfprVnicEthLifName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEthLifName.setStatus("current")
_CfprVnicEthLifNicDn_Type = SnmpAdminString
_CfprVnicEthLifNicDn_Object = MibTableColumn
cfprVnicEthLifNicDn = _CfprVnicEthLifNicDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 11, 1, 6),
    _CfprVnicEthLifNicDn_Type()
)
cfprVnicEthLifNicDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEthLifNicDn.setStatus("current")
_CfprVnicEthLifOwner_Type = CfprVnicConnectionOwner
_CfprVnicEthLifOwner_Object = MibTableColumn
cfprVnicEthLifOwner = _CfprVnicEthLifOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 11, 1, 7),
    _CfprVnicEthLifOwner_Type()
)
cfprVnicEthLifOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEthLifOwner.setStatus("current")
_CfprVnicEthLifSwitchId_Type = CfprNetworkSwitchId
_CfprVnicEthLifSwitchId_Object = MibTableColumn
cfprVnicEthLifSwitchId = _CfprVnicEthLifSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 11, 1, 8),
    _CfprVnicEthLifSwitchId_Type()
)
cfprVnicEthLifSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEthLifSwitchId.setStatus("current")
_CfprVnicEthLifType_Type = CfprVnicConnectionType
_CfprVnicEthLifType_Object = MibTableColumn
cfprVnicEthLifType = _CfprVnicEthLifType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 11, 1, 9),
    _CfprVnicEthLifType_Type()
)
cfprVnicEthLifType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEthLifType.setStatus("current")
_CfprVnicEthLifVnicDn_Type = SnmpAdminString
_CfprVnicEthLifVnicDn_Object = MibTableColumn
cfprVnicEthLifVnicDn = _CfprVnicEthLifVnicDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 11, 1, 10),
    _CfprVnicEthLifVnicDn_Type()
)
cfprVnicEthLifVnicDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEthLifVnicDn.setStatus("current")
_CfprVnicEtherTable_Object = MibTable
cfprVnicEtherTable = _CfprVnicEtherTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12)
)
if mibBuilder.loadTexts:
    cfprVnicEtherTable.setStatus("current")
_CfprVnicEtherEntry_Object = MibTableRow
cfprVnicEtherEntry = _CfprVnicEtherEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1)
)
cfprVnicEtherEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicEtherInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicEtherEntry.setStatus("current")
_CfprVnicEtherInstanceId_Type = CfprManagedObjectId
_CfprVnicEtherInstanceId_Object = MibTableColumn
cfprVnicEtherInstanceId = _CfprVnicEtherInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 1),
    _CfprVnicEtherInstanceId_Type()
)
cfprVnicEtherInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicEtherInstanceId.setStatus("current")
_CfprVnicEtherDn_Type = CfprManagedObjectDn
_CfprVnicEtherDn_Object = MibTableColumn
cfprVnicEtherDn = _CfprVnicEtherDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 2),
    _CfprVnicEtherDn_Type()
)
cfprVnicEtherDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherDn.setStatus("current")
_CfprVnicEtherRn_Type = SnmpAdminString
_CfprVnicEtherRn_Object = MibTableColumn
cfprVnicEtherRn = _CfprVnicEtherRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 3),
    _CfprVnicEtherRn_Type()
)
cfprVnicEtherRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherRn.setStatus("current")
_CfprVnicEtherAdaptorProfileName_Type = SnmpAdminString
_CfprVnicEtherAdaptorProfileName_Object = MibTableColumn
cfprVnicEtherAdaptorProfileName = _CfprVnicEtherAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 4),
    _CfprVnicEtherAdaptorProfileName_Type()
)
cfprVnicEtherAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherAdaptorProfileName.setStatus("current")
_CfprVnicEtherAddr_Type = MacAddress
_CfprVnicEtherAddr_Object = MibTableColumn
cfprVnicEtherAddr = _CfprVnicEtherAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 5),
    _CfprVnicEtherAddr_Type()
)
cfprVnicEtherAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherAddr.setStatus("current")
_CfprVnicEtherAdminHostPort_Type = CfprFabricHostPortId
_CfprVnicEtherAdminHostPort_Object = MibTableColumn
cfprVnicEtherAdminHostPort = _CfprVnicEtherAdminHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 6),
    _CfprVnicEtherAdminHostPort_Type()
)
cfprVnicEtherAdminHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherAdminHostPort.setStatus("current")
_CfprVnicEtherAdminVcon_Type = SnmpAdminString
_CfprVnicEtherAdminVcon_Object = MibTableColumn
cfprVnicEtherAdminVcon = _CfprVnicEtherAdminVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 7),
    _CfprVnicEtherAdminVcon_Type()
)
cfprVnicEtherAdminVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherAdminVcon.setStatus("current")
_CfprVnicEtherAppInstId_Type = SnmpAdminString
_CfprVnicEtherAppInstId_Object = MibTableColumn
cfprVnicEtherAppInstId = _CfprVnicEtherAppInstId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 8),
    _CfprVnicEtherAppInstId_Type()
)
cfprVnicEtherAppInstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherAppInstId.setStatus("current")
_CfprVnicEtherAppRole_Type = CfprVnicAppRole
_CfprVnicEtherAppRole_Object = MibTableColumn
cfprVnicEtherAppRole = _CfprVnicEtherAppRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 9),
    _CfprVnicEtherAppRole_Type()
)
cfprVnicEtherAppRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherAppRole.setStatus("current")
_CfprVnicEtherBootDev_Type = CfprVnicVnicBootDev
_CfprVnicEtherBootDev_Object = MibTableColumn
cfprVnicEtherBootDev = _CfprVnicEtherBootDev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 10),
    _CfprVnicEtherBootDev_Type()
)
cfprVnicEtherBootDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherBootDev.setStatus("current")
_CfprVnicEtherConfigQualifier_Type = CfprVnicConfigIssues
_CfprVnicEtherConfigQualifier_Object = MibTableColumn
cfprVnicEtherConfigQualifier = _CfprVnicEtherConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 11),
    _CfprVnicEtherConfigQualifier_Type()
)
cfprVnicEtherConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherConfigQualifier.setStatus("current")
_CfprVnicEtherConfigState_Type = CfprLsConfigState
_CfprVnicEtherConfigState_Object = MibTableColumn
cfprVnicEtherConfigState = _CfprVnicEtherConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 12),
    _CfprVnicEtherConfigState_Type()
)
cfprVnicEtherConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherConfigState.setStatus("current")
_CfprVnicEtherDynamicId_Type = Gauge32
_CfprVnicEtherDynamicId_Object = MibTableColumn
cfprVnicEtherDynamicId = _CfprVnicEtherDynamicId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 13),
    _CfprVnicEtherDynamicId_Type()
)
cfprVnicEtherDynamicId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherDynamicId.setStatus("current")
_CfprVnicEtherEquipmentDn_Type = SnmpAdminString
_CfprVnicEtherEquipmentDn_Object = MibTableColumn
cfprVnicEtherEquipmentDn = _CfprVnicEtherEquipmentDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 14),
    _CfprVnicEtherEquipmentDn_Type()
)
cfprVnicEtherEquipmentDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherEquipmentDn.setStatus("current")
_CfprVnicEtherFltAggr_Type = Unsigned64
_CfprVnicEtherFltAggr_Object = MibTableColumn
cfprVnicEtherFltAggr = _CfprVnicEtherFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 15),
    _CfprVnicEtherFltAggr_Type()
)
cfprVnicEtherFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherFltAggr.setStatus("current")
_CfprVnicEtherIdentPoolName_Type = SnmpAdminString
_CfprVnicEtherIdentPoolName_Object = MibTableColumn
cfprVnicEtherIdentPoolName = _CfprVnicEtherIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 16),
    _CfprVnicEtherIdentPoolName_Type()
)
cfprVnicEtherIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherIdentPoolName.setStatus("current")
_CfprVnicEtherInstType_Type = CfprVnicInstantiation
_CfprVnicEtherInstType_Object = MibTableColumn
cfprVnicEtherInstType = _CfprVnicEtherInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 17),
    _CfprVnicEtherInstType_Type()
)
cfprVnicEtherInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherInstType.setStatus("current")
_CfprVnicEtherIsAllocated_Type = TruthValue
_CfprVnicEtherIsAllocated_Object = MibTableColumn
cfprVnicEtherIsAllocated = _CfprVnicEtherIsAllocated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 18),
    _CfprVnicEtherIsAllocated_Type()
)
cfprVnicEtherIsAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherIsAllocated.setStatus("current")
_CfprVnicEtherMtu_Type = Gauge32
_CfprVnicEtherMtu_Object = MibTableColumn
cfprVnicEtherMtu = _CfprVnicEtherMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 19),
    _CfprVnicEtherMtu_Type()
)
cfprVnicEtherMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherMtu.setStatus("current")
_CfprVnicEtherName_Type = SnmpAdminString
_CfprVnicEtherName_Object = MibTableColumn
cfprVnicEtherName = _CfprVnicEtherName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 20),
    _CfprVnicEtherName_Type()
)
cfprVnicEtherName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherName.setStatus("current")
_CfprVnicEtherNwCtrlPolicyName_Type = SnmpAdminString
_CfprVnicEtherNwCtrlPolicyName_Object = MibTableColumn
cfprVnicEtherNwCtrlPolicyName = _CfprVnicEtherNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 21),
    _CfprVnicEtherNwCtrlPolicyName_Type()
)
cfprVnicEtherNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherNwCtrlPolicyName.setStatus("current")
_CfprVnicEtherNwTemplName_Type = SnmpAdminString
_CfprVnicEtherNwTemplName_Object = MibTableColumn
cfprVnicEtherNwTemplName = _CfprVnicEtherNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 22),
    _CfprVnicEtherNwTemplName_Type()
)
cfprVnicEtherNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherNwTemplName.setStatus("current")
_CfprVnicEtherOperAdaptorProfileName_Type = SnmpAdminString
_CfprVnicEtherOperAdaptorProfileName_Object = MibTableColumn
cfprVnicEtherOperAdaptorProfileName = _CfprVnicEtherOperAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 23),
    _CfprVnicEtherOperAdaptorProfileName_Type()
)
cfprVnicEtherOperAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherOperAdaptorProfileName.setStatus("current")
_CfprVnicEtherOperHostPort_Type = CfprVnicVnicOperHostPort
_CfprVnicEtherOperHostPort_Object = MibTableColumn
cfprVnicEtherOperHostPort = _CfprVnicEtherOperHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 24),
    _CfprVnicEtherOperHostPort_Type()
)
cfprVnicEtherOperHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherOperHostPort.setStatus("current")
_CfprVnicEtherOperIdentPoolName_Type = SnmpAdminString
_CfprVnicEtherOperIdentPoolName_Object = MibTableColumn
cfprVnicEtherOperIdentPoolName = _CfprVnicEtherOperIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 25),
    _CfprVnicEtherOperIdentPoolName_Type()
)
cfprVnicEtherOperIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherOperIdentPoolName.setStatus("current")
_CfprVnicEtherOperNwCtrlPolicyName_Type = SnmpAdminString
_CfprVnicEtherOperNwCtrlPolicyName_Object = MibTableColumn
cfprVnicEtherOperNwCtrlPolicyName = _CfprVnicEtherOperNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 26),
    _CfprVnicEtherOperNwCtrlPolicyName_Type()
)
cfprVnicEtherOperNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherOperNwCtrlPolicyName.setStatus("current")
_CfprVnicEtherOperNwTemplName_Type = SnmpAdminString
_CfprVnicEtherOperNwTemplName_Object = MibTableColumn
cfprVnicEtherOperNwTemplName = _CfprVnicEtherOperNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 27),
    _CfprVnicEtherOperNwTemplName_Type()
)
cfprVnicEtherOperNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherOperNwTemplName.setStatus("current")
_CfprVnicEtherOperOrder_Type = Gauge32
_CfprVnicEtherOperOrder_Object = MibTableColumn
cfprVnicEtherOperOrder = _CfprVnicEtherOperOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 28),
    _CfprVnicEtherOperOrder_Type()
)
cfprVnicEtherOperOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherOperOrder.setStatus("current")
_CfprVnicEtherOperPinToGroupName_Type = SnmpAdminString
_CfprVnicEtherOperPinToGroupName_Object = MibTableColumn
cfprVnicEtherOperPinToGroupName = _CfprVnicEtherOperPinToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 29),
    _CfprVnicEtherOperPinToGroupName_Type()
)
cfprVnicEtherOperPinToGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherOperPinToGroupName.setStatus("current")
_CfprVnicEtherOperQosPolicyName_Type = SnmpAdminString
_CfprVnicEtherOperQosPolicyName_Object = MibTableColumn
cfprVnicEtherOperQosPolicyName = _CfprVnicEtherOperQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 30),
    _CfprVnicEtherOperQosPolicyName_Type()
)
cfprVnicEtherOperQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherOperQosPolicyName.setStatus("current")
_CfprVnicEtherOperSpeed_Type = Gauge32
_CfprVnicEtherOperSpeed_Object = MibTableColumn
cfprVnicEtherOperSpeed = _CfprVnicEtherOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 31),
    _CfprVnicEtherOperSpeed_Type()
)
cfprVnicEtherOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherOperSpeed.setStatus("current")
_CfprVnicEtherOperStatsPolicyName_Type = SnmpAdminString
_CfprVnicEtherOperStatsPolicyName_Object = MibTableColumn
cfprVnicEtherOperStatsPolicyName = _CfprVnicEtherOperStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 32),
    _CfprVnicEtherOperStatsPolicyName_Type()
)
cfprVnicEtherOperStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherOperStatsPolicyName.setStatus("current")
_CfprVnicEtherOperVcon_Type = SnmpAdminString
_CfprVnicEtherOperVcon_Object = MibTableColumn
cfprVnicEtherOperVcon = _CfprVnicEtherOperVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 33),
    _CfprVnicEtherOperVcon_Type()
)
cfprVnicEtherOperVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherOperVcon.setStatus("current")
_CfprVnicEtherOrder_Type = Gauge32
_CfprVnicEtherOrder_Object = MibTableColumn
cfprVnicEtherOrder = _CfprVnicEtherOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 34),
    _CfprVnicEtherOrder_Type()
)
cfprVnicEtherOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherOrder.setStatus("current")
_CfprVnicEtherOwner_Type = CfprVnicConnectionOwner
_CfprVnicEtherOwner_Object = MibTableColumn
cfprVnicEtherOwner = _CfprVnicEtherOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 35),
    _CfprVnicEtherOwner_Type()
)
cfprVnicEtherOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherOwner.setStatus("current")
_CfprVnicEtherPfDn_Type = SnmpAdminString
_CfprVnicEtherPfDn_Object = MibTableColumn
cfprVnicEtherPfDn = _CfprVnicEtherPfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 36),
    _CfprVnicEtherPfDn_Type()
)
cfprVnicEtherPfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherPfDn.setStatus("current")
_CfprVnicEtherPinToGroupName_Type = SnmpAdminString
_CfprVnicEtherPinToGroupName_Object = MibTableColumn
cfprVnicEtherPinToGroupName = _CfprVnicEtherPinToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 37),
    _CfprVnicEtherPinToGroupName_Type()
)
cfprVnicEtherPinToGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherPinToGroupName.setStatus("current")
_CfprVnicEtherQosPolicyName_Type = SnmpAdminString
_CfprVnicEtherQosPolicyName_Object = MibTableColumn
cfprVnicEtherQosPolicyName = _CfprVnicEtherQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 38),
    _CfprVnicEtherQosPolicyName_Type()
)
cfprVnicEtherQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherQosPolicyName.setStatus("current")
_CfprVnicEtherStatsPolicyName_Type = SnmpAdminString
_CfprVnicEtherStatsPolicyName_Object = MibTableColumn
cfprVnicEtherStatsPolicyName = _CfprVnicEtherStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 39),
    _CfprVnicEtherStatsPolicyName_Type()
)
cfprVnicEtherStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherStatsPolicyName.setStatus("current")
_CfprVnicEtherSwitchId_Type = CfprVnicEtherBaseSwitchId
_CfprVnicEtherSwitchId_Object = MibTableColumn
cfprVnicEtherSwitchId = _CfprVnicEtherSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 40),
    _CfprVnicEtherSwitchId_Type()
)
cfprVnicEtherSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherSwitchId.setStatus("current")
_CfprVnicEtherType_Type = CfprVnicEtherType
_CfprVnicEtherType_Object = MibTableColumn
cfprVnicEtherType = _CfprVnicEtherType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 41),
    _CfprVnicEtherType_Type()
)
cfprVnicEtherType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherType.setStatus("current")
_CfprVnicEtherVirtualizationPreference_Type = CfprVnicVirtualizationPreferenceType
_CfprVnicEtherVirtualizationPreference_Object = MibTableColumn
cfprVnicEtherVirtualizationPreference = _CfprVnicEtherVirtualizationPreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 42),
    _CfprVnicEtherVirtualizationPreference_Type()
)
cfprVnicEtherVirtualizationPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherVirtualizationPreference.setStatus("current")
_CfprVnicEtherPortType_Type = CfprFabricSSAPortType
_CfprVnicEtherPortType_Object = MibTableColumn
cfprVnicEtherPortType = _CfprVnicEtherPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 12, 1, 43),
    _CfprVnicEtherPortType_Type()
)
cfprVnicEtherPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherPortType.setStatus("current")
_CfprVnicEtherIfTable_Object = MibTable
cfprVnicEtherIfTable = _CfprVnicEtherIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 13)
)
if mibBuilder.loadTexts:
    cfprVnicEtherIfTable.setStatus("current")
_CfprVnicEtherIfEntry_Object = MibTableRow
cfprVnicEtherIfEntry = _CfprVnicEtherIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 13, 1)
)
cfprVnicEtherIfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicEtherIfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicEtherIfEntry.setStatus("current")
_CfprVnicEtherIfInstanceId_Type = CfprManagedObjectId
_CfprVnicEtherIfInstanceId_Object = MibTableColumn
cfprVnicEtherIfInstanceId = _CfprVnicEtherIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 13, 1, 1),
    _CfprVnicEtherIfInstanceId_Type()
)
cfprVnicEtherIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicEtherIfInstanceId.setStatus("current")
_CfprVnicEtherIfDn_Type = CfprManagedObjectDn
_CfprVnicEtherIfDn_Object = MibTableColumn
cfprVnicEtherIfDn = _CfprVnicEtherIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 13, 1, 2),
    _CfprVnicEtherIfDn_Type()
)
cfprVnicEtherIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherIfDn.setStatus("current")
_CfprVnicEtherIfRn_Type = SnmpAdminString
_CfprVnicEtherIfRn_Object = MibTableColumn
cfprVnicEtherIfRn = _CfprVnicEtherIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 13, 1, 3),
    _CfprVnicEtherIfRn_Type()
)
cfprVnicEtherIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherIfRn.setStatus("current")
_CfprVnicEtherIfAddr_Type = MacAddress
_CfprVnicEtherIfAddr_Object = MibTableColumn
cfprVnicEtherIfAddr = _CfprVnicEtherIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 13, 1, 4),
    _CfprVnicEtherIfAddr_Type()
)
cfprVnicEtherIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherIfAddr.setStatus("current")
_CfprVnicEtherIfConfigQualifier_Type = CfprVnicConfigIssues
_CfprVnicEtherIfConfigQualifier_Object = MibTableColumn
cfprVnicEtherIfConfigQualifier = _CfprVnicEtherIfConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 13, 1, 5),
    _CfprVnicEtherIfConfigQualifier_Type()
)
cfprVnicEtherIfConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherIfConfigQualifier.setStatus("current")
_CfprVnicEtherIfDefaultNet_Type = TruthValue
_CfprVnicEtherIfDefaultNet_Object = MibTableColumn
cfprVnicEtherIfDefaultNet = _CfprVnicEtherIfDefaultNet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 13, 1, 6),
    _CfprVnicEtherIfDefaultNet_Type()
)
cfprVnicEtherIfDefaultNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherIfDefaultNet.setStatus("current")
_CfprVnicEtherIfFltAggr_Type = Unsigned64
_CfprVnicEtherIfFltAggr_Object = MibTableColumn
cfprVnicEtherIfFltAggr = _CfprVnicEtherIfFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 13, 1, 7),
    _CfprVnicEtherIfFltAggr_Type()
)
cfprVnicEtherIfFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherIfFltAggr.setStatus("current")
_CfprVnicEtherIfName_Type = SnmpAdminString
_CfprVnicEtherIfName_Object = MibTableColumn
cfprVnicEtherIfName = _CfprVnicEtherIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 13, 1, 8),
    _CfprVnicEtherIfName_Type()
)
cfprVnicEtherIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherIfName.setStatus("current")
_CfprVnicEtherIfOperState_Type = CfprVnicIfOperState
_CfprVnicEtherIfOperState_Object = MibTableColumn
cfprVnicEtherIfOperState = _CfprVnicEtherIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 13, 1, 9),
    _CfprVnicEtherIfOperState_Type()
)
cfprVnicEtherIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherIfOperState.setStatus("current")
_CfprVnicEtherIfOperVnetDn_Type = SnmpAdminString
_CfprVnicEtherIfOperVnetDn_Object = MibTableColumn
cfprVnicEtherIfOperVnetDn = _CfprVnicEtherIfOperVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 13, 1, 10),
    _CfprVnicEtherIfOperVnetDn_Type()
)
cfprVnicEtherIfOperVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherIfOperVnetDn.setStatus("current")
_CfprVnicEtherIfOperVnetName_Type = SnmpAdminString
_CfprVnicEtherIfOperVnetName_Object = MibTableColumn
cfprVnicEtherIfOperVnetName = _CfprVnicEtherIfOperVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 13, 1, 11),
    _CfprVnicEtherIfOperVnetName_Type()
)
cfprVnicEtherIfOperVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherIfOperVnetName.setStatus("current")
_CfprVnicEtherIfOwner_Type = CfprVnicConnectionOwner
_CfprVnicEtherIfOwner_Object = MibTableColumn
cfprVnicEtherIfOwner = _CfprVnicEtherIfOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 13, 1, 12),
    _CfprVnicEtherIfOwner_Type()
)
cfprVnicEtherIfOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherIfOwner.setStatus("current")
_CfprVnicEtherIfPubNwId_Type = Gauge32
_CfprVnicEtherIfPubNwId_Object = MibTableColumn
cfprVnicEtherIfPubNwId = _CfprVnicEtherIfPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 13, 1, 13),
    _CfprVnicEtherIfPubNwId_Type()
)
cfprVnicEtherIfPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherIfPubNwId.setStatus("current")
_CfprVnicEtherIfSharing_Type = CfprFabricVlanSharingType
_CfprVnicEtherIfSharing_Object = MibTableColumn
cfprVnicEtherIfSharing = _CfprVnicEtherIfSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 13, 1, 14),
    _CfprVnicEtherIfSharing_Type()
)
cfprVnicEtherIfSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherIfSharing.setStatus("current")
_CfprVnicEtherIfSwitchId_Type = CfprVnicL2IfSwitchId
_CfprVnicEtherIfSwitchId_Object = MibTableColumn
cfprVnicEtherIfSwitchId = _CfprVnicEtherIfSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 13, 1, 15),
    _CfprVnicEtherIfSwitchId_Type()
)
cfprVnicEtherIfSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherIfSwitchId.setStatus("current")
_CfprVnicEtherIfType_Type = CfprVnicAEtherIfType
_CfprVnicEtherIfType_Object = MibTableColumn
cfprVnicEtherIfType = _CfprVnicEtherIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 13, 1, 16),
    _CfprVnicEtherIfType_Type()
)
cfprVnicEtherIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherIfType.setStatus("current")
_CfprVnicEtherIfVnet_Type = Gauge32
_CfprVnicEtherIfVnet_Object = MibTableColumn
cfprVnicEtherIfVnet = _CfprVnicEtherIfVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 13, 1, 17),
    _CfprVnicEtherIfVnet_Type()
)
cfprVnicEtherIfVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicEtherIfVnet.setStatus("current")
_CfprVnicFcTable_Object = MibTable
cfprVnicFcTable = _CfprVnicFcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14)
)
if mibBuilder.loadTexts:
    cfprVnicFcTable.setStatus("current")
_CfprVnicFcEntry_Object = MibTableRow
cfprVnicFcEntry = _CfprVnicFcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1)
)
cfprVnicFcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicFcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicFcEntry.setStatus("current")
_CfprVnicFcInstanceId_Type = CfprManagedObjectId
_CfprVnicFcInstanceId_Object = MibTableColumn
cfprVnicFcInstanceId = _CfprVnicFcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 1),
    _CfprVnicFcInstanceId_Type()
)
cfprVnicFcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicFcInstanceId.setStatus("current")
_CfprVnicFcDn_Type = CfprManagedObjectDn
_CfprVnicFcDn_Object = MibTableColumn
cfprVnicFcDn = _CfprVnicFcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 2),
    _CfprVnicFcDn_Type()
)
cfprVnicFcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcDn.setStatus("current")
_CfprVnicFcRn_Type = SnmpAdminString
_CfprVnicFcRn_Object = MibTableColumn
cfprVnicFcRn = _CfprVnicFcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 3),
    _CfprVnicFcRn_Type()
)
cfprVnicFcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcRn.setStatus("current")
_CfprVnicFcAdaptorProfileName_Type = SnmpAdminString
_CfprVnicFcAdaptorProfileName_Object = MibTableColumn
cfprVnicFcAdaptorProfileName = _CfprVnicFcAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 4),
    _CfprVnicFcAdaptorProfileName_Type()
)
cfprVnicFcAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcAdaptorProfileName.setStatus("current")
_CfprVnicFcAddr_Type = Unsigned64
_CfprVnicFcAddr_Object = MibTableColumn
cfprVnicFcAddr = _CfprVnicFcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 5),
    _CfprVnicFcAddr_Type()
)
cfprVnicFcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcAddr.setStatus("current")
_CfprVnicFcAdminHostPort_Type = CfprFabricHostPortId
_CfprVnicFcAdminHostPort_Object = MibTableColumn
cfprVnicFcAdminHostPort = _CfprVnicFcAdminHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 6),
    _CfprVnicFcAdminHostPort_Type()
)
cfprVnicFcAdminHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcAdminHostPort.setStatus("current")
_CfprVnicFcAdminVcon_Type = SnmpAdminString
_CfprVnicFcAdminVcon_Object = MibTableColumn
cfprVnicFcAdminVcon = _CfprVnicFcAdminVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 7),
    _CfprVnicFcAdminVcon_Type()
)
cfprVnicFcAdminVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcAdminVcon.setStatus("current")
_CfprVnicFcAppRole_Type = CfprVnicAppRole
_CfprVnicFcAppRole_Object = MibTableColumn
cfprVnicFcAppRole = _CfprVnicFcAppRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 8),
    _CfprVnicFcAppRole_Type()
)
cfprVnicFcAppRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcAppRole.setStatus("current")
_CfprVnicFcBootDev_Type = CfprVnicVnicBootDev
_CfprVnicFcBootDev_Object = MibTableColumn
cfprVnicFcBootDev = _CfprVnicFcBootDev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 9),
    _CfprVnicFcBootDev_Type()
)
cfprVnicFcBootDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcBootDev.setStatus("current")
_CfprVnicFcConfigQualifier_Type = CfprVnicConfigIssues
_CfprVnicFcConfigQualifier_Object = MibTableColumn
cfprVnicFcConfigQualifier = _CfprVnicFcConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 10),
    _CfprVnicFcConfigQualifier_Type()
)
cfprVnicFcConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcConfigQualifier.setStatus("current")
_CfprVnicFcConfigState_Type = CfprLsConfigState
_CfprVnicFcConfigState_Object = MibTableColumn
cfprVnicFcConfigState = _CfprVnicFcConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 11),
    _CfprVnicFcConfigState_Type()
)
cfprVnicFcConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcConfigState.setStatus("current")
_CfprVnicFcEquipmentDn_Type = SnmpAdminString
_CfprVnicFcEquipmentDn_Object = MibTableColumn
cfprVnicFcEquipmentDn = _CfprVnicFcEquipmentDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 12),
    _CfprVnicFcEquipmentDn_Type()
)
cfprVnicFcEquipmentDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcEquipmentDn.setStatus("current")
_CfprVnicFcFltAggr_Type = Unsigned64
_CfprVnicFcFltAggr_Object = MibTableColumn
cfprVnicFcFltAggr = _CfprVnicFcFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 13),
    _CfprVnicFcFltAggr_Type()
)
cfprVnicFcFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcFltAggr.setStatus("current")
_CfprVnicFcIdentPoolName_Type = SnmpAdminString
_CfprVnicFcIdentPoolName_Object = MibTableColumn
cfprVnicFcIdentPoolName = _CfprVnicFcIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 14),
    _CfprVnicFcIdentPoolName_Type()
)
cfprVnicFcIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcIdentPoolName.setStatus("current")
_CfprVnicFcInstType_Type = CfprVnicInstantiation
_CfprVnicFcInstType_Object = MibTableColumn
cfprVnicFcInstType = _CfprVnicFcInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 15),
    _CfprVnicFcInstType_Type()
)
cfprVnicFcInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcInstType.setStatus("current")
_CfprVnicFcMaxDataFieldSize_Type = Gauge32
_CfprVnicFcMaxDataFieldSize_Object = MibTableColumn
cfprVnicFcMaxDataFieldSize = _CfprVnicFcMaxDataFieldSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 16),
    _CfprVnicFcMaxDataFieldSize_Type()
)
cfprVnicFcMaxDataFieldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcMaxDataFieldSize.setStatus("current")
_CfprVnicFcName_Type = SnmpAdminString
_CfprVnicFcName_Object = MibTableColumn
cfprVnicFcName = _CfprVnicFcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 17),
    _CfprVnicFcName_Type()
)
cfprVnicFcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcName.setStatus("current")
_CfprVnicFcNodeAddr_Type = Unsigned64
_CfprVnicFcNodeAddr_Object = MibTableColumn
cfprVnicFcNodeAddr = _CfprVnicFcNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 18),
    _CfprVnicFcNodeAddr_Type()
)
cfprVnicFcNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcNodeAddr.setStatus("current")
_CfprVnicFcNwTemplName_Type = SnmpAdminString
_CfprVnicFcNwTemplName_Object = MibTableColumn
cfprVnicFcNwTemplName = _CfprVnicFcNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 19),
    _CfprVnicFcNwTemplName_Type()
)
cfprVnicFcNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcNwTemplName.setStatus("current")
_CfprVnicFcOperAdaptorProfileName_Type = SnmpAdminString
_CfprVnicFcOperAdaptorProfileName_Object = MibTableColumn
cfprVnicFcOperAdaptorProfileName = _CfprVnicFcOperAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 20),
    _CfprVnicFcOperAdaptorProfileName_Type()
)
cfprVnicFcOperAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcOperAdaptorProfileName.setStatus("current")
_CfprVnicFcOperHostPort_Type = CfprVnicVnicOperHostPort
_CfprVnicFcOperHostPort_Object = MibTableColumn
cfprVnicFcOperHostPort = _CfprVnicFcOperHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 21),
    _CfprVnicFcOperHostPort_Type()
)
cfprVnicFcOperHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcOperHostPort.setStatus("current")
_CfprVnicFcOperIdentPoolName_Type = SnmpAdminString
_CfprVnicFcOperIdentPoolName_Object = MibTableColumn
cfprVnicFcOperIdentPoolName = _CfprVnicFcOperIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 22),
    _CfprVnicFcOperIdentPoolName_Type()
)
cfprVnicFcOperIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcOperIdentPoolName.setStatus("current")
_CfprVnicFcOperNwTemplName_Type = SnmpAdminString
_CfprVnicFcOperNwTemplName_Object = MibTableColumn
cfprVnicFcOperNwTemplName = _CfprVnicFcOperNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 23),
    _CfprVnicFcOperNwTemplName_Type()
)
cfprVnicFcOperNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcOperNwTemplName.setStatus("current")
_CfprVnicFcOperOrder_Type = Gauge32
_CfprVnicFcOperOrder_Object = MibTableColumn
cfprVnicFcOperOrder = _CfprVnicFcOperOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 24),
    _CfprVnicFcOperOrder_Type()
)
cfprVnicFcOperOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcOperOrder.setStatus("current")
_CfprVnicFcOperPinToGroupName_Type = SnmpAdminString
_CfprVnicFcOperPinToGroupName_Object = MibTableColumn
cfprVnicFcOperPinToGroupName = _CfprVnicFcOperPinToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 25),
    _CfprVnicFcOperPinToGroupName_Type()
)
cfprVnicFcOperPinToGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcOperPinToGroupName.setStatus("current")
_CfprVnicFcOperQosPolicyName_Type = SnmpAdminString
_CfprVnicFcOperQosPolicyName_Object = MibTableColumn
cfprVnicFcOperQosPolicyName = _CfprVnicFcOperQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 26),
    _CfprVnicFcOperQosPolicyName_Type()
)
cfprVnicFcOperQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcOperQosPolicyName.setStatus("current")
_CfprVnicFcOperSpeed_Type = Gauge32
_CfprVnicFcOperSpeed_Object = MibTableColumn
cfprVnicFcOperSpeed = _CfprVnicFcOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 27),
    _CfprVnicFcOperSpeed_Type()
)
cfprVnicFcOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcOperSpeed.setStatus("current")
_CfprVnicFcOperStatsPolicyName_Type = SnmpAdminString
_CfprVnicFcOperStatsPolicyName_Object = MibTableColumn
cfprVnicFcOperStatsPolicyName = _CfprVnicFcOperStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 28),
    _CfprVnicFcOperStatsPolicyName_Type()
)
cfprVnicFcOperStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcOperStatsPolicyName.setStatus("current")
_CfprVnicFcOperVcon_Type = SnmpAdminString
_CfprVnicFcOperVcon_Object = MibTableColumn
cfprVnicFcOperVcon = _CfprVnicFcOperVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 29),
    _CfprVnicFcOperVcon_Type()
)
cfprVnicFcOperVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcOperVcon.setStatus("current")
_CfprVnicFcOrder_Type = Gauge32
_CfprVnicFcOrder_Object = MibTableColumn
cfprVnicFcOrder = _CfprVnicFcOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 30),
    _CfprVnicFcOrder_Type()
)
cfprVnicFcOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcOrder.setStatus("current")
_CfprVnicFcOwner_Type = CfprVnicConnectionOwner
_CfprVnicFcOwner_Object = MibTableColumn
cfprVnicFcOwner = _CfprVnicFcOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 31),
    _CfprVnicFcOwner_Type()
)
cfprVnicFcOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcOwner.setStatus("current")
_CfprVnicFcPersBind_Type = CfprVnicFcBasePersBind
_CfprVnicFcPersBind_Object = MibTableColumn
cfprVnicFcPersBind = _CfprVnicFcPersBind_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 32),
    _CfprVnicFcPersBind_Type()
)
cfprVnicFcPersBind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcPersBind.setStatus("current")
_CfprVnicFcPersBindClear_Type = TruthValue
_CfprVnicFcPersBindClear_Object = MibTableColumn
cfprVnicFcPersBindClear = _CfprVnicFcPersBindClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 33),
    _CfprVnicFcPersBindClear_Type()
)
cfprVnicFcPersBindClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcPersBindClear.setStatus("current")
_CfprVnicFcPinToGroupName_Type = SnmpAdminString
_CfprVnicFcPinToGroupName_Object = MibTableColumn
cfprVnicFcPinToGroupName = _CfprVnicFcPinToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 34),
    _CfprVnicFcPinToGroupName_Type()
)
cfprVnicFcPinToGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcPinToGroupName.setStatus("current")
_CfprVnicFcQosPolicyName_Type = SnmpAdminString
_CfprVnicFcQosPolicyName_Object = MibTableColumn
cfprVnicFcQosPolicyName = _CfprVnicFcQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 35),
    _CfprVnicFcQosPolicyName_Type()
)
cfprVnicFcQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcQosPolicyName.setStatus("current")
_CfprVnicFcStatsPolicyName_Type = SnmpAdminString
_CfprVnicFcStatsPolicyName_Object = MibTableColumn
cfprVnicFcStatsPolicyName = _CfprVnicFcStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 36),
    _CfprVnicFcStatsPolicyName_Type()
)
cfprVnicFcStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcStatsPolicyName.setStatus("current")
_CfprVnicFcSwitchId_Type = CfprNetworkSwitchId
_CfprVnicFcSwitchId_Object = MibTableColumn
cfprVnicFcSwitchId = _CfprVnicFcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 37),
    _CfprVnicFcSwitchId_Type()
)
cfprVnicFcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcSwitchId.setStatus("current")
_CfprVnicFcType_Type = CfprVnicFcBaseType
_CfprVnicFcType_Object = MibTableColumn
cfprVnicFcType = _CfprVnicFcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 14, 1, 38),
    _CfprVnicFcType_Type()
)
cfprVnicFcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcType.setStatus("current")
_CfprVnicFcGroupDefTable_Object = MibTable
cfprVnicFcGroupDefTable = _CfprVnicFcGroupDefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 15)
)
if mibBuilder.loadTexts:
    cfprVnicFcGroupDefTable.setStatus("current")
_CfprVnicFcGroupDefEntry_Object = MibTableRow
cfprVnicFcGroupDefEntry = _CfprVnicFcGroupDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 15, 1)
)
cfprVnicFcGroupDefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicFcGroupDefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicFcGroupDefEntry.setStatus("current")
_CfprVnicFcGroupDefInstanceId_Type = CfprManagedObjectId
_CfprVnicFcGroupDefInstanceId_Object = MibTableColumn
cfprVnicFcGroupDefInstanceId = _CfprVnicFcGroupDefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 15, 1, 1),
    _CfprVnicFcGroupDefInstanceId_Type()
)
cfprVnicFcGroupDefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicFcGroupDefInstanceId.setStatus("current")
_CfprVnicFcGroupDefDn_Type = CfprManagedObjectDn
_CfprVnicFcGroupDefDn_Object = MibTableColumn
cfprVnicFcGroupDefDn = _CfprVnicFcGroupDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 15, 1, 2),
    _CfprVnicFcGroupDefDn_Type()
)
cfprVnicFcGroupDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcGroupDefDn.setStatus("current")
_CfprVnicFcGroupDefRn_Type = SnmpAdminString
_CfprVnicFcGroupDefRn_Object = MibTableColumn
cfprVnicFcGroupDefRn = _CfprVnicFcGroupDefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 15, 1, 3),
    _CfprVnicFcGroupDefRn_Type()
)
cfprVnicFcGroupDefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcGroupDefRn.setStatus("current")
_CfprVnicFcGroupDefAdaptorProfileName_Type = SnmpAdminString
_CfprVnicFcGroupDefAdaptorProfileName_Object = MibTableColumn
cfprVnicFcGroupDefAdaptorProfileName = _CfprVnicFcGroupDefAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 15, 1, 4),
    _CfprVnicFcGroupDefAdaptorProfileName_Type()
)
cfprVnicFcGroupDefAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcGroupDefAdaptorProfileName.setStatus("current")
_CfprVnicFcGroupDefDescr_Type = SnmpAdminString
_CfprVnicFcGroupDefDescr_Object = MibTableColumn
cfprVnicFcGroupDefDescr = _CfprVnicFcGroupDefDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 15, 1, 5),
    _CfprVnicFcGroupDefDescr_Type()
)
cfprVnicFcGroupDefDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcGroupDefDescr.setStatus("current")
_CfprVnicFcGroupDefIdentPoolName_Type = SnmpAdminString
_CfprVnicFcGroupDefIdentPoolName_Object = MibTableColumn
cfprVnicFcGroupDefIdentPoolName = _CfprVnicFcGroupDefIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 15, 1, 6),
    _CfprVnicFcGroupDefIdentPoolName_Type()
)
cfprVnicFcGroupDefIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcGroupDefIdentPoolName.setStatus("current")
_CfprVnicFcGroupDefIntId_Type = SnmpAdminString
_CfprVnicFcGroupDefIntId_Object = MibTableColumn
cfprVnicFcGroupDefIntId = _CfprVnicFcGroupDefIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 15, 1, 7),
    _CfprVnicFcGroupDefIntId_Type()
)
cfprVnicFcGroupDefIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcGroupDefIntId.setStatus("current")
_CfprVnicFcGroupDefMaxDataFieldSize_Type = Gauge32
_CfprVnicFcGroupDefMaxDataFieldSize_Object = MibTableColumn
cfprVnicFcGroupDefMaxDataFieldSize = _CfprVnicFcGroupDefMaxDataFieldSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 15, 1, 8),
    _CfprVnicFcGroupDefMaxDataFieldSize_Type()
)
cfprVnicFcGroupDefMaxDataFieldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcGroupDefMaxDataFieldSize.setStatus("current")
_CfprVnicFcGroupDefName_Type = SnmpAdminString
_CfprVnicFcGroupDefName_Object = MibTableColumn
cfprVnicFcGroupDefName = _CfprVnicFcGroupDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 15, 1, 9),
    _CfprVnicFcGroupDefName_Type()
)
cfprVnicFcGroupDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcGroupDefName.setStatus("current")
_CfprVnicFcGroupDefNwTemplName_Type = SnmpAdminString
_CfprVnicFcGroupDefNwTemplName_Object = MibTableColumn
cfprVnicFcGroupDefNwTemplName = _CfprVnicFcGroupDefNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 15, 1, 10),
    _CfprVnicFcGroupDefNwTemplName_Type()
)
cfprVnicFcGroupDefNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcGroupDefNwTemplName.setStatus("current")
_CfprVnicFcGroupDefOperStatsPolicyName_Type = SnmpAdminString
_CfprVnicFcGroupDefOperStatsPolicyName_Object = MibTableColumn
cfprVnicFcGroupDefOperStatsPolicyName = _CfprVnicFcGroupDefOperStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 15, 1, 11),
    _CfprVnicFcGroupDefOperStatsPolicyName_Type()
)
cfprVnicFcGroupDefOperStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcGroupDefOperStatsPolicyName.setStatus("current")
_CfprVnicFcGroupDefOperStorageConnPolicyName_Type = SnmpAdminString
_CfprVnicFcGroupDefOperStorageConnPolicyName_Object = MibTableColumn
cfprVnicFcGroupDefOperStorageConnPolicyName = _CfprVnicFcGroupDefOperStorageConnPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 15, 1, 12),
    _CfprVnicFcGroupDefOperStorageConnPolicyName_Type()
)
cfprVnicFcGroupDefOperStorageConnPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcGroupDefOperStorageConnPolicyName.setStatus("current")
_CfprVnicFcGroupDefPolicyLevel_Type = Gauge32
_CfprVnicFcGroupDefPolicyLevel_Object = MibTableColumn
cfprVnicFcGroupDefPolicyLevel = _CfprVnicFcGroupDefPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 15, 1, 13),
    _CfprVnicFcGroupDefPolicyLevel_Type()
)
cfprVnicFcGroupDefPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcGroupDefPolicyLevel.setStatus("current")
_CfprVnicFcGroupDefPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprVnicFcGroupDefPolicyOwner_Object = MibTableColumn
cfprVnicFcGroupDefPolicyOwner = _CfprVnicFcGroupDefPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 15, 1, 14),
    _CfprVnicFcGroupDefPolicyOwner_Type()
)
cfprVnicFcGroupDefPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcGroupDefPolicyOwner.setStatus("current")
_CfprVnicFcGroupDefQosPolicyName_Type = SnmpAdminString
_CfprVnicFcGroupDefQosPolicyName_Object = MibTableColumn
cfprVnicFcGroupDefQosPolicyName = _CfprVnicFcGroupDefQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 15, 1, 15),
    _CfprVnicFcGroupDefQosPolicyName_Type()
)
cfprVnicFcGroupDefQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcGroupDefQosPolicyName.setStatus("current")
_CfprVnicFcGroupDefStatsPolicyName_Type = SnmpAdminString
_CfprVnicFcGroupDefStatsPolicyName_Object = MibTableColumn
cfprVnicFcGroupDefStatsPolicyName = _CfprVnicFcGroupDefStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 15, 1, 16),
    _CfprVnicFcGroupDefStatsPolicyName_Type()
)
cfprVnicFcGroupDefStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcGroupDefStatsPolicyName.setStatus("current")
_CfprVnicFcGroupDefStorageConnPolicyName_Type = SnmpAdminString
_CfprVnicFcGroupDefStorageConnPolicyName_Object = MibTableColumn
cfprVnicFcGroupDefStorageConnPolicyName = _CfprVnicFcGroupDefStorageConnPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 15, 1, 17),
    _CfprVnicFcGroupDefStorageConnPolicyName_Type()
)
cfprVnicFcGroupDefStorageConnPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcGroupDefStorageConnPolicyName.setStatus("current")
_CfprVnicFcGroupTemplTable_Object = MibTable
cfprVnicFcGroupTemplTable = _CfprVnicFcGroupTemplTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 16)
)
if mibBuilder.loadTexts:
    cfprVnicFcGroupTemplTable.setStatus("current")
_CfprVnicFcGroupTemplEntry_Object = MibTableRow
cfprVnicFcGroupTemplEntry = _CfprVnicFcGroupTemplEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 16, 1)
)
cfprVnicFcGroupTemplEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicFcGroupTemplInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicFcGroupTemplEntry.setStatus("current")
_CfprVnicFcGroupTemplInstanceId_Type = CfprManagedObjectId
_CfprVnicFcGroupTemplInstanceId_Object = MibTableColumn
cfprVnicFcGroupTemplInstanceId = _CfprVnicFcGroupTemplInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 16, 1, 1),
    _CfprVnicFcGroupTemplInstanceId_Type()
)
cfprVnicFcGroupTemplInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicFcGroupTemplInstanceId.setStatus("current")
_CfprVnicFcGroupTemplDn_Type = CfprManagedObjectDn
_CfprVnicFcGroupTemplDn_Object = MibTableColumn
cfprVnicFcGroupTemplDn = _CfprVnicFcGroupTemplDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 16, 1, 2),
    _CfprVnicFcGroupTemplDn_Type()
)
cfprVnicFcGroupTemplDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcGroupTemplDn.setStatus("current")
_CfprVnicFcGroupTemplRn_Type = SnmpAdminString
_CfprVnicFcGroupTemplRn_Object = MibTableColumn
cfprVnicFcGroupTemplRn = _CfprVnicFcGroupTemplRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 16, 1, 3),
    _CfprVnicFcGroupTemplRn_Type()
)
cfprVnicFcGroupTemplRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcGroupTemplRn.setStatus("current")
_CfprVnicFcGroupTemplAdaptorProfileName_Type = SnmpAdminString
_CfprVnicFcGroupTemplAdaptorProfileName_Object = MibTableColumn
cfprVnicFcGroupTemplAdaptorProfileName = _CfprVnicFcGroupTemplAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 16, 1, 4),
    _CfprVnicFcGroupTemplAdaptorProfileName_Type()
)
cfprVnicFcGroupTemplAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcGroupTemplAdaptorProfileName.setStatus("current")
_CfprVnicFcGroupTemplDescr_Type = SnmpAdminString
_CfprVnicFcGroupTemplDescr_Object = MibTableColumn
cfprVnicFcGroupTemplDescr = _CfprVnicFcGroupTemplDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 16, 1, 5),
    _CfprVnicFcGroupTemplDescr_Type()
)
cfprVnicFcGroupTemplDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcGroupTemplDescr.setStatus("current")
_CfprVnicFcGroupTemplIdentPoolName_Type = SnmpAdminString
_CfprVnicFcGroupTemplIdentPoolName_Object = MibTableColumn
cfprVnicFcGroupTemplIdentPoolName = _CfprVnicFcGroupTemplIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 16, 1, 6),
    _CfprVnicFcGroupTemplIdentPoolName_Type()
)
cfprVnicFcGroupTemplIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcGroupTemplIdentPoolName.setStatus("current")
_CfprVnicFcGroupTemplIntId_Type = SnmpAdminString
_CfprVnicFcGroupTemplIntId_Object = MibTableColumn
cfprVnicFcGroupTemplIntId = _CfprVnicFcGroupTemplIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 16, 1, 7),
    _CfprVnicFcGroupTemplIntId_Type()
)
cfprVnicFcGroupTemplIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcGroupTemplIntId.setStatus("current")
_CfprVnicFcGroupTemplMaxDataFieldSize_Type = Gauge32
_CfprVnicFcGroupTemplMaxDataFieldSize_Object = MibTableColumn
cfprVnicFcGroupTemplMaxDataFieldSize = _CfprVnicFcGroupTemplMaxDataFieldSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 16, 1, 8),
    _CfprVnicFcGroupTemplMaxDataFieldSize_Type()
)
cfprVnicFcGroupTemplMaxDataFieldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcGroupTemplMaxDataFieldSize.setStatus("current")
_CfprVnicFcGroupTemplName_Type = SnmpAdminString
_CfprVnicFcGroupTemplName_Object = MibTableColumn
cfprVnicFcGroupTemplName = _CfprVnicFcGroupTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 16, 1, 9),
    _CfprVnicFcGroupTemplName_Type()
)
cfprVnicFcGroupTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcGroupTemplName.setStatus("current")
_CfprVnicFcGroupTemplNwTemplName_Type = SnmpAdminString
_CfprVnicFcGroupTemplNwTemplName_Object = MibTableColumn
cfprVnicFcGroupTemplNwTemplName = _CfprVnicFcGroupTemplNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 16, 1, 10),
    _CfprVnicFcGroupTemplNwTemplName_Type()
)
cfprVnicFcGroupTemplNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcGroupTemplNwTemplName.setStatus("current")
_CfprVnicFcGroupTemplOperStatsPolicyName_Type = SnmpAdminString
_CfprVnicFcGroupTemplOperStatsPolicyName_Object = MibTableColumn
cfprVnicFcGroupTemplOperStatsPolicyName = _CfprVnicFcGroupTemplOperStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 16, 1, 11),
    _CfprVnicFcGroupTemplOperStatsPolicyName_Type()
)
cfprVnicFcGroupTemplOperStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcGroupTemplOperStatsPolicyName.setStatus("current")
_CfprVnicFcGroupTemplOperStorageConnPolicyName_Type = SnmpAdminString
_CfprVnicFcGroupTemplOperStorageConnPolicyName_Object = MibTableColumn
cfprVnicFcGroupTemplOperStorageConnPolicyName = _CfprVnicFcGroupTemplOperStorageConnPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 16, 1, 12),
    _CfprVnicFcGroupTemplOperStorageConnPolicyName_Type()
)
cfprVnicFcGroupTemplOperStorageConnPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcGroupTemplOperStorageConnPolicyName.setStatus("current")
_CfprVnicFcGroupTemplPolicyLevel_Type = Gauge32
_CfprVnicFcGroupTemplPolicyLevel_Object = MibTableColumn
cfprVnicFcGroupTemplPolicyLevel = _CfprVnicFcGroupTemplPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 16, 1, 13),
    _CfprVnicFcGroupTemplPolicyLevel_Type()
)
cfprVnicFcGroupTemplPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcGroupTemplPolicyLevel.setStatus("current")
_CfprVnicFcGroupTemplPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprVnicFcGroupTemplPolicyOwner_Object = MibTableColumn
cfprVnicFcGroupTemplPolicyOwner = _CfprVnicFcGroupTemplPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 16, 1, 14),
    _CfprVnicFcGroupTemplPolicyOwner_Type()
)
cfprVnicFcGroupTemplPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcGroupTemplPolicyOwner.setStatus("current")
_CfprVnicFcGroupTemplQosPolicyName_Type = SnmpAdminString
_CfprVnicFcGroupTemplQosPolicyName_Object = MibTableColumn
cfprVnicFcGroupTemplQosPolicyName = _CfprVnicFcGroupTemplQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 16, 1, 15),
    _CfprVnicFcGroupTemplQosPolicyName_Type()
)
cfprVnicFcGroupTemplQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcGroupTemplQosPolicyName.setStatus("current")
_CfprVnicFcGroupTemplStatsPolicyName_Type = SnmpAdminString
_CfprVnicFcGroupTemplStatsPolicyName_Object = MibTableColumn
cfprVnicFcGroupTemplStatsPolicyName = _CfprVnicFcGroupTemplStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 16, 1, 16),
    _CfprVnicFcGroupTemplStatsPolicyName_Type()
)
cfprVnicFcGroupTemplStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcGroupTemplStatsPolicyName.setStatus("current")
_CfprVnicFcGroupTemplStorageConnPolicyName_Type = SnmpAdminString
_CfprVnicFcGroupTemplStorageConnPolicyName_Object = MibTableColumn
cfprVnicFcGroupTemplStorageConnPolicyName = _CfprVnicFcGroupTemplStorageConnPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 16, 1, 17),
    _CfprVnicFcGroupTemplStorageConnPolicyName_Type()
)
cfprVnicFcGroupTemplStorageConnPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcGroupTemplStorageConnPolicyName.setStatus("current")
_CfprVnicFcGroupTemplTemplType_Type = CfprVnicTemplateType
_CfprVnicFcGroupTemplTemplType_Object = MibTableColumn
cfprVnicFcGroupTemplTemplType = _CfprVnicFcGroupTemplTemplType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 16, 1, 18),
    _CfprVnicFcGroupTemplTemplType_Type()
)
cfprVnicFcGroupTemplTemplType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcGroupTemplTemplType.setStatus("current")
_CfprVnicFcIfTable_Object = MibTable
cfprVnicFcIfTable = _CfprVnicFcIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 17)
)
if mibBuilder.loadTexts:
    cfprVnicFcIfTable.setStatus("current")
_CfprVnicFcIfEntry_Object = MibTableRow
cfprVnicFcIfEntry = _CfprVnicFcIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 17, 1)
)
cfprVnicFcIfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicFcIfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicFcIfEntry.setStatus("current")
_CfprVnicFcIfInstanceId_Type = CfprManagedObjectId
_CfprVnicFcIfInstanceId_Object = MibTableColumn
cfprVnicFcIfInstanceId = _CfprVnicFcIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 17, 1, 1),
    _CfprVnicFcIfInstanceId_Type()
)
cfprVnicFcIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicFcIfInstanceId.setStatus("current")
_CfprVnicFcIfDn_Type = CfprManagedObjectDn
_CfprVnicFcIfDn_Object = MibTableColumn
cfprVnicFcIfDn = _CfprVnicFcIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 17, 1, 2),
    _CfprVnicFcIfDn_Type()
)
cfprVnicFcIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcIfDn.setStatus("current")
_CfprVnicFcIfRn_Type = SnmpAdminString
_CfprVnicFcIfRn_Object = MibTableColumn
cfprVnicFcIfRn = _CfprVnicFcIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 17, 1, 3),
    _CfprVnicFcIfRn_Type()
)
cfprVnicFcIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcIfRn.setStatus("current")
_CfprVnicFcIfConfigQualifier_Type = CfprVnicConfigIssues
_CfprVnicFcIfConfigQualifier_Object = MibTableColumn
cfprVnicFcIfConfigQualifier = _CfprVnicFcIfConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 17, 1, 4),
    _CfprVnicFcIfConfigQualifier_Type()
)
cfprVnicFcIfConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcIfConfigQualifier.setStatus("current")
_CfprVnicFcIfInitiator_Type = Unsigned64
_CfprVnicFcIfInitiator_Object = MibTableColumn
cfprVnicFcIfInitiator = _CfprVnicFcIfInitiator_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 17, 1, 5),
    _CfprVnicFcIfInitiator_Type()
)
cfprVnicFcIfInitiator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcIfInitiator.setStatus("current")
_CfprVnicFcIfName_Type = SnmpAdminString
_CfprVnicFcIfName_Object = MibTableColumn
cfprVnicFcIfName = _CfprVnicFcIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 17, 1, 6),
    _CfprVnicFcIfName_Type()
)
cfprVnicFcIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcIfName.setStatus("current")
_CfprVnicFcIfOperState_Type = CfprVnicIfOperState
_CfprVnicFcIfOperState_Object = MibTableColumn
cfprVnicFcIfOperState = _CfprVnicFcIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 17, 1, 7),
    _CfprVnicFcIfOperState_Type()
)
cfprVnicFcIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcIfOperState.setStatus("current")
_CfprVnicFcIfOperVnetDn_Type = SnmpAdminString
_CfprVnicFcIfOperVnetDn_Object = MibTableColumn
cfprVnicFcIfOperVnetDn = _CfprVnicFcIfOperVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 17, 1, 8),
    _CfprVnicFcIfOperVnetDn_Type()
)
cfprVnicFcIfOperVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcIfOperVnetDn.setStatus("current")
_CfprVnicFcIfOperVnetName_Type = SnmpAdminString
_CfprVnicFcIfOperVnetName_Object = MibTableColumn
cfprVnicFcIfOperVnetName = _CfprVnicFcIfOperVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 17, 1, 9),
    _CfprVnicFcIfOperVnetName_Type()
)
cfprVnicFcIfOperVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcIfOperVnetName.setStatus("current")
_CfprVnicFcIfOwner_Type = CfprVnicConnectionOwner
_CfprVnicFcIfOwner_Object = MibTableColumn
cfprVnicFcIfOwner = _CfprVnicFcIfOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 17, 1, 10),
    _CfprVnicFcIfOwner_Type()
)
cfprVnicFcIfOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcIfOwner.setStatus("current")
_CfprVnicFcIfPubNwId_Type = Gauge32
_CfprVnicFcIfPubNwId_Object = MibTableColumn
cfprVnicFcIfPubNwId = _CfprVnicFcIfPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 17, 1, 11),
    _CfprVnicFcIfPubNwId_Type()
)
cfprVnicFcIfPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcIfPubNwId.setStatus("current")
_CfprVnicFcIfSharing_Type = CfprFabricVlanSharingType
_CfprVnicFcIfSharing_Object = MibTableColumn
cfprVnicFcIfSharing = _CfprVnicFcIfSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 17, 1, 12),
    _CfprVnicFcIfSharing_Type()
)
cfprVnicFcIfSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcIfSharing.setStatus("current")
_CfprVnicFcIfSwitchId_Type = CfprVnicL2IfSwitchId
_CfprVnicFcIfSwitchId_Object = MibTableColumn
cfprVnicFcIfSwitchId = _CfprVnicFcIfSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 17, 1, 13),
    _CfprVnicFcIfSwitchId_Type()
)
cfprVnicFcIfSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcIfSwitchId.setStatus("current")
_CfprVnicFcIfType_Type = CfprVnicAFcIfType
_CfprVnicFcIfType_Object = MibTableColumn
cfprVnicFcIfType = _CfprVnicFcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 17, 1, 14),
    _CfprVnicFcIfType_Type()
)
cfprVnicFcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcIfType.setStatus("current")
_CfprVnicFcIfVnet_Type = Gauge32
_CfprVnicFcIfVnet_Object = MibTableColumn
cfprVnicFcIfVnet = _CfprVnicFcIfVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 17, 1, 15),
    _CfprVnicFcIfVnet_Type()
)
cfprVnicFcIfVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcIfVnet.setStatus("current")
_CfprVnicFcLifTable_Object = MibTable
cfprVnicFcLifTable = _CfprVnicFcLifTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 18)
)
if mibBuilder.loadTexts:
    cfprVnicFcLifTable.setStatus("current")
_CfprVnicFcLifEntry_Object = MibTableRow
cfprVnicFcLifEntry = _CfprVnicFcLifEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 18, 1)
)
cfprVnicFcLifEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicFcLifInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicFcLifEntry.setStatus("current")
_CfprVnicFcLifInstanceId_Type = CfprManagedObjectId
_CfprVnicFcLifInstanceId_Object = MibTableColumn
cfprVnicFcLifInstanceId = _CfprVnicFcLifInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 18, 1, 1),
    _CfprVnicFcLifInstanceId_Type()
)
cfprVnicFcLifInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicFcLifInstanceId.setStatus("current")
_CfprVnicFcLifDn_Type = CfprManagedObjectDn
_CfprVnicFcLifDn_Object = MibTableColumn
cfprVnicFcLifDn = _CfprVnicFcLifDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 18, 1, 2),
    _CfprVnicFcLifDn_Type()
)
cfprVnicFcLifDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcLifDn.setStatus("current")
_CfprVnicFcLifRn_Type = SnmpAdminString
_CfprVnicFcLifRn_Object = MibTableColumn
cfprVnicFcLifRn = _CfprVnicFcLifRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 18, 1, 3),
    _CfprVnicFcLifRn_Type()
)
cfprVnicFcLifRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcLifRn.setStatus("current")
_CfprVnicFcLifAddr_Type = Unsigned64
_CfprVnicFcLifAddr_Object = MibTableColumn
cfprVnicFcLifAddr = _CfprVnicFcLifAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 18, 1, 4),
    _CfprVnicFcLifAddr_Type()
)
cfprVnicFcLifAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcLifAddr.setStatus("current")
_CfprVnicFcLifName_Type = SnmpAdminString
_CfprVnicFcLifName_Object = MibTableColumn
cfprVnicFcLifName = _CfprVnicFcLifName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 18, 1, 5),
    _CfprVnicFcLifName_Type()
)
cfprVnicFcLifName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcLifName.setStatus("current")
_CfprVnicFcLifNicDn_Type = SnmpAdminString
_CfprVnicFcLifNicDn_Object = MibTableColumn
cfprVnicFcLifNicDn = _CfprVnicFcLifNicDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 18, 1, 6),
    _CfprVnicFcLifNicDn_Type()
)
cfprVnicFcLifNicDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcLifNicDn.setStatus("current")
_CfprVnicFcLifOwner_Type = CfprVnicConnectionOwner
_CfprVnicFcLifOwner_Object = MibTableColumn
cfprVnicFcLifOwner = _CfprVnicFcLifOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 18, 1, 7),
    _CfprVnicFcLifOwner_Type()
)
cfprVnicFcLifOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcLifOwner.setStatus("current")
_CfprVnicFcLifSwitchId_Type = CfprNetworkSwitchId
_CfprVnicFcLifSwitchId_Object = MibTableColumn
cfprVnicFcLifSwitchId = _CfprVnicFcLifSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 18, 1, 8),
    _CfprVnicFcLifSwitchId_Type()
)
cfprVnicFcLifSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcLifSwitchId.setStatus("current")
_CfprVnicFcLifType_Type = CfprVnicConnectionType
_CfprVnicFcLifType_Object = MibTableColumn
cfprVnicFcLifType = _CfprVnicFcLifType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 18, 1, 9),
    _CfprVnicFcLifType_Type()
)
cfprVnicFcLifType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcLifType.setStatus("current")
_CfprVnicFcLifVnicDn_Type = SnmpAdminString
_CfprVnicFcLifVnicDn_Object = MibTableColumn
cfprVnicFcLifVnicDn = _CfprVnicFcLifVnicDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 18, 1, 10),
    _CfprVnicFcLifVnicDn_Type()
)
cfprVnicFcLifVnicDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcLifVnicDn.setStatus("current")
_CfprVnicFcNodeTable_Object = MibTable
cfprVnicFcNodeTable = _CfprVnicFcNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 19)
)
if mibBuilder.loadTexts:
    cfprVnicFcNodeTable.setStatus("current")
_CfprVnicFcNodeEntry_Object = MibTableRow
cfprVnicFcNodeEntry = _CfprVnicFcNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 19, 1)
)
cfprVnicFcNodeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicFcNodeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicFcNodeEntry.setStatus("current")
_CfprVnicFcNodeInstanceId_Type = CfprManagedObjectId
_CfprVnicFcNodeInstanceId_Object = MibTableColumn
cfprVnicFcNodeInstanceId = _CfprVnicFcNodeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 19, 1, 1),
    _CfprVnicFcNodeInstanceId_Type()
)
cfprVnicFcNodeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicFcNodeInstanceId.setStatus("current")
_CfprVnicFcNodeDn_Type = CfprManagedObjectDn
_CfprVnicFcNodeDn_Object = MibTableColumn
cfprVnicFcNodeDn = _CfprVnicFcNodeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 19, 1, 2),
    _CfprVnicFcNodeDn_Type()
)
cfprVnicFcNodeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcNodeDn.setStatus("current")
_CfprVnicFcNodeRn_Type = SnmpAdminString
_CfprVnicFcNodeRn_Object = MibTableColumn
cfprVnicFcNodeRn = _CfprVnicFcNodeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 19, 1, 3),
    _CfprVnicFcNodeRn_Type()
)
cfprVnicFcNodeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcNodeRn.setStatus("current")
_CfprVnicFcNodeAddrData_Type = Unsigned64
_CfprVnicFcNodeAddrData_Object = MibTableColumn
cfprVnicFcNodeAddrData = _CfprVnicFcNodeAddrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 19, 1, 4),
    _CfprVnicFcNodeAddrData_Type()
)
cfprVnicFcNodeAddrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcNodeAddrData.setStatus("current")
_CfprVnicFcNodeFltAggr_Type = Unsigned64
_CfprVnicFcNodeFltAggr_Object = MibTableColumn
cfprVnicFcNodeFltAggr = _CfprVnicFcNodeFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 19, 1, 5),
    _CfprVnicFcNodeFltAggr_Type()
)
cfprVnicFcNodeFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcNodeFltAggr.setStatus("current")
_CfprVnicFcNodeIdentPoolName_Type = SnmpAdminString
_CfprVnicFcNodeIdentPoolName_Object = MibTableColumn
cfprVnicFcNodeIdentPoolName = _CfprVnicFcNodeIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 19, 1, 6),
    _CfprVnicFcNodeIdentPoolName_Type()
)
cfprVnicFcNodeIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcNodeIdentPoolName.setStatus("current")
_CfprVnicFcNodeMaxDerivableWWPN_Type = Gauge32
_CfprVnicFcNodeMaxDerivableWWPN_Object = MibTableColumn
cfprVnicFcNodeMaxDerivableWWPN = _CfprVnicFcNodeMaxDerivableWWPN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 19, 1, 7),
    _CfprVnicFcNodeMaxDerivableWWPN_Type()
)
cfprVnicFcNodeMaxDerivableWWPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcNodeMaxDerivableWWPN.setStatus("current")
_CfprVnicFcNodeOperIdentPoolName_Type = SnmpAdminString
_CfprVnicFcNodeOperIdentPoolName_Object = MibTableColumn
cfprVnicFcNodeOperIdentPoolName = _CfprVnicFcNodeOperIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 19, 1, 8),
    _CfprVnicFcNodeOperIdentPoolName_Type()
)
cfprVnicFcNodeOperIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcNodeOperIdentPoolName.setStatus("current")
_CfprVnicFcNodeOwner_Type = CfprVnicFcNodeOwner
_CfprVnicFcNodeOwner_Object = MibTableColumn
cfprVnicFcNodeOwner = _CfprVnicFcNodeOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 19, 1, 9),
    _CfprVnicFcNodeOwner_Type()
)
cfprVnicFcNodeOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcNodeOwner.setStatus("current")
_CfprVnicFcOEIfTable_Object = MibTable
cfprVnicFcOEIfTable = _CfprVnicFcOEIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 20)
)
if mibBuilder.loadTexts:
    cfprVnicFcOEIfTable.setStatus("current")
_CfprVnicFcOEIfEntry_Object = MibTableRow
cfprVnicFcOEIfEntry = _CfprVnicFcOEIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 20, 1)
)
cfprVnicFcOEIfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicFcOEIfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicFcOEIfEntry.setStatus("current")
_CfprVnicFcOEIfInstanceId_Type = CfprManagedObjectId
_CfprVnicFcOEIfInstanceId_Object = MibTableColumn
cfprVnicFcOEIfInstanceId = _CfprVnicFcOEIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 20, 1, 1),
    _CfprVnicFcOEIfInstanceId_Type()
)
cfprVnicFcOEIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicFcOEIfInstanceId.setStatus("current")
_CfprVnicFcOEIfDn_Type = CfprManagedObjectDn
_CfprVnicFcOEIfDn_Object = MibTableColumn
cfprVnicFcOEIfDn = _CfprVnicFcOEIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 20, 1, 2),
    _CfprVnicFcOEIfDn_Type()
)
cfprVnicFcOEIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcOEIfDn.setStatus("current")
_CfprVnicFcOEIfRn_Type = SnmpAdminString
_CfprVnicFcOEIfRn_Object = MibTableColumn
cfprVnicFcOEIfRn = _CfprVnicFcOEIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 20, 1, 3),
    _CfprVnicFcOEIfRn_Type()
)
cfprVnicFcOEIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcOEIfRn.setStatus("current")
_CfprVnicFcOEIfConfigQualifier_Type = CfprVnicConfigIssues
_CfprVnicFcOEIfConfigQualifier_Object = MibTableColumn
cfprVnicFcOEIfConfigQualifier = _CfprVnicFcOEIfConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 20, 1, 4),
    _CfprVnicFcOEIfConfigQualifier_Type()
)
cfprVnicFcOEIfConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcOEIfConfigQualifier.setStatus("current")
_CfprVnicFcOEIfInitiator_Type = Unsigned64
_CfprVnicFcOEIfInitiator_Object = MibTableColumn
cfprVnicFcOEIfInitiator = _CfprVnicFcOEIfInitiator_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 20, 1, 5),
    _CfprVnicFcOEIfInitiator_Type()
)
cfprVnicFcOEIfInitiator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcOEIfInitiator.setStatus("current")
_CfprVnicFcOEIfName_Type = SnmpAdminString
_CfprVnicFcOEIfName_Object = MibTableColumn
cfprVnicFcOEIfName = _CfprVnicFcOEIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 20, 1, 6),
    _CfprVnicFcOEIfName_Type()
)
cfprVnicFcOEIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcOEIfName.setStatus("current")
_CfprVnicFcOEIfOperState_Type = CfprVnicIfOperState
_CfprVnicFcOEIfOperState_Object = MibTableColumn
cfprVnicFcOEIfOperState = _CfprVnicFcOEIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 20, 1, 7),
    _CfprVnicFcOEIfOperState_Type()
)
cfprVnicFcOEIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcOEIfOperState.setStatus("current")
_CfprVnicFcOEIfOperVnetDn_Type = SnmpAdminString
_CfprVnicFcOEIfOperVnetDn_Object = MibTableColumn
cfprVnicFcOEIfOperVnetDn = _CfprVnicFcOEIfOperVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 20, 1, 8),
    _CfprVnicFcOEIfOperVnetDn_Type()
)
cfprVnicFcOEIfOperVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcOEIfOperVnetDn.setStatus("current")
_CfprVnicFcOEIfOperVnetName_Type = SnmpAdminString
_CfprVnicFcOEIfOperVnetName_Object = MibTableColumn
cfprVnicFcOEIfOperVnetName = _CfprVnicFcOEIfOperVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 20, 1, 9),
    _CfprVnicFcOEIfOperVnetName_Type()
)
cfprVnicFcOEIfOperVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcOEIfOperVnetName.setStatus("current")
_CfprVnicFcOEIfOwner_Type = CfprVnicConnectionOwner
_CfprVnicFcOEIfOwner_Object = MibTableColumn
cfprVnicFcOEIfOwner = _CfprVnicFcOEIfOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 20, 1, 10),
    _CfprVnicFcOEIfOwner_Type()
)
cfprVnicFcOEIfOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcOEIfOwner.setStatus("current")
_CfprVnicFcOEIfPubNwId_Type = Gauge32
_CfprVnicFcOEIfPubNwId_Object = MibTableColumn
cfprVnicFcOEIfPubNwId = _CfprVnicFcOEIfPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 20, 1, 11),
    _CfprVnicFcOEIfPubNwId_Type()
)
cfprVnicFcOEIfPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcOEIfPubNwId.setStatus("current")
_CfprVnicFcOEIfSharing_Type = CfprFabricVlanSharingType
_CfprVnicFcOEIfSharing_Object = MibTableColumn
cfprVnicFcOEIfSharing = _CfprVnicFcOEIfSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 20, 1, 12),
    _CfprVnicFcOEIfSharing_Type()
)
cfprVnicFcOEIfSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcOEIfSharing.setStatus("current")
_CfprVnicFcOEIfSwitchId_Type = CfprVnicL2IfSwitchId
_CfprVnicFcOEIfSwitchId_Object = MibTableColumn
cfprVnicFcOEIfSwitchId = _CfprVnicFcOEIfSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 20, 1, 13),
    _CfprVnicFcOEIfSwitchId_Type()
)
cfprVnicFcOEIfSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcOEIfSwitchId.setStatus("current")
_CfprVnicFcOEIfType_Type = CfprVnicAFcIfType
_CfprVnicFcOEIfType_Object = MibTableColumn
cfprVnicFcOEIfType = _CfprVnicFcOEIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 20, 1, 14),
    _CfprVnicFcOEIfType_Type()
)
cfprVnicFcOEIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcOEIfType.setStatus("current")
_CfprVnicFcOEIfVnet_Type = Gauge32
_CfprVnicFcOEIfVnet_Object = MibTableColumn
cfprVnicFcOEIfVnet = _CfprVnicFcOEIfVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 20, 1, 15),
    _CfprVnicFcOEIfVnet_Type()
)
cfprVnicFcOEIfVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicFcOEIfVnet.setStatus("current")
_CfprVnicIPv4DhcpTable_Object = MibTable
cfprVnicIPv4DhcpTable = _CfprVnicIPv4DhcpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 21)
)
if mibBuilder.loadTexts:
    cfprVnicIPv4DhcpTable.setStatus("current")
_CfprVnicIPv4DhcpEntry_Object = MibTableRow
cfprVnicIPv4DhcpEntry = _CfprVnicIPv4DhcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 21, 1)
)
cfprVnicIPv4DhcpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicIPv4DhcpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicIPv4DhcpEntry.setStatus("current")
_CfprVnicIPv4DhcpInstanceId_Type = CfprManagedObjectId
_CfprVnicIPv4DhcpInstanceId_Object = MibTableColumn
cfprVnicIPv4DhcpInstanceId = _CfprVnicIPv4DhcpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 21, 1, 1),
    _CfprVnicIPv4DhcpInstanceId_Type()
)
cfprVnicIPv4DhcpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicIPv4DhcpInstanceId.setStatus("current")
_CfprVnicIPv4DhcpDn_Type = CfprManagedObjectDn
_CfprVnicIPv4DhcpDn_Object = MibTableColumn
cfprVnicIPv4DhcpDn = _CfprVnicIPv4DhcpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 21, 1, 2),
    _CfprVnicIPv4DhcpDn_Type()
)
cfprVnicIPv4DhcpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4DhcpDn.setStatus("current")
_CfprVnicIPv4DhcpRn_Type = SnmpAdminString
_CfprVnicIPv4DhcpRn_Object = MibTableColumn
cfprVnicIPv4DhcpRn = _CfprVnicIPv4DhcpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 21, 1, 3),
    _CfprVnicIPv4DhcpRn_Type()
)
cfprVnicIPv4DhcpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4DhcpRn.setStatus("current")
_CfprVnicIPv4DhcpAddr_Type = InetAddressIPv4
_CfprVnicIPv4DhcpAddr_Object = MibTableColumn
cfprVnicIPv4DhcpAddr = _CfprVnicIPv4DhcpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 21, 1, 4),
    _CfprVnicIPv4DhcpAddr_Type()
)
cfprVnicIPv4DhcpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4DhcpAddr.setStatus("current")
_CfprVnicIPv4DhcpDefGw_Type = InetAddressIPv4
_CfprVnicIPv4DhcpDefGw_Object = MibTableColumn
cfprVnicIPv4DhcpDefGw = _CfprVnicIPv4DhcpDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 21, 1, 5),
    _CfprVnicIPv4DhcpDefGw_Type()
)
cfprVnicIPv4DhcpDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4DhcpDefGw.setStatus("current")
_CfprVnicIPv4DhcpSubnet_Type = InetAddressIPv4
_CfprVnicIPv4DhcpSubnet_Object = MibTableColumn
cfprVnicIPv4DhcpSubnet = _CfprVnicIPv4DhcpSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 21, 1, 6),
    _CfprVnicIPv4DhcpSubnet_Type()
)
cfprVnicIPv4DhcpSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4DhcpSubnet.setStatus("current")
_CfprVnicIPv4DnsTable_Object = MibTable
cfprVnicIPv4DnsTable = _CfprVnicIPv4DnsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 22)
)
if mibBuilder.loadTexts:
    cfprVnicIPv4DnsTable.setStatus("current")
_CfprVnicIPv4DnsEntry_Object = MibTableRow
cfprVnicIPv4DnsEntry = _CfprVnicIPv4DnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 22, 1)
)
cfprVnicIPv4DnsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicIPv4DnsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicIPv4DnsEntry.setStatus("current")
_CfprVnicIPv4DnsInstanceId_Type = CfprManagedObjectId
_CfprVnicIPv4DnsInstanceId_Object = MibTableColumn
cfprVnicIPv4DnsInstanceId = _CfprVnicIPv4DnsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 22, 1, 1),
    _CfprVnicIPv4DnsInstanceId_Type()
)
cfprVnicIPv4DnsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicIPv4DnsInstanceId.setStatus("current")
_CfprVnicIPv4DnsDn_Type = CfprManagedObjectDn
_CfprVnicIPv4DnsDn_Object = MibTableColumn
cfprVnicIPv4DnsDn = _CfprVnicIPv4DnsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 22, 1, 2),
    _CfprVnicIPv4DnsDn_Type()
)
cfprVnicIPv4DnsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4DnsDn.setStatus("current")
_CfprVnicIPv4DnsRn_Type = SnmpAdminString
_CfprVnicIPv4DnsRn_Object = MibTableColumn
cfprVnicIPv4DnsRn = _CfprVnicIPv4DnsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 22, 1, 3),
    _CfprVnicIPv4DnsRn_Type()
)
cfprVnicIPv4DnsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4DnsRn.setStatus("current")
_CfprVnicIPv4DnsAddr_Type = InetAddressIPv4
_CfprVnicIPv4DnsAddr_Object = MibTableColumn
cfprVnicIPv4DnsAddr = _CfprVnicIPv4DnsAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 22, 1, 4),
    _CfprVnicIPv4DnsAddr_Type()
)
cfprVnicIPv4DnsAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4DnsAddr.setStatus("current")
_CfprVnicIPv4DnsDefGw_Type = InetAddressIPv4
_CfprVnicIPv4DnsDefGw_Object = MibTableColumn
cfprVnicIPv4DnsDefGw = _CfprVnicIPv4DnsDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 22, 1, 5),
    _CfprVnicIPv4DnsDefGw_Type()
)
cfprVnicIPv4DnsDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4DnsDefGw.setStatus("current")
_CfprVnicIPv4DnsPref_Type = CfprVnicIPv4DnsPref
_CfprVnicIPv4DnsPref_Object = MibTableColumn
cfprVnicIPv4DnsPref = _CfprVnicIPv4DnsPref_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 22, 1, 6),
    _CfprVnicIPv4DnsPref_Type()
)
cfprVnicIPv4DnsPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4DnsPref.setStatus("current")
_CfprVnicIPv4DnsSubnet_Type = InetAddressIPv4
_CfprVnicIPv4DnsSubnet_Object = MibTableColumn
cfprVnicIPv4DnsSubnet = _CfprVnicIPv4DnsSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 22, 1, 7),
    _CfprVnicIPv4DnsSubnet_Type()
)
cfprVnicIPv4DnsSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4DnsSubnet.setStatus("current")
_CfprVnicIPv4IfTable_Object = MibTable
cfprVnicIPv4IfTable = _CfprVnicIPv4IfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 23)
)
if mibBuilder.loadTexts:
    cfprVnicIPv4IfTable.setStatus("current")
_CfprVnicIPv4IfEntry_Object = MibTableRow
cfprVnicIPv4IfEntry = _CfprVnicIPv4IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 23, 1)
)
cfprVnicIPv4IfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicIPv4IfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicIPv4IfEntry.setStatus("current")
_CfprVnicIPv4IfInstanceId_Type = CfprManagedObjectId
_CfprVnicIPv4IfInstanceId_Object = MibTableColumn
cfprVnicIPv4IfInstanceId = _CfprVnicIPv4IfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 23, 1, 1),
    _CfprVnicIPv4IfInstanceId_Type()
)
cfprVnicIPv4IfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicIPv4IfInstanceId.setStatus("current")
_CfprVnicIPv4IfDn_Type = CfprManagedObjectDn
_CfprVnicIPv4IfDn_Object = MibTableColumn
cfprVnicIPv4IfDn = _CfprVnicIPv4IfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 23, 1, 2),
    _CfprVnicIPv4IfDn_Type()
)
cfprVnicIPv4IfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4IfDn.setStatus("current")
_CfprVnicIPv4IfRn_Type = SnmpAdminString
_CfprVnicIPv4IfRn_Object = MibTableColumn
cfprVnicIPv4IfRn = _CfprVnicIPv4IfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 23, 1, 3),
    _CfprVnicIPv4IfRn_Type()
)
cfprVnicIPv4IfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4IfRn.setStatus("current")
_CfprVnicIPv4IfAddr_Type = InetAddressIPv4
_CfprVnicIPv4IfAddr_Object = MibTableColumn
cfprVnicIPv4IfAddr = _CfprVnicIPv4IfAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 23, 1, 4),
    _CfprVnicIPv4IfAddr_Type()
)
cfprVnicIPv4IfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4IfAddr.setStatus("current")
_CfprVnicIPv4IfConfigQualifier_Type = CfprVnicConfigIssues
_CfprVnicIPv4IfConfigQualifier_Object = MibTableColumn
cfprVnicIPv4IfConfigQualifier = _CfprVnicIPv4IfConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 23, 1, 5),
    _CfprVnicIPv4IfConfigQualifier_Type()
)
cfprVnicIPv4IfConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4IfConfigQualifier.setStatus("current")
_CfprVnicIPv4IfName_Type = SnmpAdminString
_CfprVnicIPv4IfName_Object = MibTableColumn
cfprVnicIPv4IfName = _CfprVnicIPv4IfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 23, 1, 6),
    _CfprVnicIPv4IfName_Type()
)
cfprVnicIPv4IfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4IfName.setStatus("current")
_CfprVnicIPv4IfOperState_Type = CfprVnicIfOperState
_CfprVnicIPv4IfOperState_Object = MibTableColumn
cfprVnicIPv4IfOperState = _CfprVnicIPv4IfOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 23, 1, 7),
    _CfprVnicIPv4IfOperState_Type()
)
cfprVnicIPv4IfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4IfOperState.setStatus("current")
_CfprVnicIPv4IfOperVnetDn_Type = SnmpAdminString
_CfprVnicIPv4IfOperVnetDn_Object = MibTableColumn
cfprVnicIPv4IfOperVnetDn = _CfprVnicIPv4IfOperVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 23, 1, 8),
    _CfprVnicIPv4IfOperVnetDn_Type()
)
cfprVnicIPv4IfOperVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4IfOperVnetDn.setStatus("current")
_CfprVnicIPv4IfOperVnetName_Type = SnmpAdminString
_CfprVnicIPv4IfOperVnetName_Object = MibTableColumn
cfprVnicIPv4IfOperVnetName = _CfprVnicIPv4IfOperVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 23, 1, 9),
    _CfprVnicIPv4IfOperVnetName_Type()
)
cfprVnicIPv4IfOperVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4IfOperVnetName.setStatus("current")
_CfprVnicIPv4IfOwner_Type = CfprVnicConnectionOwner
_CfprVnicIPv4IfOwner_Object = MibTableColumn
cfprVnicIPv4IfOwner = _CfprVnicIPv4IfOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 23, 1, 10),
    _CfprVnicIPv4IfOwner_Type()
)
cfprVnicIPv4IfOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4IfOwner.setStatus("current")
_CfprVnicIPv4IfPubNwId_Type = Gauge32
_CfprVnicIPv4IfPubNwId_Object = MibTableColumn
cfprVnicIPv4IfPubNwId = _CfprVnicIPv4IfPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 23, 1, 11),
    _CfprVnicIPv4IfPubNwId_Type()
)
cfprVnicIPv4IfPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4IfPubNwId.setStatus("current")
_CfprVnicIPv4IfSharing_Type = CfprFabricVlanSharingType
_CfprVnicIPv4IfSharing_Object = MibTableColumn
cfprVnicIPv4IfSharing = _CfprVnicIPv4IfSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 23, 1, 12),
    _CfprVnicIPv4IfSharing_Type()
)
cfprVnicIPv4IfSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4IfSharing.setStatus("current")
_CfprVnicIPv4IfSwitchId_Type = CfprNetworkSwitchId
_CfprVnicIPv4IfSwitchId_Object = MibTableColumn
cfprVnicIPv4IfSwitchId = _CfprVnicIPv4IfSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 23, 1, 13),
    _CfprVnicIPv4IfSwitchId_Type()
)
cfprVnicIPv4IfSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4IfSwitchId.setStatus("current")
_CfprVnicIPv4IfType_Type = CfprVnicConnectionType
_CfprVnicIPv4IfType_Object = MibTableColumn
cfprVnicIPv4IfType = _CfprVnicIPv4IfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 23, 1, 14),
    _CfprVnicIPv4IfType_Type()
)
cfprVnicIPv4IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4IfType.setStatus("current")
_CfprVnicIPv4IfVnet_Type = Gauge32
_CfprVnicIPv4IfVnet_Object = MibTableColumn
cfprVnicIPv4IfVnet = _CfprVnicIPv4IfVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 23, 1, 15),
    _CfprVnicIPv4IfVnet_Type()
)
cfprVnicIPv4IfVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4IfVnet.setStatus("current")
_CfprVnicIPv4IscsiAddrTable_Object = MibTable
cfprVnicIPv4IscsiAddrTable = _CfprVnicIPv4IscsiAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 24)
)
if mibBuilder.loadTexts:
    cfprVnicIPv4IscsiAddrTable.setStatus("current")
_CfprVnicIPv4IscsiAddrEntry_Object = MibTableRow
cfprVnicIPv4IscsiAddrEntry = _CfprVnicIPv4IscsiAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 24, 1)
)
cfprVnicIPv4IscsiAddrEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicIPv4IscsiAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicIPv4IscsiAddrEntry.setStatus("current")
_CfprVnicIPv4IscsiAddrInstanceId_Type = CfprManagedObjectId
_CfprVnicIPv4IscsiAddrInstanceId_Object = MibTableColumn
cfprVnicIPv4IscsiAddrInstanceId = _CfprVnicIPv4IscsiAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 24, 1, 1),
    _CfprVnicIPv4IscsiAddrInstanceId_Type()
)
cfprVnicIPv4IscsiAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicIPv4IscsiAddrInstanceId.setStatus("current")
_CfprVnicIPv4IscsiAddrDn_Type = CfprManagedObjectDn
_CfprVnicIPv4IscsiAddrDn_Object = MibTableColumn
cfprVnicIPv4IscsiAddrDn = _CfprVnicIPv4IscsiAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 24, 1, 2),
    _CfprVnicIPv4IscsiAddrDn_Type()
)
cfprVnicIPv4IscsiAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4IscsiAddrDn.setStatus("current")
_CfprVnicIPv4IscsiAddrRn_Type = SnmpAdminString
_CfprVnicIPv4IscsiAddrRn_Object = MibTableColumn
cfprVnicIPv4IscsiAddrRn = _CfprVnicIPv4IscsiAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 24, 1, 3),
    _CfprVnicIPv4IscsiAddrRn_Type()
)
cfprVnicIPv4IscsiAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4IscsiAddrRn.setStatus("current")
_CfprVnicIPv4IscsiAddrAddr_Type = InetAddressIPv4
_CfprVnicIPv4IscsiAddrAddr_Object = MibTableColumn
cfprVnicIPv4IscsiAddrAddr = _CfprVnicIPv4IscsiAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 24, 1, 4),
    _CfprVnicIPv4IscsiAddrAddr_Type()
)
cfprVnicIPv4IscsiAddrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4IscsiAddrAddr.setStatus("current")
_CfprVnicIPv4IscsiAddrDefGw_Type = InetAddressIPv4
_CfprVnicIPv4IscsiAddrDefGw_Object = MibTableColumn
cfprVnicIPv4IscsiAddrDefGw = _CfprVnicIPv4IscsiAddrDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 24, 1, 5),
    _CfprVnicIPv4IscsiAddrDefGw_Type()
)
cfprVnicIPv4IscsiAddrDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4IscsiAddrDefGw.setStatus("current")
_CfprVnicIPv4IscsiAddrPrimDns_Type = InetAddressIPv4
_CfprVnicIPv4IscsiAddrPrimDns_Object = MibTableColumn
cfprVnicIPv4IscsiAddrPrimDns = _CfprVnicIPv4IscsiAddrPrimDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 24, 1, 6),
    _CfprVnicIPv4IscsiAddrPrimDns_Type()
)
cfprVnicIPv4IscsiAddrPrimDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4IscsiAddrPrimDns.setStatus("current")
_CfprVnicIPv4IscsiAddrSecDns_Type = InetAddressIPv4
_CfprVnicIPv4IscsiAddrSecDns_Object = MibTableColumn
cfprVnicIPv4IscsiAddrSecDns = _CfprVnicIPv4IscsiAddrSecDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 24, 1, 7),
    _CfprVnicIPv4IscsiAddrSecDns_Type()
)
cfprVnicIPv4IscsiAddrSecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4IscsiAddrSecDns.setStatus("current")
_CfprVnicIPv4IscsiAddrSubnet_Type = InetAddressIPv4
_CfprVnicIPv4IscsiAddrSubnet_Object = MibTableColumn
cfprVnicIPv4IscsiAddrSubnet = _CfprVnicIPv4IscsiAddrSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 24, 1, 8),
    _CfprVnicIPv4IscsiAddrSubnet_Type()
)
cfprVnicIPv4IscsiAddrSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4IscsiAddrSubnet.setStatus("current")
_CfprVnicIPv4PooledIscsiAddrTable_Object = MibTable
cfprVnicIPv4PooledIscsiAddrTable = _CfprVnicIPv4PooledIscsiAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 25)
)
if mibBuilder.loadTexts:
    cfprVnicIPv4PooledIscsiAddrTable.setStatus("current")
_CfprVnicIPv4PooledIscsiAddrEntry_Object = MibTableRow
cfprVnicIPv4PooledIscsiAddrEntry = _CfprVnicIPv4PooledIscsiAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 25, 1)
)
cfprVnicIPv4PooledIscsiAddrEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicIPv4PooledIscsiAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicIPv4PooledIscsiAddrEntry.setStatus("current")
_CfprVnicIPv4PooledIscsiAddrInstanceId_Type = CfprManagedObjectId
_CfprVnicIPv4PooledIscsiAddrInstanceId_Object = MibTableColumn
cfprVnicIPv4PooledIscsiAddrInstanceId = _CfprVnicIPv4PooledIscsiAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 25, 1, 1),
    _CfprVnicIPv4PooledIscsiAddrInstanceId_Type()
)
cfprVnicIPv4PooledIscsiAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicIPv4PooledIscsiAddrInstanceId.setStatus("current")
_CfprVnicIPv4PooledIscsiAddrDn_Type = CfprManagedObjectDn
_CfprVnicIPv4PooledIscsiAddrDn_Object = MibTableColumn
cfprVnicIPv4PooledIscsiAddrDn = _CfprVnicIPv4PooledIscsiAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 25, 1, 2),
    _CfprVnicIPv4PooledIscsiAddrDn_Type()
)
cfprVnicIPv4PooledIscsiAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4PooledIscsiAddrDn.setStatus("current")
_CfprVnicIPv4PooledIscsiAddrRn_Type = SnmpAdminString
_CfprVnicIPv4PooledIscsiAddrRn_Object = MibTableColumn
cfprVnicIPv4PooledIscsiAddrRn = _CfprVnicIPv4PooledIscsiAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 25, 1, 3),
    _CfprVnicIPv4PooledIscsiAddrRn_Type()
)
cfprVnicIPv4PooledIscsiAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4PooledIscsiAddrRn.setStatus("current")
_CfprVnicIPv4PooledIscsiAddrAddr_Type = InetAddressIPv4
_CfprVnicIPv4PooledIscsiAddrAddr_Object = MibTableColumn
cfprVnicIPv4PooledIscsiAddrAddr = _CfprVnicIPv4PooledIscsiAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 25, 1, 4),
    _CfprVnicIPv4PooledIscsiAddrAddr_Type()
)
cfprVnicIPv4PooledIscsiAddrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4PooledIscsiAddrAddr.setStatus("current")
_CfprVnicIPv4PooledIscsiAddrDefGw_Type = InetAddressIPv4
_CfprVnicIPv4PooledIscsiAddrDefGw_Object = MibTableColumn
cfprVnicIPv4PooledIscsiAddrDefGw = _CfprVnicIPv4PooledIscsiAddrDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 25, 1, 5),
    _CfprVnicIPv4PooledIscsiAddrDefGw_Type()
)
cfprVnicIPv4PooledIscsiAddrDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4PooledIscsiAddrDefGw.setStatus("current")
_CfprVnicIPv4PooledIscsiAddrIdentPoolName_Type = SnmpAdminString
_CfprVnicIPv4PooledIscsiAddrIdentPoolName_Object = MibTableColumn
cfprVnicIPv4PooledIscsiAddrIdentPoolName = _CfprVnicIPv4PooledIscsiAddrIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 25, 1, 6),
    _CfprVnicIPv4PooledIscsiAddrIdentPoolName_Type()
)
cfprVnicIPv4PooledIscsiAddrIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4PooledIscsiAddrIdentPoolName.setStatus("current")
_CfprVnicIPv4PooledIscsiAddrOperIdentPoolName_Type = SnmpAdminString
_CfprVnicIPv4PooledIscsiAddrOperIdentPoolName_Object = MibTableColumn
cfprVnicIPv4PooledIscsiAddrOperIdentPoolName = _CfprVnicIPv4PooledIscsiAddrOperIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 25, 1, 7),
    _CfprVnicIPv4PooledIscsiAddrOperIdentPoolName_Type()
)
cfprVnicIPv4PooledIscsiAddrOperIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4PooledIscsiAddrOperIdentPoolName.setStatus("current")
_CfprVnicIPv4PooledIscsiAddrPrimDns_Type = InetAddressIPv4
_CfprVnicIPv4PooledIscsiAddrPrimDns_Object = MibTableColumn
cfprVnicIPv4PooledIscsiAddrPrimDns = _CfprVnicIPv4PooledIscsiAddrPrimDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 25, 1, 8),
    _CfprVnicIPv4PooledIscsiAddrPrimDns_Type()
)
cfprVnicIPv4PooledIscsiAddrPrimDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4PooledIscsiAddrPrimDns.setStatus("current")
_CfprVnicIPv4PooledIscsiAddrSecDns_Type = InetAddressIPv4
_CfprVnicIPv4PooledIscsiAddrSecDns_Object = MibTableColumn
cfprVnicIPv4PooledIscsiAddrSecDns = _CfprVnicIPv4PooledIscsiAddrSecDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 25, 1, 9),
    _CfprVnicIPv4PooledIscsiAddrSecDns_Type()
)
cfprVnicIPv4PooledIscsiAddrSecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4PooledIscsiAddrSecDns.setStatus("current")
_CfprVnicIPv4PooledIscsiAddrSubnet_Type = InetAddressIPv4
_CfprVnicIPv4PooledIscsiAddrSubnet_Object = MibTableColumn
cfprVnicIPv4PooledIscsiAddrSubnet = _CfprVnicIPv4PooledIscsiAddrSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 25, 1, 10),
    _CfprVnicIPv4PooledIscsiAddrSubnet_Type()
)
cfprVnicIPv4PooledIscsiAddrSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4PooledIscsiAddrSubnet.setStatus("current")
_CfprVnicIPv4StaticRouteTable_Object = MibTable
cfprVnicIPv4StaticRouteTable = _CfprVnicIPv4StaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 26)
)
if mibBuilder.loadTexts:
    cfprVnicIPv4StaticRouteTable.setStatus("current")
_CfprVnicIPv4StaticRouteEntry_Object = MibTableRow
cfprVnicIPv4StaticRouteEntry = _CfprVnicIPv4StaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 26, 1)
)
cfprVnicIPv4StaticRouteEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicIPv4StaticRouteInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicIPv4StaticRouteEntry.setStatus("current")
_CfprVnicIPv4StaticRouteInstanceId_Type = CfprManagedObjectId
_CfprVnicIPv4StaticRouteInstanceId_Object = MibTableColumn
cfprVnicIPv4StaticRouteInstanceId = _CfprVnicIPv4StaticRouteInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 26, 1, 1),
    _CfprVnicIPv4StaticRouteInstanceId_Type()
)
cfprVnicIPv4StaticRouteInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicIPv4StaticRouteInstanceId.setStatus("current")
_CfprVnicIPv4StaticRouteDn_Type = CfprManagedObjectDn
_CfprVnicIPv4StaticRouteDn_Object = MibTableColumn
cfprVnicIPv4StaticRouteDn = _CfprVnicIPv4StaticRouteDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 26, 1, 2),
    _CfprVnicIPv4StaticRouteDn_Type()
)
cfprVnicIPv4StaticRouteDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4StaticRouteDn.setStatus("current")
_CfprVnicIPv4StaticRouteRn_Type = SnmpAdminString
_CfprVnicIPv4StaticRouteRn_Object = MibTableColumn
cfprVnicIPv4StaticRouteRn = _CfprVnicIPv4StaticRouteRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 26, 1, 3),
    _CfprVnicIPv4StaticRouteRn_Type()
)
cfprVnicIPv4StaticRouteRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4StaticRouteRn.setStatus("current")
_CfprVnicIPv4StaticRouteAddr_Type = InetAddressIPv4
_CfprVnicIPv4StaticRouteAddr_Object = MibTableColumn
cfprVnicIPv4StaticRouteAddr = _CfprVnicIPv4StaticRouteAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 26, 1, 4),
    _CfprVnicIPv4StaticRouteAddr_Type()
)
cfprVnicIPv4StaticRouteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4StaticRouteAddr.setStatus("current")
_CfprVnicIPv4StaticRouteDefGw_Type = InetAddressIPv4
_CfprVnicIPv4StaticRouteDefGw_Object = MibTableColumn
cfprVnicIPv4StaticRouteDefGw = _CfprVnicIPv4StaticRouteDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 26, 1, 5),
    _CfprVnicIPv4StaticRouteDefGw_Type()
)
cfprVnicIPv4StaticRouteDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4StaticRouteDefGw.setStatus("current")
_CfprVnicIPv4StaticRouteGwAddr_Type = InetAddressIPv4
_CfprVnicIPv4StaticRouteGwAddr_Object = MibTableColumn
cfprVnicIPv4StaticRouteGwAddr = _CfprVnicIPv4StaticRouteGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 26, 1, 6),
    _CfprVnicIPv4StaticRouteGwAddr_Type()
)
cfprVnicIPv4StaticRouteGwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4StaticRouteGwAddr.setStatus("current")
_CfprVnicIPv4StaticRouteGwSubnet_Type = InetAddressIPv4
_CfprVnicIPv4StaticRouteGwSubnet_Object = MibTableColumn
cfprVnicIPv4StaticRouteGwSubnet = _CfprVnicIPv4StaticRouteGwSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 26, 1, 7),
    _CfprVnicIPv4StaticRouteGwSubnet_Type()
)
cfprVnicIPv4StaticRouteGwSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4StaticRouteGwSubnet.setStatus("current")
_CfprVnicIPv4StaticRouteSubnet_Type = InetAddressIPv4
_CfprVnicIPv4StaticRouteSubnet_Object = MibTableColumn
cfprVnicIPv4StaticRouteSubnet = _CfprVnicIPv4StaticRouteSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 26, 1, 8),
    _CfprVnicIPv4StaticRouteSubnet_Type()
)
cfprVnicIPv4StaticRouteSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIPv4StaticRouteSubnet.setStatus("current")
_CfprVnicIScsiTable_Object = MibTable
cfprVnicIScsiTable = _CfprVnicIScsiTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27)
)
if mibBuilder.loadTexts:
    cfprVnicIScsiTable.setStatus("current")
_CfprVnicIScsiEntry_Object = MibTableRow
cfprVnicIScsiEntry = _CfprVnicIScsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1)
)
cfprVnicIScsiEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicIScsiInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicIScsiEntry.setStatus("current")
_CfprVnicIScsiInstanceId_Type = CfprManagedObjectId
_CfprVnicIScsiInstanceId_Object = MibTableColumn
cfprVnicIScsiInstanceId = _CfprVnicIScsiInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 1),
    _CfprVnicIScsiInstanceId_Type()
)
cfprVnicIScsiInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicIScsiInstanceId.setStatus("current")
_CfprVnicIScsiDn_Type = CfprManagedObjectDn
_CfprVnicIScsiDn_Object = MibTableColumn
cfprVnicIScsiDn = _CfprVnicIScsiDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 2),
    _CfprVnicIScsiDn_Type()
)
cfprVnicIScsiDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiDn.setStatus("current")
_CfprVnicIScsiRn_Type = SnmpAdminString
_CfprVnicIScsiRn_Object = MibTableColumn
cfprVnicIScsiRn = _CfprVnicIScsiRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 3),
    _CfprVnicIScsiRn_Type()
)
cfprVnicIScsiRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiRn.setStatus("current")
_CfprVnicIScsiAdaptorProfileName_Type = SnmpAdminString
_CfprVnicIScsiAdaptorProfileName_Object = MibTableColumn
cfprVnicIScsiAdaptorProfileName = _CfprVnicIScsiAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 4),
    _CfprVnicIScsiAdaptorProfileName_Type()
)
cfprVnicIScsiAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiAdaptorProfileName.setStatus("current")
_CfprVnicIScsiAddr_Type = MacAddress
_CfprVnicIScsiAddr_Object = MibTableColumn
cfprVnicIScsiAddr = _CfprVnicIScsiAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 5),
    _CfprVnicIScsiAddr_Type()
)
cfprVnicIScsiAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiAddr.setStatus("current")
_CfprVnicIScsiAdminHostPort_Type = CfprFabricHostPortId
_CfprVnicIScsiAdminHostPort_Object = MibTableColumn
cfprVnicIScsiAdminHostPort = _CfprVnicIScsiAdminHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 6),
    _CfprVnicIScsiAdminHostPort_Type()
)
cfprVnicIScsiAdminHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiAdminHostPort.setStatus("current")
_CfprVnicIScsiAdminVcon_Type = SnmpAdminString
_CfprVnicIScsiAdminVcon_Object = MibTableColumn
cfprVnicIScsiAdminVcon = _CfprVnicIScsiAdminVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 7),
    _CfprVnicIScsiAdminVcon_Type()
)
cfprVnicIScsiAdminVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiAdminVcon.setStatus("current")
_CfprVnicIScsiAppRole_Type = CfprVnicAppRole
_CfprVnicIScsiAppRole_Object = MibTableColumn
cfprVnicIScsiAppRole = _CfprVnicIScsiAppRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 8),
    _CfprVnicIScsiAppRole_Type()
)
cfprVnicIScsiAppRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiAppRole.setStatus("current")
_CfprVnicIScsiAuthProfileName_Type = SnmpAdminString
_CfprVnicIScsiAuthProfileName_Object = MibTableColumn
cfprVnicIScsiAuthProfileName = _CfprVnicIScsiAuthProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 9),
    _CfprVnicIScsiAuthProfileName_Type()
)
cfprVnicIScsiAuthProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiAuthProfileName.setStatus("current")
_CfprVnicIScsiBootDev_Type = CfprVnicVnicBootDev
_CfprVnicIScsiBootDev_Object = MibTableColumn
cfprVnicIScsiBootDev = _CfprVnicIScsiBootDev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 10),
    _CfprVnicIScsiBootDev_Type()
)
cfprVnicIScsiBootDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiBootDev.setStatus("current")
_CfprVnicIScsiConfigQualifier_Type = CfprVnicConfigIssues
_CfprVnicIScsiConfigQualifier_Object = MibTableColumn
cfprVnicIScsiConfigQualifier = _CfprVnicIScsiConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 11),
    _CfprVnicIScsiConfigQualifier_Type()
)
cfprVnicIScsiConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiConfigQualifier.setStatus("current")
_CfprVnicIScsiConfigState_Type = CfprLsConfigState
_CfprVnicIScsiConfigState_Object = MibTableColumn
cfprVnicIScsiConfigState = _CfprVnicIScsiConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 12),
    _CfprVnicIScsiConfigState_Type()
)
cfprVnicIScsiConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiConfigState.setStatus("current")
_CfprVnicIScsiEquipmentDn_Type = SnmpAdminString
_CfprVnicIScsiEquipmentDn_Object = MibTableColumn
cfprVnicIScsiEquipmentDn = _CfprVnicIScsiEquipmentDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 13),
    _CfprVnicIScsiEquipmentDn_Type()
)
cfprVnicIScsiEquipmentDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiEquipmentDn.setStatus("current")
_CfprVnicIScsiEthEpDn_Type = SnmpAdminString
_CfprVnicIScsiEthEpDn_Object = MibTableColumn
cfprVnicIScsiEthEpDn = _CfprVnicIScsiEthEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 14),
    _CfprVnicIScsiEthEpDn_Type()
)
cfprVnicIScsiEthEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiEthEpDn.setStatus("current")
_CfprVnicIScsiExtIPState_Type = CfprVnicExternalMgmtIPMode
_CfprVnicIScsiExtIPState_Object = MibTableColumn
cfprVnicIScsiExtIPState = _CfprVnicIScsiExtIPState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 15),
    _CfprVnicIScsiExtIPState_Type()
)
cfprVnicIScsiExtIPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiExtIPState.setStatus("current")
_CfprVnicIScsiFltAggr_Type = Unsigned64
_CfprVnicIScsiFltAggr_Object = MibTableColumn
cfprVnicIScsiFltAggr = _CfprVnicIScsiFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 16),
    _CfprVnicIScsiFltAggr_Type()
)
cfprVnicIScsiFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiFltAggr.setStatus("current")
_CfprVnicIScsiIdentPoolName_Type = SnmpAdminString
_CfprVnicIScsiIdentPoolName_Object = MibTableColumn
cfprVnicIScsiIdentPoolName = _CfprVnicIScsiIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 17),
    _CfprVnicIScsiIdentPoolName_Type()
)
cfprVnicIScsiIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiIdentPoolName.setStatus("current")
_CfprVnicIScsiInitNameSuffix_Type = SnmpAdminString
_CfprVnicIScsiInitNameSuffix_Object = MibTableColumn
cfprVnicIScsiInitNameSuffix = _CfprVnicIScsiInitNameSuffix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 18),
    _CfprVnicIScsiInitNameSuffix_Type()
)
cfprVnicIScsiInitNameSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiInitNameSuffix.setStatus("current")
_CfprVnicIScsiInitiatorName_Type = SnmpAdminString
_CfprVnicIScsiInitiatorName_Object = MibTableColumn
cfprVnicIScsiInitiatorName = _CfprVnicIScsiInitiatorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 19),
    _CfprVnicIScsiInitiatorName_Type()
)
cfprVnicIScsiInitiatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiInitiatorName.setStatus("current")
_CfprVnicIScsiInstType_Type = CfprVnicInstantiation
_CfprVnicIScsiInstType_Object = MibTableColumn
cfprVnicIScsiInstType = _CfprVnicIScsiInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 20),
    _CfprVnicIScsiInstType_Type()
)
cfprVnicIScsiInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiInstType.setStatus("current")
_CfprVnicIScsiIqnIdentPoolName_Type = SnmpAdminString
_CfprVnicIScsiIqnIdentPoolName_Object = MibTableColumn
cfprVnicIScsiIqnIdentPoolName = _CfprVnicIScsiIqnIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 21),
    _CfprVnicIScsiIqnIdentPoolName_Type()
)
cfprVnicIScsiIqnIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiIqnIdentPoolName.setStatus("current")
_CfprVnicIScsiName_Type = SnmpAdminString
_CfprVnicIScsiName_Object = MibTableColumn
cfprVnicIScsiName = _CfprVnicIScsiName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 22),
    _CfprVnicIScsiName_Type()
)
cfprVnicIScsiName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiName.setStatus("current")
_CfprVnicIScsiNwTemplName_Type = SnmpAdminString
_CfprVnicIScsiNwTemplName_Object = MibTableColumn
cfprVnicIScsiNwTemplName = _CfprVnicIScsiNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 23),
    _CfprVnicIScsiNwTemplName_Type()
)
cfprVnicIScsiNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiNwTemplName.setStatus("current")
_CfprVnicIScsiOperAdaptorProfileName_Type = SnmpAdminString
_CfprVnicIScsiOperAdaptorProfileName_Object = MibTableColumn
cfprVnicIScsiOperAdaptorProfileName = _CfprVnicIScsiOperAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 24),
    _CfprVnicIScsiOperAdaptorProfileName_Type()
)
cfprVnicIScsiOperAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiOperAdaptorProfileName.setStatus("current")
_CfprVnicIScsiOperAuthProfileName_Type = SnmpAdminString
_CfprVnicIScsiOperAuthProfileName_Object = MibTableColumn
cfprVnicIScsiOperAuthProfileName = _CfprVnicIScsiOperAuthProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 25),
    _CfprVnicIScsiOperAuthProfileName_Type()
)
cfprVnicIScsiOperAuthProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiOperAuthProfileName.setStatus("current")
_CfprVnicIScsiOperHostPort_Type = CfprVnicVnicOperHostPort
_CfprVnicIScsiOperHostPort_Object = MibTableColumn
cfprVnicIScsiOperHostPort = _CfprVnicIScsiOperHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 26),
    _CfprVnicIScsiOperHostPort_Type()
)
cfprVnicIScsiOperHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiOperHostPort.setStatus("current")
_CfprVnicIScsiOperIdentPoolName_Type = SnmpAdminString
_CfprVnicIScsiOperIdentPoolName_Object = MibTableColumn
cfprVnicIScsiOperIdentPoolName = _CfprVnicIScsiOperIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 27),
    _CfprVnicIScsiOperIdentPoolName_Type()
)
cfprVnicIScsiOperIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiOperIdentPoolName.setStatus("current")
_CfprVnicIScsiOperIqnIdentPoolName_Type = SnmpAdminString
_CfprVnicIScsiOperIqnIdentPoolName_Object = MibTableColumn
cfprVnicIScsiOperIqnIdentPoolName = _CfprVnicIScsiOperIqnIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 28),
    _CfprVnicIScsiOperIqnIdentPoolName_Type()
)
cfprVnicIScsiOperIqnIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiOperIqnIdentPoolName.setStatus("current")
_CfprVnicIScsiOperOrder_Type = Gauge32
_CfprVnicIScsiOperOrder_Object = MibTableColumn
cfprVnicIScsiOperOrder = _CfprVnicIScsiOperOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 29),
    _CfprVnicIScsiOperOrder_Type()
)
cfprVnicIScsiOperOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiOperOrder.setStatus("current")
_CfprVnicIScsiOperSpeed_Type = Gauge32
_CfprVnicIScsiOperSpeed_Object = MibTableColumn
cfprVnicIScsiOperSpeed = _CfprVnicIScsiOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 30),
    _CfprVnicIScsiOperSpeed_Type()
)
cfprVnicIScsiOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiOperSpeed.setStatus("current")
_CfprVnicIScsiOperStatsPolicyName_Type = SnmpAdminString
_CfprVnicIScsiOperStatsPolicyName_Object = MibTableColumn
cfprVnicIScsiOperStatsPolicyName = _CfprVnicIScsiOperStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 31),
    _CfprVnicIScsiOperStatsPolicyName_Type()
)
cfprVnicIScsiOperStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiOperStatsPolicyName.setStatus("current")
_CfprVnicIScsiOperVcon_Type = SnmpAdminString
_CfprVnicIScsiOperVcon_Object = MibTableColumn
cfprVnicIScsiOperVcon = _CfprVnicIScsiOperVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 32),
    _CfprVnicIScsiOperVcon_Type()
)
cfprVnicIScsiOperVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiOperVcon.setStatus("current")
_CfprVnicIScsiOrder_Type = Gauge32
_CfprVnicIScsiOrder_Object = MibTableColumn
cfprVnicIScsiOrder = _CfprVnicIScsiOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 33),
    _CfprVnicIScsiOrder_Type()
)
cfprVnicIScsiOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiOrder.setStatus("current")
_CfprVnicIScsiOwner_Type = CfprVnicConnectionOwner
_CfprVnicIScsiOwner_Object = MibTableColumn
cfprVnicIScsiOwner = _CfprVnicIScsiOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 34),
    _CfprVnicIScsiOwner_Type()
)
cfprVnicIScsiOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiOwner.setStatus("current")
_CfprVnicIScsiPinToGroupName_Type = SnmpAdminString
_CfprVnicIScsiPinToGroupName_Object = MibTableColumn
cfprVnicIScsiPinToGroupName = _CfprVnicIScsiPinToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 35),
    _CfprVnicIScsiPinToGroupName_Type()
)
cfprVnicIScsiPinToGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiPinToGroupName.setStatus("current")
_CfprVnicIScsiQosPolicyName_Type = SnmpAdminString
_CfprVnicIScsiQosPolicyName_Object = MibTableColumn
cfprVnicIScsiQosPolicyName = _CfprVnicIScsiQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 36),
    _CfprVnicIScsiQosPolicyName_Type()
)
cfprVnicIScsiQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiQosPolicyName.setStatus("current")
_CfprVnicIScsiStatsPolicyName_Type = SnmpAdminString
_CfprVnicIScsiStatsPolicyName_Object = MibTableColumn
cfprVnicIScsiStatsPolicyName = _CfprVnicIScsiStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 37),
    _CfprVnicIScsiStatsPolicyName_Type()
)
cfprVnicIScsiStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiStatsPolicyName.setStatus("current")
_CfprVnicIScsiSwitchId_Type = CfprNetworkSwitchId
_CfprVnicIScsiSwitchId_Object = MibTableColumn
cfprVnicIScsiSwitchId = _CfprVnicIScsiSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 38),
    _CfprVnicIScsiSwitchId_Type()
)
cfprVnicIScsiSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiSwitchId.setStatus("current")
_CfprVnicIScsiType_Type = CfprVnicConnectionType
_CfprVnicIScsiType_Object = MibTableColumn
cfprVnicIScsiType = _CfprVnicIScsiType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 39),
    _CfprVnicIScsiType_Type()
)
cfprVnicIScsiType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiType.setStatus("current")
_CfprVnicIScsiVnicDefType_Type = CfprVnicIScsiIfDefType
_CfprVnicIScsiVnicDefType_Object = MibTableColumn
cfprVnicIScsiVnicDefType = _CfprVnicIScsiVnicDefType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 40),
    _CfprVnicIScsiVnicDefType_Type()
)
cfprVnicIScsiVnicDefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiVnicDefType.setStatus("current")
_CfprVnicIScsiVnicName_Type = SnmpAdminString
_CfprVnicIScsiVnicName_Object = MibTableColumn
cfprVnicIScsiVnicName = _CfprVnicIScsiVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 27, 1, 41),
    _CfprVnicIScsiVnicName_Type()
)
cfprVnicIScsiVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiVnicName.setStatus("current")
_CfprVnicIScsiAutoTargetIfTable_Object = MibTable
cfprVnicIScsiAutoTargetIfTable = _CfprVnicIScsiAutoTargetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 28)
)
if mibBuilder.loadTexts:
    cfprVnicIScsiAutoTargetIfTable.setStatus("current")
_CfprVnicIScsiAutoTargetIfEntry_Object = MibTableRow
cfprVnicIScsiAutoTargetIfEntry = _CfprVnicIScsiAutoTargetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 28, 1)
)
cfprVnicIScsiAutoTargetIfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicIScsiAutoTargetIfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicIScsiAutoTargetIfEntry.setStatus("current")
_CfprVnicIScsiAutoTargetIfInstanceId_Type = CfprManagedObjectId
_CfprVnicIScsiAutoTargetIfInstanceId_Object = MibTableColumn
cfprVnicIScsiAutoTargetIfInstanceId = _CfprVnicIScsiAutoTargetIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 28, 1, 1),
    _CfprVnicIScsiAutoTargetIfInstanceId_Type()
)
cfprVnicIScsiAutoTargetIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicIScsiAutoTargetIfInstanceId.setStatus("current")
_CfprVnicIScsiAutoTargetIfDn_Type = CfprManagedObjectDn
_CfprVnicIScsiAutoTargetIfDn_Object = MibTableColumn
cfprVnicIScsiAutoTargetIfDn = _CfprVnicIScsiAutoTargetIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 28, 1, 2),
    _CfprVnicIScsiAutoTargetIfDn_Type()
)
cfprVnicIScsiAutoTargetIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiAutoTargetIfDn.setStatus("current")
_CfprVnicIScsiAutoTargetIfRn_Type = SnmpAdminString
_CfprVnicIScsiAutoTargetIfRn_Object = MibTableColumn
cfprVnicIScsiAutoTargetIfRn = _CfprVnicIScsiAutoTargetIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 28, 1, 3),
    _CfprVnicIScsiAutoTargetIfRn_Type()
)
cfprVnicIScsiAutoTargetIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiAutoTargetIfRn.setStatus("current")
_CfprVnicIScsiAutoTargetIfDhcpVendorId_Type = SnmpAdminString
_CfprVnicIScsiAutoTargetIfDhcpVendorId_Object = MibTableColumn
cfprVnicIScsiAutoTargetIfDhcpVendorId = _CfprVnicIScsiAutoTargetIfDhcpVendorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 28, 1, 4),
    _CfprVnicIScsiAutoTargetIfDhcpVendorId_Type()
)
cfprVnicIScsiAutoTargetIfDhcpVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiAutoTargetIfDhcpVendorId.setStatus("current")
_CfprVnicIScsiBootParamsTable_Object = MibTable
cfprVnicIScsiBootParamsTable = _CfprVnicIScsiBootParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 29)
)
if mibBuilder.loadTexts:
    cfprVnicIScsiBootParamsTable.setStatus("current")
_CfprVnicIScsiBootParamsEntry_Object = MibTableRow
cfprVnicIScsiBootParamsEntry = _CfprVnicIScsiBootParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 29, 1)
)
cfprVnicIScsiBootParamsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicIScsiBootParamsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicIScsiBootParamsEntry.setStatus("current")
_CfprVnicIScsiBootParamsInstanceId_Type = CfprManagedObjectId
_CfprVnicIScsiBootParamsInstanceId_Object = MibTableColumn
cfprVnicIScsiBootParamsInstanceId = _CfprVnicIScsiBootParamsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 29, 1, 1),
    _CfprVnicIScsiBootParamsInstanceId_Type()
)
cfprVnicIScsiBootParamsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicIScsiBootParamsInstanceId.setStatus("current")
_CfprVnicIScsiBootParamsDn_Type = CfprManagedObjectDn
_CfprVnicIScsiBootParamsDn_Object = MibTableColumn
cfprVnicIScsiBootParamsDn = _CfprVnicIScsiBootParamsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 29, 1, 2),
    _CfprVnicIScsiBootParamsDn_Type()
)
cfprVnicIScsiBootParamsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiBootParamsDn.setStatus("current")
_CfprVnicIScsiBootParamsRn_Type = SnmpAdminString
_CfprVnicIScsiBootParamsRn_Object = MibTableColumn
cfprVnicIScsiBootParamsRn = _CfprVnicIScsiBootParamsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 29, 1, 3),
    _CfprVnicIScsiBootParamsRn_Type()
)
cfprVnicIScsiBootParamsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiBootParamsRn.setStatus("current")
_CfprVnicIScsiBootParamsDescr_Type = SnmpAdminString
_CfprVnicIScsiBootParamsDescr_Object = MibTableColumn
cfprVnicIScsiBootParamsDescr = _CfprVnicIScsiBootParamsDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 29, 1, 4),
    _CfprVnicIScsiBootParamsDescr_Type()
)
cfprVnicIScsiBootParamsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiBootParamsDescr.setStatus("current")
_CfprVnicIScsiBootParamsIntId_Type = SnmpAdminString
_CfprVnicIScsiBootParamsIntId_Object = MibTableColumn
cfprVnicIScsiBootParamsIntId = _CfprVnicIScsiBootParamsIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 29, 1, 5),
    _CfprVnicIScsiBootParamsIntId_Type()
)
cfprVnicIScsiBootParamsIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiBootParamsIntId.setStatus("current")
_CfprVnicIScsiBootParamsName_Type = SnmpAdminString
_CfprVnicIScsiBootParamsName_Object = MibTableColumn
cfprVnicIScsiBootParamsName = _CfprVnicIScsiBootParamsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 29, 1, 6),
    _CfprVnicIScsiBootParamsName_Type()
)
cfprVnicIScsiBootParamsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiBootParamsName.setStatus("current")
_CfprVnicIScsiBootParamsPolicyLevel_Type = Gauge32
_CfprVnicIScsiBootParamsPolicyLevel_Object = MibTableColumn
cfprVnicIScsiBootParamsPolicyLevel = _CfprVnicIScsiBootParamsPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 29, 1, 7),
    _CfprVnicIScsiBootParamsPolicyLevel_Type()
)
cfprVnicIScsiBootParamsPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiBootParamsPolicyLevel.setStatus("current")
_CfprVnicIScsiBootParamsPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprVnicIScsiBootParamsPolicyOwner_Object = MibTableColumn
cfprVnicIScsiBootParamsPolicyOwner = _CfprVnicIScsiBootParamsPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 29, 1, 8),
    _CfprVnicIScsiBootParamsPolicyOwner_Type()
)
cfprVnicIScsiBootParamsPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiBootParamsPolicyOwner.setStatus("current")
_CfprVnicIScsiBootVnicTable_Object = MibTable
cfprVnicIScsiBootVnicTable = _CfprVnicIScsiBootVnicTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 30)
)
if mibBuilder.loadTexts:
    cfprVnicIScsiBootVnicTable.setStatus("current")
_CfprVnicIScsiBootVnicEntry_Object = MibTableRow
cfprVnicIScsiBootVnicEntry = _CfprVnicIScsiBootVnicEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 30, 1)
)
cfprVnicIScsiBootVnicEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicIScsiBootVnicInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicIScsiBootVnicEntry.setStatus("current")
_CfprVnicIScsiBootVnicInstanceId_Type = CfprManagedObjectId
_CfprVnicIScsiBootVnicInstanceId_Object = MibTableColumn
cfprVnicIScsiBootVnicInstanceId = _CfprVnicIScsiBootVnicInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 30, 1, 1),
    _CfprVnicIScsiBootVnicInstanceId_Type()
)
cfprVnicIScsiBootVnicInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicIScsiBootVnicInstanceId.setStatus("current")
_CfprVnicIScsiBootVnicDn_Type = CfprManagedObjectDn
_CfprVnicIScsiBootVnicDn_Object = MibTableColumn
cfprVnicIScsiBootVnicDn = _CfprVnicIScsiBootVnicDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 30, 1, 2),
    _CfprVnicIScsiBootVnicDn_Type()
)
cfprVnicIScsiBootVnicDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiBootVnicDn.setStatus("current")
_CfprVnicIScsiBootVnicRn_Type = SnmpAdminString
_CfprVnicIScsiBootVnicRn_Object = MibTableColumn
cfprVnicIScsiBootVnicRn = _CfprVnicIScsiBootVnicRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 30, 1, 3),
    _CfprVnicIScsiBootVnicRn_Type()
)
cfprVnicIScsiBootVnicRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiBootVnicRn.setStatus("current")
_CfprVnicIScsiBootVnicAuthProfileName_Type = SnmpAdminString
_CfprVnicIScsiBootVnicAuthProfileName_Object = MibTableColumn
cfprVnicIScsiBootVnicAuthProfileName = _CfprVnicIScsiBootVnicAuthProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 30, 1, 4),
    _CfprVnicIScsiBootVnicAuthProfileName_Type()
)
cfprVnicIScsiBootVnicAuthProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiBootVnicAuthProfileName.setStatus("current")
_CfprVnicIScsiBootVnicDescr_Type = SnmpAdminString
_CfprVnicIScsiBootVnicDescr_Object = MibTableColumn
cfprVnicIScsiBootVnicDescr = _CfprVnicIScsiBootVnicDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 30, 1, 5),
    _CfprVnicIScsiBootVnicDescr_Type()
)
cfprVnicIScsiBootVnicDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiBootVnicDescr.setStatus("current")
_CfprVnicIScsiBootVnicInitiatorName_Type = SnmpAdminString
_CfprVnicIScsiBootVnicInitiatorName_Object = MibTableColumn
cfprVnicIScsiBootVnicInitiatorName = _CfprVnicIScsiBootVnicInitiatorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 30, 1, 6),
    _CfprVnicIScsiBootVnicInitiatorName_Type()
)
cfprVnicIScsiBootVnicInitiatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiBootVnicInitiatorName.setStatus("current")
_CfprVnicIScsiBootVnicIntId_Type = SnmpAdminString
_CfprVnicIScsiBootVnicIntId_Object = MibTableColumn
cfprVnicIScsiBootVnicIntId = _CfprVnicIScsiBootVnicIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 30, 1, 7),
    _CfprVnicIScsiBootVnicIntId_Type()
)
cfprVnicIScsiBootVnicIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiBootVnicIntId.setStatus("current")
_CfprVnicIScsiBootVnicIqnIdentPoolName_Type = SnmpAdminString
_CfprVnicIScsiBootVnicIqnIdentPoolName_Object = MibTableColumn
cfprVnicIScsiBootVnicIqnIdentPoolName = _CfprVnicIScsiBootVnicIqnIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 30, 1, 8),
    _CfprVnicIScsiBootVnicIqnIdentPoolName_Type()
)
cfprVnicIScsiBootVnicIqnIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiBootVnicIqnIdentPoolName.setStatus("current")
_CfprVnicIScsiBootVnicName_Type = SnmpAdminString
_CfprVnicIScsiBootVnicName_Object = MibTableColumn
cfprVnicIScsiBootVnicName = _CfprVnicIScsiBootVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 30, 1, 9),
    _CfprVnicIScsiBootVnicName_Type()
)
cfprVnicIScsiBootVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiBootVnicName.setStatus("current")
_CfprVnicIScsiBootVnicOperAuthProfileName_Type = SnmpAdminString
_CfprVnicIScsiBootVnicOperAuthProfileName_Object = MibTableColumn
cfprVnicIScsiBootVnicOperAuthProfileName = _CfprVnicIScsiBootVnicOperAuthProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 30, 1, 10),
    _CfprVnicIScsiBootVnicOperAuthProfileName_Type()
)
cfprVnicIScsiBootVnicOperAuthProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiBootVnicOperAuthProfileName.setStatus("current")
_CfprVnicIScsiBootVnicOperIqnIdentPoolName_Type = SnmpAdminString
_CfprVnicIScsiBootVnicOperIqnIdentPoolName_Object = MibTableColumn
cfprVnicIScsiBootVnicOperIqnIdentPoolName = _CfprVnicIScsiBootVnicOperIqnIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 30, 1, 11),
    _CfprVnicIScsiBootVnicOperIqnIdentPoolName_Type()
)
cfprVnicIScsiBootVnicOperIqnIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiBootVnicOperIqnIdentPoolName.setStatus("current")
_CfprVnicIScsiBootVnicPolicyLevel_Type = Gauge32
_CfprVnicIScsiBootVnicPolicyLevel_Object = MibTableColumn
cfprVnicIScsiBootVnicPolicyLevel = _CfprVnicIScsiBootVnicPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 30, 1, 12),
    _CfprVnicIScsiBootVnicPolicyLevel_Type()
)
cfprVnicIScsiBootVnicPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiBootVnicPolicyLevel.setStatus("current")
_CfprVnicIScsiBootVnicPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprVnicIScsiBootVnicPolicyOwner_Object = MibTableColumn
cfprVnicIScsiBootVnicPolicyOwner = _CfprVnicIScsiBootVnicPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 30, 1, 13),
    _CfprVnicIScsiBootVnicPolicyOwner_Type()
)
cfprVnicIScsiBootVnicPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiBootVnicPolicyOwner.setStatus("current")
_CfprVnicIScsiLCPTable_Object = MibTable
cfprVnicIScsiLCPTable = _CfprVnicIScsiLCPTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 31)
)
if mibBuilder.loadTexts:
    cfprVnicIScsiLCPTable.setStatus("current")
_CfprVnicIScsiLCPEntry_Object = MibTableRow
cfprVnicIScsiLCPEntry = _CfprVnicIScsiLCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 31, 1)
)
cfprVnicIScsiLCPEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicIScsiLCPInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicIScsiLCPEntry.setStatus("current")
_CfprVnicIScsiLCPInstanceId_Type = CfprManagedObjectId
_CfprVnicIScsiLCPInstanceId_Object = MibTableColumn
cfprVnicIScsiLCPInstanceId = _CfprVnicIScsiLCPInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 31, 1, 1),
    _CfprVnicIScsiLCPInstanceId_Type()
)
cfprVnicIScsiLCPInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicIScsiLCPInstanceId.setStatus("current")
_CfprVnicIScsiLCPDn_Type = CfprManagedObjectDn
_CfprVnicIScsiLCPDn_Object = MibTableColumn
cfprVnicIScsiLCPDn = _CfprVnicIScsiLCPDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 31, 1, 2),
    _CfprVnicIScsiLCPDn_Type()
)
cfprVnicIScsiLCPDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiLCPDn.setStatus("current")
_CfprVnicIScsiLCPRn_Type = SnmpAdminString
_CfprVnicIScsiLCPRn_Object = MibTableColumn
cfprVnicIScsiLCPRn = _CfprVnicIScsiLCPRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 31, 1, 3),
    _CfprVnicIScsiLCPRn_Type()
)
cfprVnicIScsiLCPRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiLCPRn.setStatus("current")
_CfprVnicIScsiLCPAdaptorProfileName_Type = SnmpAdminString
_CfprVnicIScsiLCPAdaptorProfileName_Object = MibTableColumn
cfprVnicIScsiLCPAdaptorProfileName = _CfprVnicIScsiLCPAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 31, 1, 4),
    _CfprVnicIScsiLCPAdaptorProfileName_Type()
)
cfprVnicIScsiLCPAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiLCPAdaptorProfileName.setStatus("current")
_CfprVnicIScsiLCPAddr_Type = MacAddress
_CfprVnicIScsiLCPAddr_Object = MibTableColumn
cfprVnicIScsiLCPAddr = _CfprVnicIScsiLCPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 31, 1, 5),
    _CfprVnicIScsiLCPAddr_Type()
)
cfprVnicIScsiLCPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiLCPAddr.setStatus("current")
_CfprVnicIScsiLCPAdminHostPort_Type = CfprFabricHostPortId
_CfprVnicIScsiLCPAdminHostPort_Object = MibTableColumn
cfprVnicIScsiLCPAdminHostPort = _CfprVnicIScsiLCPAdminHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 31, 1, 6),
    _CfprVnicIScsiLCPAdminHostPort_Type()
)
cfprVnicIScsiLCPAdminHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiLCPAdminHostPort.setStatus("current")
_CfprVnicIScsiLCPAdminVcon_Type = SnmpAdminString
_CfprVnicIScsiLCPAdminVcon_Object = MibTableColumn
cfprVnicIScsiLCPAdminVcon = _CfprVnicIScsiLCPAdminVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 31, 1, 7),
    _CfprVnicIScsiLCPAdminVcon_Type()
)
cfprVnicIScsiLCPAdminVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiLCPAdminVcon.setStatus("current")
_CfprVnicIScsiLCPAppRole_Type = CfprVnicAppRole
_CfprVnicIScsiLCPAppRole_Object = MibTableColumn
cfprVnicIScsiLCPAppRole = _CfprVnicIScsiLCPAppRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 31, 1, 8),
    _CfprVnicIScsiLCPAppRole_Type()
)
cfprVnicIScsiLCPAppRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiLCPAppRole.setStatus("current")
_CfprVnicIScsiLCPBootDev_Type = CfprVnicVnicBootDev
_CfprVnicIScsiLCPBootDev_Object = MibTableColumn
cfprVnicIScsiLCPBootDev = _CfprVnicIScsiLCPBootDev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 31, 1, 9),
    _CfprVnicIScsiLCPBootDev_Type()
)
cfprVnicIScsiLCPBootDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiLCPBootDev.setStatus("current")
_CfprVnicIScsiLCPConfigQualifier_Type = CfprVnicConfigIssues
_CfprVnicIScsiLCPConfigQualifier_Object = MibTableColumn
cfprVnicIScsiLCPConfigQualifier = _CfprVnicIScsiLCPConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 31, 1, 10),
    _CfprVnicIScsiLCPConfigQualifier_Type()
)
cfprVnicIScsiLCPConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiLCPConfigQualifier.setStatus("current")
_CfprVnicIScsiLCPConfigState_Type = CfprLsConfigState
_CfprVnicIScsiLCPConfigState_Object = MibTableColumn
cfprVnicIScsiLCPConfigState = _CfprVnicIScsiLCPConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 31, 1, 11),
    _CfprVnicIScsiLCPConfigState_Type()
)
cfprVnicIScsiLCPConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiLCPConfigState.setStatus("current")
_CfprVnicIScsiLCPEquipmentDn_Type = SnmpAdminString
_CfprVnicIScsiLCPEquipmentDn_Object = MibTableColumn
cfprVnicIScsiLCPEquipmentDn = _CfprVnicIScsiLCPEquipmentDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 31, 1, 12),
    _CfprVnicIScsiLCPEquipmentDn_Type()
)
cfprVnicIScsiLCPEquipmentDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiLCPEquipmentDn.setStatus("current")
_CfprVnicIScsiLCPFltAggr_Type = Unsigned64
_CfprVnicIScsiLCPFltAggr_Object = MibTableColumn
cfprVnicIScsiLCPFltAggr = _CfprVnicIScsiLCPFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 31, 1, 13),
    _CfprVnicIScsiLCPFltAggr_Type()
)
cfprVnicIScsiLCPFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiLCPFltAggr.setStatus("current")
_CfprVnicIScsiLCPIdentPoolName_Type = SnmpAdminString
_CfprVnicIScsiLCPIdentPoolName_Object = MibTableColumn
cfprVnicIScsiLCPIdentPoolName = _CfprVnicIScsiLCPIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 31, 1, 14),
    _CfprVnicIScsiLCPIdentPoolName_Type()
)
cfprVnicIScsiLCPIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiLCPIdentPoolName.setStatus("current")
_CfprVnicIScsiLCPInstType_Type = CfprVnicInstantiation
_CfprVnicIScsiLCPInstType_Object = MibTableColumn
cfprVnicIScsiLCPInstType = _CfprVnicIScsiLCPInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 31, 1, 15),
    _CfprVnicIScsiLCPInstType_Type()
)
cfprVnicIScsiLCPInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiLCPInstType.setStatus("current")
_CfprVnicIScsiLCPName_Type = SnmpAdminString
_CfprVnicIScsiLCPName_Object = MibTableColumn
cfprVnicIScsiLCPName = _CfprVnicIScsiLCPName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 31, 1, 16),
    _CfprVnicIScsiLCPName_Type()
)
cfprVnicIScsiLCPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiLCPName.setStatus("current")
_CfprVnicIScsiLCPNwTemplName_Type = SnmpAdminString
_CfprVnicIScsiLCPNwTemplName_Object = MibTableColumn
cfprVnicIScsiLCPNwTemplName = _CfprVnicIScsiLCPNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 31, 1, 17),
    _CfprVnicIScsiLCPNwTemplName_Type()
)
cfprVnicIScsiLCPNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiLCPNwTemplName.setStatus("current")
_CfprVnicIScsiLCPOperAdaptorProfileName_Type = SnmpAdminString
_CfprVnicIScsiLCPOperAdaptorProfileName_Object = MibTableColumn
cfprVnicIScsiLCPOperAdaptorProfileName = _CfprVnicIScsiLCPOperAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 31, 1, 18),
    _CfprVnicIScsiLCPOperAdaptorProfileName_Type()
)
cfprVnicIScsiLCPOperAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiLCPOperAdaptorProfileName.setStatus("current")
_CfprVnicIScsiLCPOperHostPort_Type = CfprVnicVnicOperHostPort
_CfprVnicIScsiLCPOperHostPort_Object = MibTableColumn
cfprVnicIScsiLCPOperHostPort = _CfprVnicIScsiLCPOperHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 31, 1, 19),
    _CfprVnicIScsiLCPOperHostPort_Type()
)
cfprVnicIScsiLCPOperHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiLCPOperHostPort.setStatus("current")
_CfprVnicIScsiLCPOperIdentPoolName_Type = SnmpAdminString
_CfprVnicIScsiLCPOperIdentPoolName_Object = MibTableColumn
cfprVnicIScsiLCPOperIdentPoolName = _CfprVnicIScsiLCPOperIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 31, 1, 20),
    _CfprVnicIScsiLCPOperIdentPoolName_Type()
)
cfprVnicIScsiLCPOperIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiLCPOperIdentPoolName.setStatus("current")
_CfprVnicIScsiLCPOperOrder_Type = Gauge32
_CfprVnicIScsiLCPOperOrder_Object = MibTableColumn
cfprVnicIScsiLCPOperOrder = _CfprVnicIScsiLCPOperOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 31, 1, 21),
    _CfprVnicIScsiLCPOperOrder_Type()
)
cfprVnicIScsiLCPOperOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiLCPOperOrder.setStatus("current")
_CfprVnicIScsiLCPOperSpeed_Type = Gauge32
_CfprVnicIScsiLCPOperSpeed_Object = MibTableColumn
cfprVnicIScsiLCPOperSpeed = _CfprVnicIScsiLCPOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 31, 1, 22),
    _CfprVnicIScsiLCPOperSpeed_Type()
)
cfprVnicIScsiLCPOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiLCPOperSpeed.setStatus("current")
_CfprVnicIScsiLCPOperStatsPolicyName_Type = SnmpAdminString
_CfprVnicIScsiLCPOperStatsPolicyName_Object = MibTableColumn
cfprVnicIScsiLCPOperStatsPolicyName = _CfprVnicIScsiLCPOperStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 31, 1, 23),
    _CfprVnicIScsiLCPOperStatsPolicyName_Type()
)
cfprVnicIScsiLCPOperStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiLCPOperStatsPolicyName.setStatus("current")
_CfprVnicIScsiLCPOperVcon_Type = SnmpAdminString
_CfprVnicIScsiLCPOperVcon_Object = MibTableColumn
cfprVnicIScsiLCPOperVcon = _CfprVnicIScsiLCPOperVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 31, 1, 24),
    _CfprVnicIScsiLCPOperVcon_Type()
)
cfprVnicIScsiLCPOperVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiLCPOperVcon.setStatus("current")
_CfprVnicIScsiLCPOrder_Type = Gauge32
_CfprVnicIScsiLCPOrder_Object = MibTableColumn
cfprVnicIScsiLCPOrder = _CfprVnicIScsiLCPOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 31, 1, 25),
    _CfprVnicIScsiLCPOrder_Type()
)
cfprVnicIScsiLCPOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiLCPOrder.setStatus("current")
_CfprVnicIScsiLCPOwner_Type = CfprVnicConnectionOwner
_CfprVnicIScsiLCPOwner_Object = MibTableColumn
cfprVnicIScsiLCPOwner = _CfprVnicIScsiLCPOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 31, 1, 26),
    _CfprVnicIScsiLCPOwner_Type()
)
cfprVnicIScsiLCPOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiLCPOwner.setStatus("current")
_CfprVnicIScsiLCPPinToGroupName_Type = SnmpAdminString
_CfprVnicIScsiLCPPinToGroupName_Object = MibTableColumn
cfprVnicIScsiLCPPinToGroupName = _CfprVnicIScsiLCPPinToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 31, 1, 27),
    _CfprVnicIScsiLCPPinToGroupName_Type()
)
cfprVnicIScsiLCPPinToGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiLCPPinToGroupName.setStatus("current")
_CfprVnicIScsiLCPQosPolicyName_Type = SnmpAdminString
_CfprVnicIScsiLCPQosPolicyName_Object = MibTableColumn
cfprVnicIScsiLCPQosPolicyName = _CfprVnicIScsiLCPQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 31, 1, 28),
    _CfprVnicIScsiLCPQosPolicyName_Type()
)
cfprVnicIScsiLCPQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiLCPQosPolicyName.setStatus("current")
_CfprVnicIScsiLCPStatsPolicyName_Type = SnmpAdminString
_CfprVnicIScsiLCPStatsPolicyName_Object = MibTableColumn
cfprVnicIScsiLCPStatsPolicyName = _CfprVnicIScsiLCPStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 31, 1, 29),
    _CfprVnicIScsiLCPStatsPolicyName_Type()
)
cfprVnicIScsiLCPStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiLCPStatsPolicyName.setStatus("current")
_CfprVnicIScsiLCPSwitchId_Type = CfprNetworkSwitchId
_CfprVnicIScsiLCPSwitchId_Object = MibTableColumn
cfprVnicIScsiLCPSwitchId = _CfprVnicIScsiLCPSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 31, 1, 30),
    _CfprVnicIScsiLCPSwitchId_Type()
)
cfprVnicIScsiLCPSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiLCPSwitchId.setStatus("current")
_CfprVnicIScsiLCPType_Type = CfprVnicConnectionType
_CfprVnicIScsiLCPType_Object = MibTableColumn
cfprVnicIScsiLCPType = _CfprVnicIScsiLCPType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 31, 1, 31),
    _CfprVnicIScsiLCPType_Type()
)
cfprVnicIScsiLCPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiLCPType.setStatus("current")
_CfprVnicIScsiLCPVnicName_Type = SnmpAdminString
_CfprVnicIScsiLCPVnicName_Object = MibTableColumn
cfprVnicIScsiLCPVnicName = _CfprVnicIScsiLCPVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 31, 1, 32),
    _CfprVnicIScsiLCPVnicName_Type()
)
cfprVnicIScsiLCPVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiLCPVnicName.setStatus("current")
_CfprVnicIScsiNodeTable_Object = MibTable
cfprVnicIScsiNodeTable = _CfprVnicIScsiNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 32)
)
if mibBuilder.loadTexts:
    cfprVnicIScsiNodeTable.setStatus("current")
_CfprVnicIScsiNodeEntry_Object = MibTableRow
cfprVnicIScsiNodeEntry = _CfprVnicIScsiNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 32, 1)
)
cfprVnicIScsiNodeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicIScsiNodeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicIScsiNodeEntry.setStatus("current")
_CfprVnicIScsiNodeInstanceId_Type = CfprManagedObjectId
_CfprVnicIScsiNodeInstanceId_Object = MibTableColumn
cfprVnicIScsiNodeInstanceId = _CfprVnicIScsiNodeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 32, 1, 1),
    _CfprVnicIScsiNodeInstanceId_Type()
)
cfprVnicIScsiNodeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicIScsiNodeInstanceId.setStatus("current")
_CfprVnicIScsiNodeDn_Type = CfprManagedObjectDn
_CfprVnicIScsiNodeDn_Object = MibTableColumn
cfprVnicIScsiNodeDn = _CfprVnicIScsiNodeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 32, 1, 2),
    _CfprVnicIScsiNodeDn_Type()
)
cfprVnicIScsiNodeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiNodeDn.setStatus("current")
_CfprVnicIScsiNodeRn_Type = SnmpAdminString
_CfprVnicIScsiNodeRn_Object = MibTableColumn
cfprVnicIScsiNodeRn = _CfprVnicIScsiNodeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 32, 1, 3),
    _CfprVnicIScsiNodeRn_Type()
)
cfprVnicIScsiNodeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiNodeRn.setStatus("current")
_CfprVnicIScsiNodeFltAggr_Type = Unsigned64
_CfprVnicIScsiNodeFltAggr_Object = MibTableColumn
cfprVnicIScsiNodeFltAggr = _CfprVnicIScsiNodeFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 32, 1, 4),
    _CfprVnicIScsiNodeFltAggr_Type()
)
cfprVnicIScsiNodeFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiNodeFltAggr.setStatus("current")
_CfprVnicIScsiNodeInitNameSuffix_Type = SnmpAdminString
_CfprVnicIScsiNodeInitNameSuffix_Object = MibTableColumn
cfprVnicIScsiNodeInitNameSuffix = _CfprVnicIScsiNodeInitNameSuffix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 32, 1, 5),
    _CfprVnicIScsiNodeInitNameSuffix_Type()
)
cfprVnicIScsiNodeInitNameSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiNodeInitNameSuffix.setStatus("current")
_CfprVnicIScsiNodeInitiatorName_Type = SnmpAdminString
_CfprVnicIScsiNodeInitiatorName_Object = MibTableColumn
cfprVnicIScsiNodeInitiatorName = _CfprVnicIScsiNodeInitiatorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 32, 1, 6),
    _CfprVnicIScsiNodeInitiatorName_Type()
)
cfprVnicIScsiNodeInitiatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiNodeInitiatorName.setStatus("current")
_CfprVnicIScsiNodeIqnIdentPoolName_Type = SnmpAdminString
_CfprVnicIScsiNodeIqnIdentPoolName_Object = MibTableColumn
cfprVnicIScsiNodeIqnIdentPoolName = _CfprVnicIScsiNodeIqnIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 32, 1, 7),
    _CfprVnicIScsiNodeIqnIdentPoolName_Type()
)
cfprVnicIScsiNodeIqnIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiNodeIqnIdentPoolName.setStatus("current")
_CfprVnicIScsiNodeOperIqnIdentPoolName_Type = SnmpAdminString
_CfprVnicIScsiNodeOperIqnIdentPoolName_Object = MibTableColumn
cfprVnicIScsiNodeOperIqnIdentPoolName = _CfprVnicIScsiNodeOperIqnIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 32, 1, 8),
    _CfprVnicIScsiNodeOperIqnIdentPoolName_Type()
)
cfprVnicIScsiNodeOperIqnIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiNodeOperIqnIdentPoolName.setStatus("current")
_CfprVnicIScsiNodeOwner_Type = CfprVnicIScsiNodeOwner
_CfprVnicIScsiNodeOwner_Object = MibTableColumn
cfprVnicIScsiNodeOwner = _CfprVnicIScsiNodeOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 32, 1, 9),
    _CfprVnicIScsiNodeOwner_Type()
)
cfprVnicIScsiNodeOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiNodeOwner.setStatus("current")
_CfprVnicIScsiStaticTargetIfTable_Object = MibTable
cfprVnicIScsiStaticTargetIfTable = _CfprVnicIScsiStaticTargetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 33)
)
if mibBuilder.loadTexts:
    cfprVnicIScsiStaticTargetIfTable.setStatus("current")
_CfprVnicIScsiStaticTargetIfEntry_Object = MibTableRow
cfprVnicIScsiStaticTargetIfEntry = _CfprVnicIScsiStaticTargetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 33, 1)
)
cfprVnicIScsiStaticTargetIfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicIScsiStaticTargetIfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicIScsiStaticTargetIfEntry.setStatus("current")
_CfprVnicIScsiStaticTargetIfInstanceId_Type = CfprManagedObjectId
_CfprVnicIScsiStaticTargetIfInstanceId_Object = MibTableColumn
cfprVnicIScsiStaticTargetIfInstanceId = _CfprVnicIScsiStaticTargetIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 33, 1, 1),
    _CfprVnicIScsiStaticTargetIfInstanceId_Type()
)
cfprVnicIScsiStaticTargetIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicIScsiStaticTargetIfInstanceId.setStatus("current")
_CfprVnicIScsiStaticTargetIfDn_Type = CfprManagedObjectDn
_CfprVnicIScsiStaticTargetIfDn_Object = MibTableColumn
cfprVnicIScsiStaticTargetIfDn = _CfprVnicIScsiStaticTargetIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 33, 1, 2),
    _CfprVnicIScsiStaticTargetIfDn_Type()
)
cfprVnicIScsiStaticTargetIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiStaticTargetIfDn.setStatus("current")
_CfprVnicIScsiStaticTargetIfRn_Type = SnmpAdminString
_CfprVnicIScsiStaticTargetIfRn_Object = MibTableColumn
cfprVnicIScsiStaticTargetIfRn = _CfprVnicIScsiStaticTargetIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 33, 1, 3),
    _CfprVnicIScsiStaticTargetIfRn_Type()
)
cfprVnicIScsiStaticTargetIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiStaticTargetIfRn.setStatus("current")
_CfprVnicIScsiStaticTargetIfAuthProfileName_Type = SnmpAdminString
_CfprVnicIScsiStaticTargetIfAuthProfileName_Object = MibTableColumn
cfprVnicIScsiStaticTargetIfAuthProfileName = _CfprVnicIScsiStaticTargetIfAuthProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 33, 1, 4),
    _CfprVnicIScsiStaticTargetIfAuthProfileName_Type()
)
cfprVnicIScsiStaticTargetIfAuthProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiStaticTargetIfAuthProfileName.setStatus("current")
_CfprVnicIScsiStaticTargetIfIpAddress_Type = InetAddressIPv4
_CfprVnicIScsiStaticTargetIfIpAddress_Object = MibTableColumn
cfprVnicIScsiStaticTargetIfIpAddress = _CfprVnicIScsiStaticTargetIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 33, 1, 5),
    _CfprVnicIScsiStaticTargetIfIpAddress_Type()
)
cfprVnicIScsiStaticTargetIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiStaticTargetIfIpAddress.setStatus("current")
_CfprVnicIScsiStaticTargetIfName_Type = SnmpAdminString
_CfprVnicIScsiStaticTargetIfName_Object = MibTableColumn
cfprVnicIScsiStaticTargetIfName = _CfprVnicIScsiStaticTargetIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 33, 1, 6),
    _CfprVnicIScsiStaticTargetIfName_Type()
)
cfprVnicIScsiStaticTargetIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiStaticTargetIfName.setStatus("current")
_CfprVnicIScsiStaticTargetIfOperAuthProfileName_Type = SnmpAdminString
_CfprVnicIScsiStaticTargetIfOperAuthProfileName_Object = MibTableColumn
cfprVnicIScsiStaticTargetIfOperAuthProfileName = _CfprVnicIScsiStaticTargetIfOperAuthProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 33, 1, 7),
    _CfprVnicIScsiStaticTargetIfOperAuthProfileName_Type()
)
cfprVnicIScsiStaticTargetIfOperAuthProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiStaticTargetIfOperAuthProfileName.setStatus("current")
_CfprVnicIScsiStaticTargetIfPort_Type = Gauge32
_CfprVnicIScsiStaticTargetIfPort_Object = MibTableColumn
cfprVnicIScsiStaticTargetIfPort = _CfprVnicIScsiStaticTargetIfPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 33, 1, 8),
    _CfprVnicIScsiStaticTargetIfPort_Type()
)
cfprVnicIScsiStaticTargetIfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiStaticTargetIfPort.setStatus("current")
_CfprVnicIScsiStaticTargetIfPriority_Type = Gauge32
_CfprVnicIScsiStaticTargetIfPriority_Object = MibTableColumn
cfprVnicIScsiStaticTargetIfPriority = _CfprVnicIScsiStaticTargetIfPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 33, 1, 9),
    _CfprVnicIScsiStaticTargetIfPriority_Type()
)
cfprVnicIScsiStaticTargetIfPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIScsiStaticTargetIfPriority.setStatus("current")
_CfprVnicInternalProfileTable_Object = MibTable
cfprVnicInternalProfileTable = _CfprVnicInternalProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 34)
)
if mibBuilder.loadTexts:
    cfprVnicInternalProfileTable.setStatus("current")
_CfprVnicInternalProfileEntry_Object = MibTableRow
cfprVnicInternalProfileEntry = _CfprVnicInternalProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 34, 1)
)
cfprVnicInternalProfileEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicInternalProfileInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicInternalProfileEntry.setStatus("current")
_CfprVnicInternalProfileInstanceId_Type = CfprManagedObjectId
_CfprVnicInternalProfileInstanceId_Object = MibTableColumn
cfprVnicInternalProfileInstanceId = _CfprVnicInternalProfileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 34, 1, 1),
    _CfprVnicInternalProfileInstanceId_Type()
)
cfprVnicInternalProfileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicInternalProfileInstanceId.setStatus("current")
_CfprVnicInternalProfileDn_Type = CfprManagedObjectDn
_CfprVnicInternalProfileDn_Object = MibTableColumn
cfprVnicInternalProfileDn = _CfprVnicInternalProfileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 34, 1, 2),
    _CfprVnicInternalProfileDn_Type()
)
cfprVnicInternalProfileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicInternalProfileDn.setStatus("current")
_CfprVnicInternalProfileRn_Type = SnmpAdminString
_CfprVnicInternalProfileRn_Object = MibTableColumn
cfprVnicInternalProfileRn = _CfprVnicInternalProfileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 34, 1, 3),
    _CfprVnicInternalProfileRn_Type()
)
cfprVnicInternalProfileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicInternalProfileRn.setStatus("current")
_CfprVnicInternalProfileDescr_Type = SnmpAdminString
_CfprVnicInternalProfileDescr_Object = MibTableColumn
cfprVnicInternalProfileDescr = _CfprVnicInternalProfileDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 34, 1, 4),
    _CfprVnicInternalProfileDescr_Type()
)
cfprVnicInternalProfileDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicInternalProfileDescr.setStatus("current")
_CfprVnicInternalProfileIntId_Type = SnmpAdminString
_CfprVnicInternalProfileIntId_Object = MibTableColumn
cfprVnicInternalProfileIntId = _CfprVnicInternalProfileIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 34, 1, 5),
    _CfprVnicInternalProfileIntId_Type()
)
cfprVnicInternalProfileIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicInternalProfileIntId.setStatus("current")
_CfprVnicInternalProfileMaxPorts_Type = Gauge32
_CfprVnicInternalProfileMaxPorts_Object = MibTableColumn
cfprVnicInternalProfileMaxPorts = _CfprVnicInternalProfileMaxPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 34, 1, 6),
    _CfprVnicInternalProfileMaxPorts_Type()
)
cfprVnicInternalProfileMaxPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicInternalProfileMaxPorts.setStatus("current")
_CfprVnicInternalProfileName_Type = SnmpAdminString
_CfprVnicInternalProfileName_Object = MibTableColumn
cfprVnicInternalProfileName = _CfprVnicInternalProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 34, 1, 7),
    _CfprVnicInternalProfileName_Type()
)
cfprVnicInternalProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicInternalProfileName.setStatus("current")
_CfprVnicInternalProfilePolicyLevel_Type = Gauge32
_CfprVnicInternalProfilePolicyLevel_Object = MibTableColumn
cfprVnicInternalProfilePolicyLevel = _CfprVnicInternalProfilePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 34, 1, 8),
    _CfprVnicInternalProfilePolicyLevel_Type()
)
cfprVnicInternalProfilePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicInternalProfilePolicyLevel.setStatus("current")
_CfprVnicInternalProfilePolicyOwner_Type = CfprPolicyPolicyOwner
_CfprVnicInternalProfilePolicyOwner_Object = MibTableColumn
cfprVnicInternalProfilePolicyOwner = _CfprVnicInternalProfilePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 34, 1, 9),
    _CfprVnicInternalProfilePolicyOwner_Type()
)
cfprVnicInternalProfilePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicInternalProfilePolicyOwner.setStatus("current")
_CfprVnicIpV4HistoryTable_Object = MibTable
cfprVnicIpV4HistoryTable = _CfprVnicIpV4HistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 35)
)
if mibBuilder.loadTexts:
    cfprVnicIpV4HistoryTable.setStatus("current")
_CfprVnicIpV4HistoryEntry_Object = MibTableRow
cfprVnicIpV4HistoryEntry = _CfprVnicIpV4HistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 35, 1)
)
cfprVnicIpV4HistoryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicIpV4HistoryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicIpV4HistoryEntry.setStatus("current")
_CfprVnicIpV4HistoryInstanceId_Type = CfprManagedObjectId
_CfprVnicIpV4HistoryInstanceId_Object = MibTableColumn
cfprVnicIpV4HistoryInstanceId = _CfprVnicIpV4HistoryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 35, 1, 1),
    _CfprVnicIpV4HistoryInstanceId_Type()
)
cfprVnicIpV4HistoryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicIpV4HistoryInstanceId.setStatus("current")
_CfprVnicIpV4HistoryDn_Type = CfprManagedObjectDn
_CfprVnicIpV4HistoryDn_Object = MibTableColumn
cfprVnicIpV4HistoryDn = _CfprVnicIpV4HistoryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 35, 1, 2),
    _CfprVnicIpV4HistoryDn_Type()
)
cfprVnicIpV4HistoryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV4HistoryDn.setStatus("current")
_CfprVnicIpV4HistoryRn_Type = SnmpAdminString
_CfprVnicIpV4HistoryRn_Object = MibTableColumn
cfprVnicIpV4HistoryRn = _CfprVnicIpV4HistoryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 35, 1, 3),
    _CfprVnicIpV4HistoryRn_Type()
)
cfprVnicIpV4HistoryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV4HistoryRn.setStatus("current")
_CfprVnicIpV4HistoryOldIpV4Addr_Type = InetAddressIPv4
_CfprVnicIpV4HistoryOldIpV4Addr_Object = MibTableColumn
cfprVnicIpV4HistoryOldIpV4Addr = _CfprVnicIpV4HistoryOldIpV4Addr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 35, 1, 4),
    _CfprVnicIpV4HistoryOldIpV4Addr_Type()
)
cfprVnicIpV4HistoryOldIpV4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV4HistoryOldIpV4Addr.setStatus("current")
_CfprVnicIpV4MgmtPooledAddrTable_Object = MibTable
cfprVnicIpV4MgmtPooledAddrTable = _CfprVnicIpV4MgmtPooledAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 36)
)
if mibBuilder.loadTexts:
    cfprVnicIpV4MgmtPooledAddrTable.setStatus("current")
_CfprVnicIpV4MgmtPooledAddrEntry_Object = MibTableRow
cfprVnicIpV4MgmtPooledAddrEntry = _CfprVnicIpV4MgmtPooledAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 36, 1)
)
cfprVnicIpV4MgmtPooledAddrEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicIpV4MgmtPooledAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicIpV4MgmtPooledAddrEntry.setStatus("current")
_CfprVnicIpV4MgmtPooledAddrInstanceId_Type = CfprManagedObjectId
_CfprVnicIpV4MgmtPooledAddrInstanceId_Object = MibTableColumn
cfprVnicIpV4MgmtPooledAddrInstanceId = _CfprVnicIpV4MgmtPooledAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 36, 1, 1),
    _CfprVnicIpV4MgmtPooledAddrInstanceId_Type()
)
cfprVnicIpV4MgmtPooledAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicIpV4MgmtPooledAddrInstanceId.setStatus("current")
_CfprVnicIpV4MgmtPooledAddrDn_Type = CfprManagedObjectDn
_CfprVnicIpV4MgmtPooledAddrDn_Object = MibTableColumn
cfprVnicIpV4MgmtPooledAddrDn = _CfprVnicIpV4MgmtPooledAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 36, 1, 2),
    _CfprVnicIpV4MgmtPooledAddrDn_Type()
)
cfprVnicIpV4MgmtPooledAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV4MgmtPooledAddrDn.setStatus("current")
_CfprVnicIpV4MgmtPooledAddrRn_Type = SnmpAdminString
_CfprVnicIpV4MgmtPooledAddrRn_Object = MibTableColumn
cfprVnicIpV4MgmtPooledAddrRn = _CfprVnicIpV4MgmtPooledAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 36, 1, 3),
    _CfprVnicIpV4MgmtPooledAddrRn_Type()
)
cfprVnicIpV4MgmtPooledAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV4MgmtPooledAddrRn.setStatus("current")
_CfprVnicIpV4MgmtPooledAddrAddr_Type = InetAddressIPv4
_CfprVnicIpV4MgmtPooledAddrAddr_Object = MibTableColumn
cfprVnicIpV4MgmtPooledAddrAddr = _CfprVnicIpV4MgmtPooledAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 36, 1, 4),
    _CfprVnicIpV4MgmtPooledAddrAddr_Type()
)
cfprVnicIpV4MgmtPooledAddrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV4MgmtPooledAddrAddr.setStatus("current")
_CfprVnicIpV4MgmtPooledAddrDefGw_Type = InetAddressIPv4
_CfprVnicIpV4MgmtPooledAddrDefGw_Object = MibTableColumn
cfprVnicIpV4MgmtPooledAddrDefGw = _CfprVnicIpV4MgmtPooledAddrDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 36, 1, 5),
    _CfprVnicIpV4MgmtPooledAddrDefGw_Type()
)
cfprVnicIpV4MgmtPooledAddrDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV4MgmtPooledAddrDefGw.setStatus("current")
_CfprVnicIpV4MgmtPooledAddrName_Type = SnmpAdminString
_CfprVnicIpV4MgmtPooledAddrName_Object = MibTableColumn
cfprVnicIpV4MgmtPooledAddrName = _CfprVnicIpV4MgmtPooledAddrName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 36, 1, 6),
    _CfprVnicIpV4MgmtPooledAddrName_Type()
)
cfprVnicIpV4MgmtPooledAddrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV4MgmtPooledAddrName.setStatus("current")
_CfprVnicIpV4MgmtPooledAddrOperName_Type = SnmpAdminString
_CfprVnicIpV4MgmtPooledAddrOperName_Object = MibTableColumn
cfprVnicIpV4MgmtPooledAddrOperName = _CfprVnicIpV4MgmtPooledAddrOperName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 36, 1, 7),
    _CfprVnicIpV4MgmtPooledAddrOperName_Type()
)
cfprVnicIpV4MgmtPooledAddrOperName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV4MgmtPooledAddrOperName.setStatus("current")
_CfprVnicIpV4MgmtPooledAddrPrimDns_Type = InetAddressIPv4
_CfprVnicIpV4MgmtPooledAddrPrimDns_Object = MibTableColumn
cfprVnicIpV4MgmtPooledAddrPrimDns = _CfprVnicIpV4MgmtPooledAddrPrimDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 36, 1, 8),
    _CfprVnicIpV4MgmtPooledAddrPrimDns_Type()
)
cfprVnicIpV4MgmtPooledAddrPrimDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV4MgmtPooledAddrPrimDns.setStatus("current")
_CfprVnicIpV4MgmtPooledAddrSecDns_Type = InetAddressIPv4
_CfprVnicIpV4MgmtPooledAddrSecDns_Object = MibTableColumn
cfprVnicIpV4MgmtPooledAddrSecDns = _CfprVnicIpV4MgmtPooledAddrSecDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 36, 1, 9),
    _CfprVnicIpV4MgmtPooledAddrSecDns_Type()
)
cfprVnicIpV4MgmtPooledAddrSecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV4MgmtPooledAddrSecDns.setStatus("current")
_CfprVnicIpV4MgmtPooledAddrSubnet_Type = InetAddressIPv4
_CfprVnicIpV4MgmtPooledAddrSubnet_Object = MibTableColumn
cfprVnicIpV4MgmtPooledAddrSubnet = _CfprVnicIpV4MgmtPooledAddrSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 36, 1, 10),
    _CfprVnicIpV4MgmtPooledAddrSubnet_Type()
)
cfprVnicIpV4MgmtPooledAddrSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV4MgmtPooledAddrSubnet.setStatus("current")
_CfprVnicIpV4PooledAddrTable_Object = MibTable
cfprVnicIpV4PooledAddrTable = _CfprVnicIpV4PooledAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 37)
)
if mibBuilder.loadTexts:
    cfprVnicIpV4PooledAddrTable.setStatus("current")
_CfprVnicIpV4PooledAddrEntry_Object = MibTableRow
cfprVnicIpV4PooledAddrEntry = _CfprVnicIpV4PooledAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 37, 1)
)
cfprVnicIpV4PooledAddrEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicIpV4PooledAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicIpV4PooledAddrEntry.setStatus("current")
_CfprVnicIpV4PooledAddrInstanceId_Type = CfprManagedObjectId
_CfprVnicIpV4PooledAddrInstanceId_Object = MibTableColumn
cfprVnicIpV4PooledAddrInstanceId = _CfprVnicIpV4PooledAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 37, 1, 1),
    _CfprVnicIpV4PooledAddrInstanceId_Type()
)
cfprVnicIpV4PooledAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicIpV4PooledAddrInstanceId.setStatus("current")
_CfprVnicIpV4PooledAddrDn_Type = CfprManagedObjectDn
_CfprVnicIpV4PooledAddrDn_Object = MibTableColumn
cfprVnicIpV4PooledAddrDn = _CfprVnicIpV4PooledAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 37, 1, 2),
    _CfprVnicIpV4PooledAddrDn_Type()
)
cfprVnicIpV4PooledAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV4PooledAddrDn.setStatus("current")
_CfprVnicIpV4PooledAddrRn_Type = SnmpAdminString
_CfprVnicIpV4PooledAddrRn_Object = MibTableColumn
cfprVnicIpV4PooledAddrRn = _CfprVnicIpV4PooledAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 37, 1, 3),
    _CfprVnicIpV4PooledAddrRn_Type()
)
cfprVnicIpV4PooledAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV4PooledAddrRn.setStatus("current")
_CfprVnicIpV4PooledAddrAddr_Type = InetAddressIPv4
_CfprVnicIpV4PooledAddrAddr_Object = MibTableColumn
cfprVnicIpV4PooledAddrAddr = _CfprVnicIpV4PooledAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 37, 1, 4),
    _CfprVnicIpV4PooledAddrAddr_Type()
)
cfprVnicIpV4PooledAddrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV4PooledAddrAddr.setStatus("current")
_CfprVnicIpV4PooledAddrDefGw_Type = InetAddressIPv4
_CfprVnicIpV4PooledAddrDefGw_Object = MibTableColumn
cfprVnicIpV4PooledAddrDefGw = _CfprVnicIpV4PooledAddrDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 37, 1, 5),
    _CfprVnicIpV4PooledAddrDefGw_Type()
)
cfprVnicIpV4PooledAddrDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV4PooledAddrDefGw.setStatus("current")
_CfprVnicIpV4PooledAddrName_Type = SnmpAdminString
_CfprVnicIpV4PooledAddrName_Object = MibTableColumn
cfprVnicIpV4PooledAddrName = _CfprVnicIpV4PooledAddrName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 37, 1, 6),
    _CfprVnicIpV4PooledAddrName_Type()
)
cfprVnicIpV4PooledAddrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV4PooledAddrName.setStatus("current")
_CfprVnicIpV4PooledAddrOperName_Type = SnmpAdminString
_CfprVnicIpV4PooledAddrOperName_Object = MibTableColumn
cfprVnicIpV4PooledAddrOperName = _CfprVnicIpV4PooledAddrOperName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 37, 1, 7),
    _CfprVnicIpV4PooledAddrOperName_Type()
)
cfprVnicIpV4PooledAddrOperName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV4PooledAddrOperName.setStatus("current")
_CfprVnicIpV4PooledAddrPrimDns_Type = InetAddressIPv4
_CfprVnicIpV4PooledAddrPrimDns_Object = MibTableColumn
cfprVnicIpV4PooledAddrPrimDns = _CfprVnicIpV4PooledAddrPrimDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 37, 1, 8),
    _CfprVnicIpV4PooledAddrPrimDns_Type()
)
cfprVnicIpV4PooledAddrPrimDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV4PooledAddrPrimDns.setStatus("current")
_CfprVnicIpV4PooledAddrSecDns_Type = InetAddressIPv4
_CfprVnicIpV4PooledAddrSecDns_Object = MibTableColumn
cfprVnicIpV4PooledAddrSecDns = _CfprVnicIpV4PooledAddrSecDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 37, 1, 9),
    _CfprVnicIpV4PooledAddrSecDns_Type()
)
cfprVnicIpV4PooledAddrSecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV4PooledAddrSecDns.setStatus("current")
_CfprVnicIpV4PooledAddrSubnet_Type = InetAddressIPv4
_CfprVnicIpV4PooledAddrSubnet_Object = MibTableColumn
cfprVnicIpV4PooledAddrSubnet = _CfprVnicIpV4PooledAddrSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 37, 1, 10),
    _CfprVnicIpV4PooledAddrSubnet_Type()
)
cfprVnicIpV4PooledAddrSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV4PooledAddrSubnet.setStatus("current")
_CfprVnicIpV4ProfDerivedAddrTable_Object = MibTable
cfprVnicIpV4ProfDerivedAddrTable = _CfprVnicIpV4ProfDerivedAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 38)
)
if mibBuilder.loadTexts:
    cfprVnicIpV4ProfDerivedAddrTable.setStatus("current")
_CfprVnicIpV4ProfDerivedAddrEntry_Object = MibTableRow
cfprVnicIpV4ProfDerivedAddrEntry = _CfprVnicIpV4ProfDerivedAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 38, 1)
)
cfprVnicIpV4ProfDerivedAddrEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicIpV4ProfDerivedAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicIpV4ProfDerivedAddrEntry.setStatus("current")
_CfprVnicIpV4ProfDerivedAddrInstanceId_Type = CfprManagedObjectId
_CfprVnicIpV4ProfDerivedAddrInstanceId_Object = MibTableColumn
cfprVnicIpV4ProfDerivedAddrInstanceId = _CfprVnicIpV4ProfDerivedAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 38, 1, 1),
    _CfprVnicIpV4ProfDerivedAddrInstanceId_Type()
)
cfprVnicIpV4ProfDerivedAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicIpV4ProfDerivedAddrInstanceId.setStatus("current")
_CfprVnicIpV4ProfDerivedAddrDn_Type = CfprManagedObjectDn
_CfprVnicIpV4ProfDerivedAddrDn_Object = MibTableColumn
cfprVnicIpV4ProfDerivedAddrDn = _CfprVnicIpV4ProfDerivedAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 38, 1, 2),
    _CfprVnicIpV4ProfDerivedAddrDn_Type()
)
cfprVnicIpV4ProfDerivedAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV4ProfDerivedAddrDn.setStatus("current")
_CfprVnicIpV4ProfDerivedAddrRn_Type = SnmpAdminString
_CfprVnicIpV4ProfDerivedAddrRn_Object = MibTableColumn
cfprVnicIpV4ProfDerivedAddrRn = _CfprVnicIpV4ProfDerivedAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 38, 1, 3),
    _CfprVnicIpV4ProfDerivedAddrRn_Type()
)
cfprVnicIpV4ProfDerivedAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV4ProfDerivedAddrRn.setStatus("current")
_CfprVnicIpV4ProfDerivedAddrAddr_Type = InetAddressIPv4
_CfprVnicIpV4ProfDerivedAddrAddr_Object = MibTableColumn
cfprVnicIpV4ProfDerivedAddrAddr = _CfprVnicIpV4ProfDerivedAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 38, 1, 4),
    _CfprVnicIpV4ProfDerivedAddrAddr_Type()
)
cfprVnicIpV4ProfDerivedAddrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV4ProfDerivedAddrAddr.setStatus("current")
_CfprVnicIpV4ProfDerivedAddrDefGw_Type = InetAddressIPv4
_CfprVnicIpV4ProfDerivedAddrDefGw_Object = MibTableColumn
cfprVnicIpV4ProfDerivedAddrDefGw = _CfprVnicIpV4ProfDerivedAddrDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 38, 1, 5),
    _CfprVnicIpV4ProfDerivedAddrDefGw_Type()
)
cfprVnicIpV4ProfDerivedAddrDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV4ProfDerivedAddrDefGw.setStatus("current")
_CfprVnicIpV4ProfDerivedAddrSubnet_Type = InetAddressIPv4
_CfprVnicIpV4ProfDerivedAddrSubnet_Object = MibTableColumn
cfprVnicIpV4ProfDerivedAddrSubnet = _CfprVnicIpV4ProfDerivedAddrSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 38, 1, 6),
    _CfprVnicIpV4ProfDerivedAddrSubnet_Type()
)
cfprVnicIpV4ProfDerivedAddrSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV4ProfDerivedAddrSubnet.setStatus("current")
_CfprVnicIpV4StaticAddrTable_Object = MibTable
cfprVnicIpV4StaticAddrTable = _CfprVnicIpV4StaticAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 39)
)
if mibBuilder.loadTexts:
    cfprVnicIpV4StaticAddrTable.setStatus("current")
_CfprVnicIpV4StaticAddrEntry_Object = MibTableRow
cfprVnicIpV4StaticAddrEntry = _CfprVnicIpV4StaticAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 39, 1)
)
cfprVnicIpV4StaticAddrEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicIpV4StaticAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicIpV4StaticAddrEntry.setStatus("current")
_CfprVnicIpV4StaticAddrInstanceId_Type = CfprManagedObjectId
_CfprVnicIpV4StaticAddrInstanceId_Object = MibTableColumn
cfprVnicIpV4StaticAddrInstanceId = _CfprVnicIpV4StaticAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 39, 1, 1),
    _CfprVnicIpV4StaticAddrInstanceId_Type()
)
cfprVnicIpV4StaticAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicIpV4StaticAddrInstanceId.setStatus("current")
_CfprVnicIpV4StaticAddrDn_Type = CfprManagedObjectDn
_CfprVnicIpV4StaticAddrDn_Object = MibTableColumn
cfprVnicIpV4StaticAddrDn = _CfprVnicIpV4StaticAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 39, 1, 2),
    _CfprVnicIpV4StaticAddrDn_Type()
)
cfprVnicIpV4StaticAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV4StaticAddrDn.setStatus("current")
_CfprVnicIpV4StaticAddrRn_Type = SnmpAdminString
_CfprVnicIpV4StaticAddrRn_Object = MibTableColumn
cfprVnicIpV4StaticAddrRn = _CfprVnicIpV4StaticAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 39, 1, 3),
    _CfprVnicIpV4StaticAddrRn_Type()
)
cfprVnicIpV4StaticAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV4StaticAddrRn.setStatus("current")
_CfprVnicIpV4StaticAddrAddr_Type = InetAddressIPv4
_CfprVnicIpV4StaticAddrAddr_Object = MibTableColumn
cfprVnicIpV4StaticAddrAddr = _CfprVnicIpV4StaticAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 39, 1, 4),
    _CfprVnicIpV4StaticAddrAddr_Type()
)
cfprVnicIpV4StaticAddrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV4StaticAddrAddr.setStatus("current")
_CfprVnicIpV4StaticAddrDefGw_Type = InetAddressIPv4
_CfprVnicIpV4StaticAddrDefGw_Object = MibTableColumn
cfprVnicIpV4StaticAddrDefGw = _CfprVnicIpV4StaticAddrDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 39, 1, 5),
    _CfprVnicIpV4StaticAddrDefGw_Type()
)
cfprVnicIpV4StaticAddrDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV4StaticAddrDefGw.setStatus("current")
_CfprVnicIpV4StaticAddrPrimDns_Type = InetAddressIPv4
_CfprVnicIpV4StaticAddrPrimDns_Object = MibTableColumn
cfprVnicIpV4StaticAddrPrimDns = _CfprVnicIpV4StaticAddrPrimDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 39, 1, 6),
    _CfprVnicIpV4StaticAddrPrimDns_Type()
)
cfprVnicIpV4StaticAddrPrimDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV4StaticAddrPrimDns.setStatus("current")
_CfprVnicIpV4StaticAddrSecDns_Type = InetAddressIPv4
_CfprVnicIpV4StaticAddrSecDns_Object = MibTableColumn
cfprVnicIpV4StaticAddrSecDns = _CfprVnicIpV4StaticAddrSecDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 39, 1, 7),
    _CfprVnicIpV4StaticAddrSecDns_Type()
)
cfprVnicIpV4StaticAddrSecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV4StaticAddrSecDns.setStatus("current")
_CfprVnicIpV4StaticAddrSubnet_Type = InetAddressIPv4
_CfprVnicIpV4StaticAddrSubnet_Object = MibTableColumn
cfprVnicIpV4StaticAddrSubnet = _CfprVnicIpV4StaticAddrSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 39, 1, 8),
    _CfprVnicIpV4StaticAddrSubnet_Type()
)
cfprVnicIpV4StaticAddrSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV4StaticAddrSubnet.setStatus("current")
_CfprVnicIpV6HistoryTable_Object = MibTable
cfprVnicIpV6HistoryTable = _CfprVnicIpV6HistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 40)
)
if mibBuilder.loadTexts:
    cfprVnicIpV6HistoryTable.setStatus("current")
_CfprVnicIpV6HistoryEntry_Object = MibTableRow
cfprVnicIpV6HistoryEntry = _CfprVnicIpV6HistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 40, 1)
)
cfprVnicIpV6HistoryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicIpV6HistoryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicIpV6HistoryEntry.setStatus("current")
_CfprVnicIpV6HistoryInstanceId_Type = CfprManagedObjectId
_CfprVnicIpV6HistoryInstanceId_Object = MibTableColumn
cfprVnicIpV6HistoryInstanceId = _CfprVnicIpV6HistoryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 40, 1, 1),
    _CfprVnicIpV6HistoryInstanceId_Type()
)
cfprVnicIpV6HistoryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicIpV6HistoryInstanceId.setStatus("current")
_CfprVnicIpV6HistoryDn_Type = CfprManagedObjectDn
_CfprVnicIpV6HistoryDn_Object = MibTableColumn
cfprVnicIpV6HistoryDn = _CfprVnicIpV6HistoryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 40, 1, 2),
    _CfprVnicIpV6HistoryDn_Type()
)
cfprVnicIpV6HistoryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV6HistoryDn.setStatus("current")
_CfprVnicIpV6HistoryRn_Type = SnmpAdminString
_CfprVnicIpV6HistoryRn_Object = MibTableColumn
cfprVnicIpV6HistoryRn = _CfprVnicIpV6HistoryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 40, 1, 3),
    _CfprVnicIpV6HistoryRn_Type()
)
cfprVnicIpV6HistoryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV6HistoryRn.setStatus("current")
_CfprVnicIpV6HistoryOldIpV6Addr_Type = InetAddressIPv6
_CfprVnicIpV6HistoryOldIpV6Addr_Object = MibTableColumn
cfprVnicIpV6HistoryOldIpV6Addr = _CfprVnicIpV6HistoryOldIpV6Addr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 40, 1, 4),
    _CfprVnicIpV6HistoryOldIpV6Addr_Type()
)
cfprVnicIpV6HistoryOldIpV6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV6HistoryOldIpV6Addr.setStatus("current")
_CfprVnicIpV6MgmtPooledAddrTable_Object = MibTable
cfprVnicIpV6MgmtPooledAddrTable = _CfprVnicIpV6MgmtPooledAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 41)
)
if mibBuilder.loadTexts:
    cfprVnicIpV6MgmtPooledAddrTable.setStatus("current")
_CfprVnicIpV6MgmtPooledAddrEntry_Object = MibTableRow
cfprVnicIpV6MgmtPooledAddrEntry = _CfprVnicIpV6MgmtPooledAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 41, 1)
)
cfprVnicIpV6MgmtPooledAddrEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicIpV6MgmtPooledAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicIpV6MgmtPooledAddrEntry.setStatus("current")
_CfprVnicIpV6MgmtPooledAddrInstanceId_Type = CfprManagedObjectId
_CfprVnicIpV6MgmtPooledAddrInstanceId_Object = MibTableColumn
cfprVnicIpV6MgmtPooledAddrInstanceId = _CfprVnicIpV6MgmtPooledAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 41, 1, 1),
    _CfprVnicIpV6MgmtPooledAddrInstanceId_Type()
)
cfprVnicIpV6MgmtPooledAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicIpV6MgmtPooledAddrInstanceId.setStatus("current")
_CfprVnicIpV6MgmtPooledAddrDn_Type = CfprManagedObjectDn
_CfprVnicIpV6MgmtPooledAddrDn_Object = MibTableColumn
cfprVnicIpV6MgmtPooledAddrDn = _CfprVnicIpV6MgmtPooledAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 41, 1, 2),
    _CfprVnicIpV6MgmtPooledAddrDn_Type()
)
cfprVnicIpV6MgmtPooledAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV6MgmtPooledAddrDn.setStatus("current")
_CfprVnicIpV6MgmtPooledAddrRn_Type = SnmpAdminString
_CfprVnicIpV6MgmtPooledAddrRn_Object = MibTableColumn
cfprVnicIpV6MgmtPooledAddrRn = _CfprVnicIpV6MgmtPooledAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 41, 1, 3),
    _CfprVnicIpV6MgmtPooledAddrRn_Type()
)
cfprVnicIpV6MgmtPooledAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV6MgmtPooledAddrRn.setStatus("current")
_CfprVnicIpV6MgmtPooledAddrAddr_Type = InetAddressIPv6
_CfprVnicIpV6MgmtPooledAddrAddr_Object = MibTableColumn
cfprVnicIpV6MgmtPooledAddrAddr = _CfprVnicIpV6MgmtPooledAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 41, 1, 4),
    _CfprVnicIpV6MgmtPooledAddrAddr_Type()
)
cfprVnicIpV6MgmtPooledAddrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV6MgmtPooledAddrAddr.setStatus("current")
_CfprVnicIpV6MgmtPooledAddrDefGw_Type = InetAddressIPv6
_CfprVnicIpV6MgmtPooledAddrDefGw_Object = MibTableColumn
cfprVnicIpV6MgmtPooledAddrDefGw = _CfprVnicIpV6MgmtPooledAddrDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 41, 1, 5),
    _CfprVnicIpV6MgmtPooledAddrDefGw_Type()
)
cfprVnicIpV6MgmtPooledAddrDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV6MgmtPooledAddrDefGw.setStatus("current")
_CfprVnicIpV6MgmtPooledAddrName_Type = SnmpAdminString
_CfprVnicIpV6MgmtPooledAddrName_Object = MibTableColumn
cfprVnicIpV6MgmtPooledAddrName = _CfprVnicIpV6MgmtPooledAddrName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 41, 1, 6),
    _CfprVnicIpV6MgmtPooledAddrName_Type()
)
cfprVnicIpV6MgmtPooledAddrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV6MgmtPooledAddrName.setStatus("current")
_CfprVnicIpV6MgmtPooledAddrOperName_Type = SnmpAdminString
_CfprVnicIpV6MgmtPooledAddrOperName_Object = MibTableColumn
cfprVnicIpV6MgmtPooledAddrOperName = _CfprVnicIpV6MgmtPooledAddrOperName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 41, 1, 7),
    _CfprVnicIpV6MgmtPooledAddrOperName_Type()
)
cfprVnicIpV6MgmtPooledAddrOperName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV6MgmtPooledAddrOperName.setStatus("current")
_CfprVnicIpV6MgmtPooledAddrPrefix_Type = Gauge32
_CfprVnicIpV6MgmtPooledAddrPrefix_Object = MibTableColumn
cfprVnicIpV6MgmtPooledAddrPrefix = _CfprVnicIpV6MgmtPooledAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 41, 1, 8),
    _CfprVnicIpV6MgmtPooledAddrPrefix_Type()
)
cfprVnicIpV6MgmtPooledAddrPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV6MgmtPooledAddrPrefix.setStatus("current")
_CfprVnicIpV6MgmtPooledAddrPrimDns_Type = InetAddressIPv6
_CfprVnicIpV6MgmtPooledAddrPrimDns_Object = MibTableColumn
cfprVnicIpV6MgmtPooledAddrPrimDns = _CfprVnicIpV6MgmtPooledAddrPrimDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 41, 1, 9),
    _CfprVnicIpV6MgmtPooledAddrPrimDns_Type()
)
cfprVnicIpV6MgmtPooledAddrPrimDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV6MgmtPooledAddrPrimDns.setStatus("current")
_CfprVnicIpV6MgmtPooledAddrSecDns_Type = InetAddressIPv6
_CfprVnicIpV6MgmtPooledAddrSecDns_Object = MibTableColumn
cfprVnicIpV6MgmtPooledAddrSecDns = _CfprVnicIpV6MgmtPooledAddrSecDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 41, 1, 10),
    _CfprVnicIpV6MgmtPooledAddrSecDns_Type()
)
cfprVnicIpV6MgmtPooledAddrSecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV6MgmtPooledAddrSecDns.setStatus("current")
_CfprVnicIpV6StaticAddrTable_Object = MibTable
cfprVnicIpV6StaticAddrTable = _CfprVnicIpV6StaticAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 42)
)
if mibBuilder.loadTexts:
    cfprVnicIpV6StaticAddrTable.setStatus("current")
_CfprVnicIpV6StaticAddrEntry_Object = MibTableRow
cfprVnicIpV6StaticAddrEntry = _CfprVnicIpV6StaticAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 42, 1)
)
cfprVnicIpV6StaticAddrEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicIpV6StaticAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicIpV6StaticAddrEntry.setStatus("current")
_CfprVnicIpV6StaticAddrInstanceId_Type = CfprManagedObjectId
_CfprVnicIpV6StaticAddrInstanceId_Object = MibTableColumn
cfprVnicIpV6StaticAddrInstanceId = _CfprVnicIpV6StaticAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 42, 1, 1),
    _CfprVnicIpV6StaticAddrInstanceId_Type()
)
cfprVnicIpV6StaticAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicIpV6StaticAddrInstanceId.setStatus("current")
_CfprVnicIpV6StaticAddrDn_Type = CfprManagedObjectDn
_CfprVnicIpV6StaticAddrDn_Object = MibTableColumn
cfprVnicIpV6StaticAddrDn = _CfprVnicIpV6StaticAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 42, 1, 2),
    _CfprVnicIpV6StaticAddrDn_Type()
)
cfprVnicIpV6StaticAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV6StaticAddrDn.setStatus("current")
_CfprVnicIpV6StaticAddrRn_Type = SnmpAdminString
_CfprVnicIpV6StaticAddrRn_Object = MibTableColumn
cfprVnicIpV6StaticAddrRn = _CfprVnicIpV6StaticAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 42, 1, 3),
    _CfprVnicIpV6StaticAddrRn_Type()
)
cfprVnicIpV6StaticAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV6StaticAddrRn.setStatus("current")
_CfprVnicIpV6StaticAddrAddr_Type = InetAddressIPv6
_CfprVnicIpV6StaticAddrAddr_Object = MibTableColumn
cfprVnicIpV6StaticAddrAddr = _CfprVnicIpV6StaticAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 42, 1, 4),
    _CfprVnicIpV6StaticAddrAddr_Type()
)
cfprVnicIpV6StaticAddrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV6StaticAddrAddr.setStatus("current")
_CfprVnicIpV6StaticAddrDefGw_Type = InetAddressIPv6
_CfprVnicIpV6StaticAddrDefGw_Object = MibTableColumn
cfprVnicIpV6StaticAddrDefGw = _CfprVnicIpV6StaticAddrDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 42, 1, 5),
    _CfprVnicIpV6StaticAddrDefGw_Type()
)
cfprVnicIpV6StaticAddrDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV6StaticAddrDefGw.setStatus("current")
_CfprVnicIpV6StaticAddrPrefix_Type = Gauge32
_CfprVnicIpV6StaticAddrPrefix_Object = MibTableColumn
cfprVnicIpV6StaticAddrPrefix = _CfprVnicIpV6StaticAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 42, 1, 6),
    _CfprVnicIpV6StaticAddrPrefix_Type()
)
cfprVnicIpV6StaticAddrPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV6StaticAddrPrefix.setStatus("current")
_CfprVnicIpV6StaticAddrPrimDns_Type = InetAddressIPv6
_CfprVnicIpV6StaticAddrPrimDns_Object = MibTableColumn
cfprVnicIpV6StaticAddrPrimDns = _CfprVnicIpV6StaticAddrPrimDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 42, 1, 7),
    _CfprVnicIpV6StaticAddrPrimDns_Type()
)
cfprVnicIpV6StaticAddrPrimDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV6StaticAddrPrimDns.setStatus("current")
_CfprVnicIpV6StaticAddrSecDns_Type = InetAddressIPv6
_CfprVnicIpV6StaticAddrSecDns_Object = MibTableColumn
cfprVnicIpV6StaticAddrSecDns = _CfprVnicIpV6StaticAddrSecDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 42, 1, 8),
    _CfprVnicIpV6StaticAddrSecDns_Type()
)
cfprVnicIpV6StaticAddrSecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpV6StaticAddrSecDns.setStatus("current")
_CfprVnicIpcTable_Object = MibTable
cfprVnicIpcTable = _CfprVnicIpcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43)
)
if mibBuilder.loadTexts:
    cfprVnicIpcTable.setStatus("current")
_CfprVnicIpcEntry_Object = MibTableRow
cfprVnicIpcEntry = _CfprVnicIpcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1)
)
cfprVnicIpcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicIpcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicIpcEntry.setStatus("current")
_CfprVnicIpcInstanceId_Type = CfprManagedObjectId
_CfprVnicIpcInstanceId_Object = MibTableColumn
cfprVnicIpcInstanceId = _CfprVnicIpcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1, 1),
    _CfprVnicIpcInstanceId_Type()
)
cfprVnicIpcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicIpcInstanceId.setStatus("current")
_CfprVnicIpcDn_Type = CfprManagedObjectDn
_CfprVnicIpcDn_Object = MibTableColumn
cfprVnicIpcDn = _CfprVnicIpcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1, 2),
    _CfprVnicIpcDn_Type()
)
cfprVnicIpcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcDn.setStatus("current")
_CfprVnicIpcRn_Type = SnmpAdminString
_CfprVnicIpcRn_Object = MibTableColumn
cfprVnicIpcRn = _CfprVnicIpcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1, 3),
    _CfprVnicIpcRn_Type()
)
cfprVnicIpcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcRn.setStatus("current")
_CfprVnicIpcAdaptorProfileName_Type = SnmpAdminString
_CfprVnicIpcAdaptorProfileName_Object = MibTableColumn
cfprVnicIpcAdaptorProfileName = _CfprVnicIpcAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1, 4),
    _CfprVnicIpcAdaptorProfileName_Type()
)
cfprVnicIpcAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcAdaptorProfileName.setStatus("current")
_CfprVnicIpcAddr_Type = MacAddress
_CfprVnicIpcAddr_Object = MibTableColumn
cfprVnicIpcAddr = _CfprVnicIpcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1, 5),
    _CfprVnicIpcAddr_Type()
)
cfprVnicIpcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcAddr.setStatus("current")
_CfprVnicIpcAdminHostPort_Type = CfprFabricHostPortId
_CfprVnicIpcAdminHostPort_Object = MibTableColumn
cfprVnicIpcAdminHostPort = _CfprVnicIpcAdminHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1, 6),
    _CfprVnicIpcAdminHostPort_Type()
)
cfprVnicIpcAdminHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcAdminHostPort.setStatus("current")
_CfprVnicIpcAdminVcon_Type = SnmpAdminString
_CfprVnicIpcAdminVcon_Object = MibTableColumn
cfprVnicIpcAdminVcon = _CfprVnicIpcAdminVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1, 7),
    _CfprVnicIpcAdminVcon_Type()
)
cfprVnicIpcAdminVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcAdminVcon.setStatus("current")
_CfprVnicIpcAppRole_Type = CfprVnicAppRole
_CfprVnicIpcAppRole_Object = MibTableColumn
cfprVnicIpcAppRole = _CfprVnicIpcAppRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1, 8),
    _CfprVnicIpcAppRole_Type()
)
cfprVnicIpcAppRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcAppRole.setStatus("current")
_CfprVnicIpcBootDev_Type = CfprVnicVnicBootDev
_CfprVnicIpcBootDev_Object = MibTableColumn
cfprVnicIpcBootDev = _CfprVnicIpcBootDev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1, 9),
    _CfprVnicIpcBootDev_Type()
)
cfprVnicIpcBootDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcBootDev.setStatus("current")
_CfprVnicIpcConfigQualifier_Type = CfprVnicConfigIssues
_CfprVnicIpcConfigQualifier_Object = MibTableColumn
cfprVnicIpcConfigQualifier = _CfprVnicIpcConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1, 10),
    _CfprVnicIpcConfigQualifier_Type()
)
cfprVnicIpcConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcConfigQualifier.setStatus("current")
_CfprVnicIpcConfigState_Type = CfprLsConfigState
_CfprVnicIpcConfigState_Object = MibTableColumn
cfprVnicIpcConfigState = _CfprVnicIpcConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1, 11),
    _CfprVnicIpcConfigState_Type()
)
cfprVnicIpcConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcConfigState.setStatus("current")
_CfprVnicIpcEquipmentDn_Type = SnmpAdminString
_CfprVnicIpcEquipmentDn_Object = MibTableColumn
cfprVnicIpcEquipmentDn = _CfprVnicIpcEquipmentDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1, 12),
    _CfprVnicIpcEquipmentDn_Type()
)
cfprVnicIpcEquipmentDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcEquipmentDn.setStatus("current")
_CfprVnicIpcIdentPoolName_Type = SnmpAdminString
_CfprVnicIpcIdentPoolName_Object = MibTableColumn
cfprVnicIpcIdentPoolName = _CfprVnicIpcIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1, 13),
    _CfprVnicIpcIdentPoolName_Type()
)
cfprVnicIpcIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcIdentPoolName.setStatus("current")
_CfprVnicIpcInstType_Type = CfprVnicInstantiation
_CfprVnicIpcInstType_Object = MibTableColumn
cfprVnicIpcInstType = _CfprVnicIpcInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1, 14),
    _CfprVnicIpcInstType_Type()
)
cfprVnicIpcInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcInstType.setStatus("current")
_CfprVnicIpcMtu_Type = Gauge32
_CfprVnicIpcMtu_Object = MibTableColumn
cfprVnicIpcMtu = _CfprVnicIpcMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1, 15),
    _CfprVnicIpcMtu_Type()
)
cfprVnicIpcMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcMtu.setStatus("current")
_CfprVnicIpcName_Type = SnmpAdminString
_CfprVnicIpcName_Object = MibTableColumn
cfprVnicIpcName = _CfprVnicIpcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1, 16),
    _CfprVnicIpcName_Type()
)
cfprVnicIpcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcName.setStatus("current")
_CfprVnicIpcNwCtrlPolicyName_Type = SnmpAdminString
_CfprVnicIpcNwCtrlPolicyName_Object = MibTableColumn
cfprVnicIpcNwCtrlPolicyName = _CfprVnicIpcNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1, 17),
    _CfprVnicIpcNwCtrlPolicyName_Type()
)
cfprVnicIpcNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcNwCtrlPolicyName.setStatus("current")
_CfprVnicIpcNwTemplName_Type = SnmpAdminString
_CfprVnicIpcNwTemplName_Object = MibTableColumn
cfprVnicIpcNwTemplName = _CfprVnicIpcNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1, 18),
    _CfprVnicIpcNwTemplName_Type()
)
cfprVnicIpcNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcNwTemplName.setStatus("current")
_CfprVnicIpcOperAdaptorProfileName_Type = SnmpAdminString
_CfprVnicIpcOperAdaptorProfileName_Object = MibTableColumn
cfprVnicIpcOperAdaptorProfileName = _CfprVnicIpcOperAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1, 19),
    _CfprVnicIpcOperAdaptorProfileName_Type()
)
cfprVnicIpcOperAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcOperAdaptorProfileName.setStatus("current")
_CfprVnicIpcOperHostPort_Type = CfprVnicVnicOperHostPort
_CfprVnicIpcOperHostPort_Object = MibTableColumn
cfprVnicIpcOperHostPort = _CfprVnicIpcOperHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1, 20),
    _CfprVnicIpcOperHostPort_Type()
)
cfprVnicIpcOperHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcOperHostPort.setStatus("current")
_CfprVnicIpcOperIdentPoolName_Type = SnmpAdminString
_CfprVnicIpcOperIdentPoolName_Object = MibTableColumn
cfprVnicIpcOperIdentPoolName = _CfprVnicIpcOperIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1, 21),
    _CfprVnicIpcOperIdentPoolName_Type()
)
cfprVnicIpcOperIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcOperIdentPoolName.setStatus("current")
_CfprVnicIpcOperNwCtrlPolicyName_Type = SnmpAdminString
_CfprVnicIpcOperNwCtrlPolicyName_Object = MibTableColumn
cfprVnicIpcOperNwCtrlPolicyName = _CfprVnicIpcOperNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1, 22),
    _CfprVnicIpcOperNwCtrlPolicyName_Type()
)
cfprVnicIpcOperNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcOperNwCtrlPolicyName.setStatus("current")
_CfprVnicIpcOperNwTemplName_Type = SnmpAdminString
_CfprVnicIpcOperNwTemplName_Object = MibTableColumn
cfprVnicIpcOperNwTemplName = _CfprVnicIpcOperNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1, 23),
    _CfprVnicIpcOperNwTemplName_Type()
)
cfprVnicIpcOperNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcOperNwTemplName.setStatus("current")
_CfprVnicIpcOperOrder_Type = Gauge32
_CfprVnicIpcOperOrder_Object = MibTableColumn
cfprVnicIpcOperOrder = _CfprVnicIpcOperOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1, 24),
    _CfprVnicIpcOperOrder_Type()
)
cfprVnicIpcOperOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcOperOrder.setStatus("current")
_CfprVnicIpcOperPinToGroupName_Type = SnmpAdminString
_CfprVnicIpcOperPinToGroupName_Object = MibTableColumn
cfprVnicIpcOperPinToGroupName = _CfprVnicIpcOperPinToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1, 25),
    _CfprVnicIpcOperPinToGroupName_Type()
)
cfprVnicIpcOperPinToGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcOperPinToGroupName.setStatus("current")
_CfprVnicIpcOperQosPolicyName_Type = SnmpAdminString
_CfprVnicIpcOperQosPolicyName_Object = MibTableColumn
cfprVnicIpcOperQosPolicyName = _CfprVnicIpcOperQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1, 26),
    _CfprVnicIpcOperQosPolicyName_Type()
)
cfprVnicIpcOperQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcOperQosPolicyName.setStatus("current")
_CfprVnicIpcOperSpeed_Type = Gauge32
_CfprVnicIpcOperSpeed_Object = MibTableColumn
cfprVnicIpcOperSpeed = _CfprVnicIpcOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1, 27),
    _CfprVnicIpcOperSpeed_Type()
)
cfprVnicIpcOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcOperSpeed.setStatus("current")
_CfprVnicIpcOperStatsPolicyName_Type = SnmpAdminString
_CfprVnicIpcOperStatsPolicyName_Object = MibTableColumn
cfprVnicIpcOperStatsPolicyName = _CfprVnicIpcOperStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1, 28),
    _CfprVnicIpcOperStatsPolicyName_Type()
)
cfprVnicIpcOperStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcOperStatsPolicyName.setStatus("current")
_CfprVnicIpcOperVcon_Type = SnmpAdminString
_CfprVnicIpcOperVcon_Object = MibTableColumn
cfprVnicIpcOperVcon = _CfprVnicIpcOperVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1, 29),
    _CfprVnicIpcOperVcon_Type()
)
cfprVnicIpcOperVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcOperVcon.setStatus("current")
_CfprVnicIpcOrder_Type = Gauge32
_CfprVnicIpcOrder_Object = MibTableColumn
cfprVnicIpcOrder = _CfprVnicIpcOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1, 30),
    _CfprVnicIpcOrder_Type()
)
cfprVnicIpcOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcOrder.setStatus("current")
_CfprVnicIpcOwner_Type = CfprVnicConnectionOwner
_CfprVnicIpcOwner_Object = MibTableColumn
cfprVnicIpcOwner = _CfprVnicIpcOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1, 31),
    _CfprVnicIpcOwner_Type()
)
cfprVnicIpcOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcOwner.setStatus("current")
_CfprVnicIpcPinToGroupName_Type = SnmpAdminString
_CfprVnicIpcPinToGroupName_Object = MibTableColumn
cfprVnicIpcPinToGroupName = _CfprVnicIpcPinToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1, 32),
    _CfprVnicIpcPinToGroupName_Type()
)
cfprVnicIpcPinToGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcPinToGroupName.setStatus("current")
_CfprVnicIpcQosPolicyName_Type = SnmpAdminString
_CfprVnicIpcQosPolicyName_Object = MibTableColumn
cfprVnicIpcQosPolicyName = _CfprVnicIpcQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1, 33),
    _CfprVnicIpcQosPolicyName_Type()
)
cfprVnicIpcQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcQosPolicyName.setStatus("current")
_CfprVnicIpcStatsPolicyName_Type = SnmpAdminString
_CfprVnicIpcStatsPolicyName_Object = MibTableColumn
cfprVnicIpcStatsPolicyName = _CfprVnicIpcStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1, 34),
    _CfprVnicIpcStatsPolicyName_Type()
)
cfprVnicIpcStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcStatsPolicyName.setStatus("current")
_CfprVnicIpcSwitchId_Type = CfprVnicEtherBaseSwitchId
_CfprVnicIpcSwitchId_Object = MibTableColumn
cfprVnicIpcSwitchId = _CfprVnicIpcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1, 35),
    _CfprVnicIpcSwitchId_Type()
)
cfprVnicIpcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcSwitchId.setStatus("current")
_CfprVnicIpcType_Type = CfprVnicIpcType
_CfprVnicIpcType_Object = MibTableColumn
cfprVnicIpcType = _CfprVnicIpcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 43, 1, 36),
    _CfprVnicIpcType_Type()
)
cfprVnicIpcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcType.setStatus("current")
_CfprVnicIpcIfTable_Object = MibTable
cfprVnicIpcIfTable = _CfprVnicIpcIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 44)
)
if mibBuilder.loadTexts:
    cfprVnicIpcIfTable.setStatus("current")
_CfprVnicIpcIfEntry_Object = MibTableRow
cfprVnicIpcIfEntry = _CfprVnicIpcIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 44, 1)
)
cfprVnicIpcIfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicIpcIfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicIpcIfEntry.setStatus("current")
_CfprVnicIpcIfInstanceId_Type = CfprManagedObjectId
_CfprVnicIpcIfInstanceId_Object = MibTableColumn
cfprVnicIpcIfInstanceId = _CfprVnicIpcIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 44, 1, 1),
    _CfprVnicIpcIfInstanceId_Type()
)
cfprVnicIpcIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicIpcIfInstanceId.setStatus("current")
_CfprVnicIpcIfDn_Type = CfprManagedObjectDn
_CfprVnicIpcIfDn_Object = MibTableColumn
cfprVnicIpcIfDn = _CfprVnicIpcIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 44, 1, 2),
    _CfprVnicIpcIfDn_Type()
)
cfprVnicIpcIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcIfDn.setStatus("current")
_CfprVnicIpcIfRn_Type = SnmpAdminString
_CfprVnicIpcIfRn_Object = MibTableColumn
cfprVnicIpcIfRn = _CfprVnicIpcIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 44, 1, 3),
    _CfprVnicIpcIfRn_Type()
)
cfprVnicIpcIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcIfRn.setStatus("current")
_CfprVnicIpcIfAddr_Type = MacAddress
_CfprVnicIpcIfAddr_Object = MibTableColumn
cfprVnicIpcIfAddr = _CfprVnicIpcIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 44, 1, 4),
    _CfprVnicIpcIfAddr_Type()
)
cfprVnicIpcIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcIfAddr.setStatus("current")
_CfprVnicIpcIfConfigQualifier_Type = CfprVnicConfigIssues
_CfprVnicIpcIfConfigQualifier_Object = MibTableColumn
cfprVnicIpcIfConfigQualifier = _CfprVnicIpcIfConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 44, 1, 5),
    _CfprVnicIpcIfConfigQualifier_Type()
)
cfprVnicIpcIfConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcIfConfigQualifier.setStatus("current")
_CfprVnicIpcIfDefaultNet_Type = TruthValue
_CfprVnicIpcIfDefaultNet_Object = MibTableColumn
cfprVnicIpcIfDefaultNet = _CfprVnicIpcIfDefaultNet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 44, 1, 6),
    _CfprVnicIpcIfDefaultNet_Type()
)
cfprVnicIpcIfDefaultNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcIfDefaultNet.setStatus("current")
_CfprVnicIpcIfName_Type = SnmpAdminString
_CfprVnicIpcIfName_Object = MibTableColumn
cfprVnicIpcIfName = _CfprVnicIpcIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 44, 1, 7),
    _CfprVnicIpcIfName_Type()
)
cfprVnicIpcIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcIfName.setStatus("current")
_CfprVnicIpcIfOperState_Type = CfprVnicIfOperState
_CfprVnicIpcIfOperState_Object = MibTableColumn
cfprVnicIpcIfOperState = _CfprVnicIpcIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 44, 1, 8),
    _CfprVnicIpcIfOperState_Type()
)
cfprVnicIpcIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcIfOperState.setStatus("current")
_CfprVnicIpcIfOperVnetDn_Type = SnmpAdminString
_CfprVnicIpcIfOperVnetDn_Object = MibTableColumn
cfprVnicIpcIfOperVnetDn = _CfprVnicIpcIfOperVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 44, 1, 9),
    _CfprVnicIpcIfOperVnetDn_Type()
)
cfprVnicIpcIfOperVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcIfOperVnetDn.setStatus("current")
_CfprVnicIpcIfOperVnetName_Type = SnmpAdminString
_CfprVnicIpcIfOperVnetName_Object = MibTableColumn
cfprVnicIpcIfOperVnetName = _CfprVnicIpcIfOperVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 44, 1, 10),
    _CfprVnicIpcIfOperVnetName_Type()
)
cfprVnicIpcIfOperVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcIfOperVnetName.setStatus("current")
_CfprVnicIpcIfOwner_Type = CfprVnicConnectionOwner
_CfprVnicIpcIfOwner_Object = MibTableColumn
cfprVnicIpcIfOwner = _CfprVnicIpcIfOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 44, 1, 11),
    _CfprVnicIpcIfOwner_Type()
)
cfprVnicIpcIfOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcIfOwner.setStatus("current")
_CfprVnicIpcIfPubNwId_Type = Gauge32
_CfprVnicIpcIfPubNwId_Object = MibTableColumn
cfprVnicIpcIfPubNwId = _CfprVnicIpcIfPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 44, 1, 12),
    _CfprVnicIpcIfPubNwId_Type()
)
cfprVnicIpcIfPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcIfPubNwId.setStatus("current")
_CfprVnicIpcIfSharing_Type = CfprFabricVlanSharingType
_CfprVnicIpcIfSharing_Object = MibTableColumn
cfprVnicIpcIfSharing = _CfprVnicIpcIfSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 44, 1, 13),
    _CfprVnicIpcIfSharing_Type()
)
cfprVnicIpcIfSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcIfSharing.setStatus("current")
_CfprVnicIpcIfSwitchId_Type = CfprVnicL2IfSwitchId
_CfprVnicIpcIfSwitchId_Object = MibTableColumn
cfprVnicIpcIfSwitchId = _CfprVnicIpcIfSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 44, 1, 14),
    _CfprVnicIpcIfSwitchId_Type()
)
cfprVnicIpcIfSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcIfSwitchId.setStatus("current")
_CfprVnicIpcIfType_Type = CfprVnicAIpcIfType
_CfprVnicIpcIfType_Object = MibTableColumn
cfprVnicIpcIfType = _CfprVnicIpcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 44, 1, 15),
    _CfprVnicIpcIfType_Type()
)
cfprVnicIpcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcIfType.setStatus("current")
_CfprVnicIpcIfVnet_Type = Gauge32
_CfprVnicIpcIfVnet_Object = MibTableColumn
cfprVnicIpcIfVnet = _CfprVnicIpcIfVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 44, 1, 16),
    _CfprVnicIpcIfVnet_Type()
)
cfprVnicIpcIfVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIpcIfVnet.setStatus("current")
_CfprVnicIqnHistoryTable_Object = MibTable
cfprVnicIqnHistoryTable = _CfprVnicIqnHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 45)
)
if mibBuilder.loadTexts:
    cfprVnicIqnHistoryTable.setStatus("current")
_CfprVnicIqnHistoryEntry_Object = MibTableRow
cfprVnicIqnHistoryEntry = _CfprVnicIqnHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 45, 1)
)
cfprVnicIqnHistoryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicIqnHistoryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicIqnHistoryEntry.setStatus("current")
_CfprVnicIqnHistoryInstanceId_Type = CfprManagedObjectId
_CfprVnicIqnHistoryInstanceId_Object = MibTableColumn
cfprVnicIqnHistoryInstanceId = _CfprVnicIqnHistoryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 45, 1, 1),
    _CfprVnicIqnHistoryInstanceId_Type()
)
cfprVnicIqnHistoryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicIqnHistoryInstanceId.setStatus("current")
_CfprVnicIqnHistoryDn_Type = CfprManagedObjectDn
_CfprVnicIqnHistoryDn_Object = MibTableColumn
cfprVnicIqnHistoryDn = _CfprVnicIqnHistoryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 45, 1, 2),
    _CfprVnicIqnHistoryDn_Type()
)
cfprVnicIqnHistoryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIqnHistoryDn.setStatus("current")
_CfprVnicIqnHistoryRn_Type = SnmpAdminString
_CfprVnicIqnHistoryRn_Object = MibTableColumn
cfprVnicIqnHistoryRn = _CfprVnicIqnHistoryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 45, 1, 3),
    _CfprVnicIqnHistoryRn_Type()
)
cfprVnicIqnHistoryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIqnHistoryRn.setStatus("current")
_CfprVnicIqnHistoryOldInitiatorName_Type = SnmpAdminString
_CfprVnicIqnHistoryOldInitiatorName_Object = MibTableColumn
cfprVnicIqnHistoryOldInitiatorName = _CfprVnicIqnHistoryOldInitiatorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 45, 1, 4),
    _CfprVnicIqnHistoryOldInitiatorName_Type()
)
cfprVnicIqnHistoryOldInitiatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicIqnHistoryOldInitiatorName.setStatus("current")
_CfprVnicLanConnPolicyTable_Object = MibTable
cfprVnicLanConnPolicyTable = _CfprVnicLanConnPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 46)
)
if mibBuilder.loadTexts:
    cfprVnicLanConnPolicyTable.setStatus("current")
_CfprVnicLanConnPolicyEntry_Object = MibTableRow
cfprVnicLanConnPolicyEntry = _CfprVnicLanConnPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 46, 1)
)
cfprVnicLanConnPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicLanConnPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicLanConnPolicyEntry.setStatus("current")
_CfprVnicLanConnPolicyInstanceId_Type = CfprManagedObjectId
_CfprVnicLanConnPolicyInstanceId_Object = MibTableColumn
cfprVnicLanConnPolicyInstanceId = _CfprVnicLanConnPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 46, 1, 1),
    _CfprVnicLanConnPolicyInstanceId_Type()
)
cfprVnicLanConnPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicLanConnPolicyInstanceId.setStatus("current")
_CfprVnicLanConnPolicyDn_Type = CfprManagedObjectDn
_CfprVnicLanConnPolicyDn_Object = MibTableColumn
cfprVnicLanConnPolicyDn = _CfprVnicLanConnPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 46, 1, 2),
    _CfprVnicLanConnPolicyDn_Type()
)
cfprVnicLanConnPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLanConnPolicyDn.setStatus("current")
_CfprVnicLanConnPolicyRn_Type = SnmpAdminString
_CfprVnicLanConnPolicyRn_Object = MibTableColumn
cfprVnicLanConnPolicyRn = _CfprVnicLanConnPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 46, 1, 3),
    _CfprVnicLanConnPolicyRn_Type()
)
cfprVnicLanConnPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLanConnPolicyRn.setStatus("current")
_CfprVnicLanConnPolicyDescr_Type = SnmpAdminString
_CfprVnicLanConnPolicyDescr_Object = MibTableColumn
cfprVnicLanConnPolicyDescr = _CfprVnicLanConnPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 46, 1, 4),
    _CfprVnicLanConnPolicyDescr_Type()
)
cfprVnicLanConnPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLanConnPolicyDescr.setStatus("current")
_CfprVnicLanConnPolicyFltAggr_Type = Unsigned64
_CfprVnicLanConnPolicyFltAggr_Object = MibTableColumn
cfprVnicLanConnPolicyFltAggr = _CfprVnicLanConnPolicyFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 46, 1, 5),
    _CfprVnicLanConnPolicyFltAggr_Type()
)
cfprVnicLanConnPolicyFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLanConnPolicyFltAggr.setStatus("current")
_CfprVnicLanConnPolicyIntId_Type = SnmpAdminString
_CfprVnicLanConnPolicyIntId_Object = MibTableColumn
cfprVnicLanConnPolicyIntId = _CfprVnicLanConnPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 46, 1, 6),
    _CfprVnicLanConnPolicyIntId_Type()
)
cfprVnicLanConnPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLanConnPolicyIntId.setStatus("current")
_CfprVnicLanConnPolicyName_Type = SnmpAdminString
_CfprVnicLanConnPolicyName_Object = MibTableColumn
cfprVnicLanConnPolicyName = _CfprVnicLanConnPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 46, 1, 7),
    _CfprVnicLanConnPolicyName_Type()
)
cfprVnicLanConnPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLanConnPolicyName.setStatus("current")
_CfprVnicLanConnPolicyPolicyLevel_Type = Gauge32
_CfprVnicLanConnPolicyPolicyLevel_Object = MibTableColumn
cfprVnicLanConnPolicyPolicyLevel = _CfprVnicLanConnPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 46, 1, 8),
    _CfprVnicLanConnPolicyPolicyLevel_Type()
)
cfprVnicLanConnPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLanConnPolicyPolicyLevel.setStatus("current")
_CfprVnicLanConnPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprVnicLanConnPolicyPolicyOwner_Object = MibTableColumn
cfprVnicLanConnPolicyPolicyOwner = _CfprVnicLanConnPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 46, 1, 9),
    _CfprVnicLanConnPolicyPolicyOwner_Type()
)
cfprVnicLanConnPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLanConnPolicyPolicyOwner.setStatus("current")
_CfprVnicLanConnTemplTable_Object = MibTable
cfprVnicLanConnTemplTable = _CfprVnicLanConnTemplTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 47)
)
if mibBuilder.loadTexts:
    cfprVnicLanConnTemplTable.setStatus("current")
_CfprVnicLanConnTemplEntry_Object = MibTableRow
cfprVnicLanConnTemplEntry = _CfprVnicLanConnTemplEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 47, 1)
)
cfprVnicLanConnTemplEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicLanConnTemplInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicLanConnTemplEntry.setStatus("current")
_CfprVnicLanConnTemplInstanceId_Type = CfprManagedObjectId
_CfprVnicLanConnTemplInstanceId_Object = MibTableColumn
cfprVnicLanConnTemplInstanceId = _CfprVnicLanConnTemplInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 47, 1, 1),
    _CfprVnicLanConnTemplInstanceId_Type()
)
cfprVnicLanConnTemplInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicLanConnTemplInstanceId.setStatus("current")
_CfprVnicLanConnTemplDn_Type = CfprManagedObjectDn
_CfprVnicLanConnTemplDn_Object = MibTableColumn
cfprVnicLanConnTemplDn = _CfprVnicLanConnTemplDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 47, 1, 2),
    _CfprVnicLanConnTemplDn_Type()
)
cfprVnicLanConnTemplDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLanConnTemplDn.setStatus("current")
_CfprVnicLanConnTemplRn_Type = SnmpAdminString
_CfprVnicLanConnTemplRn_Object = MibTableColumn
cfprVnicLanConnTemplRn = _CfprVnicLanConnTemplRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 47, 1, 3),
    _CfprVnicLanConnTemplRn_Type()
)
cfprVnicLanConnTemplRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLanConnTemplRn.setStatus("current")
_CfprVnicLanConnTemplDescr_Type = SnmpAdminString
_CfprVnicLanConnTemplDescr_Object = MibTableColumn
cfprVnicLanConnTemplDescr = _CfprVnicLanConnTemplDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 47, 1, 4),
    _CfprVnicLanConnTemplDescr_Type()
)
cfprVnicLanConnTemplDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLanConnTemplDescr.setStatus("current")
_CfprVnicLanConnTemplIdentPoolName_Type = SnmpAdminString
_CfprVnicLanConnTemplIdentPoolName_Object = MibTableColumn
cfprVnicLanConnTemplIdentPoolName = _CfprVnicLanConnTemplIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 47, 1, 5),
    _CfprVnicLanConnTemplIdentPoolName_Type()
)
cfprVnicLanConnTemplIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLanConnTemplIdentPoolName.setStatus("current")
_CfprVnicLanConnTemplIntId_Type = SnmpAdminString
_CfprVnicLanConnTemplIntId_Object = MibTableColumn
cfprVnicLanConnTemplIntId = _CfprVnicLanConnTemplIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 47, 1, 6),
    _CfprVnicLanConnTemplIntId_Type()
)
cfprVnicLanConnTemplIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLanConnTemplIntId.setStatus("current")
_CfprVnicLanConnTemplMtu_Type = Gauge32
_CfprVnicLanConnTemplMtu_Object = MibTableColumn
cfprVnicLanConnTemplMtu = _CfprVnicLanConnTemplMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 47, 1, 7),
    _CfprVnicLanConnTemplMtu_Type()
)
cfprVnicLanConnTemplMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLanConnTemplMtu.setStatus("current")
_CfprVnicLanConnTemplName_Type = SnmpAdminString
_CfprVnicLanConnTemplName_Object = MibTableColumn
cfprVnicLanConnTemplName = _CfprVnicLanConnTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 47, 1, 8),
    _CfprVnicLanConnTemplName_Type()
)
cfprVnicLanConnTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLanConnTemplName.setStatus("current")
_CfprVnicLanConnTemplNwCtrlPolicyName_Type = SnmpAdminString
_CfprVnicLanConnTemplNwCtrlPolicyName_Object = MibTableColumn
cfprVnicLanConnTemplNwCtrlPolicyName = _CfprVnicLanConnTemplNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 47, 1, 9),
    _CfprVnicLanConnTemplNwCtrlPolicyName_Type()
)
cfprVnicLanConnTemplNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLanConnTemplNwCtrlPolicyName.setStatus("current")
_CfprVnicLanConnTemplOperIdentPoolName_Type = SnmpAdminString
_CfprVnicLanConnTemplOperIdentPoolName_Object = MibTableColumn
cfprVnicLanConnTemplOperIdentPoolName = _CfprVnicLanConnTemplOperIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 47, 1, 10),
    _CfprVnicLanConnTemplOperIdentPoolName_Type()
)
cfprVnicLanConnTemplOperIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLanConnTemplOperIdentPoolName.setStatus("current")
_CfprVnicLanConnTemplOperNwCtrlPolicyName_Type = SnmpAdminString
_CfprVnicLanConnTemplOperNwCtrlPolicyName_Object = MibTableColumn
cfprVnicLanConnTemplOperNwCtrlPolicyName = _CfprVnicLanConnTemplOperNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 47, 1, 11),
    _CfprVnicLanConnTemplOperNwCtrlPolicyName_Type()
)
cfprVnicLanConnTemplOperNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLanConnTemplOperNwCtrlPolicyName.setStatus("current")
_CfprVnicLanConnTemplOperQosPolicyName_Type = SnmpAdminString
_CfprVnicLanConnTemplOperQosPolicyName_Object = MibTableColumn
cfprVnicLanConnTemplOperQosPolicyName = _CfprVnicLanConnTemplOperQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 47, 1, 12),
    _CfprVnicLanConnTemplOperQosPolicyName_Type()
)
cfprVnicLanConnTemplOperQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLanConnTemplOperQosPolicyName.setStatus("current")
_CfprVnicLanConnTemplOperStatsPolicyName_Type = SnmpAdminString
_CfprVnicLanConnTemplOperStatsPolicyName_Object = MibTableColumn
cfprVnicLanConnTemplOperStatsPolicyName = _CfprVnicLanConnTemplOperStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 47, 1, 13),
    _CfprVnicLanConnTemplOperStatsPolicyName_Type()
)
cfprVnicLanConnTemplOperStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLanConnTemplOperStatsPolicyName.setStatus("current")
_CfprVnicLanConnTemplPinToGroupName_Type = SnmpAdminString
_CfprVnicLanConnTemplPinToGroupName_Object = MibTableColumn
cfprVnicLanConnTemplPinToGroupName = _CfprVnicLanConnTemplPinToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 47, 1, 14),
    _CfprVnicLanConnTemplPinToGroupName_Type()
)
cfprVnicLanConnTemplPinToGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLanConnTemplPinToGroupName.setStatus("current")
_CfprVnicLanConnTemplPolicyLevel_Type = Gauge32
_CfprVnicLanConnTemplPolicyLevel_Object = MibTableColumn
cfprVnicLanConnTemplPolicyLevel = _CfprVnicLanConnTemplPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 47, 1, 15),
    _CfprVnicLanConnTemplPolicyLevel_Type()
)
cfprVnicLanConnTemplPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLanConnTemplPolicyLevel.setStatus("current")
_CfprVnicLanConnTemplPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprVnicLanConnTemplPolicyOwner_Object = MibTableColumn
cfprVnicLanConnTemplPolicyOwner = _CfprVnicLanConnTemplPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 47, 1, 16),
    _CfprVnicLanConnTemplPolicyOwner_Type()
)
cfprVnicLanConnTemplPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLanConnTemplPolicyOwner.setStatus("current")
_CfprVnicLanConnTemplQosPolicyName_Type = SnmpAdminString
_CfprVnicLanConnTemplQosPolicyName_Object = MibTableColumn
cfprVnicLanConnTemplQosPolicyName = _CfprVnicLanConnTemplQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 47, 1, 17),
    _CfprVnicLanConnTemplQosPolicyName_Type()
)
cfprVnicLanConnTemplQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLanConnTemplQosPolicyName.setStatus("current")
_CfprVnicLanConnTemplStatsPolicyName_Type = SnmpAdminString
_CfprVnicLanConnTemplStatsPolicyName_Object = MibTableColumn
cfprVnicLanConnTemplStatsPolicyName = _CfprVnicLanConnTemplStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 47, 1, 18),
    _CfprVnicLanConnTemplStatsPolicyName_Type()
)
cfprVnicLanConnTemplStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLanConnTemplStatsPolicyName.setStatus("current")
_CfprVnicLanConnTemplSwitchId_Type = CfprVnicLanConnTemplSwitchId
_CfprVnicLanConnTemplSwitchId_Object = MibTableColumn
cfprVnicLanConnTemplSwitchId = _CfprVnicLanConnTemplSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 47, 1, 19),
    _CfprVnicLanConnTemplSwitchId_Type()
)
cfprVnicLanConnTemplSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLanConnTemplSwitchId.setStatus("current")
_CfprVnicLanConnTemplTarget_Type = CfprVnicTemplateTarget
_CfprVnicLanConnTemplTarget_Object = MibTableColumn
cfprVnicLanConnTemplTarget = _CfprVnicLanConnTemplTarget_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 47, 1, 20),
    _CfprVnicLanConnTemplTarget_Type()
)
cfprVnicLanConnTemplTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLanConnTemplTarget.setStatus("current")
_CfprVnicLanConnTemplTemplType_Type = CfprVnicTemplateType
_CfprVnicLanConnTemplTemplType_Object = MibTableColumn
cfprVnicLanConnTemplTemplType = _CfprVnicLanConnTemplTemplType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 47, 1, 21),
    _CfprVnicLanConnTemplTemplType_Type()
)
cfprVnicLanConnTemplTemplType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLanConnTemplTemplType.setStatus("current")
_CfprVnicLifVlanTable_Object = MibTable
cfprVnicLifVlanTable = _CfprVnicLifVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 48)
)
if mibBuilder.loadTexts:
    cfprVnicLifVlanTable.setStatus("current")
_CfprVnicLifVlanEntry_Object = MibTableRow
cfprVnicLifVlanEntry = _CfprVnicLifVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 48, 1)
)
cfprVnicLifVlanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicLifVlanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicLifVlanEntry.setStatus("current")
_CfprVnicLifVlanInstanceId_Type = CfprManagedObjectId
_CfprVnicLifVlanInstanceId_Object = MibTableColumn
cfprVnicLifVlanInstanceId = _CfprVnicLifVlanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 48, 1, 1),
    _CfprVnicLifVlanInstanceId_Type()
)
cfprVnicLifVlanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicLifVlanInstanceId.setStatus("current")
_CfprVnicLifVlanDn_Type = CfprManagedObjectDn
_CfprVnicLifVlanDn_Object = MibTableColumn
cfprVnicLifVlanDn = _CfprVnicLifVlanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 48, 1, 2),
    _CfprVnicLifVlanDn_Type()
)
cfprVnicLifVlanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLifVlanDn.setStatus("current")
_CfprVnicLifVlanRn_Type = SnmpAdminString
_CfprVnicLifVlanRn_Object = MibTableColumn
cfprVnicLifVlanRn = _CfprVnicLifVlanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 48, 1, 3),
    _CfprVnicLifVlanRn_Type()
)
cfprVnicLifVlanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLifVlanRn.setStatus("current")
_CfprVnicLifVlanAddr_Type = MacAddress
_CfprVnicLifVlanAddr_Object = MibTableColumn
cfprVnicLifVlanAddr = _CfprVnicLifVlanAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 48, 1, 4),
    _CfprVnicLifVlanAddr_Type()
)
cfprVnicLifVlanAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLifVlanAddr.setStatus("current")
_CfprVnicLifVlanConfigQualifier_Type = CfprVnicConfigIssues
_CfprVnicLifVlanConfigQualifier_Object = MibTableColumn
cfprVnicLifVlanConfigQualifier = _CfprVnicLifVlanConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 48, 1, 5),
    _CfprVnicLifVlanConfigQualifier_Type()
)
cfprVnicLifVlanConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLifVlanConfigQualifier.setStatus("current")
_CfprVnicLifVlanDefaultNet_Type = TruthValue
_CfprVnicLifVlanDefaultNet_Object = MibTableColumn
cfprVnicLifVlanDefaultNet = _CfprVnicLifVlanDefaultNet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 48, 1, 6),
    _CfprVnicLifVlanDefaultNet_Type()
)
cfprVnicLifVlanDefaultNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLifVlanDefaultNet.setStatus("current")
_CfprVnicLifVlanName_Type = SnmpAdminString
_CfprVnicLifVlanName_Object = MibTableColumn
cfprVnicLifVlanName = _CfprVnicLifVlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 48, 1, 7),
    _CfprVnicLifVlanName_Type()
)
cfprVnicLifVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLifVlanName.setStatus("current")
_CfprVnicLifVlanOperState_Type = CfprVnicIfOperState
_CfprVnicLifVlanOperState_Object = MibTableColumn
cfprVnicLifVlanOperState = _CfprVnicLifVlanOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 48, 1, 8),
    _CfprVnicLifVlanOperState_Type()
)
cfprVnicLifVlanOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLifVlanOperState.setStatus("current")
_CfprVnicLifVlanOperVnetDn_Type = SnmpAdminString
_CfprVnicLifVlanOperVnetDn_Object = MibTableColumn
cfprVnicLifVlanOperVnetDn = _CfprVnicLifVlanOperVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 48, 1, 9),
    _CfprVnicLifVlanOperVnetDn_Type()
)
cfprVnicLifVlanOperVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLifVlanOperVnetDn.setStatus("current")
_CfprVnicLifVlanOperVnetName_Type = SnmpAdminString
_CfprVnicLifVlanOperVnetName_Object = MibTableColumn
cfprVnicLifVlanOperVnetName = _CfprVnicLifVlanOperVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 48, 1, 10),
    _CfprVnicLifVlanOperVnetName_Type()
)
cfprVnicLifVlanOperVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLifVlanOperVnetName.setStatus("current")
_CfprVnicLifVlanOwner_Type = CfprVnicConnectionOwner
_CfprVnicLifVlanOwner_Object = MibTableColumn
cfprVnicLifVlanOwner = _CfprVnicLifVlanOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 48, 1, 11),
    _CfprVnicLifVlanOwner_Type()
)
cfprVnicLifVlanOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLifVlanOwner.setStatus("current")
_CfprVnicLifVlanPubNwId_Type = Gauge32
_CfprVnicLifVlanPubNwId_Object = MibTableColumn
cfprVnicLifVlanPubNwId = _CfprVnicLifVlanPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 48, 1, 12),
    _CfprVnicLifVlanPubNwId_Type()
)
cfprVnicLifVlanPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLifVlanPubNwId.setStatus("current")
_CfprVnicLifVlanSharing_Type = CfprFabricVlanSharingType
_CfprVnicLifVlanSharing_Object = MibTableColumn
cfprVnicLifVlanSharing = _CfprVnicLifVlanSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 48, 1, 13),
    _CfprVnicLifVlanSharing_Type()
)
cfprVnicLifVlanSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLifVlanSharing.setStatus("current")
_CfprVnicLifVlanSwitchId_Type = CfprVnicL2IfSwitchId
_CfprVnicLifVlanSwitchId_Object = MibTableColumn
cfprVnicLifVlanSwitchId = _CfprVnicLifVlanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 48, 1, 14),
    _CfprVnicLifVlanSwitchId_Type()
)
cfprVnicLifVlanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLifVlanSwitchId.setStatus("current")
_CfprVnicLifVlanType_Type = CfprVnicAEtherIfType
_CfprVnicLifVlanType_Object = MibTableColumn
cfprVnicLifVlanType = _CfprVnicLifVlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 48, 1, 15),
    _CfprVnicLifVlanType_Type()
)
cfprVnicLifVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLifVlanType.setStatus("current")
_CfprVnicLifVlanVnet_Type = Gauge32
_CfprVnicLifVlanVnet_Object = MibTableColumn
cfprVnicLifVlanVnet = _CfprVnicLifVlanVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 48, 1, 16),
    _CfprVnicLifVlanVnet_Type()
)
cfprVnicLifVlanVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLifVlanVnet.setStatus("current")
_CfprVnicLifVsanTable_Object = MibTable
cfprVnicLifVsanTable = _CfprVnicLifVsanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 49)
)
if mibBuilder.loadTexts:
    cfprVnicLifVsanTable.setStatus("current")
_CfprVnicLifVsanEntry_Object = MibTableRow
cfprVnicLifVsanEntry = _CfprVnicLifVsanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 49, 1)
)
cfprVnicLifVsanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicLifVsanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicLifVsanEntry.setStatus("current")
_CfprVnicLifVsanInstanceId_Type = CfprManagedObjectId
_CfprVnicLifVsanInstanceId_Object = MibTableColumn
cfprVnicLifVsanInstanceId = _CfprVnicLifVsanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 49, 1, 1),
    _CfprVnicLifVsanInstanceId_Type()
)
cfprVnicLifVsanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicLifVsanInstanceId.setStatus("current")
_CfprVnicLifVsanDn_Type = CfprManagedObjectDn
_CfprVnicLifVsanDn_Object = MibTableColumn
cfprVnicLifVsanDn = _CfprVnicLifVsanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 49, 1, 2),
    _CfprVnicLifVsanDn_Type()
)
cfprVnicLifVsanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLifVsanDn.setStatus("current")
_CfprVnicLifVsanRn_Type = SnmpAdminString
_CfprVnicLifVsanRn_Object = MibTableColumn
cfprVnicLifVsanRn = _CfprVnicLifVsanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 49, 1, 3),
    _CfprVnicLifVsanRn_Type()
)
cfprVnicLifVsanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLifVsanRn.setStatus("current")
_CfprVnicLifVsanConfigQualifier_Type = CfprVnicConfigIssues
_CfprVnicLifVsanConfigQualifier_Object = MibTableColumn
cfprVnicLifVsanConfigQualifier = _CfprVnicLifVsanConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 49, 1, 4),
    _CfprVnicLifVsanConfigQualifier_Type()
)
cfprVnicLifVsanConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLifVsanConfigQualifier.setStatus("current")
_CfprVnicLifVsanInitiator_Type = Unsigned64
_CfprVnicLifVsanInitiator_Object = MibTableColumn
cfprVnicLifVsanInitiator = _CfprVnicLifVsanInitiator_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 49, 1, 5),
    _CfprVnicLifVsanInitiator_Type()
)
cfprVnicLifVsanInitiator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLifVsanInitiator.setStatus("current")
_CfprVnicLifVsanName_Type = SnmpAdminString
_CfprVnicLifVsanName_Object = MibTableColumn
cfprVnicLifVsanName = _CfprVnicLifVsanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 49, 1, 6),
    _CfprVnicLifVsanName_Type()
)
cfprVnicLifVsanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLifVsanName.setStatus("current")
_CfprVnicLifVsanOperState_Type = CfprVnicIfOperState
_CfprVnicLifVsanOperState_Object = MibTableColumn
cfprVnicLifVsanOperState = _CfprVnicLifVsanOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 49, 1, 7),
    _CfprVnicLifVsanOperState_Type()
)
cfprVnicLifVsanOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLifVsanOperState.setStatus("current")
_CfprVnicLifVsanOperVnetDn_Type = SnmpAdminString
_CfprVnicLifVsanOperVnetDn_Object = MibTableColumn
cfprVnicLifVsanOperVnetDn = _CfprVnicLifVsanOperVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 49, 1, 8),
    _CfprVnicLifVsanOperVnetDn_Type()
)
cfprVnicLifVsanOperVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLifVsanOperVnetDn.setStatus("current")
_CfprVnicLifVsanOperVnetName_Type = SnmpAdminString
_CfprVnicLifVsanOperVnetName_Object = MibTableColumn
cfprVnicLifVsanOperVnetName = _CfprVnicLifVsanOperVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 49, 1, 9),
    _CfprVnicLifVsanOperVnetName_Type()
)
cfprVnicLifVsanOperVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLifVsanOperVnetName.setStatus("current")
_CfprVnicLifVsanOwner_Type = CfprVnicConnectionOwner
_CfprVnicLifVsanOwner_Object = MibTableColumn
cfprVnicLifVsanOwner = _CfprVnicLifVsanOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 49, 1, 10),
    _CfprVnicLifVsanOwner_Type()
)
cfprVnicLifVsanOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLifVsanOwner.setStatus("current")
_CfprVnicLifVsanPubNwId_Type = Gauge32
_CfprVnicLifVsanPubNwId_Object = MibTableColumn
cfprVnicLifVsanPubNwId = _CfprVnicLifVsanPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 49, 1, 11),
    _CfprVnicLifVsanPubNwId_Type()
)
cfprVnicLifVsanPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLifVsanPubNwId.setStatus("current")
_CfprVnicLifVsanSharing_Type = CfprFabricVlanSharingType
_CfprVnicLifVsanSharing_Object = MibTableColumn
cfprVnicLifVsanSharing = _CfprVnicLifVsanSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 49, 1, 12),
    _CfprVnicLifVsanSharing_Type()
)
cfprVnicLifVsanSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLifVsanSharing.setStatus("current")
_CfprVnicLifVsanSwitchId_Type = CfprVnicL2IfSwitchId
_CfprVnicLifVsanSwitchId_Object = MibTableColumn
cfprVnicLifVsanSwitchId = _CfprVnicLifVsanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 49, 1, 13),
    _CfprVnicLifVsanSwitchId_Type()
)
cfprVnicLifVsanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLifVsanSwitchId.setStatus("current")
_CfprVnicLifVsanType_Type = CfprVnicAFcIfType
_CfprVnicLifVsanType_Object = MibTableColumn
cfprVnicLifVsanType = _CfprVnicLifVsanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 49, 1, 14),
    _CfprVnicLifVsanType_Type()
)
cfprVnicLifVsanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLifVsanType.setStatus("current")
_CfprVnicLifVsanVnet_Type = Gauge32
_CfprVnicLifVsanVnet_Object = MibTableColumn
cfprVnicLifVsanVnet = _CfprVnicLifVsanVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 49, 1, 15),
    _CfprVnicLifVsanVnet_Type()
)
cfprVnicLifVsanVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLifVsanVnet.setStatus("current")
_CfprVnicLunTable_Object = MibTable
cfprVnicLunTable = _CfprVnicLunTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 50)
)
if mibBuilder.loadTexts:
    cfprVnicLunTable.setStatus("current")
_CfprVnicLunEntry_Object = MibTableRow
cfprVnicLunEntry = _CfprVnicLunEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 50, 1)
)
cfprVnicLunEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicLunInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicLunEntry.setStatus("current")
_CfprVnicLunInstanceId_Type = CfprManagedObjectId
_CfprVnicLunInstanceId_Object = MibTableColumn
cfprVnicLunInstanceId = _CfprVnicLunInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 50, 1, 1),
    _CfprVnicLunInstanceId_Type()
)
cfprVnicLunInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicLunInstanceId.setStatus("current")
_CfprVnicLunDn_Type = CfprManagedObjectDn
_CfprVnicLunDn_Object = MibTableColumn
cfprVnicLunDn = _CfprVnicLunDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 50, 1, 2),
    _CfprVnicLunDn_Type()
)
cfprVnicLunDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLunDn.setStatus("current")
_CfprVnicLunRn_Type = SnmpAdminString
_CfprVnicLunRn_Object = MibTableColumn
cfprVnicLunRn = _CfprVnicLunRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 50, 1, 3),
    _CfprVnicLunRn_Type()
)
cfprVnicLunRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLunRn.setStatus("current")
_CfprVnicLunBootable_Type = TruthValue
_CfprVnicLunBootable_Object = MibTableColumn
cfprVnicLunBootable = _CfprVnicLunBootable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 50, 1, 4),
    _CfprVnicLunBootable_Type()
)
cfprVnicLunBootable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLunBootable.setStatus("current")
_CfprVnicLunId_Type = CfprVnicLunId
_CfprVnicLunId_Object = MibTableColumn
cfprVnicLunId = _CfprVnicLunId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 50, 1, 5),
    _CfprVnicLunId_Type()
)
cfprVnicLunId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicLunId.setStatus("current")
_CfprVnicMacHistoryTable_Object = MibTable
cfprVnicMacHistoryTable = _CfprVnicMacHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 51)
)
if mibBuilder.loadTexts:
    cfprVnicMacHistoryTable.setStatus("current")
_CfprVnicMacHistoryEntry_Object = MibTableRow
cfprVnicMacHistoryEntry = _CfprVnicMacHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 51, 1)
)
cfprVnicMacHistoryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicMacHistoryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicMacHistoryEntry.setStatus("current")
_CfprVnicMacHistoryInstanceId_Type = CfprManagedObjectId
_CfprVnicMacHistoryInstanceId_Object = MibTableColumn
cfprVnicMacHistoryInstanceId = _CfprVnicMacHistoryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 51, 1, 1),
    _CfprVnicMacHistoryInstanceId_Type()
)
cfprVnicMacHistoryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicMacHistoryInstanceId.setStatus("current")
_CfprVnicMacHistoryDn_Type = CfprManagedObjectDn
_CfprVnicMacHistoryDn_Object = MibTableColumn
cfprVnicMacHistoryDn = _CfprVnicMacHistoryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 51, 1, 2),
    _CfprVnicMacHistoryDn_Type()
)
cfprVnicMacHistoryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicMacHistoryDn.setStatus("current")
_CfprVnicMacHistoryRn_Type = SnmpAdminString
_CfprVnicMacHistoryRn_Object = MibTableColumn
cfprVnicMacHistoryRn = _CfprVnicMacHistoryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 51, 1, 3),
    _CfprVnicMacHistoryRn_Type()
)
cfprVnicMacHistoryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicMacHistoryRn.setStatus("current")
_CfprVnicMacHistoryOldaddr_Type = MacAddress
_CfprVnicMacHistoryOldaddr_Object = MibTableColumn
cfprVnicMacHistoryOldaddr = _CfprVnicMacHistoryOldaddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 51, 1, 4),
    _CfprVnicMacHistoryOldaddr_Type()
)
cfprVnicMacHistoryOldaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicMacHistoryOldaddr.setStatus("current")
_CfprVnicOProfileAliasTable_Object = MibTable
cfprVnicOProfileAliasTable = _CfprVnicOProfileAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 52)
)
if mibBuilder.loadTexts:
    cfprVnicOProfileAliasTable.setStatus("current")
_CfprVnicOProfileAliasEntry_Object = MibTableRow
cfprVnicOProfileAliasEntry = _CfprVnicOProfileAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 52, 1)
)
cfprVnicOProfileAliasEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicOProfileAliasInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicOProfileAliasEntry.setStatus("current")
_CfprVnicOProfileAliasInstanceId_Type = CfprManagedObjectId
_CfprVnicOProfileAliasInstanceId_Object = MibTableColumn
cfprVnicOProfileAliasInstanceId = _CfprVnicOProfileAliasInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 52, 1, 1),
    _CfprVnicOProfileAliasInstanceId_Type()
)
cfprVnicOProfileAliasInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicOProfileAliasInstanceId.setStatus("current")
_CfprVnicOProfileAliasDn_Type = CfprManagedObjectDn
_CfprVnicOProfileAliasDn_Object = MibTableColumn
cfprVnicOProfileAliasDn = _CfprVnicOProfileAliasDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 52, 1, 2),
    _CfprVnicOProfileAliasDn_Type()
)
cfprVnicOProfileAliasDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicOProfileAliasDn.setStatus("current")
_CfprVnicOProfileAliasRn_Type = SnmpAdminString
_CfprVnicOProfileAliasRn_Object = MibTableColumn
cfprVnicOProfileAliasRn = _CfprVnicOProfileAliasRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 52, 1, 3),
    _CfprVnicOProfileAliasRn_Type()
)
cfprVnicOProfileAliasRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicOProfileAliasRn.setStatus("current")
_CfprVnicOProfileAliasAlias_Type = SnmpAdminString
_CfprVnicOProfileAliasAlias_Object = MibTableColumn
cfprVnicOProfileAliasAlias = _CfprVnicOProfileAliasAlias_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 52, 1, 4),
    _CfprVnicOProfileAliasAlias_Type()
)
cfprVnicOProfileAliasAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicOProfileAliasAlias.setStatus("current")
_CfprVnicOProfileAliasMgmtPlane_Type = CfprVmMgmtPlane
_CfprVnicOProfileAliasMgmtPlane_Object = MibTableColumn
cfprVnicOProfileAliasMgmtPlane = _CfprVnicOProfileAliasMgmtPlane_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 52, 1, 5),
    _CfprVnicOProfileAliasMgmtPlane_Type()
)
cfprVnicOProfileAliasMgmtPlane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicOProfileAliasMgmtPlane.setStatus("current")
_CfprVnicOProfileAliasVSwitchId_Type = SnmpAdminString
_CfprVnicOProfileAliasVSwitchId_Object = MibTableColumn
cfprVnicOProfileAliasVSwitchId = _CfprVnicOProfileAliasVSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 52, 1, 6),
    _CfprVnicOProfileAliasVSwitchId_Type()
)
cfprVnicOProfileAliasVSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicOProfileAliasVSwitchId.setStatus("current")
_CfprVnicOProfileAliasVSwitchName_Type = SnmpAdminString
_CfprVnicOProfileAliasVSwitchName_Object = MibTableColumn
cfprVnicOProfileAliasVSwitchName = _CfprVnicOProfileAliasVSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 52, 1, 7),
    _CfprVnicOProfileAliasVSwitchName_Type()
)
cfprVnicOProfileAliasVSwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicOProfileAliasVSwitchName.setStatus("current")
_CfprVnicProfileTable_Object = MibTable
cfprVnicProfileTable = _CfprVnicProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 53)
)
if mibBuilder.loadTexts:
    cfprVnicProfileTable.setStatus("current")
_CfprVnicProfileEntry_Object = MibTableRow
cfprVnicProfileEntry = _CfprVnicProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 53, 1)
)
cfprVnicProfileEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicProfileInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicProfileEntry.setStatus("current")
_CfprVnicProfileInstanceId_Type = CfprManagedObjectId
_CfprVnicProfileInstanceId_Object = MibTableColumn
cfprVnicProfileInstanceId = _CfprVnicProfileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 53, 1, 1),
    _CfprVnicProfileInstanceId_Type()
)
cfprVnicProfileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicProfileInstanceId.setStatus("current")
_CfprVnicProfileDn_Type = CfprManagedObjectDn
_CfprVnicProfileDn_Object = MibTableColumn
cfprVnicProfileDn = _CfprVnicProfileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 53, 1, 2),
    _CfprVnicProfileDn_Type()
)
cfprVnicProfileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileDn.setStatus("current")
_CfprVnicProfileRn_Type = SnmpAdminString
_CfprVnicProfileRn_Object = MibTableColumn
cfprVnicProfileRn = _CfprVnicProfileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 53, 1, 3),
    _CfprVnicProfileRn_Type()
)
cfprVnicProfileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileRn.setStatus("current")
_CfprVnicProfileCdp_Type = CfprNwctrlAdminState
_CfprVnicProfileCdp_Object = MibTableColumn
cfprVnicProfileCdp = _CfprVnicProfileCdp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 53, 1, 4),
    _CfprVnicProfileCdp_Type()
)
cfprVnicProfileCdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileCdp.setStatus("current")
_CfprVnicProfileConfigQualifier_Type = CfprVnicProfileConfigQualifier
_CfprVnicProfileConfigQualifier_Object = MibTableColumn
cfprVnicProfileConfigQualifier = _CfprVnicProfileConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 53, 1, 5),
    _CfprVnicProfileConfigQualifier_Type()
)
cfprVnicProfileConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileConfigQualifier.setStatus("current")
_CfprVnicProfileCos_Type = Gauge32
_CfprVnicProfileCos_Object = MibTableColumn
cfprVnicProfileCos = _CfprVnicProfileCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 53, 1, 6),
    _CfprVnicProfileCos_Type()
)
cfprVnicProfileCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileCos.setStatus("current")
_CfprVnicProfileDescr_Type = SnmpAdminString
_CfprVnicProfileDescr_Object = MibTableColumn
cfprVnicProfileDescr = _CfprVnicProfileDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 53, 1, 7),
    _CfprVnicProfileDescr_Type()
)
cfprVnicProfileDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileDescr.setStatus("current")
_CfprVnicProfileForgeMac_Type = CfprDpsecForgedTransmit
_CfprVnicProfileForgeMac_Object = MibTableColumn
cfprVnicProfileForgeMac = _CfprVnicProfileForgeMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 53, 1, 8),
    _CfprVnicProfileForgeMac_Type()
)
cfprVnicProfileForgeMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileForgeMac.setStatus("current")
_CfprVnicProfileHostNwIOPerf_Type = CfprVnicHostNwIOPerfPref
_CfprVnicProfileHostNwIOPerf_Object = MibTableColumn
cfprVnicProfileHostNwIOPerf = _CfprVnicProfileHostNwIOPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 53, 1, 9),
    _CfprVnicProfileHostNwIOPerf_Type()
)
cfprVnicProfileHostNwIOPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileHostNwIOPerf.setStatus("current")
_CfprVnicProfileIntId_Type = SnmpAdminString
_CfprVnicProfileIntId_Object = MibTableColumn
cfprVnicProfileIntId = _CfprVnicProfileIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 53, 1, 10),
    _CfprVnicProfileIntId_Type()
)
cfprVnicProfileIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileIntId.setStatus("current")
_CfprVnicProfileMacRegisterMode_Type = CfprNwctrlRegistrationMode
_CfprVnicProfileMacRegisterMode_Object = MibTableColumn
cfprVnicProfileMacRegisterMode = _CfprVnicProfileMacRegisterMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 53, 1, 11),
    _CfprVnicProfileMacRegisterMode_Type()
)
cfprVnicProfileMacRegisterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileMacRegisterMode.setStatus("current")
_CfprVnicProfileMaxPorts_Type = Gauge32
_CfprVnicProfileMaxPorts_Object = MibTableColumn
cfprVnicProfileMaxPorts = _CfprVnicProfileMaxPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 53, 1, 12),
    _CfprVnicProfileMaxPorts_Type()
)
cfprVnicProfileMaxPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileMaxPorts.setStatus("current")
_CfprVnicProfileName_Type = SnmpAdminString
_CfprVnicProfileName_Object = MibTableColumn
cfprVnicProfileName = _CfprVnicProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 53, 1, 13),
    _CfprVnicProfileName_Type()
)
cfprVnicProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileName.setStatus("current")
_CfprVnicProfileNwCtrlPolicyName_Type = SnmpAdminString
_CfprVnicProfileNwCtrlPolicyName_Object = MibTableColumn
cfprVnicProfileNwCtrlPolicyName = _CfprVnicProfileNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 53, 1, 14),
    _CfprVnicProfileNwCtrlPolicyName_Type()
)
cfprVnicProfileNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileNwCtrlPolicyName.setStatus("current")
_CfprVnicProfileOperNwCtrlPolicyName_Type = SnmpAdminString
_CfprVnicProfileOperNwCtrlPolicyName_Object = MibTableColumn
cfprVnicProfileOperNwCtrlPolicyName = _CfprVnicProfileOperNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 53, 1, 15),
    _CfprVnicProfileOperNwCtrlPolicyName_Type()
)
cfprVnicProfileOperNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileOperNwCtrlPolicyName.setStatus("current")
_CfprVnicProfileOperQosPolicyName_Type = SnmpAdminString
_CfprVnicProfileOperQosPolicyName_Object = MibTableColumn
cfprVnicProfileOperQosPolicyName = _CfprVnicProfileOperQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 53, 1, 16),
    _CfprVnicProfileOperQosPolicyName_Type()
)
cfprVnicProfileOperQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileOperQosPolicyName.setStatus("current")
_CfprVnicProfilePinToGroupName_Type = SnmpAdminString
_CfprVnicProfilePinToGroupName_Object = MibTableColumn
cfprVnicProfilePinToGroupName = _CfprVnicProfilePinToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 53, 1, 17),
    _CfprVnicProfilePinToGroupName_Type()
)
cfprVnicProfilePinToGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfilePinToGroupName.setStatus("current")
_CfprVnicProfilePolicyLevel_Type = Gauge32
_CfprVnicProfilePolicyLevel_Object = MibTableColumn
cfprVnicProfilePolicyLevel = _CfprVnicProfilePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 53, 1, 18),
    _CfprVnicProfilePolicyLevel_Type()
)
cfprVnicProfilePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfilePolicyLevel.setStatus("current")
_CfprVnicProfilePolicyOwner_Type = CfprPolicyPolicyOwner
_CfprVnicProfilePolicyOwner_Object = MibTableColumn
cfprVnicProfilePolicyOwner = _CfprVnicProfilePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 53, 1, 19),
    _CfprVnicProfilePolicyOwner_Type()
)
cfprVnicProfilePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfilePolicyOwner.setStatus("current")
_CfprVnicProfilePortProfileUuid_Type = SnmpAdminString
_CfprVnicProfilePortProfileUuid_Object = MibTableColumn
cfprVnicProfilePortProfileUuid = _CfprVnicProfilePortProfileUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 53, 1, 20),
    _CfprVnicProfilePortProfileUuid_Type()
)
cfprVnicProfilePortProfileUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfilePortProfileUuid.setStatus("current")
_CfprVnicProfilePrimaryVlanId_Type = Gauge32
_CfprVnicProfilePrimaryVlanId_Object = MibTableColumn
cfprVnicProfilePrimaryVlanId = _CfprVnicProfilePrimaryVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 53, 1, 21),
    _CfprVnicProfilePrimaryVlanId_Type()
)
cfprVnicProfilePrimaryVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfilePrimaryVlanId.setStatus("current")
_CfprVnicProfileQosPolicyDn_Type = SnmpAdminString
_CfprVnicProfileQosPolicyDn_Object = MibTableColumn
cfprVnicProfileQosPolicyDn = _CfprVnicProfileQosPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 53, 1, 22),
    _CfprVnicProfileQosPolicyDn_Type()
)
cfprVnicProfileQosPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileQosPolicyDn.setStatus("current")
_CfprVnicProfileQosPolicyId_Type = SnmpAdminString
_CfprVnicProfileQosPolicyId_Object = MibTableColumn
cfprVnicProfileQosPolicyId = _CfprVnicProfileQosPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 53, 1, 23),
    _CfprVnicProfileQosPolicyId_Type()
)
cfprVnicProfileQosPolicyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileQosPolicyId.setStatus("current")
_CfprVnicProfileQosPolicyName_Type = SnmpAdminString
_CfprVnicProfileQosPolicyName_Object = MibTableColumn
cfprVnicProfileQosPolicyName = _CfprVnicProfileQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 53, 1, 24),
    _CfprVnicProfileQosPolicyName_Type()
)
cfprVnicProfileQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileQosPolicyName.setStatus("current")
_CfprVnicProfileSwABorderAggrPort_Type = Gauge32
_CfprVnicProfileSwABorderAggrPort_Object = MibTableColumn
cfprVnicProfileSwABorderAggrPort = _CfprVnicProfileSwABorderAggrPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 53, 1, 25),
    _CfprVnicProfileSwABorderAggrPort_Type()
)
cfprVnicProfileSwABorderAggrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSwABorderAggrPort.setStatus("current")
_CfprVnicProfileSwABorderPort_Type = Gauge32
_CfprVnicProfileSwABorderPort_Object = MibTableColumn
cfprVnicProfileSwABorderPort = _CfprVnicProfileSwABorderPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 53, 1, 26),
    _CfprVnicProfileSwABorderPort_Type()
)
cfprVnicProfileSwABorderPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSwABorderPort.setStatus("current")
_CfprVnicProfileSwABorderSlot_Type = Gauge32
_CfprVnicProfileSwABorderSlot_Object = MibTableColumn
cfprVnicProfileSwABorderSlot = _CfprVnicProfileSwABorderSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 53, 1, 27),
    _CfprVnicProfileSwABorderSlot_Type()
)
cfprVnicProfileSwABorderSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSwABorderSlot.setStatus("current")
_CfprVnicProfileSwBBorderAggrPort_Type = Gauge32
_CfprVnicProfileSwBBorderAggrPort_Object = MibTableColumn
cfprVnicProfileSwBBorderAggrPort = _CfprVnicProfileSwBBorderAggrPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 53, 1, 28),
    _CfprVnicProfileSwBBorderAggrPort_Type()
)
cfprVnicProfileSwBBorderAggrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSwBBorderAggrPort.setStatus("current")
_CfprVnicProfileSwBBorderPort_Type = Gauge32
_CfprVnicProfileSwBBorderPort_Object = MibTableColumn
cfprVnicProfileSwBBorderPort = _CfprVnicProfileSwBBorderPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 53, 1, 29),
    _CfprVnicProfileSwBBorderPort_Type()
)
cfprVnicProfileSwBBorderPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSwBBorderPort.setStatus("current")
_CfprVnicProfileSwBBorderSlot_Type = Gauge32
_CfprVnicProfileSwBBorderSlot_Object = MibTableColumn
cfprVnicProfileSwBBorderSlot = _CfprVnicProfileSwBBorderSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 53, 1, 30),
    _CfprVnicProfileSwBBorderSlot_Type()
)
cfprVnicProfileSwBBorderSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSwBBorderSlot.setStatus("current")
_CfprVnicProfileType_Type = CfprVnicPortProfileType
_CfprVnicProfileType_Object = MibTableColumn
cfprVnicProfileType = _CfprVnicProfileType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 53, 1, 31),
    _CfprVnicProfileType_Type()
)
cfprVnicProfileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileType.setStatus("current")
_CfprVnicProfileUplinkFailAction_Type = CfprNwctrlLinkFailAction
_CfprVnicProfileUplinkFailAction_Object = MibTableColumn
cfprVnicProfileUplinkFailAction = _CfprVnicProfileUplinkFailAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 53, 1, 32),
    _CfprVnicProfileUplinkFailAction_Type()
)
cfprVnicProfileUplinkFailAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileUplinkFailAction.setStatus("current")
_CfprVnicProfileAliasTable_Object = MibTable
cfprVnicProfileAliasTable = _CfprVnicProfileAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 54)
)
if mibBuilder.loadTexts:
    cfprVnicProfileAliasTable.setStatus("current")
_CfprVnicProfileAliasEntry_Object = MibTableRow
cfprVnicProfileAliasEntry = _CfprVnicProfileAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 54, 1)
)
cfprVnicProfileAliasEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicProfileAliasInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicProfileAliasEntry.setStatus("current")
_CfprVnicProfileAliasInstanceId_Type = CfprManagedObjectId
_CfprVnicProfileAliasInstanceId_Object = MibTableColumn
cfprVnicProfileAliasInstanceId = _CfprVnicProfileAliasInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 54, 1, 1),
    _CfprVnicProfileAliasInstanceId_Type()
)
cfprVnicProfileAliasInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicProfileAliasInstanceId.setStatus("current")
_CfprVnicProfileAliasDn_Type = CfprManagedObjectDn
_CfprVnicProfileAliasDn_Object = MibTableColumn
cfprVnicProfileAliasDn = _CfprVnicProfileAliasDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 54, 1, 2),
    _CfprVnicProfileAliasDn_Type()
)
cfprVnicProfileAliasDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileAliasDn.setStatus("current")
_CfprVnicProfileAliasRn_Type = SnmpAdminString
_CfprVnicProfileAliasRn_Object = MibTableColumn
cfprVnicProfileAliasRn = _CfprVnicProfileAliasRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 54, 1, 3),
    _CfprVnicProfileAliasRn_Type()
)
cfprVnicProfileAliasRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileAliasRn.setStatus("current")
_CfprVnicProfileAliasAlias_Type = SnmpAdminString
_CfprVnicProfileAliasAlias_Object = MibTableColumn
cfprVnicProfileAliasAlias = _CfprVnicProfileAliasAlias_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 54, 1, 4),
    _CfprVnicProfileAliasAlias_Type()
)
cfprVnicProfileAliasAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileAliasAlias.setStatus("current")
_CfprVnicProfileAliasSwUuid_Type = SnmpAdminString
_CfprVnicProfileAliasSwUuid_Object = MibTableColumn
cfprVnicProfileAliasSwUuid = _CfprVnicProfileAliasSwUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 54, 1, 5),
    _CfprVnicProfileAliasSwUuid_Type()
)
cfprVnicProfileAliasSwUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileAliasSwUuid.setStatus("current")
_CfprVnicProfileRefTable_Object = MibTable
cfprVnicProfileRefTable = _CfprVnicProfileRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 55)
)
if mibBuilder.loadTexts:
    cfprVnicProfileRefTable.setStatus("current")
_CfprVnicProfileRefEntry_Object = MibTableRow
cfprVnicProfileRefEntry = _CfprVnicProfileRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 55, 1)
)
cfprVnicProfileRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicProfileRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicProfileRefEntry.setStatus("current")
_CfprVnicProfileRefInstanceId_Type = CfprManagedObjectId
_CfprVnicProfileRefInstanceId_Object = MibTableColumn
cfprVnicProfileRefInstanceId = _CfprVnicProfileRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 55, 1, 1),
    _CfprVnicProfileRefInstanceId_Type()
)
cfprVnicProfileRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicProfileRefInstanceId.setStatus("current")
_CfprVnicProfileRefDn_Type = CfprManagedObjectDn
_CfprVnicProfileRefDn_Object = MibTableColumn
cfprVnicProfileRefDn = _CfprVnicProfileRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 55, 1, 2),
    _CfprVnicProfileRefDn_Type()
)
cfprVnicProfileRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileRefDn.setStatus("current")
_CfprVnicProfileRefRn_Type = SnmpAdminString
_CfprVnicProfileRefRn_Object = MibTableColumn
cfprVnicProfileRefRn = _CfprVnicProfileRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 55, 1, 3),
    _CfprVnicProfileRefRn_Type()
)
cfprVnicProfileRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileRefRn.setStatus("current")
_CfprVnicProfileRefName_Type = SnmpAdminString
_CfprVnicProfileRefName_Object = MibTableColumn
cfprVnicProfileRefName = _CfprVnicProfileRefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 55, 1, 4),
    _CfprVnicProfileRefName_Type()
)
cfprVnicProfileRefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileRefName.setStatus("current")
_CfprVnicProfileRefSourceDn_Type = SnmpAdminString
_CfprVnicProfileRefSourceDn_Object = MibTableColumn
cfprVnicProfileRefSourceDn = _CfprVnicProfileRefSourceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 55, 1, 5),
    _CfprVnicProfileRefSourceDn_Type()
)
cfprVnicProfileRefSourceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileRefSourceDn.setStatus("current")
_CfprVnicProfileSetTable_Object = MibTable
cfprVnicProfileSetTable = _CfprVnicProfileSetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 56)
)
if mibBuilder.loadTexts:
    cfprVnicProfileSetTable.setStatus("current")
_CfprVnicProfileSetEntry_Object = MibTableRow
cfprVnicProfileSetEntry = _CfprVnicProfileSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 56, 1)
)
cfprVnicProfileSetEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicProfileSetInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicProfileSetEntry.setStatus("current")
_CfprVnicProfileSetInstanceId_Type = CfprManagedObjectId
_CfprVnicProfileSetInstanceId_Object = MibTableColumn
cfprVnicProfileSetInstanceId = _CfprVnicProfileSetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 56, 1, 1),
    _CfprVnicProfileSetInstanceId_Type()
)
cfprVnicProfileSetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicProfileSetInstanceId.setStatus("current")
_CfprVnicProfileSetDn_Type = CfprManagedObjectDn
_CfprVnicProfileSetDn_Object = MibTableColumn
cfprVnicProfileSetDn = _CfprVnicProfileSetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 56, 1, 2),
    _CfprVnicProfileSetDn_Type()
)
cfprVnicProfileSetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetDn.setStatus("current")
_CfprVnicProfileSetRn_Type = SnmpAdminString
_CfprVnicProfileSetRn_Object = MibTableColumn
cfprVnicProfileSetRn = _CfprVnicProfileSetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 56, 1, 3),
    _CfprVnicProfileSetRn_Type()
)
cfprVnicProfileSetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetRn.setStatus("current")
_CfprVnicProfileSetFltAggr_Type = Unsigned64
_CfprVnicProfileSetFltAggr_Object = MibTableColumn
cfprVnicProfileSetFltAggr = _CfprVnicProfileSetFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 56, 1, 4),
    _CfprVnicProfileSetFltAggr_Type()
)
cfprVnicProfileSetFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFltAggr.setStatus("current")
_CfprVnicProfileSetFsmDescr_Type = SnmpAdminString
_CfprVnicProfileSetFsmDescr_Object = MibTableColumn
cfprVnicProfileSetFsmDescr = _CfprVnicProfileSetFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 56, 1, 5),
    _CfprVnicProfileSetFsmDescr_Type()
)
cfprVnicProfileSetFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmDescr.setStatus("current")
_CfprVnicProfileSetFsmPrev_Type = SnmpAdminString
_CfprVnicProfileSetFsmPrev_Object = MibTableColumn
cfprVnicProfileSetFsmPrev = _CfprVnicProfileSetFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 56, 1, 6),
    _CfprVnicProfileSetFsmPrev_Type()
)
cfprVnicProfileSetFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmPrev.setStatus("current")
_CfprVnicProfileSetFsmProgr_Type = Gauge32
_CfprVnicProfileSetFsmProgr_Object = MibTableColumn
cfprVnicProfileSetFsmProgr = _CfprVnicProfileSetFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 56, 1, 7),
    _CfprVnicProfileSetFsmProgr_Type()
)
cfprVnicProfileSetFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmProgr.setStatus("current")
_CfprVnicProfileSetFsmRmtInvErrCode_Type = Gauge32
_CfprVnicProfileSetFsmRmtInvErrCode_Object = MibTableColumn
cfprVnicProfileSetFsmRmtInvErrCode = _CfprVnicProfileSetFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 56, 1, 8),
    _CfprVnicProfileSetFsmRmtInvErrCode_Type()
)
cfprVnicProfileSetFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmRmtInvErrCode.setStatus("current")
_CfprVnicProfileSetFsmRmtInvErrDescr_Type = SnmpAdminString
_CfprVnicProfileSetFsmRmtInvErrDescr_Object = MibTableColumn
cfprVnicProfileSetFsmRmtInvErrDescr = _CfprVnicProfileSetFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 56, 1, 9),
    _CfprVnicProfileSetFsmRmtInvErrDescr_Type()
)
cfprVnicProfileSetFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmRmtInvErrDescr.setStatus("current")
_CfprVnicProfileSetFsmRmtInvRslt_Type = CfprConditionRemoteInvRslt
_CfprVnicProfileSetFsmRmtInvRslt_Object = MibTableColumn
cfprVnicProfileSetFsmRmtInvRslt = _CfprVnicProfileSetFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 56, 1, 10),
    _CfprVnicProfileSetFsmRmtInvRslt_Type()
)
cfprVnicProfileSetFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmRmtInvRslt.setStatus("current")
_CfprVnicProfileSetFsmStageDescr_Type = SnmpAdminString
_CfprVnicProfileSetFsmStageDescr_Object = MibTableColumn
cfprVnicProfileSetFsmStageDescr = _CfprVnicProfileSetFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 56, 1, 11),
    _CfprVnicProfileSetFsmStageDescr_Type()
)
cfprVnicProfileSetFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmStageDescr.setStatus("current")
_CfprVnicProfileSetFsmStamp_Type = DateAndTime
_CfprVnicProfileSetFsmStamp_Object = MibTableColumn
cfprVnicProfileSetFsmStamp = _CfprVnicProfileSetFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 56, 1, 12),
    _CfprVnicProfileSetFsmStamp_Type()
)
cfprVnicProfileSetFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmStamp.setStatus("current")
_CfprVnicProfileSetFsmStatus_Type = SnmpAdminString
_CfprVnicProfileSetFsmStatus_Object = MibTableColumn
cfprVnicProfileSetFsmStatus = _CfprVnicProfileSetFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 56, 1, 13),
    _CfprVnicProfileSetFsmStatus_Type()
)
cfprVnicProfileSetFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmStatus.setStatus("current")
_CfprVnicProfileSetFsmTry_Type = Gauge32
_CfprVnicProfileSetFsmTry_Object = MibTableColumn
cfprVnicProfileSetFsmTry = _CfprVnicProfileSetFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 56, 1, 14),
    _CfprVnicProfileSetFsmTry_Type()
)
cfprVnicProfileSetFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmTry.setStatus("current")
_CfprVnicProfileSetGenNum_Type = Gauge32
_CfprVnicProfileSetGenNum_Object = MibTableColumn
cfprVnicProfileSetGenNum = _CfprVnicProfileSetGenNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 56, 1, 15),
    _CfprVnicProfileSetGenNum_Type()
)
cfprVnicProfileSetGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetGenNum.setStatus("current")
_CfprVnicProfileSetFsmTable_Object = MibTable
cfprVnicProfileSetFsmTable = _CfprVnicProfileSetFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 57)
)
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmTable.setStatus("current")
_CfprVnicProfileSetFsmEntry_Object = MibTableRow
cfprVnicProfileSetFsmEntry = _CfprVnicProfileSetFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 57, 1)
)
cfprVnicProfileSetFsmEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicProfileSetFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmEntry.setStatus("current")
_CfprVnicProfileSetFsmInstanceId_Type = CfprManagedObjectId
_CfprVnicProfileSetFsmInstanceId_Object = MibTableColumn
cfprVnicProfileSetFsmInstanceId = _CfprVnicProfileSetFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 57, 1, 1),
    _CfprVnicProfileSetFsmInstanceId_Type()
)
cfprVnicProfileSetFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmInstanceId.setStatus("current")
_CfprVnicProfileSetFsmDn_Type = CfprManagedObjectDn
_CfprVnicProfileSetFsmDn_Object = MibTableColumn
cfprVnicProfileSetFsmDn = _CfprVnicProfileSetFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 57, 1, 2),
    _CfprVnicProfileSetFsmDn_Type()
)
cfprVnicProfileSetFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmDn.setStatus("current")
_CfprVnicProfileSetFsmRn_Type = SnmpAdminString
_CfprVnicProfileSetFsmRn_Object = MibTableColumn
cfprVnicProfileSetFsmRn = _CfprVnicProfileSetFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 57, 1, 3),
    _CfprVnicProfileSetFsmRn_Type()
)
cfprVnicProfileSetFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmRn.setStatus("current")
_CfprVnicProfileSetFsmCompletionTime_Type = DateAndTime
_CfprVnicProfileSetFsmCompletionTime_Object = MibTableColumn
cfprVnicProfileSetFsmCompletionTime = _CfprVnicProfileSetFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 57, 1, 4),
    _CfprVnicProfileSetFsmCompletionTime_Type()
)
cfprVnicProfileSetFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmCompletionTime.setStatus("current")
_CfprVnicProfileSetFsmCurrentFsm_Type = CfprVnicProfileSetFsmCurrentFsm
_CfprVnicProfileSetFsmCurrentFsm_Object = MibTableColumn
cfprVnicProfileSetFsmCurrentFsm = _CfprVnicProfileSetFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 57, 1, 5),
    _CfprVnicProfileSetFsmCurrentFsm_Type()
)
cfprVnicProfileSetFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmCurrentFsm.setStatus("current")
_CfprVnicProfileSetFsmDescrData_Type = SnmpAdminString
_CfprVnicProfileSetFsmDescrData_Object = MibTableColumn
cfprVnicProfileSetFsmDescrData = _CfprVnicProfileSetFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 57, 1, 6),
    _CfprVnicProfileSetFsmDescrData_Type()
)
cfprVnicProfileSetFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmDescrData.setStatus("current")
_CfprVnicProfileSetFsmFsmStatus_Type = CfprFsmFsmStageStatus
_CfprVnicProfileSetFsmFsmStatus_Object = MibTableColumn
cfprVnicProfileSetFsmFsmStatus = _CfprVnicProfileSetFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 57, 1, 7),
    _CfprVnicProfileSetFsmFsmStatus_Type()
)
cfprVnicProfileSetFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmFsmStatus.setStatus("current")
_CfprVnicProfileSetFsmProgress_Type = Gauge32
_CfprVnicProfileSetFsmProgress_Object = MibTableColumn
cfprVnicProfileSetFsmProgress = _CfprVnicProfileSetFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 57, 1, 8),
    _CfprVnicProfileSetFsmProgress_Type()
)
cfprVnicProfileSetFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmProgress.setStatus("current")
_CfprVnicProfileSetFsmRmtErrCode_Type = Gauge32
_CfprVnicProfileSetFsmRmtErrCode_Object = MibTableColumn
cfprVnicProfileSetFsmRmtErrCode = _CfprVnicProfileSetFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 57, 1, 9),
    _CfprVnicProfileSetFsmRmtErrCode_Type()
)
cfprVnicProfileSetFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmRmtErrCode.setStatus("current")
_CfprVnicProfileSetFsmRmtErrDescr_Type = SnmpAdminString
_CfprVnicProfileSetFsmRmtErrDescr_Object = MibTableColumn
cfprVnicProfileSetFsmRmtErrDescr = _CfprVnicProfileSetFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 57, 1, 10),
    _CfprVnicProfileSetFsmRmtErrDescr_Type()
)
cfprVnicProfileSetFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmRmtErrDescr.setStatus("current")
_CfprVnicProfileSetFsmRmtRslt_Type = CfprConditionRemoteInvRslt
_CfprVnicProfileSetFsmRmtRslt_Object = MibTableColumn
cfprVnicProfileSetFsmRmtRslt = _CfprVnicProfileSetFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 57, 1, 11),
    _CfprVnicProfileSetFsmRmtRslt_Type()
)
cfprVnicProfileSetFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmRmtRslt.setStatus("current")
_CfprVnicProfileSetFsmStageTable_Object = MibTable
cfprVnicProfileSetFsmStageTable = _CfprVnicProfileSetFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 58)
)
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmStageTable.setStatus("current")
_CfprVnicProfileSetFsmStageEntry_Object = MibTableRow
cfprVnicProfileSetFsmStageEntry = _CfprVnicProfileSetFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 58, 1)
)
cfprVnicProfileSetFsmStageEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicProfileSetFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmStageEntry.setStatus("current")
_CfprVnicProfileSetFsmStageInstanceId_Type = CfprManagedObjectId
_CfprVnicProfileSetFsmStageInstanceId_Object = MibTableColumn
cfprVnicProfileSetFsmStageInstanceId = _CfprVnicProfileSetFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 58, 1, 1),
    _CfprVnicProfileSetFsmStageInstanceId_Type()
)
cfprVnicProfileSetFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmStageInstanceId.setStatus("current")
_CfprVnicProfileSetFsmStageDn_Type = CfprManagedObjectDn
_CfprVnicProfileSetFsmStageDn_Object = MibTableColumn
cfprVnicProfileSetFsmStageDn = _CfprVnicProfileSetFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 58, 1, 2),
    _CfprVnicProfileSetFsmStageDn_Type()
)
cfprVnicProfileSetFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmStageDn.setStatus("current")
_CfprVnicProfileSetFsmStageRn_Type = SnmpAdminString
_CfprVnicProfileSetFsmStageRn_Object = MibTableColumn
cfprVnicProfileSetFsmStageRn = _CfprVnicProfileSetFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 58, 1, 3),
    _CfprVnicProfileSetFsmStageRn_Type()
)
cfprVnicProfileSetFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmStageRn.setStatus("current")
_CfprVnicProfileSetFsmStageDescrData_Type = SnmpAdminString
_CfprVnicProfileSetFsmStageDescrData_Object = MibTableColumn
cfprVnicProfileSetFsmStageDescrData = _CfprVnicProfileSetFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 58, 1, 4),
    _CfprVnicProfileSetFsmStageDescrData_Type()
)
cfprVnicProfileSetFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmStageDescrData.setStatus("current")
_CfprVnicProfileSetFsmStageLastUpdateTime_Type = DateAndTime
_CfprVnicProfileSetFsmStageLastUpdateTime_Object = MibTableColumn
cfprVnicProfileSetFsmStageLastUpdateTime = _CfprVnicProfileSetFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 58, 1, 5),
    _CfprVnicProfileSetFsmStageLastUpdateTime_Type()
)
cfprVnicProfileSetFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmStageLastUpdateTime.setStatus("current")
_CfprVnicProfileSetFsmStageName_Type = CfprVnicProfileSetFsmStageName
_CfprVnicProfileSetFsmStageName_Object = MibTableColumn
cfprVnicProfileSetFsmStageName = _CfprVnicProfileSetFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 58, 1, 6),
    _CfprVnicProfileSetFsmStageName_Type()
)
cfprVnicProfileSetFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmStageName.setStatus("current")
_CfprVnicProfileSetFsmStageOrder_Type = Gauge32
_CfprVnicProfileSetFsmStageOrder_Object = MibTableColumn
cfprVnicProfileSetFsmStageOrder = _CfprVnicProfileSetFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 58, 1, 7),
    _CfprVnicProfileSetFsmStageOrder_Type()
)
cfprVnicProfileSetFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmStageOrder.setStatus("current")
_CfprVnicProfileSetFsmStageRetry_Type = Gauge32
_CfprVnicProfileSetFsmStageRetry_Object = MibTableColumn
cfprVnicProfileSetFsmStageRetry = _CfprVnicProfileSetFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 58, 1, 8),
    _CfprVnicProfileSetFsmStageRetry_Type()
)
cfprVnicProfileSetFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmStageRetry.setStatus("current")
_CfprVnicProfileSetFsmStageStageStatus_Type = CfprFsmFsmStageStatus
_CfprVnicProfileSetFsmStageStageStatus_Object = MibTableColumn
cfprVnicProfileSetFsmStageStageStatus = _CfprVnicProfileSetFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 58, 1, 9),
    _CfprVnicProfileSetFsmStageStageStatus_Type()
)
cfprVnicProfileSetFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmStageStageStatus.setStatus("current")
_CfprVnicProfileSetFsmTaskTable_Object = MibTable
cfprVnicProfileSetFsmTaskTable = _CfprVnicProfileSetFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 59)
)
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmTaskTable.setStatus("current")
_CfprVnicProfileSetFsmTaskEntry_Object = MibTableRow
cfprVnicProfileSetFsmTaskEntry = _CfprVnicProfileSetFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 59, 1)
)
cfprVnicProfileSetFsmTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicProfileSetFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmTaskEntry.setStatus("current")
_CfprVnicProfileSetFsmTaskInstanceId_Type = CfprManagedObjectId
_CfprVnicProfileSetFsmTaskInstanceId_Object = MibTableColumn
cfprVnicProfileSetFsmTaskInstanceId = _CfprVnicProfileSetFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 59, 1, 1),
    _CfprVnicProfileSetFsmTaskInstanceId_Type()
)
cfprVnicProfileSetFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmTaskInstanceId.setStatus("current")
_CfprVnicProfileSetFsmTaskDn_Type = CfprManagedObjectDn
_CfprVnicProfileSetFsmTaskDn_Object = MibTableColumn
cfprVnicProfileSetFsmTaskDn = _CfprVnicProfileSetFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 59, 1, 2),
    _CfprVnicProfileSetFsmTaskDn_Type()
)
cfprVnicProfileSetFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmTaskDn.setStatus("current")
_CfprVnicProfileSetFsmTaskRn_Type = SnmpAdminString
_CfprVnicProfileSetFsmTaskRn_Object = MibTableColumn
cfprVnicProfileSetFsmTaskRn = _CfprVnicProfileSetFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 59, 1, 3),
    _CfprVnicProfileSetFsmTaskRn_Type()
)
cfprVnicProfileSetFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmTaskRn.setStatus("current")
_CfprVnicProfileSetFsmTaskCompletion_Type = CfprFsmCompletion
_CfprVnicProfileSetFsmTaskCompletion_Object = MibTableColumn
cfprVnicProfileSetFsmTaskCompletion = _CfprVnicProfileSetFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 59, 1, 4),
    _CfprVnicProfileSetFsmTaskCompletion_Type()
)
cfprVnicProfileSetFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmTaskCompletion.setStatus("current")
_CfprVnicProfileSetFsmTaskFlags_Type = CfprFsmFlags
_CfprVnicProfileSetFsmTaskFlags_Object = MibTableColumn
cfprVnicProfileSetFsmTaskFlags = _CfprVnicProfileSetFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 59, 1, 5),
    _CfprVnicProfileSetFsmTaskFlags_Type()
)
cfprVnicProfileSetFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmTaskFlags.setStatus("current")
_CfprVnicProfileSetFsmTaskItem_Type = CfprVnicProfileSetFsmTaskItem
_CfprVnicProfileSetFsmTaskItem_Object = MibTableColumn
cfprVnicProfileSetFsmTaskItem = _CfprVnicProfileSetFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 59, 1, 6),
    _CfprVnicProfileSetFsmTaskItem_Type()
)
cfprVnicProfileSetFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmTaskItem.setStatus("current")
_CfprVnicProfileSetFsmTaskSeqId_Type = Gauge32
_CfprVnicProfileSetFsmTaskSeqId_Object = MibTableColumn
cfprVnicProfileSetFsmTaskSeqId = _CfprVnicProfileSetFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 59, 1, 7),
    _CfprVnicProfileSetFsmTaskSeqId_Type()
)
cfprVnicProfileSetFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicProfileSetFsmTaskSeqId.setStatus("current")
_CfprVnicRackServerDiscoveryProfileTable_Object = MibTable
cfprVnicRackServerDiscoveryProfileTable = _CfprVnicRackServerDiscoveryProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 60)
)
if mibBuilder.loadTexts:
    cfprVnicRackServerDiscoveryProfileTable.setStatus("current")
_CfprVnicRackServerDiscoveryProfileEntry_Object = MibTableRow
cfprVnicRackServerDiscoveryProfileEntry = _CfprVnicRackServerDiscoveryProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 60, 1)
)
cfprVnicRackServerDiscoveryProfileEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicRackServerDiscoveryProfileInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicRackServerDiscoveryProfileEntry.setStatus("current")
_CfprVnicRackServerDiscoveryProfileInstanceId_Type = CfprManagedObjectId
_CfprVnicRackServerDiscoveryProfileInstanceId_Object = MibTableColumn
cfprVnicRackServerDiscoveryProfileInstanceId = _CfprVnicRackServerDiscoveryProfileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 60, 1, 1),
    _CfprVnicRackServerDiscoveryProfileInstanceId_Type()
)
cfprVnicRackServerDiscoveryProfileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicRackServerDiscoveryProfileInstanceId.setStatus("current")
_CfprVnicRackServerDiscoveryProfileDn_Type = CfprManagedObjectDn
_CfprVnicRackServerDiscoveryProfileDn_Object = MibTableColumn
cfprVnicRackServerDiscoveryProfileDn = _CfprVnicRackServerDiscoveryProfileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 60, 1, 2),
    _CfprVnicRackServerDiscoveryProfileDn_Type()
)
cfprVnicRackServerDiscoveryProfileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicRackServerDiscoveryProfileDn.setStatus("current")
_CfprVnicRackServerDiscoveryProfileRn_Type = SnmpAdminString
_CfprVnicRackServerDiscoveryProfileRn_Object = MibTableColumn
cfprVnicRackServerDiscoveryProfileRn = _CfprVnicRackServerDiscoveryProfileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 60, 1, 3),
    _CfprVnicRackServerDiscoveryProfileRn_Type()
)
cfprVnicRackServerDiscoveryProfileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicRackServerDiscoveryProfileRn.setStatus("current")
_CfprVnicRackServerDiscoveryProfileDescr_Type = SnmpAdminString
_CfprVnicRackServerDiscoveryProfileDescr_Object = MibTableColumn
cfprVnicRackServerDiscoveryProfileDescr = _CfprVnicRackServerDiscoveryProfileDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 60, 1, 4),
    _CfprVnicRackServerDiscoveryProfileDescr_Type()
)
cfprVnicRackServerDiscoveryProfileDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicRackServerDiscoveryProfileDescr.setStatus("current")
_CfprVnicRackServerDiscoveryProfileIntId_Type = SnmpAdminString
_CfprVnicRackServerDiscoveryProfileIntId_Object = MibTableColumn
cfprVnicRackServerDiscoveryProfileIntId = _CfprVnicRackServerDiscoveryProfileIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 60, 1, 5),
    _CfprVnicRackServerDiscoveryProfileIntId_Type()
)
cfprVnicRackServerDiscoveryProfileIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicRackServerDiscoveryProfileIntId.setStatus("current")
_CfprVnicRackServerDiscoveryProfileMaxPorts_Type = Gauge32
_CfprVnicRackServerDiscoveryProfileMaxPorts_Object = MibTableColumn
cfprVnicRackServerDiscoveryProfileMaxPorts = _CfprVnicRackServerDiscoveryProfileMaxPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 60, 1, 6),
    _CfprVnicRackServerDiscoveryProfileMaxPorts_Type()
)
cfprVnicRackServerDiscoveryProfileMaxPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicRackServerDiscoveryProfileMaxPorts.setStatus("current")
_CfprVnicRackServerDiscoveryProfileName_Type = SnmpAdminString
_CfprVnicRackServerDiscoveryProfileName_Object = MibTableColumn
cfprVnicRackServerDiscoveryProfileName = _CfprVnicRackServerDiscoveryProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 60, 1, 7),
    _CfprVnicRackServerDiscoveryProfileName_Type()
)
cfprVnicRackServerDiscoveryProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicRackServerDiscoveryProfileName.setStatus("current")
_CfprVnicRackServerDiscoveryProfilePolicyLevel_Type = Gauge32
_CfprVnicRackServerDiscoveryProfilePolicyLevel_Object = MibTableColumn
cfprVnicRackServerDiscoveryProfilePolicyLevel = _CfprVnicRackServerDiscoveryProfilePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 60, 1, 8),
    _CfprVnicRackServerDiscoveryProfilePolicyLevel_Type()
)
cfprVnicRackServerDiscoveryProfilePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicRackServerDiscoveryProfilePolicyLevel.setStatus("current")
_CfprVnicRackServerDiscoveryProfilePolicyOwner_Type = CfprPolicyPolicyOwner
_CfprVnicRackServerDiscoveryProfilePolicyOwner_Object = MibTableColumn
cfprVnicRackServerDiscoveryProfilePolicyOwner = _CfprVnicRackServerDiscoveryProfilePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 60, 1, 9),
    _CfprVnicRackServerDiscoveryProfilePolicyOwner_Type()
)
cfprVnicRackServerDiscoveryProfilePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicRackServerDiscoveryProfilePolicyOwner.setStatus("current")
_CfprVnicSanConnPolicyTable_Object = MibTable
cfprVnicSanConnPolicyTable = _CfprVnicSanConnPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 61)
)
if mibBuilder.loadTexts:
    cfprVnicSanConnPolicyTable.setStatus("current")
_CfprVnicSanConnPolicyEntry_Object = MibTableRow
cfprVnicSanConnPolicyEntry = _CfprVnicSanConnPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 61, 1)
)
cfprVnicSanConnPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicSanConnPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicSanConnPolicyEntry.setStatus("current")
_CfprVnicSanConnPolicyInstanceId_Type = CfprManagedObjectId
_CfprVnicSanConnPolicyInstanceId_Object = MibTableColumn
cfprVnicSanConnPolicyInstanceId = _CfprVnicSanConnPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 61, 1, 1),
    _CfprVnicSanConnPolicyInstanceId_Type()
)
cfprVnicSanConnPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicSanConnPolicyInstanceId.setStatus("current")
_CfprVnicSanConnPolicyDn_Type = CfprManagedObjectDn
_CfprVnicSanConnPolicyDn_Object = MibTableColumn
cfprVnicSanConnPolicyDn = _CfprVnicSanConnPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 61, 1, 2),
    _CfprVnicSanConnPolicyDn_Type()
)
cfprVnicSanConnPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicSanConnPolicyDn.setStatus("current")
_CfprVnicSanConnPolicyRn_Type = SnmpAdminString
_CfprVnicSanConnPolicyRn_Object = MibTableColumn
cfprVnicSanConnPolicyRn = _CfprVnicSanConnPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 61, 1, 3),
    _CfprVnicSanConnPolicyRn_Type()
)
cfprVnicSanConnPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicSanConnPolicyRn.setStatus("current")
_CfprVnicSanConnPolicyDescr_Type = SnmpAdminString
_CfprVnicSanConnPolicyDescr_Object = MibTableColumn
cfprVnicSanConnPolicyDescr = _CfprVnicSanConnPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 61, 1, 4),
    _CfprVnicSanConnPolicyDescr_Type()
)
cfprVnicSanConnPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicSanConnPolicyDescr.setStatus("current")
_CfprVnicSanConnPolicyFltAggr_Type = Unsigned64
_CfprVnicSanConnPolicyFltAggr_Object = MibTableColumn
cfprVnicSanConnPolicyFltAggr = _CfprVnicSanConnPolicyFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 61, 1, 5),
    _CfprVnicSanConnPolicyFltAggr_Type()
)
cfprVnicSanConnPolicyFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicSanConnPolicyFltAggr.setStatus("current")
_CfprVnicSanConnPolicyIntId_Type = SnmpAdminString
_CfprVnicSanConnPolicyIntId_Object = MibTableColumn
cfprVnicSanConnPolicyIntId = _CfprVnicSanConnPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 61, 1, 6),
    _CfprVnicSanConnPolicyIntId_Type()
)
cfprVnicSanConnPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicSanConnPolicyIntId.setStatus("current")
_CfprVnicSanConnPolicyName_Type = SnmpAdminString
_CfprVnicSanConnPolicyName_Object = MibTableColumn
cfprVnicSanConnPolicyName = _CfprVnicSanConnPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 61, 1, 7),
    _CfprVnicSanConnPolicyName_Type()
)
cfprVnicSanConnPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicSanConnPolicyName.setStatus("current")
_CfprVnicSanConnPolicyPolicyLevel_Type = Gauge32
_CfprVnicSanConnPolicyPolicyLevel_Object = MibTableColumn
cfprVnicSanConnPolicyPolicyLevel = _CfprVnicSanConnPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 61, 1, 8),
    _CfprVnicSanConnPolicyPolicyLevel_Type()
)
cfprVnicSanConnPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicSanConnPolicyPolicyLevel.setStatus("current")
_CfprVnicSanConnPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprVnicSanConnPolicyPolicyOwner_Object = MibTableColumn
cfprVnicSanConnPolicyPolicyOwner = _CfprVnicSanConnPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 61, 1, 9),
    _CfprVnicSanConnPolicyPolicyOwner_Type()
)
cfprVnicSanConnPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicSanConnPolicyPolicyOwner.setStatus("current")
_CfprVnicSanConnTemplTable_Object = MibTable
cfprVnicSanConnTemplTable = _CfprVnicSanConnTemplTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 62)
)
if mibBuilder.loadTexts:
    cfprVnicSanConnTemplTable.setStatus("current")
_CfprVnicSanConnTemplEntry_Object = MibTableRow
cfprVnicSanConnTemplEntry = _CfprVnicSanConnTemplEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 62, 1)
)
cfprVnicSanConnTemplEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicSanConnTemplInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicSanConnTemplEntry.setStatus("current")
_CfprVnicSanConnTemplInstanceId_Type = CfprManagedObjectId
_CfprVnicSanConnTemplInstanceId_Object = MibTableColumn
cfprVnicSanConnTemplInstanceId = _CfprVnicSanConnTemplInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 62, 1, 1),
    _CfprVnicSanConnTemplInstanceId_Type()
)
cfprVnicSanConnTemplInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicSanConnTemplInstanceId.setStatus("current")
_CfprVnicSanConnTemplDn_Type = CfprManagedObjectDn
_CfprVnicSanConnTemplDn_Object = MibTableColumn
cfprVnicSanConnTemplDn = _CfprVnicSanConnTemplDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 62, 1, 2),
    _CfprVnicSanConnTemplDn_Type()
)
cfprVnicSanConnTemplDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicSanConnTemplDn.setStatus("current")
_CfprVnicSanConnTemplRn_Type = SnmpAdminString
_CfprVnicSanConnTemplRn_Object = MibTableColumn
cfprVnicSanConnTemplRn = _CfprVnicSanConnTemplRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 62, 1, 3),
    _CfprVnicSanConnTemplRn_Type()
)
cfprVnicSanConnTemplRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicSanConnTemplRn.setStatus("current")
_CfprVnicSanConnTemplDescr_Type = SnmpAdminString
_CfprVnicSanConnTemplDescr_Object = MibTableColumn
cfprVnicSanConnTemplDescr = _CfprVnicSanConnTemplDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 62, 1, 4),
    _CfprVnicSanConnTemplDescr_Type()
)
cfprVnicSanConnTemplDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicSanConnTemplDescr.setStatus("current")
_CfprVnicSanConnTemplIdentPoolName_Type = SnmpAdminString
_CfprVnicSanConnTemplIdentPoolName_Object = MibTableColumn
cfprVnicSanConnTemplIdentPoolName = _CfprVnicSanConnTemplIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 62, 1, 5),
    _CfprVnicSanConnTemplIdentPoolName_Type()
)
cfprVnicSanConnTemplIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicSanConnTemplIdentPoolName.setStatus("current")
_CfprVnicSanConnTemplIntId_Type = SnmpAdminString
_CfprVnicSanConnTemplIntId_Object = MibTableColumn
cfprVnicSanConnTemplIntId = _CfprVnicSanConnTemplIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 62, 1, 6),
    _CfprVnicSanConnTemplIntId_Type()
)
cfprVnicSanConnTemplIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicSanConnTemplIntId.setStatus("current")
_CfprVnicSanConnTemplMaxDataFieldSize_Type = Gauge32
_CfprVnicSanConnTemplMaxDataFieldSize_Object = MibTableColumn
cfprVnicSanConnTemplMaxDataFieldSize = _CfprVnicSanConnTemplMaxDataFieldSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 62, 1, 7),
    _CfprVnicSanConnTemplMaxDataFieldSize_Type()
)
cfprVnicSanConnTemplMaxDataFieldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicSanConnTemplMaxDataFieldSize.setStatus("current")
_CfprVnicSanConnTemplName_Type = SnmpAdminString
_CfprVnicSanConnTemplName_Object = MibTableColumn
cfprVnicSanConnTemplName = _CfprVnicSanConnTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 62, 1, 8),
    _CfprVnicSanConnTemplName_Type()
)
cfprVnicSanConnTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicSanConnTemplName.setStatus("current")
_CfprVnicSanConnTemplNwCtrlPolicyName_Type = SnmpAdminString
_CfprVnicSanConnTemplNwCtrlPolicyName_Object = MibTableColumn
cfprVnicSanConnTemplNwCtrlPolicyName = _CfprVnicSanConnTemplNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 62, 1, 9),
    _CfprVnicSanConnTemplNwCtrlPolicyName_Type()
)
cfprVnicSanConnTemplNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicSanConnTemplNwCtrlPolicyName.setStatus("current")
_CfprVnicSanConnTemplOperIdentPoolName_Type = SnmpAdminString
_CfprVnicSanConnTemplOperIdentPoolName_Object = MibTableColumn
cfprVnicSanConnTemplOperIdentPoolName = _CfprVnicSanConnTemplOperIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 62, 1, 10),
    _CfprVnicSanConnTemplOperIdentPoolName_Type()
)
cfprVnicSanConnTemplOperIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicSanConnTemplOperIdentPoolName.setStatus("current")
_CfprVnicSanConnTemplOperQosPolicyName_Type = SnmpAdminString
_CfprVnicSanConnTemplOperQosPolicyName_Object = MibTableColumn
cfprVnicSanConnTemplOperQosPolicyName = _CfprVnicSanConnTemplOperQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 62, 1, 11),
    _CfprVnicSanConnTemplOperQosPolicyName_Type()
)
cfprVnicSanConnTemplOperQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicSanConnTemplOperQosPolicyName.setStatus("current")
_CfprVnicSanConnTemplOperStatsPolicyName_Type = SnmpAdminString
_CfprVnicSanConnTemplOperStatsPolicyName_Object = MibTableColumn
cfprVnicSanConnTemplOperStatsPolicyName = _CfprVnicSanConnTemplOperStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 62, 1, 12),
    _CfprVnicSanConnTemplOperStatsPolicyName_Type()
)
cfprVnicSanConnTemplOperStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicSanConnTemplOperStatsPolicyName.setStatus("current")
_CfprVnicSanConnTemplPinToGroupName_Type = SnmpAdminString
_CfprVnicSanConnTemplPinToGroupName_Object = MibTableColumn
cfprVnicSanConnTemplPinToGroupName = _CfprVnicSanConnTemplPinToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 62, 1, 13),
    _CfprVnicSanConnTemplPinToGroupName_Type()
)
cfprVnicSanConnTemplPinToGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicSanConnTemplPinToGroupName.setStatus("current")
_CfprVnicSanConnTemplPolicyLevel_Type = Gauge32
_CfprVnicSanConnTemplPolicyLevel_Object = MibTableColumn
cfprVnicSanConnTemplPolicyLevel = _CfprVnicSanConnTemplPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 62, 1, 14),
    _CfprVnicSanConnTemplPolicyLevel_Type()
)
cfprVnicSanConnTemplPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicSanConnTemplPolicyLevel.setStatus("current")
_CfprVnicSanConnTemplPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprVnicSanConnTemplPolicyOwner_Object = MibTableColumn
cfprVnicSanConnTemplPolicyOwner = _CfprVnicSanConnTemplPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 62, 1, 15),
    _CfprVnicSanConnTemplPolicyOwner_Type()
)
cfprVnicSanConnTemplPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicSanConnTemplPolicyOwner.setStatus("current")
_CfprVnicSanConnTemplQosPolicyName_Type = SnmpAdminString
_CfprVnicSanConnTemplQosPolicyName_Object = MibTableColumn
cfprVnicSanConnTemplQosPolicyName = _CfprVnicSanConnTemplQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 62, 1, 16),
    _CfprVnicSanConnTemplQosPolicyName_Type()
)
cfprVnicSanConnTemplQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicSanConnTemplQosPolicyName.setStatus("current")
_CfprVnicSanConnTemplStatsPolicyName_Type = SnmpAdminString
_CfprVnicSanConnTemplStatsPolicyName_Object = MibTableColumn
cfprVnicSanConnTemplStatsPolicyName = _CfprVnicSanConnTemplStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 62, 1, 17),
    _CfprVnicSanConnTemplStatsPolicyName_Type()
)
cfprVnicSanConnTemplStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicSanConnTemplStatsPolicyName.setStatus("current")
_CfprVnicSanConnTemplSwitchId_Type = CfprNetworkSwitchId
_CfprVnicSanConnTemplSwitchId_Object = MibTableColumn
cfprVnicSanConnTemplSwitchId = _CfprVnicSanConnTemplSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 62, 1, 18),
    _CfprVnicSanConnTemplSwitchId_Type()
)
cfprVnicSanConnTemplSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicSanConnTemplSwitchId.setStatus("current")
_CfprVnicSanConnTemplTarget_Type = CfprVnicSanConnTemplTarget
_CfprVnicSanConnTemplTarget_Object = MibTableColumn
cfprVnicSanConnTemplTarget = _CfprVnicSanConnTemplTarget_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 62, 1, 19),
    _CfprVnicSanConnTemplTarget_Type()
)
cfprVnicSanConnTemplTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicSanConnTemplTarget.setStatus("current")
_CfprVnicSanConnTemplTemplType_Type = CfprVnicTemplateType
_CfprVnicSanConnTemplTemplType_Object = MibTableColumn
cfprVnicSanConnTemplTemplType = _CfprVnicSanConnTemplTemplType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 62, 1, 20),
    _CfprVnicSanConnTemplTemplType_Type()
)
cfprVnicSanConnTemplTemplType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicSanConnTemplTemplType.setStatus("current")
_CfprVnicScsiTable_Object = MibTable
cfprVnicScsiTable = _CfprVnicScsiTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 63)
)
if mibBuilder.loadTexts:
    cfprVnicScsiTable.setStatus("current")
_CfprVnicScsiEntry_Object = MibTableRow
cfprVnicScsiEntry = _CfprVnicScsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 63, 1)
)
cfprVnicScsiEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicScsiInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicScsiEntry.setStatus("current")
_CfprVnicScsiInstanceId_Type = CfprManagedObjectId
_CfprVnicScsiInstanceId_Object = MibTableColumn
cfprVnicScsiInstanceId = _CfprVnicScsiInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 63, 1, 1),
    _CfprVnicScsiInstanceId_Type()
)
cfprVnicScsiInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicScsiInstanceId.setStatus("current")
_CfprVnicScsiDn_Type = CfprManagedObjectDn
_CfprVnicScsiDn_Object = MibTableColumn
cfprVnicScsiDn = _CfprVnicScsiDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 63, 1, 2),
    _CfprVnicScsiDn_Type()
)
cfprVnicScsiDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiDn.setStatus("current")
_CfprVnicScsiRn_Type = SnmpAdminString
_CfprVnicScsiRn_Object = MibTableColumn
cfprVnicScsiRn = _CfprVnicScsiRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 63, 1, 3),
    _CfprVnicScsiRn_Type()
)
cfprVnicScsiRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiRn.setStatus("current")
_CfprVnicScsiAdaptorProfileName_Type = SnmpAdminString
_CfprVnicScsiAdaptorProfileName_Object = MibTableColumn
cfprVnicScsiAdaptorProfileName = _CfprVnicScsiAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 63, 1, 4),
    _CfprVnicScsiAdaptorProfileName_Type()
)
cfprVnicScsiAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiAdaptorProfileName.setStatus("current")
_CfprVnicScsiAdminHostPort_Type = CfprFabricHostPortId
_CfprVnicScsiAdminHostPort_Object = MibTableColumn
cfprVnicScsiAdminHostPort = _CfprVnicScsiAdminHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 63, 1, 5),
    _CfprVnicScsiAdminHostPort_Type()
)
cfprVnicScsiAdminHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiAdminHostPort.setStatus("current")
_CfprVnicScsiAdminVcon_Type = SnmpAdminString
_CfprVnicScsiAdminVcon_Object = MibTableColumn
cfprVnicScsiAdminVcon = _CfprVnicScsiAdminVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 63, 1, 6),
    _CfprVnicScsiAdminVcon_Type()
)
cfprVnicScsiAdminVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiAdminVcon.setStatus("current")
_CfprVnicScsiAppRole_Type = CfprVnicAppRole
_CfprVnicScsiAppRole_Object = MibTableColumn
cfprVnicScsiAppRole = _CfprVnicScsiAppRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 63, 1, 7),
    _CfprVnicScsiAppRole_Type()
)
cfprVnicScsiAppRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiAppRole.setStatus("current")
_CfprVnicScsiBootDev_Type = CfprVnicVnicBootDev
_CfprVnicScsiBootDev_Object = MibTableColumn
cfprVnicScsiBootDev = _CfprVnicScsiBootDev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 63, 1, 8),
    _CfprVnicScsiBootDev_Type()
)
cfprVnicScsiBootDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiBootDev.setStatus("current")
_CfprVnicScsiConfigQualifier_Type = CfprVnicConfigIssues
_CfprVnicScsiConfigQualifier_Object = MibTableColumn
cfprVnicScsiConfigQualifier = _CfprVnicScsiConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 63, 1, 9),
    _CfprVnicScsiConfigQualifier_Type()
)
cfprVnicScsiConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiConfigQualifier.setStatus("current")
_CfprVnicScsiConfigState_Type = CfprLsConfigState
_CfprVnicScsiConfigState_Object = MibTableColumn
cfprVnicScsiConfigState = _CfprVnicScsiConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 63, 1, 10),
    _CfprVnicScsiConfigState_Type()
)
cfprVnicScsiConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiConfigState.setStatus("current")
_CfprVnicScsiEquipmentDn_Type = SnmpAdminString
_CfprVnicScsiEquipmentDn_Object = MibTableColumn
cfprVnicScsiEquipmentDn = _CfprVnicScsiEquipmentDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 63, 1, 11),
    _CfprVnicScsiEquipmentDn_Type()
)
cfprVnicScsiEquipmentDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiEquipmentDn.setStatus("current")
_CfprVnicScsiIdentPoolName_Type = SnmpAdminString
_CfprVnicScsiIdentPoolName_Object = MibTableColumn
cfprVnicScsiIdentPoolName = _CfprVnicScsiIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 63, 1, 12),
    _CfprVnicScsiIdentPoolName_Type()
)
cfprVnicScsiIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiIdentPoolName.setStatus("current")
_CfprVnicScsiInstType_Type = CfprVnicInstantiation
_CfprVnicScsiInstType_Object = MibTableColumn
cfprVnicScsiInstType = _CfprVnicScsiInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 63, 1, 13),
    _CfprVnicScsiInstType_Type()
)
cfprVnicScsiInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiInstType.setStatus("current")
_CfprVnicScsiName_Type = SnmpAdminString
_CfprVnicScsiName_Object = MibTableColumn
cfprVnicScsiName = _CfprVnicScsiName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 63, 1, 14),
    _CfprVnicScsiName_Type()
)
cfprVnicScsiName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiName.setStatus("current")
_CfprVnicScsiNwTemplName_Type = SnmpAdminString
_CfprVnicScsiNwTemplName_Object = MibTableColumn
cfprVnicScsiNwTemplName = _CfprVnicScsiNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 63, 1, 15),
    _CfprVnicScsiNwTemplName_Type()
)
cfprVnicScsiNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiNwTemplName.setStatus("current")
_CfprVnicScsiOperHostPort_Type = CfprVnicVnicOperHostPort
_CfprVnicScsiOperHostPort_Object = MibTableColumn
cfprVnicScsiOperHostPort = _CfprVnicScsiOperHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 63, 1, 16),
    _CfprVnicScsiOperHostPort_Type()
)
cfprVnicScsiOperHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiOperHostPort.setStatus("current")
_CfprVnicScsiOperOrder_Type = Gauge32
_CfprVnicScsiOperOrder_Object = MibTableColumn
cfprVnicScsiOperOrder = _CfprVnicScsiOperOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 63, 1, 17),
    _CfprVnicScsiOperOrder_Type()
)
cfprVnicScsiOperOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiOperOrder.setStatus("current")
_CfprVnicScsiOperSpeed_Type = Gauge32
_CfprVnicScsiOperSpeed_Object = MibTableColumn
cfprVnicScsiOperSpeed = _CfprVnicScsiOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 63, 1, 18),
    _CfprVnicScsiOperSpeed_Type()
)
cfprVnicScsiOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiOperSpeed.setStatus("current")
_CfprVnicScsiOperStatsPolicyName_Type = SnmpAdminString
_CfprVnicScsiOperStatsPolicyName_Object = MibTableColumn
cfprVnicScsiOperStatsPolicyName = _CfprVnicScsiOperStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 63, 1, 19),
    _CfprVnicScsiOperStatsPolicyName_Type()
)
cfprVnicScsiOperStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiOperStatsPolicyName.setStatus("current")
_CfprVnicScsiOperVcon_Type = SnmpAdminString
_CfprVnicScsiOperVcon_Object = MibTableColumn
cfprVnicScsiOperVcon = _CfprVnicScsiOperVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 63, 1, 20),
    _CfprVnicScsiOperVcon_Type()
)
cfprVnicScsiOperVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiOperVcon.setStatus("current")
_CfprVnicScsiOrder_Type = Gauge32
_CfprVnicScsiOrder_Object = MibTableColumn
cfprVnicScsiOrder = _CfprVnicScsiOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 63, 1, 21),
    _CfprVnicScsiOrder_Type()
)
cfprVnicScsiOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiOrder.setStatus("current")
_CfprVnicScsiOwner_Type = CfprVnicConnectionOwner
_CfprVnicScsiOwner_Object = MibTableColumn
cfprVnicScsiOwner = _CfprVnicScsiOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 63, 1, 22),
    _CfprVnicScsiOwner_Type()
)
cfprVnicScsiOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiOwner.setStatus("current")
_CfprVnicScsiPinToGroupName_Type = SnmpAdminString
_CfprVnicScsiPinToGroupName_Object = MibTableColumn
cfprVnicScsiPinToGroupName = _CfprVnicScsiPinToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 63, 1, 23),
    _CfprVnicScsiPinToGroupName_Type()
)
cfprVnicScsiPinToGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiPinToGroupName.setStatus("current")
_CfprVnicScsiQosPolicyName_Type = SnmpAdminString
_CfprVnicScsiQosPolicyName_Object = MibTableColumn
cfprVnicScsiQosPolicyName = _CfprVnicScsiQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 63, 1, 24),
    _CfprVnicScsiQosPolicyName_Type()
)
cfprVnicScsiQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiQosPolicyName.setStatus("current")
_CfprVnicScsiStatsPolicyName_Type = SnmpAdminString
_CfprVnicScsiStatsPolicyName_Object = MibTableColumn
cfprVnicScsiStatsPolicyName = _CfprVnicScsiStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 63, 1, 25),
    _CfprVnicScsiStatsPolicyName_Type()
)
cfprVnicScsiStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiStatsPolicyName.setStatus("current")
_CfprVnicScsiSwitchId_Type = CfprNetworkSwitchId
_CfprVnicScsiSwitchId_Object = MibTableColumn
cfprVnicScsiSwitchId = _CfprVnicScsiSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 63, 1, 26),
    _CfprVnicScsiSwitchId_Type()
)
cfprVnicScsiSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiSwitchId.setStatus("current")
_CfprVnicScsiType_Type = CfprVnicScsiType
_CfprVnicScsiType_Object = MibTableColumn
cfprVnicScsiType = _CfprVnicScsiType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 63, 1, 27),
    _CfprVnicScsiType_Type()
)
cfprVnicScsiType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiType.setStatus("current")
_CfprVnicScsiIfTable_Object = MibTable
cfprVnicScsiIfTable = _CfprVnicScsiIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 64)
)
if mibBuilder.loadTexts:
    cfprVnicScsiIfTable.setStatus("current")
_CfprVnicScsiIfEntry_Object = MibTableRow
cfprVnicScsiIfEntry = _CfprVnicScsiIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 64, 1)
)
cfprVnicScsiIfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicScsiIfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicScsiIfEntry.setStatus("current")
_CfprVnicScsiIfInstanceId_Type = CfprManagedObjectId
_CfprVnicScsiIfInstanceId_Object = MibTableColumn
cfprVnicScsiIfInstanceId = _CfprVnicScsiIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 64, 1, 1),
    _CfprVnicScsiIfInstanceId_Type()
)
cfprVnicScsiIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicScsiIfInstanceId.setStatus("current")
_CfprVnicScsiIfDn_Type = CfprManagedObjectDn
_CfprVnicScsiIfDn_Object = MibTableColumn
cfprVnicScsiIfDn = _CfprVnicScsiIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 64, 1, 2),
    _CfprVnicScsiIfDn_Type()
)
cfprVnicScsiIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiIfDn.setStatus("current")
_CfprVnicScsiIfRn_Type = SnmpAdminString
_CfprVnicScsiIfRn_Object = MibTableColumn
cfprVnicScsiIfRn = _CfprVnicScsiIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 64, 1, 3),
    _CfprVnicScsiIfRn_Type()
)
cfprVnicScsiIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiIfRn.setStatus("current")
_CfprVnicScsiIfAddr_Type = Unsigned64
_CfprVnicScsiIfAddr_Object = MibTableColumn
cfprVnicScsiIfAddr = _CfprVnicScsiIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 64, 1, 4),
    _CfprVnicScsiIfAddr_Type()
)
cfprVnicScsiIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiIfAddr.setStatus("current")
_CfprVnicScsiIfConfigQualifier_Type = CfprVnicConfigIssues
_CfprVnicScsiIfConfigQualifier_Object = MibTableColumn
cfprVnicScsiIfConfigQualifier = _CfprVnicScsiIfConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 64, 1, 5),
    _CfprVnicScsiIfConfigQualifier_Type()
)
cfprVnicScsiIfConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiIfConfigQualifier.setStatus("current")
_CfprVnicScsiIfName_Type = SnmpAdminString
_CfprVnicScsiIfName_Object = MibTableColumn
cfprVnicScsiIfName = _CfprVnicScsiIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 64, 1, 6),
    _CfprVnicScsiIfName_Type()
)
cfprVnicScsiIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiIfName.setStatus("current")
_CfprVnicScsiIfOperState_Type = CfprVnicIfOperState
_CfprVnicScsiIfOperState_Object = MibTableColumn
cfprVnicScsiIfOperState = _CfprVnicScsiIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 64, 1, 7),
    _CfprVnicScsiIfOperState_Type()
)
cfprVnicScsiIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiIfOperState.setStatus("current")
_CfprVnicScsiIfOperVnetDn_Type = SnmpAdminString
_CfprVnicScsiIfOperVnetDn_Object = MibTableColumn
cfprVnicScsiIfOperVnetDn = _CfprVnicScsiIfOperVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 64, 1, 8),
    _CfprVnicScsiIfOperVnetDn_Type()
)
cfprVnicScsiIfOperVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiIfOperVnetDn.setStatus("current")
_CfprVnicScsiIfOperVnetName_Type = SnmpAdminString
_CfprVnicScsiIfOperVnetName_Object = MibTableColumn
cfprVnicScsiIfOperVnetName = _CfprVnicScsiIfOperVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 64, 1, 9),
    _CfprVnicScsiIfOperVnetName_Type()
)
cfprVnicScsiIfOperVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiIfOperVnetName.setStatus("current")
_CfprVnicScsiIfOwner_Type = CfprVnicConnectionOwner
_CfprVnicScsiIfOwner_Object = MibTableColumn
cfprVnicScsiIfOwner = _CfprVnicScsiIfOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 64, 1, 10),
    _CfprVnicScsiIfOwner_Type()
)
cfprVnicScsiIfOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiIfOwner.setStatus("current")
_CfprVnicScsiIfPubNwId_Type = Gauge32
_CfprVnicScsiIfPubNwId_Object = MibTableColumn
cfprVnicScsiIfPubNwId = _CfprVnicScsiIfPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 64, 1, 11),
    _CfprVnicScsiIfPubNwId_Type()
)
cfprVnicScsiIfPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiIfPubNwId.setStatus("current")
_CfprVnicScsiIfSharing_Type = CfprFabricVlanSharingType
_CfprVnicScsiIfSharing_Object = MibTableColumn
cfprVnicScsiIfSharing = _CfprVnicScsiIfSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 64, 1, 12),
    _CfprVnicScsiIfSharing_Type()
)
cfprVnicScsiIfSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiIfSharing.setStatus("current")
_CfprVnicScsiIfSwitchId_Type = CfprNetworkSwitchId
_CfprVnicScsiIfSwitchId_Object = MibTableColumn
cfprVnicScsiIfSwitchId = _CfprVnicScsiIfSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 64, 1, 13),
    _CfprVnicScsiIfSwitchId_Type()
)
cfprVnicScsiIfSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiIfSwitchId.setStatus("current")
_CfprVnicScsiIfType_Type = CfprVnicAScsiIfType
_CfprVnicScsiIfType_Object = MibTableColumn
cfprVnicScsiIfType = _CfprVnicScsiIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 64, 1, 14),
    _CfprVnicScsiIfType_Type()
)
cfprVnicScsiIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiIfType.setStatus("current")
_CfprVnicScsiIfVnet_Type = Gauge32
_CfprVnicScsiIfVnet_Object = MibTableColumn
cfprVnicScsiIfVnet = _CfprVnicScsiIfVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 64, 1, 15),
    _CfprVnicScsiIfVnet_Type()
)
cfprVnicScsiIfVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicScsiIfVnet.setStatus("current")
_CfprVnicUsnicConPolicyTable_Object = MibTable
cfprVnicUsnicConPolicyTable = _CfprVnicUsnicConPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 65)
)
if mibBuilder.loadTexts:
    cfprVnicUsnicConPolicyTable.setStatus("current")
_CfprVnicUsnicConPolicyEntry_Object = MibTableRow
cfprVnicUsnicConPolicyEntry = _CfprVnicUsnicConPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 65, 1)
)
cfprVnicUsnicConPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicUsnicConPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicUsnicConPolicyEntry.setStatus("current")
_CfprVnicUsnicConPolicyInstanceId_Type = CfprManagedObjectId
_CfprVnicUsnicConPolicyInstanceId_Object = MibTableColumn
cfprVnicUsnicConPolicyInstanceId = _CfprVnicUsnicConPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 65, 1, 1),
    _CfprVnicUsnicConPolicyInstanceId_Type()
)
cfprVnicUsnicConPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicUsnicConPolicyInstanceId.setStatus("current")
_CfprVnicUsnicConPolicyDn_Type = CfprManagedObjectDn
_CfprVnicUsnicConPolicyDn_Object = MibTableColumn
cfprVnicUsnicConPolicyDn = _CfprVnicUsnicConPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 65, 1, 2),
    _CfprVnicUsnicConPolicyDn_Type()
)
cfprVnicUsnicConPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicUsnicConPolicyDn.setStatus("current")
_CfprVnicUsnicConPolicyRn_Type = SnmpAdminString
_CfprVnicUsnicConPolicyRn_Object = MibTableColumn
cfprVnicUsnicConPolicyRn = _CfprVnicUsnicConPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 65, 1, 3),
    _CfprVnicUsnicConPolicyRn_Type()
)
cfprVnicUsnicConPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicUsnicConPolicyRn.setStatus("current")
_CfprVnicUsnicConPolicyAdaptorProfileName_Type = SnmpAdminString
_CfprVnicUsnicConPolicyAdaptorProfileName_Object = MibTableColumn
cfprVnicUsnicConPolicyAdaptorProfileName = _CfprVnicUsnicConPolicyAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 65, 1, 4),
    _CfprVnicUsnicConPolicyAdaptorProfileName_Type()
)
cfprVnicUsnicConPolicyAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicUsnicConPolicyAdaptorProfileName.setStatus("current")
_CfprVnicUsnicConPolicyDescr_Type = SnmpAdminString
_CfprVnicUsnicConPolicyDescr_Object = MibTableColumn
cfprVnicUsnicConPolicyDescr = _CfprVnicUsnicConPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 65, 1, 5),
    _CfprVnicUsnicConPolicyDescr_Type()
)
cfprVnicUsnicConPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicUsnicConPolicyDescr.setStatus("current")
_CfprVnicUsnicConPolicyIntId_Type = SnmpAdminString
_CfprVnicUsnicConPolicyIntId_Object = MibTableColumn
cfprVnicUsnicConPolicyIntId = _CfprVnicUsnicConPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 65, 1, 6),
    _CfprVnicUsnicConPolicyIntId_Type()
)
cfprVnicUsnicConPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicUsnicConPolicyIntId.setStatus("current")
_CfprVnicUsnicConPolicyName_Type = SnmpAdminString
_CfprVnicUsnicConPolicyName_Object = MibTableColumn
cfprVnicUsnicConPolicyName = _CfprVnicUsnicConPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 65, 1, 7),
    _CfprVnicUsnicConPolicyName_Type()
)
cfprVnicUsnicConPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicUsnicConPolicyName.setStatus("current")
_CfprVnicUsnicConPolicyPolicyLevel_Type = Gauge32
_CfprVnicUsnicConPolicyPolicyLevel_Object = MibTableColumn
cfprVnicUsnicConPolicyPolicyLevel = _CfprVnicUsnicConPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 65, 1, 8),
    _CfprVnicUsnicConPolicyPolicyLevel_Type()
)
cfprVnicUsnicConPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicUsnicConPolicyPolicyLevel.setStatus("current")
_CfprVnicUsnicConPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprVnicUsnicConPolicyPolicyOwner_Object = MibTableColumn
cfprVnicUsnicConPolicyPolicyOwner = _CfprVnicUsnicConPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 65, 1, 9),
    _CfprVnicUsnicConPolicyPolicyOwner_Type()
)
cfprVnicUsnicConPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicUsnicConPolicyPolicyOwner.setStatus("current")
_CfprVnicUsnicConPolicyUsnicCount_Type = Gauge32
_CfprVnicUsnicConPolicyUsnicCount_Object = MibTableColumn
cfprVnicUsnicConPolicyUsnicCount = _CfprVnicUsnicConPolicyUsnicCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 65, 1, 10),
    _CfprVnicUsnicConPolicyUsnicCount_Type()
)
cfprVnicUsnicConPolicyUsnicCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicUsnicConPolicyUsnicCount.setStatus("current")
_CfprVnicUsnicConPolicyRefTable_Object = MibTable
cfprVnicUsnicConPolicyRefTable = _CfprVnicUsnicConPolicyRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 66)
)
if mibBuilder.loadTexts:
    cfprVnicUsnicConPolicyRefTable.setStatus("current")
_CfprVnicUsnicConPolicyRefEntry_Object = MibTableRow
cfprVnicUsnicConPolicyRefEntry = _CfprVnicUsnicConPolicyRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 66, 1)
)
cfprVnicUsnicConPolicyRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicUsnicConPolicyRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicUsnicConPolicyRefEntry.setStatus("current")
_CfprVnicUsnicConPolicyRefInstanceId_Type = CfprManagedObjectId
_CfprVnicUsnicConPolicyRefInstanceId_Object = MibTableColumn
cfprVnicUsnicConPolicyRefInstanceId = _CfprVnicUsnicConPolicyRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 66, 1, 1),
    _CfprVnicUsnicConPolicyRefInstanceId_Type()
)
cfprVnicUsnicConPolicyRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicUsnicConPolicyRefInstanceId.setStatus("current")
_CfprVnicUsnicConPolicyRefDn_Type = CfprManagedObjectDn
_CfprVnicUsnicConPolicyRefDn_Object = MibTableColumn
cfprVnicUsnicConPolicyRefDn = _CfprVnicUsnicConPolicyRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 66, 1, 2),
    _CfprVnicUsnicConPolicyRefDn_Type()
)
cfprVnicUsnicConPolicyRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicUsnicConPolicyRefDn.setStatus("current")
_CfprVnicUsnicConPolicyRefRn_Type = SnmpAdminString
_CfprVnicUsnicConPolicyRefRn_Object = MibTableColumn
cfprVnicUsnicConPolicyRefRn = _CfprVnicUsnicConPolicyRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 66, 1, 3),
    _CfprVnicUsnicConPolicyRefRn_Type()
)
cfprVnicUsnicConPolicyRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicUsnicConPolicyRefRn.setStatus("current")
_CfprVnicUsnicConPolicyRefConPolicyName_Type = SnmpAdminString
_CfprVnicUsnicConPolicyRefConPolicyName_Object = MibTableColumn
cfprVnicUsnicConPolicyRefConPolicyName = _CfprVnicUsnicConPolicyRefConPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 66, 1, 4),
    _CfprVnicUsnicConPolicyRefConPolicyName_Type()
)
cfprVnicUsnicConPolicyRefConPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicUsnicConPolicyRefConPolicyName.setStatus("current")
_CfprVnicUsnicConPolicyRefOperConPolicyName_Type = SnmpAdminString
_CfprVnicUsnicConPolicyRefOperConPolicyName_Object = MibTableColumn
cfprVnicUsnicConPolicyRefOperConPolicyName = _CfprVnicUsnicConPolicyRefOperConPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 66, 1, 5),
    _CfprVnicUsnicConPolicyRefOperConPolicyName_Type()
)
cfprVnicUsnicConPolicyRefOperConPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicUsnicConPolicyRefOperConPolicyName.setStatus("current")
_CfprVnicVhbaBehPolicyTable_Object = MibTable
cfprVnicVhbaBehPolicyTable = _CfprVnicVhbaBehPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 67)
)
if mibBuilder.loadTexts:
    cfprVnicVhbaBehPolicyTable.setStatus("current")
_CfprVnicVhbaBehPolicyEntry_Object = MibTableRow
cfprVnicVhbaBehPolicyEntry = _CfprVnicVhbaBehPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 67, 1)
)
cfprVnicVhbaBehPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicVhbaBehPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicVhbaBehPolicyEntry.setStatus("current")
_CfprVnicVhbaBehPolicyInstanceId_Type = CfprManagedObjectId
_CfprVnicVhbaBehPolicyInstanceId_Object = MibTableColumn
cfprVnicVhbaBehPolicyInstanceId = _CfprVnicVhbaBehPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 67, 1, 1),
    _CfprVnicVhbaBehPolicyInstanceId_Type()
)
cfprVnicVhbaBehPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicVhbaBehPolicyInstanceId.setStatus("current")
_CfprVnicVhbaBehPolicyDn_Type = CfprManagedObjectDn
_CfprVnicVhbaBehPolicyDn_Object = MibTableColumn
cfprVnicVhbaBehPolicyDn = _CfprVnicVhbaBehPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 67, 1, 2),
    _CfprVnicVhbaBehPolicyDn_Type()
)
cfprVnicVhbaBehPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVhbaBehPolicyDn.setStatus("current")
_CfprVnicVhbaBehPolicyRn_Type = SnmpAdminString
_CfprVnicVhbaBehPolicyRn_Object = MibTableColumn
cfprVnicVhbaBehPolicyRn = _CfprVnicVhbaBehPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 67, 1, 3),
    _CfprVnicVhbaBehPolicyRn_Type()
)
cfprVnicVhbaBehPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVhbaBehPolicyRn.setStatus("current")
_CfprVnicVhbaBehPolicyAction_Type = CfprVnicDefaultAction
_CfprVnicVhbaBehPolicyAction_Object = MibTableColumn
cfprVnicVhbaBehPolicyAction = _CfprVnicVhbaBehPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 67, 1, 4),
    _CfprVnicVhbaBehPolicyAction_Type()
)
cfprVnicVhbaBehPolicyAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVhbaBehPolicyAction.setStatus("current")
_CfprVnicVhbaBehPolicyDescr_Type = SnmpAdminString
_CfprVnicVhbaBehPolicyDescr_Object = MibTableColumn
cfprVnicVhbaBehPolicyDescr = _CfprVnicVhbaBehPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 67, 1, 5),
    _CfprVnicVhbaBehPolicyDescr_Type()
)
cfprVnicVhbaBehPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVhbaBehPolicyDescr.setStatus("current")
_CfprVnicVhbaBehPolicyIntId_Type = SnmpAdminString
_CfprVnicVhbaBehPolicyIntId_Object = MibTableColumn
cfprVnicVhbaBehPolicyIntId = _CfprVnicVhbaBehPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 67, 1, 6),
    _CfprVnicVhbaBehPolicyIntId_Type()
)
cfprVnicVhbaBehPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVhbaBehPolicyIntId.setStatus("current")
_CfprVnicVhbaBehPolicyName_Type = SnmpAdminString
_CfprVnicVhbaBehPolicyName_Object = MibTableColumn
cfprVnicVhbaBehPolicyName = _CfprVnicVhbaBehPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 67, 1, 7),
    _CfprVnicVhbaBehPolicyName_Type()
)
cfprVnicVhbaBehPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVhbaBehPolicyName.setStatus("current")
_CfprVnicVhbaBehPolicyNwTemplName_Type = SnmpAdminString
_CfprVnicVhbaBehPolicyNwTemplName_Object = MibTableColumn
cfprVnicVhbaBehPolicyNwTemplName = _CfprVnicVhbaBehPolicyNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 67, 1, 8),
    _CfprVnicVhbaBehPolicyNwTemplName_Type()
)
cfprVnicVhbaBehPolicyNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVhbaBehPolicyNwTemplName.setStatus("current")
_CfprVnicVhbaBehPolicyPolicyLevel_Type = Gauge32
_CfprVnicVhbaBehPolicyPolicyLevel_Object = MibTableColumn
cfprVnicVhbaBehPolicyPolicyLevel = _CfprVnicVhbaBehPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 67, 1, 9),
    _CfprVnicVhbaBehPolicyPolicyLevel_Type()
)
cfprVnicVhbaBehPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVhbaBehPolicyPolicyLevel.setStatus("current")
_CfprVnicVhbaBehPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprVnicVhbaBehPolicyPolicyOwner_Object = MibTableColumn
cfprVnicVhbaBehPolicyPolicyOwner = _CfprVnicVhbaBehPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 67, 1, 10),
    _CfprVnicVhbaBehPolicyPolicyOwner_Type()
)
cfprVnicVhbaBehPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVhbaBehPolicyPolicyOwner.setStatus("current")
_CfprVnicVhbaBehPolicyType_Type = CfprVnicVhbaBehPolicyType
_CfprVnicVhbaBehPolicyType_Object = MibTableColumn
cfprVnicVhbaBehPolicyType = _CfprVnicVhbaBehPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 67, 1, 11),
    _CfprVnicVhbaBehPolicyType_Type()
)
cfprVnicVhbaBehPolicyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVhbaBehPolicyType.setStatus("current")
_CfprVnicVlanTable_Object = MibTable
cfprVnicVlanTable = _CfprVnicVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 68)
)
if mibBuilder.loadTexts:
    cfprVnicVlanTable.setStatus("current")
_CfprVnicVlanEntry_Object = MibTableRow
cfprVnicVlanEntry = _CfprVnicVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 68, 1)
)
cfprVnicVlanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicVlanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicVlanEntry.setStatus("current")
_CfprVnicVlanInstanceId_Type = CfprManagedObjectId
_CfprVnicVlanInstanceId_Object = MibTableColumn
cfprVnicVlanInstanceId = _CfprVnicVlanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 68, 1, 1),
    _CfprVnicVlanInstanceId_Type()
)
cfprVnicVlanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicVlanInstanceId.setStatus("current")
_CfprVnicVlanDn_Type = CfprManagedObjectDn
_CfprVnicVlanDn_Object = MibTableColumn
cfprVnicVlanDn = _CfprVnicVlanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 68, 1, 2),
    _CfprVnicVlanDn_Type()
)
cfprVnicVlanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVlanDn.setStatus("current")
_CfprVnicVlanRn_Type = SnmpAdminString
_CfprVnicVlanRn_Object = MibTableColumn
cfprVnicVlanRn = _CfprVnicVlanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 68, 1, 3),
    _CfprVnicVlanRn_Type()
)
cfprVnicVlanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVlanRn.setStatus("current")
_CfprVnicVlanConfigQualifier_Type = CfprVnicConfigIssues
_CfprVnicVlanConfigQualifier_Object = MibTableColumn
cfprVnicVlanConfigQualifier = _CfprVnicVlanConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 68, 1, 4),
    _CfprVnicVlanConfigQualifier_Type()
)
cfprVnicVlanConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVlanConfigQualifier.setStatus("current")
_CfprVnicVlanFltAggr_Type = Unsigned64
_CfprVnicVlanFltAggr_Object = MibTableColumn
cfprVnicVlanFltAggr = _CfprVnicVlanFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 68, 1, 5),
    _CfprVnicVlanFltAggr_Type()
)
cfprVnicVlanFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVlanFltAggr.setStatus("current")
_CfprVnicVlanName_Type = SnmpAdminString
_CfprVnicVlanName_Object = MibTableColumn
cfprVnicVlanName = _CfprVnicVlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 68, 1, 6),
    _CfprVnicVlanName_Type()
)
cfprVnicVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVlanName.setStatus("current")
_CfprVnicVlanOperState_Type = CfprVnicIfOperState
_CfprVnicVlanOperState_Object = MibTableColumn
cfprVnicVlanOperState = _CfprVnicVlanOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 68, 1, 7),
    _CfprVnicVlanOperState_Type()
)
cfprVnicVlanOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVlanOperState.setStatus("current")
_CfprVnicVlanOperVnetDn_Type = SnmpAdminString
_CfprVnicVlanOperVnetDn_Object = MibTableColumn
cfprVnicVlanOperVnetDn = _CfprVnicVlanOperVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 68, 1, 8),
    _CfprVnicVlanOperVnetDn_Type()
)
cfprVnicVlanOperVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVlanOperVnetDn.setStatus("current")
_CfprVnicVlanOperVnetName_Type = SnmpAdminString
_CfprVnicVlanOperVnetName_Object = MibTableColumn
cfprVnicVlanOperVnetName = _CfprVnicVlanOperVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 68, 1, 9),
    _CfprVnicVlanOperVnetName_Type()
)
cfprVnicVlanOperVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVlanOperVnetName.setStatus("current")
_CfprVnicVlanOwner_Type = CfprVnicConnectionOwner
_CfprVnicVlanOwner_Object = MibTableColumn
cfprVnicVlanOwner = _CfprVnicVlanOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 68, 1, 10),
    _CfprVnicVlanOwner_Type()
)
cfprVnicVlanOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVlanOwner.setStatus("current")
_CfprVnicVlanPubNwId_Type = Gauge32
_CfprVnicVlanPubNwId_Object = MibTableColumn
cfprVnicVlanPubNwId = _CfprVnicVlanPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 68, 1, 11),
    _CfprVnicVlanPubNwId_Type()
)
cfprVnicVlanPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVlanPubNwId.setStatus("current")
_CfprVnicVlanSharing_Type = CfprFabricVlanSharingType
_CfprVnicVlanSharing_Object = MibTableColumn
cfprVnicVlanSharing = _CfprVnicVlanSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 68, 1, 12),
    _CfprVnicVlanSharing_Type()
)
cfprVnicVlanSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVlanSharing.setStatus("current")
_CfprVnicVlanSwitchId_Type = CfprNetworkSwitchId
_CfprVnicVlanSwitchId_Object = MibTableColumn
cfprVnicVlanSwitchId = _CfprVnicVlanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 68, 1, 13),
    _CfprVnicVlanSwitchId_Type()
)
cfprVnicVlanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVlanSwitchId.setStatus("current")
_CfprVnicVlanType_Type = CfprVnicConnectionType
_CfprVnicVlanType_Object = MibTableColumn
cfprVnicVlanType = _CfprVnicVlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 68, 1, 14),
    _CfprVnicVlanType_Type()
)
cfprVnicVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVlanType.setStatus("current")
_CfprVnicVlanVlanName_Type = SnmpAdminString
_CfprVnicVlanVlanName_Object = MibTableColumn
cfprVnicVlanVlanName = _CfprVnicVlanVlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 68, 1, 15),
    _CfprVnicVlanVlanName_Type()
)
cfprVnicVlanVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVlanVlanName.setStatus("current")
_CfprVnicVlanVnet_Type = Gauge32
_CfprVnicVlanVnet_Object = MibTableColumn
cfprVnicVlanVnet = _CfprVnicVlanVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 68, 1, 16),
    _CfprVnicVlanVnet_Type()
)
cfprVnicVlanVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVlanVnet.setStatus("current")
_CfprVnicVmqConPolicyTable_Object = MibTable
cfprVnicVmqConPolicyTable = _CfprVnicVmqConPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 69)
)
if mibBuilder.loadTexts:
    cfprVnicVmqConPolicyTable.setStatus("current")
_CfprVnicVmqConPolicyEntry_Object = MibTableRow
cfprVnicVmqConPolicyEntry = _CfprVnicVmqConPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 69, 1)
)
cfprVnicVmqConPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicVmqConPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicVmqConPolicyEntry.setStatus("current")
_CfprVnicVmqConPolicyInstanceId_Type = CfprManagedObjectId
_CfprVnicVmqConPolicyInstanceId_Object = MibTableColumn
cfprVnicVmqConPolicyInstanceId = _CfprVnicVmqConPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 69, 1, 1),
    _CfprVnicVmqConPolicyInstanceId_Type()
)
cfprVnicVmqConPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicVmqConPolicyInstanceId.setStatus("current")
_CfprVnicVmqConPolicyDn_Type = CfprManagedObjectDn
_CfprVnicVmqConPolicyDn_Object = MibTableColumn
cfprVnicVmqConPolicyDn = _CfprVnicVmqConPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 69, 1, 2),
    _CfprVnicVmqConPolicyDn_Type()
)
cfprVnicVmqConPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVmqConPolicyDn.setStatus("current")
_CfprVnicVmqConPolicyRn_Type = SnmpAdminString
_CfprVnicVmqConPolicyRn_Object = MibTableColumn
cfprVnicVmqConPolicyRn = _CfprVnicVmqConPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 69, 1, 3),
    _CfprVnicVmqConPolicyRn_Type()
)
cfprVnicVmqConPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVmqConPolicyRn.setStatus("current")
_CfprVnicVmqConPolicyDescr_Type = SnmpAdminString
_CfprVnicVmqConPolicyDescr_Object = MibTableColumn
cfprVnicVmqConPolicyDescr = _CfprVnicVmqConPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 69, 1, 4),
    _CfprVnicVmqConPolicyDescr_Type()
)
cfprVnicVmqConPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVmqConPolicyDescr.setStatus("current")
_CfprVnicVmqConPolicyIntId_Type = SnmpAdminString
_CfprVnicVmqConPolicyIntId_Object = MibTableColumn
cfprVnicVmqConPolicyIntId = _CfprVnicVmqConPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 69, 1, 5),
    _CfprVnicVmqConPolicyIntId_Type()
)
cfprVnicVmqConPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVmqConPolicyIntId.setStatus("current")
_CfprVnicVmqConPolicyIntrCount_Type = Gauge32
_CfprVnicVmqConPolicyIntrCount_Object = MibTableColumn
cfprVnicVmqConPolicyIntrCount = _CfprVnicVmqConPolicyIntrCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 69, 1, 6),
    _CfprVnicVmqConPolicyIntrCount_Type()
)
cfprVnicVmqConPolicyIntrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVmqConPolicyIntrCount.setStatus("current")
_CfprVnicVmqConPolicyName_Type = SnmpAdminString
_CfprVnicVmqConPolicyName_Object = MibTableColumn
cfprVnicVmqConPolicyName = _CfprVnicVmqConPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 69, 1, 7),
    _CfprVnicVmqConPolicyName_Type()
)
cfprVnicVmqConPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVmqConPolicyName.setStatus("current")
_CfprVnicVmqConPolicyPolicyLevel_Type = Gauge32
_CfprVnicVmqConPolicyPolicyLevel_Object = MibTableColumn
cfprVnicVmqConPolicyPolicyLevel = _CfprVnicVmqConPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 69, 1, 8),
    _CfprVnicVmqConPolicyPolicyLevel_Type()
)
cfprVnicVmqConPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVmqConPolicyPolicyLevel.setStatus("current")
_CfprVnicVmqConPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprVnicVmqConPolicyPolicyOwner_Object = MibTableColumn
cfprVnicVmqConPolicyPolicyOwner = _CfprVnicVmqConPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 69, 1, 9),
    _CfprVnicVmqConPolicyPolicyOwner_Type()
)
cfprVnicVmqConPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVmqConPolicyPolicyOwner.setStatus("current")
_CfprVnicVmqConPolicyVmqCount_Type = Gauge32
_CfprVnicVmqConPolicyVmqCount_Object = MibTableColumn
cfprVnicVmqConPolicyVmqCount = _CfprVnicVmqConPolicyVmqCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 69, 1, 10),
    _CfprVnicVmqConPolicyVmqCount_Type()
)
cfprVnicVmqConPolicyVmqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVmqConPolicyVmqCount.setStatus("current")
_CfprVnicVmqConPolicyRefTable_Object = MibTable
cfprVnicVmqConPolicyRefTable = _CfprVnicVmqConPolicyRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 70)
)
if mibBuilder.loadTexts:
    cfprVnicVmqConPolicyRefTable.setStatus("current")
_CfprVnicVmqConPolicyRefEntry_Object = MibTableRow
cfprVnicVmqConPolicyRefEntry = _CfprVnicVmqConPolicyRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 70, 1)
)
cfprVnicVmqConPolicyRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicVmqConPolicyRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicVmqConPolicyRefEntry.setStatus("current")
_CfprVnicVmqConPolicyRefInstanceId_Type = CfprManagedObjectId
_CfprVnicVmqConPolicyRefInstanceId_Object = MibTableColumn
cfprVnicVmqConPolicyRefInstanceId = _CfprVnicVmqConPolicyRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 70, 1, 1),
    _CfprVnicVmqConPolicyRefInstanceId_Type()
)
cfprVnicVmqConPolicyRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicVmqConPolicyRefInstanceId.setStatus("current")
_CfprVnicVmqConPolicyRefDn_Type = CfprManagedObjectDn
_CfprVnicVmqConPolicyRefDn_Object = MibTableColumn
cfprVnicVmqConPolicyRefDn = _CfprVnicVmqConPolicyRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 70, 1, 2),
    _CfprVnicVmqConPolicyRefDn_Type()
)
cfprVnicVmqConPolicyRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVmqConPolicyRefDn.setStatus("current")
_CfprVnicVmqConPolicyRefRn_Type = SnmpAdminString
_CfprVnicVmqConPolicyRefRn_Object = MibTableColumn
cfprVnicVmqConPolicyRefRn = _CfprVnicVmqConPolicyRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 70, 1, 3),
    _CfprVnicVmqConPolicyRefRn_Type()
)
cfprVnicVmqConPolicyRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVmqConPolicyRefRn.setStatus("current")
_CfprVnicVmqConPolicyRefConPolicyName_Type = SnmpAdminString
_CfprVnicVmqConPolicyRefConPolicyName_Object = MibTableColumn
cfprVnicVmqConPolicyRefConPolicyName = _CfprVnicVmqConPolicyRefConPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 70, 1, 4),
    _CfprVnicVmqConPolicyRefConPolicyName_Type()
)
cfprVnicVmqConPolicyRefConPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVmqConPolicyRefConPolicyName.setStatus("current")
_CfprVnicVmqConPolicyRefOperConPolicyName_Type = SnmpAdminString
_CfprVnicVmqConPolicyRefOperConPolicyName_Object = MibTableColumn
cfprVnicVmqConPolicyRefOperConPolicyName = _CfprVnicVmqConPolicyRefOperConPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 70, 1, 5),
    _CfprVnicVmqConPolicyRefOperConPolicyName_Type()
)
cfprVnicVmqConPolicyRefOperConPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVmqConPolicyRefOperConPolicyName.setStatus("current")
_CfprVnicVnicBehPolicyTable_Object = MibTable
cfprVnicVnicBehPolicyTable = _CfprVnicVnicBehPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 71)
)
if mibBuilder.loadTexts:
    cfprVnicVnicBehPolicyTable.setStatus("current")
_CfprVnicVnicBehPolicyEntry_Object = MibTableRow
cfprVnicVnicBehPolicyEntry = _CfprVnicVnicBehPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 71, 1)
)
cfprVnicVnicBehPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicVnicBehPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicVnicBehPolicyEntry.setStatus("current")
_CfprVnicVnicBehPolicyInstanceId_Type = CfprManagedObjectId
_CfprVnicVnicBehPolicyInstanceId_Object = MibTableColumn
cfprVnicVnicBehPolicyInstanceId = _CfprVnicVnicBehPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 71, 1, 1),
    _CfprVnicVnicBehPolicyInstanceId_Type()
)
cfprVnicVnicBehPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicVnicBehPolicyInstanceId.setStatus("current")
_CfprVnicVnicBehPolicyDn_Type = CfprManagedObjectDn
_CfprVnicVnicBehPolicyDn_Object = MibTableColumn
cfprVnicVnicBehPolicyDn = _CfprVnicVnicBehPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 71, 1, 2),
    _CfprVnicVnicBehPolicyDn_Type()
)
cfprVnicVnicBehPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVnicBehPolicyDn.setStatus("current")
_CfprVnicVnicBehPolicyRn_Type = SnmpAdminString
_CfprVnicVnicBehPolicyRn_Object = MibTableColumn
cfprVnicVnicBehPolicyRn = _CfprVnicVnicBehPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 71, 1, 3),
    _CfprVnicVnicBehPolicyRn_Type()
)
cfprVnicVnicBehPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVnicBehPolicyRn.setStatus("current")
_CfprVnicVnicBehPolicyAction_Type = CfprVnicDefaultAction
_CfprVnicVnicBehPolicyAction_Object = MibTableColumn
cfprVnicVnicBehPolicyAction = _CfprVnicVnicBehPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 71, 1, 4),
    _CfprVnicVnicBehPolicyAction_Type()
)
cfprVnicVnicBehPolicyAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVnicBehPolicyAction.setStatus("current")
_CfprVnicVnicBehPolicyDescr_Type = SnmpAdminString
_CfprVnicVnicBehPolicyDescr_Object = MibTableColumn
cfprVnicVnicBehPolicyDescr = _CfprVnicVnicBehPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 71, 1, 5),
    _CfprVnicVnicBehPolicyDescr_Type()
)
cfprVnicVnicBehPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVnicBehPolicyDescr.setStatus("current")
_CfprVnicVnicBehPolicyIntId_Type = SnmpAdminString
_CfprVnicVnicBehPolicyIntId_Object = MibTableColumn
cfprVnicVnicBehPolicyIntId = _CfprVnicVnicBehPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 71, 1, 6),
    _CfprVnicVnicBehPolicyIntId_Type()
)
cfprVnicVnicBehPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVnicBehPolicyIntId.setStatus("current")
_CfprVnicVnicBehPolicyName_Type = SnmpAdminString
_CfprVnicVnicBehPolicyName_Object = MibTableColumn
cfprVnicVnicBehPolicyName = _CfprVnicVnicBehPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 71, 1, 7),
    _CfprVnicVnicBehPolicyName_Type()
)
cfprVnicVnicBehPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVnicBehPolicyName.setStatus("current")
_CfprVnicVnicBehPolicyNwTemplName_Type = SnmpAdminString
_CfprVnicVnicBehPolicyNwTemplName_Object = MibTableColumn
cfprVnicVnicBehPolicyNwTemplName = _CfprVnicVnicBehPolicyNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 71, 1, 8),
    _CfprVnicVnicBehPolicyNwTemplName_Type()
)
cfprVnicVnicBehPolicyNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVnicBehPolicyNwTemplName.setStatus("current")
_CfprVnicVnicBehPolicyPolicyLevel_Type = Gauge32
_CfprVnicVnicBehPolicyPolicyLevel_Object = MibTableColumn
cfprVnicVnicBehPolicyPolicyLevel = _CfprVnicVnicBehPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 71, 1, 9),
    _CfprVnicVnicBehPolicyPolicyLevel_Type()
)
cfprVnicVnicBehPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVnicBehPolicyPolicyLevel.setStatus("current")
_CfprVnicVnicBehPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprVnicVnicBehPolicyPolicyOwner_Object = MibTableColumn
cfprVnicVnicBehPolicyPolicyOwner = _CfprVnicVnicBehPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 71, 1, 10),
    _CfprVnicVnicBehPolicyPolicyOwner_Type()
)
cfprVnicVnicBehPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVnicBehPolicyPolicyOwner.setStatus("current")
_CfprVnicVnicBehPolicyType_Type = CfprVnicVnicBehPolicyType
_CfprVnicVnicBehPolicyType_Object = MibTableColumn
cfprVnicVnicBehPolicyType = _CfprVnicVnicBehPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 71, 1, 11),
    _CfprVnicVnicBehPolicyType_Type()
)
cfprVnicVnicBehPolicyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicVnicBehPolicyType.setStatus("current")
_CfprVnicWwnnHistoryTable_Object = MibTable
cfprVnicWwnnHistoryTable = _CfprVnicWwnnHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 72)
)
if mibBuilder.loadTexts:
    cfprVnicWwnnHistoryTable.setStatus("current")
_CfprVnicWwnnHistoryEntry_Object = MibTableRow
cfprVnicWwnnHistoryEntry = _CfprVnicWwnnHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 72, 1)
)
cfprVnicWwnnHistoryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicWwnnHistoryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicWwnnHistoryEntry.setStatus("current")
_CfprVnicWwnnHistoryInstanceId_Type = CfprManagedObjectId
_CfprVnicWwnnHistoryInstanceId_Object = MibTableColumn
cfprVnicWwnnHistoryInstanceId = _CfprVnicWwnnHistoryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 72, 1, 1),
    _CfprVnicWwnnHistoryInstanceId_Type()
)
cfprVnicWwnnHistoryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicWwnnHistoryInstanceId.setStatus("current")
_CfprVnicWwnnHistoryDn_Type = CfprManagedObjectDn
_CfprVnicWwnnHistoryDn_Object = MibTableColumn
cfprVnicWwnnHistoryDn = _CfprVnicWwnnHistoryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 72, 1, 2),
    _CfprVnicWwnnHistoryDn_Type()
)
cfprVnicWwnnHistoryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicWwnnHistoryDn.setStatus("current")
_CfprVnicWwnnHistoryRn_Type = SnmpAdminString
_CfprVnicWwnnHistoryRn_Object = MibTableColumn
cfprVnicWwnnHistoryRn = _CfprVnicWwnnHistoryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 72, 1, 3),
    _CfprVnicWwnnHistoryRn_Type()
)
cfprVnicWwnnHistoryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicWwnnHistoryRn.setStatus("current")
_CfprVnicWwnnHistoryOldwwnn_Type = Unsigned64
_CfprVnicWwnnHistoryOldwwnn_Object = MibTableColumn
cfprVnicWwnnHistoryOldwwnn = _CfprVnicWwnnHistoryOldwwnn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 72, 1, 4),
    _CfprVnicWwnnHistoryOldwwnn_Type()
)
cfprVnicWwnnHistoryOldwwnn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicWwnnHistoryOldwwnn.setStatus("current")
_CfprVnicWwpnHistoryTable_Object = MibTable
cfprVnicWwpnHistoryTable = _CfprVnicWwpnHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 73)
)
if mibBuilder.loadTexts:
    cfprVnicWwpnHistoryTable.setStatus("current")
_CfprVnicWwpnHistoryEntry_Object = MibTableRow
cfprVnicWwpnHistoryEntry = _CfprVnicWwpnHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 73, 1)
)
cfprVnicWwpnHistoryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-VNIC-MIB", "cfprVnicWwpnHistoryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprVnicWwpnHistoryEntry.setStatus("current")
_CfprVnicWwpnHistoryInstanceId_Type = CfprManagedObjectId
_CfprVnicWwpnHistoryInstanceId_Object = MibTableColumn
cfprVnicWwpnHistoryInstanceId = _CfprVnicWwpnHistoryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 73, 1, 1),
    _CfprVnicWwpnHistoryInstanceId_Type()
)
cfprVnicWwpnHistoryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprVnicWwpnHistoryInstanceId.setStatus("current")
_CfprVnicWwpnHistoryDn_Type = CfprManagedObjectDn
_CfprVnicWwpnHistoryDn_Object = MibTableColumn
cfprVnicWwpnHistoryDn = _CfprVnicWwpnHistoryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 73, 1, 2),
    _CfprVnicWwpnHistoryDn_Type()
)
cfprVnicWwpnHistoryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicWwpnHistoryDn.setStatus("current")
_CfprVnicWwpnHistoryRn_Type = SnmpAdminString
_CfprVnicWwpnHistoryRn_Object = MibTableColumn
cfprVnicWwpnHistoryRn = _CfprVnicWwpnHistoryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 73, 1, 3),
    _CfprVnicWwpnHistoryRn_Type()
)
cfprVnicWwpnHistoryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicWwpnHistoryRn.setStatus("current")
_CfprVnicWwpnHistoryOldaddr_Type = Unsigned64
_CfprVnicWwpnHistoryOldaddr_Object = MibTableColumn
cfprVnicWwpnHistoryOldaddr = _CfprVnicWwpnHistoryOldaddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 83, 73, 1, 4),
    _CfprVnicWwpnHistoryOldaddr_Type()
)
cfprVnicWwpnHistoryOldaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprVnicWwpnHistoryOldaddr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-VNIC-MIB",
    **{"cfprVnicObjects": cfprVnicObjects,
       "cfprVnicBootIpPolicyTable": cfprVnicBootIpPolicyTable,
       "cfprVnicBootIpPolicyEntry": cfprVnicBootIpPolicyEntry,
       "cfprVnicBootIpPolicyInstanceId": cfprVnicBootIpPolicyInstanceId,
       "cfprVnicBootIpPolicyDn": cfprVnicBootIpPolicyDn,
       "cfprVnicBootIpPolicyRn": cfprVnicBootIpPolicyRn,
       "cfprVnicBootIpPolicyDescr": cfprVnicBootIpPolicyDescr,
       "cfprVnicBootIpPolicyIntId": cfprVnicBootIpPolicyIntId,
       "cfprVnicBootIpPolicyName": cfprVnicBootIpPolicyName,
       "cfprVnicBootIpPolicyPolicyLevel": cfprVnicBootIpPolicyPolicyLevel,
       "cfprVnicBootIpPolicyPolicyOwner": cfprVnicBootIpPolicyPolicyOwner,
       "cfprVnicBootIpPolicyPoolName": cfprVnicBootIpPolicyPoolName,
       "cfprVnicBootTargetTable": cfprVnicBootTargetTable,
       "cfprVnicBootTargetEntry": cfprVnicBootTargetEntry,
       "cfprVnicBootTargetInstanceId": cfprVnicBootTargetInstanceId,
       "cfprVnicBootTargetDn": cfprVnicBootTargetDn,
       "cfprVnicBootTargetRn": cfprVnicBootTargetRn,
       "cfprVnicBootTargetLun": cfprVnicBootTargetLun,
       "cfprVnicBootTargetWwn": cfprVnicBootTargetWwn,
       "cfprVnicConnDefTable": cfprVnicConnDefTable,
       "cfprVnicConnDefEntry": cfprVnicConnDefEntry,
       "cfprVnicConnDefInstanceId": cfprVnicConnDefInstanceId,
       "cfprVnicConnDefDn": cfprVnicConnDefDn,
       "cfprVnicConnDefRn": cfprVnicConnDefRn,
       "cfprVnicConnDefFltAggr": cfprVnicConnDefFltAggr,
       "cfprVnicConnDefLanConnPolicyName": cfprVnicConnDefLanConnPolicyName,
       "cfprVnicConnDefOperLanConnPolicyName": cfprVnicConnDefOperLanConnPolicyName,
       "cfprVnicConnDefOperSanConnPolicyName": cfprVnicConnDefOperSanConnPolicyName,
       "cfprVnicConnDefSanConnPolicyName": cfprVnicConnDefSanConnPolicyName,
       "cfprVnicDefBehTable": cfprVnicDefBehTable,
       "cfprVnicDefBehEntry": cfprVnicDefBehEntry,
       "cfprVnicDefBehInstanceId": cfprVnicDefBehInstanceId,
       "cfprVnicDefBehDn": cfprVnicDefBehDn,
       "cfprVnicDefBehRn": cfprVnicDefBehRn,
       "cfprVnicDefBehAction": cfprVnicDefBehAction,
       "cfprVnicDefBehDescr": cfprVnicDefBehDescr,
       "cfprVnicDefBehIntId": cfprVnicDefBehIntId,
       "cfprVnicDefBehName": cfprVnicDefBehName,
       "cfprVnicDefBehNwTemplName": cfprVnicDefBehNwTemplName,
       "cfprVnicDefBehPolicyLevel": cfprVnicDefBehPolicyLevel,
       "cfprVnicDefBehPolicyOwner": cfprVnicDefBehPolicyOwner,
       "cfprVnicDefBehType": cfprVnicDefBehType,
       "cfprVnicDynamicConTable": cfprVnicDynamicConTable,
       "cfprVnicDynamicConEntry": cfprVnicDynamicConEntry,
       "cfprVnicDynamicConInstanceId": cfprVnicDynamicConInstanceId,
       "cfprVnicDynamicConDn": cfprVnicDynamicConDn,
       "cfprVnicDynamicConRn": cfprVnicDynamicConRn,
       "cfprVnicDynamicConAdaptorProfileName": cfprVnicDynamicConAdaptorProfileName,
       "cfprVnicDynamicConDescr": cfprVnicDynamicConDescr,
       "cfprVnicDynamicConDynamicEth": cfprVnicDynamicConDynamicEth,
       "cfprVnicDynamicConIntId": cfprVnicDynamicConIntId,
       "cfprVnicDynamicConMtu": cfprVnicDynamicConMtu,
       "cfprVnicDynamicConName": cfprVnicDynamicConName,
       "cfprVnicDynamicConNamingPrefix": cfprVnicDynamicConNamingPrefix,
       "cfprVnicDynamicConPolicyLevel": cfprVnicDynamicConPolicyLevel,
       "cfprVnicDynamicConPolicyOwner": cfprVnicDynamicConPolicyOwner,
       "cfprVnicDynamicConProtection": cfprVnicDynamicConProtection,
       "cfprVnicDynamicConPolicyTable": cfprVnicDynamicConPolicyTable,
       "cfprVnicDynamicConPolicyEntry": cfprVnicDynamicConPolicyEntry,
       "cfprVnicDynamicConPolicyInstanceId": cfprVnicDynamicConPolicyInstanceId,
       "cfprVnicDynamicConPolicyDn": cfprVnicDynamicConPolicyDn,
       "cfprVnicDynamicConPolicyRn": cfprVnicDynamicConPolicyRn,
       "cfprVnicDynamicConPolicyAdaptorProfileName": cfprVnicDynamicConPolicyAdaptorProfileName,
       "cfprVnicDynamicConPolicyDescr": cfprVnicDynamicConPolicyDescr,
       "cfprVnicDynamicConPolicyDynamicEth": cfprVnicDynamicConPolicyDynamicEth,
       "cfprVnicDynamicConPolicyIntId": cfprVnicDynamicConPolicyIntId,
       "cfprVnicDynamicConPolicyMtu": cfprVnicDynamicConPolicyMtu,
       "cfprVnicDynamicConPolicyName": cfprVnicDynamicConPolicyName,
       "cfprVnicDynamicConPolicyNamingPrefix": cfprVnicDynamicConPolicyNamingPrefix,
       "cfprVnicDynamicConPolicyPolicyLevel": cfprVnicDynamicConPolicyPolicyLevel,
       "cfprVnicDynamicConPolicyPolicyOwner": cfprVnicDynamicConPolicyPolicyOwner,
       "cfprVnicDynamicConPolicyProtection": cfprVnicDynamicConPolicyProtection,
       "cfprVnicDynamicConPolicyRefTable": cfprVnicDynamicConPolicyRefTable,
       "cfprVnicDynamicConPolicyRefEntry": cfprVnicDynamicConPolicyRefEntry,
       "cfprVnicDynamicConPolicyRefInstanceId": cfprVnicDynamicConPolicyRefInstanceId,
       "cfprVnicDynamicConPolicyRefDn": cfprVnicDynamicConPolicyRefDn,
       "cfprVnicDynamicConPolicyRefRn": cfprVnicDynamicConPolicyRefRn,
       "cfprVnicDynamicConPolicyRefConPolicyName": cfprVnicDynamicConPolicyRefConPolicyName,
       "cfprVnicDynamicConPolicyRefOperConPolicyName": cfprVnicDynamicConPolicyRefOperConPolicyName,
       "cfprVnicDynamicIdUniverseTable": cfprVnicDynamicIdUniverseTable,
       "cfprVnicDynamicIdUniverseEntry": cfprVnicDynamicIdUniverseEntry,
       "cfprVnicDynamicIdUniverseInstanceId": cfprVnicDynamicIdUniverseInstanceId,
       "cfprVnicDynamicIdUniverseDn": cfprVnicDynamicIdUniverseDn,
       "cfprVnicDynamicIdUniverseRn": cfprVnicDynamicIdUniverseRn,
       "cfprVnicDynamicIdUniverseDescr": cfprVnicDynamicIdUniverseDescr,
       "cfprVnicDynamicIdUniverseIntId": cfprVnicDynamicIdUniverseIntId,
       "cfprVnicDynamicIdUniverseName": cfprVnicDynamicIdUniverseName,
       "cfprVnicDynamicIdUniversePolicyLevel": cfprVnicDynamicIdUniversePolicyLevel,
       "cfprVnicDynamicIdUniversePolicyOwner": cfprVnicDynamicIdUniversePolicyOwner,
       "cfprVnicDynamicProviderTable": cfprVnicDynamicProviderTable,
       "cfprVnicDynamicProviderEntry": cfprVnicDynamicProviderEntry,
       "cfprVnicDynamicProviderInstanceId": cfprVnicDynamicProviderInstanceId,
       "cfprVnicDynamicProviderDn": cfprVnicDynamicProviderDn,
       "cfprVnicDynamicProviderRn": cfprVnicDynamicProviderRn,
       "cfprVnicDynamicProviderName": cfprVnicDynamicProviderName,
       "cfprVnicDynamicProviderEpTable": cfprVnicDynamicProviderEpTable,
       "cfprVnicDynamicProviderEpEntry": cfprVnicDynamicProviderEpEntry,
       "cfprVnicDynamicProviderEpInstanceId": cfprVnicDynamicProviderEpInstanceId,
       "cfprVnicDynamicProviderEpDn": cfprVnicDynamicProviderEpDn,
       "cfprVnicDynamicProviderEpRn": cfprVnicDynamicProviderEpRn,
       "cfprVnicDynamicProviderEpChassisId": cfprVnicDynamicProviderEpChassisId,
       "cfprVnicDynamicProviderEpPortId": cfprVnicDynamicProviderEpPortId,
       "cfprVnicDynamicProviderEpSlotId": cfprVnicDynamicProviderEpSlotId,
       "cfprVnicDynamicProviderEpSwitchId": cfprVnicDynamicProviderEpSwitchId,
       "cfprVnicEthLifTable": cfprVnicEthLifTable,
       "cfprVnicEthLifEntry": cfprVnicEthLifEntry,
       "cfprVnicEthLifInstanceId": cfprVnicEthLifInstanceId,
       "cfprVnicEthLifDn": cfprVnicEthLifDn,
       "cfprVnicEthLifRn": cfprVnicEthLifRn,
       "cfprVnicEthLifAddr": cfprVnicEthLifAddr,
       "cfprVnicEthLifName": cfprVnicEthLifName,
       "cfprVnicEthLifNicDn": cfprVnicEthLifNicDn,
       "cfprVnicEthLifOwner": cfprVnicEthLifOwner,
       "cfprVnicEthLifSwitchId": cfprVnicEthLifSwitchId,
       "cfprVnicEthLifType": cfprVnicEthLifType,
       "cfprVnicEthLifVnicDn": cfprVnicEthLifVnicDn,
       "cfprVnicEtherTable": cfprVnicEtherTable,
       "cfprVnicEtherEntry": cfprVnicEtherEntry,
       "cfprVnicEtherInstanceId": cfprVnicEtherInstanceId,
       "cfprVnicEtherDn": cfprVnicEtherDn,
       "cfprVnicEtherRn": cfprVnicEtherRn,
       "cfprVnicEtherAdaptorProfileName": cfprVnicEtherAdaptorProfileName,
       "cfprVnicEtherAddr": cfprVnicEtherAddr,
       "cfprVnicEtherAdminHostPort": cfprVnicEtherAdminHostPort,
       "cfprVnicEtherAdminVcon": cfprVnicEtherAdminVcon,
       "cfprVnicEtherAppInstId": cfprVnicEtherAppInstId,
       "cfprVnicEtherAppRole": cfprVnicEtherAppRole,
       "cfprVnicEtherBootDev": cfprVnicEtherBootDev,
       "cfprVnicEtherConfigQualifier": cfprVnicEtherConfigQualifier,
       "cfprVnicEtherConfigState": cfprVnicEtherConfigState,
       "cfprVnicEtherDynamicId": cfprVnicEtherDynamicId,
       "cfprVnicEtherEquipmentDn": cfprVnicEtherEquipmentDn,
       "cfprVnicEtherFltAggr": cfprVnicEtherFltAggr,
       "cfprVnicEtherIdentPoolName": cfprVnicEtherIdentPoolName,
       "cfprVnicEtherInstType": cfprVnicEtherInstType,
       "cfprVnicEtherIsAllocated": cfprVnicEtherIsAllocated,
       "cfprVnicEtherMtu": cfprVnicEtherMtu,
       "cfprVnicEtherName": cfprVnicEtherName,
       "cfprVnicEtherNwCtrlPolicyName": cfprVnicEtherNwCtrlPolicyName,
       "cfprVnicEtherNwTemplName": cfprVnicEtherNwTemplName,
       "cfprVnicEtherOperAdaptorProfileName": cfprVnicEtherOperAdaptorProfileName,
       "cfprVnicEtherOperHostPort": cfprVnicEtherOperHostPort,
       "cfprVnicEtherOperIdentPoolName": cfprVnicEtherOperIdentPoolName,
       "cfprVnicEtherOperNwCtrlPolicyName": cfprVnicEtherOperNwCtrlPolicyName,
       "cfprVnicEtherOperNwTemplName": cfprVnicEtherOperNwTemplName,
       "cfprVnicEtherOperOrder": cfprVnicEtherOperOrder,
       "cfprVnicEtherOperPinToGroupName": cfprVnicEtherOperPinToGroupName,
       "cfprVnicEtherOperQosPolicyName": cfprVnicEtherOperQosPolicyName,
       "cfprVnicEtherOperSpeed": cfprVnicEtherOperSpeed,
       "cfprVnicEtherOperStatsPolicyName": cfprVnicEtherOperStatsPolicyName,
       "cfprVnicEtherOperVcon": cfprVnicEtherOperVcon,
       "cfprVnicEtherOrder": cfprVnicEtherOrder,
       "cfprVnicEtherOwner": cfprVnicEtherOwner,
       "cfprVnicEtherPfDn": cfprVnicEtherPfDn,
       "cfprVnicEtherPinToGroupName": cfprVnicEtherPinToGroupName,
       "cfprVnicEtherQosPolicyName": cfprVnicEtherQosPolicyName,
       "cfprVnicEtherStatsPolicyName": cfprVnicEtherStatsPolicyName,
       "cfprVnicEtherSwitchId": cfprVnicEtherSwitchId,
       "cfprVnicEtherType": cfprVnicEtherType,
       "cfprVnicEtherVirtualizationPreference": cfprVnicEtherVirtualizationPreference,
       "cfprVnicEtherPortType": cfprVnicEtherPortType,
       "cfprVnicEtherIfTable": cfprVnicEtherIfTable,
       "cfprVnicEtherIfEntry": cfprVnicEtherIfEntry,
       "cfprVnicEtherIfInstanceId": cfprVnicEtherIfInstanceId,
       "cfprVnicEtherIfDn": cfprVnicEtherIfDn,
       "cfprVnicEtherIfRn": cfprVnicEtherIfRn,
       "cfprVnicEtherIfAddr": cfprVnicEtherIfAddr,
       "cfprVnicEtherIfConfigQualifier": cfprVnicEtherIfConfigQualifier,
       "cfprVnicEtherIfDefaultNet": cfprVnicEtherIfDefaultNet,
       "cfprVnicEtherIfFltAggr": cfprVnicEtherIfFltAggr,
       "cfprVnicEtherIfName": cfprVnicEtherIfName,
       "cfprVnicEtherIfOperState": cfprVnicEtherIfOperState,
       "cfprVnicEtherIfOperVnetDn": cfprVnicEtherIfOperVnetDn,
       "cfprVnicEtherIfOperVnetName": cfprVnicEtherIfOperVnetName,
       "cfprVnicEtherIfOwner": cfprVnicEtherIfOwner,
       "cfprVnicEtherIfPubNwId": cfprVnicEtherIfPubNwId,
       "cfprVnicEtherIfSharing": cfprVnicEtherIfSharing,
       "cfprVnicEtherIfSwitchId": cfprVnicEtherIfSwitchId,
       "cfprVnicEtherIfType": cfprVnicEtherIfType,
       "cfprVnicEtherIfVnet": cfprVnicEtherIfVnet,
       "cfprVnicFcTable": cfprVnicFcTable,
       "cfprVnicFcEntry": cfprVnicFcEntry,
       "cfprVnicFcInstanceId": cfprVnicFcInstanceId,
       "cfprVnicFcDn": cfprVnicFcDn,
       "cfprVnicFcRn": cfprVnicFcRn,
       "cfprVnicFcAdaptorProfileName": cfprVnicFcAdaptorProfileName,
       "cfprVnicFcAddr": cfprVnicFcAddr,
       "cfprVnicFcAdminHostPort": cfprVnicFcAdminHostPort,
       "cfprVnicFcAdminVcon": cfprVnicFcAdminVcon,
       "cfprVnicFcAppRole": cfprVnicFcAppRole,
       "cfprVnicFcBootDev": cfprVnicFcBootDev,
       "cfprVnicFcConfigQualifier": cfprVnicFcConfigQualifier,
       "cfprVnicFcConfigState": cfprVnicFcConfigState,
       "cfprVnicFcEquipmentDn": cfprVnicFcEquipmentDn,
       "cfprVnicFcFltAggr": cfprVnicFcFltAggr,
       "cfprVnicFcIdentPoolName": cfprVnicFcIdentPoolName,
       "cfprVnicFcInstType": cfprVnicFcInstType,
       "cfprVnicFcMaxDataFieldSize": cfprVnicFcMaxDataFieldSize,
       "cfprVnicFcName": cfprVnicFcName,
       "cfprVnicFcNodeAddr": cfprVnicFcNodeAddr,
       "cfprVnicFcNwTemplName": cfprVnicFcNwTemplName,
       "cfprVnicFcOperAdaptorProfileName": cfprVnicFcOperAdaptorProfileName,
       "cfprVnicFcOperHostPort": cfprVnicFcOperHostPort,
       "cfprVnicFcOperIdentPoolName": cfprVnicFcOperIdentPoolName,
       "cfprVnicFcOperNwTemplName": cfprVnicFcOperNwTemplName,
       "cfprVnicFcOperOrder": cfprVnicFcOperOrder,
       "cfprVnicFcOperPinToGroupName": cfprVnicFcOperPinToGroupName,
       "cfprVnicFcOperQosPolicyName": cfprVnicFcOperQosPolicyName,
       "cfprVnicFcOperSpeed": cfprVnicFcOperSpeed,
       "cfprVnicFcOperStatsPolicyName": cfprVnicFcOperStatsPolicyName,
       "cfprVnicFcOperVcon": cfprVnicFcOperVcon,
       "cfprVnicFcOrder": cfprVnicFcOrder,
       "cfprVnicFcOwner": cfprVnicFcOwner,
       "cfprVnicFcPersBind": cfprVnicFcPersBind,
       "cfprVnicFcPersBindClear": cfprVnicFcPersBindClear,
       "cfprVnicFcPinToGroupName": cfprVnicFcPinToGroupName,
       "cfprVnicFcQosPolicyName": cfprVnicFcQosPolicyName,
       "cfprVnicFcStatsPolicyName": cfprVnicFcStatsPolicyName,
       "cfprVnicFcSwitchId": cfprVnicFcSwitchId,
       "cfprVnicFcType": cfprVnicFcType,
       "cfprVnicFcGroupDefTable": cfprVnicFcGroupDefTable,
       "cfprVnicFcGroupDefEntry": cfprVnicFcGroupDefEntry,
       "cfprVnicFcGroupDefInstanceId": cfprVnicFcGroupDefInstanceId,
       "cfprVnicFcGroupDefDn": cfprVnicFcGroupDefDn,
       "cfprVnicFcGroupDefRn": cfprVnicFcGroupDefRn,
       "cfprVnicFcGroupDefAdaptorProfileName": cfprVnicFcGroupDefAdaptorProfileName,
       "cfprVnicFcGroupDefDescr": cfprVnicFcGroupDefDescr,
       "cfprVnicFcGroupDefIdentPoolName": cfprVnicFcGroupDefIdentPoolName,
       "cfprVnicFcGroupDefIntId": cfprVnicFcGroupDefIntId,
       "cfprVnicFcGroupDefMaxDataFieldSize": cfprVnicFcGroupDefMaxDataFieldSize,
       "cfprVnicFcGroupDefName": cfprVnicFcGroupDefName,
       "cfprVnicFcGroupDefNwTemplName": cfprVnicFcGroupDefNwTemplName,
       "cfprVnicFcGroupDefOperStatsPolicyName": cfprVnicFcGroupDefOperStatsPolicyName,
       "cfprVnicFcGroupDefOperStorageConnPolicyName": cfprVnicFcGroupDefOperStorageConnPolicyName,
       "cfprVnicFcGroupDefPolicyLevel": cfprVnicFcGroupDefPolicyLevel,
       "cfprVnicFcGroupDefPolicyOwner": cfprVnicFcGroupDefPolicyOwner,
       "cfprVnicFcGroupDefQosPolicyName": cfprVnicFcGroupDefQosPolicyName,
       "cfprVnicFcGroupDefStatsPolicyName": cfprVnicFcGroupDefStatsPolicyName,
       "cfprVnicFcGroupDefStorageConnPolicyName": cfprVnicFcGroupDefStorageConnPolicyName,
       "cfprVnicFcGroupTemplTable": cfprVnicFcGroupTemplTable,
       "cfprVnicFcGroupTemplEntry": cfprVnicFcGroupTemplEntry,
       "cfprVnicFcGroupTemplInstanceId": cfprVnicFcGroupTemplInstanceId,
       "cfprVnicFcGroupTemplDn": cfprVnicFcGroupTemplDn,
       "cfprVnicFcGroupTemplRn": cfprVnicFcGroupTemplRn,
       "cfprVnicFcGroupTemplAdaptorProfileName": cfprVnicFcGroupTemplAdaptorProfileName,
       "cfprVnicFcGroupTemplDescr": cfprVnicFcGroupTemplDescr,
       "cfprVnicFcGroupTemplIdentPoolName": cfprVnicFcGroupTemplIdentPoolName,
       "cfprVnicFcGroupTemplIntId": cfprVnicFcGroupTemplIntId,
       "cfprVnicFcGroupTemplMaxDataFieldSize": cfprVnicFcGroupTemplMaxDataFieldSize,
       "cfprVnicFcGroupTemplName": cfprVnicFcGroupTemplName,
       "cfprVnicFcGroupTemplNwTemplName": cfprVnicFcGroupTemplNwTemplName,
       "cfprVnicFcGroupTemplOperStatsPolicyName": cfprVnicFcGroupTemplOperStatsPolicyName,
       "cfprVnicFcGroupTemplOperStorageConnPolicyName": cfprVnicFcGroupTemplOperStorageConnPolicyName,
       "cfprVnicFcGroupTemplPolicyLevel": cfprVnicFcGroupTemplPolicyLevel,
       "cfprVnicFcGroupTemplPolicyOwner": cfprVnicFcGroupTemplPolicyOwner,
       "cfprVnicFcGroupTemplQosPolicyName": cfprVnicFcGroupTemplQosPolicyName,
       "cfprVnicFcGroupTemplStatsPolicyName": cfprVnicFcGroupTemplStatsPolicyName,
       "cfprVnicFcGroupTemplStorageConnPolicyName": cfprVnicFcGroupTemplStorageConnPolicyName,
       "cfprVnicFcGroupTemplTemplType": cfprVnicFcGroupTemplTemplType,
       "cfprVnicFcIfTable": cfprVnicFcIfTable,
       "cfprVnicFcIfEntry": cfprVnicFcIfEntry,
       "cfprVnicFcIfInstanceId": cfprVnicFcIfInstanceId,
       "cfprVnicFcIfDn": cfprVnicFcIfDn,
       "cfprVnicFcIfRn": cfprVnicFcIfRn,
       "cfprVnicFcIfConfigQualifier": cfprVnicFcIfConfigQualifier,
       "cfprVnicFcIfInitiator": cfprVnicFcIfInitiator,
       "cfprVnicFcIfName": cfprVnicFcIfName,
       "cfprVnicFcIfOperState": cfprVnicFcIfOperState,
       "cfprVnicFcIfOperVnetDn": cfprVnicFcIfOperVnetDn,
       "cfprVnicFcIfOperVnetName": cfprVnicFcIfOperVnetName,
       "cfprVnicFcIfOwner": cfprVnicFcIfOwner,
       "cfprVnicFcIfPubNwId": cfprVnicFcIfPubNwId,
       "cfprVnicFcIfSharing": cfprVnicFcIfSharing,
       "cfprVnicFcIfSwitchId": cfprVnicFcIfSwitchId,
       "cfprVnicFcIfType": cfprVnicFcIfType,
       "cfprVnicFcIfVnet": cfprVnicFcIfVnet,
       "cfprVnicFcLifTable": cfprVnicFcLifTable,
       "cfprVnicFcLifEntry": cfprVnicFcLifEntry,
       "cfprVnicFcLifInstanceId": cfprVnicFcLifInstanceId,
       "cfprVnicFcLifDn": cfprVnicFcLifDn,
       "cfprVnicFcLifRn": cfprVnicFcLifRn,
       "cfprVnicFcLifAddr": cfprVnicFcLifAddr,
       "cfprVnicFcLifName": cfprVnicFcLifName,
       "cfprVnicFcLifNicDn": cfprVnicFcLifNicDn,
       "cfprVnicFcLifOwner": cfprVnicFcLifOwner,
       "cfprVnicFcLifSwitchId": cfprVnicFcLifSwitchId,
       "cfprVnicFcLifType": cfprVnicFcLifType,
       "cfprVnicFcLifVnicDn": cfprVnicFcLifVnicDn,
       "cfprVnicFcNodeTable": cfprVnicFcNodeTable,
       "cfprVnicFcNodeEntry": cfprVnicFcNodeEntry,
       "cfprVnicFcNodeInstanceId": cfprVnicFcNodeInstanceId,
       "cfprVnicFcNodeDn": cfprVnicFcNodeDn,
       "cfprVnicFcNodeRn": cfprVnicFcNodeRn,
       "cfprVnicFcNodeAddrData": cfprVnicFcNodeAddrData,
       "cfprVnicFcNodeFltAggr": cfprVnicFcNodeFltAggr,
       "cfprVnicFcNodeIdentPoolName": cfprVnicFcNodeIdentPoolName,
       "cfprVnicFcNodeMaxDerivableWWPN": cfprVnicFcNodeMaxDerivableWWPN,
       "cfprVnicFcNodeOperIdentPoolName": cfprVnicFcNodeOperIdentPoolName,
       "cfprVnicFcNodeOwner": cfprVnicFcNodeOwner,
       "cfprVnicFcOEIfTable": cfprVnicFcOEIfTable,
       "cfprVnicFcOEIfEntry": cfprVnicFcOEIfEntry,
       "cfprVnicFcOEIfInstanceId": cfprVnicFcOEIfInstanceId,
       "cfprVnicFcOEIfDn": cfprVnicFcOEIfDn,
       "cfprVnicFcOEIfRn": cfprVnicFcOEIfRn,
       "cfprVnicFcOEIfConfigQualifier": cfprVnicFcOEIfConfigQualifier,
       "cfprVnicFcOEIfInitiator": cfprVnicFcOEIfInitiator,
       "cfprVnicFcOEIfName": cfprVnicFcOEIfName,
       "cfprVnicFcOEIfOperState": cfprVnicFcOEIfOperState,
       "cfprVnicFcOEIfOperVnetDn": cfprVnicFcOEIfOperVnetDn,
       "cfprVnicFcOEIfOperVnetName": cfprVnicFcOEIfOperVnetName,
       "cfprVnicFcOEIfOwner": cfprVnicFcOEIfOwner,
       "cfprVnicFcOEIfPubNwId": cfprVnicFcOEIfPubNwId,
       "cfprVnicFcOEIfSharing": cfprVnicFcOEIfSharing,
       "cfprVnicFcOEIfSwitchId": cfprVnicFcOEIfSwitchId,
       "cfprVnicFcOEIfType": cfprVnicFcOEIfType,
       "cfprVnicFcOEIfVnet": cfprVnicFcOEIfVnet,
       "cfprVnicIPv4DhcpTable": cfprVnicIPv4DhcpTable,
       "cfprVnicIPv4DhcpEntry": cfprVnicIPv4DhcpEntry,
       "cfprVnicIPv4DhcpInstanceId": cfprVnicIPv4DhcpInstanceId,
       "cfprVnicIPv4DhcpDn": cfprVnicIPv4DhcpDn,
       "cfprVnicIPv4DhcpRn": cfprVnicIPv4DhcpRn,
       "cfprVnicIPv4DhcpAddr": cfprVnicIPv4DhcpAddr,
       "cfprVnicIPv4DhcpDefGw": cfprVnicIPv4DhcpDefGw,
       "cfprVnicIPv4DhcpSubnet": cfprVnicIPv4DhcpSubnet,
       "cfprVnicIPv4DnsTable": cfprVnicIPv4DnsTable,
       "cfprVnicIPv4DnsEntry": cfprVnicIPv4DnsEntry,
       "cfprVnicIPv4DnsInstanceId": cfprVnicIPv4DnsInstanceId,
       "cfprVnicIPv4DnsDn": cfprVnicIPv4DnsDn,
       "cfprVnicIPv4DnsRn": cfprVnicIPv4DnsRn,
       "cfprVnicIPv4DnsAddr": cfprVnicIPv4DnsAddr,
       "cfprVnicIPv4DnsDefGw": cfprVnicIPv4DnsDefGw,
       "cfprVnicIPv4DnsPref": cfprVnicIPv4DnsPref,
       "cfprVnicIPv4DnsSubnet": cfprVnicIPv4DnsSubnet,
       "cfprVnicIPv4IfTable": cfprVnicIPv4IfTable,
       "cfprVnicIPv4IfEntry": cfprVnicIPv4IfEntry,
       "cfprVnicIPv4IfInstanceId": cfprVnicIPv4IfInstanceId,
       "cfprVnicIPv4IfDn": cfprVnicIPv4IfDn,
       "cfprVnicIPv4IfRn": cfprVnicIPv4IfRn,
       "cfprVnicIPv4IfAddr": cfprVnicIPv4IfAddr,
       "cfprVnicIPv4IfConfigQualifier": cfprVnicIPv4IfConfigQualifier,
       "cfprVnicIPv4IfName": cfprVnicIPv4IfName,
       "cfprVnicIPv4IfOperState": cfprVnicIPv4IfOperState,
       "cfprVnicIPv4IfOperVnetDn": cfprVnicIPv4IfOperVnetDn,
       "cfprVnicIPv4IfOperVnetName": cfprVnicIPv4IfOperVnetName,
       "cfprVnicIPv4IfOwner": cfprVnicIPv4IfOwner,
       "cfprVnicIPv4IfPubNwId": cfprVnicIPv4IfPubNwId,
       "cfprVnicIPv4IfSharing": cfprVnicIPv4IfSharing,
       "cfprVnicIPv4IfSwitchId": cfprVnicIPv4IfSwitchId,
       "cfprVnicIPv4IfType": cfprVnicIPv4IfType,
       "cfprVnicIPv4IfVnet": cfprVnicIPv4IfVnet,
       "cfprVnicIPv4IscsiAddrTable": cfprVnicIPv4IscsiAddrTable,
       "cfprVnicIPv4IscsiAddrEntry": cfprVnicIPv4IscsiAddrEntry,
       "cfprVnicIPv4IscsiAddrInstanceId": cfprVnicIPv4IscsiAddrInstanceId,
       "cfprVnicIPv4IscsiAddrDn": cfprVnicIPv4IscsiAddrDn,
       "cfprVnicIPv4IscsiAddrRn": cfprVnicIPv4IscsiAddrRn,
       "cfprVnicIPv4IscsiAddrAddr": cfprVnicIPv4IscsiAddrAddr,
       "cfprVnicIPv4IscsiAddrDefGw": cfprVnicIPv4IscsiAddrDefGw,
       "cfprVnicIPv4IscsiAddrPrimDns": cfprVnicIPv4IscsiAddrPrimDns,
       "cfprVnicIPv4IscsiAddrSecDns": cfprVnicIPv4IscsiAddrSecDns,
       "cfprVnicIPv4IscsiAddrSubnet": cfprVnicIPv4IscsiAddrSubnet,
       "cfprVnicIPv4PooledIscsiAddrTable": cfprVnicIPv4PooledIscsiAddrTable,
       "cfprVnicIPv4PooledIscsiAddrEntry": cfprVnicIPv4PooledIscsiAddrEntry,
       "cfprVnicIPv4PooledIscsiAddrInstanceId": cfprVnicIPv4PooledIscsiAddrInstanceId,
       "cfprVnicIPv4PooledIscsiAddrDn": cfprVnicIPv4PooledIscsiAddrDn,
       "cfprVnicIPv4PooledIscsiAddrRn": cfprVnicIPv4PooledIscsiAddrRn,
       "cfprVnicIPv4PooledIscsiAddrAddr": cfprVnicIPv4PooledIscsiAddrAddr,
       "cfprVnicIPv4PooledIscsiAddrDefGw": cfprVnicIPv4PooledIscsiAddrDefGw,
       "cfprVnicIPv4PooledIscsiAddrIdentPoolName": cfprVnicIPv4PooledIscsiAddrIdentPoolName,
       "cfprVnicIPv4PooledIscsiAddrOperIdentPoolName": cfprVnicIPv4PooledIscsiAddrOperIdentPoolName,
       "cfprVnicIPv4PooledIscsiAddrPrimDns": cfprVnicIPv4PooledIscsiAddrPrimDns,
       "cfprVnicIPv4PooledIscsiAddrSecDns": cfprVnicIPv4PooledIscsiAddrSecDns,
       "cfprVnicIPv4PooledIscsiAddrSubnet": cfprVnicIPv4PooledIscsiAddrSubnet,
       "cfprVnicIPv4StaticRouteTable": cfprVnicIPv4StaticRouteTable,
       "cfprVnicIPv4StaticRouteEntry": cfprVnicIPv4StaticRouteEntry,
       "cfprVnicIPv4StaticRouteInstanceId": cfprVnicIPv4StaticRouteInstanceId,
       "cfprVnicIPv4StaticRouteDn": cfprVnicIPv4StaticRouteDn,
       "cfprVnicIPv4StaticRouteRn": cfprVnicIPv4StaticRouteRn,
       "cfprVnicIPv4StaticRouteAddr": cfprVnicIPv4StaticRouteAddr,
       "cfprVnicIPv4StaticRouteDefGw": cfprVnicIPv4StaticRouteDefGw,
       "cfprVnicIPv4StaticRouteGwAddr": cfprVnicIPv4StaticRouteGwAddr,
       "cfprVnicIPv4StaticRouteGwSubnet": cfprVnicIPv4StaticRouteGwSubnet,
       "cfprVnicIPv4StaticRouteSubnet": cfprVnicIPv4StaticRouteSubnet,
       "cfprVnicIScsiTable": cfprVnicIScsiTable,
       "cfprVnicIScsiEntry": cfprVnicIScsiEntry,
       "cfprVnicIScsiInstanceId": cfprVnicIScsiInstanceId,
       "cfprVnicIScsiDn": cfprVnicIScsiDn,
       "cfprVnicIScsiRn": cfprVnicIScsiRn,
       "cfprVnicIScsiAdaptorProfileName": cfprVnicIScsiAdaptorProfileName,
       "cfprVnicIScsiAddr": cfprVnicIScsiAddr,
       "cfprVnicIScsiAdminHostPort": cfprVnicIScsiAdminHostPort,
       "cfprVnicIScsiAdminVcon": cfprVnicIScsiAdminVcon,
       "cfprVnicIScsiAppRole": cfprVnicIScsiAppRole,
       "cfprVnicIScsiAuthProfileName": cfprVnicIScsiAuthProfileName,
       "cfprVnicIScsiBootDev": cfprVnicIScsiBootDev,
       "cfprVnicIScsiConfigQualifier": cfprVnicIScsiConfigQualifier,
       "cfprVnicIScsiConfigState": cfprVnicIScsiConfigState,
       "cfprVnicIScsiEquipmentDn": cfprVnicIScsiEquipmentDn,
       "cfprVnicIScsiEthEpDn": cfprVnicIScsiEthEpDn,
       "cfprVnicIScsiExtIPState": cfprVnicIScsiExtIPState,
       "cfprVnicIScsiFltAggr": cfprVnicIScsiFltAggr,
       "cfprVnicIScsiIdentPoolName": cfprVnicIScsiIdentPoolName,
       "cfprVnicIScsiInitNameSuffix": cfprVnicIScsiInitNameSuffix,
       "cfprVnicIScsiInitiatorName": cfprVnicIScsiInitiatorName,
       "cfprVnicIScsiInstType": cfprVnicIScsiInstType,
       "cfprVnicIScsiIqnIdentPoolName": cfprVnicIScsiIqnIdentPoolName,
       "cfprVnicIScsiName": cfprVnicIScsiName,
       "cfprVnicIScsiNwTemplName": cfprVnicIScsiNwTemplName,
       "cfprVnicIScsiOperAdaptorProfileName": cfprVnicIScsiOperAdaptorProfileName,
       "cfprVnicIScsiOperAuthProfileName": cfprVnicIScsiOperAuthProfileName,
       "cfprVnicIScsiOperHostPort": cfprVnicIScsiOperHostPort,
       "cfprVnicIScsiOperIdentPoolName": cfprVnicIScsiOperIdentPoolName,
       "cfprVnicIScsiOperIqnIdentPoolName": cfprVnicIScsiOperIqnIdentPoolName,
       "cfprVnicIScsiOperOrder": cfprVnicIScsiOperOrder,
       "cfprVnicIScsiOperSpeed": cfprVnicIScsiOperSpeed,
       "cfprVnicIScsiOperStatsPolicyName": cfprVnicIScsiOperStatsPolicyName,
       "cfprVnicIScsiOperVcon": cfprVnicIScsiOperVcon,
       "cfprVnicIScsiOrder": cfprVnicIScsiOrder,
       "cfprVnicIScsiOwner": cfprVnicIScsiOwner,
       "cfprVnicIScsiPinToGroupName": cfprVnicIScsiPinToGroupName,
       "cfprVnicIScsiQosPolicyName": cfprVnicIScsiQosPolicyName,
       "cfprVnicIScsiStatsPolicyName": cfprVnicIScsiStatsPolicyName,
       "cfprVnicIScsiSwitchId": cfprVnicIScsiSwitchId,
       "cfprVnicIScsiType": cfprVnicIScsiType,
       "cfprVnicIScsiVnicDefType": cfprVnicIScsiVnicDefType,
       "cfprVnicIScsiVnicName": cfprVnicIScsiVnicName,
       "cfprVnicIScsiAutoTargetIfTable": cfprVnicIScsiAutoTargetIfTable,
       "cfprVnicIScsiAutoTargetIfEntry": cfprVnicIScsiAutoTargetIfEntry,
       "cfprVnicIScsiAutoTargetIfInstanceId": cfprVnicIScsiAutoTargetIfInstanceId,
       "cfprVnicIScsiAutoTargetIfDn": cfprVnicIScsiAutoTargetIfDn,
       "cfprVnicIScsiAutoTargetIfRn": cfprVnicIScsiAutoTargetIfRn,
       "cfprVnicIScsiAutoTargetIfDhcpVendorId": cfprVnicIScsiAutoTargetIfDhcpVendorId,
       "cfprVnicIScsiBootParamsTable": cfprVnicIScsiBootParamsTable,
       "cfprVnicIScsiBootParamsEntry": cfprVnicIScsiBootParamsEntry,
       "cfprVnicIScsiBootParamsInstanceId": cfprVnicIScsiBootParamsInstanceId,
       "cfprVnicIScsiBootParamsDn": cfprVnicIScsiBootParamsDn,
       "cfprVnicIScsiBootParamsRn": cfprVnicIScsiBootParamsRn,
       "cfprVnicIScsiBootParamsDescr": cfprVnicIScsiBootParamsDescr,
       "cfprVnicIScsiBootParamsIntId": cfprVnicIScsiBootParamsIntId,
       "cfprVnicIScsiBootParamsName": cfprVnicIScsiBootParamsName,
       "cfprVnicIScsiBootParamsPolicyLevel": cfprVnicIScsiBootParamsPolicyLevel,
       "cfprVnicIScsiBootParamsPolicyOwner": cfprVnicIScsiBootParamsPolicyOwner,
       "cfprVnicIScsiBootVnicTable": cfprVnicIScsiBootVnicTable,
       "cfprVnicIScsiBootVnicEntry": cfprVnicIScsiBootVnicEntry,
       "cfprVnicIScsiBootVnicInstanceId": cfprVnicIScsiBootVnicInstanceId,
       "cfprVnicIScsiBootVnicDn": cfprVnicIScsiBootVnicDn,
       "cfprVnicIScsiBootVnicRn": cfprVnicIScsiBootVnicRn,
       "cfprVnicIScsiBootVnicAuthProfileName": cfprVnicIScsiBootVnicAuthProfileName,
       "cfprVnicIScsiBootVnicDescr": cfprVnicIScsiBootVnicDescr,
       "cfprVnicIScsiBootVnicInitiatorName": cfprVnicIScsiBootVnicInitiatorName,
       "cfprVnicIScsiBootVnicIntId": cfprVnicIScsiBootVnicIntId,
       "cfprVnicIScsiBootVnicIqnIdentPoolName": cfprVnicIScsiBootVnicIqnIdentPoolName,
       "cfprVnicIScsiBootVnicName": cfprVnicIScsiBootVnicName,
       "cfprVnicIScsiBootVnicOperAuthProfileName": cfprVnicIScsiBootVnicOperAuthProfileName,
       "cfprVnicIScsiBootVnicOperIqnIdentPoolName": cfprVnicIScsiBootVnicOperIqnIdentPoolName,
       "cfprVnicIScsiBootVnicPolicyLevel": cfprVnicIScsiBootVnicPolicyLevel,
       "cfprVnicIScsiBootVnicPolicyOwner": cfprVnicIScsiBootVnicPolicyOwner,
       "cfprVnicIScsiLCPTable": cfprVnicIScsiLCPTable,
       "cfprVnicIScsiLCPEntry": cfprVnicIScsiLCPEntry,
       "cfprVnicIScsiLCPInstanceId": cfprVnicIScsiLCPInstanceId,
       "cfprVnicIScsiLCPDn": cfprVnicIScsiLCPDn,
       "cfprVnicIScsiLCPRn": cfprVnicIScsiLCPRn,
       "cfprVnicIScsiLCPAdaptorProfileName": cfprVnicIScsiLCPAdaptorProfileName,
       "cfprVnicIScsiLCPAddr": cfprVnicIScsiLCPAddr,
       "cfprVnicIScsiLCPAdminHostPort": cfprVnicIScsiLCPAdminHostPort,
       "cfprVnicIScsiLCPAdminVcon": cfprVnicIScsiLCPAdminVcon,
       "cfprVnicIScsiLCPAppRole": cfprVnicIScsiLCPAppRole,
       "cfprVnicIScsiLCPBootDev": cfprVnicIScsiLCPBootDev,
       "cfprVnicIScsiLCPConfigQualifier": cfprVnicIScsiLCPConfigQualifier,
       "cfprVnicIScsiLCPConfigState": cfprVnicIScsiLCPConfigState,
       "cfprVnicIScsiLCPEquipmentDn": cfprVnicIScsiLCPEquipmentDn,
       "cfprVnicIScsiLCPFltAggr": cfprVnicIScsiLCPFltAggr,
       "cfprVnicIScsiLCPIdentPoolName": cfprVnicIScsiLCPIdentPoolName,
       "cfprVnicIScsiLCPInstType": cfprVnicIScsiLCPInstType,
       "cfprVnicIScsiLCPName": cfprVnicIScsiLCPName,
       "cfprVnicIScsiLCPNwTemplName": cfprVnicIScsiLCPNwTemplName,
       "cfprVnicIScsiLCPOperAdaptorProfileName": cfprVnicIScsiLCPOperAdaptorProfileName,
       "cfprVnicIScsiLCPOperHostPort": cfprVnicIScsiLCPOperHostPort,
       "cfprVnicIScsiLCPOperIdentPoolName": cfprVnicIScsiLCPOperIdentPoolName,
       "cfprVnicIScsiLCPOperOrder": cfprVnicIScsiLCPOperOrder,
       "cfprVnicIScsiLCPOperSpeed": cfprVnicIScsiLCPOperSpeed,
       "cfprVnicIScsiLCPOperStatsPolicyName": cfprVnicIScsiLCPOperStatsPolicyName,
       "cfprVnicIScsiLCPOperVcon": cfprVnicIScsiLCPOperVcon,
       "cfprVnicIScsiLCPOrder": cfprVnicIScsiLCPOrder,
       "cfprVnicIScsiLCPOwner": cfprVnicIScsiLCPOwner,
       "cfprVnicIScsiLCPPinToGroupName": cfprVnicIScsiLCPPinToGroupName,
       "cfprVnicIScsiLCPQosPolicyName": cfprVnicIScsiLCPQosPolicyName,
       "cfprVnicIScsiLCPStatsPolicyName": cfprVnicIScsiLCPStatsPolicyName,
       "cfprVnicIScsiLCPSwitchId": cfprVnicIScsiLCPSwitchId,
       "cfprVnicIScsiLCPType": cfprVnicIScsiLCPType,
       "cfprVnicIScsiLCPVnicName": cfprVnicIScsiLCPVnicName,
       "cfprVnicIScsiNodeTable": cfprVnicIScsiNodeTable,
       "cfprVnicIScsiNodeEntry": cfprVnicIScsiNodeEntry,
       "cfprVnicIScsiNodeInstanceId": cfprVnicIScsiNodeInstanceId,
       "cfprVnicIScsiNodeDn": cfprVnicIScsiNodeDn,
       "cfprVnicIScsiNodeRn": cfprVnicIScsiNodeRn,
       "cfprVnicIScsiNodeFltAggr": cfprVnicIScsiNodeFltAggr,
       "cfprVnicIScsiNodeInitNameSuffix": cfprVnicIScsiNodeInitNameSuffix,
       "cfprVnicIScsiNodeInitiatorName": cfprVnicIScsiNodeInitiatorName,
       "cfprVnicIScsiNodeIqnIdentPoolName": cfprVnicIScsiNodeIqnIdentPoolName,
       "cfprVnicIScsiNodeOperIqnIdentPoolName": cfprVnicIScsiNodeOperIqnIdentPoolName,
       "cfprVnicIScsiNodeOwner": cfprVnicIScsiNodeOwner,
       "cfprVnicIScsiStaticTargetIfTable": cfprVnicIScsiStaticTargetIfTable,
       "cfprVnicIScsiStaticTargetIfEntry": cfprVnicIScsiStaticTargetIfEntry,
       "cfprVnicIScsiStaticTargetIfInstanceId": cfprVnicIScsiStaticTargetIfInstanceId,
       "cfprVnicIScsiStaticTargetIfDn": cfprVnicIScsiStaticTargetIfDn,
       "cfprVnicIScsiStaticTargetIfRn": cfprVnicIScsiStaticTargetIfRn,
       "cfprVnicIScsiStaticTargetIfAuthProfileName": cfprVnicIScsiStaticTargetIfAuthProfileName,
       "cfprVnicIScsiStaticTargetIfIpAddress": cfprVnicIScsiStaticTargetIfIpAddress,
       "cfprVnicIScsiStaticTargetIfName": cfprVnicIScsiStaticTargetIfName,
       "cfprVnicIScsiStaticTargetIfOperAuthProfileName": cfprVnicIScsiStaticTargetIfOperAuthProfileName,
       "cfprVnicIScsiStaticTargetIfPort": cfprVnicIScsiStaticTargetIfPort,
       "cfprVnicIScsiStaticTargetIfPriority": cfprVnicIScsiStaticTargetIfPriority,
       "cfprVnicInternalProfileTable": cfprVnicInternalProfileTable,
       "cfprVnicInternalProfileEntry": cfprVnicInternalProfileEntry,
       "cfprVnicInternalProfileInstanceId": cfprVnicInternalProfileInstanceId,
       "cfprVnicInternalProfileDn": cfprVnicInternalProfileDn,
       "cfprVnicInternalProfileRn": cfprVnicInternalProfileRn,
       "cfprVnicInternalProfileDescr": cfprVnicInternalProfileDescr,
       "cfprVnicInternalProfileIntId": cfprVnicInternalProfileIntId,
       "cfprVnicInternalProfileMaxPorts": cfprVnicInternalProfileMaxPorts,
       "cfprVnicInternalProfileName": cfprVnicInternalProfileName,
       "cfprVnicInternalProfilePolicyLevel": cfprVnicInternalProfilePolicyLevel,
       "cfprVnicInternalProfilePolicyOwner": cfprVnicInternalProfilePolicyOwner,
       "cfprVnicIpV4HistoryTable": cfprVnicIpV4HistoryTable,
       "cfprVnicIpV4HistoryEntry": cfprVnicIpV4HistoryEntry,
       "cfprVnicIpV4HistoryInstanceId": cfprVnicIpV4HistoryInstanceId,
       "cfprVnicIpV4HistoryDn": cfprVnicIpV4HistoryDn,
       "cfprVnicIpV4HistoryRn": cfprVnicIpV4HistoryRn,
       "cfprVnicIpV4HistoryOldIpV4Addr": cfprVnicIpV4HistoryOldIpV4Addr,
       "cfprVnicIpV4MgmtPooledAddrTable": cfprVnicIpV4MgmtPooledAddrTable,
       "cfprVnicIpV4MgmtPooledAddrEntry": cfprVnicIpV4MgmtPooledAddrEntry,
       "cfprVnicIpV4MgmtPooledAddrInstanceId": cfprVnicIpV4MgmtPooledAddrInstanceId,
       "cfprVnicIpV4MgmtPooledAddrDn": cfprVnicIpV4MgmtPooledAddrDn,
       "cfprVnicIpV4MgmtPooledAddrRn": cfprVnicIpV4MgmtPooledAddrRn,
       "cfprVnicIpV4MgmtPooledAddrAddr": cfprVnicIpV4MgmtPooledAddrAddr,
       "cfprVnicIpV4MgmtPooledAddrDefGw": cfprVnicIpV4MgmtPooledAddrDefGw,
       "cfprVnicIpV4MgmtPooledAddrName": cfprVnicIpV4MgmtPooledAddrName,
       "cfprVnicIpV4MgmtPooledAddrOperName": cfprVnicIpV4MgmtPooledAddrOperName,
       "cfprVnicIpV4MgmtPooledAddrPrimDns": cfprVnicIpV4MgmtPooledAddrPrimDns,
       "cfprVnicIpV4MgmtPooledAddrSecDns": cfprVnicIpV4MgmtPooledAddrSecDns,
       "cfprVnicIpV4MgmtPooledAddrSubnet": cfprVnicIpV4MgmtPooledAddrSubnet,
       "cfprVnicIpV4PooledAddrTable": cfprVnicIpV4PooledAddrTable,
       "cfprVnicIpV4PooledAddrEntry": cfprVnicIpV4PooledAddrEntry,
       "cfprVnicIpV4PooledAddrInstanceId": cfprVnicIpV4PooledAddrInstanceId,
       "cfprVnicIpV4PooledAddrDn": cfprVnicIpV4PooledAddrDn,
       "cfprVnicIpV4PooledAddrRn": cfprVnicIpV4PooledAddrRn,
       "cfprVnicIpV4PooledAddrAddr": cfprVnicIpV4PooledAddrAddr,
       "cfprVnicIpV4PooledAddrDefGw": cfprVnicIpV4PooledAddrDefGw,
       "cfprVnicIpV4PooledAddrName": cfprVnicIpV4PooledAddrName,
       "cfprVnicIpV4PooledAddrOperName": cfprVnicIpV4PooledAddrOperName,
       "cfprVnicIpV4PooledAddrPrimDns": cfprVnicIpV4PooledAddrPrimDns,
       "cfprVnicIpV4PooledAddrSecDns": cfprVnicIpV4PooledAddrSecDns,
       "cfprVnicIpV4PooledAddrSubnet": cfprVnicIpV4PooledAddrSubnet,
       "cfprVnicIpV4ProfDerivedAddrTable": cfprVnicIpV4ProfDerivedAddrTable,
       "cfprVnicIpV4ProfDerivedAddrEntry": cfprVnicIpV4ProfDerivedAddrEntry,
       "cfprVnicIpV4ProfDerivedAddrInstanceId": cfprVnicIpV4ProfDerivedAddrInstanceId,
       "cfprVnicIpV4ProfDerivedAddrDn": cfprVnicIpV4ProfDerivedAddrDn,
       "cfprVnicIpV4ProfDerivedAddrRn": cfprVnicIpV4ProfDerivedAddrRn,
       "cfprVnicIpV4ProfDerivedAddrAddr": cfprVnicIpV4ProfDerivedAddrAddr,
       "cfprVnicIpV4ProfDerivedAddrDefGw": cfprVnicIpV4ProfDerivedAddrDefGw,
       "cfprVnicIpV4ProfDerivedAddrSubnet": cfprVnicIpV4ProfDerivedAddrSubnet,
       "cfprVnicIpV4StaticAddrTable": cfprVnicIpV4StaticAddrTable,
       "cfprVnicIpV4StaticAddrEntry": cfprVnicIpV4StaticAddrEntry,
       "cfprVnicIpV4StaticAddrInstanceId": cfprVnicIpV4StaticAddrInstanceId,
       "cfprVnicIpV4StaticAddrDn": cfprVnicIpV4StaticAddrDn,
       "cfprVnicIpV4StaticAddrRn": cfprVnicIpV4StaticAddrRn,
       "cfprVnicIpV4StaticAddrAddr": cfprVnicIpV4StaticAddrAddr,
       "cfprVnicIpV4StaticAddrDefGw": cfprVnicIpV4StaticAddrDefGw,
       "cfprVnicIpV4StaticAddrPrimDns": cfprVnicIpV4StaticAddrPrimDns,
       "cfprVnicIpV4StaticAddrSecDns": cfprVnicIpV4StaticAddrSecDns,
       "cfprVnicIpV4StaticAddrSubnet": cfprVnicIpV4StaticAddrSubnet,
       "cfprVnicIpV6HistoryTable": cfprVnicIpV6HistoryTable,
       "cfprVnicIpV6HistoryEntry": cfprVnicIpV6HistoryEntry,
       "cfprVnicIpV6HistoryInstanceId": cfprVnicIpV6HistoryInstanceId,
       "cfprVnicIpV6HistoryDn": cfprVnicIpV6HistoryDn,
       "cfprVnicIpV6HistoryRn": cfprVnicIpV6HistoryRn,
       "cfprVnicIpV6HistoryOldIpV6Addr": cfprVnicIpV6HistoryOldIpV6Addr,
       "cfprVnicIpV6MgmtPooledAddrTable": cfprVnicIpV6MgmtPooledAddrTable,
       "cfprVnicIpV6MgmtPooledAddrEntry": cfprVnicIpV6MgmtPooledAddrEntry,
       "cfprVnicIpV6MgmtPooledAddrInstanceId": cfprVnicIpV6MgmtPooledAddrInstanceId,
       "cfprVnicIpV6MgmtPooledAddrDn": cfprVnicIpV6MgmtPooledAddrDn,
       "cfprVnicIpV6MgmtPooledAddrRn": cfprVnicIpV6MgmtPooledAddrRn,
       "cfprVnicIpV6MgmtPooledAddrAddr": cfprVnicIpV6MgmtPooledAddrAddr,
       "cfprVnicIpV6MgmtPooledAddrDefGw": cfprVnicIpV6MgmtPooledAddrDefGw,
       "cfprVnicIpV6MgmtPooledAddrName": cfprVnicIpV6MgmtPooledAddrName,
       "cfprVnicIpV6MgmtPooledAddrOperName": cfprVnicIpV6MgmtPooledAddrOperName,
       "cfprVnicIpV6MgmtPooledAddrPrefix": cfprVnicIpV6MgmtPooledAddrPrefix,
       "cfprVnicIpV6MgmtPooledAddrPrimDns": cfprVnicIpV6MgmtPooledAddrPrimDns,
       "cfprVnicIpV6MgmtPooledAddrSecDns": cfprVnicIpV6MgmtPooledAddrSecDns,
       "cfprVnicIpV6StaticAddrTable": cfprVnicIpV6StaticAddrTable,
       "cfprVnicIpV6StaticAddrEntry": cfprVnicIpV6StaticAddrEntry,
       "cfprVnicIpV6StaticAddrInstanceId": cfprVnicIpV6StaticAddrInstanceId,
       "cfprVnicIpV6StaticAddrDn": cfprVnicIpV6StaticAddrDn,
       "cfprVnicIpV6StaticAddrRn": cfprVnicIpV6StaticAddrRn,
       "cfprVnicIpV6StaticAddrAddr": cfprVnicIpV6StaticAddrAddr,
       "cfprVnicIpV6StaticAddrDefGw": cfprVnicIpV6StaticAddrDefGw,
       "cfprVnicIpV6StaticAddrPrefix": cfprVnicIpV6StaticAddrPrefix,
       "cfprVnicIpV6StaticAddrPrimDns": cfprVnicIpV6StaticAddrPrimDns,
       "cfprVnicIpV6StaticAddrSecDns": cfprVnicIpV6StaticAddrSecDns,
       "cfprVnicIpcTable": cfprVnicIpcTable,
       "cfprVnicIpcEntry": cfprVnicIpcEntry,
       "cfprVnicIpcInstanceId": cfprVnicIpcInstanceId,
       "cfprVnicIpcDn": cfprVnicIpcDn,
       "cfprVnicIpcRn": cfprVnicIpcRn,
       "cfprVnicIpcAdaptorProfileName": cfprVnicIpcAdaptorProfileName,
       "cfprVnicIpcAddr": cfprVnicIpcAddr,
       "cfprVnicIpcAdminHostPort": cfprVnicIpcAdminHostPort,
       "cfprVnicIpcAdminVcon": cfprVnicIpcAdminVcon,
       "cfprVnicIpcAppRole": cfprVnicIpcAppRole,
       "cfprVnicIpcBootDev": cfprVnicIpcBootDev,
       "cfprVnicIpcConfigQualifier": cfprVnicIpcConfigQualifier,
       "cfprVnicIpcConfigState": cfprVnicIpcConfigState,
       "cfprVnicIpcEquipmentDn": cfprVnicIpcEquipmentDn,
       "cfprVnicIpcIdentPoolName": cfprVnicIpcIdentPoolName,
       "cfprVnicIpcInstType": cfprVnicIpcInstType,
       "cfprVnicIpcMtu": cfprVnicIpcMtu,
       "cfprVnicIpcName": cfprVnicIpcName,
       "cfprVnicIpcNwCtrlPolicyName": cfprVnicIpcNwCtrlPolicyName,
       "cfprVnicIpcNwTemplName": cfprVnicIpcNwTemplName,
       "cfprVnicIpcOperAdaptorProfileName": cfprVnicIpcOperAdaptorProfileName,
       "cfprVnicIpcOperHostPort": cfprVnicIpcOperHostPort,
       "cfprVnicIpcOperIdentPoolName": cfprVnicIpcOperIdentPoolName,
       "cfprVnicIpcOperNwCtrlPolicyName": cfprVnicIpcOperNwCtrlPolicyName,
       "cfprVnicIpcOperNwTemplName": cfprVnicIpcOperNwTemplName,
       "cfprVnicIpcOperOrder": cfprVnicIpcOperOrder,
       "cfprVnicIpcOperPinToGroupName": cfprVnicIpcOperPinToGroupName,
       "cfprVnicIpcOperQosPolicyName": cfprVnicIpcOperQosPolicyName,
       "cfprVnicIpcOperSpeed": cfprVnicIpcOperSpeed,
       "cfprVnicIpcOperStatsPolicyName": cfprVnicIpcOperStatsPolicyName,
       "cfprVnicIpcOperVcon": cfprVnicIpcOperVcon,
       "cfprVnicIpcOrder": cfprVnicIpcOrder,
       "cfprVnicIpcOwner": cfprVnicIpcOwner,
       "cfprVnicIpcPinToGroupName": cfprVnicIpcPinToGroupName,
       "cfprVnicIpcQosPolicyName": cfprVnicIpcQosPolicyName,
       "cfprVnicIpcStatsPolicyName": cfprVnicIpcStatsPolicyName,
       "cfprVnicIpcSwitchId": cfprVnicIpcSwitchId,
       "cfprVnicIpcType": cfprVnicIpcType,
       "cfprVnicIpcIfTable": cfprVnicIpcIfTable,
       "cfprVnicIpcIfEntry": cfprVnicIpcIfEntry,
       "cfprVnicIpcIfInstanceId": cfprVnicIpcIfInstanceId,
       "cfprVnicIpcIfDn": cfprVnicIpcIfDn,
       "cfprVnicIpcIfRn": cfprVnicIpcIfRn,
       "cfprVnicIpcIfAddr": cfprVnicIpcIfAddr,
       "cfprVnicIpcIfConfigQualifier": cfprVnicIpcIfConfigQualifier,
       "cfprVnicIpcIfDefaultNet": cfprVnicIpcIfDefaultNet,
       "cfprVnicIpcIfName": cfprVnicIpcIfName,
       "cfprVnicIpcIfOperState": cfprVnicIpcIfOperState,
       "cfprVnicIpcIfOperVnetDn": cfprVnicIpcIfOperVnetDn,
       "cfprVnicIpcIfOperVnetName": cfprVnicIpcIfOperVnetName,
       "cfprVnicIpcIfOwner": cfprVnicIpcIfOwner,
       "cfprVnicIpcIfPubNwId": cfprVnicIpcIfPubNwId,
       "cfprVnicIpcIfSharing": cfprVnicIpcIfSharing,
       "cfprVnicIpcIfSwitchId": cfprVnicIpcIfSwitchId,
       "cfprVnicIpcIfType": cfprVnicIpcIfType,
       "cfprVnicIpcIfVnet": cfprVnicIpcIfVnet,
       "cfprVnicIqnHistoryTable": cfprVnicIqnHistoryTable,
       "cfprVnicIqnHistoryEntry": cfprVnicIqnHistoryEntry,
       "cfprVnicIqnHistoryInstanceId": cfprVnicIqnHistoryInstanceId,
       "cfprVnicIqnHistoryDn": cfprVnicIqnHistoryDn,
       "cfprVnicIqnHistoryRn": cfprVnicIqnHistoryRn,
       "cfprVnicIqnHistoryOldInitiatorName": cfprVnicIqnHistoryOldInitiatorName,
       "cfprVnicLanConnPolicyTable": cfprVnicLanConnPolicyTable,
       "cfprVnicLanConnPolicyEntry": cfprVnicLanConnPolicyEntry,
       "cfprVnicLanConnPolicyInstanceId": cfprVnicLanConnPolicyInstanceId,
       "cfprVnicLanConnPolicyDn": cfprVnicLanConnPolicyDn,
       "cfprVnicLanConnPolicyRn": cfprVnicLanConnPolicyRn,
       "cfprVnicLanConnPolicyDescr": cfprVnicLanConnPolicyDescr,
       "cfprVnicLanConnPolicyFltAggr": cfprVnicLanConnPolicyFltAggr,
       "cfprVnicLanConnPolicyIntId": cfprVnicLanConnPolicyIntId,
       "cfprVnicLanConnPolicyName": cfprVnicLanConnPolicyName,
       "cfprVnicLanConnPolicyPolicyLevel": cfprVnicLanConnPolicyPolicyLevel,
       "cfprVnicLanConnPolicyPolicyOwner": cfprVnicLanConnPolicyPolicyOwner,
       "cfprVnicLanConnTemplTable": cfprVnicLanConnTemplTable,
       "cfprVnicLanConnTemplEntry": cfprVnicLanConnTemplEntry,
       "cfprVnicLanConnTemplInstanceId": cfprVnicLanConnTemplInstanceId,
       "cfprVnicLanConnTemplDn": cfprVnicLanConnTemplDn,
       "cfprVnicLanConnTemplRn": cfprVnicLanConnTemplRn,
       "cfprVnicLanConnTemplDescr": cfprVnicLanConnTemplDescr,
       "cfprVnicLanConnTemplIdentPoolName": cfprVnicLanConnTemplIdentPoolName,
       "cfprVnicLanConnTemplIntId": cfprVnicLanConnTemplIntId,
       "cfprVnicLanConnTemplMtu": cfprVnicLanConnTemplMtu,
       "cfprVnicLanConnTemplName": cfprVnicLanConnTemplName,
       "cfprVnicLanConnTemplNwCtrlPolicyName": cfprVnicLanConnTemplNwCtrlPolicyName,
       "cfprVnicLanConnTemplOperIdentPoolName": cfprVnicLanConnTemplOperIdentPoolName,
       "cfprVnicLanConnTemplOperNwCtrlPolicyName": cfprVnicLanConnTemplOperNwCtrlPolicyName,
       "cfprVnicLanConnTemplOperQosPolicyName": cfprVnicLanConnTemplOperQosPolicyName,
       "cfprVnicLanConnTemplOperStatsPolicyName": cfprVnicLanConnTemplOperStatsPolicyName,
       "cfprVnicLanConnTemplPinToGroupName": cfprVnicLanConnTemplPinToGroupName,
       "cfprVnicLanConnTemplPolicyLevel": cfprVnicLanConnTemplPolicyLevel,
       "cfprVnicLanConnTemplPolicyOwner": cfprVnicLanConnTemplPolicyOwner,
       "cfprVnicLanConnTemplQosPolicyName": cfprVnicLanConnTemplQosPolicyName,
       "cfprVnicLanConnTemplStatsPolicyName": cfprVnicLanConnTemplStatsPolicyName,
       "cfprVnicLanConnTemplSwitchId": cfprVnicLanConnTemplSwitchId,
       "cfprVnicLanConnTemplTarget": cfprVnicLanConnTemplTarget,
       "cfprVnicLanConnTemplTemplType": cfprVnicLanConnTemplTemplType,
       "cfprVnicLifVlanTable": cfprVnicLifVlanTable,
       "cfprVnicLifVlanEntry": cfprVnicLifVlanEntry,
       "cfprVnicLifVlanInstanceId": cfprVnicLifVlanInstanceId,
       "cfprVnicLifVlanDn": cfprVnicLifVlanDn,
       "cfprVnicLifVlanRn": cfprVnicLifVlanRn,
       "cfprVnicLifVlanAddr": cfprVnicLifVlanAddr,
       "cfprVnicLifVlanConfigQualifier": cfprVnicLifVlanConfigQualifier,
       "cfprVnicLifVlanDefaultNet": cfprVnicLifVlanDefaultNet,
       "cfprVnicLifVlanName": cfprVnicLifVlanName,
       "cfprVnicLifVlanOperState": cfprVnicLifVlanOperState,
       "cfprVnicLifVlanOperVnetDn": cfprVnicLifVlanOperVnetDn,
       "cfprVnicLifVlanOperVnetName": cfprVnicLifVlanOperVnetName,
       "cfprVnicLifVlanOwner": cfprVnicLifVlanOwner,
       "cfprVnicLifVlanPubNwId": cfprVnicLifVlanPubNwId,
       "cfprVnicLifVlanSharing": cfprVnicLifVlanSharing,
       "cfprVnicLifVlanSwitchId": cfprVnicLifVlanSwitchId,
       "cfprVnicLifVlanType": cfprVnicLifVlanType,
       "cfprVnicLifVlanVnet": cfprVnicLifVlanVnet,
       "cfprVnicLifVsanTable": cfprVnicLifVsanTable,
       "cfprVnicLifVsanEntry": cfprVnicLifVsanEntry,
       "cfprVnicLifVsanInstanceId": cfprVnicLifVsanInstanceId,
       "cfprVnicLifVsanDn": cfprVnicLifVsanDn,
       "cfprVnicLifVsanRn": cfprVnicLifVsanRn,
       "cfprVnicLifVsanConfigQualifier": cfprVnicLifVsanConfigQualifier,
       "cfprVnicLifVsanInitiator": cfprVnicLifVsanInitiator,
       "cfprVnicLifVsanName": cfprVnicLifVsanName,
       "cfprVnicLifVsanOperState": cfprVnicLifVsanOperState,
       "cfprVnicLifVsanOperVnetDn": cfprVnicLifVsanOperVnetDn,
       "cfprVnicLifVsanOperVnetName": cfprVnicLifVsanOperVnetName,
       "cfprVnicLifVsanOwner": cfprVnicLifVsanOwner,
       "cfprVnicLifVsanPubNwId": cfprVnicLifVsanPubNwId,
       "cfprVnicLifVsanSharing": cfprVnicLifVsanSharing,
       "cfprVnicLifVsanSwitchId": cfprVnicLifVsanSwitchId,
       "cfprVnicLifVsanType": cfprVnicLifVsanType,
       "cfprVnicLifVsanVnet": cfprVnicLifVsanVnet,
       "cfprVnicLunTable": cfprVnicLunTable,
       "cfprVnicLunEntry": cfprVnicLunEntry,
       "cfprVnicLunInstanceId": cfprVnicLunInstanceId,
       "cfprVnicLunDn": cfprVnicLunDn,
       "cfprVnicLunRn": cfprVnicLunRn,
       "cfprVnicLunBootable": cfprVnicLunBootable,
       "cfprVnicLunId": cfprVnicLunId,
       "cfprVnicMacHistoryTable": cfprVnicMacHistoryTable,
       "cfprVnicMacHistoryEntry": cfprVnicMacHistoryEntry,
       "cfprVnicMacHistoryInstanceId": cfprVnicMacHistoryInstanceId,
       "cfprVnicMacHistoryDn": cfprVnicMacHistoryDn,
       "cfprVnicMacHistoryRn": cfprVnicMacHistoryRn,
       "cfprVnicMacHistoryOldaddr": cfprVnicMacHistoryOldaddr,
       "cfprVnicOProfileAliasTable": cfprVnicOProfileAliasTable,
       "cfprVnicOProfileAliasEntry": cfprVnicOProfileAliasEntry,
       "cfprVnicOProfileAliasInstanceId": cfprVnicOProfileAliasInstanceId,
       "cfprVnicOProfileAliasDn": cfprVnicOProfileAliasDn,
       "cfprVnicOProfileAliasRn": cfprVnicOProfileAliasRn,
       "cfprVnicOProfileAliasAlias": cfprVnicOProfileAliasAlias,
       "cfprVnicOProfileAliasMgmtPlane": cfprVnicOProfileAliasMgmtPlane,
       "cfprVnicOProfileAliasVSwitchId": cfprVnicOProfileAliasVSwitchId,
       "cfprVnicOProfileAliasVSwitchName": cfprVnicOProfileAliasVSwitchName,
       "cfprVnicProfileTable": cfprVnicProfileTable,
       "cfprVnicProfileEntry": cfprVnicProfileEntry,
       "cfprVnicProfileInstanceId": cfprVnicProfileInstanceId,
       "cfprVnicProfileDn": cfprVnicProfileDn,
       "cfprVnicProfileRn": cfprVnicProfileRn,
       "cfprVnicProfileCdp": cfprVnicProfileCdp,
       "cfprVnicProfileConfigQualifier": cfprVnicProfileConfigQualifier,
       "cfprVnicProfileCos": cfprVnicProfileCos,
       "cfprVnicProfileDescr": cfprVnicProfileDescr,
       "cfprVnicProfileForgeMac": cfprVnicProfileForgeMac,
       "cfprVnicProfileHostNwIOPerf": cfprVnicProfileHostNwIOPerf,
       "cfprVnicProfileIntId": cfprVnicProfileIntId,
       "cfprVnicProfileMacRegisterMode": cfprVnicProfileMacRegisterMode,
       "cfprVnicProfileMaxPorts": cfprVnicProfileMaxPorts,
       "cfprVnicProfileName": cfprVnicProfileName,
       "cfprVnicProfileNwCtrlPolicyName": cfprVnicProfileNwCtrlPolicyName,
       "cfprVnicProfileOperNwCtrlPolicyName": cfprVnicProfileOperNwCtrlPolicyName,
       "cfprVnicProfileOperQosPolicyName": cfprVnicProfileOperQosPolicyName,
       "cfprVnicProfilePinToGroupName": cfprVnicProfilePinToGroupName,
       "cfprVnicProfilePolicyLevel": cfprVnicProfilePolicyLevel,
       "cfprVnicProfilePolicyOwner": cfprVnicProfilePolicyOwner,
       "cfprVnicProfilePortProfileUuid": cfprVnicProfilePortProfileUuid,
       "cfprVnicProfilePrimaryVlanId": cfprVnicProfilePrimaryVlanId,
       "cfprVnicProfileQosPolicyDn": cfprVnicProfileQosPolicyDn,
       "cfprVnicProfileQosPolicyId": cfprVnicProfileQosPolicyId,
       "cfprVnicProfileQosPolicyName": cfprVnicProfileQosPolicyName,
       "cfprVnicProfileSwABorderAggrPort": cfprVnicProfileSwABorderAggrPort,
       "cfprVnicProfileSwABorderPort": cfprVnicProfileSwABorderPort,
       "cfprVnicProfileSwABorderSlot": cfprVnicProfileSwABorderSlot,
       "cfprVnicProfileSwBBorderAggrPort": cfprVnicProfileSwBBorderAggrPort,
       "cfprVnicProfileSwBBorderPort": cfprVnicProfileSwBBorderPort,
       "cfprVnicProfileSwBBorderSlot": cfprVnicProfileSwBBorderSlot,
       "cfprVnicProfileType": cfprVnicProfileType,
       "cfprVnicProfileUplinkFailAction": cfprVnicProfileUplinkFailAction,
       "cfprVnicProfileAliasTable": cfprVnicProfileAliasTable,
       "cfprVnicProfileAliasEntry": cfprVnicProfileAliasEntry,
       "cfprVnicProfileAliasInstanceId": cfprVnicProfileAliasInstanceId,
       "cfprVnicProfileAliasDn": cfprVnicProfileAliasDn,
       "cfprVnicProfileAliasRn": cfprVnicProfileAliasRn,
       "cfprVnicProfileAliasAlias": cfprVnicProfileAliasAlias,
       "cfprVnicProfileAliasSwUuid": cfprVnicProfileAliasSwUuid,
       "cfprVnicProfileRefTable": cfprVnicProfileRefTable,
       "cfprVnicProfileRefEntry": cfprVnicProfileRefEntry,
       "cfprVnicProfileRefInstanceId": cfprVnicProfileRefInstanceId,
       "cfprVnicProfileRefDn": cfprVnicProfileRefDn,
       "cfprVnicProfileRefRn": cfprVnicProfileRefRn,
       "cfprVnicProfileRefName": cfprVnicProfileRefName,
       "cfprVnicProfileRefSourceDn": cfprVnicProfileRefSourceDn,
       "cfprVnicProfileSetTable": cfprVnicProfileSetTable,
       "cfprVnicProfileSetEntry": cfprVnicProfileSetEntry,
       "cfprVnicProfileSetInstanceId": cfprVnicProfileSetInstanceId,
       "cfprVnicProfileSetDn": cfprVnicProfileSetDn,
       "cfprVnicProfileSetRn": cfprVnicProfileSetRn,
       "cfprVnicProfileSetFltAggr": cfprVnicProfileSetFltAggr,
       "cfprVnicProfileSetFsmDescr": cfprVnicProfileSetFsmDescr,
       "cfprVnicProfileSetFsmPrev": cfprVnicProfileSetFsmPrev,
       "cfprVnicProfileSetFsmProgr": cfprVnicProfileSetFsmProgr,
       "cfprVnicProfileSetFsmRmtInvErrCode": cfprVnicProfileSetFsmRmtInvErrCode,
       "cfprVnicProfileSetFsmRmtInvErrDescr": cfprVnicProfileSetFsmRmtInvErrDescr,
       "cfprVnicProfileSetFsmRmtInvRslt": cfprVnicProfileSetFsmRmtInvRslt,
       "cfprVnicProfileSetFsmStageDescr": cfprVnicProfileSetFsmStageDescr,
       "cfprVnicProfileSetFsmStamp": cfprVnicProfileSetFsmStamp,
       "cfprVnicProfileSetFsmStatus": cfprVnicProfileSetFsmStatus,
       "cfprVnicProfileSetFsmTry": cfprVnicProfileSetFsmTry,
       "cfprVnicProfileSetGenNum": cfprVnicProfileSetGenNum,
       "cfprVnicProfileSetFsmTable": cfprVnicProfileSetFsmTable,
       "cfprVnicProfileSetFsmEntry": cfprVnicProfileSetFsmEntry,
       "cfprVnicProfileSetFsmInstanceId": cfprVnicProfileSetFsmInstanceId,
       "cfprVnicProfileSetFsmDn": cfprVnicProfileSetFsmDn,
       "cfprVnicProfileSetFsmRn": cfprVnicProfileSetFsmRn,
       "cfprVnicProfileSetFsmCompletionTime": cfprVnicProfileSetFsmCompletionTime,
       "cfprVnicProfileSetFsmCurrentFsm": cfprVnicProfileSetFsmCurrentFsm,
       "cfprVnicProfileSetFsmDescrData": cfprVnicProfileSetFsmDescrData,
       "cfprVnicProfileSetFsmFsmStatus": cfprVnicProfileSetFsmFsmStatus,
       "cfprVnicProfileSetFsmProgress": cfprVnicProfileSetFsmProgress,
       "cfprVnicProfileSetFsmRmtErrCode": cfprVnicProfileSetFsmRmtErrCode,
       "cfprVnicProfileSetFsmRmtErrDescr": cfprVnicProfileSetFsmRmtErrDescr,
       "cfprVnicProfileSetFsmRmtRslt": cfprVnicProfileSetFsmRmtRslt,
       "cfprVnicProfileSetFsmStageTable": cfprVnicProfileSetFsmStageTable,
       "cfprVnicProfileSetFsmStageEntry": cfprVnicProfileSetFsmStageEntry,
       "cfprVnicProfileSetFsmStageInstanceId": cfprVnicProfileSetFsmStageInstanceId,
       "cfprVnicProfileSetFsmStageDn": cfprVnicProfileSetFsmStageDn,
       "cfprVnicProfileSetFsmStageRn": cfprVnicProfileSetFsmStageRn,
       "cfprVnicProfileSetFsmStageDescrData": cfprVnicProfileSetFsmStageDescrData,
       "cfprVnicProfileSetFsmStageLastUpdateTime": cfprVnicProfileSetFsmStageLastUpdateTime,
       "cfprVnicProfileSetFsmStageName": cfprVnicProfileSetFsmStageName,
       "cfprVnicProfileSetFsmStageOrder": cfprVnicProfileSetFsmStageOrder,
       "cfprVnicProfileSetFsmStageRetry": cfprVnicProfileSetFsmStageRetry,
       "cfprVnicProfileSetFsmStageStageStatus": cfprVnicProfileSetFsmStageStageStatus,
       "cfprVnicProfileSetFsmTaskTable": cfprVnicProfileSetFsmTaskTable,
       "cfprVnicProfileSetFsmTaskEntry": cfprVnicProfileSetFsmTaskEntry,
       "cfprVnicProfileSetFsmTaskInstanceId": cfprVnicProfileSetFsmTaskInstanceId,
       "cfprVnicProfileSetFsmTaskDn": cfprVnicProfileSetFsmTaskDn,
       "cfprVnicProfileSetFsmTaskRn": cfprVnicProfileSetFsmTaskRn,
       "cfprVnicProfileSetFsmTaskCompletion": cfprVnicProfileSetFsmTaskCompletion,
       "cfprVnicProfileSetFsmTaskFlags": cfprVnicProfileSetFsmTaskFlags,
       "cfprVnicProfileSetFsmTaskItem": cfprVnicProfileSetFsmTaskItem,
       "cfprVnicProfileSetFsmTaskSeqId": cfprVnicProfileSetFsmTaskSeqId,
       "cfprVnicRackServerDiscoveryProfileTable": cfprVnicRackServerDiscoveryProfileTable,
       "cfprVnicRackServerDiscoveryProfileEntry": cfprVnicRackServerDiscoveryProfileEntry,
       "cfprVnicRackServerDiscoveryProfileInstanceId": cfprVnicRackServerDiscoveryProfileInstanceId,
       "cfprVnicRackServerDiscoveryProfileDn": cfprVnicRackServerDiscoveryProfileDn,
       "cfprVnicRackServerDiscoveryProfileRn": cfprVnicRackServerDiscoveryProfileRn,
       "cfprVnicRackServerDiscoveryProfileDescr": cfprVnicRackServerDiscoveryProfileDescr,
       "cfprVnicRackServerDiscoveryProfileIntId": cfprVnicRackServerDiscoveryProfileIntId,
       "cfprVnicRackServerDiscoveryProfileMaxPorts": cfprVnicRackServerDiscoveryProfileMaxPorts,
       "cfprVnicRackServerDiscoveryProfileName": cfprVnicRackServerDiscoveryProfileName,
       "cfprVnicRackServerDiscoveryProfilePolicyLevel": cfprVnicRackServerDiscoveryProfilePolicyLevel,
       "cfprVnicRackServerDiscoveryProfilePolicyOwner": cfprVnicRackServerDiscoveryProfilePolicyOwner,
       "cfprVnicSanConnPolicyTable": cfprVnicSanConnPolicyTable,
       "cfprVnicSanConnPolicyEntry": cfprVnicSanConnPolicyEntry,
       "cfprVnicSanConnPolicyInstanceId": cfprVnicSanConnPolicyInstanceId,
       "cfprVnicSanConnPolicyDn": cfprVnicSanConnPolicyDn,
       "cfprVnicSanConnPolicyRn": cfprVnicSanConnPolicyRn,
       "cfprVnicSanConnPolicyDescr": cfprVnicSanConnPolicyDescr,
       "cfprVnicSanConnPolicyFltAggr": cfprVnicSanConnPolicyFltAggr,
       "cfprVnicSanConnPolicyIntId": cfprVnicSanConnPolicyIntId,
       "cfprVnicSanConnPolicyName": cfprVnicSanConnPolicyName,
       "cfprVnicSanConnPolicyPolicyLevel": cfprVnicSanConnPolicyPolicyLevel,
       "cfprVnicSanConnPolicyPolicyOwner": cfprVnicSanConnPolicyPolicyOwner,
       "cfprVnicSanConnTemplTable": cfprVnicSanConnTemplTable,
       "cfprVnicSanConnTemplEntry": cfprVnicSanConnTemplEntry,
       "cfprVnicSanConnTemplInstanceId": cfprVnicSanConnTemplInstanceId,
       "cfprVnicSanConnTemplDn": cfprVnicSanConnTemplDn,
       "cfprVnicSanConnTemplRn": cfprVnicSanConnTemplRn,
       "cfprVnicSanConnTemplDescr": cfprVnicSanConnTemplDescr,
       "cfprVnicSanConnTemplIdentPoolName": cfprVnicSanConnTemplIdentPoolName,
       "cfprVnicSanConnTemplIntId": cfprVnicSanConnTemplIntId,
       "cfprVnicSanConnTemplMaxDataFieldSize": cfprVnicSanConnTemplMaxDataFieldSize,
       "cfprVnicSanConnTemplName": cfprVnicSanConnTemplName,
       "cfprVnicSanConnTemplNwCtrlPolicyName": cfprVnicSanConnTemplNwCtrlPolicyName,
       "cfprVnicSanConnTemplOperIdentPoolName": cfprVnicSanConnTemplOperIdentPoolName,
       "cfprVnicSanConnTemplOperQosPolicyName": cfprVnicSanConnTemplOperQosPolicyName,
       "cfprVnicSanConnTemplOperStatsPolicyName": cfprVnicSanConnTemplOperStatsPolicyName,
       "cfprVnicSanConnTemplPinToGroupName": cfprVnicSanConnTemplPinToGroupName,
       "cfprVnicSanConnTemplPolicyLevel": cfprVnicSanConnTemplPolicyLevel,
       "cfprVnicSanConnTemplPolicyOwner": cfprVnicSanConnTemplPolicyOwner,
       "cfprVnicSanConnTemplQosPolicyName": cfprVnicSanConnTemplQosPolicyName,
       "cfprVnicSanConnTemplStatsPolicyName": cfprVnicSanConnTemplStatsPolicyName,
       "cfprVnicSanConnTemplSwitchId": cfprVnicSanConnTemplSwitchId,
       "cfprVnicSanConnTemplTarget": cfprVnicSanConnTemplTarget,
       "cfprVnicSanConnTemplTemplType": cfprVnicSanConnTemplTemplType,
       "cfprVnicScsiTable": cfprVnicScsiTable,
       "cfprVnicScsiEntry": cfprVnicScsiEntry,
       "cfprVnicScsiInstanceId": cfprVnicScsiInstanceId,
       "cfprVnicScsiDn": cfprVnicScsiDn,
       "cfprVnicScsiRn": cfprVnicScsiRn,
       "cfprVnicScsiAdaptorProfileName": cfprVnicScsiAdaptorProfileName,
       "cfprVnicScsiAdminHostPort": cfprVnicScsiAdminHostPort,
       "cfprVnicScsiAdminVcon": cfprVnicScsiAdminVcon,
       "cfprVnicScsiAppRole": cfprVnicScsiAppRole,
       "cfprVnicScsiBootDev": cfprVnicScsiBootDev,
       "cfprVnicScsiConfigQualifier": cfprVnicScsiConfigQualifier,
       "cfprVnicScsiConfigState": cfprVnicScsiConfigState,
       "cfprVnicScsiEquipmentDn": cfprVnicScsiEquipmentDn,
       "cfprVnicScsiIdentPoolName": cfprVnicScsiIdentPoolName,
       "cfprVnicScsiInstType": cfprVnicScsiInstType,
       "cfprVnicScsiName": cfprVnicScsiName,
       "cfprVnicScsiNwTemplName": cfprVnicScsiNwTemplName,
       "cfprVnicScsiOperHostPort": cfprVnicScsiOperHostPort,
       "cfprVnicScsiOperOrder": cfprVnicScsiOperOrder,
       "cfprVnicScsiOperSpeed": cfprVnicScsiOperSpeed,
       "cfprVnicScsiOperStatsPolicyName": cfprVnicScsiOperStatsPolicyName,
       "cfprVnicScsiOperVcon": cfprVnicScsiOperVcon,
       "cfprVnicScsiOrder": cfprVnicScsiOrder,
       "cfprVnicScsiOwner": cfprVnicScsiOwner,
       "cfprVnicScsiPinToGroupName": cfprVnicScsiPinToGroupName,
       "cfprVnicScsiQosPolicyName": cfprVnicScsiQosPolicyName,
       "cfprVnicScsiStatsPolicyName": cfprVnicScsiStatsPolicyName,
       "cfprVnicScsiSwitchId": cfprVnicScsiSwitchId,
       "cfprVnicScsiType": cfprVnicScsiType,
       "cfprVnicScsiIfTable": cfprVnicScsiIfTable,
       "cfprVnicScsiIfEntry": cfprVnicScsiIfEntry,
       "cfprVnicScsiIfInstanceId": cfprVnicScsiIfInstanceId,
       "cfprVnicScsiIfDn": cfprVnicScsiIfDn,
       "cfprVnicScsiIfRn": cfprVnicScsiIfRn,
       "cfprVnicScsiIfAddr": cfprVnicScsiIfAddr,
       "cfprVnicScsiIfConfigQualifier": cfprVnicScsiIfConfigQualifier,
       "cfprVnicScsiIfName": cfprVnicScsiIfName,
       "cfprVnicScsiIfOperState": cfprVnicScsiIfOperState,
       "cfprVnicScsiIfOperVnetDn": cfprVnicScsiIfOperVnetDn,
       "cfprVnicScsiIfOperVnetName": cfprVnicScsiIfOperVnetName,
       "cfprVnicScsiIfOwner": cfprVnicScsiIfOwner,
       "cfprVnicScsiIfPubNwId": cfprVnicScsiIfPubNwId,
       "cfprVnicScsiIfSharing": cfprVnicScsiIfSharing,
       "cfprVnicScsiIfSwitchId": cfprVnicScsiIfSwitchId,
       "cfprVnicScsiIfType": cfprVnicScsiIfType,
       "cfprVnicScsiIfVnet": cfprVnicScsiIfVnet,
       "cfprVnicUsnicConPolicyTable": cfprVnicUsnicConPolicyTable,
       "cfprVnicUsnicConPolicyEntry": cfprVnicUsnicConPolicyEntry,
       "cfprVnicUsnicConPolicyInstanceId": cfprVnicUsnicConPolicyInstanceId,
       "cfprVnicUsnicConPolicyDn": cfprVnicUsnicConPolicyDn,
       "cfprVnicUsnicConPolicyRn": cfprVnicUsnicConPolicyRn,
       "cfprVnicUsnicConPolicyAdaptorProfileName": cfprVnicUsnicConPolicyAdaptorProfileName,
       "cfprVnicUsnicConPolicyDescr": cfprVnicUsnicConPolicyDescr,
       "cfprVnicUsnicConPolicyIntId": cfprVnicUsnicConPolicyIntId,
       "cfprVnicUsnicConPolicyName": cfprVnicUsnicConPolicyName,
       "cfprVnicUsnicConPolicyPolicyLevel": cfprVnicUsnicConPolicyPolicyLevel,
       "cfprVnicUsnicConPolicyPolicyOwner": cfprVnicUsnicConPolicyPolicyOwner,
       "cfprVnicUsnicConPolicyUsnicCount": cfprVnicUsnicConPolicyUsnicCount,
       "cfprVnicUsnicConPolicyRefTable": cfprVnicUsnicConPolicyRefTable,
       "cfprVnicUsnicConPolicyRefEntry": cfprVnicUsnicConPolicyRefEntry,
       "cfprVnicUsnicConPolicyRefInstanceId": cfprVnicUsnicConPolicyRefInstanceId,
       "cfprVnicUsnicConPolicyRefDn": cfprVnicUsnicConPolicyRefDn,
       "cfprVnicUsnicConPolicyRefRn": cfprVnicUsnicConPolicyRefRn,
       "cfprVnicUsnicConPolicyRefConPolicyName": cfprVnicUsnicConPolicyRefConPolicyName,
       "cfprVnicUsnicConPolicyRefOperConPolicyName": cfprVnicUsnicConPolicyRefOperConPolicyName,
       "cfprVnicVhbaBehPolicyTable": cfprVnicVhbaBehPolicyTable,
       "cfprVnicVhbaBehPolicyEntry": cfprVnicVhbaBehPolicyEntry,
       "cfprVnicVhbaBehPolicyInstanceId": cfprVnicVhbaBehPolicyInstanceId,
       "cfprVnicVhbaBehPolicyDn": cfprVnicVhbaBehPolicyDn,
       "cfprVnicVhbaBehPolicyRn": cfprVnicVhbaBehPolicyRn,
       "cfprVnicVhbaBehPolicyAction": cfprVnicVhbaBehPolicyAction,
       "cfprVnicVhbaBehPolicyDescr": cfprVnicVhbaBehPolicyDescr,
       "cfprVnicVhbaBehPolicyIntId": cfprVnicVhbaBehPolicyIntId,
       "cfprVnicVhbaBehPolicyName": cfprVnicVhbaBehPolicyName,
       "cfprVnicVhbaBehPolicyNwTemplName": cfprVnicVhbaBehPolicyNwTemplName,
       "cfprVnicVhbaBehPolicyPolicyLevel": cfprVnicVhbaBehPolicyPolicyLevel,
       "cfprVnicVhbaBehPolicyPolicyOwner": cfprVnicVhbaBehPolicyPolicyOwner,
       "cfprVnicVhbaBehPolicyType": cfprVnicVhbaBehPolicyType,
       "cfprVnicVlanTable": cfprVnicVlanTable,
       "cfprVnicVlanEntry": cfprVnicVlanEntry,
       "cfprVnicVlanInstanceId": cfprVnicVlanInstanceId,
       "cfprVnicVlanDn": cfprVnicVlanDn,
       "cfprVnicVlanRn": cfprVnicVlanRn,
       "cfprVnicVlanConfigQualifier": cfprVnicVlanConfigQualifier,
       "cfprVnicVlanFltAggr": cfprVnicVlanFltAggr,
       "cfprVnicVlanName": cfprVnicVlanName,
       "cfprVnicVlanOperState": cfprVnicVlanOperState,
       "cfprVnicVlanOperVnetDn": cfprVnicVlanOperVnetDn,
       "cfprVnicVlanOperVnetName": cfprVnicVlanOperVnetName,
       "cfprVnicVlanOwner": cfprVnicVlanOwner,
       "cfprVnicVlanPubNwId": cfprVnicVlanPubNwId,
       "cfprVnicVlanSharing": cfprVnicVlanSharing,
       "cfprVnicVlanSwitchId": cfprVnicVlanSwitchId,
       "cfprVnicVlanType": cfprVnicVlanType,
       "cfprVnicVlanVlanName": cfprVnicVlanVlanName,
       "cfprVnicVlanVnet": cfprVnicVlanVnet,
       "cfprVnicVmqConPolicyTable": cfprVnicVmqConPolicyTable,
       "cfprVnicVmqConPolicyEntry": cfprVnicVmqConPolicyEntry,
       "cfprVnicVmqConPolicyInstanceId": cfprVnicVmqConPolicyInstanceId,
       "cfprVnicVmqConPolicyDn": cfprVnicVmqConPolicyDn,
       "cfprVnicVmqConPolicyRn": cfprVnicVmqConPolicyRn,
       "cfprVnicVmqConPolicyDescr": cfprVnicVmqConPolicyDescr,
       "cfprVnicVmqConPolicyIntId": cfprVnicVmqConPolicyIntId,
       "cfprVnicVmqConPolicyIntrCount": cfprVnicVmqConPolicyIntrCount,
       "cfprVnicVmqConPolicyName": cfprVnicVmqConPolicyName,
       "cfprVnicVmqConPolicyPolicyLevel": cfprVnicVmqConPolicyPolicyLevel,
       "cfprVnicVmqConPolicyPolicyOwner": cfprVnicVmqConPolicyPolicyOwner,
       "cfprVnicVmqConPolicyVmqCount": cfprVnicVmqConPolicyVmqCount,
       "cfprVnicVmqConPolicyRefTable": cfprVnicVmqConPolicyRefTable,
       "cfprVnicVmqConPolicyRefEntry": cfprVnicVmqConPolicyRefEntry,
       "cfprVnicVmqConPolicyRefInstanceId": cfprVnicVmqConPolicyRefInstanceId,
       "cfprVnicVmqConPolicyRefDn": cfprVnicVmqConPolicyRefDn,
       "cfprVnicVmqConPolicyRefRn": cfprVnicVmqConPolicyRefRn,
       "cfprVnicVmqConPolicyRefConPolicyName": cfprVnicVmqConPolicyRefConPolicyName,
       "cfprVnicVmqConPolicyRefOperConPolicyName": cfprVnicVmqConPolicyRefOperConPolicyName,
       "cfprVnicVnicBehPolicyTable": cfprVnicVnicBehPolicyTable,
       "cfprVnicVnicBehPolicyEntry": cfprVnicVnicBehPolicyEntry,
       "cfprVnicVnicBehPolicyInstanceId": cfprVnicVnicBehPolicyInstanceId,
       "cfprVnicVnicBehPolicyDn": cfprVnicVnicBehPolicyDn,
       "cfprVnicVnicBehPolicyRn": cfprVnicVnicBehPolicyRn,
       "cfprVnicVnicBehPolicyAction": cfprVnicVnicBehPolicyAction,
       "cfprVnicVnicBehPolicyDescr": cfprVnicVnicBehPolicyDescr,
       "cfprVnicVnicBehPolicyIntId": cfprVnicVnicBehPolicyIntId,
       "cfprVnicVnicBehPolicyName": cfprVnicVnicBehPolicyName,
       "cfprVnicVnicBehPolicyNwTemplName": cfprVnicVnicBehPolicyNwTemplName,
       "cfprVnicVnicBehPolicyPolicyLevel": cfprVnicVnicBehPolicyPolicyLevel,
       "cfprVnicVnicBehPolicyPolicyOwner": cfprVnicVnicBehPolicyPolicyOwner,
       "cfprVnicVnicBehPolicyType": cfprVnicVnicBehPolicyType,
       "cfprVnicWwnnHistoryTable": cfprVnicWwnnHistoryTable,
       "cfprVnicWwnnHistoryEntry": cfprVnicWwnnHistoryEntry,
       "cfprVnicWwnnHistoryInstanceId": cfprVnicWwnnHistoryInstanceId,
       "cfprVnicWwnnHistoryDn": cfprVnicWwnnHistoryDn,
       "cfprVnicWwnnHistoryRn": cfprVnicWwnnHistoryRn,
       "cfprVnicWwnnHistoryOldwwnn": cfprVnicWwnnHistoryOldwwnn,
       "cfprVnicWwpnHistoryTable": cfprVnicWwpnHistoryTable,
       "cfprVnicWwpnHistoryEntry": cfprVnicWwpnHistoryEntry,
       "cfprVnicWwpnHistoryInstanceId": cfprVnicWwpnHistoryInstanceId,
       "cfprVnicWwpnHistoryDn": cfprVnicWwpnHistoryDn,
       "cfprVnicWwpnHistoryRn": cfprVnicWwpnHistoryRn,
       "cfprVnicWwpnHistoryOldaddr": cfprVnicWwpnHistoryOldaddr}
)
