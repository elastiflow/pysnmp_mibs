# SNMP MIB module (CISCO-FIREPOWER-AP-VNIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-VNIC-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:21:40 2025
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

(CfprApDpsecForgedTransmit,
 CfprApFabricHostPortId,
 CfprApFabricSSAPortType,
 CfprApFabricVlanSharingType,
 CfprApLsConfigState,
 CfprApNetworkSwitchId,
 CfprApNwctrlAdminState,
 CfprApNwctrlLinkFailAction,
 CfprApNwctrlRegistrationMode,
 CfprApPolicyPolicyOwner,
 CfprApVmMgmtPlane,
 CfprApVnicAEtherIfType,
 CfprApVnicAFcIfType,
 CfprApVnicAIpcIfType,
 CfprApVnicAScsiIfType,
 CfprApVnicAppRole,
 CfprApVnicConfigIssues,
 CfprApVnicConnectionOwner,
 CfprApVnicConnectionType,
 CfprApVnicDefBehType,
 CfprApVnicDefaultAction,
 CfprApVnicDynamicConReqProtection,
 CfprApVnicEtherBaseSwitchId,
 CfprApVnicEtherType,
 CfprApVnicExternalMgmtIPMode,
 CfprApVnicFcBasePersBind,
 CfprApVnicFcBaseType,
 CfprApVnicHostNwIOPerfPref,
 CfprApVnicIPv4DnsPref,
 CfprApVnicIScsiIfDefType,
 CfprApVnicIScsiNodeOwner,
 CfprApVnicIfOperState,
 CfprApVnicInstantiation,
 CfprApVnicIpcType,
 CfprApVnicL2IfSwitchId,
 CfprApVnicLanConnTemplSwitchId,
 CfprApVnicLunId,
 CfprApVnicPortProfileType,
 CfprApVnicProfileConfigQualifier,
 CfprApVnicSanConnTemplTarget,
 CfprApVnicScsiType,
 CfprApVnicTemplateTarget,
 CfprApVnicTemplateType,
 CfprApVnicVhbaBehPolicyType,
 CfprApVnicVirtualizationPreferenceType,
 CfprApVnicVnicBehPolicyType,
 CfprApVnicVnicBootDev,
 CfprApVnicVnicOperHostPort) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApDpsecForgedTransmit",
    "CfprApFabricHostPortId",
    "CfprApFabricSSAPortType",
    "CfprApFabricVlanSharingType",
    "CfprApLsConfigState",
    "CfprApNetworkSwitchId",
    "CfprApNwctrlAdminState",
    "CfprApNwctrlLinkFailAction",
    "CfprApNwctrlRegistrationMode",
    "CfprApPolicyPolicyOwner",
    "CfprApVmMgmtPlane",
    "CfprApVnicAEtherIfType",
    "CfprApVnicAFcIfType",
    "CfprApVnicAIpcIfType",
    "CfprApVnicAScsiIfType",
    "CfprApVnicAppRole",
    "CfprApVnicConfigIssues",
    "CfprApVnicConnectionOwner",
    "CfprApVnicConnectionType",
    "CfprApVnicDefBehType",
    "CfprApVnicDefaultAction",
    "CfprApVnicDynamicConReqProtection",
    "CfprApVnicEtherBaseSwitchId",
    "CfprApVnicEtherType",
    "CfprApVnicExternalMgmtIPMode",
    "CfprApVnicFcBasePersBind",
    "CfprApVnicFcBaseType",
    "CfprApVnicHostNwIOPerfPref",
    "CfprApVnicIPv4DnsPref",
    "CfprApVnicIScsiIfDefType",
    "CfprApVnicIScsiNodeOwner",
    "CfprApVnicIfOperState",
    "CfprApVnicInstantiation",
    "CfprApVnicIpcType",
    "CfprApVnicL2IfSwitchId",
    "CfprApVnicLanConnTemplSwitchId",
    "CfprApVnicLunId",
    "CfprApVnicPortProfileType",
    "CfprApVnicProfileConfigQualifier",
    "CfprApVnicSanConnTemplTarget",
    "CfprApVnicScsiType",
    "CfprApVnicTemplateTarget",
    "CfprApVnicTemplateType",
    "CfprApVnicVhbaBehPolicyType",
    "CfprApVnicVirtualizationPreferenceType",
    "CfprApVnicVnicBehPolicyType",
    "CfprApVnicVnicBootDev",
    "CfprApVnicVnicOperHostPort")

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

cfprApVnicObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApVnicBootIpPolicyTable_Object = MibTable
cfprApVnicBootIpPolicyTable = _CfprApVnicBootIpPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 1)
)
if mibBuilder.loadTexts:
    cfprApVnicBootIpPolicyTable.setStatus("current")
_CfprApVnicBootIpPolicyEntry_Object = MibTableRow
cfprApVnicBootIpPolicyEntry = _CfprApVnicBootIpPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 1, 1)
)
cfprApVnicBootIpPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicBootIpPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicBootIpPolicyEntry.setStatus("current")
_CfprApVnicBootIpPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApVnicBootIpPolicyInstanceId_Object = MibTableColumn
cfprApVnicBootIpPolicyInstanceId = _CfprApVnicBootIpPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 1, 1, 1),
    _CfprApVnicBootIpPolicyInstanceId_Type()
)
cfprApVnicBootIpPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicBootIpPolicyInstanceId.setStatus("current")
_CfprApVnicBootIpPolicyDn_Type = CfprApManagedObjectDn
_CfprApVnicBootIpPolicyDn_Object = MibTableColumn
cfprApVnicBootIpPolicyDn = _CfprApVnicBootIpPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 1, 1, 2),
    _CfprApVnicBootIpPolicyDn_Type()
)
cfprApVnicBootIpPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicBootIpPolicyDn.setStatus("current")
_CfprApVnicBootIpPolicyRn_Type = SnmpAdminString
_CfprApVnicBootIpPolicyRn_Object = MibTableColumn
cfprApVnicBootIpPolicyRn = _CfprApVnicBootIpPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 1, 1, 3),
    _CfprApVnicBootIpPolicyRn_Type()
)
cfprApVnicBootIpPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicBootIpPolicyRn.setStatus("current")
_CfprApVnicBootIpPolicyDescr_Type = SnmpAdminString
_CfprApVnicBootIpPolicyDescr_Object = MibTableColumn
cfprApVnicBootIpPolicyDescr = _CfprApVnicBootIpPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 1, 1, 4),
    _CfprApVnicBootIpPolicyDescr_Type()
)
cfprApVnicBootIpPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicBootIpPolicyDescr.setStatus("current")
_CfprApVnicBootIpPolicyIntId_Type = SnmpAdminString
_CfprApVnicBootIpPolicyIntId_Object = MibTableColumn
cfprApVnicBootIpPolicyIntId = _CfprApVnicBootIpPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 1, 1, 5),
    _CfprApVnicBootIpPolicyIntId_Type()
)
cfprApVnicBootIpPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicBootIpPolicyIntId.setStatus("current")
_CfprApVnicBootIpPolicyName_Type = SnmpAdminString
_CfprApVnicBootIpPolicyName_Object = MibTableColumn
cfprApVnicBootIpPolicyName = _CfprApVnicBootIpPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 1, 1, 6),
    _CfprApVnicBootIpPolicyName_Type()
)
cfprApVnicBootIpPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicBootIpPolicyName.setStatus("current")
_CfprApVnicBootIpPolicyPolicyLevel_Type = Gauge32
_CfprApVnicBootIpPolicyPolicyLevel_Object = MibTableColumn
cfprApVnicBootIpPolicyPolicyLevel = _CfprApVnicBootIpPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 1, 1, 7),
    _CfprApVnicBootIpPolicyPolicyLevel_Type()
)
cfprApVnicBootIpPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicBootIpPolicyPolicyLevel.setStatus("current")
_CfprApVnicBootIpPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApVnicBootIpPolicyPolicyOwner_Object = MibTableColumn
cfprApVnicBootIpPolicyPolicyOwner = _CfprApVnicBootIpPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 1, 1, 8),
    _CfprApVnicBootIpPolicyPolicyOwner_Type()
)
cfprApVnicBootIpPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicBootIpPolicyPolicyOwner.setStatus("current")
_CfprApVnicBootIpPolicyPoolName_Type = SnmpAdminString
_CfprApVnicBootIpPolicyPoolName_Object = MibTableColumn
cfprApVnicBootIpPolicyPoolName = _CfprApVnicBootIpPolicyPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 1, 1, 9),
    _CfprApVnicBootIpPolicyPoolName_Type()
)
cfprApVnicBootIpPolicyPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicBootIpPolicyPoolName.setStatus("current")
_CfprApVnicBootTargetTable_Object = MibTable
cfprApVnicBootTargetTable = _CfprApVnicBootTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 2)
)
if mibBuilder.loadTexts:
    cfprApVnicBootTargetTable.setStatus("current")
_CfprApVnicBootTargetEntry_Object = MibTableRow
cfprApVnicBootTargetEntry = _CfprApVnicBootTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 2, 1)
)
cfprApVnicBootTargetEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicBootTargetInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicBootTargetEntry.setStatus("current")
_CfprApVnicBootTargetInstanceId_Type = CfprApManagedObjectId
_CfprApVnicBootTargetInstanceId_Object = MibTableColumn
cfprApVnicBootTargetInstanceId = _CfprApVnicBootTargetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 2, 1, 1),
    _CfprApVnicBootTargetInstanceId_Type()
)
cfprApVnicBootTargetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicBootTargetInstanceId.setStatus("current")
_CfprApVnicBootTargetDn_Type = CfprApManagedObjectDn
_CfprApVnicBootTargetDn_Object = MibTableColumn
cfprApVnicBootTargetDn = _CfprApVnicBootTargetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 2, 1, 2),
    _CfprApVnicBootTargetDn_Type()
)
cfprApVnicBootTargetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicBootTargetDn.setStatus("current")
_CfprApVnicBootTargetRn_Type = SnmpAdminString
_CfprApVnicBootTargetRn_Object = MibTableColumn
cfprApVnicBootTargetRn = _CfprApVnicBootTargetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 2, 1, 3),
    _CfprApVnicBootTargetRn_Type()
)
cfprApVnicBootTargetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicBootTargetRn.setStatus("current")
_CfprApVnicBootTargetLun_Type = SnmpAdminString
_CfprApVnicBootTargetLun_Object = MibTableColumn
cfprApVnicBootTargetLun = _CfprApVnicBootTargetLun_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 2, 1, 4),
    _CfprApVnicBootTargetLun_Type()
)
cfprApVnicBootTargetLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicBootTargetLun.setStatus("current")
_CfprApVnicBootTargetWwn_Type = Unsigned64
_CfprApVnicBootTargetWwn_Object = MibTableColumn
cfprApVnicBootTargetWwn = _CfprApVnicBootTargetWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 2, 1, 5),
    _CfprApVnicBootTargetWwn_Type()
)
cfprApVnicBootTargetWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicBootTargetWwn.setStatus("current")
_CfprApVnicConnDefTable_Object = MibTable
cfprApVnicConnDefTable = _CfprApVnicConnDefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 3)
)
if mibBuilder.loadTexts:
    cfprApVnicConnDefTable.setStatus("current")
_CfprApVnicConnDefEntry_Object = MibTableRow
cfprApVnicConnDefEntry = _CfprApVnicConnDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 3, 1)
)
cfprApVnicConnDefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicConnDefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicConnDefEntry.setStatus("current")
_CfprApVnicConnDefInstanceId_Type = CfprApManagedObjectId
_CfprApVnicConnDefInstanceId_Object = MibTableColumn
cfprApVnicConnDefInstanceId = _CfprApVnicConnDefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 3, 1, 1),
    _CfprApVnicConnDefInstanceId_Type()
)
cfprApVnicConnDefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicConnDefInstanceId.setStatus("current")
_CfprApVnicConnDefDn_Type = CfprApManagedObjectDn
_CfprApVnicConnDefDn_Object = MibTableColumn
cfprApVnicConnDefDn = _CfprApVnicConnDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 3, 1, 2),
    _CfprApVnicConnDefDn_Type()
)
cfprApVnicConnDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicConnDefDn.setStatus("current")
_CfprApVnicConnDefRn_Type = SnmpAdminString
_CfprApVnicConnDefRn_Object = MibTableColumn
cfprApVnicConnDefRn = _CfprApVnicConnDefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 3, 1, 3),
    _CfprApVnicConnDefRn_Type()
)
cfprApVnicConnDefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicConnDefRn.setStatus("current")
_CfprApVnicConnDefFltAggr_Type = Unsigned64
_CfprApVnicConnDefFltAggr_Object = MibTableColumn
cfprApVnicConnDefFltAggr = _CfprApVnicConnDefFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 3, 1, 4),
    _CfprApVnicConnDefFltAggr_Type()
)
cfprApVnicConnDefFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicConnDefFltAggr.setStatus("current")
_CfprApVnicConnDefLanConnPolicyName_Type = SnmpAdminString
_CfprApVnicConnDefLanConnPolicyName_Object = MibTableColumn
cfprApVnicConnDefLanConnPolicyName = _CfprApVnicConnDefLanConnPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 3, 1, 5),
    _CfprApVnicConnDefLanConnPolicyName_Type()
)
cfprApVnicConnDefLanConnPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicConnDefLanConnPolicyName.setStatus("current")
_CfprApVnicConnDefOperLanConnPolicyName_Type = SnmpAdminString
_CfprApVnicConnDefOperLanConnPolicyName_Object = MibTableColumn
cfprApVnicConnDefOperLanConnPolicyName = _CfprApVnicConnDefOperLanConnPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 3, 1, 6),
    _CfprApVnicConnDefOperLanConnPolicyName_Type()
)
cfprApVnicConnDefOperLanConnPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicConnDefOperLanConnPolicyName.setStatus("current")
_CfprApVnicDefBehTable_Object = MibTable
cfprApVnicDefBehTable = _CfprApVnicDefBehTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 4)
)
if mibBuilder.loadTexts:
    cfprApVnicDefBehTable.setStatus("current")
_CfprApVnicDefBehEntry_Object = MibTableRow
cfprApVnicDefBehEntry = _CfprApVnicDefBehEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 4, 1)
)
cfprApVnicDefBehEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicDefBehInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicDefBehEntry.setStatus("current")
_CfprApVnicDefBehInstanceId_Type = CfprApManagedObjectId
_CfprApVnicDefBehInstanceId_Object = MibTableColumn
cfprApVnicDefBehInstanceId = _CfprApVnicDefBehInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 4, 1, 1),
    _CfprApVnicDefBehInstanceId_Type()
)
cfprApVnicDefBehInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicDefBehInstanceId.setStatus("current")
_CfprApVnicDefBehDn_Type = CfprApManagedObjectDn
_CfprApVnicDefBehDn_Object = MibTableColumn
cfprApVnicDefBehDn = _CfprApVnicDefBehDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 4, 1, 2),
    _CfprApVnicDefBehDn_Type()
)
cfprApVnicDefBehDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDefBehDn.setStatus("current")
_CfprApVnicDefBehRn_Type = SnmpAdminString
_CfprApVnicDefBehRn_Object = MibTableColumn
cfprApVnicDefBehRn = _CfprApVnicDefBehRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 4, 1, 3),
    _CfprApVnicDefBehRn_Type()
)
cfprApVnicDefBehRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDefBehRn.setStatus("current")
_CfprApVnicDefBehAction_Type = CfprApVnicDefaultAction
_CfprApVnicDefBehAction_Object = MibTableColumn
cfprApVnicDefBehAction = _CfprApVnicDefBehAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 4, 1, 4),
    _CfprApVnicDefBehAction_Type()
)
cfprApVnicDefBehAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDefBehAction.setStatus("current")
_CfprApVnicDefBehDescr_Type = SnmpAdminString
_CfprApVnicDefBehDescr_Object = MibTableColumn
cfprApVnicDefBehDescr = _CfprApVnicDefBehDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 4, 1, 5),
    _CfprApVnicDefBehDescr_Type()
)
cfprApVnicDefBehDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDefBehDescr.setStatus("current")
_CfprApVnicDefBehIntId_Type = SnmpAdminString
_CfprApVnicDefBehIntId_Object = MibTableColumn
cfprApVnicDefBehIntId = _CfprApVnicDefBehIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 4, 1, 6),
    _CfprApVnicDefBehIntId_Type()
)
cfprApVnicDefBehIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDefBehIntId.setStatus("current")
_CfprApVnicDefBehName_Type = SnmpAdminString
_CfprApVnicDefBehName_Object = MibTableColumn
cfprApVnicDefBehName = _CfprApVnicDefBehName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 4, 1, 7),
    _CfprApVnicDefBehName_Type()
)
cfprApVnicDefBehName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDefBehName.setStatus("current")
_CfprApVnicDefBehNwTemplName_Type = SnmpAdminString
_CfprApVnicDefBehNwTemplName_Object = MibTableColumn
cfprApVnicDefBehNwTemplName = _CfprApVnicDefBehNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 4, 1, 8),
    _CfprApVnicDefBehNwTemplName_Type()
)
cfprApVnicDefBehNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDefBehNwTemplName.setStatus("current")
_CfprApVnicDefBehPolicyLevel_Type = Gauge32
_CfprApVnicDefBehPolicyLevel_Object = MibTableColumn
cfprApVnicDefBehPolicyLevel = _CfprApVnicDefBehPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 4, 1, 9),
    _CfprApVnicDefBehPolicyLevel_Type()
)
cfprApVnicDefBehPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDefBehPolicyLevel.setStatus("current")
_CfprApVnicDefBehPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApVnicDefBehPolicyOwner_Object = MibTableColumn
cfprApVnicDefBehPolicyOwner = _CfprApVnicDefBehPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 4, 1, 10),
    _CfprApVnicDefBehPolicyOwner_Type()
)
cfprApVnicDefBehPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDefBehPolicyOwner.setStatus("current")
_CfprApVnicDefBehType_Type = CfprApVnicDefBehType
_CfprApVnicDefBehType_Object = MibTableColumn
cfprApVnicDefBehType = _CfprApVnicDefBehType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 4, 1, 11),
    _CfprApVnicDefBehType_Type()
)
cfprApVnicDefBehType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDefBehType.setStatus("current")
_CfprApVnicDynamicConTable_Object = MibTable
cfprApVnicDynamicConTable = _CfprApVnicDynamicConTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 5)
)
if mibBuilder.loadTexts:
    cfprApVnicDynamicConTable.setStatus("current")
_CfprApVnicDynamicConEntry_Object = MibTableRow
cfprApVnicDynamicConEntry = _CfprApVnicDynamicConEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 5, 1)
)
cfprApVnicDynamicConEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicDynamicConInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicDynamicConEntry.setStatus("current")
_CfprApVnicDynamicConInstanceId_Type = CfprApManagedObjectId
_CfprApVnicDynamicConInstanceId_Object = MibTableColumn
cfprApVnicDynamicConInstanceId = _CfprApVnicDynamicConInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 5, 1, 1),
    _CfprApVnicDynamicConInstanceId_Type()
)
cfprApVnicDynamicConInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicDynamicConInstanceId.setStatus("current")
_CfprApVnicDynamicConDn_Type = CfprApManagedObjectDn
_CfprApVnicDynamicConDn_Object = MibTableColumn
cfprApVnicDynamicConDn = _CfprApVnicDynamicConDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 5, 1, 2),
    _CfprApVnicDynamicConDn_Type()
)
cfprApVnicDynamicConDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicConDn.setStatus("current")
_CfprApVnicDynamicConRn_Type = SnmpAdminString
_CfprApVnicDynamicConRn_Object = MibTableColumn
cfprApVnicDynamicConRn = _CfprApVnicDynamicConRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 5, 1, 3),
    _CfprApVnicDynamicConRn_Type()
)
cfprApVnicDynamicConRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicConRn.setStatus("current")
_CfprApVnicDynamicConAdaptorProfileName_Type = SnmpAdminString
_CfprApVnicDynamicConAdaptorProfileName_Object = MibTableColumn
cfprApVnicDynamicConAdaptorProfileName = _CfprApVnicDynamicConAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 5, 1, 4),
    _CfprApVnicDynamicConAdaptorProfileName_Type()
)
cfprApVnicDynamicConAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicConAdaptorProfileName.setStatus("current")
_CfprApVnicDynamicConDescr_Type = SnmpAdminString
_CfprApVnicDynamicConDescr_Object = MibTableColumn
cfprApVnicDynamicConDescr = _CfprApVnicDynamicConDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 5, 1, 5),
    _CfprApVnicDynamicConDescr_Type()
)
cfprApVnicDynamicConDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicConDescr.setStatus("current")
_CfprApVnicDynamicConDynamicEth_Type = Gauge32
_CfprApVnicDynamicConDynamicEth_Object = MibTableColumn
cfprApVnicDynamicConDynamicEth = _CfprApVnicDynamicConDynamicEth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 5, 1, 6),
    _CfprApVnicDynamicConDynamicEth_Type()
)
cfprApVnicDynamicConDynamicEth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicConDynamicEth.setStatus("current")
_CfprApVnicDynamicConIntId_Type = SnmpAdminString
_CfprApVnicDynamicConIntId_Object = MibTableColumn
cfprApVnicDynamicConIntId = _CfprApVnicDynamicConIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 5, 1, 7),
    _CfprApVnicDynamicConIntId_Type()
)
cfprApVnicDynamicConIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicConIntId.setStatus("current")
_CfprApVnicDynamicConMtu_Type = Gauge32
_CfprApVnicDynamicConMtu_Object = MibTableColumn
cfprApVnicDynamicConMtu = _CfprApVnicDynamicConMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 5, 1, 8),
    _CfprApVnicDynamicConMtu_Type()
)
cfprApVnicDynamicConMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicConMtu.setStatus("current")
_CfprApVnicDynamicConName_Type = SnmpAdminString
_CfprApVnicDynamicConName_Object = MibTableColumn
cfprApVnicDynamicConName = _CfprApVnicDynamicConName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 5, 1, 9),
    _CfprApVnicDynamicConName_Type()
)
cfprApVnicDynamicConName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicConName.setStatus("current")
_CfprApVnicDynamicConNamingPrefix_Type = SnmpAdminString
_CfprApVnicDynamicConNamingPrefix_Object = MibTableColumn
cfprApVnicDynamicConNamingPrefix = _CfprApVnicDynamicConNamingPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 5, 1, 10),
    _CfprApVnicDynamicConNamingPrefix_Type()
)
cfprApVnicDynamicConNamingPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicConNamingPrefix.setStatus("current")
_CfprApVnicDynamicConPolicyLevel_Type = Gauge32
_CfprApVnicDynamicConPolicyLevel_Object = MibTableColumn
cfprApVnicDynamicConPolicyLevel = _CfprApVnicDynamicConPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 5, 1, 11),
    _CfprApVnicDynamicConPolicyLevel_Type()
)
cfprApVnicDynamicConPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicConPolicyLevel.setStatus("current")
_CfprApVnicDynamicConPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApVnicDynamicConPolicyOwner_Object = MibTableColumn
cfprApVnicDynamicConPolicyOwner = _CfprApVnicDynamicConPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 5, 1, 12),
    _CfprApVnicDynamicConPolicyOwner_Type()
)
cfprApVnicDynamicConPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicConPolicyOwner.setStatus("current")
_CfprApVnicDynamicConProtection_Type = CfprApVnicDynamicConReqProtection
_CfprApVnicDynamicConProtection_Object = MibTableColumn
cfprApVnicDynamicConProtection = _CfprApVnicDynamicConProtection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 5, 1, 13),
    _CfprApVnicDynamicConProtection_Type()
)
cfprApVnicDynamicConProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicConProtection.setStatus("current")
_CfprApVnicDynamicConPolicyTable_Object = MibTable
cfprApVnicDynamicConPolicyTable = _CfprApVnicDynamicConPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 6)
)
if mibBuilder.loadTexts:
    cfprApVnicDynamicConPolicyTable.setStatus("current")
_CfprApVnicDynamicConPolicyEntry_Object = MibTableRow
cfprApVnicDynamicConPolicyEntry = _CfprApVnicDynamicConPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 6, 1)
)
cfprApVnicDynamicConPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicDynamicConPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicDynamicConPolicyEntry.setStatus("current")
_CfprApVnicDynamicConPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApVnicDynamicConPolicyInstanceId_Object = MibTableColumn
cfprApVnicDynamicConPolicyInstanceId = _CfprApVnicDynamicConPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 6, 1, 1),
    _CfprApVnicDynamicConPolicyInstanceId_Type()
)
cfprApVnicDynamicConPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicDynamicConPolicyInstanceId.setStatus("current")
_CfprApVnicDynamicConPolicyDn_Type = CfprApManagedObjectDn
_CfprApVnicDynamicConPolicyDn_Object = MibTableColumn
cfprApVnicDynamicConPolicyDn = _CfprApVnicDynamicConPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 6, 1, 2),
    _CfprApVnicDynamicConPolicyDn_Type()
)
cfprApVnicDynamicConPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicConPolicyDn.setStatus("current")
_CfprApVnicDynamicConPolicyRn_Type = SnmpAdminString
_CfprApVnicDynamicConPolicyRn_Object = MibTableColumn
cfprApVnicDynamicConPolicyRn = _CfprApVnicDynamicConPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 6, 1, 3),
    _CfprApVnicDynamicConPolicyRn_Type()
)
cfprApVnicDynamicConPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicConPolicyRn.setStatus("current")
_CfprApVnicDynamicConPolicyAdaptorProfileName_Type = SnmpAdminString
_CfprApVnicDynamicConPolicyAdaptorProfileName_Object = MibTableColumn
cfprApVnicDynamicConPolicyAdaptorProfileName = _CfprApVnicDynamicConPolicyAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 6, 1, 4),
    _CfprApVnicDynamicConPolicyAdaptorProfileName_Type()
)
cfprApVnicDynamicConPolicyAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicConPolicyAdaptorProfileName.setStatus("current")
_CfprApVnicDynamicConPolicyDescr_Type = SnmpAdminString
_CfprApVnicDynamicConPolicyDescr_Object = MibTableColumn
cfprApVnicDynamicConPolicyDescr = _CfprApVnicDynamicConPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 6, 1, 5),
    _CfprApVnicDynamicConPolicyDescr_Type()
)
cfprApVnicDynamicConPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicConPolicyDescr.setStatus("current")
_CfprApVnicDynamicConPolicyDynamicEth_Type = Gauge32
_CfprApVnicDynamicConPolicyDynamicEth_Object = MibTableColumn
cfprApVnicDynamicConPolicyDynamicEth = _CfprApVnicDynamicConPolicyDynamicEth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 6, 1, 6),
    _CfprApVnicDynamicConPolicyDynamicEth_Type()
)
cfprApVnicDynamicConPolicyDynamicEth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicConPolicyDynamicEth.setStatus("current")
_CfprApVnicDynamicConPolicyIntId_Type = SnmpAdminString
_CfprApVnicDynamicConPolicyIntId_Object = MibTableColumn
cfprApVnicDynamicConPolicyIntId = _CfprApVnicDynamicConPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 6, 1, 7),
    _CfprApVnicDynamicConPolicyIntId_Type()
)
cfprApVnicDynamicConPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicConPolicyIntId.setStatus("current")
_CfprApVnicDynamicConPolicyMtu_Type = Gauge32
_CfprApVnicDynamicConPolicyMtu_Object = MibTableColumn
cfprApVnicDynamicConPolicyMtu = _CfprApVnicDynamicConPolicyMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 6, 1, 8),
    _CfprApVnicDynamicConPolicyMtu_Type()
)
cfprApVnicDynamicConPolicyMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicConPolicyMtu.setStatus("current")
_CfprApVnicDynamicConPolicyName_Type = SnmpAdminString
_CfprApVnicDynamicConPolicyName_Object = MibTableColumn
cfprApVnicDynamicConPolicyName = _CfprApVnicDynamicConPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 6, 1, 9),
    _CfprApVnicDynamicConPolicyName_Type()
)
cfprApVnicDynamicConPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicConPolicyName.setStatus("current")
_CfprApVnicDynamicConPolicyNamingPrefix_Type = SnmpAdminString
_CfprApVnicDynamicConPolicyNamingPrefix_Object = MibTableColumn
cfprApVnicDynamicConPolicyNamingPrefix = _CfprApVnicDynamicConPolicyNamingPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 6, 1, 10),
    _CfprApVnicDynamicConPolicyNamingPrefix_Type()
)
cfprApVnicDynamicConPolicyNamingPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicConPolicyNamingPrefix.setStatus("current")
_CfprApVnicDynamicConPolicyPolicyLevel_Type = Gauge32
_CfprApVnicDynamicConPolicyPolicyLevel_Object = MibTableColumn
cfprApVnicDynamicConPolicyPolicyLevel = _CfprApVnicDynamicConPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 6, 1, 11),
    _CfprApVnicDynamicConPolicyPolicyLevel_Type()
)
cfprApVnicDynamicConPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicConPolicyPolicyLevel.setStatus("current")
_CfprApVnicDynamicConPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApVnicDynamicConPolicyPolicyOwner_Object = MibTableColumn
cfprApVnicDynamicConPolicyPolicyOwner = _CfprApVnicDynamicConPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 6, 1, 12),
    _CfprApVnicDynamicConPolicyPolicyOwner_Type()
)
cfprApVnicDynamicConPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicConPolicyPolicyOwner.setStatus("current")
_CfprApVnicDynamicConPolicyProtection_Type = CfprApVnicDynamicConReqProtection
_CfprApVnicDynamicConPolicyProtection_Object = MibTableColumn
cfprApVnicDynamicConPolicyProtection = _CfprApVnicDynamicConPolicyProtection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 6, 1, 13),
    _CfprApVnicDynamicConPolicyProtection_Type()
)
cfprApVnicDynamicConPolicyProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicConPolicyProtection.setStatus("current")
_CfprApVnicDynamicConPolicyRefTable_Object = MibTable
cfprApVnicDynamicConPolicyRefTable = _CfprApVnicDynamicConPolicyRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 7)
)
if mibBuilder.loadTexts:
    cfprApVnicDynamicConPolicyRefTable.setStatus("current")
_CfprApVnicDynamicConPolicyRefEntry_Object = MibTableRow
cfprApVnicDynamicConPolicyRefEntry = _CfprApVnicDynamicConPolicyRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 7, 1)
)
cfprApVnicDynamicConPolicyRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicDynamicConPolicyRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicDynamicConPolicyRefEntry.setStatus("current")
_CfprApVnicDynamicConPolicyRefInstanceId_Type = CfprApManagedObjectId
_CfprApVnicDynamicConPolicyRefInstanceId_Object = MibTableColumn
cfprApVnicDynamicConPolicyRefInstanceId = _CfprApVnicDynamicConPolicyRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 7, 1, 1),
    _CfprApVnicDynamicConPolicyRefInstanceId_Type()
)
cfprApVnicDynamicConPolicyRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicDynamicConPolicyRefInstanceId.setStatus("current")
_CfprApVnicDynamicConPolicyRefDn_Type = CfprApManagedObjectDn
_CfprApVnicDynamicConPolicyRefDn_Object = MibTableColumn
cfprApVnicDynamicConPolicyRefDn = _CfprApVnicDynamicConPolicyRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 7, 1, 2),
    _CfprApVnicDynamicConPolicyRefDn_Type()
)
cfprApVnicDynamicConPolicyRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicConPolicyRefDn.setStatus("current")
_CfprApVnicDynamicConPolicyRefRn_Type = SnmpAdminString
_CfprApVnicDynamicConPolicyRefRn_Object = MibTableColumn
cfprApVnicDynamicConPolicyRefRn = _CfprApVnicDynamicConPolicyRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 7, 1, 3),
    _CfprApVnicDynamicConPolicyRefRn_Type()
)
cfprApVnicDynamicConPolicyRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicConPolicyRefRn.setStatus("current")
_CfprApVnicDynamicConPolicyRefConPolicyName_Type = SnmpAdminString
_CfprApVnicDynamicConPolicyRefConPolicyName_Object = MibTableColumn
cfprApVnicDynamicConPolicyRefConPolicyName = _CfprApVnicDynamicConPolicyRefConPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 7, 1, 4),
    _CfprApVnicDynamicConPolicyRefConPolicyName_Type()
)
cfprApVnicDynamicConPolicyRefConPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicConPolicyRefConPolicyName.setStatus("current")
_CfprApVnicDynamicConPolicyRefOperConPolicyName_Type = SnmpAdminString
_CfprApVnicDynamicConPolicyRefOperConPolicyName_Object = MibTableColumn
cfprApVnicDynamicConPolicyRefOperConPolicyName = _CfprApVnicDynamicConPolicyRefOperConPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 7, 1, 5),
    _CfprApVnicDynamicConPolicyRefOperConPolicyName_Type()
)
cfprApVnicDynamicConPolicyRefOperConPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicConPolicyRefOperConPolicyName.setStatus("current")
_CfprApVnicDynamicIdUniverseTable_Object = MibTable
cfprApVnicDynamicIdUniverseTable = _CfprApVnicDynamicIdUniverseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 8)
)
if mibBuilder.loadTexts:
    cfprApVnicDynamicIdUniverseTable.setStatus("current")
_CfprApVnicDynamicIdUniverseEntry_Object = MibTableRow
cfprApVnicDynamicIdUniverseEntry = _CfprApVnicDynamicIdUniverseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 8, 1)
)
cfprApVnicDynamicIdUniverseEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicDynamicIdUniverseInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicDynamicIdUniverseEntry.setStatus("current")
_CfprApVnicDynamicIdUniverseInstanceId_Type = CfprApManagedObjectId
_CfprApVnicDynamicIdUniverseInstanceId_Object = MibTableColumn
cfprApVnicDynamicIdUniverseInstanceId = _CfprApVnicDynamicIdUniverseInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 8, 1, 1),
    _CfprApVnicDynamicIdUniverseInstanceId_Type()
)
cfprApVnicDynamicIdUniverseInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicDynamicIdUniverseInstanceId.setStatus("current")
_CfprApVnicDynamicIdUniverseDn_Type = CfprApManagedObjectDn
_CfprApVnicDynamicIdUniverseDn_Object = MibTableColumn
cfprApVnicDynamicIdUniverseDn = _CfprApVnicDynamicIdUniverseDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 8, 1, 2),
    _CfprApVnicDynamicIdUniverseDn_Type()
)
cfprApVnicDynamicIdUniverseDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicIdUniverseDn.setStatus("current")
_CfprApVnicDynamicIdUniverseRn_Type = SnmpAdminString
_CfprApVnicDynamicIdUniverseRn_Object = MibTableColumn
cfprApVnicDynamicIdUniverseRn = _CfprApVnicDynamicIdUniverseRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 8, 1, 3),
    _CfprApVnicDynamicIdUniverseRn_Type()
)
cfprApVnicDynamicIdUniverseRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicIdUniverseRn.setStatus("current")
_CfprApVnicDynamicIdUniverseDescr_Type = SnmpAdminString
_CfprApVnicDynamicIdUniverseDescr_Object = MibTableColumn
cfprApVnicDynamicIdUniverseDescr = _CfprApVnicDynamicIdUniverseDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 8, 1, 4),
    _CfprApVnicDynamicIdUniverseDescr_Type()
)
cfprApVnicDynamicIdUniverseDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicIdUniverseDescr.setStatus("current")
_CfprApVnicDynamicIdUniverseIntId_Type = SnmpAdminString
_CfprApVnicDynamicIdUniverseIntId_Object = MibTableColumn
cfprApVnicDynamicIdUniverseIntId = _CfprApVnicDynamicIdUniverseIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 8, 1, 5),
    _CfprApVnicDynamicIdUniverseIntId_Type()
)
cfprApVnicDynamicIdUniverseIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicIdUniverseIntId.setStatus("current")
_CfprApVnicDynamicIdUniverseName_Type = SnmpAdminString
_CfprApVnicDynamicIdUniverseName_Object = MibTableColumn
cfprApVnicDynamicIdUniverseName = _CfprApVnicDynamicIdUniverseName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 8, 1, 6),
    _CfprApVnicDynamicIdUniverseName_Type()
)
cfprApVnicDynamicIdUniverseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicIdUniverseName.setStatus("current")
_CfprApVnicDynamicIdUniversePolicyLevel_Type = Gauge32
_CfprApVnicDynamicIdUniversePolicyLevel_Object = MibTableColumn
cfprApVnicDynamicIdUniversePolicyLevel = _CfprApVnicDynamicIdUniversePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 8, 1, 7),
    _CfprApVnicDynamicIdUniversePolicyLevel_Type()
)
cfprApVnicDynamicIdUniversePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicIdUniversePolicyLevel.setStatus("current")
_CfprApVnicDynamicIdUniversePolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApVnicDynamicIdUniversePolicyOwner_Object = MibTableColumn
cfprApVnicDynamicIdUniversePolicyOwner = _CfprApVnicDynamicIdUniversePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 8, 1, 8),
    _CfprApVnicDynamicIdUniversePolicyOwner_Type()
)
cfprApVnicDynamicIdUniversePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicIdUniversePolicyOwner.setStatus("current")
_CfprApVnicDynamicProviderTable_Object = MibTable
cfprApVnicDynamicProviderTable = _CfprApVnicDynamicProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 9)
)
if mibBuilder.loadTexts:
    cfprApVnicDynamicProviderTable.setStatus("current")
_CfprApVnicDynamicProviderEntry_Object = MibTableRow
cfprApVnicDynamicProviderEntry = _CfprApVnicDynamicProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 9, 1)
)
cfprApVnicDynamicProviderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicDynamicProviderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicDynamicProviderEntry.setStatus("current")
_CfprApVnicDynamicProviderInstanceId_Type = CfprApManagedObjectId
_CfprApVnicDynamicProviderInstanceId_Object = MibTableColumn
cfprApVnicDynamicProviderInstanceId = _CfprApVnicDynamicProviderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 9, 1, 1),
    _CfprApVnicDynamicProviderInstanceId_Type()
)
cfprApVnicDynamicProviderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicDynamicProviderInstanceId.setStatus("current")
_CfprApVnicDynamicProviderDn_Type = CfprApManagedObjectDn
_CfprApVnicDynamicProviderDn_Object = MibTableColumn
cfprApVnicDynamicProviderDn = _CfprApVnicDynamicProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 9, 1, 2),
    _CfprApVnicDynamicProviderDn_Type()
)
cfprApVnicDynamicProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicProviderDn.setStatus("current")
_CfprApVnicDynamicProviderRn_Type = SnmpAdminString
_CfprApVnicDynamicProviderRn_Object = MibTableColumn
cfprApVnicDynamicProviderRn = _CfprApVnicDynamicProviderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 9, 1, 3),
    _CfprApVnicDynamicProviderRn_Type()
)
cfprApVnicDynamicProviderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicProviderRn.setStatus("current")
_CfprApVnicDynamicProviderName_Type = SnmpAdminString
_CfprApVnicDynamicProviderName_Object = MibTableColumn
cfprApVnicDynamicProviderName = _CfprApVnicDynamicProviderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 9, 1, 4),
    _CfprApVnicDynamicProviderName_Type()
)
cfprApVnicDynamicProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicProviderName.setStatus("current")
_CfprApVnicDynamicProviderEpTable_Object = MibTable
cfprApVnicDynamicProviderEpTable = _CfprApVnicDynamicProviderEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 10)
)
if mibBuilder.loadTexts:
    cfprApVnicDynamicProviderEpTable.setStatus("current")
_CfprApVnicDynamicProviderEpEntry_Object = MibTableRow
cfprApVnicDynamicProviderEpEntry = _CfprApVnicDynamicProviderEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 10, 1)
)
cfprApVnicDynamicProviderEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicDynamicProviderEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicDynamicProviderEpEntry.setStatus("current")
_CfprApVnicDynamicProviderEpInstanceId_Type = CfprApManagedObjectId
_CfprApVnicDynamicProviderEpInstanceId_Object = MibTableColumn
cfprApVnicDynamicProviderEpInstanceId = _CfprApVnicDynamicProviderEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 10, 1, 1),
    _CfprApVnicDynamicProviderEpInstanceId_Type()
)
cfprApVnicDynamicProviderEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicDynamicProviderEpInstanceId.setStatus("current")
_CfprApVnicDynamicProviderEpDn_Type = CfprApManagedObjectDn
_CfprApVnicDynamicProviderEpDn_Object = MibTableColumn
cfprApVnicDynamicProviderEpDn = _CfprApVnicDynamicProviderEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 10, 1, 2),
    _CfprApVnicDynamicProviderEpDn_Type()
)
cfprApVnicDynamicProviderEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicProviderEpDn.setStatus("current")
_CfprApVnicDynamicProviderEpRn_Type = SnmpAdminString
_CfprApVnicDynamicProviderEpRn_Object = MibTableColumn
cfprApVnicDynamicProviderEpRn = _CfprApVnicDynamicProviderEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 10, 1, 3),
    _CfprApVnicDynamicProviderEpRn_Type()
)
cfprApVnicDynamicProviderEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicProviderEpRn.setStatus("current")
_CfprApVnicDynamicProviderEpChassisId_Type = Gauge32
_CfprApVnicDynamicProviderEpChassisId_Object = MibTableColumn
cfprApVnicDynamicProviderEpChassisId = _CfprApVnicDynamicProviderEpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 10, 1, 4),
    _CfprApVnicDynamicProviderEpChassisId_Type()
)
cfprApVnicDynamicProviderEpChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicProviderEpChassisId.setStatus("current")
_CfprApVnicDynamicProviderEpPortId_Type = Gauge32
_CfprApVnicDynamicProviderEpPortId_Object = MibTableColumn
cfprApVnicDynamicProviderEpPortId = _CfprApVnicDynamicProviderEpPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 10, 1, 5),
    _CfprApVnicDynamicProviderEpPortId_Type()
)
cfprApVnicDynamicProviderEpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicProviderEpPortId.setStatus("current")
_CfprApVnicDynamicProviderEpSlotId_Type = Gauge32
_CfprApVnicDynamicProviderEpSlotId_Object = MibTableColumn
cfprApVnicDynamicProviderEpSlotId = _CfprApVnicDynamicProviderEpSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 10, 1, 6),
    _CfprApVnicDynamicProviderEpSlotId_Type()
)
cfprApVnicDynamicProviderEpSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicProviderEpSlotId.setStatus("current")
_CfprApVnicDynamicProviderEpSwitchId_Type = CfprApNetworkSwitchId
_CfprApVnicDynamicProviderEpSwitchId_Object = MibTableColumn
cfprApVnicDynamicProviderEpSwitchId = _CfprApVnicDynamicProviderEpSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 10, 1, 7),
    _CfprApVnicDynamicProviderEpSwitchId_Type()
)
cfprApVnicDynamicProviderEpSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicDynamicProviderEpSwitchId.setStatus("current")
_CfprApVnicEthLifTable_Object = MibTable
cfprApVnicEthLifTable = _CfprApVnicEthLifTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 11)
)
if mibBuilder.loadTexts:
    cfprApVnicEthLifTable.setStatus("current")
_CfprApVnicEthLifEntry_Object = MibTableRow
cfprApVnicEthLifEntry = _CfprApVnicEthLifEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 11, 1)
)
cfprApVnicEthLifEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicEthLifInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicEthLifEntry.setStatus("current")
_CfprApVnicEthLifInstanceId_Type = CfprApManagedObjectId
_CfprApVnicEthLifInstanceId_Object = MibTableColumn
cfprApVnicEthLifInstanceId = _CfprApVnicEthLifInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 11, 1, 1),
    _CfprApVnicEthLifInstanceId_Type()
)
cfprApVnicEthLifInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicEthLifInstanceId.setStatus("current")
_CfprApVnicEthLifDn_Type = CfprApManagedObjectDn
_CfprApVnicEthLifDn_Object = MibTableColumn
cfprApVnicEthLifDn = _CfprApVnicEthLifDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 11, 1, 2),
    _CfprApVnicEthLifDn_Type()
)
cfprApVnicEthLifDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEthLifDn.setStatus("current")
_CfprApVnicEthLifRn_Type = SnmpAdminString
_CfprApVnicEthLifRn_Object = MibTableColumn
cfprApVnicEthLifRn = _CfprApVnicEthLifRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 11, 1, 3),
    _CfprApVnicEthLifRn_Type()
)
cfprApVnicEthLifRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEthLifRn.setStatus("current")
_CfprApVnicEthLifAddr_Type = MacAddress
_CfprApVnicEthLifAddr_Object = MibTableColumn
cfprApVnicEthLifAddr = _CfprApVnicEthLifAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 11, 1, 4),
    _CfprApVnicEthLifAddr_Type()
)
cfprApVnicEthLifAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEthLifAddr.setStatus("current")
_CfprApVnicEthLifName_Type = SnmpAdminString
_CfprApVnicEthLifName_Object = MibTableColumn
cfprApVnicEthLifName = _CfprApVnicEthLifName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 11, 1, 5),
    _CfprApVnicEthLifName_Type()
)
cfprApVnicEthLifName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEthLifName.setStatus("current")
_CfprApVnicEthLifNicDn_Type = SnmpAdminString
_CfprApVnicEthLifNicDn_Object = MibTableColumn
cfprApVnicEthLifNicDn = _CfprApVnicEthLifNicDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 11, 1, 6),
    _CfprApVnicEthLifNicDn_Type()
)
cfprApVnicEthLifNicDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEthLifNicDn.setStatus("current")
_CfprApVnicEthLifOwner_Type = CfprApVnicConnectionOwner
_CfprApVnicEthLifOwner_Object = MibTableColumn
cfprApVnicEthLifOwner = _CfprApVnicEthLifOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 11, 1, 7),
    _CfprApVnicEthLifOwner_Type()
)
cfprApVnicEthLifOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEthLifOwner.setStatus("current")
_CfprApVnicEthLifSwitchId_Type = CfprApNetworkSwitchId
_CfprApVnicEthLifSwitchId_Object = MibTableColumn
cfprApVnicEthLifSwitchId = _CfprApVnicEthLifSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 11, 1, 8),
    _CfprApVnicEthLifSwitchId_Type()
)
cfprApVnicEthLifSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEthLifSwitchId.setStatus("current")
_CfprApVnicEthLifType_Type = CfprApVnicConnectionType
_CfprApVnicEthLifType_Object = MibTableColumn
cfprApVnicEthLifType = _CfprApVnicEthLifType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 11, 1, 9),
    _CfprApVnicEthLifType_Type()
)
cfprApVnicEthLifType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEthLifType.setStatus("current")
_CfprApVnicEthLifVnicDn_Type = SnmpAdminString
_CfprApVnicEthLifVnicDn_Object = MibTableColumn
cfprApVnicEthLifVnicDn = _CfprApVnicEthLifVnicDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 11, 1, 10),
    _CfprApVnicEthLifVnicDn_Type()
)
cfprApVnicEthLifVnicDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEthLifVnicDn.setStatus("current")
_CfprApVnicEtherTable_Object = MibTable
cfprApVnicEtherTable = _CfprApVnicEtherTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12)
)
if mibBuilder.loadTexts:
    cfprApVnicEtherTable.setStatus("current")
_CfprApVnicEtherEntry_Object = MibTableRow
cfprApVnicEtherEntry = _CfprApVnicEtherEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1)
)
cfprApVnicEtherEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicEtherInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicEtherEntry.setStatus("current")
_CfprApVnicEtherInstanceId_Type = CfprApManagedObjectId
_CfprApVnicEtherInstanceId_Object = MibTableColumn
cfprApVnicEtherInstanceId = _CfprApVnicEtherInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 1),
    _CfprApVnicEtherInstanceId_Type()
)
cfprApVnicEtherInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicEtherInstanceId.setStatus("current")
_CfprApVnicEtherDn_Type = CfprApManagedObjectDn
_CfprApVnicEtherDn_Object = MibTableColumn
cfprApVnicEtherDn = _CfprApVnicEtherDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 2),
    _CfprApVnicEtherDn_Type()
)
cfprApVnicEtherDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherDn.setStatus("current")
_CfprApVnicEtherRn_Type = SnmpAdminString
_CfprApVnicEtherRn_Object = MibTableColumn
cfprApVnicEtherRn = _CfprApVnicEtherRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 3),
    _CfprApVnicEtherRn_Type()
)
cfprApVnicEtherRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherRn.setStatus("current")
_CfprApVnicEtherAdaptorProfileName_Type = SnmpAdminString
_CfprApVnicEtherAdaptorProfileName_Object = MibTableColumn
cfprApVnicEtherAdaptorProfileName = _CfprApVnicEtherAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 4),
    _CfprApVnicEtherAdaptorProfileName_Type()
)
cfprApVnicEtherAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherAdaptorProfileName.setStatus("current")
_CfprApVnicEtherAddr_Type = MacAddress
_CfprApVnicEtherAddr_Object = MibTableColumn
cfprApVnicEtherAddr = _CfprApVnicEtherAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 5),
    _CfprApVnicEtherAddr_Type()
)
cfprApVnicEtherAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherAddr.setStatus("current")
_CfprApVnicEtherAdminHostPort_Type = CfprApFabricHostPortId
_CfprApVnicEtherAdminHostPort_Object = MibTableColumn
cfprApVnicEtherAdminHostPort = _CfprApVnicEtherAdminHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 6),
    _CfprApVnicEtherAdminHostPort_Type()
)
cfprApVnicEtherAdminHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherAdminHostPort.setStatus("current")
_CfprApVnicEtherAdminVcon_Type = SnmpAdminString
_CfprApVnicEtherAdminVcon_Object = MibTableColumn
cfprApVnicEtherAdminVcon = _CfprApVnicEtherAdminVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 7),
    _CfprApVnicEtherAdminVcon_Type()
)
cfprApVnicEtherAdminVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherAdminVcon.setStatus("current")
_CfprApVnicEtherAppInstId_Type = SnmpAdminString
_CfprApVnicEtherAppInstId_Object = MibTableColumn
cfprApVnicEtherAppInstId = _CfprApVnicEtherAppInstId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 8),
    _CfprApVnicEtherAppInstId_Type()
)
cfprApVnicEtherAppInstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherAppInstId.setStatus("current")
_CfprApVnicEtherAppRole_Type = CfprApVnicAppRole
_CfprApVnicEtherAppRole_Object = MibTableColumn
cfprApVnicEtherAppRole = _CfprApVnicEtherAppRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 9),
    _CfprApVnicEtherAppRole_Type()
)
cfprApVnicEtherAppRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherAppRole.setStatus("current")
_CfprApVnicEtherBootDev_Type = CfprApVnicVnicBootDev
_CfprApVnicEtherBootDev_Object = MibTableColumn
cfprApVnicEtherBootDev = _CfprApVnicEtherBootDev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 10),
    _CfprApVnicEtherBootDev_Type()
)
cfprApVnicEtherBootDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherBootDev.setStatus("current")
_CfprApVnicEtherConfigQualifier_Type = CfprApVnicConfigIssues
_CfprApVnicEtherConfigQualifier_Object = MibTableColumn
cfprApVnicEtherConfigQualifier = _CfprApVnicEtherConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 11),
    _CfprApVnicEtherConfigQualifier_Type()
)
cfprApVnicEtherConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherConfigQualifier.setStatus("current")
_CfprApVnicEtherConfigState_Type = CfprApLsConfigState
_CfprApVnicEtherConfigState_Object = MibTableColumn
cfprApVnicEtherConfigState = _CfprApVnicEtherConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 12),
    _CfprApVnicEtherConfigState_Type()
)
cfprApVnicEtherConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherConfigState.setStatus("current")
_CfprApVnicEtherDynamicId_Type = Gauge32
_CfprApVnicEtherDynamicId_Object = MibTableColumn
cfprApVnicEtherDynamicId = _CfprApVnicEtherDynamicId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 13),
    _CfprApVnicEtherDynamicId_Type()
)
cfprApVnicEtherDynamicId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherDynamicId.setStatus("current")
_CfprApVnicEtherEquipmentDn_Type = SnmpAdminString
_CfprApVnicEtherEquipmentDn_Object = MibTableColumn
cfprApVnicEtherEquipmentDn = _CfprApVnicEtherEquipmentDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 14),
    _CfprApVnicEtherEquipmentDn_Type()
)
cfprApVnicEtherEquipmentDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherEquipmentDn.setStatus("current")
_CfprApVnicEtherFltAggr_Type = Unsigned64
_CfprApVnicEtherFltAggr_Object = MibTableColumn
cfprApVnicEtherFltAggr = _CfprApVnicEtherFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 15),
    _CfprApVnicEtherFltAggr_Type()
)
cfprApVnicEtherFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherFltAggr.setStatus("current")
_CfprApVnicEtherIdentPoolName_Type = SnmpAdminString
_CfprApVnicEtherIdentPoolName_Object = MibTableColumn
cfprApVnicEtherIdentPoolName = _CfprApVnicEtherIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 16),
    _CfprApVnicEtherIdentPoolName_Type()
)
cfprApVnicEtherIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherIdentPoolName.setStatus("current")
_CfprApVnicEtherInstType_Type = CfprApVnicInstantiation
_CfprApVnicEtherInstType_Object = MibTableColumn
cfprApVnicEtherInstType = _CfprApVnicEtherInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 17),
    _CfprApVnicEtherInstType_Type()
)
cfprApVnicEtherInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherInstType.setStatus("current")
_CfprApVnicEtherIsAllocated_Type = TruthValue
_CfprApVnicEtherIsAllocated_Object = MibTableColumn
cfprApVnicEtherIsAllocated = _CfprApVnicEtherIsAllocated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 18),
    _CfprApVnicEtherIsAllocated_Type()
)
cfprApVnicEtherIsAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherIsAllocated.setStatus("current")
_CfprApVnicEtherMtu_Type = Gauge32
_CfprApVnicEtherMtu_Object = MibTableColumn
cfprApVnicEtherMtu = _CfprApVnicEtherMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 19),
    _CfprApVnicEtherMtu_Type()
)
cfprApVnicEtherMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherMtu.setStatus("current")
_CfprApVnicEtherName_Type = SnmpAdminString
_CfprApVnicEtherName_Object = MibTableColumn
cfprApVnicEtherName = _CfprApVnicEtherName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 20),
    _CfprApVnicEtherName_Type()
)
cfprApVnicEtherName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherName.setStatus("current")
_CfprApVnicEtherNwCtrlPolicyName_Type = SnmpAdminString
_CfprApVnicEtherNwCtrlPolicyName_Object = MibTableColumn
cfprApVnicEtherNwCtrlPolicyName = _CfprApVnicEtherNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 21),
    _CfprApVnicEtherNwCtrlPolicyName_Type()
)
cfprApVnicEtherNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherNwCtrlPolicyName.setStatus("current")
_CfprApVnicEtherNwTemplName_Type = SnmpAdminString
_CfprApVnicEtherNwTemplName_Object = MibTableColumn
cfprApVnicEtherNwTemplName = _CfprApVnicEtherNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 22),
    _CfprApVnicEtherNwTemplName_Type()
)
cfprApVnicEtherNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherNwTemplName.setStatus("current")
_CfprApVnicEtherOperAdaptorProfileName_Type = SnmpAdminString
_CfprApVnicEtherOperAdaptorProfileName_Object = MibTableColumn
cfprApVnicEtherOperAdaptorProfileName = _CfprApVnicEtherOperAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 23),
    _CfprApVnicEtherOperAdaptorProfileName_Type()
)
cfprApVnicEtherOperAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherOperAdaptorProfileName.setStatus("current")
_CfprApVnicEtherOperHostPort_Type = CfprApVnicVnicOperHostPort
_CfprApVnicEtherOperHostPort_Object = MibTableColumn
cfprApVnicEtherOperHostPort = _CfprApVnicEtherOperHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 24),
    _CfprApVnicEtherOperHostPort_Type()
)
cfprApVnicEtherOperHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherOperHostPort.setStatus("current")
_CfprApVnicEtherOperIdentPoolName_Type = SnmpAdminString
_CfprApVnicEtherOperIdentPoolName_Object = MibTableColumn
cfprApVnicEtherOperIdentPoolName = _CfprApVnicEtherOperIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 25),
    _CfprApVnicEtherOperIdentPoolName_Type()
)
cfprApVnicEtherOperIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherOperIdentPoolName.setStatus("current")
_CfprApVnicEtherOperNwCtrlPolicyName_Type = SnmpAdminString
_CfprApVnicEtherOperNwCtrlPolicyName_Object = MibTableColumn
cfprApVnicEtherOperNwCtrlPolicyName = _CfprApVnicEtherOperNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 26),
    _CfprApVnicEtherOperNwCtrlPolicyName_Type()
)
cfprApVnicEtherOperNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherOperNwCtrlPolicyName.setStatus("current")
_CfprApVnicEtherOperNwTemplName_Type = SnmpAdminString
_CfprApVnicEtherOperNwTemplName_Object = MibTableColumn
cfprApVnicEtherOperNwTemplName = _CfprApVnicEtherOperNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 27),
    _CfprApVnicEtherOperNwTemplName_Type()
)
cfprApVnicEtherOperNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherOperNwTemplName.setStatus("current")
_CfprApVnicEtherOperOrder_Type = Gauge32
_CfprApVnicEtherOperOrder_Object = MibTableColumn
cfprApVnicEtherOperOrder = _CfprApVnicEtherOperOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 28),
    _CfprApVnicEtherOperOrder_Type()
)
cfprApVnicEtherOperOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherOperOrder.setStatus("current")
_CfprApVnicEtherOperPinToGroupName_Type = SnmpAdminString
_CfprApVnicEtherOperPinToGroupName_Object = MibTableColumn
cfprApVnicEtherOperPinToGroupName = _CfprApVnicEtherOperPinToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 29),
    _CfprApVnicEtherOperPinToGroupName_Type()
)
cfprApVnicEtherOperPinToGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherOperPinToGroupName.setStatus("current")
_CfprApVnicEtherOperQosPolicyName_Type = SnmpAdminString
_CfprApVnicEtherOperQosPolicyName_Object = MibTableColumn
cfprApVnicEtherOperQosPolicyName = _CfprApVnicEtherOperQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 30),
    _CfprApVnicEtherOperQosPolicyName_Type()
)
cfprApVnicEtherOperQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherOperQosPolicyName.setStatus("current")
_CfprApVnicEtherOperSpeed_Type = Gauge32
_CfprApVnicEtherOperSpeed_Object = MibTableColumn
cfprApVnicEtherOperSpeed = _CfprApVnicEtherOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 31),
    _CfprApVnicEtherOperSpeed_Type()
)
cfprApVnicEtherOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherOperSpeed.setStatus("current")
_CfprApVnicEtherOperStatsPolicyName_Type = SnmpAdminString
_CfprApVnicEtherOperStatsPolicyName_Object = MibTableColumn
cfprApVnicEtherOperStatsPolicyName = _CfprApVnicEtherOperStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 32),
    _CfprApVnicEtherOperStatsPolicyName_Type()
)
cfprApVnicEtherOperStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherOperStatsPolicyName.setStatus("current")
_CfprApVnicEtherOperVcon_Type = SnmpAdminString
_CfprApVnicEtherOperVcon_Object = MibTableColumn
cfprApVnicEtherOperVcon = _CfprApVnicEtherOperVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 33),
    _CfprApVnicEtherOperVcon_Type()
)
cfprApVnicEtherOperVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherOperVcon.setStatus("current")
_CfprApVnicEtherOrder_Type = Gauge32
_CfprApVnicEtherOrder_Object = MibTableColumn
cfprApVnicEtherOrder = _CfprApVnicEtherOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 34),
    _CfprApVnicEtherOrder_Type()
)
cfprApVnicEtherOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherOrder.setStatus("current")
_CfprApVnicEtherOwner_Type = CfprApVnicConnectionOwner
_CfprApVnicEtherOwner_Object = MibTableColumn
cfprApVnicEtherOwner = _CfprApVnicEtherOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 35),
    _CfprApVnicEtherOwner_Type()
)
cfprApVnicEtherOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherOwner.setStatus("current")
_CfprApVnicEtherPfDn_Type = SnmpAdminString
_CfprApVnicEtherPfDn_Object = MibTableColumn
cfprApVnicEtherPfDn = _CfprApVnicEtherPfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 36),
    _CfprApVnicEtherPfDn_Type()
)
cfprApVnicEtherPfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherPfDn.setStatus("current")
_CfprApVnicEtherPinToGroupName_Type = SnmpAdminString
_CfprApVnicEtherPinToGroupName_Object = MibTableColumn
cfprApVnicEtherPinToGroupName = _CfprApVnicEtherPinToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 37),
    _CfprApVnicEtherPinToGroupName_Type()
)
cfprApVnicEtherPinToGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherPinToGroupName.setStatus("current")
_CfprApVnicEtherPortType_Type = CfprApFabricSSAPortType
_CfprApVnicEtherPortType_Object = MibTableColumn
cfprApVnicEtherPortType = _CfprApVnicEtherPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 38),
    _CfprApVnicEtherPortType_Type()
)
cfprApVnicEtherPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherPortType.setStatus("current")
_CfprApVnicEtherQosPolicyName_Type = SnmpAdminString
_CfprApVnicEtherQosPolicyName_Object = MibTableColumn
cfprApVnicEtherQosPolicyName = _CfprApVnicEtherQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 39),
    _CfprApVnicEtherQosPolicyName_Type()
)
cfprApVnicEtherQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherQosPolicyName.setStatus("current")
_CfprApVnicEtherStatsPolicyName_Type = SnmpAdminString
_CfprApVnicEtherStatsPolicyName_Object = MibTableColumn
cfprApVnicEtherStatsPolicyName = _CfprApVnicEtherStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 40),
    _CfprApVnicEtherStatsPolicyName_Type()
)
cfprApVnicEtherStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherStatsPolicyName.setStatus("current")
_CfprApVnicEtherSwitchId_Type = CfprApVnicEtherBaseSwitchId
_CfprApVnicEtherSwitchId_Object = MibTableColumn
cfprApVnicEtherSwitchId = _CfprApVnicEtherSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 41),
    _CfprApVnicEtherSwitchId_Type()
)
cfprApVnicEtherSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherSwitchId.setStatus("current")
_CfprApVnicEtherType_Type = CfprApVnicEtherType
_CfprApVnicEtherType_Object = MibTableColumn
cfprApVnicEtherType = _CfprApVnicEtherType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 42),
    _CfprApVnicEtherType_Type()
)
cfprApVnicEtherType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherType.setStatus("current")
_CfprApVnicEtherVirtualizationPreference_Type = CfprApVnicVirtualizationPreferenceType
_CfprApVnicEtherVirtualizationPreference_Object = MibTableColumn
cfprApVnicEtherVirtualizationPreference = _CfprApVnicEtherVirtualizationPreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 12, 1, 43),
    _CfprApVnicEtherVirtualizationPreference_Type()
)
cfprApVnicEtherVirtualizationPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherVirtualizationPreference.setStatus("current")
_CfprApVnicEtherIfTable_Object = MibTable
cfprApVnicEtherIfTable = _CfprApVnicEtherIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 13)
)
if mibBuilder.loadTexts:
    cfprApVnicEtherIfTable.setStatus("current")
_CfprApVnicEtherIfEntry_Object = MibTableRow
cfprApVnicEtherIfEntry = _CfprApVnicEtherIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 13, 1)
)
cfprApVnicEtherIfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicEtherIfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicEtherIfEntry.setStatus("current")
_CfprApVnicEtherIfInstanceId_Type = CfprApManagedObjectId
_CfprApVnicEtherIfInstanceId_Object = MibTableColumn
cfprApVnicEtherIfInstanceId = _CfprApVnicEtherIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 13, 1, 1),
    _CfprApVnicEtherIfInstanceId_Type()
)
cfprApVnicEtherIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicEtherIfInstanceId.setStatus("current")
_CfprApVnicEtherIfDn_Type = CfprApManagedObjectDn
_CfprApVnicEtherIfDn_Object = MibTableColumn
cfprApVnicEtherIfDn = _CfprApVnicEtherIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 13, 1, 2),
    _CfprApVnicEtherIfDn_Type()
)
cfprApVnicEtherIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherIfDn.setStatus("current")
_CfprApVnicEtherIfRn_Type = SnmpAdminString
_CfprApVnicEtherIfRn_Object = MibTableColumn
cfprApVnicEtherIfRn = _CfprApVnicEtherIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 13, 1, 3),
    _CfprApVnicEtherIfRn_Type()
)
cfprApVnicEtherIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherIfRn.setStatus("current")
_CfprApVnicEtherIfAddr_Type = MacAddress
_CfprApVnicEtherIfAddr_Object = MibTableColumn
cfprApVnicEtherIfAddr = _CfprApVnicEtherIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 13, 1, 4),
    _CfprApVnicEtherIfAddr_Type()
)
cfprApVnicEtherIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherIfAddr.setStatus("current")
_CfprApVnicEtherIfConfigQualifier_Type = CfprApVnicConfigIssues
_CfprApVnicEtherIfConfigQualifier_Object = MibTableColumn
cfprApVnicEtherIfConfigQualifier = _CfprApVnicEtherIfConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 13, 1, 5),
    _CfprApVnicEtherIfConfigQualifier_Type()
)
cfprApVnicEtherIfConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherIfConfigQualifier.setStatus("current")
_CfprApVnicEtherIfDefaultNet_Type = TruthValue
_CfprApVnicEtherIfDefaultNet_Object = MibTableColumn
cfprApVnicEtherIfDefaultNet = _CfprApVnicEtherIfDefaultNet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 13, 1, 6),
    _CfprApVnicEtherIfDefaultNet_Type()
)
cfprApVnicEtherIfDefaultNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherIfDefaultNet.setStatus("current")
_CfprApVnicEtherIfFltAggr_Type = Unsigned64
_CfprApVnicEtherIfFltAggr_Object = MibTableColumn
cfprApVnicEtherIfFltAggr = _CfprApVnicEtherIfFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 13, 1, 7),
    _CfprApVnicEtherIfFltAggr_Type()
)
cfprApVnicEtherIfFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherIfFltAggr.setStatus("current")
_CfprApVnicEtherIfName_Type = SnmpAdminString
_CfprApVnicEtherIfName_Object = MibTableColumn
cfprApVnicEtherIfName = _CfprApVnicEtherIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 13, 1, 8),
    _CfprApVnicEtherIfName_Type()
)
cfprApVnicEtherIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherIfName.setStatus("current")
_CfprApVnicEtherIfOperState_Type = CfprApVnicIfOperState
_CfprApVnicEtherIfOperState_Object = MibTableColumn
cfprApVnicEtherIfOperState = _CfprApVnicEtherIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 13, 1, 9),
    _CfprApVnicEtherIfOperState_Type()
)
cfprApVnicEtherIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherIfOperState.setStatus("current")
_CfprApVnicEtherIfOperVnetDn_Type = SnmpAdminString
_CfprApVnicEtherIfOperVnetDn_Object = MibTableColumn
cfprApVnicEtherIfOperVnetDn = _CfprApVnicEtherIfOperVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 13, 1, 10),
    _CfprApVnicEtherIfOperVnetDn_Type()
)
cfprApVnicEtherIfOperVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherIfOperVnetDn.setStatus("current")
_CfprApVnicEtherIfOperVnetName_Type = SnmpAdminString
_CfprApVnicEtherIfOperVnetName_Object = MibTableColumn
cfprApVnicEtherIfOperVnetName = _CfprApVnicEtherIfOperVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 13, 1, 11),
    _CfprApVnicEtherIfOperVnetName_Type()
)
cfprApVnicEtherIfOperVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherIfOperVnetName.setStatus("current")
_CfprApVnicEtherIfOwner_Type = CfprApVnicConnectionOwner
_CfprApVnicEtherIfOwner_Object = MibTableColumn
cfprApVnicEtherIfOwner = _CfprApVnicEtherIfOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 13, 1, 12),
    _CfprApVnicEtherIfOwner_Type()
)
cfprApVnicEtherIfOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherIfOwner.setStatus("current")
_CfprApVnicEtherIfPubNwId_Type = Gauge32
_CfprApVnicEtherIfPubNwId_Object = MibTableColumn
cfprApVnicEtherIfPubNwId = _CfprApVnicEtherIfPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 13, 1, 13),
    _CfprApVnicEtherIfPubNwId_Type()
)
cfprApVnicEtherIfPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherIfPubNwId.setStatus("current")
_CfprApVnicEtherIfSharing_Type = CfprApFabricVlanSharingType
_CfprApVnicEtherIfSharing_Object = MibTableColumn
cfprApVnicEtherIfSharing = _CfprApVnicEtherIfSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 13, 1, 14),
    _CfprApVnicEtherIfSharing_Type()
)
cfprApVnicEtherIfSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherIfSharing.setStatus("current")
_CfprApVnicEtherIfSwitchId_Type = CfprApVnicL2IfSwitchId
_CfprApVnicEtherIfSwitchId_Object = MibTableColumn
cfprApVnicEtherIfSwitchId = _CfprApVnicEtherIfSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 13, 1, 15),
    _CfprApVnicEtherIfSwitchId_Type()
)
cfprApVnicEtherIfSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherIfSwitchId.setStatus("current")
_CfprApVnicEtherIfType_Type = CfprApVnicAEtherIfType
_CfprApVnicEtherIfType_Object = MibTableColumn
cfprApVnicEtherIfType = _CfprApVnicEtherIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 13, 1, 16),
    _CfprApVnicEtherIfType_Type()
)
cfprApVnicEtherIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherIfType.setStatus("current")
_CfprApVnicEtherIfVnet_Type = Gauge32
_CfprApVnicEtherIfVnet_Object = MibTableColumn
cfprApVnicEtherIfVnet = _CfprApVnicEtherIfVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 13, 1, 17),
    _CfprApVnicEtherIfVnet_Type()
)
cfprApVnicEtherIfVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicEtherIfVnet.setStatus("current")
_CfprApVnicFcTable_Object = MibTable
cfprApVnicFcTable = _CfprApVnicFcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14)
)
if mibBuilder.loadTexts:
    cfprApVnicFcTable.setStatus("current")
_CfprApVnicFcEntry_Object = MibTableRow
cfprApVnicFcEntry = _CfprApVnicFcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1)
)
cfprApVnicFcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicFcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicFcEntry.setStatus("current")
_CfprApVnicFcInstanceId_Type = CfprApManagedObjectId
_CfprApVnicFcInstanceId_Object = MibTableColumn
cfprApVnicFcInstanceId = _CfprApVnicFcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 1),
    _CfprApVnicFcInstanceId_Type()
)
cfprApVnicFcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicFcInstanceId.setStatus("current")
_CfprApVnicFcDn_Type = CfprApManagedObjectDn
_CfprApVnicFcDn_Object = MibTableColumn
cfprApVnicFcDn = _CfprApVnicFcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 2),
    _CfprApVnicFcDn_Type()
)
cfprApVnicFcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcDn.setStatus("current")
_CfprApVnicFcRn_Type = SnmpAdminString
_CfprApVnicFcRn_Object = MibTableColumn
cfprApVnicFcRn = _CfprApVnicFcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 3),
    _CfprApVnicFcRn_Type()
)
cfprApVnicFcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcRn.setStatus("current")
_CfprApVnicFcAdaptorProfileName_Type = SnmpAdminString
_CfprApVnicFcAdaptorProfileName_Object = MibTableColumn
cfprApVnicFcAdaptorProfileName = _CfprApVnicFcAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 4),
    _CfprApVnicFcAdaptorProfileName_Type()
)
cfprApVnicFcAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcAdaptorProfileName.setStatus("current")
_CfprApVnicFcAddr_Type = Unsigned64
_CfprApVnicFcAddr_Object = MibTableColumn
cfprApVnicFcAddr = _CfprApVnicFcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 5),
    _CfprApVnicFcAddr_Type()
)
cfprApVnicFcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcAddr.setStatus("current")
_CfprApVnicFcAdminHostPort_Type = CfprApFabricHostPortId
_CfprApVnicFcAdminHostPort_Object = MibTableColumn
cfprApVnicFcAdminHostPort = _CfprApVnicFcAdminHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 6),
    _CfprApVnicFcAdminHostPort_Type()
)
cfprApVnicFcAdminHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcAdminHostPort.setStatus("current")
_CfprApVnicFcAdminVcon_Type = SnmpAdminString
_CfprApVnicFcAdminVcon_Object = MibTableColumn
cfprApVnicFcAdminVcon = _CfprApVnicFcAdminVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 7),
    _CfprApVnicFcAdminVcon_Type()
)
cfprApVnicFcAdminVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcAdminVcon.setStatus("current")
_CfprApVnicFcAppRole_Type = CfprApVnicAppRole
_CfprApVnicFcAppRole_Object = MibTableColumn
cfprApVnicFcAppRole = _CfprApVnicFcAppRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 8),
    _CfprApVnicFcAppRole_Type()
)
cfprApVnicFcAppRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcAppRole.setStatus("current")
_CfprApVnicFcBootDev_Type = CfprApVnicVnicBootDev
_CfprApVnicFcBootDev_Object = MibTableColumn
cfprApVnicFcBootDev = _CfprApVnicFcBootDev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 9),
    _CfprApVnicFcBootDev_Type()
)
cfprApVnicFcBootDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcBootDev.setStatus("current")
_CfprApVnicFcConfigQualifier_Type = CfprApVnicConfigIssues
_CfprApVnicFcConfigQualifier_Object = MibTableColumn
cfprApVnicFcConfigQualifier = _CfprApVnicFcConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 10),
    _CfprApVnicFcConfigQualifier_Type()
)
cfprApVnicFcConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcConfigQualifier.setStatus("current")
_CfprApVnicFcConfigState_Type = CfprApLsConfigState
_CfprApVnicFcConfigState_Object = MibTableColumn
cfprApVnicFcConfigState = _CfprApVnicFcConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 11),
    _CfprApVnicFcConfigState_Type()
)
cfprApVnicFcConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcConfigState.setStatus("current")
_CfprApVnicFcEquipmentDn_Type = SnmpAdminString
_CfprApVnicFcEquipmentDn_Object = MibTableColumn
cfprApVnicFcEquipmentDn = _CfprApVnicFcEquipmentDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 12),
    _CfprApVnicFcEquipmentDn_Type()
)
cfprApVnicFcEquipmentDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcEquipmentDn.setStatus("current")
_CfprApVnicFcFltAggr_Type = Unsigned64
_CfprApVnicFcFltAggr_Object = MibTableColumn
cfprApVnicFcFltAggr = _CfprApVnicFcFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 13),
    _CfprApVnicFcFltAggr_Type()
)
cfprApVnicFcFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcFltAggr.setStatus("current")
_CfprApVnicFcIdentPoolName_Type = SnmpAdminString
_CfprApVnicFcIdentPoolName_Object = MibTableColumn
cfprApVnicFcIdentPoolName = _CfprApVnicFcIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 14),
    _CfprApVnicFcIdentPoolName_Type()
)
cfprApVnicFcIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcIdentPoolName.setStatus("current")
_CfprApVnicFcInstType_Type = CfprApVnicInstantiation
_CfprApVnicFcInstType_Object = MibTableColumn
cfprApVnicFcInstType = _CfprApVnicFcInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 15),
    _CfprApVnicFcInstType_Type()
)
cfprApVnicFcInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcInstType.setStatus("current")
_CfprApVnicFcMaxDataFieldSize_Type = Gauge32
_CfprApVnicFcMaxDataFieldSize_Object = MibTableColumn
cfprApVnicFcMaxDataFieldSize = _CfprApVnicFcMaxDataFieldSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 16),
    _CfprApVnicFcMaxDataFieldSize_Type()
)
cfprApVnicFcMaxDataFieldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcMaxDataFieldSize.setStatus("current")
_CfprApVnicFcName_Type = SnmpAdminString
_CfprApVnicFcName_Object = MibTableColumn
cfprApVnicFcName = _CfprApVnicFcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 17),
    _CfprApVnicFcName_Type()
)
cfprApVnicFcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcName.setStatus("current")
_CfprApVnicFcNodeAddr_Type = Unsigned64
_CfprApVnicFcNodeAddr_Object = MibTableColumn
cfprApVnicFcNodeAddr = _CfprApVnicFcNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 18),
    _CfprApVnicFcNodeAddr_Type()
)
cfprApVnicFcNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcNodeAddr.setStatus("current")
_CfprApVnicFcNwTemplName_Type = SnmpAdminString
_CfprApVnicFcNwTemplName_Object = MibTableColumn
cfprApVnicFcNwTemplName = _CfprApVnicFcNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 19),
    _CfprApVnicFcNwTemplName_Type()
)
cfprApVnicFcNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcNwTemplName.setStatus("current")
_CfprApVnicFcOperHostPort_Type = CfprApVnicVnicOperHostPort
_CfprApVnicFcOperHostPort_Object = MibTableColumn
cfprApVnicFcOperHostPort = _CfprApVnicFcOperHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 21),
    _CfprApVnicFcOperHostPort_Type()
)
cfprApVnicFcOperHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcOperHostPort.setStatus("current")
_CfprApVnicFcOperIdentPoolName_Type = SnmpAdminString
_CfprApVnicFcOperIdentPoolName_Object = MibTableColumn
cfprApVnicFcOperIdentPoolName = _CfprApVnicFcOperIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 22),
    _CfprApVnicFcOperIdentPoolName_Type()
)
cfprApVnicFcOperIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcOperIdentPoolName.setStatus("current")
_CfprApVnicFcOperNwTemplName_Type = SnmpAdminString
_CfprApVnicFcOperNwTemplName_Object = MibTableColumn
cfprApVnicFcOperNwTemplName = _CfprApVnicFcOperNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 23),
    _CfprApVnicFcOperNwTemplName_Type()
)
cfprApVnicFcOperNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcOperNwTemplName.setStatus("current")
_CfprApVnicFcOperOrder_Type = Gauge32
_CfprApVnicFcOperOrder_Object = MibTableColumn
cfprApVnicFcOperOrder = _CfprApVnicFcOperOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 24),
    _CfprApVnicFcOperOrder_Type()
)
cfprApVnicFcOperOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcOperOrder.setStatus("current")
_CfprApVnicFcOperPinToGroupName_Type = SnmpAdminString
_CfprApVnicFcOperPinToGroupName_Object = MibTableColumn
cfprApVnicFcOperPinToGroupName = _CfprApVnicFcOperPinToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 25),
    _CfprApVnicFcOperPinToGroupName_Type()
)
cfprApVnicFcOperPinToGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcOperPinToGroupName.setStatus("current")
_CfprApVnicFcOperQosPolicyName_Type = SnmpAdminString
_CfprApVnicFcOperQosPolicyName_Object = MibTableColumn
cfprApVnicFcOperQosPolicyName = _CfprApVnicFcOperQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 26),
    _CfprApVnicFcOperQosPolicyName_Type()
)
cfprApVnicFcOperQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcOperQosPolicyName.setStatus("current")
_CfprApVnicFcOperSpeed_Type = Gauge32
_CfprApVnicFcOperSpeed_Object = MibTableColumn
cfprApVnicFcOperSpeed = _CfprApVnicFcOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 27),
    _CfprApVnicFcOperSpeed_Type()
)
cfprApVnicFcOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcOperSpeed.setStatus("current")
_CfprApVnicFcOperStatsPolicyName_Type = SnmpAdminString
_CfprApVnicFcOperStatsPolicyName_Object = MibTableColumn
cfprApVnicFcOperStatsPolicyName = _CfprApVnicFcOperStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 28),
    _CfprApVnicFcOperStatsPolicyName_Type()
)
cfprApVnicFcOperStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcOperStatsPolicyName.setStatus("current")
_CfprApVnicFcOperVcon_Type = SnmpAdminString
_CfprApVnicFcOperVcon_Object = MibTableColumn
cfprApVnicFcOperVcon = _CfprApVnicFcOperVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 29),
    _CfprApVnicFcOperVcon_Type()
)
cfprApVnicFcOperVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcOperVcon.setStatus("current")
_CfprApVnicFcOrder_Type = Gauge32
_CfprApVnicFcOrder_Object = MibTableColumn
cfprApVnicFcOrder = _CfprApVnicFcOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 30),
    _CfprApVnicFcOrder_Type()
)
cfprApVnicFcOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcOrder.setStatus("current")
_CfprApVnicFcOwner_Type = CfprApVnicConnectionOwner
_CfprApVnicFcOwner_Object = MibTableColumn
cfprApVnicFcOwner = _CfprApVnicFcOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 31),
    _CfprApVnicFcOwner_Type()
)
cfprApVnicFcOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcOwner.setStatus("current")
_CfprApVnicFcPersBind_Type = CfprApVnicFcBasePersBind
_CfprApVnicFcPersBind_Object = MibTableColumn
cfprApVnicFcPersBind = _CfprApVnicFcPersBind_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 32),
    _CfprApVnicFcPersBind_Type()
)
cfprApVnicFcPersBind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcPersBind.setStatus("current")
_CfprApVnicFcPersBindClear_Type = TruthValue
_CfprApVnicFcPersBindClear_Object = MibTableColumn
cfprApVnicFcPersBindClear = _CfprApVnicFcPersBindClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 33),
    _CfprApVnicFcPersBindClear_Type()
)
cfprApVnicFcPersBindClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcPersBindClear.setStatus("current")
_CfprApVnicFcPinToGroupName_Type = SnmpAdminString
_CfprApVnicFcPinToGroupName_Object = MibTableColumn
cfprApVnicFcPinToGroupName = _CfprApVnicFcPinToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 34),
    _CfprApVnicFcPinToGroupName_Type()
)
cfprApVnicFcPinToGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcPinToGroupName.setStatus("current")
_CfprApVnicFcQosPolicyName_Type = SnmpAdminString
_CfprApVnicFcQosPolicyName_Object = MibTableColumn
cfprApVnicFcQosPolicyName = _CfprApVnicFcQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 35),
    _CfprApVnicFcQosPolicyName_Type()
)
cfprApVnicFcQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcQosPolicyName.setStatus("current")
_CfprApVnicFcStatsPolicyName_Type = SnmpAdminString
_CfprApVnicFcStatsPolicyName_Object = MibTableColumn
cfprApVnicFcStatsPolicyName = _CfprApVnicFcStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 36),
    _CfprApVnicFcStatsPolicyName_Type()
)
cfprApVnicFcStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcStatsPolicyName.setStatus("current")
_CfprApVnicFcSwitchId_Type = CfprApNetworkSwitchId
_CfprApVnicFcSwitchId_Object = MibTableColumn
cfprApVnicFcSwitchId = _CfprApVnicFcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 37),
    _CfprApVnicFcSwitchId_Type()
)
cfprApVnicFcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcSwitchId.setStatus("current")
_CfprApVnicFcType_Type = CfprApVnicFcBaseType
_CfprApVnicFcType_Object = MibTableColumn
cfprApVnicFcType = _CfprApVnicFcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 14, 1, 38),
    _CfprApVnicFcType_Type()
)
cfprApVnicFcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcType.setStatus("current")
_CfprApVnicFcGroupDefTable_Object = MibTable
cfprApVnicFcGroupDefTable = _CfprApVnicFcGroupDefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 15)
)
if mibBuilder.loadTexts:
    cfprApVnicFcGroupDefTable.setStatus("current")
_CfprApVnicFcGroupDefEntry_Object = MibTableRow
cfprApVnicFcGroupDefEntry = _CfprApVnicFcGroupDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 15, 1)
)
cfprApVnicFcGroupDefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicFcGroupDefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicFcGroupDefEntry.setStatus("current")
_CfprApVnicFcGroupDefInstanceId_Type = CfprApManagedObjectId
_CfprApVnicFcGroupDefInstanceId_Object = MibTableColumn
cfprApVnicFcGroupDefInstanceId = _CfprApVnicFcGroupDefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 15, 1, 1),
    _CfprApVnicFcGroupDefInstanceId_Type()
)
cfprApVnicFcGroupDefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicFcGroupDefInstanceId.setStatus("current")
_CfprApVnicFcGroupDefDn_Type = CfprApManagedObjectDn
_CfprApVnicFcGroupDefDn_Object = MibTableColumn
cfprApVnicFcGroupDefDn = _CfprApVnicFcGroupDefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 15, 1, 2),
    _CfprApVnicFcGroupDefDn_Type()
)
cfprApVnicFcGroupDefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcGroupDefDn.setStatus("current")
_CfprApVnicFcGroupDefRn_Type = SnmpAdminString
_CfprApVnicFcGroupDefRn_Object = MibTableColumn
cfprApVnicFcGroupDefRn = _CfprApVnicFcGroupDefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 15, 1, 3),
    _CfprApVnicFcGroupDefRn_Type()
)
cfprApVnicFcGroupDefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcGroupDefRn.setStatus("current")
_CfprApVnicFcGroupDefAdaptorProfileName_Type = SnmpAdminString
_CfprApVnicFcGroupDefAdaptorProfileName_Object = MibTableColumn
cfprApVnicFcGroupDefAdaptorProfileName = _CfprApVnicFcGroupDefAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 15, 1, 4),
    _CfprApVnicFcGroupDefAdaptorProfileName_Type()
)
cfprApVnicFcGroupDefAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcGroupDefAdaptorProfileName.setStatus("current")
_CfprApVnicFcGroupDefDescr_Type = SnmpAdminString
_CfprApVnicFcGroupDefDescr_Object = MibTableColumn
cfprApVnicFcGroupDefDescr = _CfprApVnicFcGroupDefDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 15, 1, 5),
    _CfprApVnicFcGroupDefDescr_Type()
)
cfprApVnicFcGroupDefDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcGroupDefDescr.setStatus("current")
_CfprApVnicFcGroupDefIdentPoolName_Type = SnmpAdminString
_CfprApVnicFcGroupDefIdentPoolName_Object = MibTableColumn
cfprApVnicFcGroupDefIdentPoolName = _CfprApVnicFcGroupDefIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 15, 1, 6),
    _CfprApVnicFcGroupDefIdentPoolName_Type()
)
cfprApVnicFcGroupDefIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcGroupDefIdentPoolName.setStatus("current")
_CfprApVnicFcGroupDefIntId_Type = SnmpAdminString
_CfprApVnicFcGroupDefIntId_Object = MibTableColumn
cfprApVnicFcGroupDefIntId = _CfprApVnicFcGroupDefIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 15, 1, 7),
    _CfprApVnicFcGroupDefIntId_Type()
)
cfprApVnicFcGroupDefIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcGroupDefIntId.setStatus("current")
_CfprApVnicFcGroupDefMaxDataFieldSize_Type = Gauge32
_CfprApVnicFcGroupDefMaxDataFieldSize_Object = MibTableColumn
cfprApVnicFcGroupDefMaxDataFieldSize = _CfprApVnicFcGroupDefMaxDataFieldSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 15, 1, 8),
    _CfprApVnicFcGroupDefMaxDataFieldSize_Type()
)
cfprApVnicFcGroupDefMaxDataFieldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcGroupDefMaxDataFieldSize.setStatus("current")
_CfprApVnicFcGroupDefName_Type = SnmpAdminString
_CfprApVnicFcGroupDefName_Object = MibTableColumn
cfprApVnicFcGroupDefName = _CfprApVnicFcGroupDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 15, 1, 9),
    _CfprApVnicFcGroupDefName_Type()
)
cfprApVnicFcGroupDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcGroupDefName.setStatus("current")
_CfprApVnicFcGroupDefNwTemplName_Type = SnmpAdminString
_CfprApVnicFcGroupDefNwTemplName_Object = MibTableColumn
cfprApVnicFcGroupDefNwTemplName = _CfprApVnicFcGroupDefNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 15, 1, 10),
    _CfprApVnicFcGroupDefNwTemplName_Type()
)
cfprApVnicFcGroupDefNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcGroupDefNwTemplName.setStatus("current")
_CfprApVnicFcGroupDefOperStatsPolicyName_Type = SnmpAdminString
_CfprApVnicFcGroupDefOperStatsPolicyName_Object = MibTableColumn
cfprApVnicFcGroupDefOperStatsPolicyName = _CfprApVnicFcGroupDefOperStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 15, 1, 11),
    _CfprApVnicFcGroupDefOperStatsPolicyName_Type()
)
cfprApVnicFcGroupDefOperStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcGroupDefOperStatsPolicyName.setStatus("current")
_CfprApVnicFcGroupDefPolicyLevel_Type = Gauge32
_CfprApVnicFcGroupDefPolicyLevel_Object = MibTableColumn
cfprApVnicFcGroupDefPolicyLevel = _CfprApVnicFcGroupDefPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 15, 1, 13),
    _CfprApVnicFcGroupDefPolicyLevel_Type()
)
cfprApVnicFcGroupDefPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcGroupDefPolicyLevel.setStatus("current")
_CfprApVnicFcGroupDefPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApVnicFcGroupDefPolicyOwner_Object = MibTableColumn
cfprApVnicFcGroupDefPolicyOwner = _CfprApVnicFcGroupDefPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 15, 1, 14),
    _CfprApVnicFcGroupDefPolicyOwner_Type()
)
cfprApVnicFcGroupDefPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcGroupDefPolicyOwner.setStatus("current")
_CfprApVnicFcGroupDefQosPolicyName_Type = SnmpAdminString
_CfprApVnicFcGroupDefQosPolicyName_Object = MibTableColumn
cfprApVnicFcGroupDefQosPolicyName = _CfprApVnicFcGroupDefQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 15, 1, 15),
    _CfprApVnicFcGroupDefQosPolicyName_Type()
)
cfprApVnicFcGroupDefQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcGroupDefQosPolicyName.setStatus("current")
_CfprApVnicFcGroupDefStatsPolicyName_Type = SnmpAdminString
_CfprApVnicFcGroupDefStatsPolicyName_Object = MibTableColumn
cfprApVnicFcGroupDefStatsPolicyName = _CfprApVnicFcGroupDefStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 15, 1, 16),
    _CfprApVnicFcGroupDefStatsPolicyName_Type()
)
cfprApVnicFcGroupDefStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcGroupDefStatsPolicyName.setStatus("current")
_CfprApVnicFcGroupTemplTable_Object = MibTable
cfprApVnicFcGroupTemplTable = _CfprApVnicFcGroupTemplTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 16)
)
if mibBuilder.loadTexts:
    cfprApVnicFcGroupTemplTable.setStatus("current")
_CfprApVnicFcGroupTemplEntry_Object = MibTableRow
cfprApVnicFcGroupTemplEntry = _CfprApVnicFcGroupTemplEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 16, 1)
)
cfprApVnicFcGroupTemplEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicFcGroupTemplInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicFcGroupTemplEntry.setStatus("current")
_CfprApVnicFcGroupTemplInstanceId_Type = CfprApManagedObjectId
_CfprApVnicFcGroupTemplInstanceId_Object = MibTableColumn
cfprApVnicFcGroupTemplInstanceId = _CfprApVnicFcGroupTemplInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 16, 1, 1),
    _CfprApVnicFcGroupTemplInstanceId_Type()
)
cfprApVnicFcGroupTemplInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicFcGroupTemplInstanceId.setStatus("current")
_CfprApVnicFcGroupTemplDn_Type = CfprApManagedObjectDn
_CfprApVnicFcGroupTemplDn_Object = MibTableColumn
cfprApVnicFcGroupTemplDn = _CfprApVnicFcGroupTemplDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 16, 1, 2),
    _CfprApVnicFcGroupTemplDn_Type()
)
cfprApVnicFcGroupTemplDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcGroupTemplDn.setStatus("current")
_CfprApVnicFcGroupTemplRn_Type = SnmpAdminString
_CfprApVnicFcGroupTemplRn_Object = MibTableColumn
cfprApVnicFcGroupTemplRn = _CfprApVnicFcGroupTemplRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 16, 1, 3),
    _CfprApVnicFcGroupTemplRn_Type()
)
cfprApVnicFcGroupTemplRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcGroupTemplRn.setStatus("current")
_CfprApVnicFcGroupTemplAdaptorProfileName_Type = SnmpAdminString
_CfprApVnicFcGroupTemplAdaptorProfileName_Object = MibTableColumn
cfprApVnicFcGroupTemplAdaptorProfileName = _CfprApVnicFcGroupTemplAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 16, 1, 4),
    _CfprApVnicFcGroupTemplAdaptorProfileName_Type()
)
cfprApVnicFcGroupTemplAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcGroupTemplAdaptorProfileName.setStatus("current")
_CfprApVnicFcGroupTemplDescr_Type = SnmpAdminString
_CfprApVnicFcGroupTemplDescr_Object = MibTableColumn
cfprApVnicFcGroupTemplDescr = _CfprApVnicFcGroupTemplDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 16, 1, 5),
    _CfprApVnicFcGroupTemplDescr_Type()
)
cfprApVnicFcGroupTemplDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcGroupTemplDescr.setStatus("current")
_CfprApVnicFcGroupTemplIdentPoolName_Type = SnmpAdminString
_CfprApVnicFcGroupTemplIdentPoolName_Object = MibTableColumn
cfprApVnicFcGroupTemplIdentPoolName = _CfprApVnicFcGroupTemplIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 16, 1, 6),
    _CfprApVnicFcGroupTemplIdentPoolName_Type()
)
cfprApVnicFcGroupTemplIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcGroupTemplIdentPoolName.setStatus("current")
_CfprApVnicFcGroupTemplIntId_Type = SnmpAdminString
_CfprApVnicFcGroupTemplIntId_Object = MibTableColumn
cfprApVnicFcGroupTemplIntId = _CfprApVnicFcGroupTemplIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 16, 1, 7),
    _CfprApVnicFcGroupTemplIntId_Type()
)
cfprApVnicFcGroupTemplIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcGroupTemplIntId.setStatus("current")
_CfprApVnicFcGroupTemplMaxDataFieldSize_Type = Gauge32
_CfprApVnicFcGroupTemplMaxDataFieldSize_Object = MibTableColumn
cfprApVnicFcGroupTemplMaxDataFieldSize = _CfprApVnicFcGroupTemplMaxDataFieldSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 16, 1, 8),
    _CfprApVnicFcGroupTemplMaxDataFieldSize_Type()
)
cfprApVnicFcGroupTemplMaxDataFieldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcGroupTemplMaxDataFieldSize.setStatus("current")
_CfprApVnicFcGroupTemplName_Type = SnmpAdminString
_CfprApVnicFcGroupTemplName_Object = MibTableColumn
cfprApVnicFcGroupTemplName = _CfprApVnicFcGroupTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 16, 1, 9),
    _CfprApVnicFcGroupTemplName_Type()
)
cfprApVnicFcGroupTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcGroupTemplName.setStatus("current")
_CfprApVnicFcGroupTemplNwTemplName_Type = SnmpAdminString
_CfprApVnicFcGroupTemplNwTemplName_Object = MibTableColumn
cfprApVnicFcGroupTemplNwTemplName = _CfprApVnicFcGroupTemplNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 16, 1, 10),
    _CfprApVnicFcGroupTemplNwTemplName_Type()
)
cfprApVnicFcGroupTemplNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcGroupTemplNwTemplName.setStatus("current")
_CfprApVnicFcGroupTemplOperStatsPolicyName_Type = SnmpAdminString
_CfprApVnicFcGroupTemplOperStatsPolicyName_Object = MibTableColumn
cfprApVnicFcGroupTemplOperStatsPolicyName = _CfprApVnicFcGroupTemplOperStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 16, 1, 11),
    _CfprApVnicFcGroupTemplOperStatsPolicyName_Type()
)
cfprApVnicFcGroupTemplOperStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcGroupTemplOperStatsPolicyName.setStatus("current")
_CfprApVnicFcGroupTemplPolicyLevel_Type = Gauge32
_CfprApVnicFcGroupTemplPolicyLevel_Object = MibTableColumn
cfprApVnicFcGroupTemplPolicyLevel = _CfprApVnicFcGroupTemplPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 16, 1, 13),
    _CfprApVnicFcGroupTemplPolicyLevel_Type()
)
cfprApVnicFcGroupTemplPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcGroupTemplPolicyLevel.setStatus("current")
_CfprApVnicFcGroupTemplPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApVnicFcGroupTemplPolicyOwner_Object = MibTableColumn
cfprApVnicFcGroupTemplPolicyOwner = _CfprApVnicFcGroupTemplPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 16, 1, 14),
    _CfprApVnicFcGroupTemplPolicyOwner_Type()
)
cfprApVnicFcGroupTemplPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcGroupTemplPolicyOwner.setStatus("current")
_CfprApVnicFcGroupTemplQosPolicyName_Type = SnmpAdminString
_CfprApVnicFcGroupTemplQosPolicyName_Object = MibTableColumn
cfprApVnicFcGroupTemplQosPolicyName = _CfprApVnicFcGroupTemplQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 16, 1, 15),
    _CfprApVnicFcGroupTemplQosPolicyName_Type()
)
cfprApVnicFcGroupTemplQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcGroupTemplQosPolicyName.setStatus("current")
_CfprApVnicFcGroupTemplStatsPolicyName_Type = SnmpAdminString
_CfprApVnicFcGroupTemplStatsPolicyName_Object = MibTableColumn
cfprApVnicFcGroupTemplStatsPolicyName = _CfprApVnicFcGroupTemplStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 16, 1, 16),
    _CfprApVnicFcGroupTemplStatsPolicyName_Type()
)
cfprApVnicFcGroupTemplStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcGroupTemplStatsPolicyName.setStatus("current")
_CfprApVnicFcGroupTemplTemplType_Type = CfprApVnicTemplateType
_CfprApVnicFcGroupTemplTemplType_Object = MibTableColumn
cfprApVnicFcGroupTemplTemplType = _CfprApVnicFcGroupTemplTemplType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 16, 1, 18),
    _CfprApVnicFcGroupTemplTemplType_Type()
)
cfprApVnicFcGroupTemplTemplType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcGroupTemplTemplType.setStatus("current")
_CfprApVnicFcIfTable_Object = MibTable
cfprApVnicFcIfTable = _CfprApVnicFcIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 17)
)
if mibBuilder.loadTexts:
    cfprApVnicFcIfTable.setStatus("current")
_CfprApVnicFcIfEntry_Object = MibTableRow
cfprApVnicFcIfEntry = _CfprApVnicFcIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 17, 1)
)
cfprApVnicFcIfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicFcIfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicFcIfEntry.setStatus("current")
_CfprApVnicFcIfInstanceId_Type = CfprApManagedObjectId
_CfprApVnicFcIfInstanceId_Object = MibTableColumn
cfprApVnicFcIfInstanceId = _CfprApVnicFcIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 17, 1, 1),
    _CfprApVnicFcIfInstanceId_Type()
)
cfprApVnicFcIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicFcIfInstanceId.setStatus("current")
_CfprApVnicFcIfDn_Type = CfprApManagedObjectDn
_CfprApVnicFcIfDn_Object = MibTableColumn
cfprApVnicFcIfDn = _CfprApVnicFcIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 17, 1, 2),
    _CfprApVnicFcIfDn_Type()
)
cfprApVnicFcIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcIfDn.setStatus("current")
_CfprApVnicFcIfRn_Type = SnmpAdminString
_CfprApVnicFcIfRn_Object = MibTableColumn
cfprApVnicFcIfRn = _CfprApVnicFcIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 17, 1, 3),
    _CfprApVnicFcIfRn_Type()
)
cfprApVnicFcIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcIfRn.setStatus("current")
_CfprApVnicFcIfConfigQualifier_Type = CfprApVnicConfigIssues
_CfprApVnicFcIfConfigQualifier_Object = MibTableColumn
cfprApVnicFcIfConfigQualifier = _CfprApVnicFcIfConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 17, 1, 4),
    _CfprApVnicFcIfConfigQualifier_Type()
)
cfprApVnicFcIfConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcIfConfigQualifier.setStatus("current")
_CfprApVnicFcIfInitiator_Type = Unsigned64
_CfprApVnicFcIfInitiator_Object = MibTableColumn
cfprApVnicFcIfInitiator = _CfprApVnicFcIfInitiator_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 17, 1, 5),
    _CfprApVnicFcIfInitiator_Type()
)
cfprApVnicFcIfInitiator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcIfInitiator.setStatus("current")
_CfprApVnicFcIfName_Type = SnmpAdminString
_CfprApVnicFcIfName_Object = MibTableColumn
cfprApVnicFcIfName = _CfprApVnicFcIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 17, 1, 6),
    _CfprApVnicFcIfName_Type()
)
cfprApVnicFcIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcIfName.setStatus("current")
_CfprApVnicFcIfOperState_Type = CfprApVnicIfOperState
_CfprApVnicFcIfOperState_Object = MibTableColumn
cfprApVnicFcIfOperState = _CfprApVnicFcIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 17, 1, 7),
    _CfprApVnicFcIfOperState_Type()
)
cfprApVnicFcIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcIfOperState.setStatus("current")
_CfprApVnicFcIfOperVnetDn_Type = SnmpAdminString
_CfprApVnicFcIfOperVnetDn_Object = MibTableColumn
cfprApVnicFcIfOperVnetDn = _CfprApVnicFcIfOperVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 17, 1, 8),
    _CfprApVnicFcIfOperVnetDn_Type()
)
cfprApVnicFcIfOperVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcIfOperVnetDn.setStatus("current")
_CfprApVnicFcIfOperVnetName_Type = SnmpAdminString
_CfprApVnicFcIfOperVnetName_Object = MibTableColumn
cfprApVnicFcIfOperVnetName = _CfprApVnicFcIfOperVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 17, 1, 9),
    _CfprApVnicFcIfOperVnetName_Type()
)
cfprApVnicFcIfOperVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcIfOperVnetName.setStatus("current")
_CfprApVnicFcIfOwner_Type = CfprApVnicConnectionOwner
_CfprApVnicFcIfOwner_Object = MibTableColumn
cfprApVnicFcIfOwner = _CfprApVnicFcIfOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 17, 1, 10),
    _CfprApVnicFcIfOwner_Type()
)
cfprApVnicFcIfOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcIfOwner.setStatus("current")
_CfprApVnicFcIfPubNwId_Type = Gauge32
_CfprApVnicFcIfPubNwId_Object = MibTableColumn
cfprApVnicFcIfPubNwId = _CfprApVnicFcIfPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 17, 1, 11),
    _CfprApVnicFcIfPubNwId_Type()
)
cfprApVnicFcIfPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcIfPubNwId.setStatus("current")
_CfprApVnicFcIfSharing_Type = CfprApFabricVlanSharingType
_CfprApVnicFcIfSharing_Object = MibTableColumn
cfprApVnicFcIfSharing = _CfprApVnicFcIfSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 17, 1, 12),
    _CfprApVnicFcIfSharing_Type()
)
cfprApVnicFcIfSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcIfSharing.setStatus("current")
_CfprApVnicFcIfSwitchId_Type = CfprApVnicL2IfSwitchId
_CfprApVnicFcIfSwitchId_Object = MibTableColumn
cfprApVnicFcIfSwitchId = _CfprApVnicFcIfSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 17, 1, 13),
    _CfprApVnicFcIfSwitchId_Type()
)
cfprApVnicFcIfSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcIfSwitchId.setStatus("current")
_CfprApVnicFcIfType_Type = CfprApVnicAFcIfType
_CfprApVnicFcIfType_Object = MibTableColumn
cfprApVnicFcIfType = _CfprApVnicFcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 17, 1, 14),
    _CfprApVnicFcIfType_Type()
)
cfprApVnicFcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcIfType.setStatus("current")
_CfprApVnicFcIfVnet_Type = Gauge32
_CfprApVnicFcIfVnet_Object = MibTableColumn
cfprApVnicFcIfVnet = _CfprApVnicFcIfVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 17, 1, 15),
    _CfprApVnicFcIfVnet_Type()
)
cfprApVnicFcIfVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcIfVnet.setStatus("current")
_CfprApVnicFcLifTable_Object = MibTable
cfprApVnicFcLifTable = _CfprApVnicFcLifTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 18)
)
if mibBuilder.loadTexts:
    cfprApVnicFcLifTable.setStatus("current")
_CfprApVnicFcLifEntry_Object = MibTableRow
cfprApVnicFcLifEntry = _CfprApVnicFcLifEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 18, 1)
)
cfprApVnicFcLifEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicFcLifInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicFcLifEntry.setStatus("current")
_CfprApVnicFcLifInstanceId_Type = CfprApManagedObjectId
_CfprApVnicFcLifInstanceId_Object = MibTableColumn
cfprApVnicFcLifInstanceId = _CfprApVnicFcLifInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 18, 1, 1),
    _CfprApVnicFcLifInstanceId_Type()
)
cfprApVnicFcLifInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicFcLifInstanceId.setStatus("current")
_CfprApVnicFcLifDn_Type = CfprApManagedObjectDn
_CfprApVnicFcLifDn_Object = MibTableColumn
cfprApVnicFcLifDn = _CfprApVnicFcLifDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 18, 1, 2),
    _CfprApVnicFcLifDn_Type()
)
cfprApVnicFcLifDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcLifDn.setStatus("current")
_CfprApVnicFcLifRn_Type = SnmpAdminString
_CfprApVnicFcLifRn_Object = MibTableColumn
cfprApVnicFcLifRn = _CfprApVnicFcLifRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 18, 1, 3),
    _CfprApVnicFcLifRn_Type()
)
cfprApVnicFcLifRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcLifRn.setStatus("current")
_CfprApVnicFcLifAddr_Type = Unsigned64
_CfprApVnicFcLifAddr_Object = MibTableColumn
cfprApVnicFcLifAddr = _CfprApVnicFcLifAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 18, 1, 4),
    _CfprApVnicFcLifAddr_Type()
)
cfprApVnicFcLifAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcLifAddr.setStatus("current")
_CfprApVnicFcLifName_Type = SnmpAdminString
_CfprApVnicFcLifName_Object = MibTableColumn
cfprApVnicFcLifName = _CfprApVnicFcLifName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 18, 1, 5),
    _CfprApVnicFcLifName_Type()
)
cfprApVnicFcLifName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcLifName.setStatus("current")
_CfprApVnicFcLifNicDn_Type = SnmpAdminString
_CfprApVnicFcLifNicDn_Object = MibTableColumn
cfprApVnicFcLifNicDn = _CfprApVnicFcLifNicDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 18, 1, 6),
    _CfprApVnicFcLifNicDn_Type()
)
cfprApVnicFcLifNicDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcLifNicDn.setStatus("current")
_CfprApVnicFcLifOwner_Type = CfprApVnicConnectionOwner
_CfprApVnicFcLifOwner_Object = MibTableColumn
cfprApVnicFcLifOwner = _CfprApVnicFcLifOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 18, 1, 7),
    _CfprApVnicFcLifOwner_Type()
)
cfprApVnicFcLifOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcLifOwner.setStatus("current")
_CfprApVnicFcLifSwitchId_Type = CfprApNetworkSwitchId
_CfprApVnicFcLifSwitchId_Object = MibTableColumn
cfprApVnicFcLifSwitchId = _CfprApVnicFcLifSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 18, 1, 8),
    _CfprApVnicFcLifSwitchId_Type()
)
cfprApVnicFcLifSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcLifSwitchId.setStatus("current")
_CfprApVnicFcLifType_Type = CfprApVnicConnectionType
_CfprApVnicFcLifType_Object = MibTableColumn
cfprApVnicFcLifType = _CfprApVnicFcLifType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 18, 1, 9),
    _CfprApVnicFcLifType_Type()
)
cfprApVnicFcLifType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcLifType.setStatus("current")
_CfprApVnicFcLifVnicDn_Type = SnmpAdminString
_CfprApVnicFcLifVnicDn_Object = MibTableColumn
cfprApVnicFcLifVnicDn = _CfprApVnicFcLifVnicDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 18, 1, 10),
    _CfprApVnicFcLifVnicDn_Type()
)
cfprApVnicFcLifVnicDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcLifVnicDn.setStatus("current")
_CfprApVnicFcOEIfTable_Object = MibTable
cfprApVnicFcOEIfTable = _CfprApVnicFcOEIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 20)
)
if mibBuilder.loadTexts:
    cfprApVnicFcOEIfTable.setStatus("current")
_CfprApVnicFcOEIfEntry_Object = MibTableRow
cfprApVnicFcOEIfEntry = _CfprApVnicFcOEIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 20, 1)
)
cfprApVnicFcOEIfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicFcOEIfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicFcOEIfEntry.setStatus("current")
_CfprApVnicFcOEIfInstanceId_Type = CfprApManagedObjectId
_CfprApVnicFcOEIfInstanceId_Object = MibTableColumn
cfprApVnicFcOEIfInstanceId = _CfprApVnicFcOEIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 20, 1, 1),
    _CfprApVnicFcOEIfInstanceId_Type()
)
cfprApVnicFcOEIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicFcOEIfInstanceId.setStatus("current")
_CfprApVnicFcOEIfDn_Type = CfprApManagedObjectDn
_CfprApVnicFcOEIfDn_Object = MibTableColumn
cfprApVnicFcOEIfDn = _CfprApVnicFcOEIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 20, 1, 2),
    _CfprApVnicFcOEIfDn_Type()
)
cfprApVnicFcOEIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcOEIfDn.setStatus("current")
_CfprApVnicFcOEIfRn_Type = SnmpAdminString
_CfprApVnicFcOEIfRn_Object = MibTableColumn
cfprApVnicFcOEIfRn = _CfprApVnicFcOEIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 20, 1, 3),
    _CfprApVnicFcOEIfRn_Type()
)
cfprApVnicFcOEIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcOEIfRn.setStatus("current")
_CfprApVnicFcOEIfConfigQualifier_Type = CfprApVnicConfigIssues
_CfprApVnicFcOEIfConfigQualifier_Object = MibTableColumn
cfprApVnicFcOEIfConfigQualifier = _CfprApVnicFcOEIfConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 20, 1, 4),
    _CfprApVnicFcOEIfConfigQualifier_Type()
)
cfprApVnicFcOEIfConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcOEIfConfigQualifier.setStatus("current")
_CfprApVnicFcOEIfInitiator_Type = Unsigned64
_CfprApVnicFcOEIfInitiator_Object = MibTableColumn
cfprApVnicFcOEIfInitiator = _CfprApVnicFcOEIfInitiator_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 20, 1, 5),
    _CfprApVnicFcOEIfInitiator_Type()
)
cfprApVnicFcOEIfInitiator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcOEIfInitiator.setStatus("current")
_CfprApVnicFcOEIfName_Type = SnmpAdminString
_CfprApVnicFcOEIfName_Object = MibTableColumn
cfprApVnicFcOEIfName = _CfprApVnicFcOEIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 20, 1, 6),
    _CfprApVnicFcOEIfName_Type()
)
cfprApVnicFcOEIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcOEIfName.setStatus("current")
_CfprApVnicFcOEIfOperState_Type = CfprApVnicIfOperState
_CfprApVnicFcOEIfOperState_Object = MibTableColumn
cfprApVnicFcOEIfOperState = _CfprApVnicFcOEIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 20, 1, 7),
    _CfprApVnicFcOEIfOperState_Type()
)
cfprApVnicFcOEIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcOEIfOperState.setStatus("current")
_CfprApVnicFcOEIfOperVnetDn_Type = SnmpAdminString
_CfprApVnicFcOEIfOperVnetDn_Object = MibTableColumn
cfprApVnicFcOEIfOperVnetDn = _CfprApVnicFcOEIfOperVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 20, 1, 8),
    _CfprApVnicFcOEIfOperVnetDn_Type()
)
cfprApVnicFcOEIfOperVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcOEIfOperVnetDn.setStatus("current")
_CfprApVnicFcOEIfOperVnetName_Type = SnmpAdminString
_CfprApVnicFcOEIfOperVnetName_Object = MibTableColumn
cfprApVnicFcOEIfOperVnetName = _CfprApVnicFcOEIfOperVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 20, 1, 9),
    _CfprApVnicFcOEIfOperVnetName_Type()
)
cfprApVnicFcOEIfOperVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcOEIfOperVnetName.setStatus("current")
_CfprApVnicFcOEIfOwner_Type = CfprApVnicConnectionOwner
_CfprApVnicFcOEIfOwner_Object = MibTableColumn
cfprApVnicFcOEIfOwner = _CfprApVnicFcOEIfOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 20, 1, 10),
    _CfprApVnicFcOEIfOwner_Type()
)
cfprApVnicFcOEIfOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcOEIfOwner.setStatus("current")
_CfprApVnicFcOEIfPubNwId_Type = Gauge32
_CfprApVnicFcOEIfPubNwId_Object = MibTableColumn
cfprApVnicFcOEIfPubNwId = _CfprApVnicFcOEIfPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 20, 1, 11),
    _CfprApVnicFcOEIfPubNwId_Type()
)
cfprApVnicFcOEIfPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcOEIfPubNwId.setStatus("current")
_CfprApVnicFcOEIfSharing_Type = CfprApFabricVlanSharingType
_CfprApVnicFcOEIfSharing_Object = MibTableColumn
cfprApVnicFcOEIfSharing = _CfprApVnicFcOEIfSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 20, 1, 12),
    _CfprApVnicFcOEIfSharing_Type()
)
cfprApVnicFcOEIfSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcOEIfSharing.setStatus("current")
_CfprApVnicFcOEIfSwitchId_Type = CfprApVnicL2IfSwitchId
_CfprApVnicFcOEIfSwitchId_Object = MibTableColumn
cfprApVnicFcOEIfSwitchId = _CfprApVnicFcOEIfSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 20, 1, 13),
    _CfprApVnicFcOEIfSwitchId_Type()
)
cfprApVnicFcOEIfSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcOEIfSwitchId.setStatus("current")
_CfprApVnicFcOEIfType_Type = CfprApVnicAFcIfType
_CfprApVnicFcOEIfType_Object = MibTableColumn
cfprApVnicFcOEIfType = _CfprApVnicFcOEIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 20, 1, 14),
    _CfprApVnicFcOEIfType_Type()
)
cfprApVnicFcOEIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcOEIfType.setStatus("current")
_CfprApVnicFcOEIfVnet_Type = Gauge32
_CfprApVnicFcOEIfVnet_Object = MibTableColumn
cfprApVnicFcOEIfVnet = _CfprApVnicFcOEIfVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 20, 1, 15),
    _CfprApVnicFcOEIfVnet_Type()
)
cfprApVnicFcOEIfVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicFcOEIfVnet.setStatus("current")
_CfprApVnicIPv4DhcpTable_Object = MibTable
cfprApVnicIPv4DhcpTable = _CfprApVnicIPv4DhcpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 21)
)
if mibBuilder.loadTexts:
    cfprApVnicIPv4DhcpTable.setStatus("current")
_CfprApVnicIPv4DhcpEntry_Object = MibTableRow
cfprApVnicIPv4DhcpEntry = _CfprApVnicIPv4DhcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 21, 1)
)
cfprApVnicIPv4DhcpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicIPv4DhcpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicIPv4DhcpEntry.setStatus("current")
_CfprApVnicIPv4DhcpInstanceId_Type = CfprApManagedObjectId
_CfprApVnicIPv4DhcpInstanceId_Object = MibTableColumn
cfprApVnicIPv4DhcpInstanceId = _CfprApVnicIPv4DhcpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 21, 1, 1),
    _CfprApVnicIPv4DhcpInstanceId_Type()
)
cfprApVnicIPv4DhcpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicIPv4DhcpInstanceId.setStatus("current")
_CfprApVnicIPv4DhcpDn_Type = CfprApManagedObjectDn
_CfprApVnicIPv4DhcpDn_Object = MibTableColumn
cfprApVnicIPv4DhcpDn = _CfprApVnicIPv4DhcpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 21, 1, 2),
    _CfprApVnicIPv4DhcpDn_Type()
)
cfprApVnicIPv4DhcpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4DhcpDn.setStatus("current")
_CfprApVnicIPv4DhcpRn_Type = SnmpAdminString
_CfprApVnicIPv4DhcpRn_Object = MibTableColumn
cfprApVnicIPv4DhcpRn = _CfprApVnicIPv4DhcpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 21, 1, 3),
    _CfprApVnicIPv4DhcpRn_Type()
)
cfprApVnicIPv4DhcpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4DhcpRn.setStatus("current")
_CfprApVnicIPv4DhcpAddr_Type = InetAddressIPv4
_CfprApVnicIPv4DhcpAddr_Object = MibTableColumn
cfprApVnicIPv4DhcpAddr = _CfprApVnicIPv4DhcpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 21, 1, 4),
    _CfprApVnicIPv4DhcpAddr_Type()
)
cfprApVnicIPv4DhcpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4DhcpAddr.setStatus("current")
_CfprApVnicIPv4DhcpDefGw_Type = InetAddressIPv4
_CfprApVnicIPv4DhcpDefGw_Object = MibTableColumn
cfprApVnicIPv4DhcpDefGw = _CfprApVnicIPv4DhcpDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 21, 1, 5),
    _CfprApVnicIPv4DhcpDefGw_Type()
)
cfprApVnicIPv4DhcpDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4DhcpDefGw.setStatus("current")
_CfprApVnicIPv4DhcpSubnet_Type = InetAddressIPv4
_CfprApVnicIPv4DhcpSubnet_Object = MibTableColumn
cfprApVnicIPv4DhcpSubnet = _CfprApVnicIPv4DhcpSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 21, 1, 6),
    _CfprApVnicIPv4DhcpSubnet_Type()
)
cfprApVnicIPv4DhcpSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4DhcpSubnet.setStatus("current")
_CfprApVnicIPv4DnsTable_Object = MibTable
cfprApVnicIPv4DnsTable = _CfprApVnicIPv4DnsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 22)
)
if mibBuilder.loadTexts:
    cfprApVnicIPv4DnsTable.setStatus("current")
_CfprApVnicIPv4DnsEntry_Object = MibTableRow
cfprApVnicIPv4DnsEntry = _CfprApVnicIPv4DnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 22, 1)
)
cfprApVnicIPv4DnsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicIPv4DnsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicIPv4DnsEntry.setStatus("current")
_CfprApVnicIPv4DnsInstanceId_Type = CfprApManagedObjectId
_CfprApVnicIPv4DnsInstanceId_Object = MibTableColumn
cfprApVnicIPv4DnsInstanceId = _CfprApVnicIPv4DnsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 22, 1, 1),
    _CfprApVnicIPv4DnsInstanceId_Type()
)
cfprApVnicIPv4DnsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicIPv4DnsInstanceId.setStatus("current")
_CfprApVnicIPv4DnsDn_Type = CfprApManagedObjectDn
_CfprApVnicIPv4DnsDn_Object = MibTableColumn
cfprApVnicIPv4DnsDn = _CfprApVnicIPv4DnsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 22, 1, 2),
    _CfprApVnicIPv4DnsDn_Type()
)
cfprApVnicIPv4DnsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4DnsDn.setStatus("current")
_CfprApVnicIPv4DnsRn_Type = SnmpAdminString
_CfprApVnicIPv4DnsRn_Object = MibTableColumn
cfprApVnicIPv4DnsRn = _CfprApVnicIPv4DnsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 22, 1, 3),
    _CfprApVnicIPv4DnsRn_Type()
)
cfprApVnicIPv4DnsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4DnsRn.setStatus("current")
_CfprApVnicIPv4DnsAddr_Type = InetAddressIPv4
_CfprApVnicIPv4DnsAddr_Object = MibTableColumn
cfprApVnicIPv4DnsAddr = _CfprApVnicIPv4DnsAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 22, 1, 4),
    _CfprApVnicIPv4DnsAddr_Type()
)
cfprApVnicIPv4DnsAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4DnsAddr.setStatus("current")
_CfprApVnicIPv4DnsDefGw_Type = InetAddressIPv4
_CfprApVnicIPv4DnsDefGw_Object = MibTableColumn
cfprApVnicIPv4DnsDefGw = _CfprApVnicIPv4DnsDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 22, 1, 5),
    _CfprApVnicIPv4DnsDefGw_Type()
)
cfprApVnicIPv4DnsDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4DnsDefGw.setStatus("current")
_CfprApVnicIPv4DnsPref_Type = CfprApVnicIPv4DnsPref
_CfprApVnicIPv4DnsPref_Object = MibTableColumn
cfprApVnicIPv4DnsPref = _CfprApVnicIPv4DnsPref_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 22, 1, 6),
    _CfprApVnicIPv4DnsPref_Type()
)
cfprApVnicIPv4DnsPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4DnsPref.setStatus("current")
_CfprApVnicIPv4DnsSubnet_Type = InetAddressIPv4
_CfprApVnicIPv4DnsSubnet_Object = MibTableColumn
cfprApVnicIPv4DnsSubnet = _CfprApVnicIPv4DnsSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 22, 1, 7),
    _CfprApVnicIPv4DnsSubnet_Type()
)
cfprApVnicIPv4DnsSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4DnsSubnet.setStatus("current")
_CfprApVnicIPv4IfTable_Object = MibTable
cfprApVnicIPv4IfTable = _CfprApVnicIPv4IfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 23)
)
if mibBuilder.loadTexts:
    cfprApVnicIPv4IfTable.setStatus("current")
_CfprApVnicIPv4IfEntry_Object = MibTableRow
cfprApVnicIPv4IfEntry = _CfprApVnicIPv4IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 23, 1)
)
cfprApVnicIPv4IfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicIPv4IfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicIPv4IfEntry.setStatus("current")
_CfprApVnicIPv4IfInstanceId_Type = CfprApManagedObjectId
_CfprApVnicIPv4IfInstanceId_Object = MibTableColumn
cfprApVnicIPv4IfInstanceId = _CfprApVnicIPv4IfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 23, 1, 1),
    _CfprApVnicIPv4IfInstanceId_Type()
)
cfprApVnicIPv4IfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicIPv4IfInstanceId.setStatus("current")
_CfprApVnicIPv4IfDn_Type = CfprApManagedObjectDn
_CfprApVnicIPv4IfDn_Object = MibTableColumn
cfprApVnicIPv4IfDn = _CfprApVnicIPv4IfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 23, 1, 2),
    _CfprApVnicIPv4IfDn_Type()
)
cfprApVnicIPv4IfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4IfDn.setStatus("current")
_CfprApVnicIPv4IfRn_Type = SnmpAdminString
_CfprApVnicIPv4IfRn_Object = MibTableColumn
cfprApVnicIPv4IfRn = _CfprApVnicIPv4IfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 23, 1, 3),
    _CfprApVnicIPv4IfRn_Type()
)
cfprApVnicIPv4IfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4IfRn.setStatus("current")
_CfprApVnicIPv4IfAddr_Type = InetAddressIPv4
_CfprApVnicIPv4IfAddr_Object = MibTableColumn
cfprApVnicIPv4IfAddr = _CfprApVnicIPv4IfAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 23, 1, 4),
    _CfprApVnicIPv4IfAddr_Type()
)
cfprApVnicIPv4IfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4IfAddr.setStatus("current")
_CfprApVnicIPv4IfConfigQualifier_Type = CfprApVnicConfigIssues
_CfprApVnicIPv4IfConfigQualifier_Object = MibTableColumn
cfprApVnicIPv4IfConfigQualifier = _CfprApVnicIPv4IfConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 23, 1, 5),
    _CfprApVnicIPv4IfConfigQualifier_Type()
)
cfprApVnicIPv4IfConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4IfConfigQualifier.setStatus("current")
_CfprApVnicIPv4IfName_Type = SnmpAdminString
_CfprApVnicIPv4IfName_Object = MibTableColumn
cfprApVnicIPv4IfName = _CfprApVnicIPv4IfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 23, 1, 6),
    _CfprApVnicIPv4IfName_Type()
)
cfprApVnicIPv4IfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4IfName.setStatus("current")
_CfprApVnicIPv4IfOperState_Type = CfprApVnicIfOperState
_CfprApVnicIPv4IfOperState_Object = MibTableColumn
cfprApVnicIPv4IfOperState = _CfprApVnicIPv4IfOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 23, 1, 7),
    _CfprApVnicIPv4IfOperState_Type()
)
cfprApVnicIPv4IfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4IfOperState.setStatus("current")
_CfprApVnicIPv4IfOperVnetDn_Type = SnmpAdminString
_CfprApVnicIPv4IfOperVnetDn_Object = MibTableColumn
cfprApVnicIPv4IfOperVnetDn = _CfprApVnicIPv4IfOperVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 23, 1, 8),
    _CfprApVnicIPv4IfOperVnetDn_Type()
)
cfprApVnicIPv4IfOperVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4IfOperVnetDn.setStatus("current")
_CfprApVnicIPv4IfOperVnetName_Type = SnmpAdminString
_CfprApVnicIPv4IfOperVnetName_Object = MibTableColumn
cfprApVnicIPv4IfOperVnetName = _CfprApVnicIPv4IfOperVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 23, 1, 9),
    _CfprApVnicIPv4IfOperVnetName_Type()
)
cfprApVnicIPv4IfOperVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4IfOperVnetName.setStatus("current")
_CfprApVnicIPv4IfOwner_Type = CfprApVnicConnectionOwner
_CfprApVnicIPv4IfOwner_Object = MibTableColumn
cfprApVnicIPv4IfOwner = _CfprApVnicIPv4IfOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 23, 1, 10),
    _CfprApVnicIPv4IfOwner_Type()
)
cfprApVnicIPv4IfOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4IfOwner.setStatus("current")
_CfprApVnicIPv4IfPubNwId_Type = Gauge32
_CfprApVnicIPv4IfPubNwId_Object = MibTableColumn
cfprApVnicIPv4IfPubNwId = _CfprApVnicIPv4IfPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 23, 1, 11),
    _CfprApVnicIPv4IfPubNwId_Type()
)
cfprApVnicIPv4IfPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4IfPubNwId.setStatus("current")
_CfprApVnicIPv4IfSharing_Type = CfprApFabricVlanSharingType
_CfprApVnicIPv4IfSharing_Object = MibTableColumn
cfprApVnicIPv4IfSharing = _CfprApVnicIPv4IfSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 23, 1, 12),
    _CfprApVnicIPv4IfSharing_Type()
)
cfprApVnicIPv4IfSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4IfSharing.setStatus("current")
_CfprApVnicIPv4IfSwitchId_Type = CfprApNetworkSwitchId
_CfprApVnicIPv4IfSwitchId_Object = MibTableColumn
cfprApVnicIPv4IfSwitchId = _CfprApVnicIPv4IfSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 23, 1, 13),
    _CfprApVnicIPv4IfSwitchId_Type()
)
cfprApVnicIPv4IfSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4IfSwitchId.setStatus("current")
_CfprApVnicIPv4IfType_Type = CfprApVnicConnectionType
_CfprApVnicIPv4IfType_Object = MibTableColumn
cfprApVnicIPv4IfType = _CfprApVnicIPv4IfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 23, 1, 14),
    _CfprApVnicIPv4IfType_Type()
)
cfprApVnicIPv4IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4IfType.setStatus("current")
_CfprApVnicIPv4IfVnet_Type = Gauge32
_CfprApVnicIPv4IfVnet_Object = MibTableColumn
cfprApVnicIPv4IfVnet = _CfprApVnicIPv4IfVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 23, 1, 15),
    _CfprApVnicIPv4IfVnet_Type()
)
cfprApVnicIPv4IfVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4IfVnet.setStatus("current")
_CfprApVnicIPv4IscsiAddrTable_Object = MibTable
cfprApVnicIPv4IscsiAddrTable = _CfprApVnicIPv4IscsiAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 24)
)
if mibBuilder.loadTexts:
    cfprApVnicIPv4IscsiAddrTable.setStatus("current")
_CfprApVnicIPv4IscsiAddrEntry_Object = MibTableRow
cfprApVnicIPv4IscsiAddrEntry = _CfprApVnicIPv4IscsiAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 24, 1)
)
cfprApVnicIPv4IscsiAddrEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicIPv4IscsiAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicIPv4IscsiAddrEntry.setStatus("current")
_CfprApVnicIPv4IscsiAddrInstanceId_Type = CfprApManagedObjectId
_CfprApVnicIPv4IscsiAddrInstanceId_Object = MibTableColumn
cfprApVnicIPv4IscsiAddrInstanceId = _CfprApVnicIPv4IscsiAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 24, 1, 1),
    _CfprApVnicIPv4IscsiAddrInstanceId_Type()
)
cfprApVnicIPv4IscsiAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicIPv4IscsiAddrInstanceId.setStatus("current")
_CfprApVnicIPv4IscsiAddrDn_Type = CfprApManagedObjectDn
_CfprApVnicIPv4IscsiAddrDn_Object = MibTableColumn
cfprApVnicIPv4IscsiAddrDn = _CfprApVnicIPv4IscsiAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 24, 1, 2),
    _CfprApVnicIPv4IscsiAddrDn_Type()
)
cfprApVnicIPv4IscsiAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4IscsiAddrDn.setStatus("current")
_CfprApVnicIPv4IscsiAddrRn_Type = SnmpAdminString
_CfprApVnicIPv4IscsiAddrRn_Object = MibTableColumn
cfprApVnicIPv4IscsiAddrRn = _CfprApVnicIPv4IscsiAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 24, 1, 3),
    _CfprApVnicIPv4IscsiAddrRn_Type()
)
cfprApVnicIPv4IscsiAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4IscsiAddrRn.setStatus("current")
_CfprApVnicIPv4IscsiAddrAddr_Type = InetAddressIPv4
_CfprApVnicIPv4IscsiAddrAddr_Object = MibTableColumn
cfprApVnicIPv4IscsiAddrAddr = _CfprApVnicIPv4IscsiAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 24, 1, 4),
    _CfprApVnicIPv4IscsiAddrAddr_Type()
)
cfprApVnicIPv4IscsiAddrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4IscsiAddrAddr.setStatus("current")
_CfprApVnicIPv4IscsiAddrDefGw_Type = InetAddressIPv4
_CfprApVnicIPv4IscsiAddrDefGw_Object = MibTableColumn
cfprApVnicIPv4IscsiAddrDefGw = _CfprApVnicIPv4IscsiAddrDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 24, 1, 5),
    _CfprApVnicIPv4IscsiAddrDefGw_Type()
)
cfprApVnicIPv4IscsiAddrDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4IscsiAddrDefGw.setStatus("current")
_CfprApVnicIPv4IscsiAddrPrimDns_Type = InetAddressIPv4
_CfprApVnicIPv4IscsiAddrPrimDns_Object = MibTableColumn
cfprApVnicIPv4IscsiAddrPrimDns = _CfprApVnicIPv4IscsiAddrPrimDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 24, 1, 6),
    _CfprApVnicIPv4IscsiAddrPrimDns_Type()
)
cfprApVnicIPv4IscsiAddrPrimDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4IscsiAddrPrimDns.setStatus("current")
_CfprApVnicIPv4IscsiAddrSecDns_Type = InetAddressIPv4
_CfprApVnicIPv4IscsiAddrSecDns_Object = MibTableColumn
cfprApVnicIPv4IscsiAddrSecDns = _CfprApVnicIPv4IscsiAddrSecDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 24, 1, 7),
    _CfprApVnicIPv4IscsiAddrSecDns_Type()
)
cfprApVnicIPv4IscsiAddrSecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4IscsiAddrSecDns.setStatus("current")
_CfprApVnicIPv4IscsiAddrSubnet_Type = InetAddressIPv4
_CfprApVnicIPv4IscsiAddrSubnet_Object = MibTableColumn
cfprApVnicIPv4IscsiAddrSubnet = _CfprApVnicIPv4IscsiAddrSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 24, 1, 8),
    _CfprApVnicIPv4IscsiAddrSubnet_Type()
)
cfprApVnicIPv4IscsiAddrSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4IscsiAddrSubnet.setStatus("current")
_CfprApVnicIPv4PooledIscsiAddrTable_Object = MibTable
cfprApVnicIPv4PooledIscsiAddrTable = _CfprApVnicIPv4PooledIscsiAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 25)
)
if mibBuilder.loadTexts:
    cfprApVnicIPv4PooledIscsiAddrTable.setStatus("current")
_CfprApVnicIPv4PooledIscsiAddrEntry_Object = MibTableRow
cfprApVnicIPv4PooledIscsiAddrEntry = _CfprApVnicIPv4PooledIscsiAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 25, 1)
)
cfprApVnicIPv4PooledIscsiAddrEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicIPv4PooledIscsiAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicIPv4PooledIscsiAddrEntry.setStatus("current")
_CfprApVnicIPv4PooledIscsiAddrInstanceId_Type = CfprApManagedObjectId
_CfprApVnicIPv4PooledIscsiAddrInstanceId_Object = MibTableColumn
cfprApVnicIPv4PooledIscsiAddrInstanceId = _CfprApVnicIPv4PooledIscsiAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 25, 1, 1),
    _CfprApVnicIPv4PooledIscsiAddrInstanceId_Type()
)
cfprApVnicIPv4PooledIscsiAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicIPv4PooledIscsiAddrInstanceId.setStatus("current")
_CfprApVnicIPv4PooledIscsiAddrDn_Type = CfprApManagedObjectDn
_CfprApVnicIPv4PooledIscsiAddrDn_Object = MibTableColumn
cfprApVnicIPv4PooledIscsiAddrDn = _CfprApVnicIPv4PooledIscsiAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 25, 1, 2),
    _CfprApVnicIPv4PooledIscsiAddrDn_Type()
)
cfprApVnicIPv4PooledIscsiAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4PooledIscsiAddrDn.setStatus("current")
_CfprApVnicIPv4PooledIscsiAddrRn_Type = SnmpAdminString
_CfprApVnicIPv4PooledIscsiAddrRn_Object = MibTableColumn
cfprApVnicIPv4PooledIscsiAddrRn = _CfprApVnicIPv4PooledIscsiAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 25, 1, 3),
    _CfprApVnicIPv4PooledIscsiAddrRn_Type()
)
cfprApVnicIPv4PooledIscsiAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4PooledIscsiAddrRn.setStatus("current")
_CfprApVnicIPv4PooledIscsiAddrAddr_Type = InetAddressIPv4
_CfprApVnicIPv4PooledIscsiAddrAddr_Object = MibTableColumn
cfprApVnicIPv4PooledIscsiAddrAddr = _CfprApVnicIPv4PooledIscsiAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 25, 1, 4),
    _CfprApVnicIPv4PooledIscsiAddrAddr_Type()
)
cfprApVnicIPv4PooledIscsiAddrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4PooledIscsiAddrAddr.setStatus("current")
_CfprApVnicIPv4PooledIscsiAddrDefGw_Type = InetAddressIPv4
_CfprApVnicIPv4PooledIscsiAddrDefGw_Object = MibTableColumn
cfprApVnicIPv4PooledIscsiAddrDefGw = _CfprApVnicIPv4PooledIscsiAddrDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 25, 1, 5),
    _CfprApVnicIPv4PooledIscsiAddrDefGw_Type()
)
cfprApVnicIPv4PooledIscsiAddrDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4PooledIscsiAddrDefGw.setStatus("current")
_CfprApVnicIPv4PooledIscsiAddrIdentPoolName_Type = SnmpAdminString
_CfprApVnicIPv4PooledIscsiAddrIdentPoolName_Object = MibTableColumn
cfprApVnicIPv4PooledIscsiAddrIdentPoolName = _CfprApVnicIPv4PooledIscsiAddrIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 25, 1, 6),
    _CfprApVnicIPv4PooledIscsiAddrIdentPoolName_Type()
)
cfprApVnicIPv4PooledIscsiAddrIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4PooledIscsiAddrIdentPoolName.setStatus("current")
_CfprApVnicIPv4PooledIscsiAddrOperIdentPoolName_Type = SnmpAdminString
_CfprApVnicIPv4PooledIscsiAddrOperIdentPoolName_Object = MibTableColumn
cfprApVnicIPv4PooledIscsiAddrOperIdentPoolName = _CfprApVnicIPv4PooledIscsiAddrOperIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 25, 1, 7),
    _CfprApVnicIPv4PooledIscsiAddrOperIdentPoolName_Type()
)
cfprApVnicIPv4PooledIscsiAddrOperIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4PooledIscsiAddrOperIdentPoolName.setStatus("current")
_CfprApVnicIPv4PooledIscsiAddrPrimDns_Type = InetAddressIPv4
_CfprApVnicIPv4PooledIscsiAddrPrimDns_Object = MibTableColumn
cfprApVnicIPv4PooledIscsiAddrPrimDns = _CfprApVnicIPv4PooledIscsiAddrPrimDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 25, 1, 8),
    _CfprApVnicIPv4PooledIscsiAddrPrimDns_Type()
)
cfprApVnicIPv4PooledIscsiAddrPrimDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4PooledIscsiAddrPrimDns.setStatus("current")
_CfprApVnicIPv4PooledIscsiAddrSecDns_Type = InetAddressIPv4
_CfprApVnicIPv4PooledIscsiAddrSecDns_Object = MibTableColumn
cfprApVnicIPv4PooledIscsiAddrSecDns = _CfprApVnicIPv4PooledIscsiAddrSecDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 25, 1, 9),
    _CfprApVnicIPv4PooledIscsiAddrSecDns_Type()
)
cfprApVnicIPv4PooledIscsiAddrSecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4PooledIscsiAddrSecDns.setStatus("current")
_CfprApVnicIPv4PooledIscsiAddrSubnet_Type = InetAddressIPv4
_CfprApVnicIPv4PooledIscsiAddrSubnet_Object = MibTableColumn
cfprApVnicIPv4PooledIscsiAddrSubnet = _CfprApVnicIPv4PooledIscsiAddrSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 25, 1, 10),
    _CfprApVnicIPv4PooledIscsiAddrSubnet_Type()
)
cfprApVnicIPv4PooledIscsiAddrSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4PooledIscsiAddrSubnet.setStatus("current")
_CfprApVnicIPv4StaticRouteTable_Object = MibTable
cfprApVnicIPv4StaticRouteTable = _CfprApVnicIPv4StaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 26)
)
if mibBuilder.loadTexts:
    cfprApVnicIPv4StaticRouteTable.setStatus("current")
_CfprApVnicIPv4StaticRouteEntry_Object = MibTableRow
cfprApVnicIPv4StaticRouteEntry = _CfprApVnicIPv4StaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 26, 1)
)
cfprApVnicIPv4StaticRouteEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicIPv4StaticRouteInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicIPv4StaticRouteEntry.setStatus("current")
_CfprApVnicIPv4StaticRouteInstanceId_Type = CfprApManagedObjectId
_CfprApVnicIPv4StaticRouteInstanceId_Object = MibTableColumn
cfprApVnicIPv4StaticRouteInstanceId = _CfprApVnicIPv4StaticRouteInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 26, 1, 1),
    _CfprApVnicIPv4StaticRouteInstanceId_Type()
)
cfprApVnicIPv4StaticRouteInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicIPv4StaticRouteInstanceId.setStatus("current")
_CfprApVnicIPv4StaticRouteDn_Type = CfprApManagedObjectDn
_CfprApVnicIPv4StaticRouteDn_Object = MibTableColumn
cfprApVnicIPv4StaticRouteDn = _CfprApVnicIPv4StaticRouteDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 26, 1, 2),
    _CfprApVnicIPv4StaticRouteDn_Type()
)
cfprApVnicIPv4StaticRouteDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4StaticRouteDn.setStatus("current")
_CfprApVnicIPv4StaticRouteRn_Type = SnmpAdminString
_CfprApVnicIPv4StaticRouteRn_Object = MibTableColumn
cfprApVnicIPv4StaticRouteRn = _CfprApVnicIPv4StaticRouteRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 26, 1, 3),
    _CfprApVnicIPv4StaticRouteRn_Type()
)
cfprApVnicIPv4StaticRouteRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4StaticRouteRn.setStatus("current")
_CfprApVnicIPv4StaticRouteAddr_Type = InetAddressIPv4
_CfprApVnicIPv4StaticRouteAddr_Object = MibTableColumn
cfprApVnicIPv4StaticRouteAddr = _CfprApVnicIPv4StaticRouteAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 26, 1, 4),
    _CfprApVnicIPv4StaticRouteAddr_Type()
)
cfprApVnicIPv4StaticRouteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4StaticRouteAddr.setStatus("current")
_CfprApVnicIPv4StaticRouteDefGw_Type = InetAddressIPv4
_CfprApVnicIPv4StaticRouteDefGw_Object = MibTableColumn
cfprApVnicIPv4StaticRouteDefGw = _CfprApVnicIPv4StaticRouteDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 26, 1, 5),
    _CfprApVnicIPv4StaticRouteDefGw_Type()
)
cfprApVnicIPv4StaticRouteDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4StaticRouteDefGw.setStatus("current")
_CfprApVnicIPv4StaticRouteGwAddr_Type = InetAddressIPv4
_CfprApVnicIPv4StaticRouteGwAddr_Object = MibTableColumn
cfprApVnicIPv4StaticRouteGwAddr = _CfprApVnicIPv4StaticRouteGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 26, 1, 6),
    _CfprApVnicIPv4StaticRouteGwAddr_Type()
)
cfprApVnicIPv4StaticRouteGwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4StaticRouteGwAddr.setStatus("current")
_CfprApVnicIPv4StaticRouteGwSubnet_Type = InetAddressIPv4
_CfprApVnicIPv4StaticRouteGwSubnet_Object = MibTableColumn
cfprApVnicIPv4StaticRouteGwSubnet = _CfprApVnicIPv4StaticRouteGwSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 26, 1, 7),
    _CfprApVnicIPv4StaticRouteGwSubnet_Type()
)
cfprApVnicIPv4StaticRouteGwSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4StaticRouteGwSubnet.setStatus("current")
_CfprApVnicIPv4StaticRouteSubnet_Type = InetAddressIPv4
_CfprApVnicIPv4StaticRouteSubnet_Object = MibTableColumn
cfprApVnicIPv4StaticRouteSubnet = _CfprApVnicIPv4StaticRouteSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 26, 1, 8),
    _CfprApVnicIPv4StaticRouteSubnet_Type()
)
cfprApVnicIPv4StaticRouteSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIPv4StaticRouteSubnet.setStatus("current")
_CfprApVnicIScsiTable_Object = MibTable
cfprApVnicIScsiTable = _CfprApVnicIScsiTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27)
)
if mibBuilder.loadTexts:
    cfprApVnicIScsiTable.setStatus("current")
_CfprApVnicIScsiEntry_Object = MibTableRow
cfprApVnicIScsiEntry = _CfprApVnicIScsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1)
)
cfprApVnicIScsiEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicIScsiInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicIScsiEntry.setStatus("current")
_CfprApVnicIScsiInstanceId_Type = CfprApManagedObjectId
_CfprApVnicIScsiInstanceId_Object = MibTableColumn
cfprApVnicIScsiInstanceId = _CfprApVnicIScsiInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 1),
    _CfprApVnicIScsiInstanceId_Type()
)
cfprApVnicIScsiInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicIScsiInstanceId.setStatus("current")
_CfprApVnicIScsiDn_Type = CfprApManagedObjectDn
_CfprApVnicIScsiDn_Object = MibTableColumn
cfprApVnicIScsiDn = _CfprApVnicIScsiDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 2),
    _CfprApVnicIScsiDn_Type()
)
cfprApVnicIScsiDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiDn.setStatus("current")
_CfprApVnicIScsiRn_Type = SnmpAdminString
_CfprApVnicIScsiRn_Object = MibTableColumn
cfprApVnicIScsiRn = _CfprApVnicIScsiRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 3),
    _CfprApVnicIScsiRn_Type()
)
cfprApVnicIScsiRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiRn.setStatus("current")
_CfprApVnicIScsiAdaptorProfileName_Type = SnmpAdminString
_CfprApVnicIScsiAdaptorProfileName_Object = MibTableColumn
cfprApVnicIScsiAdaptorProfileName = _CfprApVnicIScsiAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 4),
    _CfprApVnicIScsiAdaptorProfileName_Type()
)
cfprApVnicIScsiAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiAdaptorProfileName.setStatus("current")
_CfprApVnicIScsiAddr_Type = MacAddress
_CfprApVnicIScsiAddr_Object = MibTableColumn
cfprApVnicIScsiAddr = _CfprApVnicIScsiAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 5),
    _CfprApVnicIScsiAddr_Type()
)
cfprApVnicIScsiAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiAddr.setStatus("current")
_CfprApVnicIScsiAdminHostPort_Type = CfprApFabricHostPortId
_CfprApVnicIScsiAdminHostPort_Object = MibTableColumn
cfprApVnicIScsiAdminHostPort = _CfprApVnicIScsiAdminHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 6),
    _CfprApVnicIScsiAdminHostPort_Type()
)
cfprApVnicIScsiAdminHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiAdminHostPort.setStatus("current")
_CfprApVnicIScsiAdminVcon_Type = SnmpAdminString
_CfprApVnicIScsiAdminVcon_Object = MibTableColumn
cfprApVnicIScsiAdminVcon = _CfprApVnicIScsiAdminVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 7),
    _CfprApVnicIScsiAdminVcon_Type()
)
cfprApVnicIScsiAdminVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiAdminVcon.setStatus("current")
_CfprApVnicIScsiAppRole_Type = CfprApVnicAppRole
_CfprApVnicIScsiAppRole_Object = MibTableColumn
cfprApVnicIScsiAppRole = _CfprApVnicIScsiAppRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 8),
    _CfprApVnicIScsiAppRole_Type()
)
cfprApVnicIScsiAppRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiAppRole.setStatus("current")
_CfprApVnicIScsiBootDev_Type = CfprApVnicVnicBootDev
_CfprApVnicIScsiBootDev_Object = MibTableColumn
cfprApVnicIScsiBootDev = _CfprApVnicIScsiBootDev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 10),
    _CfprApVnicIScsiBootDev_Type()
)
cfprApVnicIScsiBootDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiBootDev.setStatus("current")
_CfprApVnicIScsiConfigQualifier_Type = CfprApVnicConfigIssues
_CfprApVnicIScsiConfigQualifier_Object = MibTableColumn
cfprApVnicIScsiConfigQualifier = _CfprApVnicIScsiConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 11),
    _CfprApVnicIScsiConfigQualifier_Type()
)
cfprApVnicIScsiConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiConfigQualifier.setStatus("current")
_CfprApVnicIScsiConfigState_Type = CfprApLsConfigState
_CfprApVnicIScsiConfigState_Object = MibTableColumn
cfprApVnicIScsiConfigState = _CfprApVnicIScsiConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 12),
    _CfprApVnicIScsiConfigState_Type()
)
cfprApVnicIScsiConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiConfigState.setStatus("current")
_CfprApVnicIScsiEquipmentDn_Type = SnmpAdminString
_CfprApVnicIScsiEquipmentDn_Object = MibTableColumn
cfprApVnicIScsiEquipmentDn = _CfprApVnicIScsiEquipmentDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 13),
    _CfprApVnicIScsiEquipmentDn_Type()
)
cfprApVnicIScsiEquipmentDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiEquipmentDn.setStatus("current")
_CfprApVnicIScsiEthEpDn_Type = SnmpAdminString
_CfprApVnicIScsiEthEpDn_Object = MibTableColumn
cfprApVnicIScsiEthEpDn = _CfprApVnicIScsiEthEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 14),
    _CfprApVnicIScsiEthEpDn_Type()
)
cfprApVnicIScsiEthEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiEthEpDn.setStatus("current")
_CfprApVnicIScsiExtIPState_Type = CfprApVnicExternalMgmtIPMode
_CfprApVnicIScsiExtIPState_Object = MibTableColumn
cfprApVnicIScsiExtIPState = _CfprApVnicIScsiExtIPState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 15),
    _CfprApVnicIScsiExtIPState_Type()
)
cfprApVnicIScsiExtIPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiExtIPState.setStatus("current")
_CfprApVnicIScsiFltAggr_Type = Unsigned64
_CfprApVnicIScsiFltAggr_Object = MibTableColumn
cfprApVnicIScsiFltAggr = _CfprApVnicIScsiFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 16),
    _CfprApVnicIScsiFltAggr_Type()
)
cfprApVnicIScsiFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiFltAggr.setStatus("current")
_CfprApVnicIScsiIdentPoolName_Type = SnmpAdminString
_CfprApVnicIScsiIdentPoolName_Object = MibTableColumn
cfprApVnicIScsiIdentPoolName = _CfprApVnicIScsiIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 17),
    _CfprApVnicIScsiIdentPoolName_Type()
)
cfprApVnicIScsiIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiIdentPoolName.setStatus("current")
_CfprApVnicIScsiInitNameSuffix_Type = SnmpAdminString
_CfprApVnicIScsiInitNameSuffix_Object = MibTableColumn
cfprApVnicIScsiInitNameSuffix = _CfprApVnicIScsiInitNameSuffix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 18),
    _CfprApVnicIScsiInitNameSuffix_Type()
)
cfprApVnicIScsiInitNameSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiInitNameSuffix.setStatus("current")
_CfprApVnicIScsiInitiatorName_Type = SnmpAdminString
_CfprApVnicIScsiInitiatorName_Object = MibTableColumn
cfprApVnicIScsiInitiatorName = _CfprApVnicIScsiInitiatorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 19),
    _CfprApVnicIScsiInitiatorName_Type()
)
cfprApVnicIScsiInitiatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiInitiatorName.setStatus("current")
_CfprApVnicIScsiInstType_Type = CfprApVnicInstantiation
_CfprApVnicIScsiInstType_Object = MibTableColumn
cfprApVnicIScsiInstType = _CfprApVnicIScsiInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 20),
    _CfprApVnicIScsiInstType_Type()
)
cfprApVnicIScsiInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiInstType.setStatus("current")
_CfprApVnicIScsiIqnIdentPoolName_Type = SnmpAdminString
_CfprApVnicIScsiIqnIdentPoolName_Object = MibTableColumn
cfprApVnicIScsiIqnIdentPoolName = _CfprApVnicIScsiIqnIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 21),
    _CfprApVnicIScsiIqnIdentPoolName_Type()
)
cfprApVnicIScsiIqnIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiIqnIdentPoolName.setStatus("current")
_CfprApVnicIScsiName_Type = SnmpAdminString
_CfprApVnicIScsiName_Object = MibTableColumn
cfprApVnicIScsiName = _CfprApVnicIScsiName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 22),
    _CfprApVnicIScsiName_Type()
)
cfprApVnicIScsiName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiName.setStatus("current")
_CfprApVnicIScsiNwTemplName_Type = SnmpAdminString
_CfprApVnicIScsiNwTemplName_Object = MibTableColumn
cfprApVnicIScsiNwTemplName = _CfprApVnicIScsiNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 23),
    _CfprApVnicIScsiNwTemplName_Type()
)
cfprApVnicIScsiNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiNwTemplName.setStatus("current")
_CfprApVnicIScsiOperHostPort_Type = CfprApVnicVnicOperHostPort
_CfprApVnicIScsiOperHostPort_Object = MibTableColumn
cfprApVnicIScsiOperHostPort = _CfprApVnicIScsiOperHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 26),
    _CfprApVnicIScsiOperHostPort_Type()
)
cfprApVnicIScsiOperHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiOperHostPort.setStatus("current")
_CfprApVnicIScsiOperIdentPoolName_Type = SnmpAdminString
_CfprApVnicIScsiOperIdentPoolName_Object = MibTableColumn
cfprApVnicIScsiOperIdentPoolName = _CfprApVnicIScsiOperIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 27),
    _CfprApVnicIScsiOperIdentPoolName_Type()
)
cfprApVnicIScsiOperIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiOperIdentPoolName.setStatus("current")
_CfprApVnicIScsiOperIqnIdentPoolName_Type = SnmpAdminString
_CfprApVnicIScsiOperIqnIdentPoolName_Object = MibTableColumn
cfprApVnicIScsiOperIqnIdentPoolName = _CfprApVnicIScsiOperIqnIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 28),
    _CfprApVnicIScsiOperIqnIdentPoolName_Type()
)
cfprApVnicIScsiOperIqnIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiOperIqnIdentPoolName.setStatus("current")
_CfprApVnicIScsiOperOrder_Type = Gauge32
_CfprApVnicIScsiOperOrder_Object = MibTableColumn
cfprApVnicIScsiOperOrder = _CfprApVnicIScsiOperOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 29),
    _CfprApVnicIScsiOperOrder_Type()
)
cfprApVnicIScsiOperOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiOperOrder.setStatus("current")
_CfprApVnicIScsiOperSpeed_Type = Gauge32
_CfprApVnicIScsiOperSpeed_Object = MibTableColumn
cfprApVnicIScsiOperSpeed = _CfprApVnicIScsiOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 30),
    _CfprApVnicIScsiOperSpeed_Type()
)
cfprApVnicIScsiOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiOperSpeed.setStatus("current")
_CfprApVnicIScsiOperStatsPolicyName_Type = SnmpAdminString
_CfprApVnicIScsiOperStatsPolicyName_Object = MibTableColumn
cfprApVnicIScsiOperStatsPolicyName = _CfprApVnicIScsiOperStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 31),
    _CfprApVnicIScsiOperStatsPolicyName_Type()
)
cfprApVnicIScsiOperStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiOperStatsPolicyName.setStatus("current")
_CfprApVnicIScsiOperVcon_Type = SnmpAdminString
_CfprApVnicIScsiOperVcon_Object = MibTableColumn
cfprApVnicIScsiOperVcon = _CfprApVnicIScsiOperVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 32),
    _CfprApVnicIScsiOperVcon_Type()
)
cfprApVnicIScsiOperVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiOperVcon.setStatus("current")
_CfprApVnicIScsiOrder_Type = Gauge32
_CfprApVnicIScsiOrder_Object = MibTableColumn
cfprApVnicIScsiOrder = _CfprApVnicIScsiOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 33),
    _CfprApVnicIScsiOrder_Type()
)
cfprApVnicIScsiOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiOrder.setStatus("current")
_CfprApVnicIScsiOwner_Type = CfprApVnicConnectionOwner
_CfprApVnicIScsiOwner_Object = MibTableColumn
cfprApVnicIScsiOwner = _CfprApVnicIScsiOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 34),
    _CfprApVnicIScsiOwner_Type()
)
cfprApVnicIScsiOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiOwner.setStatus("current")
_CfprApVnicIScsiPinToGroupName_Type = SnmpAdminString
_CfprApVnicIScsiPinToGroupName_Object = MibTableColumn
cfprApVnicIScsiPinToGroupName = _CfprApVnicIScsiPinToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 35),
    _CfprApVnicIScsiPinToGroupName_Type()
)
cfprApVnicIScsiPinToGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiPinToGroupName.setStatus("current")
_CfprApVnicIScsiQosPolicyName_Type = SnmpAdminString
_CfprApVnicIScsiQosPolicyName_Object = MibTableColumn
cfprApVnicIScsiQosPolicyName = _CfprApVnicIScsiQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 36),
    _CfprApVnicIScsiQosPolicyName_Type()
)
cfprApVnicIScsiQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiQosPolicyName.setStatus("current")
_CfprApVnicIScsiStatsPolicyName_Type = SnmpAdminString
_CfprApVnicIScsiStatsPolicyName_Object = MibTableColumn
cfprApVnicIScsiStatsPolicyName = _CfprApVnicIScsiStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 37),
    _CfprApVnicIScsiStatsPolicyName_Type()
)
cfprApVnicIScsiStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiStatsPolicyName.setStatus("current")
_CfprApVnicIScsiSwitchId_Type = CfprApNetworkSwitchId
_CfprApVnicIScsiSwitchId_Object = MibTableColumn
cfprApVnicIScsiSwitchId = _CfprApVnicIScsiSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 38),
    _CfprApVnicIScsiSwitchId_Type()
)
cfprApVnicIScsiSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiSwitchId.setStatus("current")
_CfprApVnicIScsiType_Type = CfprApVnicConnectionType
_CfprApVnicIScsiType_Object = MibTableColumn
cfprApVnicIScsiType = _CfprApVnicIScsiType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 39),
    _CfprApVnicIScsiType_Type()
)
cfprApVnicIScsiType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiType.setStatus("current")
_CfprApVnicIScsiVnicDefType_Type = CfprApVnicIScsiIfDefType
_CfprApVnicIScsiVnicDefType_Object = MibTableColumn
cfprApVnicIScsiVnicDefType = _CfprApVnicIScsiVnicDefType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 40),
    _CfprApVnicIScsiVnicDefType_Type()
)
cfprApVnicIScsiVnicDefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiVnicDefType.setStatus("current")
_CfprApVnicIScsiVnicName_Type = SnmpAdminString
_CfprApVnicIScsiVnicName_Object = MibTableColumn
cfprApVnicIScsiVnicName = _CfprApVnicIScsiVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 27, 1, 41),
    _CfprApVnicIScsiVnicName_Type()
)
cfprApVnicIScsiVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiVnicName.setStatus("current")
_CfprApVnicIScsiAutoTargetIfTable_Object = MibTable
cfprApVnicIScsiAutoTargetIfTable = _CfprApVnicIScsiAutoTargetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 28)
)
if mibBuilder.loadTexts:
    cfprApVnicIScsiAutoTargetIfTable.setStatus("current")
_CfprApVnicIScsiAutoTargetIfEntry_Object = MibTableRow
cfprApVnicIScsiAutoTargetIfEntry = _CfprApVnicIScsiAutoTargetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 28, 1)
)
cfprApVnicIScsiAutoTargetIfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicIScsiAutoTargetIfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicIScsiAutoTargetIfEntry.setStatus("current")
_CfprApVnicIScsiAutoTargetIfInstanceId_Type = CfprApManagedObjectId
_CfprApVnicIScsiAutoTargetIfInstanceId_Object = MibTableColumn
cfprApVnicIScsiAutoTargetIfInstanceId = _CfprApVnicIScsiAutoTargetIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 28, 1, 1),
    _CfprApVnicIScsiAutoTargetIfInstanceId_Type()
)
cfprApVnicIScsiAutoTargetIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicIScsiAutoTargetIfInstanceId.setStatus("current")
_CfprApVnicIScsiAutoTargetIfDn_Type = CfprApManagedObjectDn
_CfprApVnicIScsiAutoTargetIfDn_Object = MibTableColumn
cfprApVnicIScsiAutoTargetIfDn = _CfprApVnicIScsiAutoTargetIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 28, 1, 2),
    _CfprApVnicIScsiAutoTargetIfDn_Type()
)
cfprApVnicIScsiAutoTargetIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiAutoTargetIfDn.setStatus("current")
_CfprApVnicIScsiAutoTargetIfRn_Type = SnmpAdminString
_CfprApVnicIScsiAutoTargetIfRn_Object = MibTableColumn
cfprApVnicIScsiAutoTargetIfRn = _CfprApVnicIScsiAutoTargetIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 28, 1, 3),
    _CfprApVnicIScsiAutoTargetIfRn_Type()
)
cfprApVnicIScsiAutoTargetIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiAutoTargetIfRn.setStatus("current")
_CfprApVnicIScsiAutoTargetIfDhcpVendorId_Type = SnmpAdminString
_CfprApVnicIScsiAutoTargetIfDhcpVendorId_Object = MibTableColumn
cfprApVnicIScsiAutoTargetIfDhcpVendorId = _CfprApVnicIScsiAutoTargetIfDhcpVendorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 28, 1, 4),
    _CfprApVnicIScsiAutoTargetIfDhcpVendorId_Type()
)
cfprApVnicIScsiAutoTargetIfDhcpVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiAutoTargetIfDhcpVendorId.setStatus("current")
_CfprApVnicIScsiBootParamsTable_Object = MibTable
cfprApVnicIScsiBootParamsTable = _CfprApVnicIScsiBootParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 29)
)
if mibBuilder.loadTexts:
    cfprApVnicIScsiBootParamsTable.setStatus("current")
_CfprApVnicIScsiBootParamsEntry_Object = MibTableRow
cfprApVnicIScsiBootParamsEntry = _CfprApVnicIScsiBootParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 29, 1)
)
cfprApVnicIScsiBootParamsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicIScsiBootParamsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicIScsiBootParamsEntry.setStatus("current")
_CfprApVnicIScsiBootParamsInstanceId_Type = CfprApManagedObjectId
_CfprApVnicIScsiBootParamsInstanceId_Object = MibTableColumn
cfprApVnicIScsiBootParamsInstanceId = _CfprApVnicIScsiBootParamsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 29, 1, 1),
    _CfprApVnicIScsiBootParamsInstanceId_Type()
)
cfprApVnicIScsiBootParamsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicIScsiBootParamsInstanceId.setStatus("current")
_CfprApVnicIScsiBootParamsDn_Type = CfprApManagedObjectDn
_CfprApVnicIScsiBootParamsDn_Object = MibTableColumn
cfprApVnicIScsiBootParamsDn = _CfprApVnicIScsiBootParamsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 29, 1, 2),
    _CfprApVnicIScsiBootParamsDn_Type()
)
cfprApVnicIScsiBootParamsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiBootParamsDn.setStatus("current")
_CfprApVnicIScsiBootParamsRn_Type = SnmpAdminString
_CfprApVnicIScsiBootParamsRn_Object = MibTableColumn
cfprApVnicIScsiBootParamsRn = _CfprApVnicIScsiBootParamsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 29, 1, 3),
    _CfprApVnicIScsiBootParamsRn_Type()
)
cfprApVnicIScsiBootParamsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiBootParamsRn.setStatus("current")
_CfprApVnicIScsiBootParamsDescr_Type = SnmpAdminString
_CfprApVnicIScsiBootParamsDescr_Object = MibTableColumn
cfprApVnicIScsiBootParamsDescr = _CfprApVnicIScsiBootParamsDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 29, 1, 4),
    _CfprApVnicIScsiBootParamsDescr_Type()
)
cfprApVnicIScsiBootParamsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiBootParamsDescr.setStatus("current")
_CfprApVnicIScsiBootParamsIntId_Type = SnmpAdminString
_CfprApVnicIScsiBootParamsIntId_Object = MibTableColumn
cfprApVnicIScsiBootParamsIntId = _CfprApVnicIScsiBootParamsIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 29, 1, 5),
    _CfprApVnicIScsiBootParamsIntId_Type()
)
cfprApVnicIScsiBootParamsIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiBootParamsIntId.setStatus("current")
_CfprApVnicIScsiBootParamsName_Type = SnmpAdminString
_CfprApVnicIScsiBootParamsName_Object = MibTableColumn
cfprApVnicIScsiBootParamsName = _CfprApVnicIScsiBootParamsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 29, 1, 6),
    _CfprApVnicIScsiBootParamsName_Type()
)
cfprApVnicIScsiBootParamsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiBootParamsName.setStatus("current")
_CfprApVnicIScsiBootParamsPolicyLevel_Type = Gauge32
_CfprApVnicIScsiBootParamsPolicyLevel_Object = MibTableColumn
cfprApVnicIScsiBootParamsPolicyLevel = _CfprApVnicIScsiBootParamsPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 29, 1, 7),
    _CfprApVnicIScsiBootParamsPolicyLevel_Type()
)
cfprApVnicIScsiBootParamsPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiBootParamsPolicyLevel.setStatus("current")
_CfprApVnicIScsiBootParamsPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApVnicIScsiBootParamsPolicyOwner_Object = MibTableColumn
cfprApVnicIScsiBootParamsPolicyOwner = _CfprApVnicIScsiBootParamsPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 29, 1, 8),
    _CfprApVnicIScsiBootParamsPolicyOwner_Type()
)
cfprApVnicIScsiBootParamsPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiBootParamsPolicyOwner.setStatus("current")
_CfprApVnicIScsiBootVnicTable_Object = MibTable
cfprApVnicIScsiBootVnicTable = _CfprApVnicIScsiBootVnicTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 30)
)
if mibBuilder.loadTexts:
    cfprApVnicIScsiBootVnicTable.setStatus("current")
_CfprApVnicIScsiBootVnicEntry_Object = MibTableRow
cfprApVnicIScsiBootVnicEntry = _CfprApVnicIScsiBootVnicEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 30, 1)
)
cfprApVnicIScsiBootVnicEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicIScsiBootVnicInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicIScsiBootVnicEntry.setStatus("current")
_CfprApVnicIScsiBootVnicInstanceId_Type = CfprApManagedObjectId
_CfprApVnicIScsiBootVnicInstanceId_Object = MibTableColumn
cfprApVnicIScsiBootVnicInstanceId = _CfprApVnicIScsiBootVnicInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 30, 1, 1),
    _CfprApVnicIScsiBootVnicInstanceId_Type()
)
cfprApVnicIScsiBootVnicInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicIScsiBootVnicInstanceId.setStatus("current")
_CfprApVnicIScsiBootVnicDn_Type = CfprApManagedObjectDn
_CfprApVnicIScsiBootVnicDn_Object = MibTableColumn
cfprApVnicIScsiBootVnicDn = _CfprApVnicIScsiBootVnicDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 30, 1, 2),
    _CfprApVnicIScsiBootVnicDn_Type()
)
cfprApVnicIScsiBootVnicDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiBootVnicDn.setStatus("current")
_CfprApVnicIScsiBootVnicRn_Type = SnmpAdminString
_CfprApVnicIScsiBootVnicRn_Object = MibTableColumn
cfprApVnicIScsiBootVnicRn = _CfprApVnicIScsiBootVnicRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 30, 1, 3),
    _CfprApVnicIScsiBootVnicRn_Type()
)
cfprApVnicIScsiBootVnicRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiBootVnicRn.setStatus("current")
_CfprApVnicIScsiBootVnicDescr_Type = SnmpAdminString
_CfprApVnicIScsiBootVnicDescr_Object = MibTableColumn
cfprApVnicIScsiBootVnicDescr = _CfprApVnicIScsiBootVnicDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 30, 1, 5),
    _CfprApVnicIScsiBootVnicDescr_Type()
)
cfprApVnicIScsiBootVnicDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiBootVnicDescr.setStatus("current")
_CfprApVnicIScsiBootVnicInitiatorName_Type = SnmpAdminString
_CfprApVnicIScsiBootVnicInitiatorName_Object = MibTableColumn
cfprApVnicIScsiBootVnicInitiatorName = _CfprApVnicIScsiBootVnicInitiatorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 30, 1, 6),
    _CfprApVnicIScsiBootVnicInitiatorName_Type()
)
cfprApVnicIScsiBootVnicInitiatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiBootVnicInitiatorName.setStatus("current")
_CfprApVnicIScsiBootVnicIntId_Type = SnmpAdminString
_CfprApVnicIScsiBootVnicIntId_Object = MibTableColumn
cfprApVnicIScsiBootVnicIntId = _CfprApVnicIScsiBootVnicIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 30, 1, 7),
    _CfprApVnicIScsiBootVnicIntId_Type()
)
cfprApVnicIScsiBootVnicIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiBootVnicIntId.setStatus("current")
_CfprApVnicIScsiBootVnicIqnIdentPoolName_Type = SnmpAdminString
_CfprApVnicIScsiBootVnicIqnIdentPoolName_Object = MibTableColumn
cfprApVnicIScsiBootVnicIqnIdentPoolName = _CfprApVnicIScsiBootVnicIqnIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 30, 1, 8),
    _CfprApVnicIScsiBootVnicIqnIdentPoolName_Type()
)
cfprApVnicIScsiBootVnicIqnIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiBootVnicIqnIdentPoolName.setStatus("current")
_CfprApVnicIScsiBootVnicName_Type = SnmpAdminString
_CfprApVnicIScsiBootVnicName_Object = MibTableColumn
cfprApVnicIScsiBootVnicName = _CfprApVnicIScsiBootVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 30, 1, 9),
    _CfprApVnicIScsiBootVnicName_Type()
)
cfprApVnicIScsiBootVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiBootVnicName.setStatus("current")
_CfprApVnicIScsiBootVnicOperIqnIdentPoolName_Type = SnmpAdminString
_CfprApVnicIScsiBootVnicOperIqnIdentPoolName_Object = MibTableColumn
cfprApVnicIScsiBootVnicOperIqnIdentPoolName = _CfprApVnicIScsiBootVnicOperIqnIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 30, 1, 11),
    _CfprApVnicIScsiBootVnicOperIqnIdentPoolName_Type()
)
cfprApVnicIScsiBootVnicOperIqnIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiBootVnicOperIqnIdentPoolName.setStatus("current")
_CfprApVnicIScsiBootVnicPolicyLevel_Type = Gauge32
_CfprApVnicIScsiBootVnicPolicyLevel_Object = MibTableColumn
cfprApVnicIScsiBootVnicPolicyLevel = _CfprApVnicIScsiBootVnicPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 30, 1, 12),
    _CfprApVnicIScsiBootVnicPolicyLevel_Type()
)
cfprApVnicIScsiBootVnicPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiBootVnicPolicyLevel.setStatus("current")
_CfprApVnicIScsiBootVnicPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApVnicIScsiBootVnicPolicyOwner_Object = MibTableColumn
cfprApVnicIScsiBootVnicPolicyOwner = _CfprApVnicIScsiBootVnicPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 30, 1, 13),
    _CfprApVnicIScsiBootVnicPolicyOwner_Type()
)
cfprApVnicIScsiBootVnicPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiBootVnicPolicyOwner.setStatus("current")
_CfprApVnicIScsiLCPTable_Object = MibTable
cfprApVnicIScsiLCPTable = _CfprApVnicIScsiLCPTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 31)
)
if mibBuilder.loadTexts:
    cfprApVnicIScsiLCPTable.setStatus("current")
_CfprApVnicIScsiLCPEntry_Object = MibTableRow
cfprApVnicIScsiLCPEntry = _CfprApVnicIScsiLCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 31, 1)
)
cfprApVnicIScsiLCPEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicIScsiLCPInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicIScsiLCPEntry.setStatus("current")
_CfprApVnicIScsiLCPInstanceId_Type = CfprApManagedObjectId
_CfprApVnicIScsiLCPInstanceId_Object = MibTableColumn
cfprApVnicIScsiLCPInstanceId = _CfprApVnicIScsiLCPInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 31, 1, 1),
    _CfprApVnicIScsiLCPInstanceId_Type()
)
cfprApVnicIScsiLCPInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicIScsiLCPInstanceId.setStatus("current")
_CfprApVnicIScsiLCPDn_Type = CfprApManagedObjectDn
_CfprApVnicIScsiLCPDn_Object = MibTableColumn
cfprApVnicIScsiLCPDn = _CfprApVnicIScsiLCPDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 31, 1, 2),
    _CfprApVnicIScsiLCPDn_Type()
)
cfprApVnicIScsiLCPDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiLCPDn.setStatus("current")
_CfprApVnicIScsiLCPRn_Type = SnmpAdminString
_CfprApVnicIScsiLCPRn_Object = MibTableColumn
cfprApVnicIScsiLCPRn = _CfprApVnicIScsiLCPRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 31, 1, 3),
    _CfprApVnicIScsiLCPRn_Type()
)
cfprApVnicIScsiLCPRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiLCPRn.setStatus("current")
_CfprApVnicIScsiLCPAdaptorProfileName_Type = SnmpAdminString
_CfprApVnicIScsiLCPAdaptorProfileName_Object = MibTableColumn
cfprApVnicIScsiLCPAdaptorProfileName = _CfprApVnicIScsiLCPAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 31, 1, 4),
    _CfprApVnicIScsiLCPAdaptorProfileName_Type()
)
cfprApVnicIScsiLCPAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiLCPAdaptorProfileName.setStatus("current")
_CfprApVnicIScsiLCPAddr_Type = MacAddress
_CfprApVnicIScsiLCPAddr_Object = MibTableColumn
cfprApVnicIScsiLCPAddr = _CfprApVnicIScsiLCPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 31, 1, 5),
    _CfprApVnicIScsiLCPAddr_Type()
)
cfprApVnicIScsiLCPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiLCPAddr.setStatus("current")
_CfprApVnicIScsiLCPAdminHostPort_Type = CfprApFabricHostPortId
_CfprApVnicIScsiLCPAdminHostPort_Object = MibTableColumn
cfprApVnicIScsiLCPAdminHostPort = _CfprApVnicIScsiLCPAdminHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 31, 1, 6),
    _CfprApVnicIScsiLCPAdminHostPort_Type()
)
cfprApVnicIScsiLCPAdminHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiLCPAdminHostPort.setStatus("current")
_CfprApVnicIScsiLCPAdminVcon_Type = SnmpAdminString
_CfprApVnicIScsiLCPAdminVcon_Object = MibTableColumn
cfprApVnicIScsiLCPAdminVcon = _CfprApVnicIScsiLCPAdminVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 31, 1, 7),
    _CfprApVnicIScsiLCPAdminVcon_Type()
)
cfprApVnicIScsiLCPAdminVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiLCPAdminVcon.setStatus("current")
_CfprApVnicIScsiLCPAppRole_Type = CfprApVnicAppRole
_CfprApVnicIScsiLCPAppRole_Object = MibTableColumn
cfprApVnicIScsiLCPAppRole = _CfprApVnicIScsiLCPAppRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 31, 1, 8),
    _CfprApVnicIScsiLCPAppRole_Type()
)
cfprApVnicIScsiLCPAppRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiLCPAppRole.setStatus("current")
_CfprApVnicIScsiLCPBootDev_Type = CfprApVnicVnicBootDev
_CfprApVnicIScsiLCPBootDev_Object = MibTableColumn
cfprApVnicIScsiLCPBootDev = _CfprApVnicIScsiLCPBootDev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 31, 1, 9),
    _CfprApVnicIScsiLCPBootDev_Type()
)
cfprApVnicIScsiLCPBootDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiLCPBootDev.setStatus("current")
_CfprApVnicIScsiLCPConfigQualifier_Type = CfprApVnicConfigIssues
_CfprApVnicIScsiLCPConfigQualifier_Object = MibTableColumn
cfprApVnicIScsiLCPConfigQualifier = _CfprApVnicIScsiLCPConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 31, 1, 10),
    _CfprApVnicIScsiLCPConfigQualifier_Type()
)
cfprApVnicIScsiLCPConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiLCPConfigQualifier.setStatus("current")
_CfprApVnicIScsiLCPConfigState_Type = CfprApLsConfigState
_CfprApVnicIScsiLCPConfigState_Object = MibTableColumn
cfprApVnicIScsiLCPConfigState = _CfprApVnicIScsiLCPConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 31, 1, 11),
    _CfprApVnicIScsiLCPConfigState_Type()
)
cfprApVnicIScsiLCPConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiLCPConfigState.setStatus("current")
_CfprApVnicIScsiLCPEquipmentDn_Type = SnmpAdminString
_CfprApVnicIScsiLCPEquipmentDn_Object = MibTableColumn
cfprApVnicIScsiLCPEquipmentDn = _CfprApVnicIScsiLCPEquipmentDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 31, 1, 12),
    _CfprApVnicIScsiLCPEquipmentDn_Type()
)
cfprApVnicIScsiLCPEquipmentDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiLCPEquipmentDn.setStatus("current")
_CfprApVnicIScsiLCPFltAggr_Type = Unsigned64
_CfprApVnicIScsiLCPFltAggr_Object = MibTableColumn
cfprApVnicIScsiLCPFltAggr = _CfprApVnicIScsiLCPFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 31, 1, 13),
    _CfprApVnicIScsiLCPFltAggr_Type()
)
cfprApVnicIScsiLCPFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiLCPFltAggr.setStatus("current")
_CfprApVnicIScsiLCPIdentPoolName_Type = SnmpAdminString
_CfprApVnicIScsiLCPIdentPoolName_Object = MibTableColumn
cfprApVnicIScsiLCPIdentPoolName = _CfprApVnicIScsiLCPIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 31, 1, 14),
    _CfprApVnicIScsiLCPIdentPoolName_Type()
)
cfprApVnicIScsiLCPIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiLCPIdentPoolName.setStatus("current")
_CfprApVnicIScsiLCPInstType_Type = CfprApVnicInstantiation
_CfprApVnicIScsiLCPInstType_Object = MibTableColumn
cfprApVnicIScsiLCPInstType = _CfprApVnicIScsiLCPInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 31, 1, 15),
    _CfprApVnicIScsiLCPInstType_Type()
)
cfprApVnicIScsiLCPInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiLCPInstType.setStatus("current")
_CfprApVnicIScsiLCPName_Type = SnmpAdminString
_CfprApVnicIScsiLCPName_Object = MibTableColumn
cfprApVnicIScsiLCPName = _CfprApVnicIScsiLCPName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 31, 1, 16),
    _CfprApVnicIScsiLCPName_Type()
)
cfprApVnicIScsiLCPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiLCPName.setStatus("current")
_CfprApVnicIScsiLCPNwTemplName_Type = SnmpAdminString
_CfprApVnicIScsiLCPNwTemplName_Object = MibTableColumn
cfprApVnicIScsiLCPNwTemplName = _CfprApVnicIScsiLCPNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 31, 1, 17),
    _CfprApVnicIScsiLCPNwTemplName_Type()
)
cfprApVnicIScsiLCPNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiLCPNwTemplName.setStatus("current")
_CfprApVnicIScsiLCPOperHostPort_Type = CfprApVnicVnicOperHostPort
_CfprApVnicIScsiLCPOperHostPort_Object = MibTableColumn
cfprApVnicIScsiLCPOperHostPort = _CfprApVnicIScsiLCPOperHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 31, 1, 19),
    _CfprApVnicIScsiLCPOperHostPort_Type()
)
cfprApVnicIScsiLCPOperHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiLCPOperHostPort.setStatus("current")
_CfprApVnicIScsiLCPOperIdentPoolName_Type = SnmpAdminString
_CfprApVnicIScsiLCPOperIdentPoolName_Object = MibTableColumn
cfprApVnicIScsiLCPOperIdentPoolName = _CfprApVnicIScsiLCPOperIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 31, 1, 20),
    _CfprApVnicIScsiLCPOperIdentPoolName_Type()
)
cfprApVnicIScsiLCPOperIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiLCPOperIdentPoolName.setStatus("current")
_CfprApVnicIScsiLCPOperOrder_Type = Gauge32
_CfprApVnicIScsiLCPOperOrder_Object = MibTableColumn
cfprApVnicIScsiLCPOperOrder = _CfprApVnicIScsiLCPOperOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 31, 1, 21),
    _CfprApVnicIScsiLCPOperOrder_Type()
)
cfprApVnicIScsiLCPOperOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiLCPOperOrder.setStatus("current")
_CfprApVnicIScsiLCPOperSpeed_Type = Gauge32
_CfprApVnicIScsiLCPOperSpeed_Object = MibTableColumn
cfprApVnicIScsiLCPOperSpeed = _CfprApVnicIScsiLCPOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 31, 1, 22),
    _CfprApVnicIScsiLCPOperSpeed_Type()
)
cfprApVnicIScsiLCPOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiLCPOperSpeed.setStatus("current")
_CfprApVnicIScsiLCPOperStatsPolicyName_Type = SnmpAdminString
_CfprApVnicIScsiLCPOperStatsPolicyName_Object = MibTableColumn
cfprApVnicIScsiLCPOperStatsPolicyName = _CfprApVnicIScsiLCPOperStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 31, 1, 23),
    _CfprApVnicIScsiLCPOperStatsPolicyName_Type()
)
cfprApVnicIScsiLCPOperStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiLCPOperStatsPolicyName.setStatus("current")
_CfprApVnicIScsiLCPOperVcon_Type = SnmpAdminString
_CfprApVnicIScsiLCPOperVcon_Object = MibTableColumn
cfprApVnicIScsiLCPOperVcon = _CfprApVnicIScsiLCPOperVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 31, 1, 24),
    _CfprApVnicIScsiLCPOperVcon_Type()
)
cfprApVnicIScsiLCPOperVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiLCPOperVcon.setStatus("current")
_CfprApVnicIScsiLCPOrder_Type = Gauge32
_CfprApVnicIScsiLCPOrder_Object = MibTableColumn
cfprApVnicIScsiLCPOrder = _CfprApVnicIScsiLCPOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 31, 1, 25),
    _CfprApVnicIScsiLCPOrder_Type()
)
cfprApVnicIScsiLCPOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiLCPOrder.setStatus("current")
_CfprApVnicIScsiLCPOwner_Type = CfprApVnicConnectionOwner
_CfprApVnicIScsiLCPOwner_Object = MibTableColumn
cfprApVnicIScsiLCPOwner = _CfprApVnicIScsiLCPOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 31, 1, 26),
    _CfprApVnicIScsiLCPOwner_Type()
)
cfprApVnicIScsiLCPOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiLCPOwner.setStatus("current")
_CfprApVnicIScsiLCPPinToGroupName_Type = SnmpAdminString
_CfprApVnicIScsiLCPPinToGroupName_Object = MibTableColumn
cfprApVnicIScsiLCPPinToGroupName = _CfprApVnicIScsiLCPPinToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 31, 1, 27),
    _CfprApVnicIScsiLCPPinToGroupName_Type()
)
cfprApVnicIScsiLCPPinToGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiLCPPinToGroupName.setStatus("current")
_CfprApVnicIScsiLCPQosPolicyName_Type = SnmpAdminString
_CfprApVnicIScsiLCPQosPolicyName_Object = MibTableColumn
cfprApVnicIScsiLCPQosPolicyName = _CfprApVnicIScsiLCPQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 31, 1, 28),
    _CfprApVnicIScsiLCPQosPolicyName_Type()
)
cfprApVnicIScsiLCPQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiLCPQosPolicyName.setStatus("current")
_CfprApVnicIScsiLCPStatsPolicyName_Type = SnmpAdminString
_CfprApVnicIScsiLCPStatsPolicyName_Object = MibTableColumn
cfprApVnicIScsiLCPStatsPolicyName = _CfprApVnicIScsiLCPStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 31, 1, 29),
    _CfprApVnicIScsiLCPStatsPolicyName_Type()
)
cfprApVnicIScsiLCPStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiLCPStatsPolicyName.setStatus("current")
_CfprApVnicIScsiLCPSwitchId_Type = CfprApNetworkSwitchId
_CfprApVnicIScsiLCPSwitchId_Object = MibTableColumn
cfprApVnicIScsiLCPSwitchId = _CfprApVnicIScsiLCPSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 31, 1, 30),
    _CfprApVnicIScsiLCPSwitchId_Type()
)
cfprApVnicIScsiLCPSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiLCPSwitchId.setStatus("current")
_CfprApVnicIScsiLCPType_Type = CfprApVnicConnectionType
_CfprApVnicIScsiLCPType_Object = MibTableColumn
cfprApVnicIScsiLCPType = _CfprApVnicIScsiLCPType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 31, 1, 31),
    _CfprApVnicIScsiLCPType_Type()
)
cfprApVnicIScsiLCPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiLCPType.setStatus("current")
_CfprApVnicIScsiLCPVnicName_Type = SnmpAdminString
_CfprApVnicIScsiLCPVnicName_Object = MibTableColumn
cfprApVnicIScsiLCPVnicName = _CfprApVnicIScsiLCPVnicName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 31, 1, 32),
    _CfprApVnicIScsiLCPVnicName_Type()
)
cfprApVnicIScsiLCPVnicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiLCPVnicName.setStatus("current")
_CfprApVnicIScsiNodeTable_Object = MibTable
cfprApVnicIScsiNodeTable = _CfprApVnicIScsiNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 32)
)
if mibBuilder.loadTexts:
    cfprApVnicIScsiNodeTable.setStatus("current")
_CfprApVnicIScsiNodeEntry_Object = MibTableRow
cfprApVnicIScsiNodeEntry = _CfprApVnicIScsiNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 32, 1)
)
cfprApVnicIScsiNodeEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicIScsiNodeInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicIScsiNodeEntry.setStatus("current")
_CfprApVnicIScsiNodeInstanceId_Type = CfprApManagedObjectId
_CfprApVnicIScsiNodeInstanceId_Object = MibTableColumn
cfprApVnicIScsiNodeInstanceId = _CfprApVnicIScsiNodeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 32, 1, 1),
    _CfprApVnicIScsiNodeInstanceId_Type()
)
cfprApVnicIScsiNodeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicIScsiNodeInstanceId.setStatus("current")
_CfprApVnicIScsiNodeDn_Type = CfprApManagedObjectDn
_CfprApVnicIScsiNodeDn_Object = MibTableColumn
cfprApVnicIScsiNodeDn = _CfprApVnicIScsiNodeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 32, 1, 2),
    _CfprApVnicIScsiNodeDn_Type()
)
cfprApVnicIScsiNodeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiNodeDn.setStatus("current")
_CfprApVnicIScsiNodeRn_Type = SnmpAdminString
_CfprApVnicIScsiNodeRn_Object = MibTableColumn
cfprApVnicIScsiNodeRn = _CfprApVnicIScsiNodeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 32, 1, 3),
    _CfprApVnicIScsiNodeRn_Type()
)
cfprApVnicIScsiNodeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiNodeRn.setStatus("current")
_CfprApVnicIScsiNodeFltAggr_Type = Unsigned64
_CfprApVnicIScsiNodeFltAggr_Object = MibTableColumn
cfprApVnicIScsiNodeFltAggr = _CfprApVnicIScsiNodeFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 32, 1, 4),
    _CfprApVnicIScsiNodeFltAggr_Type()
)
cfprApVnicIScsiNodeFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiNodeFltAggr.setStatus("current")
_CfprApVnicIScsiNodeInitNameSuffix_Type = SnmpAdminString
_CfprApVnicIScsiNodeInitNameSuffix_Object = MibTableColumn
cfprApVnicIScsiNodeInitNameSuffix = _CfprApVnicIScsiNodeInitNameSuffix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 32, 1, 5),
    _CfprApVnicIScsiNodeInitNameSuffix_Type()
)
cfprApVnicIScsiNodeInitNameSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiNodeInitNameSuffix.setStatus("current")
_CfprApVnicIScsiNodeInitiatorName_Type = SnmpAdminString
_CfprApVnicIScsiNodeInitiatorName_Object = MibTableColumn
cfprApVnicIScsiNodeInitiatorName = _CfprApVnicIScsiNodeInitiatorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 32, 1, 6),
    _CfprApVnicIScsiNodeInitiatorName_Type()
)
cfprApVnicIScsiNodeInitiatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiNodeInitiatorName.setStatus("current")
_CfprApVnicIScsiNodeIqnIdentPoolName_Type = SnmpAdminString
_CfprApVnicIScsiNodeIqnIdentPoolName_Object = MibTableColumn
cfprApVnicIScsiNodeIqnIdentPoolName = _CfprApVnicIScsiNodeIqnIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 32, 1, 7),
    _CfprApVnicIScsiNodeIqnIdentPoolName_Type()
)
cfprApVnicIScsiNodeIqnIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiNodeIqnIdentPoolName.setStatus("current")
_CfprApVnicIScsiNodeOperIqnIdentPoolName_Type = SnmpAdminString
_CfprApVnicIScsiNodeOperIqnIdentPoolName_Object = MibTableColumn
cfprApVnicIScsiNodeOperIqnIdentPoolName = _CfprApVnicIScsiNodeOperIqnIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 32, 1, 8),
    _CfprApVnicIScsiNodeOperIqnIdentPoolName_Type()
)
cfprApVnicIScsiNodeOperIqnIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiNodeOperIqnIdentPoolName.setStatus("current")
_CfprApVnicIScsiNodeOwner_Type = CfprApVnicIScsiNodeOwner
_CfprApVnicIScsiNodeOwner_Object = MibTableColumn
cfprApVnicIScsiNodeOwner = _CfprApVnicIScsiNodeOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 32, 1, 9),
    _CfprApVnicIScsiNodeOwner_Type()
)
cfprApVnicIScsiNodeOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiNodeOwner.setStatus("current")
_CfprApVnicIScsiStaticTargetIfTable_Object = MibTable
cfprApVnicIScsiStaticTargetIfTable = _CfprApVnicIScsiStaticTargetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 33)
)
if mibBuilder.loadTexts:
    cfprApVnicIScsiStaticTargetIfTable.setStatus("current")
_CfprApVnicIScsiStaticTargetIfEntry_Object = MibTableRow
cfprApVnicIScsiStaticTargetIfEntry = _CfprApVnicIScsiStaticTargetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 33, 1)
)
cfprApVnicIScsiStaticTargetIfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicIScsiStaticTargetIfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicIScsiStaticTargetIfEntry.setStatus("current")
_CfprApVnicIScsiStaticTargetIfInstanceId_Type = CfprApManagedObjectId
_CfprApVnicIScsiStaticTargetIfInstanceId_Object = MibTableColumn
cfprApVnicIScsiStaticTargetIfInstanceId = _CfprApVnicIScsiStaticTargetIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 33, 1, 1),
    _CfprApVnicIScsiStaticTargetIfInstanceId_Type()
)
cfprApVnicIScsiStaticTargetIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicIScsiStaticTargetIfInstanceId.setStatus("current")
_CfprApVnicIScsiStaticTargetIfDn_Type = CfprApManagedObjectDn
_CfprApVnicIScsiStaticTargetIfDn_Object = MibTableColumn
cfprApVnicIScsiStaticTargetIfDn = _CfprApVnicIScsiStaticTargetIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 33, 1, 2),
    _CfprApVnicIScsiStaticTargetIfDn_Type()
)
cfprApVnicIScsiStaticTargetIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiStaticTargetIfDn.setStatus("current")
_CfprApVnicIScsiStaticTargetIfRn_Type = SnmpAdminString
_CfprApVnicIScsiStaticTargetIfRn_Object = MibTableColumn
cfprApVnicIScsiStaticTargetIfRn = _CfprApVnicIScsiStaticTargetIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 33, 1, 3),
    _CfprApVnicIScsiStaticTargetIfRn_Type()
)
cfprApVnicIScsiStaticTargetIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiStaticTargetIfRn.setStatus("current")
_CfprApVnicIScsiStaticTargetIfIpAddress_Type = InetAddressIPv4
_CfprApVnicIScsiStaticTargetIfIpAddress_Object = MibTableColumn
cfprApVnicIScsiStaticTargetIfIpAddress = _CfprApVnicIScsiStaticTargetIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 33, 1, 5),
    _CfprApVnicIScsiStaticTargetIfIpAddress_Type()
)
cfprApVnicIScsiStaticTargetIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiStaticTargetIfIpAddress.setStatus("current")
_CfprApVnicIScsiStaticTargetIfName_Type = SnmpAdminString
_CfprApVnicIScsiStaticTargetIfName_Object = MibTableColumn
cfprApVnicIScsiStaticTargetIfName = _CfprApVnicIScsiStaticTargetIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 33, 1, 6),
    _CfprApVnicIScsiStaticTargetIfName_Type()
)
cfprApVnicIScsiStaticTargetIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiStaticTargetIfName.setStatus("current")
_CfprApVnicIScsiStaticTargetIfPort_Type = Gauge32
_CfprApVnicIScsiStaticTargetIfPort_Object = MibTableColumn
cfprApVnicIScsiStaticTargetIfPort = _CfprApVnicIScsiStaticTargetIfPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 33, 1, 8),
    _CfprApVnicIScsiStaticTargetIfPort_Type()
)
cfprApVnicIScsiStaticTargetIfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiStaticTargetIfPort.setStatus("current")
_CfprApVnicIScsiStaticTargetIfPriority_Type = Gauge32
_CfprApVnicIScsiStaticTargetIfPriority_Object = MibTableColumn
cfprApVnicIScsiStaticTargetIfPriority = _CfprApVnicIScsiStaticTargetIfPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 33, 1, 9),
    _CfprApVnicIScsiStaticTargetIfPriority_Type()
)
cfprApVnicIScsiStaticTargetIfPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIScsiStaticTargetIfPriority.setStatus("current")
_CfprApVnicInternalProfileTable_Object = MibTable
cfprApVnicInternalProfileTable = _CfprApVnicInternalProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 34)
)
if mibBuilder.loadTexts:
    cfprApVnicInternalProfileTable.setStatus("current")
_CfprApVnicInternalProfileEntry_Object = MibTableRow
cfprApVnicInternalProfileEntry = _CfprApVnicInternalProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 34, 1)
)
cfprApVnicInternalProfileEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicInternalProfileInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicInternalProfileEntry.setStatus("current")
_CfprApVnicInternalProfileInstanceId_Type = CfprApManagedObjectId
_CfprApVnicInternalProfileInstanceId_Object = MibTableColumn
cfprApVnicInternalProfileInstanceId = _CfprApVnicInternalProfileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 34, 1, 1),
    _CfprApVnicInternalProfileInstanceId_Type()
)
cfprApVnicInternalProfileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicInternalProfileInstanceId.setStatus("current")
_CfprApVnicInternalProfileDn_Type = CfprApManagedObjectDn
_CfprApVnicInternalProfileDn_Object = MibTableColumn
cfprApVnicInternalProfileDn = _CfprApVnicInternalProfileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 34, 1, 2),
    _CfprApVnicInternalProfileDn_Type()
)
cfprApVnicInternalProfileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicInternalProfileDn.setStatus("current")
_CfprApVnicInternalProfileRn_Type = SnmpAdminString
_CfprApVnicInternalProfileRn_Object = MibTableColumn
cfprApVnicInternalProfileRn = _CfprApVnicInternalProfileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 34, 1, 3),
    _CfprApVnicInternalProfileRn_Type()
)
cfprApVnicInternalProfileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicInternalProfileRn.setStatus("current")
_CfprApVnicInternalProfileDescr_Type = SnmpAdminString
_CfprApVnicInternalProfileDescr_Object = MibTableColumn
cfprApVnicInternalProfileDescr = _CfprApVnicInternalProfileDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 34, 1, 4),
    _CfprApVnicInternalProfileDescr_Type()
)
cfprApVnicInternalProfileDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicInternalProfileDescr.setStatus("current")
_CfprApVnicInternalProfileIntId_Type = SnmpAdminString
_CfprApVnicInternalProfileIntId_Object = MibTableColumn
cfprApVnicInternalProfileIntId = _CfprApVnicInternalProfileIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 34, 1, 5),
    _CfprApVnicInternalProfileIntId_Type()
)
cfprApVnicInternalProfileIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicInternalProfileIntId.setStatus("current")
_CfprApVnicInternalProfileMaxPorts_Type = Gauge32
_CfprApVnicInternalProfileMaxPorts_Object = MibTableColumn
cfprApVnicInternalProfileMaxPorts = _CfprApVnicInternalProfileMaxPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 34, 1, 6),
    _CfprApVnicInternalProfileMaxPorts_Type()
)
cfprApVnicInternalProfileMaxPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicInternalProfileMaxPorts.setStatus("current")
_CfprApVnicInternalProfileName_Type = SnmpAdminString
_CfprApVnicInternalProfileName_Object = MibTableColumn
cfprApVnicInternalProfileName = _CfprApVnicInternalProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 34, 1, 7),
    _CfprApVnicInternalProfileName_Type()
)
cfprApVnicInternalProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicInternalProfileName.setStatus("current")
_CfprApVnicInternalProfilePolicyLevel_Type = Gauge32
_CfprApVnicInternalProfilePolicyLevel_Object = MibTableColumn
cfprApVnicInternalProfilePolicyLevel = _CfprApVnicInternalProfilePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 34, 1, 8),
    _CfprApVnicInternalProfilePolicyLevel_Type()
)
cfprApVnicInternalProfilePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicInternalProfilePolicyLevel.setStatus("current")
_CfprApVnicInternalProfilePolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApVnicInternalProfilePolicyOwner_Object = MibTableColumn
cfprApVnicInternalProfilePolicyOwner = _CfprApVnicInternalProfilePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 34, 1, 9),
    _CfprApVnicInternalProfilePolicyOwner_Type()
)
cfprApVnicInternalProfilePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicInternalProfilePolicyOwner.setStatus("current")
_CfprApVnicIpV4HistoryTable_Object = MibTable
cfprApVnicIpV4HistoryTable = _CfprApVnicIpV4HistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 35)
)
if mibBuilder.loadTexts:
    cfprApVnicIpV4HistoryTable.setStatus("current")
_CfprApVnicIpV4HistoryEntry_Object = MibTableRow
cfprApVnicIpV4HistoryEntry = _CfprApVnicIpV4HistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 35, 1)
)
cfprApVnicIpV4HistoryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicIpV4HistoryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicIpV4HistoryEntry.setStatus("current")
_CfprApVnicIpV4HistoryInstanceId_Type = CfprApManagedObjectId
_CfprApVnicIpV4HistoryInstanceId_Object = MibTableColumn
cfprApVnicIpV4HistoryInstanceId = _CfprApVnicIpV4HistoryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 35, 1, 1),
    _CfprApVnicIpV4HistoryInstanceId_Type()
)
cfprApVnicIpV4HistoryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicIpV4HistoryInstanceId.setStatus("current")
_CfprApVnicIpV4HistoryDn_Type = CfprApManagedObjectDn
_CfprApVnicIpV4HistoryDn_Object = MibTableColumn
cfprApVnicIpV4HistoryDn = _CfprApVnicIpV4HistoryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 35, 1, 2),
    _CfprApVnicIpV4HistoryDn_Type()
)
cfprApVnicIpV4HistoryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV4HistoryDn.setStatus("current")
_CfprApVnicIpV4HistoryRn_Type = SnmpAdminString
_CfprApVnicIpV4HistoryRn_Object = MibTableColumn
cfprApVnicIpV4HistoryRn = _CfprApVnicIpV4HistoryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 35, 1, 3),
    _CfprApVnicIpV4HistoryRn_Type()
)
cfprApVnicIpV4HistoryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV4HistoryRn.setStatus("current")
_CfprApVnicIpV4HistoryOldIpV4Addr_Type = InetAddressIPv4
_CfprApVnicIpV4HistoryOldIpV4Addr_Object = MibTableColumn
cfprApVnicIpV4HistoryOldIpV4Addr = _CfprApVnicIpV4HistoryOldIpV4Addr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 35, 1, 4),
    _CfprApVnicIpV4HistoryOldIpV4Addr_Type()
)
cfprApVnicIpV4HistoryOldIpV4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV4HistoryOldIpV4Addr.setStatus("current")
_CfprApVnicIpV4MgmtPooledAddrTable_Object = MibTable
cfprApVnicIpV4MgmtPooledAddrTable = _CfprApVnicIpV4MgmtPooledAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 36)
)
if mibBuilder.loadTexts:
    cfprApVnicIpV4MgmtPooledAddrTable.setStatus("current")
_CfprApVnicIpV4MgmtPooledAddrEntry_Object = MibTableRow
cfprApVnicIpV4MgmtPooledAddrEntry = _CfprApVnicIpV4MgmtPooledAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 36, 1)
)
cfprApVnicIpV4MgmtPooledAddrEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicIpV4MgmtPooledAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicIpV4MgmtPooledAddrEntry.setStatus("current")
_CfprApVnicIpV4MgmtPooledAddrInstanceId_Type = CfprApManagedObjectId
_CfprApVnicIpV4MgmtPooledAddrInstanceId_Object = MibTableColumn
cfprApVnicIpV4MgmtPooledAddrInstanceId = _CfprApVnicIpV4MgmtPooledAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 36, 1, 1),
    _CfprApVnicIpV4MgmtPooledAddrInstanceId_Type()
)
cfprApVnicIpV4MgmtPooledAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicIpV4MgmtPooledAddrInstanceId.setStatus("current")
_CfprApVnicIpV4MgmtPooledAddrDn_Type = CfprApManagedObjectDn
_CfprApVnicIpV4MgmtPooledAddrDn_Object = MibTableColumn
cfprApVnicIpV4MgmtPooledAddrDn = _CfprApVnicIpV4MgmtPooledAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 36, 1, 2),
    _CfprApVnicIpV4MgmtPooledAddrDn_Type()
)
cfprApVnicIpV4MgmtPooledAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV4MgmtPooledAddrDn.setStatus("current")
_CfprApVnicIpV4MgmtPooledAddrRn_Type = SnmpAdminString
_CfprApVnicIpV4MgmtPooledAddrRn_Object = MibTableColumn
cfprApVnicIpV4MgmtPooledAddrRn = _CfprApVnicIpV4MgmtPooledAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 36, 1, 3),
    _CfprApVnicIpV4MgmtPooledAddrRn_Type()
)
cfprApVnicIpV4MgmtPooledAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV4MgmtPooledAddrRn.setStatus("current")
_CfprApVnicIpV4MgmtPooledAddrAddr_Type = InetAddressIPv4
_CfprApVnicIpV4MgmtPooledAddrAddr_Object = MibTableColumn
cfprApVnicIpV4MgmtPooledAddrAddr = _CfprApVnicIpV4MgmtPooledAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 36, 1, 4),
    _CfprApVnicIpV4MgmtPooledAddrAddr_Type()
)
cfprApVnicIpV4MgmtPooledAddrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV4MgmtPooledAddrAddr.setStatus("current")
_CfprApVnicIpV4MgmtPooledAddrDefGw_Type = InetAddressIPv4
_CfprApVnicIpV4MgmtPooledAddrDefGw_Object = MibTableColumn
cfprApVnicIpV4MgmtPooledAddrDefGw = _CfprApVnicIpV4MgmtPooledAddrDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 36, 1, 5),
    _CfprApVnicIpV4MgmtPooledAddrDefGw_Type()
)
cfprApVnicIpV4MgmtPooledAddrDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV4MgmtPooledAddrDefGw.setStatus("current")
_CfprApVnicIpV4MgmtPooledAddrName_Type = SnmpAdminString
_CfprApVnicIpV4MgmtPooledAddrName_Object = MibTableColumn
cfprApVnicIpV4MgmtPooledAddrName = _CfprApVnicIpV4MgmtPooledAddrName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 36, 1, 6),
    _CfprApVnicIpV4MgmtPooledAddrName_Type()
)
cfprApVnicIpV4MgmtPooledAddrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV4MgmtPooledAddrName.setStatus("current")
_CfprApVnicIpV4MgmtPooledAddrOperName_Type = SnmpAdminString
_CfprApVnicIpV4MgmtPooledAddrOperName_Object = MibTableColumn
cfprApVnicIpV4MgmtPooledAddrOperName = _CfprApVnicIpV4MgmtPooledAddrOperName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 36, 1, 7),
    _CfprApVnicIpV4MgmtPooledAddrOperName_Type()
)
cfprApVnicIpV4MgmtPooledAddrOperName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV4MgmtPooledAddrOperName.setStatus("current")
_CfprApVnicIpV4MgmtPooledAddrPrimDns_Type = InetAddressIPv4
_CfprApVnicIpV4MgmtPooledAddrPrimDns_Object = MibTableColumn
cfprApVnicIpV4MgmtPooledAddrPrimDns = _CfprApVnicIpV4MgmtPooledAddrPrimDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 36, 1, 8),
    _CfprApVnicIpV4MgmtPooledAddrPrimDns_Type()
)
cfprApVnicIpV4MgmtPooledAddrPrimDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV4MgmtPooledAddrPrimDns.setStatus("current")
_CfprApVnicIpV4MgmtPooledAddrSecDns_Type = InetAddressIPv4
_CfprApVnicIpV4MgmtPooledAddrSecDns_Object = MibTableColumn
cfprApVnicIpV4MgmtPooledAddrSecDns = _CfprApVnicIpV4MgmtPooledAddrSecDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 36, 1, 9),
    _CfprApVnicIpV4MgmtPooledAddrSecDns_Type()
)
cfprApVnicIpV4MgmtPooledAddrSecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV4MgmtPooledAddrSecDns.setStatus("current")
_CfprApVnicIpV4MgmtPooledAddrSubnet_Type = InetAddressIPv4
_CfprApVnicIpV4MgmtPooledAddrSubnet_Object = MibTableColumn
cfprApVnicIpV4MgmtPooledAddrSubnet = _CfprApVnicIpV4MgmtPooledAddrSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 36, 1, 10),
    _CfprApVnicIpV4MgmtPooledAddrSubnet_Type()
)
cfprApVnicIpV4MgmtPooledAddrSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV4MgmtPooledAddrSubnet.setStatus("current")
_CfprApVnicIpV4PooledAddrTable_Object = MibTable
cfprApVnicIpV4PooledAddrTable = _CfprApVnicIpV4PooledAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 37)
)
if mibBuilder.loadTexts:
    cfprApVnicIpV4PooledAddrTable.setStatus("current")
_CfprApVnicIpV4PooledAddrEntry_Object = MibTableRow
cfprApVnicIpV4PooledAddrEntry = _CfprApVnicIpV4PooledAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 37, 1)
)
cfprApVnicIpV4PooledAddrEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicIpV4PooledAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicIpV4PooledAddrEntry.setStatus("current")
_CfprApVnicIpV4PooledAddrInstanceId_Type = CfprApManagedObjectId
_CfprApVnicIpV4PooledAddrInstanceId_Object = MibTableColumn
cfprApVnicIpV4PooledAddrInstanceId = _CfprApVnicIpV4PooledAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 37, 1, 1),
    _CfprApVnicIpV4PooledAddrInstanceId_Type()
)
cfprApVnicIpV4PooledAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicIpV4PooledAddrInstanceId.setStatus("current")
_CfprApVnicIpV4PooledAddrDn_Type = CfprApManagedObjectDn
_CfprApVnicIpV4PooledAddrDn_Object = MibTableColumn
cfprApVnicIpV4PooledAddrDn = _CfprApVnicIpV4PooledAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 37, 1, 2),
    _CfprApVnicIpV4PooledAddrDn_Type()
)
cfprApVnicIpV4PooledAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV4PooledAddrDn.setStatus("current")
_CfprApVnicIpV4PooledAddrRn_Type = SnmpAdminString
_CfprApVnicIpV4PooledAddrRn_Object = MibTableColumn
cfprApVnicIpV4PooledAddrRn = _CfprApVnicIpV4PooledAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 37, 1, 3),
    _CfprApVnicIpV4PooledAddrRn_Type()
)
cfprApVnicIpV4PooledAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV4PooledAddrRn.setStatus("current")
_CfprApVnicIpV4PooledAddrAddr_Type = InetAddressIPv4
_CfprApVnicIpV4PooledAddrAddr_Object = MibTableColumn
cfprApVnicIpV4PooledAddrAddr = _CfprApVnicIpV4PooledAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 37, 1, 4),
    _CfprApVnicIpV4PooledAddrAddr_Type()
)
cfprApVnicIpV4PooledAddrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV4PooledAddrAddr.setStatus("current")
_CfprApVnicIpV4PooledAddrDefGw_Type = InetAddressIPv4
_CfprApVnicIpV4PooledAddrDefGw_Object = MibTableColumn
cfprApVnicIpV4PooledAddrDefGw = _CfprApVnicIpV4PooledAddrDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 37, 1, 5),
    _CfprApVnicIpV4PooledAddrDefGw_Type()
)
cfprApVnicIpV4PooledAddrDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV4PooledAddrDefGw.setStatus("current")
_CfprApVnicIpV4PooledAddrName_Type = SnmpAdminString
_CfprApVnicIpV4PooledAddrName_Object = MibTableColumn
cfprApVnicIpV4PooledAddrName = _CfprApVnicIpV4PooledAddrName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 37, 1, 6),
    _CfprApVnicIpV4PooledAddrName_Type()
)
cfprApVnicIpV4PooledAddrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV4PooledAddrName.setStatus("current")
_CfprApVnicIpV4PooledAddrOperName_Type = SnmpAdminString
_CfprApVnicIpV4PooledAddrOperName_Object = MibTableColumn
cfprApVnicIpV4PooledAddrOperName = _CfprApVnicIpV4PooledAddrOperName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 37, 1, 7),
    _CfprApVnicIpV4PooledAddrOperName_Type()
)
cfprApVnicIpV4PooledAddrOperName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV4PooledAddrOperName.setStatus("current")
_CfprApVnicIpV4PooledAddrPrimDns_Type = InetAddressIPv4
_CfprApVnicIpV4PooledAddrPrimDns_Object = MibTableColumn
cfprApVnicIpV4PooledAddrPrimDns = _CfprApVnicIpV4PooledAddrPrimDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 37, 1, 8),
    _CfprApVnicIpV4PooledAddrPrimDns_Type()
)
cfprApVnicIpV4PooledAddrPrimDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV4PooledAddrPrimDns.setStatus("current")
_CfprApVnicIpV4PooledAddrSecDns_Type = InetAddressIPv4
_CfprApVnicIpV4PooledAddrSecDns_Object = MibTableColumn
cfprApVnicIpV4PooledAddrSecDns = _CfprApVnicIpV4PooledAddrSecDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 37, 1, 9),
    _CfprApVnicIpV4PooledAddrSecDns_Type()
)
cfprApVnicIpV4PooledAddrSecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV4PooledAddrSecDns.setStatus("current")
_CfprApVnicIpV4PooledAddrSubnet_Type = InetAddressIPv4
_CfprApVnicIpV4PooledAddrSubnet_Object = MibTableColumn
cfprApVnicIpV4PooledAddrSubnet = _CfprApVnicIpV4PooledAddrSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 37, 1, 10),
    _CfprApVnicIpV4PooledAddrSubnet_Type()
)
cfprApVnicIpV4PooledAddrSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV4PooledAddrSubnet.setStatus("current")
_CfprApVnicIpV4ProfDerivedAddrTable_Object = MibTable
cfprApVnicIpV4ProfDerivedAddrTable = _CfprApVnicIpV4ProfDerivedAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 38)
)
if mibBuilder.loadTexts:
    cfprApVnicIpV4ProfDerivedAddrTable.setStatus("current")
_CfprApVnicIpV4ProfDerivedAddrEntry_Object = MibTableRow
cfprApVnicIpV4ProfDerivedAddrEntry = _CfprApVnicIpV4ProfDerivedAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 38, 1)
)
cfprApVnicIpV4ProfDerivedAddrEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicIpV4ProfDerivedAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicIpV4ProfDerivedAddrEntry.setStatus("current")
_CfprApVnicIpV4ProfDerivedAddrInstanceId_Type = CfprApManagedObjectId
_CfprApVnicIpV4ProfDerivedAddrInstanceId_Object = MibTableColumn
cfprApVnicIpV4ProfDerivedAddrInstanceId = _CfprApVnicIpV4ProfDerivedAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 38, 1, 1),
    _CfprApVnicIpV4ProfDerivedAddrInstanceId_Type()
)
cfprApVnicIpV4ProfDerivedAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicIpV4ProfDerivedAddrInstanceId.setStatus("current")
_CfprApVnicIpV4ProfDerivedAddrDn_Type = CfprApManagedObjectDn
_CfprApVnicIpV4ProfDerivedAddrDn_Object = MibTableColumn
cfprApVnicIpV4ProfDerivedAddrDn = _CfprApVnicIpV4ProfDerivedAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 38, 1, 2),
    _CfprApVnicIpV4ProfDerivedAddrDn_Type()
)
cfprApVnicIpV4ProfDerivedAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV4ProfDerivedAddrDn.setStatus("current")
_CfprApVnicIpV4ProfDerivedAddrRn_Type = SnmpAdminString
_CfprApVnicIpV4ProfDerivedAddrRn_Object = MibTableColumn
cfprApVnicIpV4ProfDerivedAddrRn = _CfprApVnicIpV4ProfDerivedAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 38, 1, 3),
    _CfprApVnicIpV4ProfDerivedAddrRn_Type()
)
cfprApVnicIpV4ProfDerivedAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV4ProfDerivedAddrRn.setStatus("current")
_CfprApVnicIpV4ProfDerivedAddrAddr_Type = InetAddressIPv4
_CfprApVnicIpV4ProfDerivedAddrAddr_Object = MibTableColumn
cfprApVnicIpV4ProfDerivedAddrAddr = _CfprApVnicIpV4ProfDerivedAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 38, 1, 4),
    _CfprApVnicIpV4ProfDerivedAddrAddr_Type()
)
cfprApVnicIpV4ProfDerivedAddrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV4ProfDerivedAddrAddr.setStatus("current")
_CfprApVnicIpV4ProfDerivedAddrDefGw_Type = InetAddressIPv4
_CfprApVnicIpV4ProfDerivedAddrDefGw_Object = MibTableColumn
cfprApVnicIpV4ProfDerivedAddrDefGw = _CfprApVnicIpV4ProfDerivedAddrDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 38, 1, 5),
    _CfprApVnicIpV4ProfDerivedAddrDefGw_Type()
)
cfprApVnicIpV4ProfDerivedAddrDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV4ProfDerivedAddrDefGw.setStatus("current")
_CfprApVnicIpV4ProfDerivedAddrSubnet_Type = InetAddressIPv4
_CfprApVnicIpV4ProfDerivedAddrSubnet_Object = MibTableColumn
cfprApVnicIpV4ProfDerivedAddrSubnet = _CfprApVnicIpV4ProfDerivedAddrSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 38, 1, 6),
    _CfprApVnicIpV4ProfDerivedAddrSubnet_Type()
)
cfprApVnicIpV4ProfDerivedAddrSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV4ProfDerivedAddrSubnet.setStatus("current")
_CfprApVnicIpV4StaticAddrTable_Object = MibTable
cfprApVnicIpV4StaticAddrTable = _CfprApVnicIpV4StaticAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 39)
)
if mibBuilder.loadTexts:
    cfprApVnicIpV4StaticAddrTable.setStatus("current")
_CfprApVnicIpV4StaticAddrEntry_Object = MibTableRow
cfprApVnicIpV4StaticAddrEntry = _CfprApVnicIpV4StaticAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 39, 1)
)
cfprApVnicIpV4StaticAddrEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicIpV4StaticAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicIpV4StaticAddrEntry.setStatus("current")
_CfprApVnicIpV4StaticAddrInstanceId_Type = CfprApManagedObjectId
_CfprApVnicIpV4StaticAddrInstanceId_Object = MibTableColumn
cfprApVnicIpV4StaticAddrInstanceId = _CfprApVnicIpV4StaticAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 39, 1, 1),
    _CfprApVnicIpV4StaticAddrInstanceId_Type()
)
cfprApVnicIpV4StaticAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicIpV4StaticAddrInstanceId.setStatus("current")
_CfprApVnicIpV4StaticAddrDn_Type = CfprApManagedObjectDn
_CfprApVnicIpV4StaticAddrDn_Object = MibTableColumn
cfprApVnicIpV4StaticAddrDn = _CfprApVnicIpV4StaticAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 39, 1, 2),
    _CfprApVnicIpV4StaticAddrDn_Type()
)
cfprApVnicIpV4StaticAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV4StaticAddrDn.setStatus("current")
_CfprApVnicIpV4StaticAddrRn_Type = SnmpAdminString
_CfprApVnicIpV4StaticAddrRn_Object = MibTableColumn
cfprApVnicIpV4StaticAddrRn = _CfprApVnicIpV4StaticAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 39, 1, 3),
    _CfprApVnicIpV4StaticAddrRn_Type()
)
cfprApVnicIpV4StaticAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV4StaticAddrRn.setStatus("current")
_CfprApVnicIpV4StaticAddrAddr_Type = InetAddressIPv4
_CfprApVnicIpV4StaticAddrAddr_Object = MibTableColumn
cfprApVnicIpV4StaticAddrAddr = _CfprApVnicIpV4StaticAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 39, 1, 4),
    _CfprApVnicIpV4StaticAddrAddr_Type()
)
cfprApVnicIpV4StaticAddrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV4StaticAddrAddr.setStatus("current")
_CfprApVnicIpV4StaticAddrDefGw_Type = InetAddressIPv4
_CfprApVnicIpV4StaticAddrDefGw_Object = MibTableColumn
cfprApVnicIpV4StaticAddrDefGw = _CfprApVnicIpV4StaticAddrDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 39, 1, 5),
    _CfprApVnicIpV4StaticAddrDefGw_Type()
)
cfprApVnicIpV4StaticAddrDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV4StaticAddrDefGw.setStatus("current")
_CfprApVnicIpV4StaticAddrPrimDns_Type = InetAddressIPv4
_CfprApVnicIpV4StaticAddrPrimDns_Object = MibTableColumn
cfprApVnicIpV4StaticAddrPrimDns = _CfprApVnicIpV4StaticAddrPrimDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 39, 1, 6),
    _CfprApVnicIpV4StaticAddrPrimDns_Type()
)
cfprApVnicIpV4StaticAddrPrimDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV4StaticAddrPrimDns.setStatus("current")
_CfprApVnicIpV4StaticAddrSecDns_Type = InetAddressIPv4
_CfprApVnicIpV4StaticAddrSecDns_Object = MibTableColumn
cfprApVnicIpV4StaticAddrSecDns = _CfprApVnicIpV4StaticAddrSecDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 39, 1, 7),
    _CfprApVnicIpV4StaticAddrSecDns_Type()
)
cfprApVnicIpV4StaticAddrSecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV4StaticAddrSecDns.setStatus("current")
_CfprApVnicIpV4StaticAddrSubnet_Type = InetAddressIPv4
_CfprApVnicIpV4StaticAddrSubnet_Object = MibTableColumn
cfprApVnicIpV4StaticAddrSubnet = _CfprApVnicIpV4StaticAddrSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 39, 1, 8),
    _CfprApVnicIpV4StaticAddrSubnet_Type()
)
cfprApVnicIpV4StaticAddrSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV4StaticAddrSubnet.setStatus("current")
_CfprApVnicIpV6HistoryTable_Object = MibTable
cfprApVnicIpV6HistoryTable = _CfprApVnicIpV6HistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 40)
)
if mibBuilder.loadTexts:
    cfprApVnicIpV6HistoryTable.setStatus("current")
_CfprApVnicIpV6HistoryEntry_Object = MibTableRow
cfprApVnicIpV6HistoryEntry = _CfprApVnicIpV6HistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 40, 1)
)
cfprApVnicIpV6HistoryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicIpV6HistoryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicIpV6HistoryEntry.setStatus("current")
_CfprApVnicIpV6HistoryInstanceId_Type = CfprApManagedObjectId
_CfprApVnicIpV6HistoryInstanceId_Object = MibTableColumn
cfprApVnicIpV6HistoryInstanceId = _CfprApVnicIpV6HistoryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 40, 1, 1),
    _CfprApVnicIpV6HistoryInstanceId_Type()
)
cfprApVnicIpV6HistoryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicIpV6HistoryInstanceId.setStatus("current")
_CfprApVnicIpV6HistoryDn_Type = CfprApManagedObjectDn
_CfprApVnicIpV6HistoryDn_Object = MibTableColumn
cfprApVnicIpV6HistoryDn = _CfprApVnicIpV6HistoryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 40, 1, 2),
    _CfprApVnicIpV6HistoryDn_Type()
)
cfprApVnicIpV6HistoryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV6HistoryDn.setStatus("current")
_CfprApVnicIpV6HistoryRn_Type = SnmpAdminString
_CfprApVnicIpV6HistoryRn_Object = MibTableColumn
cfprApVnicIpV6HistoryRn = _CfprApVnicIpV6HistoryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 40, 1, 3),
    _CfprApVnicIpV6HistoryRn_Type()
)
cfprApVnicIpV6HistoryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV6HistoryRn.setStatus("current")
_CfprApVnicIpV6HistoryOldIpV6Addr_Type = InetAddressIPv6
_CfprApVnicIpV6HistoryOldIpV6Addr_Object = MibTableColumn
cfprApVnicIpV6HistoryOldIpV6Addr = _CfprApVnicIpV6HistoryOldIpV6Addr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 40, 1, 4),
    _CfprApVnicIpV6HistoryOldIpV6Addr_Type()
)
cfprApVnicIpV6HistoryOldIpV6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV6HistoryOldIpV6Addr.setStatus("current")
_CfprApVnicIpV6MgmtPooledAddrTable_Object = MibTable
cfprApVnicIpV6MgmtPooledAddrTable = _CfprApVnicIpV6MgmtPooledAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 41)
)
if mibBuilder.loadTexts:
    cfprApVnicIpV6MgmtPooledAddrTable.setStatus("current")
_CfprApVnicIpV6MgmtPooledAddrEntry_Object = MibTableRow
cfprApVnicIpV6MgmtPooledAddrEntry = _CfprApVnicIpV6MgmtPooledAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 41, 1)
)
cfprApVnicIpV6MgmtPooledAddrEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicIpV6MgmtPooledAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicIpV6MgmtPooledAddrEntry.setStatus("current")
_CfprApVnicIpV6MgmtPooledAddrInstanceId_Type = CfprApManagedObjectId
_CfprApVnicIpV6MgmtPooledAddrInstanceId_Object = MibTableColumn
cfprApVnicIpV6MgmtPooledAddrInstanceId = _CfprApVnicIpV6MgmtPooledAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 41, 1, 1),
    _CfprApVnicIpV6MgmtPooledAddrInstanceId_Type()
)
cfprApVnicIpV6MgmtPooledAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicIpV6MgmtPooledAddrInstanceId.setStatus("current")
_CfprApVnicIpV6MgmtPooledAddrDn_Type = CfprApManagedObjectDn
_CfprApVnicIpV6MgmtPooledAddrDn_Object = MibTableColumn
cfprApVnicIpV6MgmtPooledAddrDn = _CfprApVnicIpV6MgmtPooledAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 41, 1, 2),
    _CfprApVnicIpV6MgmtPooledAddrDn_Type()
)
cfprApVnicIpV6MgmtPooledAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV6MgmtPooledAddrDn.setStatus("current")
_CfprApVnicIpV6MgmtPooledAddrRn_Type = SnmpAdminString
_CfprApVnicIpV6MgmtPooledAddrRn_Object = MibTableColumn
cfprApVnicIpV6MgmtPooledAddrRn = _CfprApVnicIpV6MgmtPooledAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 41, 1, 3),
    _CfprApVnicIpV6MgmtPooledAddrRn_Type()
)
cfprApVnicIpV6MgmtPooledAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV6MgmtPooledAddrRn.setStatus("current")
_CfprApVnicIpV6MgmtPooledAddrAddr_Type = InetAddressIPv6
_CfprApVnicIpV6MgmtPooledAddrAddr_Object = MibTableColumn
cfprApVnicIpV6MgmtPooledAddrAddr = _CfprApVnicIpV6MgmtPooledAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 41, 1, 4),
    _CfprApVnicIpV6MgmtPooledAddrAddr_Type()
)
cfprApVnicIpV6MgmtPooledAddrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV6MgmtPooledAddrAddr.setStatus("current")
_CfprApVnicIpV6MgmtPooledAddrDefGw_Type = InetAddressIPv6
_CfprApVnicIpV6MgmtPooledAddrDefGw_Object = MibTableColumn
cfprApVnicIpV6MgmtPooledAddrDefGw = _CfprApVnicIpV6MgmtPooledAddrDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 41, 1, 5),
    _CfprApVnicIpV6MgmtPooledAddrDefGw_Type()
)
cfprApVnicIpV6MgmtPooledAddrDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV6MgmtPooledAddrDefGw.setStatus("current")
_CfprApVnicIpV6MgmtPooledAddrName_Type = SnmpAdminString
_CfprApVnicIpV6MgmtPooledAddrName_Object = MibTableColumn
cfprApVnicIpV6MgmtPooledAddrName = _CfprApVnicIpV6MgmtPooledAddrName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 41, 1, 6),
    _CfprApVnicIpV6MgmtPooledAddrName_Type()
)
cfprApVnicIpV6MgmtPooledAddrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV6MgmtPooledAddrName.setStatus("current")
_CfprApVnicIpV6MgmtPooledAddrOperName_Type = SnmpAdminString
_CfprApVnicIpV6MgmtPooledAddrOperName_Object = MibTableColumn
cfprApVnicIpV6MgmtPooledAddrOperName = _CfprApVnicIpV6MgmtPooledAddrOperName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 41, 1, 7),
    _CfprApVnicIpV6MgmtPooledAddrOperName_Type()
)
cfprApVnicIpV6MgmtPooledAddrOperName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV6MgmtPooledAddrOperName.setStatus("current")
_CfprApVnicIpV6MgmtPooledAddrPrefix_Type = Gauge32
_CfprApVnicIpV6MgmtPooledAddrPrefix_Object = MibTableColumn
cfprApVnicIpV6MgmtPooledAddrPrefix = _CfprApVnicIpV6MgmtPooledAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 41, 1, 8),
    _CfprApVnicIpV6MgmtPooledAddrPrefix_Type()
)
cfprApVnicIpV6MgmtPooledAddrPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV6MgmtPooledAddrPrefix.setStatus("current")
_CfprApVnicIpV6MgmtPooledAddrPrimDns_Type = InetAddressIPv6
_CfprApVnicIpV6MgmtPooledAddrPrimDns_Object = MibTableColumn
cfprApVnicIpV6MgmtPooledAddrPrimDns = _CfprApVnicIpV6MgmtPooledAddrPrimDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 41, 1, 9),
    _CfprApVnicIpV6MgmtPooledAddrPrimDns_Type()
)
cfprApVnicIpV6MgmtPooledAddrPrimDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV6MgmtPooledAddrPrimDns.setStatus("current")
_CfprApVnicIpV6MgmtPooledAddrSecDns_Type = InetAddressIPv6
_CfprApVnicIpV6MgmtPooledAddrSecDns_Object = MibTableColumn
cfprApVnicIpV6MgmtPooledAddrSecDns = _CfprApVnicIpV6MgmtPooledAddrSecDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 41, 1, 10),
    _CfprApVnicIpV6MgmtPooledAddrSecDns_Type()
)
cfprApVnicIpV6MgmtPooledAddrSecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV6MgmtPooledAddrSecDns.setStatus("current")
_CfprApVnicIpV6StaticAddrTable_Object = MibTable
cfprApVnicIpV6StaticAddrTable = _CfprApVnicIpV6StaticAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 42)
)
if mibBuilder.loadTexts:
    cfprApVnicIpV6StaticAddrTable.setStatus("current")
_CfprApVnicIpV6StaticAddrEntry_Object = MibTableRow
cfprApVnicIpV6StaticAddrEntry = _CfprApVnicIpV6StaticAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 42, 1)
)
cfprApVnicIpV6StaticAddrEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicIpV6StaticAddrInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicIpV6StaticAddrEntry.setStatus("current")
_CfprApVnicIpV6StaticAddrInstanceId_Type = CfprApManagedObjectId
_CfprApVnicIpV6StaticAddrInstanceId_Object = MibTableColumn
cfprApVnicIpV6StaticAddrInstanceId = _CfprApVnicIpV6StaticAddrInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 42, 1, 1),
    _CfprApVnicIpV6StaticAddrInstanceId_Type()
)
cfprApVnicIpV6StaticAddrInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicIpV6StaticAddrInstanceId.setStatus("current")
_CfprApVnicIpV6StaticAddrDn_Type = CfprApManagedObjectDn
_CfprApVnicIpV6StaticAddrDn_Object = MibTableColumn
cfprApVnicIpV6StaticAddrDn = _CfprApVnicIpV6StaticAddrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 42, 1, 2),
    _CfprApVnicIpV6StaticAddrDn_Type()
)
cfprApVnicIpV6StaticAddrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV6StaticAddrDn.setStatus("current")
_CfprApVnicIpV6StaticAddrRn_Type = SnmpAdminString
_CfprApVnicIpV6StaticAddrRn_Object = MibTableColumn
cfprApVnicIpV6StaticAddrRn = _CfprApVnicIpV6StaticAddrRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 42, 1, 3),
    _CfprApVnicIpV6StaticAddrRn_Type()
)
cfprApVnicIpV6StaticAddrRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV6StaticAddrRn.setStatus("current")
_CfprApVnicIpV6StaticAddrAddr_Type = InetAddressIPv6
_CfprApVnicIpV6StaticAddrAddr_Object = MibTableColumn
cfprApVnicIpV6StaticAddrAddr = _CfprApVnicIpV6StaticAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 42, 1, 4),
    _CfprApVnicIpV6StaticAddrAddr_Type()
)
cfprApVnicIpV6StaticAddrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV6StaticAddrAddr.setStatus("current")
_CfprApVnicIpV6StaticAddrDefGw_Type = InetAddressIPv6
_CfprApVnicIpV6StaticAddrDefGw_Object = MibTableColumn
cfprApVnicIpV6StaticAddrDefGw = _CfprApVnicIpV6StaticAddrDefGw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 42, 1, 5),
    _CfprApVnicIpV6StaticAddrDefGw_Type()
)
cfprApVnicIpV6StaticAddrDefGw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV6StaticAddrDefGw.setStatus("current")
_CfprApVnicIpV6StaticAddrPrefix_Type = Gauge32
_CfprApVnicIpV6StaticAddrPrefix_Object = MibTableColumn
cfprApVnicIpV6StaticAddrPrefix = _CfprApVnicIpV6StaticAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 42, 1, 6),
    _CfprApVnicIpV6StaticAddrPrefix_Type()
)
cfprApVnicIpV6StaticAddrPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV6StaticAddrPrefix.setStatus("current")
_CfprApVnicIpV6StaticAddrPrimDns_Type = InetAddressIPv6
_CfprApVnicIpV6StaticAddrPrimDns_Object = MibTableColumn
cfprApVnicIpV6StaticAddrPrimDns = _CfprApVnicIpV6StaticAddrPrimDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 42, 1, 7),
    _CfprApVnicIpV6StaticAddrPrimDns_Type()
)
cfprApVnicIpV6StaticAddrPrimDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV6StaticAddrPrimDns.setStatus("current")
_CfprApVnicIpV6StaticAddrSecDns_Type = InetAddressIPv6
_CfprApVnicIpV6StaticAddrSecDns_Object = MibTableColumn
cfprApVnicIpV6StaticAddrSecDns = _CfprApVnicIpV6StaticAddrSecDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 42, 1, 8),
    _CfprApVnicIpV6StaticAddrSecDns_Type()
)
cfprApVnicIpV6StaticAddrSecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpV6StaticAddrSecDns.setStatus("current")
_CfprApVnicIpcTable_Object = MibTable
cfprApVnicIpcTable = _CfprApVnicIpcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43)
)
if mibBuilder.loadTexts:
    cfprApVnicIpcTable.setStatus("current")
_CfprApVnicIpcEntry_Object = MibTableRow
cfprApVnicIpcEntry = _CfprApVnicIpcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1)
)
cfprApVnicIpcEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicIpcInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicIpcEntry.setStatus("current")
_CfprApVnicIpcInstanceId_Type = CfprApManagedObjectId
_CfprApVnicIpcInstanceId_Object = MibTableColumn
cfprApVnicIpcInstanceId = _CfprApVnicIpcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1, 1),
    _CfprApVnicIpcInstanceId_Type()
)
cfprApVnicIpcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicIpcInstanceId.setStatus("current")
_CfprApVnicIpcDn_Type = CfprApManagedObjectDn
_CfprApVnicIpcDn_Object = MibTableColumn
cfprApVnicIpcDn = _CfprApVnicIpcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1, 2),
    _CfprApVnicIpcDn_Type()
)
cfprApVnicIpcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcDn.setStatus("current")
_CfprApVnicIpcRn_Type = SnmpAdminString
_CfprApVnicIpcRn_Object = MibTableColumn
cfprApVnicIpcRn = _CfprApVnicIpcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1, 3),
    _CfprApVnicIpcRn_Type()
)
cfprApVnicIpcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcRn.setStatus("current")
_CfprApVnicIpcAdaptorProfileName_Type = SnmpAdminString
_CfprApVnicIpcAdaptorProfileName_Object = MibTableColumn
cfprApVnicIpcAdaptorProfileName = _CfprApVnicIpcAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1, 4),
    _CfprApVnicIpcAdaptorProfileName_Type()
)
cfprApVnicIpcAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcAdaptorProfileName.setStatus("current")
_CfprApVnicIpcAddr_Type = MacAddress
_CfprApVnicIpcAddr_Object = MibTableColumn
cfprApVnicIpcAddr = _CfprApVnicIpcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1, 5),
    _CfprApVnicIpcAddr_Type()
)
cfprApVnicIpcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcAddr.setStatus("current")
_CfprApVnicIpcAdminHostPort_Type = CfprApFabricHostPortId
_CfprApVnicIpcAdminHostPort_Object = MibTableColumn
cfprApVnicIpcAdminHostPort = _CfprApVnicIpcAdminHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1, 6),
    _CfprApVnicIpcAdminHostPort_Type()
)
cfprApVnicIpcAdminHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcAdminHostPort.setStatus("current")
_CfprApVnicIpcAdminVcon_Type = SnmpAdminString
_CfprApVnicIpcAdminVcon_Object = MibTableColumn
cfprApVnicIpcAdminVcon = _CfprApVnicIpcAdminVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1, 7),
    _CfprApVnicIpcAdminVcon_Type()
)
cfprApVnicIpcAdminVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcAdminVcon.setStatus("current")
_CfprApVnicIpcAppRole_Type = CfprApVnicAppRole
_CfprApVnicIpcAppRole_Object = MibTableColumn
cfprApVnicIpcAppRole = _CfprApVnicIpcAppRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1, 8),
    _CfprApVnicIpcAppRole_Type()
)
cfprApVnicIpcAppRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcAppRole.setStatus("current")
_CfprApVnicIpcBootDev_Type = CfprApVnicVnicBootDev
_CfprApVnicIpcBootDev_Object = MibTableColumn
cfprApVnicIpcBootDev = _CfprApVnicIpcBootDev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1, 9),
    _CfprApVnicIpcBootDev_Type()
)
cfprApVnicIpcBootDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcBootDev.setStatus("current")
_CfprApVnicIpcConfigQualifier_Type = CfprApVnicConfigIssues
_CfprApVnicIpcConfigQualifier_Object = MibTableColumn
cfprApVnicIpcConfigQualifier = _CfprApVnicIpcConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1, 10),
    _CfprApVnicIpcConfigQualifier_Type()
)
cfprApVnicIpcConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcConfigQualifier.setStatus("current")
_CfprApVnicIpcConfigState_Type = CfprApLsConfigState
_CfprApVnicIpcConfigState_Object = MibTableColumn
cfprApVnicIpcConfigState = _CfprApVnicIpcConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1, 11),
    _CfprApVnicIpcConfigState_Type()
)
cfprApVnicIpcConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcConfigState.setStatus("current")
_CfprApVnicIpcEquipmentDn_Type = SnmpAdminString
_CfprApVnicIpcEquipmentDn_Object = MibTableColumn
cfprApVnicIpcEquipmentDn = _CfprApVnicIpcEquipmentDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1, 12),
    _CfprApVnicIpcEquipmentDn_Type()
)
cfprApVnicIpcEquipmentDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcEquipmentDn.setStatus("current")
_CfprApVnicIpcIdentPoolName_Type = SnmpAdminString
_CfprApVnicIpcIdentPoolName_Object = MibTableColumn
cfprApVnicIpcIdentPoolName = _CfprApVnicIpcIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1, 13),
    _CfprApVnicIpcIdentPoolName_Type()
)
cfprApVnicIpcIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcIdentPoolName.setStatus("current")
_CfprApVnicIpcInstType_Type = CfprApVnicInstantiation
_CfprApVnicIpcInstType_Object = MibTableColumn
cfprApVnicIpcInstType = _CfprApVnicIpcInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1, 14),
    _CfprApVnicIpcInstType_Type()
)
cfprApVnicIpcInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcInstType.setStatus("current")
_CfprApVnicIpcMtu_Type = Gauge32
_CfprApVnicIpcMtu_Object = MibTableColumn
cfprApVnicIpcMtu = _CfprApVnicIpcMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1, 15),
    _CfprApVnicIpcMtu_Type()
)
cfprApVnicIpcMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcMtu.setStatus("current")
_CfprApVnicIpcName_Type = SnmpAdminString
_CfprApVnicIpcName_Object = MibTableColumn
cfprApVnicIpcName = _CfprApVnicIpcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1, 16),
    _CfprApVnicIpcName_Type()
)
cfprApVnicIpcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcName.setStatus("current")
_CfprApVnicIpcNwCtrlPolicyName_Type = SnmpAdminString
_CfprApVnicIpcNwCtrlPolicyName_Object = MibTableColumn
cfprApVnicIpcNwCtrlPolicyName = _CfprApVnicIpcNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1, 17),
    _CfprApVnicIpcNwCtrlPolicyName_Type()
)
cfprApVnicIpcNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcNwCtrlPolicyName.setStatus("current")
_CfprApVnicIpcNwTemplName_Type = SnmpAdminString
_CfprApVnicIpcNwTemplName_Object = MibTableColumn
cfprApVnicIpcNwTemplName = _CfprApVnicIpcNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1, 18),
    _CfprApVnicIpcNwTemplName_Type()
)
cfprApVnicIpcNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcNwTemplName.setStatus("current")
_CfprApVnicIpcOperAdaptorProfileName_Type = SnmpAdminString
_CfprApVnicIpcOperAdaptorProfileName_Object = MibTableColumn
cfprApVnicIpcOperAdaptorProfileName = _CfprApVnicIpcOperAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1, 19),
    _CfprApVnicIpcOperAdaptorProfileName_Type()
)
cfprApVnicIpcOperAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcOperAdaptorProfileName.setStatus("current")
_CfprApVnicIpcOperHostPort_Type = CfprApVnicVnicOperHostPort
_CfprApVnicIpcOperHostPort_Object = MibTableColumn
cfprApVnicIpcOperHostPort = _CfprApVnicIpcOperHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1, 20),
    _CfprApVnicIpcOperHostPort_Type()
)
cfprApVnicIpcOperHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcOperHostPort.setStatus("current")
_CfprApVnicIpcOperIdentPoolName_Type = SnmpAdminString
_CfprApVnicIpcOperIdentPoolName_Object = MibTableColumn
cfprApVnicIpcOperIdentPoolName = _CfprApVnicIpcOperIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1, 21),
    _CfprApVnicIpcOperIdentPoolName_Type()
)
cfprApVnicIpcOperIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcOperIdentPoolName.setStatus("current")
_CfprApVnicIpcOperNwCtrlPolicyName_Type = SnmpAdminString
_CfprApVnicIpcOperNwCtrlPolicyName_Object = MibTableColumn
cfprApVnicIpcOperNwCtrlPolicyName = _CfprApVnicIpcOperNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1, 22),
    _CfprApVnicIpcOperNwCtrlPolicyName_Type()
)
cfprApVnicIpcOperNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcOperNwCtrlPolicyName.setStatus("current")
_CfprApVnicIpcOperNwTemplName_Type = SnmpAdminString
_CfprApVnicIpcOperNwTemplName_Object = MibTableColumn
cfprApVnicIpcOperNwTemplName = _CfprApVnicIpcOperNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1, 23),
    _CfprApVnicIpcOperNwTemplName_Type()
)
cfprApVnicIpcOperNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcOperNwTemplName.setStatus("current")
_CfprApVnicIpcOperOrder_Type = Gauge32
_CfprApVnicIpcOperOrder_Object = MibTableColumn
cfprApVnicIpcOperOrder = _CfprApVnicIpcOperOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1, 24),
    _CfprApVnicIpcOperOrder_Type()
)
cfprApVnicIpcOperOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcOperOrder.setStatus("current")
_CfprApVnicIpcOperPinToGroupName_Type = SnmpAdminString
_CfprApVnicIpcOperPinToGroupName_Object = MibTableColumn
cfprApVnicIpcOperPinToGroupName = _CfprApVnicIpcOperPinToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1, 25),
    _CfprApVnicIpcOperPinToGroupName_Type()
)
cfprApVnicIpcOperPinToGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcOperPinToGroupName.setStatus("current")
_CfprApVnicIpcOperQosPolicyName_Type = SnmpAdminString
_CfprApVnicIpcOperQosPolicyName_Object = MibTableColumn
cfprApVnicIpcOperQosPolicyName = _CfprApVnicIpcOperQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1, 26),
    _CfprApVnicIpcOperQosPolicyName_Type()
)
cfprApVnicIpcOperQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcOperQosPolicyName.setStatus("current")
_CfprApVnicIpcOperSpeed_Type = Gauge32
_CfprApVnicIpcOperSpeed_Object = MibTableColumn
cfprApVnicIpcOperSpeed = _CfprApVnicIpcOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1, 27),
    _CfprApVnicIpcOperSpeed_Type()
)
cfprApVnicIpcOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcOperSpeed.setStatus("current")
_CfprApVnicIpcOperStatsPolicyName_Type = SnmpAdminString
_CfprApVnicIpcOperStatsPolicyName_Object = MibTableColumn
cfprApVnicIpcOperStatsPolicyName = _CfprApVnicIpcOperStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1, 28),
    _CfprApVnicIpcOperStatsPolicyName_Type()
)
cfprApVnicIpcOperStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcOperStatsPolicyName.setStatus("current")
_CfprApVnicIpcOperVcon_Type = SnmpAdminString
_CfprApVnicIpcOperVcon_Object = MibTableColumn
cfprApVnicIpcOperVcon = _CfprApVnicIpcOperVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1, 29),
    _CfprApVnicIpcOperVcon_Type()
)
cfprApVnicIpcOperVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcOperVcon.setStatus("current")
_CfprApVnicIpcOrder_Type = Gauge32
_CfprApVnicIpcOrder_Object = MibTableColumn
cfprApVnicIpcOrder = _CfprApVnicIpcOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1, 30),
    _CfprApVnicIpcOrder_Type()
)
cfprApVnicIpcOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcOrder.setStatus("current")
_CfprApVnicIpcOwner_Type = CfprApVnicConnectionOwner
_CfprApVnicIpcOwner_Object = MibTableColumn
cfprApVnicIpcOwner = _CfprApVnicIpcOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1, 31),
    _CfprApVnicIpcOwner_Type()
)
cfprApVnicIpcOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcOwner.setStatus("current")
_CfprApVnicIpcPinToGroupName_Type = SnmpAdminString
_CfprApVnicIpcPinToGroupName_Object = MibTableColumn
cfprApVnicIpcPinToGroupName = _CfprApVnicIpcPinToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1, 32),
    _CfprApVnicIpcPinToGroupName_Type()
)
cfprApVnicIpcPinToGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcPinToGroupName.setStatus("current")
_CfprApVnicIpcQosPolicyName_Type = SnmpAdminString
_CfprApVnicIpcQosPolicyName_Object = MibTableColumn
cfprApVnicIpcQosPolicyName = _CfprApVnicIpcQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1, 33),
    _CfprApVnicIpcQosPolicyName_Type()
)
cfprApVnicIpcQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcQosPolicyName.setStatus("current")
_CfprApVnicIpcStatsPolicyName_Type = SnmpAdminString
_CfprApVnicIpcStatsPolicyName_Object = MibTableColumn
cfprApVnicIpcStatsPolicyName = _CfprApVnicIpcStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1, 34),
    _CfprApVnicIpcStatsPolicyName_Type()
)
cfprApVnicIpcStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcStatsPolicyName.setStatus("current")
_CfprApVnicIpcSwitchId_Type = CfprApVnicEtherBaseSwitchId
_CfprApVnicIpcSwitchId_Object = MibTableColumn
cfprApVnicIpcSwitchId = _CfprApVnicIpcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1, 35),
    _CfprApVnicIpcSwitchId_Type()
)
cfprApVnicIpcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcSwitchId.setStatus("current")
_CfprApVnicIpcType_Type = CfprApVnicIpcType
_CfprApVnicIpcType_Object = MibTableColumn
cfprApVnicIpcType = _CfprApVnicIpcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 43, 1, 36),
    _CfprApVnicIpcType_Type()
)
cfprApVnicIpcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcType.setStatus("current")
_CfprApVnicIpcIfTable_Object = MibTable
cfprApVnicIpcIfTable = _CfprApVnicIpcIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 44)
)
if mibBuilder.loadTexts:
    cfprApVnicIpcIfTable.setStatus("current")
_CfprApVnicIpcIfEntry_Object = MibTableRow
cfprApVnicIpcIfEntry = _CfprApVnicIpcIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 44, 1)
)
cfprApVnicIpcIfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicIpcIfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicIpcIfEntry.setStatus("current")
_CfprApVnicIpcIfInstanceId_Type = CfprApManagedObjectId
_CfprApVnicIpcIfInstanceId_Object = MibTableColumn
cfprApVnicIpcIfInstanceId = _CfprApVnicIpcIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 44, 1, 1),
    _CfprApVnicIpcIfInstanceId_Type()
)
cfprApVnicIpcIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicIpcIfInstanceId.setStatus("current")
_CfprApVnicIpcIfDn_Type = CfprApManagedObjectDn
_CfprApVnicIpcIfDn_Object = MibTableColumn
cfprApVnicIpcIfDn = _CfprApVnicIpcIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 44, 1, 2),
    _CfprApVnicIpcIfDn_Type()
)
cfprApVnicIpcIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcIfDn.setStatus("current")
_CfprApVnicIpcIfRn_Type = SnmpAdminString
_CfprApVnicIpcIfRn_Object = MibTableColumn
cfprApVnicIpcIfRn = _CfprApVnicIpcIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 44, 1, 3),
    _CfprApVnicIpcIfRn_Type()
)
cfprApVnicIpcIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcIfRn.setStatus("current")
_CfprApVnicIpcIfAddr_Type = MacAddress
_CfprApVnicIpcIfAddr_Object = MibTableColumn
cfprApVnicIpcIfAddr = _CfprApVnicIpcIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 44, 1, 4),
    _CfprApVnicIpcIfAddr_Type()
)
cfprApVnicIpcIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcIfAddr.setStatus("current")
_CfprApVnicIpcIfConfigQualifier_Type = CfprApVnicConfigIssues
_CfprApVnicIpcIfConfigQualifier_Object = MibTableColumn
cfprApVnicIpcIfConfigQualifier = _CfprApVnicIpcIfConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 44, 1, 5),
    _CfprApVnicIpcIfConfigQualifier_Type()
)
cfprApVnicIpcIfConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcIfConfigQualifier.setStatus("current")
_CfprApVnicIpcIfDefaultNet_Type = TruthValue
_CfprApVnicIpcIfDefaultNet_Object = MibTableColumn
cfprApVnicIpcIfDefaultNet = _CfprApVnicIpcIfDefaultNet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 44, 1, 6),
    _CfprApVnicIpcIfDefaultNet_Type()
)
cfprApVnicIpcIfDefaultNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcIfDefaultNet.setStatus("current")
_CfprApVnicIpcIfName_Type = SnmpAdminString
_CfprApVnicIpcIfName_Object = MibTableColumn
cfprApVnicIpcIfName = _CfprApVnicIpcIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 44, 1, 7),
    _CfprApVnicIpcIfName_Type()
)
cfprApVnicIpcIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcIfName.setStatus("current")
_CfprApVnicIpcIfOperState_Type = CfprApVnicIfOperState
_CfprApVnicIpcIfOperState_Object = MibTableColumn
cfprApVnicIpcIfOperState = _CfprApVnicIpcIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 44, 1, 8),
    _CfprApVnicIpcIfOperState_Type()
)
cfprApVnicIpcIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcIfOperState.setStatus("current")
_CfprApVnicIpcIfOperVnetDn_Type = SnmpAdminString
_CfprApVnicIpcIfOperVnetDn_Object = MibTableColumn
cfprApVnicIpcIfOperVnetDn = _CfprApVnicIpcIfOperVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 44, 1, 9),
    _CfprApVnicIpcIfOperVnetDn_Type()
)
cfprApVnicIpcIfOperVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcIfOperVnetDn.setStatus("current")
_CfprApVnicIpcIfOperVnetName_Type = SnmpAdminString
_CfprApVnicIpcIfOperVnetName_Object = MibTableColumn
cfprApVnicIpcIfOperVnetName = _CfprApVnicIpcIfOperVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 44, 1, 10),
    _CfprApVnicIpcIfOperVnetName_Type()
)
cfprApVnicIpcIfOperVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcIfOperVnetName.setStatus("current")
_CfprApVnicIpcIfOwner_Type = CfprApVnicConnectionOwner
_CfprApVnicIpcIfOwner_Object = MibTableColumn
cfprApVnicIpcIfOwner = _CfprApVnicIpcIfOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 44, 1, 11),
    _CfprApVnicIpcIfOwner_Type()
)
cfprApVnicIpcIfOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcIfOwner.setStatus("current")
_CfprApVnicIpcIfPubNwId_Type = Gauge32
_CfprApVnicIpcIfPubNwId_Object = MibTableColumn
cfprApVnicIpcIfPubNwId = _CfprApVnicIpcIfPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 44, 1, 12),
    _CfprApVnicIpcIfPubNwId_Type()
)
cfprApVnicIpcIfPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcIfPubNwId.setStatus("current")
_CfprApVnicIpcIfSharing_Type = CfprApFabricVlanSharingType
_CfprApVnicIpcIfSharing_Object = MibTableColumn
cfprApVnicIpcIfSharing = _CfprApVnicIpcIfSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 44, 1, 13),
    _CfprApVnicIpcIfSharing_Type()
)
cfprApVnicIpcIfSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcIfSharing.setStatus("current")
_CfprApVnicIpcIfSwitchId_Type = CfprApVnicL2IfSwitchId
_CfprApVnicIpcIfSwitchId_Object = MibTableColumn
cfprApVnicIpcIfSwitchId = _CfprApVnicIpcIfSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 44, 1, 14),
    _CfprApVnicIpcIfSwitchId_Type()
)
cfprApVnicIpcIfSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcIfSwitchId.setStatus("current")
_CfprApVnicIpcIfType_Type = CfprApVnicAIpcIfType
_CfprApVnicIpcIfType_Object = MibTableColumn
cfprApVnicIpcIfType = _CfprApVnicIpcIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 44, 1, 15),
    _CfprApVnicIpcIfType_Type()
)
cfprApVnicIpcIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcIfType.setStatus("current")
_CfprApVnicIpcIfVnet_Type = Gauge32
_CfprApVnicIpcIfVnet_Object = MibTableColumn
cfprApVnicIpcIfVnet = _CfprApVnicIpcIfVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 44, 1, 16),
    _CfprApVnicIpcIfVnet_Type()
)
cfprApVnicIpcIfVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIpcIfVnet.setStatus("current")
_CfprApVnicIqnHistoryTable_Object = MibTable
cfprApVnicIqnHistoryTable = _CfprApVnicIqnHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 45)
)
if mibBuilder.loadTexts:
    cfprApVnicIqnHistoryTable.setStatus("current")
_CfprApVnicIqnHistoryEntry_Object = MibTableRow
cfprApVnicIqnHistoryEntry = _CfprApVnicIqnHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 45, 1)
)
cfprApVnicIqnHistoryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicIqnHistoryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicIqnHistoryEntry.setStatus("current")
_CfprApVnicIqnHistoryInstanceId_Type = CfprApManagedObjectId
_CfprApVnicIqnHistoryInstanceId_Object = MibTableColumn
cfprApVnicIqnHistoryInstanceId = _CfprApVnicIqnHistoryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 45, 1, 1),
    _CfprApVnicIqnHistoryInstanceId_Type()
)
cfprApVnicIqnHistoryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicIqnHistoryInstanceId.setStatus("current")
_CfprApVnicIqnHistoryDn_Type = CfprApManagedObjectDn
_CfprApVnicIqnHistoryDn_Object = MibTableColumn
cfprApVnicIqnHistoryDn = _CfprApVnicIqnHistoryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 45, 1, 2),
    _CfprApVnicIqnHistoryDn_Type()
)
cfprApVnicIqnHistoryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIqnHistoryDn.setStatus("current")
_CfprApVnicIqnHistoryRn_Type = SnmpAdminString
_CfprApVnicIqnHistoryRn_Object = MibTableColumn
cfprApVnicIqnHistoryRn = _CfprApVnicIqnHistoryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 45, 1, 3),
    _CfprApVnicIqnHistoryRn_Type()
)
cfprApVnicIqnHistoryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIqnHistoryRn.setStatus("current")
_CfprApVnicIqnHistoryOldInitiatorName_Type = SnmpAdminString
_CfprApVnicIqnHistoryOldInitiatorName_Object = MibTableColumn
cfprApVnicIqnHistoryOldInitiatorName = _CfprApVnicIqnHistoryOldInitiatorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 45, 1, 4),
    _CfprApVnicIqnHistoryOldInitiatorName_Type()
)
cfprApVnicIqnHistoryOldInitiatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicIqnHistoryOldInitiatorName.setStatus("current")
_CfprApVnicLanConnPolicyTable_Object = MibTable
cfprApVnicLanConnPolicyTable = _CfprApVnicLanConnPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 46)
)
if mibBuilder.loadTexts:
    cfprApVnicLanConnPolicyTable.setStatus("current")
_CfprApVnicLanConnPolicyEntry_Object = MibTableRow
cfprApVnicLanConnPolicyEntry = _CfprApVnicLanConnPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 46, 1)
)
cfprApVnicLanConnPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicLanConnPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicLanConnPolicyEntry.setStatus("current")
_CfprApVnicLanConnPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApVnicLanConnPolicyInstanceId_Object = MibTableColumn
cfprApVnicLanConnPolicyInstanceId = _CfprApVnicLanConnPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 46, 1, 1),
    _CfprApVnicLanConnPolicyInstanceId_Type()
)
cfprApVnicLanConnPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicLanConnPolicyInstanceId.setStatus("current")
_CfprApVnicLanConnPolicyDn_Type = CfprApManagedObjectDn
_CfprApVnicLanConnPolicyDn_Object = MibTableColumn
cfprApVnicLanConnPolicyDn = _CfprApVnicLanConnPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 46, 1, 2),
    _CfprApVnicLanConnPolicyDn_Type()
)
cfprApVnicLanConnPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLanConnPolicyDn.setStatus("current")
_CfprApVnicLanConnPolicyRn_Type = SnmpAdminString
_CfprApVnicLanConnPolicyRn_Object = MibTableColumn
cfprApVnicLanConnPolicyRn = _CfprApVnicLanConnPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 46, 1, 3),
    _CfprApVnicLanConnPolicyRn_Type()
)
cfprApVnicLanConnPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLanConnPolicyRn.setStatus("current")
_CfprApVnicLanConnPolicyDescr_Type = SnmpAdminString
_CfprApVnicLanConnPolicyDescr_Object = MibTableColumn
cfprApVnicLanConnPolicyDescr = _CfprApVnicLanConnPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 46, 1, 4),
    _CfprApVnicLanConnPolicyDescr_Type()
)
cfprApVnicLanConnPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLanConnPolicyDescr.setStatus("current")
_CfprApVnicLanConnPolicyFltAggr_Type = Unsigned64
_CfprApVnicLanConnPolicyFltAggr_Object = MibTableColumn
cfprApVnicLanConnPolicyFltAggr = _CfprApVnicLanConnPolicyFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 46, 1, 5),
    _CfprApVnicLanConnPolicyFltAggr_Type()
)
cfprApVnicLanConnPolicyFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLanConnPolicyFltAggr.setStatus("current")
_CfprApVnicLanConnPolicyIntId_Type = SnmpAdminString
_CfprApVnicLanConnPolicyIntId_Object = MibTableColumn
cfprApVnicLanConnPolicyIntId = _CfprApVnicLanConnPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 46, 1, 6),
    _CfprApVnicLanConnPolicyIntId_Type()
)
cfprApVnicLanConnPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLanConnPolicyIntId.setStatus("current")
_CfprApVnicLanConnPolicyName_Type = SnmpAdminString
_CfprApVnicLanConnPolicyName_Object = MibTableColumn
cfprApVnicLanConnPolicyName = _CfprApVnicLanConnPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 46, 1, 7),
    _CfprApVnicLanConnPolicyName_Type()
)
cfprApVnicLanConnPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLanConnPolicyName.setStatus("current")
_CfprApVnicLanConnPolicyPolicyLevel_Type = Gauge32
_CfprApVnicLanConnPolicyPolicyLevel_Object = MibTableColumn
cfprApVnicLanConnPolicyPolicyLevel = _CfprApVnicLanConnPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 46, 1, 8),
    _CfprApVnicLanConnPolicyPolicyLevel_Type()
)
cfprApVnicLanConnPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLanConnPolicyPolicyLevel.setStatus("current")
_CfprApVnicLanConnPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApVnicLanConnPolicyPolicyOwner_Object = MibTableColumn
cfprApVnicLanConnPolicyPolicyOwner = _CfprApVnicLanConnPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 46, 1, 9),
    _CfprApVnicLanConnPolicyPolicyOwner_Type()
)
cfprApVnicLanConnPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLanConnPolicyPolicyOwner.setStatus("current")
_CfprApVnicLanConnTemplTable_Object = MibTable
cfprApVnicLanConnTemplTable = _CfprApVnicLanConnTemplTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 47)
)
if mibBuilder.loadTexts:
    cfprApVnicLanConnTemplTable.setStatus("current")
_CfprApVnicLanConnTemplEntry_Object = MibTableRow
cfprApVnicLanConnTemplEntry = _CfprApVnicLanConnTemplEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 47, 1)
)
cfprApVnicLanConnTemplEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicLanConnTemplInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicLanConnTemplEntry.setStatus("current")
_CfprApVnicLanConnTemplInstanceId_Type = CfprApManagedObjectId
_CfprApVnicLanConnTemplInstanceId_Object = MibTableColumn
cfprApVnicLanConnTemplInstanceId = _CfprApVnicLanConnTemplInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 47, 1, 1),
    _CfprApVnicLanConnTemplInstanceId_Type()
)
cfprApVnicLanConnTemplInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicLanConnTemplInstanceId.setStatus("current")
_CfprApVnicLanConnTemplDn_Type = CfprApManagedObjectDn
_CfprApVnicLanConnTemplDn_Object = MibTableColumn
cfprApVnicLanConnTemplDn = _CfprApVnicLanConnTemplDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 47, 1, 2),
    _CfprApVnicLanConnTemplDn_Type()
)
cfprApVnicLanConnTemplDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLanConnTemplDn.setStatus("current")
_CfprApVnicLanConnTemplRn_Type = SnmpAdminString
_CfprApVnicLanConnTemplRn_Object = MibTableColumn
cfprApVnicLanConnTemplRn = _CfprApVnicLanConnTemplRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 47, 1, 3),
    _CfprApVnicLanConnTemplRn_Type()
)
cfprApVnicLanConnTemplRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLanConnTemplRn.setStatus("current")
_CfprApVnicLanConnTemplDescr_Type = SnmpAdminString
_CfprApVnicLanConnTemplDescr_Object = MibTableColumn
cfprApVnicLanConnTemplDescr = _CfprApVnicLanConnTemplDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 47, 1, 4),
    _CfprApVnicLanConnTemplDescr_Type()
)
cfprApVnicLanConnTemplDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLanConnTemplDescr.setStatus("current")
_CfprApVnicLanConnTemplIdentPoolName_Type = SnmpAdminString
_CfprApVnicLanConnTemplIdentPoolName_Object = MibTableColumn
cfprApVnicLanConnTemplIdentPoolName = _CfprApVnicLanConnTemplIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 47, 1, 5),
    _CfprApVnicLanConnTemplIdentPoolName_Type()
)
cfprApVnicLanConnTemplIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLanConnTemplIdentPoolName.setStatus("current")
_CfprApVnicLanConnTemplIntId_Type = SnmpAdminString
_CfprApVnicLanConnTemplIntId_Object = MibTableColumn
cfprApVnicLanConnTemplIntId = _CfprApVnicLanConnTemplIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 47, 1, 6),
    _CfprApVnicLanConnTemplIntId_Type()
)
cfprApVnicLanConnTemplIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLanConnTemplIntId.setStatus("current")
_CfprApVnicLanConnTemplMtu_Type = Gauge32
_CfprApVnicLanConnTemplMtu_Object = MibTableColumn
cfprApVnicLanConnTemplMtu = _CfprApVnicLanConnTemplMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 47, 1, 7),
    _CfprApVnicLanConnTemplMtu_Type()
)
cfprApVnicLanConnTemplMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLanConnTemplMtu.setStatus("current")
_CfprApVnicLanConnTemplName_Type = SnmpAdminString
_CfprApVnicLanConnTemplName_Object = MibTableColumn
cfprApVnicLanConnTemplName = _CfprApVnicLanConnTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 47, 1, 8),
    _CfprApVnicLanConnTemplName_Type()
)
cfprApVnicLanConnTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLanConnTemplName.setStatus("current")
_CfprApVnicLanConnTemplNwCtrlPolicyName_Type = SnmpAdminString
_CfprApVnicLanConnTemplNwCtrlPolicyName_Object = MibTableColumn
cfprApVnicLanConnTemplNwCtrlPolicyName = _CfprApVnicLanConnTemplNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 47, 1, 9),
    _CfprApVnicLanConnTemplNwCtrlPolicyName_Type()
)
cfprApVnicLanConnTemplNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLanConnTemplNwCtrlPolicyName.setStatus("current")
_CfprApVnicLanConnTemplOperIdentPoolName_Type = SnmpAdminString
_CfprApVnicLanConnTemplOperIdentPoolName_Object = MibTableColumn
cfprApVnicLanConnTemplOperIdentPoolName = _CfprApVnicLanConnTemplOperIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 47, 1, 10),
    _CfprApVnicLanConnTemplOperIdentPoolName_Type()
)
cfprApVnicLanConnTemplOperIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLanConnTemplOperIdentPoolName.setStatus("current")
_CfprApVnicLanConnTemplOperNwCtrlPolicyName_Type = SnmpAdminString
_CfprApVnicLanConnTemplOperNwCtrlPolicyName_Object = MibTableColumn
cfprApVnicLanConnTemplOperNwCtrlPolicyName = _CfprApVnicLanConnTemplOperNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 47, 1, 11),
    _CfprApVnicLanConnTemplOperNwCtrlPolicyName_Type()
)
cfprApVnicLanConnTemplOperNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLanConnTemplOperNwCtrlPolicyName.setStatus("current")
_CfprApVnicLanConnTemplOperQosPolicyName_Type = SnmpAdminString
_CfprApVnicLanConnTemplOperQosPolicyName_Object = MibTableColumn
cfprApVnicLanConnTemplOperQosPolicyName = _CfprApVnicLanConnTemplOperQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 47, 1, 12),
    _CfprApVnicLanConnTemplOperQosPolicyName_Type()
)
cfprApVnicLanConnTemplOperQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLanConnTemplOperQosPolicyName.setStatus("current")
_CfprApVnicLanConnTemplOperStatsPolicyName_Type = SnmpAdminString
_CfprApVnicLanConnTemplOperStatsPolicyName_Object = MibTableColumn
cfprApVnicLanConnTemplOperStatsPolicyName = _CfprApVnicLanConnTemplOperStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 47, 1, 13),
    _CfprApVnicLanConnTemplOperStatsPolicyName_Type()
)
cfprApVnicLanConnTemplOperStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLanConnTemplOperStatsPolicyName.setStatus("current")
_CfprApVnicLanConnTemplPinToGroupName_Type = SnmpAdminString
_CfprApVnicLanConnTemplPinToGroupName_Object = MibTableColumn
cfprApVnicLanConnTemplPinToGroupName = _CfprApVnicLanConnTemplPinToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 47, 1, 14),
    _CfprApVnicLanConnTemplPinToGroupName_Type()
)
cfprApVnicLanConnTemplPinToGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLanConnTemplPinToGroupName.setStatus("current")
_CfprApVnicLanConnTemplPolicyLevel_Type = Gauge32
_CfprApVnicLanConnTemplPolicyLevel_Object = MibTableColumn
cfprApVnicLanConnTemplPolicyLevel = _CfprApVnicLanConnTemplPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 47, 1, 15),
    _CfprApVnicLanConnTemplPolicyLevel_Type()
)
cfprApVnicLanConnTemplPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLanConnTemplPolicyLevel.setStatus("current")
_CfprApVnicLanConnTemplPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApVnicLanConnTemplPolicyOwner_Object = MibTableColumn
cfprApVnicLanConnTemplPolicyOwner = _CfprApVnicLanConnTemplPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 47, 1, 16),
    _CfprApVnicLanConnTemplPolicyOwner_Type()
)
cfprApVnicLanConnTemplPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLanConnTemplPolicyOwner.setStatus("current")
_CfprApVnicLanConnTemplQosPolicyName_Type = SnmpAdminString
_CfprApVnicLanConnTemplQosPolicyName_Object = MibTableColumn
cfprApVnicLanConnTemplQosPolicyName = _CfprApVnicLanConnTemplQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 47, 1, 17),
    _CfprApVnicLanConnTemplQosPolicyName_Type()
)
cfprApVnicLanConnTemplQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLanConnTemplQosPolicyName.setStatus("current")
_CfprApVnicLanConnTemplStatsPolicyName_Type = SnmpAdminString
_CfprApVnicLanConnTemplStatsPolicyName_Object = MibTableColumn
cfprApVnicLanConnTemplStatsPolicyName = _CfprApVnicLanConnTemplStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 47, 1, 18),
    _CfprApVnicLanConnTemplStatsPolicyName_Type()
)
cfprApVnicLanConnTemplStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLanConnTemplStatsPolicyName.setStatus("current")
_CfprApVnicLanConnTemplSwitchId_Type = CfprApVnicLanConnTemplSwitchId
_CfprApVnicLanConnTemplSwitchId_Object = MibTableColumn
cfprApVnicLanConnTemplSwitchId = _CfprApVnicLanConnTemplSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 47, 1, 19),
    _CfprApVnicLanConnTemplSwitchId_Type()
)
cfprApVnicLanConnTemplSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLanConnTemplSwitchId.setStatus("current")
_CfprApVnicLanConnTemplTarget_Type = CfprApVnicTemplateTarget
_CfprApVnicLanConnTemplTarget_Object = MibTableColumn
cfprApVnicLanConnTemplTarget = _CfprApVnicLanConnTemplTarget_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 47, 1, 20),
    _CfprApVnicLanConnTemplTarget_Type()
)
cfprApVnicLanConnTemplTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLanConnTemplTarget.setStatus("current")
_CfprApVnicLanConnTemplTemplType_Type = CfprApVnicTemplateType
_CfprApVnicLanConnTemplTemplType_Object = MibTableColumn
cfprApVnicLanConnTemplTemplType = _CfprApVnicLanConnTemplTemplType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 47, 1, 21),
    _CfprApVnicLanConnTemplTemplType_Type()
)
cfprApVnicLanConnTemplTemplType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLanConnTemplTemplType.setStatus("current")
_CfprApVnicLifVlanTable_Object = MibTable
cfprApVnicLifVlanTable = _CfprApVnicLifVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 48)
)
if mibBuilder.loadTexts:
    cfprApVnicLifVlanTable.setStatus("current")
_CfprApVnicLifVlanEntry_Object = MibTableRow
cfprApVnicLifVlanEntry = _CfprApVnicLifVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 48, 1)
)
cfprApVnicLifVlanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicLifVlanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicLifVlanEntry.setStatus("current")
_CfprApVnicLifVlanInstanceId_Type = CfprApManagedObjectId
_CfprApVnicLifVlanInstanceId_Object = MibTableColumn
cfprApVnicLifVlanInstanceId = _CfprApVnicLifVlanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 48, 1, 1),
    _CfprApVnicLifVlanInstanceId_Type()
)
cfprApVnicLifVlanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicLifVlanInstanceId.setStatus("current")
_CfprApVnicLifVlanDn_Type = CfprApManagedObjectDn
_CfprApVnicLifVlanDn_Object = MibTableColumn
cfprApVnicLifVlanDn = _CfprApVnicLifVlanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 48, 1, 2),
    _CfprApVnicLifVlanDn_Type()
)
cfprApVnicLifVlanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLifVlanDn.setStatus("current")
_CfprApVnicLifVlanRn_Type = SnmpAdminString
_CfprApVnicLifVlanRn_Object = MibTableColumn
cfprApVnicLifVlanRn = _CfprApVnicLifVlanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 48, 1, 3),
    _CfprApVnicLifVlanRn_Type()
)
cfprApVnicLifVlanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLifVlanRn.setStatus("current")
_CfprApVnicLifVlanAddr_Type = MacAddress
_CfprApVnicLifVlanAddr_Object = MibTableColumn
cfprApVnicLifVlanAddr = _CfprApVnicLifVlanAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 48, 1, 4),
    _CfprApVnicLifVlanAddr_Type()
)
cfprApVnicLifVlanAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLifVlanAddr.setStatus("current")
_CfprApVnicLifVlanConfigQualifier_Type = CfprApVnicConfigIssues
_CfprApVnicLifVlanConfigQualifier_Object = MibTableColumn
cfprApVnicLifVlanConfigQualifier = _CfprApVnicLifVlanConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 48, 1, 5),
    _CfprApVnicLifVlanConfigQualifier_Type()
)
cfprApVnicLifVlanConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLifVlanConfigQualifier.setStatus("current")
_CfprApVnicLifVlanDefaultNet_Type = TruthValue
_CfprApVnicLifVlanDefaultNet_Object = MibTableColumn
cfprApVnicLifVlanDefaultNet = _CfprApVnicLifVlanDefaultNet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 48, 1, 6),
    _CfprApVnicLifVlanDefaultNet_Type()
)
cfprApVnicLifVlanDefaultNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLifVlanDefaultNet.setStatus("current")
_CfprApVnicLifVlanName_Type = SnmpAdminString
_CfprApVnicLifVlanName_Object = MibTableColumn
cfprApVnicLifVlanName = _CfprApVnicLifVlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 48, 1, 7),
    _CfprApVnicLifVlanName_Type()
)
cfprApVnicLifVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLifVlanName.setStatus("current")
_CfprApVnicLifVlanOperState_Type = CfprApVnicIfOperState
_CfprApVnicLifVlanOperState_Object = MibTableColumn
cfprApVnicLifVlanOperState = _CfprApVnicLifVlanOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 48, 1, 8),
    _CfprApVnicLifVlanOperState_Type()
)
cfprApVnicLifVlanOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLifVlanOperState.setStatus("current")
_CfprApVnicLifVlanOperVnetDn_Type = SnmpAdminString
_CfprApVnicLifVlanOperVnetDn_Object = MibTableColumn
cfprApVnicLifVlanOperVnetDn = _CfprApVnicLifVlanOperVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 48, 1, 9),
    _CfprApVnicLifVlanOperVnetDn_Type()
)
cfprApVnicLifVlanOperVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLifVlanOperVnetDn.setStatus("current")
_CfprApVnicLifVlanOperVnetName_Type = SnmpAdminString
_CfprApVnicLifVlanOperVnetName_Object = MibTableColumn
cfprApVnicLifVlanOperVnetName = _CfprApVnicLifVlanOperVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 48, 1, 10),
    _CfprApVnicLifVlanOperVnetName_Type()
)
cfprApVnicLifVlanOperVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLifVlanOperVnetName.setStatus("current")
_CfprApVnicLifVlanOwner_Type = CfprApVnicConnectionOwner
_CfprApVnicLifVlanOwner_Object = MibTableColumn
cfprApVnicLifVlanOwner = _CfprApVnicLifVlanOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 48, 1, 11),
    _CfprApVnicLifVlanOwner_Type()
)
cfprApVnicLifVlanOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLifVlanOwner.setStatus("current")
_CfprApVnicLifVlanPubNwId_Type = Gauge32
_CfprApVnicLifVlanPubNwId_Object = MibTableColumn
cfprApVnicLifVlanPubNwId = _CfprApVnicLifVlanPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 48, 1, 12),
    _CfprApVnicLifVlanPubNwId_Type()
)
cfprApVnicLifVlanPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLifVlanPubNwId.setStatus("current")
_CfprApVnicLifVlanSharing_Type = CfprApFabricVlanSharingType
_CfprApVnicLifVlanSharing_Object = MibTableColumn
cfprApVnicLifVlanSharing = _CfprApVnicLifVlanSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 48, 1, 13),
    _CfprApVnicLifVlanSharing_Type()
)
cfprApVnicLifVlanSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLifVlanSharing.setStatus("current")
_CfprApVnicLifVlanSwitchId_Type = CfprApVnicL2IfSwitchId
_CfprApVnicLifVlanSwitchId_Object = MibTableColumn
cfprApVnicLifVlanSwitchId = _CfprApVnicLifVlanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 48, 1, 14),
    _CfprApVnicLifVlanSwitchId_Type()
)
cfprApVnicLifVlanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLifVlanSwitchId.setStatus("current")
_CfprApVnicLifVlanType_Type = CfprApVnicAEtherIfType
_CfprApVnicLifVlanType_Object = MibTableColumn
cfprApVnicLifVlanType = _CfprApVnicLifVlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 48, 1, 15),
    _CfprApVnicLifVlanType_Type()
)
cfprApVnicLifVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLifVlanType.setStatus("current")
_CfprApVnicLifVlanVnet_Type = Gauge32
_CfprApVnicLifVlanVnet_Object = MibTableColumn
cfprApVnicLifVlanVnet = _CfprApVnicLifVlanVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 48, 1, 16),
    _CfprApVnicLifVlanVnet_Type()
)
cfprApVnicLifVlanVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLifVlanVnet.setStatus("current")
_CfprApVnicLifVsanTable_Object = MibTable
cfprApVnicLifVsanTable = _CfprApVnicLifVsanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 49)
)
if mibBuilder.loadTexts:
    cfprApVnicLifVsanTable.setStatus("current")
_CfprApVnicLifVsanEntry_Object = MibTableRow
cfprApVnicLifVsanEntry = _CfprApVnicLifVsanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 49, 1)
)
cfprApVnicLifVsanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicLifVsanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicLifVsanEntry.setStatus("current")
_CfprApVnicLifVsanInstanceId_Type = CfprApManagedObjectId
_CfprApVnicLifVsanInstanceId_Object = MibTableColumn
cfprApVnicLifVsanInstanceId = _CfprApVnicLifVsanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 49, 1, 1),
    _CfprApVnicLifVsanInstanceId_Type()
)
cfprApVnicLifVsanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicLifVsanInstanceId.setStatus("current")
_CfprApVnicLifVsanDn_Type = CfprApManagedObjectDn
_CfprApVnicLifVsanDn_Object = MibTableColumn
cfprApVnicLifVsanDn = _CfprApVnicLifVsanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 49, 1, 2),
    _CfprApVnicLifVsanDn_Type()
)
cfprApVnicLifVsanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLifVsanDn.setStatus("current")
_CfprApVnicLifVsanRn_Type = SnmpAdminString
_CfprApVnicLifVsanRn_Object = MibTableColumn
cfprApVnicLifVsanRn = _CfprApVnicLifVsanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 49, 1, 3),
    _CfprApVnicLifVsanRn_Type()
)
cfprApVnicLifVsanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLifVsanRn.setStatus("current")
_CfprApVnicLifVsanConfigQualifier_Type = CfprApVnicConfigIssues
_CfprApVnicLifVsanConfigQualifier_Object = MibTableColumn
cfprApVnicLifVsanConfigQualifier = _CfprApVnicLifVsanConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 49, 1, 4),
    _CfprApVnicLifVsanConfigQualifier_Type()
)
cfprApVnicLifVsanConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLifVsanConfigQualifier.setStatus("current")
_CfprApVnicLifVsanInitiator_Type = Unsigned64
_CfprApVnicLifVsanInitiator_Object = MibTableColumn
cfprApVnicLifVsanInitiator = _CfprApVnicLifVsanInitiator_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 49, 1, 5),
    _CfprApVnicLifVsanInitiator_Type()
)
cfprApVnicLifVsanInitiator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLifVsanInitiator.setStatus("current")
_CfprApVnicLifVsanName_Type = SnmpAdminString
_CfprApVnicLifVsanName_Object = MibTableColumn
cfprApVnicLifVsanName = _CfprApVnicLifVsanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 49, 1, 6),
    _CfprApVnicLifVsanName_Type()
)
cfprApVnicLifVsanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLifVsanName.setStatus("current")
_CfprApVnicLifVsanOperState_Type = CfprApVnicIfOperState
_CfprApVnicLifVsanOperState_Object = MibTableColumn
cfprApVnicLifVsanOperState = _CfprApVnicLifVsanOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 49, 1, 7),
    _CfprApVnicLifVsanOperState_Type()
)
cfprApVnicLifVsanOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLifVsanOperState.setStatus("current")
_CfprApVnicLifVsanOperVnetDn_Type = SnmpAdminString
_CfprApVnicLifVsanOperVnetDn_Object = MibTableColumn
cfprApVnicLifVsanOperVnetDn = _CfprApVnicLifVsanOperVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 49, 1, 8),
    _CfprApVnicLifVsanOperVnetDn_Type()
)
cfprApVnicLifVsanOperVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLifVsanOperVnetDn.setStatus("current")
_CfprApVnicLifVsanOperVnetName_Type = SnmpAdminString
_CfprApVnicLifVsanOperVnetName_Object = MibTableColumn
cfprApVnicLifVsanOperVnetName = _CfprApVnicLifVsanOperVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 49, 1, 9),
    _CfprApVnicLifVsanOperVnetName_Type()
)
cfprApVnicLifVsanOperVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLifVsanOperVnetName.setStatus("current")
_CfprApVnicLifVsanOwner_Type = CfprApVnicConnectionOwner
_CfprApVnicLifVsanOwner_Object = MibTableColumn
cfprApVnicLifVsanOwner = _CfprApVnicLifVsanOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 49, 1, 10),
    _CfprApVnicLifVsanOwner_Type()
)
cfprApVnicLifVsanOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLifVsanOwner.setStatus("current")
_CfprApVnicLifVsanPubNwId_Type = Gauge32
_CfprApVnicLifVsanPubNwId_Object = MibTableColumn
cfprApVnicLifVsanPubNwId = _CfprApVnicLifVsanPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 49, 1, 11),
    _CfprApVnicLifVsanPubNwId_Type()
)
cfprApVnicLifVsanPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLifVsanPubNwId.setStatus("current")
_CfprApVnicLifVsanSharing_Type = CfprApFabricVlanSharingType
_CfprApVnicLifVsanSharing_Object = MibTableColumn
cfprApVnicLifVsanSharing = _CfprApVnicLifVsanSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 49, 1, 12),
    _CfprApVnicLifVsanSharing_Type()
)
cfprApVnicLifVsanSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLifVsanSharing.setStatus("current")
_CfprApVnicLifVsanSwitchId_Type = CfprApVnicL2IfSwitchId
_CfprApVnicLifVsanSwitchId_Object = MibTableColumn
cfprApVnicLifVsanSwitchId = _CfprApVnicLifVsanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 49, 1, 13),
    _CfprApVnicLifVsanSwitchId_Type()
)
cfprApVnicLifVsanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLifVsanSwitchId.setStatus("current")
_CfprApVnicLifVsanType_Type = CfprApVnicAFcIfType
_CfprApVnicLifVsanType_Object = MibTableColumn
cfprApVnicLifVsanType = _CfprApVnicLifVsanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 49, 1, 14),
    _CfprApVnicLifVsanType_Type()
)
cfprApVnicLifVsanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLifVsanType.setStatus("current")
_CfprApVnicLifVsanVnet_Type = Gauge32
_CfprApVnicLifVsanVnet_Object = MibTableColumn
cfprApVnicLifVsanVnet = _CfprApVnicLifVsanVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 49, 1, 15),
    _CfprApVnicLifVsanVnet_Type()
)
cfprApVnicLifVsanVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLifVsanVnet.setStatus("current")
_CfprApVnicLunTable_Object = MibTable
cfprApVnicLunTable = _CfprApVnicLunTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 50)
)
if mibBuilder.loadTexts:
    cfprApVnicLunTable.setStatus("current")
_CfprApVnicLunEntry_Object = MibTableRow
cfprApVnicLunEntry = _CfprApVnicLunEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 50, 1)
)
cfprApVnicLunEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicLunInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicLunEntry.setStatus("current")
_CfprApVnicLunInstanceId_Type = CfprApManagedObjectId
_CfprApVnicLunInstanceId_Object = MibTableColumn
cfprApVnicLunInstanceId = _CfprApVnicLunInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 50, 1, 1),
    _CfprApVnicLunInstanceId_Type()
)
cfprApVnicLunInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicLunInstanceId.setStatus("current")
_CfprApVnicLunDn_Type = CfprApManagedObjectDn
_CfprApVnicLunDn_Object = MibTableColumn
cfprApVnicLunDn = _CfprApVnicLunDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 50, 1, 2),
    _CfprApVnicLunDn_Type()
)
cfprApVnicLunDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLunDn.setStatus("current")
_CfprApVnicLunRn_Type = SnmpAdminString
_CfprApVnicLunRn_Object = MibTableColumn
cfprApVnicLunRn = _CfprApVnicLunRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 50, 1, 3),
    _CfprApVnicLunRn_Type()
)
cfprApVnicLunRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLunRn.setStatus("current")
_CfprApVnicLunBootable_Type = TruthValue
_CfprApVnicLunBootable_Object = MibTableColumn
cfprApVnicLunBootable = _CfprApVnicLunBootable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 50, 1, 4),
    _CfprApVnicLunBootable_Type()
)
cfprApVnicLunBootable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLunBootable.setStatus("current")
_CfprApVnicLunId_Type = CfprApVnicLunId
_CfprApVnicLunId_Object = MibTableColumn
cfprApVnicLunId = _CfprApVnicLunId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 50, 1, 5),
    _CfprApVnicLunId_Type()
)
cfprApVnicLunId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicLunId.setStatus("current")
_CfprApVnicMacHistoryTable_Object = MibTable
cfprApVnicMacHistoryTable = _CfprApVnicMacHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 51)
)
if mibBuilder.loadTexts:
    cfprApVnicMacHistoryTable.setStatus("current")
_CfprApVnicMacHistoryEntry_Object = MibTableRow
cfprApVnicMacHistoryEntry = _CfprApVnicMacHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 51, 1)
)
cfprApVnicMacHistoryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicMacHistoryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicMacHistoryEntry.setStatus("current")
_CfprApVnicMacHistoryInstanceId_Type = CfprApManagedObjectId
_CfprApVnicMacHistoryInstanceId_Object = MibTableColumn
cfprApVnicMacHistoryInstanceId = _CfprApVnicMacHistoryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 51, 1, 1),
    _CfprApVnicMacHistoryInstanceId_Type()
)
cfprApVnicMacHistoryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicMacHistoryInstanceId.setStatus("current")
_CfprApVnicMacHistoryDn_Type = CfprApManagedObjectDn
_CfprApVnicMacHistoryDn_Object = MibTableColumn
cfprApVnicMacHistoryDn = _CfprApVnicMacHistoryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 51, 1, 2),
    _CfprApVnicMacHistoryDn_Type()
)
cfprApVnicMacHistoryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicMacHistoryDn.setStatus("current")
_CfprApVnicMacHistoryRn_Type = SnmpAdminString
_CfprApVnicMacHistoryRn_Object = MibTableColumn
cfprApVnicMacHistoryRn = _CfprApVnicMacHistoryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 51, 1, 3),
    _CfprApVnicMacHistoryRn_Type()
)
cfprApVnicMacHistoryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicMacHistoryRn.setStatus("current")
_CfprApVnicMacHistoryOldaddr_Type = MacAddress
_CfprApVnicMacHistoryOldaddr_Object = MibTableColumn
cfprApVnicMacHistoryOldaddr = _CfprApVnicMacHistoryOldaddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 51, 1, 4),
    _CfprApVnicMacHistoryOldaddr_Type()
)
cfprApVnicMacHistoryOldaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicMacHistoryOldaddr.setStatus("current")
_CfprApVnicOProfileAliasTable_Object = MibTable
cfprApVnicOProfileAliasTable = _CfprApVnicOProfileAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 52)
)
if mibBuilder.loadTexts:
    cfprApVnicOProfileAliasTable.setStatus("current")
_CfprApVnicOProfileAliasEntry_Object = MibTableRow
cfprApVnicOProfileAliasEntry = _CfprApVnicOProfileAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 52, 1)
)
cfprApVnicOProfileAliasEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicOProfileAliasInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicOProfileAliasEntry.setStatus("current")
_CfprApVnicOProfileAliasInstanceId_Type = CfprApManagedObjectId
_CfprApVnicOProfileAliasInstanceId_Object = MibTableColumn
cfprApVnicOProfileAliasInstanceId = _CfprApVnicOProfileAliasInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 52, 1, 1),
    _CfprApVnicOProfileAliasInstanceId_Type()
)
cfprApVnicOProfileAliasInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicOProfileAliasInstanceId.setStatus("current")
_CfprApVnicOProfileAliasDn_Type = CfprApManagedObjectDn
_CfprApVnicOProfileAliasDn_Object = MibTableColumn
cfprApVnicOProfileAliasDn = _CfprApVnicOProfileAliasDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 52, 1, 2),
    _CfprApVnicOProfileAliasDn_Type()
)
cfprApVnicOProfileAliasDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicOProfileAliasDn.setStatus("current")
_CfprApVnicOProfileAliasRn_Type = SnmpAdminString
_CfprApVnicOProfileAliasRn_Object = MibTableColumn
cfprApVnicOProfileAliasRn = _CfprApVnicOProfileAliasRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 52, 1, 3),
    _CfprApVnicOProfileAliasRn_Type()
)
cfprApVnicOProfileAliasRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicOProfileAliasRn.setStatus("current")
_CfprApVnicOProfileAliasAlias_Type = SnmpAdminString
_CfprApVnicOProfileAliasAlias_Object = MibTableColumn
cfprApVnicOProfileAliasAlias = _CfprApVnicOProfileAliasAlias_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 52, 1, 4),
    _CfprApVnicOProfileAliasAlias_Type()
)
cfprApVnicOProfileAliasAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicOProfileAliasAlias.setStatus("current")
_CfprApVnicOProfileAliasMgmtPlane_Type = CfprApVmMgmtPlane
_CfprApVnicOProfileAliasMgmtPlane_Object = MibTableColumn
cfprApVnicOProfileAliasMgmtPlane = _CfprApVnicOProfileAliasMgmtPlane_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 52, 1, 5),
    _CfprApVnicOProfileAliasMgmtPlane_Type()
)
cfprApVnicOProfileAliasMgmtPlane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicOProfileAliasMgmtPlane.setStatus("current")
_CfprApVnicOProfileAliasVSwitchId_Type = SnmpAdminString
_CfprApVnicOProfileAliasVSwitchId_Object = MibTableColumn
cfprApVnicOProfileAliasVSwitchId = _CfprApVnicOProfileAliasVSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 52, 1, 6),
    _CfprApVnicOProfileAliasVSwitchId_Type()
)
cfprApVnicOProfileAliasVSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicOProfileAliasVSwitchId.setStatus("current")
_CfprApVnicOProfileAliasVSwitchName_Type = SnmpAdminString
_CfprApVnicOProfileAliasVSwitchName_Object = MibTableColumn
cfprApVnicOProfileAliasVSwitchName = _CfprApVnicOProfileAliasVSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 52, 1, 7),
    _CfprApVnicOProfileAliasVSwitchName_Type()
)
cfprApVnicOProfileAliasVSwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicOProfileAliasVSwitchName.setStatus("current")
_CfprApVnicProfileTable_Object = MibTable
cfprApVnicProfileTable = _CfprApVnicProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 53)
)
if mibBuilder.loadTexts:
    cfprApVnicProfileTable.setStatus("current")
_CfprApVnicProfileEntry_Object = MibTableRow
cfprApVnicProfileEntry = _CfprApVnicProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 53, 1)
)
cfprApVnicProfileEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicProfileInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicProfileEntry.setStatus("current")
_CfprApVnicProfileInstanceId_Type = CfprApManagedObjectId
_CfprApVnicProfileInstanceId_Object = MibTableColumn
cfprApVnicProfileInstanceId = _CfprApVnicProfileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 53, 1, 1),
    _CfprApVnicProfileInstanceId_Type()
)
cfprApVnicProfileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicProfileInstanceId.setStatus("current")
_CfprApVnicProfileDn_Type = CfprApManagedObjectDn
_CfprApVnicProfileDn_Object = MibTableColumn
cfprApVnicProfileDn = _CfprApVnicProfileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 53, 1, 2),
    _CfprApVnicProfileDn_Type()
)
cfprApVnicProfileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileDn.setStatus("current")
_CfprApVnicProfileRn_Type = SnmpAdminString
_CfprApVnicProfileRn_Object = MibTableColumn
cfprApVnicProfileRn = _CfprApVnicProfileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 53, 1, 3),
    _CfprApVnicProfileRn_Type()
)
cfprApVnicProfileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileRn.setStatus("current")
_CfprApVnicProfileCdp_Type = CfprApNwctrlAdminState
_CfprApVnicProfileCdp_Object = MibTableColumn
cfprApVnicProfileCdp = _CfprApVnicProfileCdp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 53, 1, 4),
    _CfprApVnicProfileCdp_Type()
)
cfprApVnicProfileCdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileCdp.setStatus("current")
_CfprApVnicProfileConfigQualifier_Type = CfprApVnicProfileConfigQualifier
_CfprApVnicProfileConfigQualifier_Object = MibTableColumn
cfprApVnicProfileConfigQualifier = _CfprApVnicProfileConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 53, 1, 5),
    _CfprApVnicProfileConfigQualifier_Type()
)
cfprApVnicProfileConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileConfigQualifier.setStatus("current")
_CfprApVnicProfileCos_Type = Gauge32
_CfprApVnicProfileCos_Object = MibTableColumn
cfprApVnicProfileCos = _CfprApVnicProfileCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 53, 1, 6),
    _CfprApVnicProfileCos_Type()
)
cfprApVnicProfileCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileCos.setStatus("current")
_CfprApVnicProfileDescr_Type = SnmpAdminString
_CfprApVnicProfileDescr_Object = MibTableColumn
cfprApVnicProfileDescr = _CfprApVnicProfileDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 53, 1, 7),
    _CfprApVnicProfileDescr_Type()
)
cfprApVnicProfileDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileDescr.setStatus("current")
_CfprApVnicProfileForgeMac_Type = CfprApDpsecForgedTransmit
_CfprApVnicProfileForgeMac_Object = MibTableColumn
cfprApVnicProfileForgeMac = _CfprApVnicProfileForgeMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 53, 1, 8),
    _CfprApVnicProfileForgeMac_Type()
)
cfprApVnicProfileForgeMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileForgeMac.setStatus("current")
_CfprApVnicProfileHostNwIOPerf_Type = CfprApVnicHostNwIOPerfPref
_CfprApVnicProfileHostNwIOPerf_Object = MibTableColumn
cfprApVnicProfileHostNwIOPerf = _CfprApVnicProfileHostNwIOPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 53, 1, 9),
    _CfprApVnicProfileHostNwIOPerf_Type()
)
cfprApVnicProfileHostNwIOPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileHostNwIOPerf.setStatus("current")
_CfprApVnicProfileIntId_Type = SnmpAdminString
_CfprApVnicProfileIntId_Object = MibTableColumn
cfprApVnicProfileIntId = _CfprApVnicProfileIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 53, 1, 10),
    _CfprApVnicProfileIntId_Type()
)
cfprApVnicProfileIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileIntId.setStatus("current")
_CfprApVnicProfileMacRegisterMode_Type = CfprApNwctrlRegistrationMode
_CfprApVnicProfileMacRegisterMode_Object = MibTableColumn
cfprApVnicProfileMacRegisterMode = _CfprApVnicProfileMacRegisterMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 53, 1, 11),
    _CfprApVnicProfileMacRegisterMode_Type()
)
cfprApVnicProfileMacRegisterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileMacRegisterMode.setStatus("current")
_CfprApVnicProfileMaxPorts_Type = Gauge32
_CfprApVnicProfileMaxPorts_Object = MibTableColumn
cfprApVnicProfileMaxPorts = _CfprApVnicProfileMaxPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 53, 1, 12),
    _CfprApVnicProfileMaxPorts_Type()
)
cfprApVnicProfileMaxPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileMaxPorts.setStatus("current")
_CfprApVnicProfileName_Type = SnmpAdminString
_CfprApVnicProfileName_Object = MibTableColumn
cfprApVnicProfileName = _CfprApVnicProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 53, 1, 13),
    _CfprApVnicProfileName_Type()
)
cfprApVnicProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileName.setStatus("current")
_CfprApVnicProfileNwCtrlPolicyName_Type = SnmpAdminString
_CfprApVnicProfileNwCtrlPolicyName_Object = MibTableColumn
cfprApVnicProfileNwCtrlPolicyName = _CfprApVnicProfileNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 53, 1, 14),
    _CfprApVnicProfileNwCtrlPolicyName_Type()
)
cfprApVnicProfileNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileNwCtrlPolicyName.setStatus("current")
_CfprApVnicProfileOperNwCtrlPolicyName_Type = SnmpAdminString
_CfprApVnicProfileOperNwCtrlPolicyName_Object = MibTableColumn
cfprApVnicProfileOperNwCtrlPolicyName = _CfprApVnicProfileOperNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 53, 1, 15),
    _CfprApVnicProfileOperNwCtrlPolicyName_Type()
)
cfprApVnicProfileOperNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileOperNwCtrlPolicyName.setStatus("current")
_CfprApVnicProfileOperQosPolicyName_Type = SnmpAdminString
_CfprApVnicProfileOperQosPolicyName_Object = MibTableColumn
cfprApVnicProfileOperQosPolicyName = _CfprApVnicProfileOperQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 53, 1, 16),
    _CfprApVnicProfileOperQosPolicyName_Type()
)
cfprApVnicProfileOperQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileOperQosPolicyName.setStatus("current")
_CfprApVnicProfilePinToGroupName_Type = SnmpAdminString
_CfprApVnicProfilePinToGroupName_Object = MibTableColumn
cfprApVnicProfilePinToGroupName = _CfprApVnicProfilePinToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 53, 1, 17),
    _CfprApVnicProfilePinToGroupName_Type()
)
cfprApVnicProfilePinToGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfilePinToGroupName.setStatus("current")
_CfprApVnicProfilePolicyLevel_Type = Gauge32
_CfprApVnicProfilePolicyLevel_Object = MibTableColumn
cfprApVnicProfilePolicyLevel = _CfprApVnicProfilePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 53, 1, 18),
    _CfprApVnicProfilePolicyLevel_Type()
)
cfprApVnicProfilePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfilePolicyLevel.setStatus("current")
_CfprApVnicProfilePolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApVnicProfilePolicyOwner_Object = MibTableColumn
cfprApVnicProfilePolicyOwner = _CfprApVnicProfilePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 53, 1, 19),
    _CfprApVnicProfilePolicyOwner_Type()
)
cfprApVnicProfilePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfilePolicyOwner.setStatus("current")
_CfprApVnicProfilePortProfileUuid_Type = SnmpAdminString
_CfprApVnicProfilePortProfileUuid_Object = MibTableColumn
cfprApVnicProfilePortProfileUuid = _CfprApVnicProfilePortProfileUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 53, 1, 20),
    _CfprApVnicProfilePortProfileUuid_Type()
)
cfprApVnicProfilePortProfileUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfilePortProfileUuid.setStatus("current")
_CfprApVnicProfilePrimaryVlanId_Type = Gauge32
_CfprApVnicProfilePrimaryVlanId_Object = MibTableColumn
cfprApVnicProfilePrimaryVlanId = _CfprApVnicProfilePrimaryVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 53, 1, 21),
    _CfprApVnicProfilePrimaryVlanId_Type()
)
cfprApVnicProfilePrimaryVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfilePrimaryVlanId.setStatus("current")
_CfprApVnicProfileQosPolicyDn_Type = SnmpAdminString
_CfprApVnicProfileQosPolicyDn_Object = MibTableColumn
cfprApVnicProfileQosPolicyDn = _CfprApVnicProfileQosPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 53, 1, 22),
    _CfprApVnicProfileQosPolicyDn_Type()
)
cfprApVnicProfileQosPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileQosPolicyDn.setStatus("current")
_CfprApVnicProfileQosPolicyId_Type = SnmpAdminString
_CfprApVnicProfileQosPolicyId_Object = MibTableColumn
cfprApVnicProfileQosPolicyId = _CfprApVnicProfileQosPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 53, 1, 23),
    _CfprApVnicProfileQosPolicyId_Type()
)
cfprApVnicProfileQosPolicyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileQosPolicyId.setStatus("current")
_CfprApVnicProfileQosPolicyName_Type = SnmpAdminString
_CfprApVnicProfileQosPolicyName_Object = MibTableColumn
cfprApVnicProfileQosPolicyName = _CfprApVnicProfileQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 53, 1, 24),
    _CfprApVnicProfileQosPolicyName_Type()
)
cfprApVnicProfileQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileQosPolicyName.setStatus("current")
_CfprApVnicProfileSwABorderAggrPort_Type = Gauge32
_CfprApVnicProfileSwABorderAggrPort_Object = MibTableColumn
cfprApVnicProfileSwABorderAggrPort = _CfprApVnicProfileSwABorderAggrPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 53, 1, 25),
    _CfprApVnicProfileSwABorderAggrPort_Type()
)
cfprApVnicProfileSwABorderAggrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileSwABorderAggrPort.setStatus("current")
_CfprApVnicProfileSwABorderPort_Type = Gauge32
_CfprApVnicProfileSwABorderPort_Object = MibTableColumn
cfprApVnicProfileSwABorderPort = _CfprApVnicProfileSwABorderPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 53, 1, 26),
    _CfprApVnicProfileSwABorderPort_Type()
)
cfprApVnicProfileSwABorderPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileSwABorderPort.setStatus("current")
_CfprApVnicProfileSwABorderSlot_Type = Gauge32
_CfprApVnicProfileSwABorderSlot_Object = MibTableColumn
cfprApVnicProfileSwABorderSlot = _CfprApVnicProfileSwABorderSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 53, 1, 27),
    _CfprApVnicProfileSwABorderSlot_Type()
)
cfprApVnicProfileSwABorderSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileSwABorderSlot.setStatus("current")
_CfprApVnicProfileSwBBorderAggrPort_Type = Gauge32
_CfprApVnicProfileSwBBorderAggrPort_Object = MibTableColumn
cfprApVnicProfileSwBBorderAggrPort = _CfprApVnicProfileSwBBorderAggrPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 53, 1, 28),
    _CfprApVnicProfileSwBBorderAggrPort_Type()
)
cfprApVnicProfileSwBBorderAggrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileSwBBorderAggrPort.setStatus("current")
_CfprApVnicProfileSwBBorderPort_Type = Gauge32
_CfprApVnicProfileSwBBorderPort_Object = MibTableColumn
cfprApVnicProfileSwBBorderPort = _CfprApVnicProfileSwBBorderPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 53, 1, 29),
    _CfprApVnicProfileSwBBorderPort_Type()
)
cfprApVnicProfileSwBBorderPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileSwBBorderPort.setStatus("current")
_CfprApVnicProfileSwBBorderSlot_Type = Gauge32
_CfprApVnicProfileSwBBorderSlot_Object = MibTableColumn
cfprApVnicProfileSwBBorderSlot = _CfprApVnicProfileSwBBorderSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 53, 1, 30),
    _CfprApVnicProfileSwBBorderSlot_Type()
)
cfprApVnicProfileSwBBorderSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileSwBBorderSlot.setStatus("current")
_CfprApVnicProfileType_Type = CfprApVnicPortProfileType
_CfprApVnicProfileType_Object = MibTableColumn
cfprApVnicProfileType = _CfprApVnicProfileType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 53, 1, 31),
    _CfprApVnicProfileType_Type()
)
cfprApVnicProfileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileType.setStatus("current")
_CfprApVnicProfileUplinkFailAction_Type = CfprApNwctrlLinkFailAction
_CfprApVnicProfileUplinkFailAction_Object = MibTableColumn
cfprApVnicProfileUplinkFailAction = _CfprApVnicProfileUplinkFailAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 53, 1, 32),
    _CfprApVnicProfileUplinkFailAction_Type()
)
cfprApVnicProfileUplinkFailAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileUplinkFailAction.setStatus("current")
_CfprApVnicProfileAliasTable_Object = MibTable
cfprApVnicProfileAliasTable = _CfprApVnicProfileAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 54)
)
if mibBuilder.loadTexts:
    cfprApVnicProfileAliasTable.setStatus("current")
_CfprApVnicProfileAliasEntry_Object = MibTableRow
cfprApVnicProfileAliasEntry = _CfprApVnicProfileAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 54, 1)
)
cfprApVnicProfileAliasEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicProfileAliasInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicProfileAliasEntry.setStatus("current")
_CfprApVnicProfileAliasInstanceId_Type = CfprApManagedObjectId
_CfprApVnicProfileAliasInstanceId_Object = MibTableColumn
cfprApVnicProfileAliasInstanceId = _CfprApVnicProfileAliasInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 54, 1, 1),
    _CfprApVnicProfileAliasInstanceId_Type()
)
cfprApVnicProfileAliasInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicProfileAliasInstanceId.setStatus("current")
_CfprApVnicProfileAliasDn_Type = CfprApManagedObjectDn
_CfprApVnicProfileAliasDn_Object = MibTableColumn
cfprApVnicProfileAliasDn = _CfprApVnicProfileAliasDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 54, 1, 2),
    _CfprApVnicProfileAliasDn_Type()
)
cfprApVnicProfileAliasDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileAliasDn.setStatus("current")
_CfprApVnicProfileAliasRn_Type = SnmpAdminString
_CfprApVnicProfileAliasRn_Object = MibTableColumn
cfprApVnicProfileAliasRn = _CfprApVnicProfileAliasRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 54, 1, 3),
    _CfprApVnicProfileAliasRn_Type()
)
cfprApVnicProfileAliasRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileAliasRn.setStatus("current")
_CfprApVnicProfileAliasAlias_Type = SnmpAdminString
_CfprApVnicProfileAliasAlias_Object = MibTableColumn
cfprApVnicProfileAliasAlias = _CfprApVnicProfileAliasAlias_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 54, 1, 4),
    _CfprApVnicProfileAliasAlias_Type()
)
cfprApVnicProfileAliasAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileAliasAlias.setStatus("current")
_CfprApVnicProfileAliasSwUuid_Type = SnmpAdminString
_CfprApVnicProfileAliasSwUuid_Object = MibTableColumn
cfprApVnicProfileAliasSwUuid = _CfprApVnicProfileAliasSwUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 54, 1, 5),
    _CfprApVnicProfileAliasSwUuid_Type()
)
cfprApVnicProfileAliasSwUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileAliasSwUuid.setStatus("current")
_CfprApVnicProfileRefTable_Object = MibTable
cfprApVnicProfileRefTable = _CfprApVnicProfileRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 55)
)
if mibBuilder.loadTexts:
    cfprApVnicProfileRefTable.setStatus("current")
_CfprApVnicProfileRefEntry_Object = MibTableRow
cfprApVnicProfileRefEntry = _CfprApVnicProfileRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 55, 1)
)
cfprApVnicProfileRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicProfileRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicProfileRefEntry.setStatus("current")
_CfprApVnicProfileRefInstanceId_Type = CfprApManagedObjectId
_CfprApVnicProfileRefInstanceId_Object = MibTableColumn
cfprApVnicProfileRefInstanceId = _CfprApVnicProfileRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 55, 1, 1),
    _CfprApVnicProfileRefInstanceId_Type()
)
cfprApVnicProfileRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicProfileRefInstanceId.setStatus("current")
_CfprApVnicProfileRefDn_Type = CfprApManagedObjectDn
_CfprApVnicProfileRefDn_Object = MibTableColumn
cfprApVnicProfileRefDn = _CfprApVnicProfileRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 55, 1, 2),
    _CfprApVnicProfileRefDn_Type()
)
cfprApVnicProfileRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileRefDn.setStatus("current")
_CfprApVnicProfileRefRn_Type = SnmpAdminString
_CfprApVnicProfileRefRn_Object = MibTableColumn
cfprApVnicProfileRefRn = _CfprApVnicProfileRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 55, 1, 3),
    _CfprApVnicProfileRefRn_Type()
)
cfprApVnicProfileRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileRefRn.setStatus("current")
_CfprApVnicProfileRefName_Type = SnmpAdminString
_CfprApVnicProfileRefName_Object = MibTableColumn
cfprApVnicProfileRefName = _CfprApVnicProfileRefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 55, 1, 4),
    _CfprApVnicProfileRefName_Type()
)
cfprApVnicProfileRefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileRefName.setStatus("current")
_CfprApVnicProfileRefSourceDn_Type = SnmpAdminString
_CfprApVnicProfileRefSourceDn_Object = MibTableColumn
cfprApVnicProfileRefSourceDn = _CfprApVnicProfileRefSourceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 55, 1, 5),
    _CfprApVnicProfileRefSourceDn_Type()
)
cfprApVnicProfileRefSourceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileRefSourceDn.setStatus("current")
_CfprApVnicProfileSetTable_Object = MibTable
cfprApVnicProfileSetTable = _CfprApVnicProfileSetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 56)
)
if mibBuilder.loadTexts:
    cfprApVnicProfileSetTable.setStatus("current")
_CfprApVnicProfileSetEntry_Object = MibTableRow
cfprApVnicProfileSetEntry = _CfprApVnicProfileSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 56, 1)
)
cfprApVnicProfileSetEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicProfileSetInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicProfileSetEntry.setStatus("current")
_CfprApVnicProfileSetInstanceId_Type = CfprApManagedObjectId
_CfprApVnicProfileSetInstanceId_Object = MibTableColumn
cfprApVnicProfileSetInstanceId = _CfprApVnicProfileSetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 56, 1, 1),
    _CfprApVnicProfileSetInstanceId_Type()
)
cfprApVnicProfileSetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicProfileSetInstanceId.setStatus("current")
_CfprApVnicProfileSetDn_Type = CfprApManagedObjectDn
_CfprApVnicProfileSetDn_Object = MibTableColumn
cfprApVnicProfileSetDn = _CfprApVnicProfileSetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 56, 1, 2),
    _CfprApVnicProfileSetDn_Type()
)
cfprApVnicProfileSetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileSetDn.setStatus("current")
_CfprApVnicProfileSetRn_Type = SnmpAdminString
_CfprApVnicProfileSetRn_Object = MibTableColumn
cfprApVnicProfileSetRn = _CfprApVnicProfileSetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 56, 1, 3),
    _CfprApVnicProfileSetRn_Type()
)
cfprApVnicProfileSetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileSetRn.setStatus("current")
_CfprApVnicProfileSetFltAggr_Type = Unsigned64
_CfprApVnicProfileSetFltAggr_Object = MibTableColumn
cfprApVnicProfileSetFltAggr = _CfprApVnicProfileSetFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 56, 1, 4),
    _CfprApVnicProfileSetFltAggr_Type()
)
cfprApVnicProfileSetFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileSetFltAggr.setStatus("current")
_CfprApVnicProfileSetGenNum_Type = Gauge32
_CfprApVnicProfileSetGenNum_Object = MibTableColumn
cfprApVnicProfileSetGenNum = _CfprApVnicProfileSetGenNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 56, 1, 5),
    _CfprApVnicProfileSetGenNum_Type()
)
cfprApVnicProfileSetGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicProfileSetGenNum.setStatus("current")
_CfprApVnicRackServerDiscoveryProfileTable_Object = MibTable
cfprApVnicRackServerDiscoveryProfileTable = _CfprApVnicRackServerDiscoveryProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 57)
)
if mibBuilder.loadTexts:
    cfprApVnicRackServerDiscoveryProfileTable.setStatus("current")
_CfprApVnicRackServerDiscoveryProfileEntry_Object = MibTableRow
cfprApVnicRackServerDiscoveryProfileEntry = _CfprApVnicRackServerDiscoveryProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 57, 1)
)
cfprApVnicRackServerDiscoveryProfileEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicRackServerDiscoveryProfileInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicRackServerDiscoveryProfileEntry.setStatus("current")
_CfprApVnicRackServerDiscoveryProfileInstanceId_Type = CfprApManagedObjectId
_CfprApVnicRackServerDiscoveryProfileInstanceId_Object = MibTableColumn
cfprApVnicRackServerDiscoveryProfileInstanceId = _CfprApVnicRackServerDiscoveryProfileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 57, 1, 1),
    _CfprApVnicRackServerDiscoveryProfileInstanceId_Type()
)
cfprApVnicRackServerDiscoveryProfileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicRackServerDiscoveryProfileInstanceId.setStatus("current")
_CfprApVnicRackServerDiscoveryProfileDn_Type = CfprApManagedObjectDn
_CfprApVnicRackServerDiscoveryProfileDn_Object = MibTableColumn
cfprApVnicRackServerDiscoveryProfileDn = _CfprApVnicRackServerDiscoveryProfileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 57, 1, 2),
    _CfprApVnicRackServerDiscoveryProfileDn_Type()
)
cfprApVnicRackServerDiscoveryProfileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicRackServerDiscoveryProfileDn.setStatus("current")
_CfprApVnicRackServerDiscoveryProfileRn_Type = SnmpAdminString
_CfprApVnicRackServerDiscoveryProfileRn_Object = MibTableColumn
cfprApVnicRackServerDiscoveryProfileRn = _CfprApVnicRackServerDiscoveryProfileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 57, 1, 3),
    _CfprApVnicRackServerDiscoveryProfileRn_Type()
)
cfprApVnicRackServerDiscoveryProfileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicRackServerDiscoveryProfileRn.setStatus("current")
_CfprApVnicRackServerDiscoveryProfileDescr_Type = SnmpAdminString
_CfprApVnicRackServerDiscoveryProfileDescr_Object = MibTableColumn
cfprApVnicRackServerDiscoveryProfileDescr = _CfprApVnicRackServerDiscoveryProfileDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 57, 1, 4),
    _CfprApVnicRackServerDiscoveryProfileDescr_Type()
)
cfprApVnicRackServerDiscoveryProfileDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicRackServerDiscoveryProfileDescr.setStatus("current")
_CfprApVnicRackServerDiscoveryProfileIntId_Type = SnmpAdminString
_CfprApVnicRackServerDiscoveryProfileIntId_Object = MibTableColumn
cfprApVnicRackServerDiscoveryProfileIntId = _CfprApVnicRackServerDiscoveryProfileIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 57, 1, 5),
    _CfprApVnicRackServerDiscoveryProfileIntId_Type()
)
cfprApVnicRackServerDiscoveryProfileIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicRackServerDiscoveryProfileIntId.setStatus("current")
_CfprApVnicRackServerDiscoveryProfileMaxPorts_Type = Gauge32
_CfprApVnicRackServerDiscoveryProfileMaxPorts_Object = MibTableColumn
cfprApVnicRackServerDiscoveryProfileMaxPorts = _CfprApVnicRackServerDiscoveryProfileMaxPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 57, 1, 6),
    _CfprApVnicRackServerDiscoveryProfileMaxPorts_Type()
)
cfprApVnicRackServerDiscoveryProfileMaxPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicRackServerDiscoveryProfileMaxPorts.setStatus("current")
_CfprApVnicRackServerDiscoveryProfileName_Type = SnmpAdminString
_CfprApVnicRackServerDiscoveryProfileName_Object = MibTableColumn
cfprApVnicRackServerDiscoveryProfileName = _CfprApVnicRackServerDiscoveryProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 57, 1, 7),
    _CfprApVnicRackServerDiscoveryProfileName_Type()
)
cfprApVnicRackServerDiscoveryProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicRackServerDiscoveryProfileName.setStatus("current")
_CfprApVnicRackServerDiscoveryProfilePolicyLevel_Type = Gauge32
_CfprApVnicRackServerDiscoveryProfilePolicyLevel_Object = MibTableColumn
cfprApVnicRackServerDiscoveryProfilePolicyLevel = _CfprApVnicRackServerDiscoveryProfilePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 57, 1, 8),
    _CfprApVnicRackServerDiscoveryProfilePolicyLevel_Type()
)
cfprApVnicRackServerDiscoveryProfilePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicRackServerDiscoveryProfilePolicyLevel.setStatus("current")
_CfprApVnicRackServerDiscoveryProfilePolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApVnicRackServerDiscoveryProfilePolicyOwner_Object = MibTableColumn
cfprApVnicRackServerDiscoveryProfilePolicyOwner = _CfprApVnicRackServerDiscoveryProfilePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 57, 1, 9),
    _CfprApVnicRackServerDiscoveryProfilePolicyOwner_Type()
)
cfprApVnicRackServerDiscoveryProfilePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicRackServerDiscoveryProfilePolicyOwner.setStatus("current")
_CfprApVnicSanConnTemplTable_Object = MibTable
cfprApVnicSanConnTemplTable = _CfprApVnicSanConnTemplTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 59)
)
if mibBuilder.loadTexts:
    cfprApVnicSanConnTemplTable.setStatus("current")
_CfprApVnicSanConnTemplEntry_Object = MibTableRow
cfprApVnicSanConnTemplEntry = _CfprApVnicSanConnTemplEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 59, 1)
)
cfprApVnicSanConnTemplEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicSanConnTemplInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicSanConnTemplEntry.setStatus("current")
_CfprApVnicSanConnTemplInstanceId_Type = CfprApManagedObjectId
_CfprApVnicSanConnTemplInstanceId_Object = MibTableColumn
cfprApVnicSanConnTemplInstanceId = _CfprApVnicSanConnTemplInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 59, 1, 1),
    _CfprApVnicSanConnTemplInstanceId_Type()
)
cfprApVnicSanConnTemplInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicSanConnTemplInstanceId.setStatus("current")
_CfprApVnicSanConnTemplDn_Type = CfprApManagedObjectDn
_CfprApVnicSanConnTemplDn_Object = MibTableColumn
cfprApVnicSanConnTemplDn = _CfprApVnicSanConnTemplDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 59, 1, 2),
    _CfprApVnicSanConnTemplDn_Type()
)
cfprApVnicSanConnTemplDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicSanConnTemplDn.setStatus("current")
_CfprApVnicSanConnTemplRn_Type = SnmpAdminString
_CfprApVnicSanConnTemplRn_Object = MibTableColumn
cfprApVnicSanConnTemplRn = _CfprApVnicSanConnTemplRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 59, 1, 3),
    _CfprApVnicSanConnTemplRn_Type()
)
cfprApVnicSanConnTemplRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicSanConnTemplRn.setStatus("current")
_CfprApVnicSanConnTemplDescr_Type = SnmpAdminString
_CfprApVnicSanConnTemplDescr_Object = MibTableColumn
cfprApVnicSanConnTemplDescr = _CfprApVnicSanConnTemplDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 59, 1, 4),
    _CfprApVnicSanConnTemplDescr_Type()
)
cfprApVnicSanConnTemplDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicSanConnTemplDescr.setStatus("current")
_CfprApVnicSanConnTemplIdentPoolName_Type = SnmpAdminString
_CfprApVnicSanConnTemplIdentPoolName_Object = MibTableColumn
cfprApVnicSanConnTemplIdentPoolName = _CfprApVnicSanConnTemplIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 59, 1, 5),
    _CfprApVnicSanConnTemplIdentPoolName_Type()
)
cfprApVnicSanConnTemplIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicSanConnTemplIdentPoolName.setStatus("current")
_CfprApVnicSanConnTemplIntId_Type = SnmpAdminString
_CfprApVnicSanConnTemplIntId_Object = MibTableColumn
cfprApVnicSanConnTemplIntId = _CfprApVnicSanConnTemplIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 59, 1, 6),
    _CfprApVnicSanConnTemplIntId_Type()
)
cfprApVnicSanConnTemplIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicSanConnTemplIntId.setStatus("current")
_CfprApVnicSanConnTemplMaxDataFieldSize_Type = Gauge32
_CfprApVnicSanConnTemplMaxDataFieldSize_Object = MibTableColumn
cfprApVnicSanConnTemplMaxDataFieldSize = _CfprApVnicSanConnTemplMaxDataFieldSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 59, 1, 7),
    _CfprApVnicSanConnTemplMaxDataFieldSize_Type()
)
cfprApVnicSanConnTemplMaxDataFieldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicSanConnTemplMaxDataFieldSize.setStatus("current")
_CfprApVnicSanConnTemplName_Type = SnmpAdminString
_CfprApVnicSanConnTemplName_Object = MibTableColumn
cfprApVnicSanConnTemplName = _CfprApVnicSanConnTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 59, 1, 8),
    _CfprApVnicSanConnTemplName_Type()
)
cfprApVnicSanConnTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicSanConnTemplName.setStatus("current")
_CfprApVnicSanConnTemplNwCtrlPolicyName_Type = SnmpAdminString
_CfprApVnicSanConnTemplNwCtrlPolicyName_Object = MibTableColumn
cfprApVnicSanConnTemplNwCtrlPolicyName = _CfprApVnicSanConnTemplNwCtrlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 59, 1, 9),
    _CfprApVnicSanConnTemplNwCtrlPolicyName_Type()
)
cfprApVnicSanConnTemplNwCtrlPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicSanConnTemplNwCtrlPolicyName.setStatus("current")
_CfprApVnicSanConnTemplOperIdentPoolName_Type = SnmpAdminString
_CfprApVnicSanConnTemplOperIdentPoolName_Object = MibTableColumn
cfprApVnicSanConnTemplOperIdentPoolName = _CfprApVnicSanConnTemplOperIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 59, 1, 10),
    _CfprApVnicSanConnTemplOperIdentPoolName_Type()
)
cfprApVnicSanConnTemplOperIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicSanConnTemplOperIdentPoolName.setStatus("current")
_CfprApVnicSanConnTemplOperQosPolicyName_Type = SnmpAdminString
_CfprApVnicSanConnTemplOperQosPolicyName_Object = MibTableColumn
cfprApVnicSanConnTemplOperQosPolicyName = _CfprApVnicSanConnTemplOperQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 59, 1, 11),
    _CfprApVnicSanConnTemplOperQosPolicyName_Type()
)
cfprApVnicSanConnTemplOperQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicSanConnTemplOperQosPolicyName.setStatus("current")
_CfprApVnicSanConnTemplOperStatsPolicyName_Type = SnmpAdminString
_CfprApVnicSanConnTemplOperStatsPolicyName_Object = MibTableColumn
cfprApVnicSanConnTemplOperStatsPolicyName = _CfprApVnicSanConnTemplOperStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 59, 1, 12),
    _CfprApVnicSanConnTemplOperStatsPolicyName_Type()
)
cfprApVnicSanConnTemplOperStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicSanConnTemplOperStatsPolicyName.setStatus("current")
_CfprApVnicSanConnTemplPinToGroupName_Type = SnmpAdminString
_CfprApVnicSanConnTemplPinToGroupName_Object = MibTableColumn
cfprApVnicSanConnTemplPinToGroupName = _CfprApVnicSanConnTemplPinToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 59, 1, 13),
    _CfprApVnicSanConnTemplPinToGroupName_Type()
)
cfprApVnicSanConnTemplPinToGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicSanConnTemplPinToGroupName.setStatus("current")
_CfprApVnicSanConnTemplPolicyLevel_Type = Gauge32
_CfprApVnicSanConnTemplPolicyLevel_Object = MibTableColumn
cfprApVnicSanConnTemplPolicyLevel = _CfprApVnicSanConnTemplPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 59, 1, 14),
    _CfprApVnicSanConnTemplPolicyLevel_Type()
)
cfprApVnicSanConnTemplPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicSanConnTemplPolicyLevel.setStatus("current")
_CfprApVnicSanConnTemplPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApVnicSanConnTemplPolicyOwner_Object = MibTableColumn
cfprApVnicSanConnTemplPolicyOwner = _CfprApVnicSanConnTemplPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 59, 1, 15),
    _CfprApVnicSanConnTemplPolicyOwner_Type()
)
cfprApVnicSanConnTemplPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicSanConnTemplPolicyOwner.setStatus("current")
_CfprApVnicSanConnTemplQosPolicyName_Type = SnmpAdminString
_CfprApVnicSanConnTemplQosPolicyName_Object = MibTableColumn
cfprApVnicSanConnTemplQosPolicyName = _CfprApVnicSanConnTemplQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 59, 1, 16),
    _CfprApVnicSanConnTemplQosPolicyName_Type()
)
cfprApVnicSanConnTemplQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicSanConnTemplQosPolicyName.setStatus("current")
_CfprApVnicSanConnTemplStatsPolicyName_Type = SnmpAdminString
_CfprApVnicSanConnTemplStatsPolicyName_Object = MibTableColumn
cfprApVnicSanConnTemplStatsPolicyName = _CfprApVnicSanConnTemplStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 59, 1, 17),
    _CfprApVnicSanConnTemplStatsPolicyName_Type()
)
cfprApVnicSanConnTemplStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicSanConnTemplStatsPolicyName.setStatus("current")
_CfprApVnicSanConnTemplSwitchId_Type = CfprApNetworkSwitchId
_CfprApVnicSanConnTemplSwitchId_Object = MibTableColumn
cfprApVnicSanConnTemplSwitchId = _CfprApVnicSanConnTemplSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 59, 1, 18),
    _CfprApVnicSanConnTemplSwitchId_Type()
)
cfprApVnicSanConnTemplSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicSanConnTemplSwitchId.setStatus("current")
_CfprApVnicSanConnTemplTarget_Type = CfprApVnicSanConnTemplTarget
_CfprApVnicSanConnTemplTarget_Object = MibTableColumn
cfprApVnicSanConnTemplTarget = _CfprApVnicSanConnTemplTarget_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 59, 1, 19),
    _CfprApVnicSanConnTemplTarget_Type()
)
cfprApVnicSanConnTemplTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicSanConnTemplTarget.setStatus("current")
_CfprApVnicSanConnTemplTemplType_Type = CfprApVnicTemplateType
_CfprApVnicSanConnTemplTemplType_Object = MibTableColumn
cfprApVnicSanConnTemplTemplType = _CfprApVnicSanConnTemplTemplType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 59, 1, 20),
    _CfprApVnicSanConnTemplTemplType_Type()
)
cfprApVnicSanConnTemplTemplType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicSanConnTemplTemplType.setStatus("current")
_CfprApVnicScsiTable_Object = MibTable
cfprApVnicScsiTable = _CfprApVnicScsiTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 60)
)
if mibBuilder.loadTexts:
    cfprApVnicScsiTable.setStatus("current")
_CfprApVnicScsiEntry_Object = MibTableRow
cfprApVnicScsiEntry = _CfprApVnicScsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 60, 1)
)
cfprApVnicScsiEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicScsiInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicScsiEntry.setStatus("current")
_CfprApVnicScsiInstanceId_Type = CfprApManagedObjectId
_CfprApVnicScsiInstanceId_Object = MibTableColumn
cfprApVnicScsiInstanceId = _CfprApVnicScsiInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 60, 1, 1),
    _CfprApVnicScsiInstanceId_Type()
)
cfprApVnicScsiInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicScsiInstanceId.setStatus("current")
_CfprApVnicScsiDn_Type = CfprApManagedObjectDn
_CfprApVnicScsiDn_Object = MibTableColumn
cfprApVnicScsiDn = _CfprApVnicScsiDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 60, 1, 2),
    _CfprApVnicScsiDn_Type()
)
cfprApVnicScsiDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiDn.setStatus("current")
_CfprApVnicScsiRn_Type = SnmpAdminString
_CfprApVnicScsiRn_Object = MibTableColumn
cfprApVnicScsiRn = _CfprApVnicScsiRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 60, 1, 3),
    _CfprApVnicScsiRn_Type()
)
cfprApVnicScsiRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiRn.setStatus("current")
_CfprApVnicScsiAdaptorProfileName_Type = SnmpAdminString
_CfprApVnicScsiAdaptorProfileName_Object = MibTableColumn
cfprApVnicScsiAdaptorProfileName = _CfprApVnicScsiAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 60, 1, 4),
    _CfprApVnicScsiAdaptorProfileName_Type()
)
cfprApVnicScsiAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiAdaptorProfileName.setStatus("current")
_CfprApVnicScsiAdminHostPort_Type = CfprApFabricHostPortId
_CfprApVnicScsiAdminHostPort_Object = MibTableColumn
cfprApVnicScsiAdminHostPort = _CfprApVnicScsiAdminHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 60, 1, 5),
    _CfprApVnicScsiAdminHostPort_Type()
)
cfprApVnicScsiAdminHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiAdminHostPort.setStatus("current")
_CfprApVnicScsiAdminVcon_Type = SnmpAdminString
_CfprApVnicScsiAdminVcon_Object = MibTableColumn
cfprApVnicScsiAdminVcon = _CfprApVnicScsiAdminVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 60, 1, 6),
    _CfprApVnicScsiAdminVcon_Type()
)
cfprApVnicScsiAdminVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiAdminVcon.setStatus("current")
_CfprApVnicScsiAppRole_Type = CfprApVnicAppRole
_CfprApVnicScsiAppRole_Object = MibTableColumn
cfprApVnicScsiAppRole = _CfprApVnicScsiAppRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 60, 1, 7),
    _CfprApVnicScsiAppRole_Type()
)
cfprApVnicScsiAppRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiAppRole.setStatus("current")
_CfprApVnicScsiBootDev_Type = CfprApVnicVnicBootDev
_CfprApVnicScsiBootDev_Object = MibTableColumn
cfprApVnicScsiBootDev = _CfprApVnicScsiBootDev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 60, 1, 8),
    _CfprApVnicScsiBootDev_Type()
)
cfprApVnicScsiBootDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiBootDev.setStatus("current")
_CfprApVnicScsiConfigQualifier_Type = CfprApVnicConfigIssues
_CfprApVnicScsiConfigQualifier_Object = MibTableColumn
cfprApVnicScsiConfigQualifier = _CfprApVnicScsiConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 60, 1, 9),
    _CfprApVnicScsiConfigQualifier_Type()
)
cfprApVnicScsiConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiConfigQualifier.setStatus("current")
_CfprApVnicScsiConfigState_Type = CfprApLsConfigState
_CfprApVnicScsiConfigState_Object = MibTableColumn
cfprApVnicScsiConfigState = _CfprApVnicScsiConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 60, 1, 10),
    _CfprApVnicScsiConfigState_Type()
)
cfprApVnicScsiConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiConfigState.setStatus("current")
_CfprApVnicScsiEquipmentDn_Type = SnmpAdminString
_CfprApVnicScsiEquipmentDn_Object = MibTableColumn
cfprApVnicScsiEquipmentDn = _CfprApVnicScsiEquipmentDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 60, 1, 11),
    _CfprApVnicScsiEquipmentDn_Type()
)
cfprApVnicScsiEquipmentDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiEquipmentDn.setStatus("current")
_CfprApVnicScsiIdentPoolName_Type = SnmpAdminString
_CfprApVnicScsiIdentPoolName_Object = MibTableColumn
cfprApVnicScsiIdentPoolName = _CfprApVnicScsiIdentPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 60, 1, 12),
    _CfprApVnicScsiIdentPoolName_Type()
)
cfprApVnicScsiIdentPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiIdentPoolName.setStatus("current")
_CfprApVnicScsiInstType_Type = CfprApVnicInstantiation
_CfprApVnicScsiInstType_Object = MibTableColumn
cfprApVnicScsiInstType = _CfprApVnicScsiInstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 60, 1, 13),
    _CfprApVnicScsiInstType_Type()
)
cfprApVnicScsiInstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiInstType.setStatus("current")
_CfprApVnicScsiName_Type = SnmpAdminString
_CfprApVnicScsiName_Object = MibTableColumn
cfprApVnicScsiName = _CfprApVnicScsiName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 60, 1, 14),
    _CfprApVnicScsiName_Type()
)
cfprApVnicScsiName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiName.setStatus("current")
_CfprApVnicScsiNwTemplName_Type = SnmpAdminString
_CfprApVnicScsiNwTemplName_Object = MibTableColumn
cfprApVnicScsiNwTemplName = _CfprApVnicScsiNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 60, 1, 15),
    _CfprApVnicScsiNwTemplName_Type()
)
cfprApVnicScsiNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiNwTemplName.setStatus("current")
_CfprApVnicScsiOperHostPort_Type = CfprApVnicVnicOperHostPort
_CfprApVnicScsiOperHostPort_Object = MibTableColumn
cfprApVnicScsiOperHostPort = _CfprApVnicScsiOperHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 60, 1, 16),
    _CfprApVnicScsiOperHostPort_Type()
)
cfprApVnicScsiOperHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiOperHostPort.setStatus("current")
_CfprApVnicScsiOperOrder_Type = Gauge32
_CfprApVnicScsiOperOrder_Object = MibTableColumn
cfprApVnicScsiOperOrder = _CfprApVnicScsiOperOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 60, 1, 17),
    _CfprApVnicScsiOperOrder_Type()
)
cfprApVnicScsiOperOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiOperOrder.setStatus("current")
_CfprApVnicScsiOperSpeed_Type = Gauge32
_CfprApVnicScsiOperSpeed_Object = MibTableColumn
cfprApVnicScsiOperSpeed = _CfprApVnicScsiOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 60, 1, 18),
    _CfprApVnicScsiOperSpeed_Type()
)
cfprApVnicScsiOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiOperSpeed.setStatus("current")
_CfprApVnicScsiOperStatsPolicyName_Type = SnmpAdminString
_CfprApVnicScsiOperStatsPolicyName_Object = MibTableColumn
cfprApVnicScsiOperStatsPolicyName = _CfprApVnicScsiOperStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 60, 1, 19),
    _CfprApVnicScsiOperStatsPolicyName_Type()
)
cfprApVnicScsiOperStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiOperStatsPolicyName.setStatus("current")
_CfprApVnicScsiOperVcon_Type = SnmpAdminString
_CfprApVnicScsiOperVcon_Object = MibTableColumn
cfprApVnicScsiOperVcon = _CfprApVnicScsiOperVcon_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 60, 1, 20),
    _CfprApVnicScsiOperVcon_Type()
)
cfprApVnicScsiOperVcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiOperVcon.setStatus("current")
_CfprApVnicScsiOrder_Type = Gauge32
_CfprApVnicScsiOrder_Object = MibTableColumn
cfprApVnicScsiOrder = _CfprApVnicScsiOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 60, 1, 21),
    _CfprApVnicScsiOrder_Type()
)
cfprApVnicScsiOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiOrder.setStatus("current")
_CfprApVnicScsiOwner_Type = CfprApVnicConnectionOwner
_CfprApVnicScsiOwner_Object = MibTableColumn
cfprApVnicScsiOwner = _CfprApVnicScsiOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 60, 1, 22),
    _CfprApVnicScsiOwner_Type()
)
cfprApVnicScsiOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiOwner.setStatus("current")
_CfprApVnicScsiPinToGroupName_Type = SnmpAdminString
_CfprApVnicScsiPinToGroupName_Object = MibTableColumn
cfprApVnicScsiPinToGroupName = _CfprApVnicScsiPinToGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 60, 1, 23),
    _CfprApVnicScsiPinToGroupName_Type()
)
cfprApVnicScsiPinToGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiPinToGroupName.setStatus("current")
_CfprApVnicScsiQosPolicyName_Type = SnmpAdminString
_CfprApVnicScsiQosPolicyName_Object = MibTableColumn
cfprApVnicScsiQosPolicyName = _CfprApVnicScsiQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 60, 1, 24),
    _CfprApVnicScsiQosPolicyName_Type()
)
cfprApVnicScsiQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiQosPolicyName.setStatus("current")
_CfprApVnicScsiStatsPolicyName_Type = SnmpAdminString
_CfprApVnicScsiStatsPolicyName_Object = MibTableColumn
cfprApVnicScsiStatsPolicyName = _CfprApVnicScsiStatsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 60, 1, 25),
    _CfprApVnicScsiStatsPolicyName_Type()
)
cfprApVnicScsiStatsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiStatsPolicyName.setStatus("current")
_CfprApVnicScsiSwitchId_Type = CfprApNetworkSwitchId
_CfprApVnicScsiSwitchId_Object = MibTableColumn
cfprApVnicScsiSwitchId = _CfprApVnicScsiSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 60, 1, 26),
    _CfprApVnicScsiSwitchId_Type()
)
cfprApVnicScsiSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiSwitchId.setStatus("current")
_CfprApVnicScsiType_Type = CfprApVnicScsiType
_CfprApVnicScsiType_Object = MibTableColumn
cfprApVnicScsiType = _CfprApVnicScsiType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 60, 1, 27),
    _CfprApVnicScsiType_Type()
)
cfprApVnicScsiType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiType.setStatus("current")
_CfprApVnicScsiIfTable_Object = MibTable
cfprApVnicScsiIfTable = _CfprApVnicScsiIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 61)
)
if mibBuilder.loadTexts:
    cfprApVnicScsiIfTable.setStatus("current")
_CfprApVnicScsiIfEntry_Object = MibTableRow
cfprApVnicScsiIfEntry = _CfprApVnicScsiIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 61, 1)
)
cfprApVnicScsiIfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicScsiIfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicScsiIfEntry.setStatus("current")
_CfprApVnicScsiIfInstanceId_Type = CfprApManagedObjectId
_CfprApVnicScsiIfInstanceId_Object = MibTableColumn
cfprApVnicScsiIfInstanceId = _CfprApVnicScsiIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 61, 1, 1),
    _CfprApVnicScsiIfInstanceId_Type()
)
cfprApVnicScsiIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicScsiIfInstanceId.setStatus("current")
_CfprApVnicScsiIfDn_Type = CfprApManagedObjectDn
_CfprApVnicScsiIfDn_Object = MibTableColumn
cfprApVnicScsiIfDn = _CfprApVnicScsiIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 61, 1, 2),
    _CfprApVnicScsiIfDn_Type()
)
cfprApVnicScsiIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiIfDn.setStatus("current")
_CfprApVnicScsiIfRn_Type = SnmpAdminString
_CfprApVnicScsiIfRn_Object = MibTableColumn
cfprApVnicScsiIfRn = _CfprApVnicScsiIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 61, 1, 3),
    _CfprApVnicScsiIfRn_Type()
)
cfprApVnicScsiIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiIfRn.setStatus("current")
_CfprApVnicScsiIfAddr_Type = Unsigned64
_CfprApVnicScsiIfAddr_Object = MibTableColumn
cfprApVnicScsiIfAddr = _CfprApVnicScsiIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 61, 1, 4),
    _CfprApVnicScsiIfAddr_Type()
)
cfprApVnicScsiIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiIfAddr.setStatus("current")
_CfprApVnicScsiIfConfigQualifier_Type = CfprApVnicConfigIssues
_CfprApVnicScsiIfConfigQualifier_Object = MibTableColumn
cfprApVnicScsiIfConfigQualifier = _CfprApVnicScsiIfConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 61, 1, 5),
    _CfprApVnicScsiIfConfigQualifier_Type()
)
cfprApVnicScsiIfConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiIfConfigQualifier.setStatus("current")
_CfprApVnicScsiIfName_Type = SnmpAdminString
_CfprApVnicScsiIfName_Object = MibTableColumn
cfprApVnicScsiIfName = _CfprApVnicScsiIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 61, 1, 6),
    _CfprApVnicScsiIfName_Type()
)
cfprApVnicScsiIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiIfName.setStatus("current")
_CfprApVnicScsiIfOperState_Type = CfprApVnicIfOperState
_CfprApVnicScsiIfOperState_Object = MibTableColumn
cfprApVnicScsiIfOperState = _CfprApVnicScsiIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 61, 1, 7),
    _CfprApVnicScsiIfOperState_Type()
)
cfprApVnicScsiIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiIfOperState.setStatus("current")
_CfprApVnicScsiIfOperVnetDn_Type = SnmpAdminString
_CfprApVnicScsiIfOperVnetDn_Object = MibTableColumn
cfprApVnicScsiIfOperVnetDn = _CfprApVnicScsiIfOperVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 61, 1, 8),
    _CfprApVnicScsiIfOperVnetDn_Type()
)
cfprApVnicScsiIfOperVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiIfOperVnetDn.setStatus("current")
_CfprApVnicScsiIfOperVnetName_Type = SnmpAdminString
_CfprApVnicScsiIfOperVnetName_Object = MibTableColumn
cfprApVnicScsiIfOperVnetName = _CfprApVnicScsiIfOperVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 61, 1, 9),
    _CfprApVnicScsiIfOperVnetName_Type()
)
cfprApVnicScsiIfOperVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiIfOperVnetName.setStatus("current")
_CfprApVnicScsiIfOwner_Type = CfprApVnicConnectionOwner
_CfprApVnicScsiIfOwner_Object = MibTableColumn
cfprApVnicScsiIfOwner = _CfprApVnicScsiIfOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 61, 1, 10),
    _CfprApVnicScsiIfOwner_Type()
)
cfprApVnicScsiIfOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiIfOwner.setStatus("current")
_CfprApVnicScsiIfPubNwId_Type = Gauge32
_CfprApVnicScsiIfPubNwId_Object = MibTableColumn
cfprApVnicScsiIfPubNwId = _CfprApVnicScsiIfPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 61, 1, 11),
    _CfprApVnicScsiIfPubNwId_Type()
)
cfprApVnicScsiIfPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiIfPubNwId.setStatus("current")
_CfprApVnicScsiIfSharing_Type = CfprApFabricVlanSharingType
_CfprApVnicScsiIfSharing_Object = MibTableColumn
cfprApVnicScsiIfSharing = _CfprApVnicScsiIfSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 61, 1, 12),
    _CfprApVnicScsiIfSharing_Type()
)
cfprApVnicScsiIfSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiIfSharing.setStatus("current")
_CfprApVnicScsiIfSwitchId_Type = CfprApNetworkSwitchId
_CfprApVnicScsiIfSwitchId_Object = MibTableColumn
cfprApVnicScsiIfSwitchId = _CfprApVnicScsiIfSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 61, 1, 13),
    _CfprApVnicScsiIfSwitchId_Type()
)
cfprApVnicScsiIfSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiIfSwitchId.setStatus("current")
_CfprApVnicScsiIfType_Type = CfprApVnicAScsiIfType
_CfprApVnicScsiIfType_Object = MibTableColumn
cfprApVnicScsiIfType = _CfprApVnicScsiIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 61, 1, 14),
    _CfprApVnicScsiIfType_Type()
)
cfprApVnicScsiIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiIfType.setStatus("current")
_CfprApVnicScsiIfVnet_Type = Gauge32
_CfprApVnicScsiIfVnet_Object = MibTableColumn
cfprApVnicScsiIfVnet = _CfprApVnicScsiIfVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 61, 1, 15),
    _CfprApVnicScsiIfVnet_Type()
)
cfprApVnicScsiIfVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicScsiIfVnet.setStatus("current")
_CfprApVnicUsnicConPolicyTable_Object = MibTable
cfprApVnicUsnicConPolicyTable = _CfprApVnicUsnicConPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 62)
)
if mibBuilder.loadTexts:
    cfprApVnicUsnicConPolicyTable.setStatus("current")
_CfprApVnicUsnicConPolicyEntry_Object = MibTableRow
cfprApVnicUsnicConPolicyEntry = _CfprApVnicUsnicConPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 62, 1)
)
cfprApVnicUsnicConPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicUsnicConPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicUsnicConPolicyEntry.setStatus("current")
_CfprApVnicUsnicConPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApVnicUsnicConPolicyInstanceId_Object = MibTableColumn
cfprApVnicUsnicConPolicyInstanceId = _CfprApVnicUsnicConPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 62, 1, 1),
    _CfprApVnicUsnicConPolicyInstanceId_Type()
)
cfprApVnicUsnicConPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicUsnicConPolicyInstanceId.setStatus("current")
_CfprApVnicUsnicConPolicyDn_Type = CfprApManagedObjectDn
_CfprApVnicUsnicConPolicyDn_Object = MibTableColumn
cfprApVnicUsnicConPolicyDn = _CfprApVnicUsnicConPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 62, 1, 2),
    _CfprApVnicUsnicConPolicyDn_Type()
)
cfprApVnicUsnicConPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicUsnicConPolicyDn.setStatus("current")
_CfprApVnicUsnicConPolicyRn_Type = SnmpAdminString
_CfprApVnicUsnicConPolicyRn_Object = MibTableColumn
cfprApVnicUsnicConPolicyRn = _CfprApVnicUsnicConPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 62, 1, 3),
    _CfprApVnicUsnicConPolicyRn_Type()
)
cfprApVnicUsnicConPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicUsnicConPolicyRn.setStatus("current")
_CfprApVnicUsnicConPolicyAdaptorProfileName_Type = SnmpAdminString
_CfprApVnicUsnicConPolicyAdaptorProfileName_Object = MibTableColumn
cfprApVnicUsnicConPolicyAdaptorProfileName = _CfprApVnicUsnicConPolicyAdaptorProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 62, 1, 4),
    _CfprApVnicUsnicConPolicyAdaptorProfileName_Type()
)
cfprApVnicUsnicConPolicyAdaptorProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicUsnicConPolicyAdaptorProfileName.setStatus("current")
_CfprApVnicUsnicConPolicyDescr_Type = SnmpAdminString
_CfprApVnicUsnicConPolicyDescr_Object = MibTableColumn
cfprApVnicUsnicConPolicyDescr = _CfprApVnicUsnicConPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 62, 1, 5),
    _CfprApVnicUsnicConPolicyDescr_Type()
)
cfprApVnicUsnicConPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicUsnicConPolicyDescr.setStatus("current")
_CfprApVnicUsnicConPolicyIntId_Type = SnmpAdminString
_CfprApVnicUsnicConPolicyIntId_Object = MibTableColumn
cfprApVnicUsnicConPolicyIntId = _CfprApVnicUsnicConPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 62, 1, 6),
    _CfprApVnicUsnicConPolicyIntId_Type()
)
cfprApVnicUsnicConPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicUsnicConPolicyIntId.setStatus("current")
_CfprApVnicUsnicConPolicyName_Type = SnmpAdminString
_CfprApVnicUsnicConPolicyName_Object = MibTableColumn
cfprApVnicUsnicConPolicyName = _CfprApVnicUsnicConPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 62, 1, 7),
    _CfprApVnicUsnicConPolicyName_Type()
)
cfprApVnicUsnicConPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicUsnicConPolicyName.setStatus("current")
_CfprApVnicUsnicConPolicyPolicyLevel_Type = Gauge32
_CfprApVnicUsnicConPolicyPolicyLevel_Object = MibTableColumn
cfprApVnicUsnicConPolicyPolicyLevel = _CfprApVnicUsnicConPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 62, 1, 8),
    _CfprApVnicUsnicConPolicyPolicyLevel_Type()
)
cfprApVnicUsnicConPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicUsnicConPolicyPolicyLevel.setStatus("current")
_CfprApVnicUsnicConPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApVnicUsnicConPolicyPolicyOwner_Object = MibTableColumn
cfprApVnicUsnicConPolicyPolicyOwner = _CfprApVnicUsnicConPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 62, 1, 9),
    _CfprApVnicUsnicConPolicyPolicyOwner_Type()
)
cfprApVnicUsnicConPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicUsnicConPolicyPolicyOwner.setStatus("current")
_CfprApVnicUsnicConPolicyUsnicCount_Type = Gauge32
_CfprApVnicUsnicConPolicyUsnicCount_Object = MibTableColumn
cfprApVnicUsnicConPolicyUsnicCount = _CfprApVnicUsnicConPolicyUsnicCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 62, 1, 10),
    _CfprApVnicUsnicConPolicyUsnicCount_Type()
)
cfprApVnicUsnicConPolicyUsnicCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicUsnicConPolicyUsnicCount.setStatus("current")
_CfprApVnicUsnicConPolicyRefTable_Object = MibTable
cfprApVnicUsnicConPolicyRefTable = _CfprApVnicUsnicConPolicyRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 63)
)
if mibBuilder.loadTexts:
    cfprApVnicUsnicConPolicyRefTable.setStatus("current")
_CfprApVnicUsnicConPolicyRefEntry_Object = MibTableRow
cfprApVnicUsnicConPolicyRefEntry = _CfprApVnicUsnicConPolicyRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 63, 1)
)
cfprApVnicUsnicConPolicyRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicUsnicConPolicyRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicUsnicConPolicyRefEntry.setStatus("current")
_CfprApVnicUsnicConPolicyRefInstanceId_Type = CfprApManagedObjectId
_CfprApVnicUsnicConPolicyRefInstanceId_Object = MibTableColumn
cfprApVnicUsnicConPolicyRefInstanceId = _CfprApVnicUsnicConPolicyRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 63, 1, 1),
    _CfprApVnicUsnicConPolicyRefInstanceId_Type()
)
cfprApVnicUsnicConPolicyRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicUsnicConPolicyRefInstanceId.setStatus("current")
_CfprApVnicUsnicConPolicyRefDn_Type = CfprApManagedObjectDn
_CfprApVnicUsnicConPolicyRefDn_Object = MibTableColumn
cfprApVnicUsnicConPolicyRefDn = _CfprApVnicUsnicConPolicyRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 63, 1, 2),
    _CfprApVnicUsnicConPolicyRefDn_Type()
)
cfprApVnicUsnicConPolicyRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicUsnicConPolicyRefDn.setStatus("current")
_CfprApVnicUsnicConPolicyRefRn_Type = SnmpAdminString
_CfprApVnicUsnicConPolicyRefRn_Object = MibTableColumn
cfprApVnicUsnicConPolicyRefRn = _CfprApVnicUsnicConPolicyRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 63, 1, 3),
    _CfprApVnicUsnicConPolicyRefRn_Type()
)
cfprApVnicUsnicConPolicyRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicUsnicConPolicyRefRn.setStatus("current")
_CfprApVnicUsnicConPolicyRefConPolicyName_Type = SnmpAdminString
_CfprApVnicUsnicConPolicyRefConPolicyName_Object = MibTableColumn
cfprApVnicUsnicConPolicyRefConPolicyName = _CfprApVnicUsnicConPolicyRefConPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 63, 1, 4),
    _CfprApVnicUsnicConPolicyRefConPolicyName_Type()
)
cfprApVnicUsnicConPolicyRefConPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicUsnicConPolicyRefConPolicyName.setStatus("current")
_CfprApVnicUsnicConPolicyRefOperConPolicyName_Type = SnmpAdminString
_CfprApVnicUsnicConPolicyRefOperConPolicyName_Object = MibTableColumn
cfprApVnicUsnicConPolicyRefOperConPolicyName = _CfprApVnicUsnicConPolicyRefOperConPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 63, 1, 5),
    _CfprApVnicUsnicConPolicyRefOperConPolicyName_Type()
)
cfprApVnicUsnicConPolicyRefOperConPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicUsnicConPolicyRefOperConPolicyName.setStatus("current")
_CfprApVnicVhbaBehPolicyTable_Object = MibTable
cfprApVnicVhbaBehPolicyTable = _CfprApVnicVhbaBehPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 64)
)
if mibBuilder.loadTexts:
    cfprApVnicVhbaBehPolicyTable.setStatus("current")
_CfprApVnicVhbaBehPolicyEntry_Object = MibTableRow
cfprApVnicVhbaBehPolicyEntry = _CfprApVnicVhbaBehPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 64, 1)
)
cfprApVnicVhbaBehPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicVhbaBehPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicVhbaBehPolicyEntry.setStatus("current")
_CfprApVnicVhbaBehPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApVnicVhbaBehPolicyInstanceId_Object = MibTableColumn
cfprApVnicVhbaBehPolicyInstanceId = _CfprApVnicVhbaBehPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 64, 1, 1),
    _CfprApVnicVhbaBehPolicyInstanceId_Type()
)
cfprApVnicVhbaBehPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicVhbaBehPolicyInstanceId.setStatus("current")
_CfprApVnicVhbaBehPolicyDn_Type = CfprApManagedObjectDn
_CfprApVnicVhbaBehPolicyDn_Object = MibTableColumn
cfprApVnicVhbaBehPolicyDn = _CfprApVnicVhbaBehPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 64, 1, 2),
    _CfprApVnicVhbaBehPolicyDn_Type()
)
cfprApVnicVhbaBehPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVhbaBehPolicyDn.setStatus("current")
_CfprApVnicVhbaBehPolicyRn_Type = SnmpAdminString
_CfprApVnicVhbaBehPolicyRn_Object = MibTableColumn
cfprApVnicVhbaBehPolicyRn = _CfprApVnicVhbaBehPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 64, 1, 3),
    _CfprApVnicVhbaBehPolicyRn_Type()
)
cfprApVnicVhbaBehPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVhbaBehPolicyRn.setStatus("current")
_CfprApVnicVhbaBehPolicyAction_Type = CfprApVnicDefaultAction
_CfprApVnicVhbaBehPolicyAction_Object = MibTableColumn
cfprApVnicVhbaBehPolicyAction = _CfprApVnicVhbaBehPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 64, 1, 4),
    _CfprApVnicVhbaBehPolicyAction_Type()
)
cfprApVnicVhbaBehPolicyAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVhbaBehPolicyAction.setStatus("current")
_CfprApVnicVhbaBehPolicyDescr_Type = SnmpAdminString
_CfprApVnicVhbaBehPolicyDescr_Object = MibTableColumn
cfprApVnicVhbaBehPolicyDescr = _CfprApVnicVhbaBehPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 64, 1, 5),
    _CfprApVnicVhbaBehPolicyDescr_Type()
)
cfprApVnicVhbaBehPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVhbaBehPolicyDescr.setStatus("current")
_CfprApVnicVhbaBehPolicyIntId_Type = SnmpAdminString
_CfprApVnicVhbaBehPolicyIntId_Object = MibTableColumn
cfprApVnicVhbaBehPolicyIntId = _CfprApVnicVhbaBehPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 64, 1, 6),
    _CfprApVnicVhbaBehPolicyIntId_Type()
)
cfprApVnicVhbaBehPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVhbaBehPolicyIntId.setStatus("current")
_CfprApVnicVhbaBehPolicyName_Type = SnmpAdminString
_CfprApVnicVhbaBehPolicyName_Object = MibTableColumn
cfprApVnicVhbaBehPolicyName = _CfprApVnicVhbaBehPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 64, 1, 7),
    _CfprApVnicVhbaBehPolicyName_Type()
)
cfprApVnicVhbaBehPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVhbaBehPolicyName.setStatus("current")
_CfprApVnicVhbaBehPolicyNwTemplName_Type = SnmpAdminString
_CfprApVnicVhbaBehPolicyNwTemplName_Object = MibTableColumn
cfprApVnicVhbaBehPolicyNwTemplName = _CfprApVnicVhbaBehPolicyNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 64, 1, 8),
    _CfprApVnicVhbaBehPolicyNwTemplName_Type()
)
cfprApVnicVhbaBehPolicyNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVhbaBehPolicyNwTemplName.setStatus("current")
_CfprApVnicVhbaBehPolicyPolicyLevel_Type = Gauge32
_CfprApVnicVhbaBehPolicyPolicyLevel_Object = MibTableColumn
cfprApVnicVhbaBehPolicyPolicyLevel = _CfprApVnicVhbaBehPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 64, 1, 9),
    _CfprApVnicVhbaBehPolicyPolicyLevel_Type()
)
cfprApVnicVhbaBehPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVhbaBehPolicyPolicyLevel.setStatus("current")
_CfprApVnicVhbaBehPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApVnicVhbaBehPolicyPolicyOwner_Object = MibTableColumn
cfprApVnicVhbaBehPolicyPolicyOwner = _CfprApVnicVhbaBehPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 64, 1, 10),
    _CfprApVnicVhbaBehPolicyPolicyOwner_Type()
)
cfprApVnicVhbaBehPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVhbaBehPolicyPolicyOwner.setStatus("current")
_CfprApVnicVhbaBehPolicyType_Type = CfprApVnicVhbaBehPolicyType
_CfprApVnicVhbaBehPolicyType_Object = MibTableColumn
cfprApVnicVhbaBehPolicyType = _CfprApVnicVhbaBehPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 64, 1, 11),
    _CfprApVnicVhbaBehPolicyType_Type()
)
cfprApVnicVhbaBehPolicyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVhbaBehPolicyType.setStatus("current")
_CfprApVnicVlanTable_Object = MibTable
cfprApVnicVlanTable = _CfprApVnicVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 65)
)
if mibBuilder.loadTexts:
    cfprApVnicVlanTable.setStatus("current")
_CfprApVnicVlanEntry_Object = MibTableRow
cfprApVnicVlanEntry = _CfprApVnicVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 65, 1)
)
cfprApVnicVlanEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicVlanInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicVlanEntry.setStatus("current")
_CfprApVnicVlanInstanceId_Type = CfprApManagedObjectId
_CfprApVnicVlanInstanceId_Object = MibTableColumn
cfprApVnicVlanInstanceId = _CfprApVnicVlanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 65, 1, 1),
    _CfprApVnicVlanInstanceId_Type()
)
cfprApVnicVlanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicVlanInstanceId.setStatus("current")
_CfprApVnicVlanDn_Type = CfprApManagedObjectDn
_CfprApVnicVlanDn_Object = MibTableColumn
cfprApVnicVlanDn = _CfprApVnicVlanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 65, 1, 2),
    _CfprApVnicVlanDn_Type()
)
cfprApVnicVlanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVlanDn.setStatus("current")
_CfprApVnicVlanRn_Type = SnmpAdminString
_CfprApVnicVlanRn_Object = MibTableColumn
cfprApVnicVlanRn = _CfprApVnicVlanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 65, 1, 3),
    _CfprApVnicVlanRn_Type()
)
cfprApVnicVlanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVlanRn.setStatus("current")
_CfprApVnicVlanConfigQualifier_Type = CfprApVnicConfigIssues
_CfprApVnicVlanConfigQualifier_Object = MibTableColumn
cfprApVnicVlanConfigQualifier = _CfprApVnicVlanConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 65, 1, 4),
    _CfprApVnicVlanConfigQualifier_Type()
)
cfprApVnicVlanConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVlanConfigQualifier.setStatus("current")
_CfprApVnicVlanFltAggr_Type = Unsigned64
_CfprApVnicVlanFltAggr_Object = MibTableColumn
cfprApVnicVlanFltAggr = _CfprApVnicVlanFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 65, 1, 5),
    _CfprApVnicVlanFltAggr_Type()
)
cfprApVnicVlanFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVlanFltAggr.setStatus("current")
_CfprApVnicVlanName_Type = SnmpAdminString
_CfprApVnicVlanName_Object = MibTableColumn
cfprApVnicVlanName = _CfprApVnicVlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 65, 1, 6),
    _CfprApVnicVlanName_Type()
)
cfprApVnicVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVlanName.setStatus("current")
_CfprApVnicVlanOperState_Type = CfprApVnicIfOperState
_CfprApVnicVlanOperState_Object = MibTableColumn
cfprApVnicVlanOperState = _CfprApVnicVlanOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 65, 1, 7),
    _CfprApVnicVlanOperState_Type()
)
cfprApVnicVlanOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVlanOperState.setStatus("current")
_CfprApVnicVlanOperVnetDn_Type = SnmpAdminString
_CfprApVnicVlanOperVnetDn_Object = MibTableColumn
cfprApVnicVlanOperVnetDn = _CfprApVnicVlanOperVnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 65, 1, 8),
    _CfprApVnicVlanOperVnetDn_Type()
)
cfprApVnicVlanOperVnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVlanOperVnetDn.setStatus("current")
_CfprApVnicVlanOperVnetName_Type = SnmpAdminString
_CfprApVnicVlanOperVnetName_Object = MibTableColumn
cfprApVnicVlanOperVnetName = _CfprApVnicVlanOperVnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 65, 1, 9),
    _CfprApVnicVlanOperVnetName_Type()
)
cfprApVnicVlanOperVnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVlanOperVnetName.setStatus("current")
_CfprApVnicVlanOwner_Type = CfprApVnicConnectionOwner
_CfprApVnicVlanOwner_Object = MibTableColumn
cfprApVnicVlanOwner = _CfprApVnicVlanOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 65, 1, 10),
    _CfprApVnicVlanOwner_Type()
)
cfprApVnicVlanOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVlanOwner.setStatus("current")
_CfprApVnicVlanPubNwId_Type = Gauge32
_CfprApVnicVlanPubNwId_Object = MibTableColumn
cfprApVnicVlanPubNwId = _CfprApVnicVlanPubNwId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 65, 1, 11),
    _CfprApVnicVlanPubNwId_Type()
)
cfprApVnicVlanPubNwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVlanPubNwId.setStatus("current")
_CfprApVnicVlanSharing_Type = CfprApFabricVlanSharingType
_CfprApVnicVlanSharing_Object = MibTableColumn
cfprApVnicVlanSharing = _CfprApVnicVlanSharing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 65, 1, 12),
    _CfprApVnicVlanSharing_Type()
)
cfprApVnicVlanSharing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVlanSharing.setStatus("current")
_CfprApVnicVlanSwitchId_Type = CfprApNetworkSwitchId
_CfprApVnicVlanSwitchId_Object = MibTableColumn
cfprApVnicVlanSwitchId = _CfprApVnicVlanSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 65, 1, 13),
    _CfprApVnicVlanSwitchId_Type()
)
cfprApVnicVlanSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVlanSwitchId.setStatus("current")
_CfprApVnicVlanType_Type = CfprApVnicConnectionType
_CfprApVnicVlanType_Object = MibTableColumn
cfprApVnicVlanType = _CfprApVnicVlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 65, 1, 14),
    _CfprApVnicVlanType_Type()
)
cfprApVnicVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVlanType.setStatus("current")
_CfprApVnicVlanVlanName_Type = SnmpAdminString
_CfprApVnicVlanVlanName_Object = MibTableColumn
cfprApVnicVlanVlanName = _CfprApVnicVlanVlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 65, 1, 15),
    _CfprApVnicVlanVlanName_Type()
)
cfprApVnicVlanVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVlanVlanName.setStatus("current")
_CfprApVnicVlanVnet_Type = Gauge32
_CfprApVnicVlanVnet_Object = MibTableColumn
cfprApVnicVlanVnet = _CfprApVnicVlanVnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 65, 1, 16),
    _CfprApVnicVlanVnet_Type()
)
cfprApVnicVlanVnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVlanVnet.setStatus("current")
_CfprApVnicVmqConPolicyTable_Object = MibTable
cfprApVnicVmqConPolicyTable = _CfprApVnicVmqConPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 66)
)
if mibBuilder.loadTexts:
    cfprApVnicVmqConPolicyTable.setStatus("current")
_CfprApVnicVmqConPolicyEntry_Object = MibTableRow
cfprApVnicVmqConPolicyEntry = _CfprApVnicVmqConPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 66, 1)
)
cfprApVnicVmqConPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicVmqConPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicVmqConPolicyEntry.setStatus("current")
_CfprApVnicVmqConPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApVnicVmqConPolicyInstanceId_Object = MibTableColumn
cfprApVnicVmqConPolicyInstanceId = _CfprApVnicVmqConPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 66, 1, 1),
    _CfprApVnicVmqConPolicyInstanceId_Type()
)
cfprApVnicVmqConPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicVmqConPolicyInstanceId.setStatus("current")
_CfprApVnicVmqConPolicyDn_Type = CfprApManagedObjectDn
_CfprApVnicVmqConPolicyDn_Object = MibTableColumn
cfprApVnicVmqConPolicyDn = _CfprApVnicVmqConPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 66, 1, 2),
    _CfprApVnicVmqConPolicyDn_Type()
)
cfprApVnicVmqConPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVmqConPolicyDn.setStatus("current")
_CfprApVnicVmqConPolicyRn_Type = SnmpAdminString
_CfprApVnicVmqConPolicyRn_Object = MibTableColumn
cfprApVnicVmqConPolicyRn = _CfprApVnicVmqConPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 66, 1, 3),
    _CfprApVnicVmqConPolicyRn_Type()
)
cfprApVnicVmqConPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVmqConPolicyRn.setStatus("current")
_CfprApVnicVmqConPolicyDescr_Type = SnmpAdminString
_CfprApVnicVmqConPolicyDescr_Object = MibTableColumn
cfprApVnicVmqConPolicyDescr = _CfprApVnicVmqConPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 66, 1, 4),
    _CfprApVnicVmqConPolicyDescr_Type()
)
cfprApVnicVmqConPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVmqConPolicyDescr.setStatus("current")
_CfprApVnicVmqConPolicyIntId_Type = SnmpAdminString
_CfprApVnicVmqConPolicyIntId_Object = MibTableColumn
cfprApVnicVmqConPolicyIntId = _CfprApVnicVmqConPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 66, 1, 5),
    _CfprApVnicVmqConPolicyIntId_Type()
)
cfprApVnicVmqConPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVmqConPolicyIntId.setStatus("current")
_CfprApVnicVmqConPolicyIntrCount_Type = Gauge32
_CfprApVnicVmqConPolicyIntrCount_Object = MibTableColumn
cfprApVnicVmqConPolicyIntrCount = _CfprApVnicVmqConPolicyIntrCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 66, 1, 6),
    _CfprApVnicVmqConPolicyIntrCount_Type()
)
cfprApVnicVmqConPolicyIntrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVmqConPolicyIntrCount.setStatus("current")
_CfprApVnicVmqConPolicyName_Type = SnmpAdminString
_CfprApVnicVmqConPolicyName_Object = MibTableColumn
cfprApVnicVmqConPolicyName = _CfprApVnicVmqConPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 66, 1, 7),
    _CfprApVnicVmqConPolicyName_Type()
)
cfprApVnicVmqConPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVmqConPolicyName.setStatus("current")
_CfprApVnicVmqConPolicyPolicyLevel_Type = Gauge32
_CfprApVnicVmqConPolicyPolicyLevel_Object = MibTableColumn
cfprApVnicVmqConPolicyPolicyLevel = _CfprApVnicVmqConPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 66, 1, 8),
    _CfprApVnicVmqConPolicyPolicyLevel_Type()
)
cfprApVnicVmqConPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVmqConPolicyPolicyLevel.setStatus("current")
_CfprApVnicVmqConPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApVnicVmqConPolicyPolicyOwner_Object = MibTableColumn
cfprApVnicVmqConPolicyPolicyOwner = _CfprApVnicVmqConPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 66, 1, 9),
    _CfprApVnicVmqConPolicyPolicyOwner_Type()
)
cfprApVnicVmqConPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVmqConPolicyPolicyOwner.setStatus("current")
_CfprApVnicVmqConPolicyVmqCount_Type = Gauge32
_CfprApVnicVmqConPolicyVmqCount_Object = MibTableColumn
cfprApVnicVmqConPolicyVmqCount = _CfprApVnicVmqConPolicyVmqCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 66, 1, 10),
    _CfprApVnicVmqConPolicyVmqCount_Type()
)
cfprApVnicVmqConPolicyVmqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVmqConPolicyVmqCount.setStatus("current")
_CfprApVnicVmqConPolicyRefTable_Object = MibTable
cfprApVnicVmqConPolicyRefTable = _CfprApVnicVmqConPolicyRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 67)
)
if mibBuilder.loadTexts:
    cfprApVnicVmqConPolicyRefTable.setStatus("current")
_CfprApVnicVmqConPolicyRefEntry_Object = MibTableRow
cfprApVnicVmqConPolicyRefEntry = _CfprApVnicVmqConPolicyRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 67, 1)
)
cfprApVnicVmqConPolicyRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicVmqConPolicyRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicVmqConPolicyRefEntry.setStatus("current")
_CfprApVnicVmqConPolicyRefInstanceId_Type = CfprApManagedObjectId
_CfprApVnicVmqConPolicyRefInstanceId_Object = MibTableColumn
cfprApVnicVmqConPolicyRefInstanceId = _CfprApVnicVmqConPolicyRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 67, 1, 1),
    _CfprApVnicVmqConPolicyRefInstanceId_Type()
)
cfprApVnicVmqConPolicyRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicVmqConPolicyRefInstanceId.setStatus("current")
_CfprApVnicVmqConPolicyRefDn_Type = CfprApManagedObjectDn
_CfprApVnicVmqConPolicyRefDn_Object = MibTableColumn
cfprApVnicVmqConPolicyRefDn = _CfprApVnicVmqConPolicyRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 67, 1, 2),
    _CfprApVnicVmqConPolicyRefDn_Type()
)
cfprApVnicVmqConPolicyRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVmqConPolicyRefDn.setStatus("current")
_CfprApVnicVmqConPolicyRefRn_Type = SnmpAdminString
_CfprApVnicVmqConPolicyRefRn_Object = MibTableColumn
cfprApVnicVmqConPolicyRefRn = _CfprApVnicVmqConPolicyRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 67, 1, 3),
    _CfprApVnicVmqConPolicyRefRn_Type()
)
cfprApVnicVmqConPolicyRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVmqConPolicyRefRn.setStatus("current")
_CfprApVnicVmqConPolicyRefConPolicyName_Type = SnmpAdminString
_CfprApVnicVmqConPolicyRefConPolicyName_Object = MibTableColumn
cfprApVnicVmqConPolicyRefConPolicyName = _CfprApVnicVmqConPolicyRefConPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 67, 1, 4),
    _CfprApVnicVmqConPolicyRefConPolicyName_Type()
)
cfprApVnicVmqConPolicyRefConPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVmqConPolicyRefConPolicyName.setStatus("current")
_CfprApVnicVmqConPolicyRefOperConPolicyName_Type = SnmpAdminString
_CfprApVnicVmqConPolicyRefOperConPolicyName_Object = MibTableColumn
cfprApVnicVmqConPolicyRefOperConPolicyName = _CfprApVnicVmqConPolicyRefOperConPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 67, 1, 5),
    _CfprApVnicVmqConPolicyRefOperConPolicyName_Type()
)
cfprApVnicVmqConPolicyRefOperConPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVmqConPolicyRefOperConPolicyName.setStatus("current")
_CfprApVnicVnicBehPolicyTable_Object = MibTable
cfprApVnicVnicBehPolicyTable = _CfprApVnicVnicBehPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 68)
)
if mibBuilder.loadTexts:
    cfprApVnicVnicBehPolicyTable.setStatus("current")
_CfprApVnicVnicBehPolicyEntry_Object = MibTableRow
cfprApVnicVnicBehPolicyEntry = _CfprApVnicVnicBehPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 68, 1)
)
cfprApVnicVnicBehPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicVnicBehPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicVnicBehPolicyEntry.setStatus("current")
_CfprApVnicVnicBehPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApVnicVnicBehPolicyInstanceId_Object = MibTableColumn
cfprApVnicVnicBehPolicyInstanceId = _CfprApVnicVnicBehPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 68, 1, 1),
    _CfprApVnicVnicBehPolicyInstanceId_Type()
)
cfprApVnicVnicBehPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicVnicBehPolicyInstanceId.setStatus("current")
_CfprApVnicVnicBehPolicyDn_Type = CfprApManagedObjectDn
_CfprApVnicVnicBehPolicyDn_Object = MibTableColumn
cfprApVnicVnicBehPolicyDn = _CfprApVnicVnicBehPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 68, 1, 2),
    _CfprApVnicVnicBehPolicyDn_Type()
)
cfprApVnicVnicBehPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVnicBehPolicyDn.setStatus("current")
_CfprApVnicVnicBehPolicyRn_Type = SnmpAdminString
_CfprApVnicVnicBehPolicyRn_Object = MibTableColumn
cfprApVnicVnicBehPolicyRn = _CfprApVnicVnicBehPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 68, 1, 3),
    _CfprApVnicVnicBehPolicyRn_Type()
)
cfprApVnicVnicBehPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVnicBehPolicyRn.setStatus("current")
_CfprApVnicVnicBehPolicyAction_Type = CfprApVnicDefaultAction
_CfprApVnicVnicBehPolicyAction_Object = MibTableColumn
cfprApVnicVnicBehPolicyAction = _CfprApVnicVnicBehPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 68, 1, 4),
    _CfprApVnicVnicBehPolicyAction_Type()
)
cfprApVnicVnicBehPolicyAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVnicBehPolicyAction.setStatus("current")
_CfprApVnicVnicBehPolicyDescr_Type = SnmpAdminString
_CfprApVnicVnicBehPolicyDescr_Object = MibTableColumn
cfprApVnicVnicBehPolicyDescr = _CfprApVnicVnicBehPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 68, 1, 5),
    _CfprApVnicVnicBehPolicyDescr_Type()
)
cfprApVnicVnicBehPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVnicBehPolicyDescr.setStatus("current")
_CfprApVnicVnicBehPolicyIntId_Type = SnmpAdminString
_CfprApVnicVnicBehPolicyIntId_Object = MibTableColumn
cfprApVnicVnicBehPolicyIntId = _CfprApVnicVnicBehPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 68, 1, 6),
    _CfprApVnicVnicBehPolicyIntId_Type()
)
cfprApVnicVnicBehPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVnicBehPolicyIntId.setStatus("current")
_CfprApVnicVnicBehPolicyName_Type = SnmpAdminString
_CfprApVnicVnicBehPolicyName_Object = MibTableColumn
cfprApVnicVnicBehPolicyName = _CfprApVnicVnicBehPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 68, 1, 7),
    _CfprApVnicVnicBehPolicyName_Type()
)
cfprApVnicVnicBehPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVnicBehPolicyName.setStatus("current")
_CfprApVnicVnicBehPolicyNwTemplName_Type = SnmpAdminString
_CfprApVnicVnicBehPolicyNwTemplName_Object = MibTableColumn
cfprApVnicVnicBehPolicyNwTemplName = _CfprApVnicVnicBehPolicyNwTemplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 68, 1, 8),
    _CfprApVnicVnicBehPolicyNwTemplName_Type()
)
cfprApVnicVnicBehPolicyNwTemplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVnicBehPolicyNwTemplName.setStatus("current")
_CfprApVnicVnicBehPolicyPolicyLevel_Type = Gauge32
_CfprApVnicVnicBehPolicyPolicyLevel_Object = MibTableColumn
cfprApVnicVnicBehPolicyPolicyLevel = _CfprApVnicVnicBehPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 68, 1, 9),
    _CfprApVnicVnicBehPolicyPolicyLevel_Type()
)
cfprApVnicVnicBehPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVnicBehPolicyPolicyLevel.setStatus("current")
_CfprApVnicVnicBehPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApVnicVnicBehPolicyPolicyOwner_Object = MibTableColumn
cfprApVnicVnicBehPolicyPolicyOwner = _CfprApVnicVnicBehPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 68, 1, 10),
    _CfprApVnicVnicBehPolicyPolicyOwner_Type()
)
cfprApVnicVnicBehPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVnicBehPolicyPolicyOwner.setStatus("current")
_CfprApVnicVnicBehPolicyType_Type = CfprApVnicVnicBehPolicyType
_CfprApVnicVnicBehPolicyType_Object = MibTableColumn
cfprApVnicVnicBehPolicyType = _CfprApVnicVnicBehPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 68, 1, 11),
    _CfprApVnicVnicBehPolicyType_Type()
)
cfprApVnicVnicBehPolicyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicVnicBehPolicyType.setStatus("current")
_CfprApVnicWwpnHistoryTable_Object = MibTable
cfprApVnicWwpnHistoryTable = _CfprApVnicWwpnHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 70)
)
if mibBuilder.loadTexts:
    cfprApVnicWwpnHistoryTable.setStatus("current")
_CfprApVnicWwpnHistoryEntry_Object = MibTableRow
cfprApVnicWwpnHistoryEntry = _CfprApVnicWwpnHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 70, 1)
)
cfprApVnicWwpnHistoryEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-VNIC-MIB", "cfprApVnicWwpnHistoryInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApVnicWwpnHistoryEntry.setStatus("current")
_CfprApVnicWwpnHistoryInstanceId_Type = CfprApManagedObjectId
_CfprApVnicWwpnHistoryInstanceId_Object = MibTableColumn
cfprApVnicWwpnHistoryInstanceId = _CfprApVnicWwpnHistoryInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 70, 1, 1),
    _CfprApVnicWwpnHistoryInstanceId_Type()
)
cfprApVnicWwpnHistoryInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApVnicWwpnHistoryInstanceId.setStatus("current")
_CfprApVnicWwpnHistoryDn_Type = CfprApManagedObjectDn
_CfprApVnicWwpnHistoryDn_Object = MibTableColumn
cfprApVnicWwpnHistoryDn = _CfprApVnicWwpnHistoryDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 70, 1, 2),
    _CfprApVnicWwpnHistoryDn_Type()
)
cfprApVnicWwpnHistoryDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicWwpnHistoryDn.setStatus("current")
_CfprApVnicWwpnHistoryRn_Type = SnmpAdminString
_CfprApVnicWwpnHistoryRn_Object = MibTableColumn
cfprApVnicWwpnHistoryRn = _CfprApVnicWwpnHistoryRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 70, 1, 3),
    _CfprApVnicWwpnHistoryRn_Type()
)
cfprApVnicWwpnHistoryRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicWwpnHistoryRn.setStatus("current")
_CfprApVnicWwpnHistoryOldaddr_Type = Unsigned64
_CfprApVnicWwpnHistoryOldaddr_Object = MibTableColumn
cfprApVnicWwpnHistoryOldaddr = _CfprApVnicWwpnHistoryOldaddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 83, 70, 1, 4),
    _CfprApVnicWwpnHistoryOldaddr_Type()
)
cfprApVnicWwpnHistoryOldaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApVnicWwpnHistoryOldaddr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-VNIC-MIB",
    **{"cfprApVnicObjects": cfprApVnicObjects,
       "cfprApVnicBootIpPolicyTable": cfprApVnicBootIpPolicyTable,
       "cfprApVnicBootIpPolicyEntry": cfprApVnicBootIpPolicyEntry,
       "cfprApVnicBootIpPolicyInstanceId": cfprApVnicBootIpPolicyInstanceId,
       "cfprApVnicBootIpPolicyDn": cfprApVnicBootIpPolicyDn,
       "cfprApVnicBootIpPolicyRn": cfprApVnicBootIpPolicyRn,
       "cfprApVnicBootIpPolicyDescr": cfprApVnicBootIpPolicyDescr,
       "cfprApVnicBootIpPolicyIntId": cfprApVnicBootIpPolicyIntId,
       "cfprApVnicBootIpPolicyName": cfprApVnicBootIpPolicyName,
       "cfprApVnicBootIpPolicyPolicyLevel": cfprApVnicBootIpPolicyPolicyLevel,
       "cfprApVnicBootIpPolicyPolicyOwner": cfprApVnicBootIpPolicyPolicyOwner,
       "cfprApVnicBootIpPolicyPoolName": cfprApVnicBootIpPolicyPoolName,
       "cfprApVnicBootTargetTable": cfprApVnicBootTargetTable,
       "cfprApVnicBootTargetEntry": cfprApVnicBootTargetEntry,
       "cfprApVnicBootTargetInstanceId": cfprApVnicBootTargetInstanceId,
       "cfprApVnicBootTargetDn": cfprApVnicBootTargetDn,
       "cfprApVnicBootTargetRn": cfprApVnicBootTargetRn,
       "cfprApVnicBootTargetLun": cfprApVnicBootTargetLun,
       "cfprApVnicBootTargetWwn": cfprApVnicBootTargetWwn,
       "cfprApVnicConnDefTable": cfprApVnicConnDefTable,
       "cfprApVnicConnDefEntry": cfprApVnicConnDefEntry,
       "cfprApVnicConnDefInstanceId": cfprApVnicConnDefInstanceId,
       "cfprApVnicConnDefDn": cfprApVnicConnDefDn,
       "cfprApVnicConnDefRn": cfprApVnicConnDefRn,
       "cfprApVnicConnDefFltAggr": cfprApVnicConnDefFltAggr,
       "cfprApVnicConnDefLanConnPolicyName": cfprApVnicConnDefLanConnPolicyName,
       "cfprApVnicConnDefOperLanConnPolicyName": cfprApVnicConnDefOperLanConnPolicyName,
       "cfprApVnicDefBehTable": cfprApVnicDefBehTable,
       "cfprApVnicDefBehEntry": cfprApVnicDefBehEntry,
       "cfprApVnicDefBehInstanceId": cfprApVnicDefBehInstanceId,
       "cfprApVnicDefBehDn": cfprApVnicDefBehDn,
       "cfprApVnicDefBehRn": cfprApVnicDefBehRn,
       "cfprApVnicDefBehAction": cfprApVnicDefBehAction,
       "cfprApVnicDefBehDescr": cfprApVnicDefBehDescr,
       "cfprApVnicDefBehIntId": cfprApVnicDefBehIntId,
       "cfprApVnicDefBehName": cfprApVnicDefBehName,
       "cfprApVnicDefBehNwTemplName": cfprApVnicDefBehNwTemplName,
       "cfprApVnicDefBehPolicyLevel": cfprApVnicDefBehPolicyLevel,
       "cfprApVnicDefBehPolicyOwner": cfprApVnicDefBehPolicyOwner,
       "cfprApVnicDefBehType": cfprApVnicDefBehType,
       "cfprApVnicDynamicConTable": cfprApVnicDynamicConTable,
       "cfprApVnicDynamicConEntry": cfprApVnicDynamicConEntry,
       "cfprApVnicDynamicConInstanceId": cfprApVnicDynamicConInstanceId,
       "cfprApVnicDynamicConDn": cfprApVnicDynamicConDn,
       "cfprApVnicDynamicConRn": cfprApVnicDynamicConRn,
       "cfprApVnicDynamicConAdaptorProfileName": cfprApVnicDynamicConAdaptorProfileName,
       "cfprApVnicDynamicConDescr": cfprApVnicDynamicConDescr,
       "cfprApVnicDynamicConDynamicEth": cfprApVnicDynamicConDynamicEth,
       "cfprApVnicDynamicConIntId": cfprApVnicDynamicConIntId,
       "cfprApVnicDynamicConMtu": cfprApVnicDynamicConMtu,
       "cfprApVnicDynamicConName": cfprApVnicDynamicConName,
       "cfprApVnicDynamicConNamingPrefix": cfprApVnicDynamicConNamingPrefix,
       "cfprApVnicDynamicConPolicyLevel": cfprApVnicDynamicConPolicyLevel,
       "cfprApVnicDynamicConPolicyOwner": cfprApVnicDynamicConPolicyOwner,
       "cfprApVnicDynamicConProtection": cfprApVnicDynamicConProtection,
       "cfprApVnicDynamicConPolicyTable": cfprApVnicDynamicConPolicyTable,
       "cfprApVnicDynamicConPolicyEntry": cfprApVnicDynamicConPolicyEntry,
       "cfprApVnicDynamicConPolicyInstanceId": cfprApVnicDynamicConPolicyInstanceId,
       "cfprApVnicDynamicConPolicyDn": cfprApVnicDynamicConPolicyDn,
       "cfprApVnicDynamicConPolicyRn": cfprApVnicDynamicConPolicyRn,
       "cfprApVnicDynamicConPolicyAdaptorProfileName": cfprApVnicDynamicConPolicyAdaptorProfileName,
       "cfprApVnicDynamicConPolicyDescr": cfprApVnicDynamicConPolicyDescr,
       "cfprApVnicDynamicConPolicyDynamicEth": cfprApVnicDynamicConPolicyDynamicEth,
       "cfprApVnicDynamicConPolicyIntId": cfprApVnicDynamicConPolicyIntId,
       "cfprApVnicDynamicConPolicyMtu": cfprApVnicDynamicConPolicyMtu,
       "cfprApVnicDynamicConPolicyName": cfprApVnicDynamicConPolicyName,
       "cfprApVnicDynamicConPolicyNamingPrefix": cfprApVnicDynamicConPolicyNamingPrefix,
       "cfprApVnicDynamicConPolicyPolicyLevel": cfprApVnicDynamicConPolicyPolicyLevel,
       "cfprApVnicDynamicConPolicyPolicyOwner": cfprApVnicDynamicConPolicyPolicyOwner,
       "cfprApVnicDynamicConPolicyProtection": cfprApVnicDynamicConPolicyProtection,
       "cfprApVnicDynamicConPolicyRefTable": cfprApVnicDynamicConPolicyRefTable,
       "cfprApVnicDynamicConPolicyRefEntry": cfprApVnicDynamicConPolicyRefEntry,
       "cfprApVnicDynamicConPolicyRefInstanceId": cfprApVnicDynamicConPolicyRefInstanceId,
       "cfprApVnicDynamicConPolicyRefDn": cfprApVnicDynamicConPolicyRefDn,
       "cfprApVnicDynamicConPolicyRefRn": cfprApVnicDynamicConPolicyRefRn,
       "cfprApVnicDynamicConPolicyRefConPolicyName": cfprApVnicDynamicConPolicyRefConPolicyName,
       "cfprApVnicDynamicConPolicyRefOperConPolicyName": cfprApVnicDynamicConPolicyRefOperConPolicyName,
       "cfprApVnicDynamicIdUniverseTable": cfprApVnicDynamicIdUniverseTable,
       "cfprApVnicDynamicIdUniverseEntry": cfprApVnicDynamicIdUniverseEntry,
       "cfprApVnicDynamicIdUniverseInstanceId": cfprApVnicDynamicIdUniverseInstanceId,
       "cfprApVnicDynamicIdUniverseDn": cfprApVnicDynamicIdUniverseDn,
       "cfprApVnicDynamicIdUniverseRn": cfprApVnicDynamicIdUniverseRn,
       "cfprApVnicDynamicIdUniverseDescr": cfprApVnicDynamicIdUniverseDescr,
       "cfprApVnicDynamicIdUniverseIntId": cfprApVnicDynamicIdUniverseIntId,
       "cfprApVnicDynamicIdUniverseName": cfprApVnicDynamicIdUniverseName,
       "cfprApVnicDynamicIdUniversePolicyLevel": cfprApVnicDynamicIdUniversePolicyLevel,
       "cfprApVnicDynamicIdUniversePolicyOwner": cfprApVnicDynamicIdUniversePolicyOwner,
       "cfprApVnicDynamicProviderTable": cfprApVnicDynamicProviderTable,
       "cfprApVnicDynamicProviderEntry": cfprApVnicDynamicProviderEntry,
       "cfprApVnicDynamicProviderInstanceId": cfprApVnicDynamicProviderInstanceId,
       "cfprApVnicDynamicProviderDn": cfprApVnicDynamicProviderDn,
       "cfprApVnicDynamicProviderRn": cfprApVnicDynamicProviderRn,
       "cfprApVnicDynamicProviderName": cfprApVnicDynamicProviderName,
       "cfprApVnicDynamicProviderEpTable": cfprApVnicDynamicProviderEpTable,
       "cfprApVnicDynamicProviderEpEntry": cfprApVnicDynamicProviderEpEntry,
       "cfprApVnicDynamicProviderEpInstanceId": cfprApVnicDynamicProviderEpInstanceId,
       "cfprApVnicDynamicProviderEpDn": cfprApVnicDynamicProviderEpDn,
       "cfprApVnicDynamicProviderEpRn": cfprApVnicDynamicProviderEpRn,
       "cfprApVnicDynamicProviderEpChassisId": cfprApVnicDynamicProviderEpChassisId,
       "cfprApVnicDynamicProviderEpPortId": cfprApVnicDynamicProviderEpPortId,
       "cfprApVnicDynamicProviderEpSlotId": cfprApVnicDynamicProviderEpSlotId,
       "cfprApVnicDynamicProviderEpSwitchId": cfprApVnicDynamicProviderEpSwitchId,
       "cfprApVnicEthLifTable": cfprApVnicEthLifTable,
       "cfprApVnicEthLifEntry": cfprApVnicEthLifEntry,
       "cfprApVnicEthLifInstanceId": cfprApVnicEthLifInstanceId,
       "cfprApVnicEthLifDn": cfprApVnicEthLifDn,
       "cfprApVnicEthLifRn": cfprApVnicEthLifRn,
       "cfprApVnicEthLifAddr": cfprApVnicEthLifAddr,
       "cfprApVnicEthLifName": cfprApVnicEthLifName,
       "cfprApVnicEthLifNicDn": cfprApVnicEthLifNicDn,
       "cfprApVnicEthLifOwner": cfprApVnicEthLifOwner,
       "cfprApVnicEthLifSwitchId": cfprApVnicEthLifSwitchId,
       "cfprApVnicEthLifType": cfprApVnicEthLifType,
       "cfprApVnicEthLifVnicDn": cfprApVnicEthLifVnicDn,
       "cfprApVnicEtherTable": cfprApVnicEtherTable,
       "cfprApVnicEtherEntry": cfprApVnicEtherEntry,
       "cfprApVnicEtherInstanceId": cfprApVnicEtherInstanceId,
       "cfprApVnicEtherDn": cfprApVnicEtherDn,
       "cfprApVnicEtherRn": cfprApVnicEtherRn,
       "cfprApVnicEtherAdaptorProfileName": cfprApVnicEtherAdaptorProfileName,
       "cfprApVnicEtherAddr": cfprApVnicEtherAddr,
       "cfprApVnicEtherAdminHostPort": cfprApVnicEtherAdminHostPort,
       "cfprApVnicEtherAdminVcon": cfprApVnicEtherAdminVcon,
       "cfprApVnicEtherAppInstId": cfprApVnicEtherAppInstId,
       "cfprApVnicEtherAppRole": cfprApVnicEtherAppRole,
       "cfprApVnicEtherBootDev": cfprApVnicEtherBootDev,
       "cfprApVnicEtherConfigQualifier": cfprApVnicEtherConfigQualifier,
       "cfprApVnicEtherConfigState": cfprApVnicEtherConfigState,
       "cfprApVnicEtherDynamicId": cfprApVnicEtherDynamicId,
       "cfprApVnicEtherEquipmentDn": cfprApVnicEtherEquipmentDn,
       "cfprApVnicEtherFltAggr": cfprApVnicEtherFltAggr,
       "cfprApVnicEtherIdentPoolName": cfprApVnicEtherIdentPoolName,
       "cfprApVnicEtherInstType": cfprApVnicEtherInstType,
       "cfprApVnicEtherIsAllocated": cfprApVnicEtherIsAllocated,
       "cfprApVnicEtherMtu": cfprApVnicEtherMtu,
       "cfprApVnicEtherName": cfprApVnicEtherName,
       "cfprApVnicEtherNwCtrlPolicyName": cfprApVnicEtherNwCtrlPolicyName,
       "cfprApVnicEtherNwTemplName": cfprApVnicEtherNwTemplName,
       "cfprApVnicEtherOperAdaptorProfileName": cfprApVnicEtherOperAdaptorProfileName,
       "cfprApVnicEtherOperHostPort": cfprApVnicEtherOperHostPort,
       "cfprApVnicEtherOperIdentPoolName": cfprApVnicEtherOperIdentPoolName,
       "cfprApVnicEtherOperNwCtrlPolicyName": cfprApVnicEtherOperNwCtrlPolicyName,
       "cfprApVnicEtherOperNwTemplName": cfprApVnicEtherOperNwTemplName,
       "cfprApVnicEtherOperOrder": cfprApVnicEtherOperOrder,
       "cfprApVnicEtherOperPinToGroupName": cfprApVnicEtherOperPinToGroupName,
       "cfprApVnicEtherOperQosPolicyName": cfprApVnicEtherOperQosPolicyName,
       "cfprApVnicEtherOperSpeed": cfprApVnicEtherOperSpeed,
       "cfprApVnicEtherOperStatsPolicyName": cfprApVnicEtherOperStatsPolicyName,
       "cfprApVnicEtherOperVcon": cfprApVnicEtherOperVcon,
       "cfprApVnicEtherOrder": cfprApVnicEtherOrder,
       "cfprApVnicEtherOwner": cfprApVnicEtherOwner,
       "cfprApVnicEtherPfDn": cfprApVnicEtherPfDn,
       "cfprApVnicEtherPinToGroupName": cfprApVnicEtherPinToGroupName,
       "cfprApVnicEtherPortType": cfprApVnicEtherPortType,
       "cfprApVnicEtherQosPolicyName": cfprApVnicEtherQosPolicyName,
       "cfprApVnicEtherStatsPolicyName": cfprApVnicEtherStatsPolicyName,
       "cfprApVnicEtherSwitchId": cfprApVnicEtherSwitchId,
       "cfprApVnicEtherType": cfprApVnicEtherType,
       "cfprApVnicEtherVirtualizationPreference": cfprApVnicEtherVirtualizationPreference,
       "cfprApVnicEtherIfTable": cfprApVnicEtherIfTable,
       "cfprApVnicEtherIfEntry": cfprApVnicEtherIfEntry,
       "cfprApVnicEtherIfInstanceId": cfprApVnicEtherIfInstanceId,
       "cfprApVnicEtherIfDn": cfprApVnicEtherIfDn,
       "cfprApVnicEtherIfRn": cfprApVnicEtherIfRn,
       "cfprApVnicEtherIfAddr": cfprApVnicEtherIfAddr,
       "cfprApVnicEtherIfConfigQualifier": cfprApVnicEtherIfConfigQualifier,
       "cfprApVnicEtherIfDefaultNet": cfprApVnicEtherIfDefaultNet,
       "cfprApVnicEtherIfFltAggr": cfprApVnicEtherIfFltAggr,
       "cfprApVnicEtherIfName": cfprApVnicEtherIfName,
       "cfprApVnicEtherIfOperState": cfprApVnicEtherIfOperState,
       "cfprApVnicEtherIfOperVnetDn": cfprApVnicEtherIfOperVnetDn,
       "cfprApVnicEtherIfOperVnetName": cfprApVnicEtherIfOperVnetName,
       "cfprApVnicEtherIfOwner": cfprApVnicEtherIfOwner,
       "cfprApVnicEtherIfPubNwId": cfprApVnicEtherIfPubNwId,
       "cfprApVnicEtherIfSharing": cfprApVnicEtherIfSharing,
       "cfprApVnicEtherIfSwitchId": cfprApVnicEtherIfSwitchId,
       "cfprApVnicEtherIfType": cfprApVnicEtherIfType,
       "cfprApVnicEtherIfVnet": cfprApVnicEtherIfVnet,
       "cfprApVnicFcTable": cfprApVnicFcTable,
       "cfprApVnicFcEntry": cfprApVnicFcEntry,
       "cfprApVnicFcInstanceId": cfprApVnicFcInstanceId,
       "cfprApVnicFcDn": cfprApVnicFcDn,
       "cfprApVnicFcRn": cfprApVnicFcRn,
       "cfprApVnicFcAdaptorProfileName": cfprApVnicFcAdaptorProfileName,
       "cfprApVnicFcAddr": cfprApVnicFcAddr,
       "cfprApVnicFcAdminHostPort": cfprApVnicFcAdminHostPort,
       "cfprApVnicFcAdminVcon": cfprApVnicFcAdminVcon,
       "cfprApVnicFcAppRole": cfprApVnicFcAppRole,
       "cfprApVnicFcBootDev": cfprApVnicFcBootDev,
       "cfprApVnicFcConfigQualifier": cfprApVnicFcConfigQualifier,
       "cfprApVnicFcConfigState": cfprApVnicFcConfigState,
       "cfprApVnicFcEquipmentDn": cfprApVnicFcEquipmentDn,
       "cfprApVnicFcFltAggr": cfprApVnicFcFltAggr,
       "cfprApVnicFcIdentPoolName": cfprApVnicFcIdentPoolName,
       "cfprApVnicFcInstType": cfprApVnicFcInstType,
       "cfprApVnicFcMaxDataFieldSize": cfprApVnicFcMaxDataFieldSize,
       "cfprApVnicFcName": cfprApVnicFcName,
       "cfprApVnicFcNodeAddr": cfprApVnicFcNodeAddr,
       "cfprApVnicFcNwTemplName": cfprApVnicFcNwTemplName,
       "cfprApVnicFcOperHostPort": cfprApVnicFcOperHostPort,
       "cfprApVnicFcOperIdentPoolName": cfprApVnicFcOperIdentPoolName,
       "cfprApVnicFcOperNwTemplName": cfprApVnicFcOperNwTemplName,
       "cfprApVnicFcOperOrder": cfprApVnicFcOperOrder,
       "cfprApVnicFcOperPinToGroupName": cfprApVnicFcOperPinToGroupName,
       "cfprApVnicFcOperQosPolicyName": cfprApVnicFcOperQosPolicyName,
       "cfprApVnicFcOperSpeed": cfprApVnicFcOperSpeed,
       "cfprApVnicFcOperStatsPolicyName": cfprApVnicFcOperStatsPolicyName,
       "cfprApVnicFcOperVcon": cfprApVnicFcOperVcon,
       "cfprApVnicFcOrder": cfprApVnicFcOrder,
       "cfprApVnicFcOwner": cfprApVnicFcOwner,
       "cfprApVnicFcPersBind": cfprApVnicFcPersBind,
       "cfprApVnicFcPersBindClear": cfprApVnicFcPersBindClear,
       "cfprApVnicFcPinToGroupName": cfprApVnicFcPinToGroupName,
       "cfprApVnicFcQosPolicyName": cfprApVnicFcQosPolicyName,
       "cfprApVnicFcStatsPolicyName": cfprApVnicFcStatsPolicyName,
       "cfprApVnicFcSwitchId": cfprApVnicFcSwitchId,
       "cfprApVnicFcType": cfprApVnicFcType,
       "cfprApVnicFcGroupDefTable": cfprApVnicFcGroupDefTable,
       "cfprApVnicFcGroupDefEntry": cfprApVnicFcGroupDefEntry,
       "cfprApVnicFcGroupDefInstanceId": cfprApVnicFcGroupDefInstanceId,
       "cfprApVnicFcGroupDefDn": cfprApVnicFcGroupDefDn,
       "cfprApVnicFcGroupDefRn": cfprApVnicFcGroupDefRn,
       "cfprApVnicFcGroupDefAdaptorProfileName": cfprApVnicFcGroupDefAdaptorProfileName,
       "cfprApVnicFcGroupDefDescr": cfprApVnicFcGroupDefDescr,
       "cfprApVnicFcGroupDefIdentPoolName": cfprApVnicFcGroupDefIdentPoolName,
       "cfprApVnicFcGroupDefIntId": cfprApVnicFcGroupDefIntId,
       "cfprApVnicFcGroupDefMaxDataFieldSize": cfprApVnicFcGroupDefMaxDataFieldSize,
       "cfprApVnicFcGroupDefName": cfprApVnicFcGroupDefName,
       "cfprApVnicFcGroupDefNwTemplName": cfprApVnicFcGroupDefNwTemplName,
       "cfprApVnicFcGroupDefOperStatsPolicyName": cfprApVnicFcGroupDefOperStatsPolicyName,
       "cfprApVnicFcGroupDefPolicyLevel": cfprApVnicFcGroupDefPolicyLevel,
       "cfprApVnicFcGroupDefPolicyOwner": cfprApVnicFcGroupDefPolicyOwner,
       "cfprApVnicFcGroupDefQosPolicyName": cfprApVnicFcGroupDefQosPolicyName,
       "cfprApVnicFcGroupDefStatsPolicyName": cfprApVnicFcGroupDefStatsPolicyName,
       "cfprApVnicFcGroupTemplTable": cfprApVnicFcGroupTemplTable,
       "cfprApVnicFcGroupTemplEntry": cfprApVnicFcGroupTemplEntry,
       "cfprApVnicFcGroupTemplInstanceId": cfprApVnicFcGroupTemplInstanceId,
       "cfprApVnicFcGroupTemplDn": cfprApVnicFcGroupTemplDn,
       "cfprApVnicFcGroupTemplRn": cfprApVnicFcGroupTemplRn,
       "cfprApVnicFcGroupTemplAdaptorProfileName": cfprApVnicFcGroupTemplAdaptorProfileName,
       "cfprApVnicFcGroupTemplDescr": cfprApVnicFcGroupTemplDescr,
       "cfprApVnicFcGroupTemplIdentPoolName": cfprApVnicFcGroupTemplIdentPoolName,
       "cfprApVnicFcGroupTemplIntId": cfprApVnicFcGroupTemplIntId,
       "cfprApVnicFcGroupTemplMaxDataFieldSize": cfprApVnicFcGroupTemplMaxDataFieldSize,
       "cfprApVnicFcGroupTemplName": cfprApVnicFcGroupTemplName,
       "cfprApVnicFcGroupTemplNwTemplName": cfprApVnicFcGroupTemplNwTemplName,
       "cfprApVnicFcGroupTemplOperStatsPolicyName": cfprApVnicFcGroupTemplOperStatsPolicyName,
       "cfprApVnicFcGroupTemplPolicyLevel": cfprApVnicFcGroupTemplPolicyLevel,
       "cfprApVnicFcGroupTemplPolicyOwner": cfprApVnicFcGroupTemplPolicyOwner,
       "cfprApVnicFcGroupTemplQosPolicyName": cfprApVnicFcGroupTemplQosPolicyName,
       "cfprApVnicFcGroupTemplStatsPolicyName": cfprApVnicFcGroupTemplStatsPolicyName,
       "cfprApVnicFcGroupTemplTemplType": cfprApVnicFcGroupTemplTemplType,
       "cfprApVnicFcIfTable": cfprApVnicFcIfTable,
       "cfprApVnicFcIfEntry": cfprApVnicFcIfEntry,
       "cfprApVnicFcIfInstanceId": cfprApVnicFcIfInstanceId,
       "cfprApVnicFcIfDn": cfprApVnicFcIfDn,
       "cfprApVnicFcIfRn": cfprApVnicFcIfRn,
       "cfprApVnicFcIfConfigQualifier": cfprApVnicFcIfConfigQualifier,
       "cfprApVnicFcIfInitiator": cfprApVnicFcIfInitiator,
       "cfprApVnicFcIfName": cfprApVnicFcIfName,
       "cfprApVnicFcIfOperState": cfprApVnicFcIfOperState,
       "cfprApVnicFcIfOperVnetDn": cfprApVnicFcIfOperVnetDn,
       "cfprApVnicFcIfOperVnetName": cfprApVnicFcIfOperVnetName,
       "cfprApVnicFcIfOwner": cfprApVnicFcIfOwner,
       "cfprApVnicFcIfPubNwId": cfprApVnicFcIfPubNwId,
       "cfprApVnicFcIfSharing": cfprApVnicFcIfSharing,
       "cfprApVnicFcIfSwitchId": cfprApVnicFcIfSwitchId,
       "cfprApVnicFcIfType": cfprApVnicFcIfType,
       "cfprApVnicFcIfVnet": cfprApVnicFcIfVnet,
       "cfprApVnicFcLifTable": cfprApVnicFcLifTable,
       "cfprApVnicFcLifEntry": cfprApVnicFcLifEntry,
       "cfprApVnicFcLifInstanceId": cfprApVnicFcLifInstanceId,
       "cfprApVnicFcLifDn": cfprApVnicFcLifDn,
       "cfprApVnicFcLifRn": cfprApVnicFcLifRn,
       "cfprApVnicFcLifAddr": cfprApVnicFcLifAddr,
       "cfprApVnicFcLifName": cfprApVnicFcLifName,
       "cfprApVnicFcLifNicDn": cfprApVnicFcLifNicDn,
       "cfprApVnicFcLifOwner": cfprApVnicFcLifOwner,
       "cfprApVnicFcLifSwitchId": cfprApVnicFcLifSwitchId,
       "cfprApVnicFcLifType": cfprApVnicFcLifType,
       "cfprApVnicFcLifVnicDn": cfprApVnicFcLifVnicDn,
       "cfprApVnicFcOEIfTable": cfprApVnicFcOEIfTable,
       "cfprApVnicFcOEIfEntry": cfprApVnicFcOEIfEntry,
       "cfprApVnicFcOEIfInstanceId": cfprApVnicFcOEIfInstanceId,
       "cfprApVnicFcOEIfDn": cfprApVnicFcOEIfDn,
       "cfprApVnicFcOEIfRn": cfprApVnicFcOEIfRn,
       "cfprApVnicFcOEIfConfigQualifier": cfprApVnicFcOEIfConfigQualifier,
       "cfprApVnicFcOEIfInitiator": cfprApVnicFcOEIfInitiator,
       "cfprApVnicFcOEIfName": cfprApVnicFcOEIfName,
       "cfprApVnicFcOEIfOperState": cfprApVnicFcOEIfOperState,
       "cfprApVnicFcOEIfOperVnetDn": cfprApVnicFcOEIfOperVnetDn,
       "cfprApVnicFcOEIfOperVnetName": cfprApVnicFcOEIfOperVnetName,
       "cfprApVnicFcOEIfOwner": cfprApVnicFcOEIfOwner,
       "cfprApVnicFcOEIfPubNwId": cfprApVnicFcOEIfPubNwId,
       "cfprApVnicFcOEIfSharing": cfprApVnicFcOEIfSharing,
       "cfprApVnicFcOEIfSwitchId": cfprApVnicFcOEIfSwitchId,
       "cfprApVnicFcOEIfType": cfprApVnicFcOEIfType,
       "cfprApVnicFcOEIfVnet": cfprApVnicFcOEIfVnet,
       "cfprApVnicIPv4DhcpTable": cfprApVnicIPv4DhcpTable,
       "cfprApVnicIPv4DhcpEntry": cfprApVnicIPv4DhcpEntry,
       "cfprApVnicIPv4DhcpInstanceId": cfprApVnicIPv4DhcpInstanceId,
       "cfprApVnicIPv4DhcpDn": cfprApVnicIPv4DhcpDn,
       "cfprApVnicIPv4DhcpRn": cfprApVnicIPv4DhcpRn,
       "cfprApVnicIPv4DhcpAddr": cfprApVnicIPv4DhcpAddr,
       "cfprApVnicIPv4DhcpDefGw": cfprApVnicIPv4DhcpDefGw,
       "cfprApVnicIPv4DhcpSubnet": cfprApVnicIPv4DhcpSubnet,
       "cfprApVnicIPv4DnsTable": cfprApVnicIPv4DnsTable,
       "cfprApVnicIPv4DnsEntry": cfprApVnicIPv4DnsEntry,
       "cfprApVnicIPv4DnsInstanceId": cfprApVnicIPv4DnsInstanceId,
       "cfprApVnicIPv4DnsDn": cfprApVnicIPv4DnsDn,
       "cfprApVnicIPv4DnsRn": cfprApVnicIPv4DnsRn,
       "cfprApVnicIPv4DnsAddr": cfprApVnicIPv4DnsAddr,
       "cfprApVnicIPv4DnsDefGw": cfprApVnicIPv4DnsDefGw,
       "cfprApVnicIPv4DnsPref": cfprApVnicIPv4DnsPref,
       "cfprApVnicIPv4DnsSubnet": cfprApVnicIPv4DnsSubnet,
       "cfprApVnicIPv4IfTable": cfprApVnicIPv4IfTable,
       "cfprApVnicIPv4IfEntry": cfprApVnicIPv4IfEntry,
       "cfprApVnicIPv4IfInstanceId": cfprApVnicIPv4IfInstanceId,
       "cfprApVnicIPv4IfDn": cfprApVnicIPv4IfDn,
       "cfprApVnicIPv4IfRn": cfprApVnicIPv4IfRn,
       "cfprApVnicIPv4IfAddr": cfprApVnicIPv4IfAddr,
       "cfprApVnicIPv4IfConfigQualifier": cfprApVnicIPv4IfConfigQualifier,
       "cfprApVnicIPv4IfName": cfprApVnicIPv4IfName,
       "cfprApVnicIPv4IfOperState": cfprApVnicIPv4IfOperState,
       "cfprApVnicIPv4IfOperVnetDn": cfprApVnicIPv4IfOperVnetDn,
       "cfprApVnicIPv4IfOperVnetName": cfprApVnicIPv4IfOperVnetName,
       "cfprApVnicIPv4IfOwner": cfprApVnicIPv4IfOwner,
       "cfprApVnicIPv4IfPubNwId": cfprApVnicIPv4IfPubNwId,
       "cfprApVnicIPv4IfSharing": cfprApVnicIPv4IfSharing,
       "cfprApVnicIPv4IfSwitchId": cfprApVnicIPv4IfSwitchId,
       "cfprApVnicIPv4IfType": cfprApVnicIPv4IfType,
       "cfprApVnicIPv4IfVnet": cfprApVnicIPv4IfVnet,
       "cfprApVnicIPv4IscsiAddrTable": cfprApVnicIPv4IscsiAddrTable,
       "cfprApVnicIPv4IscsiAddrEntry": cfprApVnicIPv4IscsiAddrEntry,
       "cfprApVnicIPv4IscsiAddrInstanceId": cfprApVnicIPv4IscsiAddrInstanceId,
       "cfprApVnicIPv4IscsiAddrDn": cfprApVnicIPv4IscsiAddrDn,
       "cfprApVnicIPv4IscsiAddrRn": cfprApVnicIPv4IscsiAddrRn,
       "cfprApVnicIPv4IscsiAddrAddr": cfprApVnicIPv4IscsiAddrAddr,
       "cfprApVnicIPv4IscsiAddrDefGw": cfprApVnicIPv4IscsiAddrDefGw,
       "cfprApVnicIPv4IscsiAddrPrimDns": cfprApVnicIPv4IscsiAddrPrimDns,
       "cfprApVnicIPv4IscsiAddrSecDns": cfprApVnicIPv4IscsiAddrSecDns,
       "cfprApVnicIPv4IscsiAddrSubnet": cfprApVnicIPv4IscsiAddrSubnet,
       "cfprApVnicIPv4PooledIscsiAddrTable": cfprApVnicIPv4PooledIscsiAddrTable,
       "cfprApVnicIPv4PooledIscsiAddrEntry": cfprApVnicIPv4PooledIscsiAddrEntry,
       "cfprApVnicIPv4PooledIscsiAddrInstanceId": cfprApVnicIPv4PooledIscsiAddrInstanceId,
       "cfprApVnicIPv4PooledIscsiAddrDn": cfprApVnicIPv4PooledIscsiAddrDn,
       "cfprApVnicIPv4PooledIscsiAddrRn": cfprApVnicIPv4PooledIscsiAddrRn,
       "cfprApVnicIPv4PooledIscsiAddrAddr": cfprApVnicIPv4PooledIscsiAddrAddr,
       "cfprApVnicIPv4PooledIscsiAddrDefGw": cfprApVnicIPv4PooledIscsiAddrDefGw,
       "cfprApVnicIPv4PooledIscsiAddrIdentPoolName": cfprApVnicIPv4PooledIscsiAddrIdentPoolName,
       "cfprApVnicIPv4PooledIscsiAddrOperIdentPoolName": cfprApVnicIPv4PooledIscsiAddrOperIdentPoolName,
       "cfprApVnicIPv4PooledIscsiAddrPrimDns": cfprApVnicIPv4PooledIscsiAddrPrimDns,
       "cfprApVnicIPv4PooledIscsiAddrSecDns": cfprApVnicIPv4PooledIscsiAddrSecDns,
       "cfprApVnicIPv4PooledIscsiAddrSubnet": cfprApVnicIPv4PooledIscsiAddrSubnet,
       "cfprApVnicIPv4StaticRouteTable": cfprApVnicIPv4StaticRouteTable,
       "cfprApVnicIPv4StaticRouteEntry": cfprApVnicIPv4StaticRouteEntry,
       "cfprApVnicIPv4StaticRouteInstanceId": cfprApVnicIPv4StaticRouteInstanceId,
       "cfprApVnicIPv4StaticRouteDn": cfprApVnicIPv4StaticRouteDn,
       "cfprApVnicIPv4StaticRouteRn": cfprApVnicIPv4StaticRouteRn,
       "cfprApVnicIPv4StaticRouteAddr": cfprApVnicIPv4StaticRouteAddr,
       "cfprApVnicIPv4StaticRouteDefGw": cfprApVnicIPv4StaticRouteDefGw,
       "cfprApVnicIPv4StaticRouteGwAddr": cfprApVnicIPv4StaticRouteGwAddr,
       "cfprApVnicIPv4StaticRouteGwSubnet": cfprApVnicIPv4StaticRouteGwSubnet,
       "cfprApVnicIPv4StaticRouteSubnet": cfprApVnicIPv4StaticRouteSubnet,
       "cfprApVnicIScsiTable": cfprApVnicIScsiTable,
       "cfprApVnicIScsiEntry": cfprApVnicIScsiEntry,
       "cfprApVnicIScsiInstanceId": cfprApVnicIScsiInstanceId,
       "cfprApVnicIScsiDn": cfprApVnicIScsiDn,
       "cfprApVnicIScsiRn": cfprApVnicIScsiRn,
       "cfprApVnicIScsiAdaptorProfileName": cfprApVnicIScsiAdaptorProfileName,
       "cfprApVnicIScsiAddr": cfprApVnicIScsiAddr,
       "cfprApVnicIScsiAdminHostPort": cfprApVnicIScsiAdminHostPort,
       "cfprApVnicIScsiAdminVcon": cfprApVnicIScsiAdminVcon,
       "cfprApVnicIScsiAppRole": cfprApVnicIScsiAppRole,
       "cfprApVnicIScsiBootDev": cfprApVnicIScsiBootDev,
       "cfprApVnicIScsiConfigQualifier": cfprApVnicIScsiConfigQualifier,
       "cfprApVnicIScsiConfigState": cfprApVnicIScsiConfigState,
       "cfprApVnicIScsiEquipmentDn": cfprApVnicIScsiEquipmentDn,
       "cfprApVnicIScsiEthEpDn": cfprApVnicIScsiEthEpDn,
       "cfprApVnicIScsiExtIPState": cfprApVnicIScsiExtIPState,
       "cfprApVnicIScsiFltAggr": cfprApVnicIScsiFltAggr,
       "cfprApVnicIScsiIdentPoolName": cfprApVnicIScsiIdentPoolName,
       "cfprApVnicIScsiInitNameSuffix": cfprApVnicIScsiInitNameSuffix,
       "cfprApVnicIScsiInitiatorName": cfprApVnicIScsiInitiatorName,
       "cfprApVnicIScsiInstType": cfprApVnicIScsiInstType,
       "cfprApVnicIScsiIqnIdentPoolName": cfprApVnicIScsiIqnIdentPoolName,
       "cfprApVnicIScsiName": cfprApVnicIScsiName,
       "cfprApVnicIScsiNwTemplName": cfprApVnicIScsiNwTemplName,
       "cfprApVnicIScsiOperHostPort": cfprApVnicIScsiOperHostPort,
       "cfprApVnicIScsiOperIdentPoolName": cfprApVnicIScsiOperIdentPoolName,
       "cfprApVnicIScsiOperIqnIdentPoolName": cfprApVnicIScsiOperIqnIdentPoolName,
       "cfprApVnicIScsiOperOrder": cfprApVnicIScsiOperOrder,
       "cfprApVnicIScsiOperSpeed": cfprApVnicIScsiOperSpeed,
       "cfprApVnicIScsiOperStatsPolicyName": cfprApVnicIScsiOperStatsPolicyName,
       "cfprApVnicIScsiOperVcon": cfprApVnicIScsiOperVcon,
       "cfprApVnicIScsiOrder": cfprApVnicIScsiOrder,
       "cfprApVnicIScsiOwner": cfprApVnicIScsiOwner,
       "cfprApVnicIScsiPinToGroupName": cfprApVnicIScsiPinToGroupName,
       "cfprApVnicIScsiQosPolicyName": cfprApVnicIScsiQosPolicyName,
       "cfprApVnicIScsiStatsPolicyName": cfprApVnicIScsiStatsPolicyName,
       "cfprApVnicIScsiSwitchId": cfprApVnicIScsiSwitchId,
       "cfprApVnicIScsiType": cfprApVnicIScsiType,
       "cfprApVnicIScsiVnicDefType": cfprApVnicIScsiVnicDefType,
       "cfprApVnicIScsiVnicName": cfprApVnicIScsiVnicName,
       "cfprApVnicIScsiAutoTargetIfTable": cfprApVnicIScsiAutoTargetIfTable,
       "cfprApVnicIScsiAutoTargetIfEntry": cfprApVnicIScsiAutoTargetIfEntry,
       "cfprApVnicIScsiAutoTargetIfInstanceId": cfprApVnicIScsiAutoTargetIfInstanceId,
       "cfprApVnicIScsiAutoTargetIfDn": cfprApVnicIScsiAutoTargetIfDn,
       "cfprApVnicIScsiAutoTargetIfRn": cfprApVnicIScsiAutoTargetIfRn,
       "cfprApVnicIScsiAutoTargetIfDhcpVendorId": cfprApVnicIScsiAutoTargetIfDhcpVendorId,
       "cfprApVnicIScsiBootParamsTable": cfprApVnicIScsiBootParamsTable,
       "cfprApVnicIScsiBootParamsEntry": cfprApVnicIScsiBootParamsEntry,
       "cfprApVnicIScsiBootParamsInstanceId": cfprApVnicIScsiBootParamsInstanceId,
       "cfprApVnicIScsiBootParamsDn": cfprApVnicIScsiBootParamsDn,
       "cfprApVnicIScsiBootParamsRn": cfprApVnicIScsiBootParamsRn,
       "cfprApVnicIScsiBootParamsDescr": cfprApVnicIScsiBootParamsDescr,
       "cfprApVnicIScsiBootParamsIntId": cfprApVnicIScsiBootParamsIntId,
       "cfprApVnicIScsiBootParamsName": cfprApVnicIScsiBootParamsName,
       "cfprApVnicIScsiBootParamsPolicyLevel": cfprApVnicIScsiBootParamsPolicyLevel,
       "cfprApVnicIScsiBootParamsPolicyOwner": cfprApVnicIScsiBootParamsPolicyOwner,
       "cfprApVnicIScsiBootVnicTable": cfprApVnicIScsiBootVnicTable,
       "cfprApVnicIScsiBootVnicEntry": cfprApVnicIScsiBootVnicEntry,
       "cfprApVnicIScsiBootVnicInstanceId": cfprApVnicIScsiBootVnicInstanceId,
       "cfprApVnicIScsiBootVnicDn": cfprApVnicIScsiBootVnicDn,
       "cfprApVnicIScsiBootVnicRn": cfprApVnicIScsiBootVnicRn,
       "cfprApVnicIScsiBootVnicDescr": cfprApVnicIScsiBootVnicDescr,
       "cfprApVnicIScsiBootVnicInitiatorName": cfprApVnicIScsiBootVnicInitiatorName,
       "cfprApVnicIScsiBootVnicIntId": cfprApVnicIScsiBootVnicIntId,
       "cfprApVnicIScsiBootVnicIqnIdentPoolName": cfprApVnicIScsiBootVnicIqnIdentPoolName,
       "cfprApVnicIScsiBootVnicName": cfprApVnicIScsiBootVnicName,
       "cfprApVnicIScsiBootVnicOperIqnIdentPoolName": cfprApVnicIScsiBootVnicOperIqnIdentPoolName,
       "cfprApVnicIScsiBootVnicPolicyLevel": cfprApVnicIScsiBootVnicPolicyLevel,
       "cfprApVnicIScsiBootVnicPolicyOwner": cfprApVnicIScsiBootVnicPolicyOwner,
       "cfprApVnicIScsiLCPTable": cfprApVnicIScsiLCPTable,
       "cfprApVnicIScsiLCPEntry": cfprApVnicIScsiLCPEntry,
       "cfprApVnicIScsiLCPInstanceId": cfprApVnicIScsiLCPInstanceId,
       "cfprApVnicIScsiLCPDn": cfprApVnicIScsiLCPDn,
       "cfprApVnicIScsiLCPRn": cfprApVnicIScsiLCPRn,
       "cfprApVnicIScsiLCPAdaptorProfileName": cfprApVnicIScsiLCPAdaptorProfileName,
       "cfprApVnicIScsiLCPAddr": cfprApVnicIScsiLCPAddr,
       "cfprApVnicIScsiLCPAdminHostPort": cfprApVnicIScsiLCPAdminHostPort,
       "cfprApVnicIScsiLCPAdminVcon": cfprApVnicIScsiLCPAdminVcon,
       "cfprApVnicIScsiLCPAppRole": cfprApVnicIScsiLCPAppRole,
       "cfprApVnicIScsiLCPBootDev": cfprApVnicIScsiLCPBootDev,
       "cfprApVnicIScsiLCPConfigQualifier": cfprApVnicIScsiLCPConfigQualifier,
       "cfprApVnicIScsiLCPConfigState": cfprApVnicIScsiLCPConfigState,
       "cfprApVnicIScsiLCPEquipmentDn": cfprApVnicIScsiLCPEquipmentDn,
       "cfprApVnicIScsiLCPFltAggr": cfprApVnicIScsiLCPFltAggr,
       "cfprApVnicIScsiLCPIdentPoolName": cfprApVnicIScsiLCPIdentPoolName,
       "cfprApVnicIScsiLCPInstType": cfprApVnicIScsiLCPInstType,
       "cfprApVnicIScsiLCPName": cfprApVnicIScsiLCPName,
       "cfprApVnicIScsiLCPNwTemplName": cfprApVnicIScsiLCPNwTemplName,
       "cfprApVnicIScsiLCPOperHostPort": cfprApVnicIScsiLCPOperHostPort,
       "cfprApVnicIScsiLCPOperIdentPoolName": cfprApVnicIScsiLCPOperIdentPoolName,
       "cfprApVnicIScsiLCPOperOrder": cfprApVnicIScsiLCPOperOrder,
       "cfprApVnicIScsiLCPOperSpeed": cfprApVnicIScsiLCPOperSpeed,
       "cfprApVnicIScsiLCPOperStatsPolicyName": cfprApVnicIScsiLCPOperStatsPolicyName,
       "cfprApVnicIScsiLCPOperVcon": cfprApVnicIScsiLCPOperVcon,
       "cfprApVnicIScsiLCPOrder": cfprApVnicIScsiLCPOrder,
       "cfprApVnicIScsiLCPOwner": cfprApVnicIScsiLCPOwner,
       "cfprApVnicIScsiLCPPinToGroupName": cfprApVnicIScsiLCPPinToGroupName,
       "cfprApVnicIScsiLCPQosPolicyName": cfprApVnicIScsiLCPQosPolicyName,
       "cfprApVnicIScsiLCPStatsPolicyName": cfprApVnicIScsiLCPStatsPolicyName,
       "cfprApVnicIScsiLCPSwitchId": cfprApVnicIScsiLCPSwitchId,
       "cfprApVnicIScsiLCPType": cfprApVnicIScsiLCPType,
       "cfprApVnicIScsiLCPVnicName": cfprApVnicIScsiLCPVnicName,
       "cfprApVnicIScsiNodeTable": cfprApVnicIScsiNodeTable,
       "cfprApVnicIScsiNodeEntry": cfprApVnicIScsiNodeEntry,
       "cfprApVnicIScsiNodeInstanceId": cfprApVnicIScsiNodeInstanceId,
       "cfprApVnicIScsiNodeDn": cfprApVnicIScsiNodeDn,
       "cfprApVnicIScsiNodeRn": cfprApVnicIScsiNodeRn,
       "cfprApVnicIScsiNodeFltAggr": cfprApVnicIScsiNodeFltAggr,
       "cfprApVnicIScsiNodeInitNameSuffix": cfprApVnicIScsiNodeInitNameSuffix,
       "cfprApVnicIScsiNodeInitiatorName": cfprApVnicIScsiNodeInitiatorName,
       "cfprApVnicIScsiNodeIqnIdentPoolName": cfprApVnicIScsiNodeIqnIdentPoolName,
       "cfprApVnicIScsiNodeOperIqnIdentPoolName": cfprApVnicIScsiNodeOperIqnIdentPoolName,
       "cfprApVnicIScsiNodeOwner": cfprApVnicIScsiNodeOwner,
       "cfprApVnicIScsiStaticTargetIfTable": cfprApVnicIScsiStaticTargetIfTable,
       "cfprApVnicIScsiStaticTargetIfEntry": cfprApVnicIScsiStaticTargetIfEntry,
       "cfprApVnicIScsiStaticTargetIfInstanceId": cfprApVnicIScsiStaticTargetIfInstanceId,
       "cfprApVnicIScsiStaticTargetIfDn": cfprApVnicIScsiStaticTargetIfDn,
       "cfprApVnicIScsiStaticTargetIfRn": cfprApVnicIScsiStaticTargetIfRn,
       "cfprApVnicIScsiStaticTargetIfIpAddress": cfprApVnicIScsiStaticTargetIfIpAddress,
       "cfprApVnicIScsiStaticTargetIfName": cfprApVnicIScsiStaticTargetIfName,
       "cfprApVnicIScsiStaticTargetIfPort": cfprApVnicIScsiStaticTargetIfPort,
       "cfprApVnicIScsiStaticTargetIfPriority": cfprApVnicIScsiStaticTargetIfPriority,
       "cfprApVnicInternalProfileTable": cfprApVnicInternalProfileTable,
       "cfprApVnicInternalProfileEntry": cfprApVnicInternalProfileEntry,
       "cfprApVnicInternalProfileInstanceId": cfprApVnicInternalProfileInstanceId,
       "cfprApVnicInternalProfileDn": cfprApVnicInternalProfileDn,
       "cfprApVnicInternalProfileRn": cfprApVnicInternalProfileRn,
       "cfprApVnicInternalProfileDescr": cfprApVnicInternalProfileDescr,
       "cfprApVnicInternalProfileIntId": cfprApVnicInternalProfileIntId,
       "cfprApVnicInternalProfileMaxPorts": cfprApVnicInternalProfileMaxPorts,
       "cfprApVnicInternalProfileName": cfprApVnicInternalProfileName,
       "cfprApVnicInternalProfilePolicyLevel": cfprApVnicInternalProfilePolicyLevel,
       "cfprApVnicInternalProfilePolicyOwner": cfprApVnicInternalProfilePolicyOwner,
       "cfprApVnicIpV4HistoryTable": cfprApVnicIpV4HistoryTable,
       "cfprApVnicIpV4HistoryEntry": cfprApVnicIpV4HistoryEntry,
       "cfprApVnicIpV4HistoryInstanceId": cfprApVnicIpV4HistoryInstanceId,
       "cfprApVnicIpV4HistoryDn": cfprApVnicIpV4HistoryDn,
       "cfprApVnicIpV4HistoryRn": cfprApVnicIpV4HistoryRn,
       "cfprApVnicIpV4HistoryOldIpV4Addr": cfprApVnicIpV4HistoryOldIpV4Addr,
       "cfprApVnicIpV4MgmtPooledAddrTable": cfprApVnicIpV4MgmtPooledAddrTable,
       "cfprApVnicIpV4MgmtPooledAddrEntry": cfprApVnicIpV4MgmtPooledAddrEntry,
       "cfprApVnicIpV4MgmtPooledAddrInstanceId": cfprApVnicIpV4MgmtPooledAddrInstanceId,
       "cfprApVnicIpV4MgmtPooledAddrDn": cfprApVnicIpV4MgmtPooledAddrDn,
       "cfprApVnicIpV4MgmtPooledAddrRn": cfprApVnicIpV4MgmtPooledAddrRn,
       "cfprApVnicIpV4MgmtPooledAddrAddr": cfprApVnicIpV4MgmtPooledAddrAddr,
       "cfprApVnicIpV4MgmtPooledAddrDefGw": cfprApVnicIpV4MgmtPooledAddrDefGw,
       "cfprApVnicIpV4MgmtPooledAddrName": cfprApVnicIpV4MgmtPooledAddrName,
       "cfprApVnicIpV4MgmtPooledAddrOperName": cfprApVnicIpV4MgmtPooledAddrOperName,
       "cfprApVnicIpV4MgmtPooledAddrPrimDns": cfprApVnicIpV4MgmtPooledAddrPrimDns,
       "cfprApVnicIpV4MgmtPooledAddrSecDns": cfprApVnicIpV4MgmtPooledAddrSecDns,
       "cfprApVnicIpV4MgmtPooledAddrSubnet": cfprApVnicIpV4MgmtPooledAddrSubnet,
       "cfprApVnicIpV4PooledAddrTable": cfprApVnicIpV4PooledAddrTable,
       "cfprApVnicIpV4PooledAddrEntry": cfprApVnicIpV4PooledAddrEntry,
       "cfprApVnicIpV4PooledAddrInstanceId": cfprApVnicIpV4PooledAddrInstanceId,
       "cfprApVnicIpV4PooledAddrDn": cfprApVnicIpV4PooledAddrDn,
       "cfprApVnicIpV4PooledAddrRn": cfprApVnicIpV4PooledAddrRn,
       "cfprApVnicIpV4PooledAddrAddr": cfprApVnicIpV4PooledAddrAddr,
       "cfprApVnicIpV4PooledAddrDefGw": cfprApVnicIpV4PooledAddrDefGw,
       "cfprApVnicIpV4PooledAddrName": cfprApVnicIpV4PooledAddrName,
       "cfprApVnicIpV4PooledAddrOperName": cfprApVnicIpV4PooledAddrOperName,
       "cfprApVnicIpV4PooledAddrPrimDns": cfprApVnicIpV4PooledAddrPrimDns,
       "cfprApVnicIpV4PooledAddrSecDns": cfprApVnicIpV4PooledAddrSecDns,
       "cfprApVnicIpV4PooledAddrSubnet": cfprApVnicIpV4PooledAddrSubnet,
       "cfprApVnicIpV4ProfDerivedAddrTable": cfprApVnicIpV4ProfDerivedAddrTable,
       "cfprApVnicIpV4ProfDerivedAddrEntry": cfprApVnicIpV4ProfDerivedAddrEntry,
       "cfprApVnicIpV4ProfDerivedAddrInstanceId": cfprApVnicIpV4ProfDerivedAddrInstanceId,
       "cfprApVnicIpV4ProfDerivedAddrDn": cfprApVnicIpV4ProfDerivedAddrDn,
       "cfprApVnicIpV4ProfDerivedAddrRn": cfprApVnicIpV4ProfDerivedAddrRn,
       "cfprApVnicIpV4ProfDerivedAddrAddr": cfprApVnicIpV4ProfDerivedAddrAddr,
       "cfprApVnicIpV4ProfDerivedAddrDefGw": cfprApVnicIpV4ProfDerivedAddrDefGw,
       "cfprApVnicIpV4ProfDerivedAddrSubnet": cfprApVnicIpV4ProfDerivedAddrSubnet,
       "cfprApVnicIpV4StaticAddrTable": cfprApVnicIpV4StaticAddrTable,
       "cfprApVnicIpV4StaticAddrEntry": cfprApVnicIpV4StaticAddrEntry,
       "cfprApVnicIpV4StaticAddrInstanceId": cfprApVnicIpV4StaticAddrInstanceId,
       "cfprApVnicIpV4StaticAddrDn": cfprApVnicIpV4StaticAddrDn,
       "cfprApVnicIpV4StaticAddrRn": cfprApVnicIpV4StaticAddrRn,
       "cfprApVnicIpV4StaticAddrAddr": cfprApVnicIpV4StaticAddrAddr,
       "cfprApVnicIpV4StaticAddrDefGw": cfprApVnicIpV4StaticAddrDefGw,
       "cfprApVnicIpV4StaticAddrPrimDns": cfprApVnicIpV4StaticAddrPrimDns,
       "cfprApVnicIpV4StaticAddrSecDns": cfprApVnicIpV4StaticAddrSecDns,
       "cfprApVnicIpV4StaticAddrSubnet": cfprApVnicIpV4StaticAddrSubnet,
       "cfprApVnicIpV6HistoryTable": cfprApVnicIpV6HistoryTable,
       "cfprApVnicIpV6HistoryEntry": cfprApVnicIpV6HistoryEntry,
       "cfprApVnicIpV6HistoryInstanceId": cfprApVnicIpV6HistoryInstanceId,
       "cfprApVnicIpV6HistoryDn": cfprApVnicIpV6HistoryDn,
       "cfprApVnicIpV6HistoryRn": cfprApVnicIpV6HistoryRn,
       "cfprApVnicIpV6HistoryOldIpV6Addr": cfprApVnicIpV6HistoryOldIpV6Addr,
       "cfprApVnicIpV6MgmtPooledAddrTable": cfprApVnicIpV6MgmtPooledAddrTable,
       "cfprApVnicIpV6MgmtPooledAddrEntry": cfprApVnicIpV6MgmtPooledAddrEntry,
       "cfprApVnicIpV6MgmtPooledAddrInstanceId": cfprApVnicIpV6MgmtPooledAddrInstanceId,
       "cfprApVnicIpV6MgmtPooledAddrDn": cfprApVnicIpV6MgmtPooledAddrDn,
       "cfprApVnicIpV6MgmtPooledAddrRn": cfprApVnicIpV6MgmtPooledAddrRn,
       "cfprApVnicIpV6MgmtPooledAddrAddr": cfprApVnicIpV6MgmtPooledAddrAddr,
       "cfprApVnicIpV6MgmtPooledAddrDefGw": cfprApVnicIpV6MgmtPooledAddrDefGw,
       "cfprApVnicIpV6MgmtPooledAddrName": cfprApVnicIpV6MgmtPooledAddrName,
       "cfprApVnicIpV6MgmtPooledAddrOperName": cfprApVnicIpV6MgmtPooledAddrOperName,
       "cfprApVnicIpV6MgmtPooledAddrPrefix": cfprApVnicIpV6MgmtPooledAddrPrefix,
       "cfprApVnicIpV6MgmtPooledAddrPrimDns": cfprApVnicIpV6MgmtPooledAddrPrimDns,
       "cfprApVnicIpV6MgmtPooledAddrSecDns": cfprApVnicIpV6MgmtPooledAddrSecDns,
       "cfprApVnicIpV6StaticAddrTable": cfprApVnicIpV6StaticAddrTable,
       "cfprApVnicIpV6StaticAddrEntry": cfprApVnicIpV6StaticAddrEntry,
       "cfprApVnicIpV6StaticAddrInstanceId": cfprApVnicIpV6StaticAddrInstanceId,
       "cfprApVnicIpV6StaticAddrDn": cfprApVnicIpV6StaticAddrDn,
       "cfprApVnicIpV6StaticAddrRn": cfprApVnicIpV6StaticAddrRn,
       "cfprApVnicIpV6StaticAddrAddr": cfprApVnicIpV6StaticAddrAddr,
       "cfprApVnicIpV6StaticAddrDefGw": cfprApVnicIpV6StaticAddrDefGw,
       "cfprApVnicIpV6StaticAddrPrefix": cfprApVnicIpV6StaticAddrPrefix,
       "cfprApVnicIpV6StaticAddrPrimDns": cfprApVnicIpV6StaticAddrPrimDns,
       "cfprApVnicIpV6StaticAddrSecDns": cfprApVnicIpV6StaticAddrSecDns,
       "cfprApVnicIpcTable": cfprApVnicIpcTable,
       "cfprApVnicIpcEntry": cfprApVnicIpcEntry,
       "cfprApVnicIpcInstanceId": cfprApVnicIpcInstanceId,
       "cfprApVnicIpcDn": cfprApVnicIpcDn,
       "cfprApVnicIpcRn": cfprApVnicIpcRn,
       "cfprApVnicIpcAdaptorProfileName": cfprApVnicIpcAdaptorProfileName,
       "cfprApVnicIpcAddr": cfprApVnicIpcAddr,
       "cfprApVnicIpcAdminHostPort": cfprApVnicIpcAdminHostPort,
       "cfprApVnicIpcAdminVcon": cfprApVnicIpcAdminVcon,
       "cfprApVnicIpcAppRole": cfprApVnicIpcAppRole,
       "cfprApVnicIpcBootDev": cfprApVnicIpcBootDev,
       "cfprApVnicIpcConfigQualifier": cfprApVnicIpcConfigQualifier,
       "cfprApVnicIpcConfigState": cfprApVnicIpcConfigState,
       "cfprApVnicIpcEquipmentDn": cfprApVnicIpcEquipmentDn,
       "cfprApVnicIpcIdentPoolName": cfprApVnicIpcIdentPoolName,
       "cfprApVnicIpcInstType": cfprApVnicIpcInstType,
       "cfprApVnicIpcMtu": cfprApVnicIpcMtu,
       "cfprApVnicIpcName": cfprApVnicIpcName,
       "cfprApVnicIpcNwCtrlPolicyName": cfprApVnicIpcNwCtrlPolicyName,
       "cfprApVnicIpcNwTemplName": cfprApVnicIpcNwTemplName,
       "cfprApVnicIpcOperAdaptorProfileName": cfprApVnicIpcOperAdaptorProfileName,
       "cfprApVnicIpcOperHostPort": cfprApVnicIpcOperHostPort,
       "cfprApVnicIpcOperIdentPoolName": cfprApVnicIpcOperIdentPoolName,
       "cfprApVnicIpcOperNwCtrlPolicyName": cfprApVnicIpcOperNwCtrlPolicyName,
       "cfprApVnicIpcOperNwTemplName": cfprApVnicIpcOperNwTemplName,
       "cfprApVnicIpcOperOrder": cfprApVnicIpcOperOrder,
       "cfprApVnicIpcOperPinToGroupName": cfprApVnicIpcOperPinToGroupName,
       "cfprApVnicIpcOperQosPolicyName": cfprApVnicIpcOperQosPolicyName,
       "cfprApVnicIpcOperSpeed": cfprApVnicIpcOperSpeed,
       "cfprApVnicIpcOperStatsPolicyName": cfprApVnicIpcOperStatsPolicyName,
       "cfprApVnicIpcOperVcon": cfprApVnicIpcOperVcon,
       "cfprApVnicIpcOrder": cfprApVnicIpcOrder,
       "cfprApVnicIpcOwner": cfprApVnicIpcOwner,
       "cfprApVnicIpcPinToGroupName": cfprApVnicIpcPinToGroupName,
       "cfprApVnicIpcQosPolicyName": cfprApVnicIpcQosPolicyName,
       "cfprApVnicIpcStatsPolicyName": cfprApVnicIpcStatsPolicyName,
       "cfprApVnicIpcSwitchId": cfprApVnicIpcSwitchId,
       "cfprApVnicIpcType": cfprApVnicIpcType,
       "cfprApVnicIpcIfTable": cfprApVnicIpcIfTable,
       "cfprApVnicIpcIfEntry": cfprApVnicIpcIfEntry,
       "cfprApVnicIpcIfInstanceId": cfprApVnicIpcIfInstanceId,
       "cfprApVnicIpcIfDn": cfprApVnicIpcIfDn,
       "cfprApVnicIpcIfRn": cfprApVnicIpcIfRn,
       "cfprApVnicIpcIfAddr": cfprApVnicIpcIfAddr,
       "cfprApVnicIpcIfConfigQualifier": cfprApVnicIpcIfConfigQualifier,
       "cfprApVnicIpcIfDefaultNet": cfprApVnicIpcIfDefaultNet,
       "cfprApVnicIpcIfName": cfprApVnicIpcIfName,
       "cfprApVnicIpcIfOperState": cfprApVnicIpcIfOperState,
       "cfprApVnicIpcIfOperVnetDn": cfprApVnicIpcIfOperVnetDn,
       "cfprApVnicIpcIfOperVnetName": cfprApVnicIpcIfOperVnetName,
       "cfprApVnicIpcIfOwner": cfprApVnicIpcIfOwner,
       "cfprApVnicIpcIfPubNwId": cfprApVnicIpcIfPubNwId,
       "cfprApVnicIpcIfSharing": cfprApVnicIpcIfSharing,
       "cfprApVnicIpcIfSwitchId": cfprApVnicIpcIfSwitchId,
       "cfprApVnicIpcIfType": cfprApVnicIpcIfType,
       "cfprApVnicIpcIfVnet": cfprApVnicIpcIfVnet,
       "cfprApVnicIqnHistoryTable": cfprApVnicIqnHistoryTable,
       "cfprApVnicIqnHistoryEntry": cfprApVnicIqnHistoryEntry,
       "cfprApVnicIqnHistoryInstanceId": cfprApVnicIqnHistoryInstanceId,
       "cfprApVnicIqnHistoryDn": cfprApVnicIqnHistoryDn,
       "cfprApVnicIqnHistoryRn": cfprApVnicIqnHistoryRn,
       "cfprApVnicIqnHistoryOldInitiatorName": cfprApVnicIqnHistoryOldInitiatorName,
       "cfprApVnicLanConnPolicyTable": cfprApVnicLanConnPolicyTable,
       "cfprApVnicLanConnPolicyEntry": cfprApVnicLanConnPolicyEntry,
       "cfprApVnicLanConnPolicyInstanceId": cfprApVnicLanConnPolicyInstanceId,
       "cfprApVnicLanConnPolicyDn": cfprApVnicLanConnPolicyDn,
       "cfprApVnicLanConnPolicyRn": cfprApVnicLanConnPolicyRn,
       "cfprApVnicLanConnPolicyDescr": cfprApVnicLanConnPolicyDescr,
       "cfprApVnicLanConnPolicyFltAggr": cfprApVnicLanConnPolicyFltAggr,
       "cfprApVnicLanConnPolicyIntId": cfprApVnicLanConnPolicyIntId,
       "cfprApVnicLanConnPolicyName": cfprApVnicLanConnPolicyName,
       "cfprApVnicLanConnPolicyPolicyLevel": cfprApVnicLanConnPolicyPolicyLevel,
       "cfprApVnicLanConnPolicyPolicyOwner": cfprApVnicLanConnPolicyPolicyOwner,
       "cfprApVnicLanConnTemplTable": cfprApVnicLanConnTemplTable,
       "cfprApVnicLanConnTemplEntry": cfprApVnicLanConnTemplEntry,
       "cfprApVnicLanConnTemplInstanceId": cfprApVnicLanConnTemplInstanceId,
       "cfprApVnicLanConnTemplDn": cfprApVnicLanConnTemplDn,
       "cfprApVnicLanConnTemplRn": cfprApVnicLanConnTemplRn,
       "cfprApVnicLanConnTemplDescr": cfprApVnicLanConnTemplDescr,
       "cfprApVnicLanConnTemplIdentPoolName": cfprApVnicLanConnTemplIdentPoolName,
       "cfprApVnicLanConnTemplIntId": cfprApVnicLanConnTemplIntId,
       "cfprApVnicLanConnTemplMtu": cfprApVnicLanConnTemplMtu,
       "cfprApVnicLanConnTemplName": cfprApVnicLanConnTemplName,
       "cfprApVnicLanConnTemplNwCtrlPolicyName": cfprApVnicLanConnTemplNwCtrlPolicyName,
       "cfprApVnicLanConnTemplOperIdentPoolName": cfprApVnicLanConnTemplOperIdentPoolName,
       "cfprApVnicLanConnTemplOperNwCtrlPolicyName": cfprApVnicLanConnTemplOperNwCtrlPolicyName,
       "cfprApVnicLanConnTemplOperQosPolicyName": cfprApVnicLanConnTemplOperQosPolicyName,
       "cfprApVnicLanConnTemplOperStatsPolicyName": cfprApVnicLanConnTemplOperStatsPolicyName,
       "cfprApVnicLanConnTemplPinToGroupName": cfprApVnicLanConnTemplPinToGroupName,
       "cfprApVnicLanConnTemplPolicyLevel": cfprApVnicLanConnTemplPolicyLevel,
       "cfprApVnicLanConnTemplPolicyOwner": cfprApVnicLanConnTemplPolicyOwner,
       "cfprApVnicLanConnTemplQosPolicyName": cfprApVnicLanConnTemplQosPolicyName,
       "cfprApVnicLanConnTemplStatsPolicyName": cfprApVnicLanConnTemplStatsPolicyName,
       "cfprApVnicLanConnTemplSwitchId": cfprApVnicLanConnTemplSwitchId,
       "cfprApVnicLanConnTemplTarget": cfprApVnicLanConnTemplTarget,
       "cfprApVnicLanConnTemplTemplType": cfprApVnicLanConnTemplTemplType,
       "cfprApVnicLifVlanTable": cfprApVnicLifVlanTable,
       "cfprApVnicLifVlanEntry": cfprApVnicLifVlanEntry,
       "cfprApVnicLifVlanInstanceId": cfprApVnicLifVlanInstanceId,
       "cfprApVnicLifVlanDn": cfprApVnicLifVlanDn,
       "cfprApVnicLifVlanRn": cfprApVnicLifVlanRn,
       "cfprApVnicLifVlanAddr": cfprApVnicLifVlanAddr,
       "cfprApVnicLifVlanConfigQualifier": cfprApVnicLifVlanConfigQualifier,
       "cfprApVnicLifVlanDefaultNet": cfprApVnicLifVlanDefaultNet,
       "cfprApVnicLifVlanName": cfprApVnicLifVlanName,
       "cfprApVnicLifVlanOperState": cfprApVnicLifVlanOperState,
       "cfprApVnicLifVlanOperVnetDn": cfprApVnicLifVlanOperVnetDn,
       "cfprApVnicLifVlanOperVnetName": cfprApVnicLifVlanOperVnetName,
       "cfprApVnicLifVlanOwner": cfprApVnicLifVlanOwner,
       "cfprApVnicLifVlanPubNwId": cfprApVnicLifVlanPubNwId,
       "cfprApVnicLifVlanSharing": cfprApVnicLifVlanSharing,
       "cfprApVnicLifVlanSwitchId": cfprApVnicLifVlanSwitchId,
       "cfprApVnicLifVlanType": cfprApVnicLifVlanType,
       "cfprApVnicLifVlanVnet": cfprApVnicLifVlanVnet,
       "cfprApVnicLifVsanTable": cfprApVnicLifVsanTable,
       "cfprApVnicLifVsanEntry": cfprApVnicLifVsanEntry,
       "cfprApVnicLifVsanInstanceId": cfprApVnicLifVsanInstanceId,
       "cfprApVnicLifVsanDn": cfprApVnicLifVsanDn,
       "cfprApVnicLifVsanRn": cfprApVnicLifVsanRn,
       "cfprApVnicLifVsanConfigQualifier": cfprApVnicLifVsanConfigQualifier,
       "cfprApVnicLifVsanInitiator": cfprApVnicLifVsanInitiator,
       "cfprApVnicLifVsanName": cfprApVnicLifVsanName,
       "cfprApVnicLifVsanOperState": cfprApVnicLifVsanOperState,
       "cfprApVnicLifVsanOperVnetDn": cfprApVnicLifVsanOperVnetDn,
       "cfprApVnicLifVsanOperVnetName": cfprApVnicLifVsanOperVnetName,
       "cfprApVnicLifVsanOwner": cfprApVnicLifVsanOwner,
       "cfprApVnicLifVsanPubNwId": cfprApVnicLifVsanPubNwId,
       "cfprApVnicLifVsanSharing": cfprApVnicLifVsanSharing,
       "cfprApVnicLifVsanSwitchId": cfprApVnicLifVsanSwitchId,
       "cfprApVnicLifVsanType": cfprApVnicLifVsanType,
       "cfprApVnicLifVsanVnet": cfprApVnicLifVsanVnet,
       "cfprApVnicLunTable": cfprApVnicLunTable,
       "cfprApVnicLunEntry": cfprApVnicLunEntry,
       "cfprApVnicLunInstanceId": cfprApVnicLunInstanceId,
       "cfprApVnicLunDn": cfprApVnicLunDn,
       "cfprApVnicLunRn": cfprApVnicLunRn,
       "cfprApVnicLunBootable": cfprApVnicLunBootable,
       "cfprApVnicLunId": cfprApVnicLunId,
       "cfprApVnicMacHistoryTable": cfprApVnicMacHistoryTable,
       "cfprApVnicMacHistoryEntry": cfprApVnicMacHistoryEntry,
       "cfprApVnicMacHistoryInstanceId": cfprApVnicMacHistoryInstanceId,
       "cfprApVnicMacHistoryDn": cfprApVnicMacHistoryDn,
       "cfprApVnicMacHistoryRn": cfprApVnicMacHistoryRn,
       "cfprApVnicMacHistoryOldaddr": cfprApVnicMacHistoryOldaddr,
       "cfprApVnicOProfileAliasTable": cfprApVnicOProfileAliasTable,
       "cfprApVnicOProfileAliasEntry": cfprApVnicOProfileAliasEntry,
       "cfprApVnicOProfileAliasInstanceId": cfprApVnicOProfileAliasInstanceId,
       "cfprApVnicOProfileAliasDn": cfprApVnicOProfileAliasDn,
       "cfprApVnicOProfileAliasRn": cfprApVnicOProfileAliasRn,
       "cfprApVnicOProfileAliasAlias": cfprApVnicOProfileAliasAlias,
       "cfprApVnicOProfileAliasMgmtPlane": cfprApVnicOProfileAliasMgmtPlane,
       "cfprApVnicOProfileAliasVSwitchId": cfprApVnicOProfileAliasVSwitchId,
       "cfprApVnicOProfileAliasVSwitchName": cfprApVnicOProfileAliasVSwitchName,
       "cfprApVnicProfileTable": cfprApVnicProfileTable,
       "cfprApVnicProfileEntry": cfprApVnicProfileEntry,
       "cfprApVnicProfileInstanceId": cfprApVnicProfileInstanceId,
       "cfprApVnicProfileDn": cfprApVnicProfileDn,
       "cfprApVnicProfileRn": cfprApVnicProfileRn,
       "cfprApVnicProfileCdp": cfprApVnicProfileCdp,
       "cfprApVnicProfileConfigQualifier": cfprApVnicProfileConfigQualifier,
       "cfprApVnicProfileCos": cfprApVnicProfileCos,
       "cfprApVnicProfileDescr": cfprApVnicProfileDescr,
       "cfprApVnicProfileForgeMac": cfprApVnicProfileForgeMac,
       "cfprApVnicProfileHostNwIOPerf": cfprApVnicProfileHostNwIOPerf,
       "cfprApVnicProfileIntId": cfprApVnicProfileIntId,
       "cfprApVnicProfileMacRegisterMode": cfprApVnicProfileMacRegisterMode,
       "cfprApVnicProfileMaxPorts": cfprApVnicProfileMaxPorts,
       "cfprApVnicProfileName": cfprApVnicProfileName,
       "cfprApVnicProfileNwCtrlPolicyName": cfprApVnicProfileNwCtrlPolicyName,
       "cfprApVnicProfileOperNwCtrlPolicyName": cfprApVnicProfileOperNwCtrlPolicyName,
       "cfprApVnicProfileOperQosPolicyName": cfprApVnicProfileOperQosPolicyName,
       "cfprApVnicProfilePinToGroupName": cfprApVnicProfilePinToGroupName,
       "cfprApVnicProfilePolicyLevel": cfprApVnicProfilePolicyLevel,
       "cfprApVnicProfilePolicyOwner": cfprApVnicProfilePolicyOwner,
       "cfprApVnicProfilePortProfileUuid": cfprApVnicProfilePortProfileUuid,
       "cfprApVnicProfilePrimaryVlanId": cfprApVnicProfilePrimaryVlanId,
       "cfprApVnicProfileQosPolicyDn": cfprApVnicProfileQosPolicyDn,
       "cfprApVnicProfileQosPolicyId": cfprApVnicProfileQosPolicyId,
       "cfprApVnicProfileQosPolicyName": cfprApVnicProfileQosPolicyName,
       "cfprApVnicProfileSwABorderAggrPort": cfprApVnicProfileSwABorderAggrPort,
       "cfprApVnicProfileSwABorderPort": cfprApVnicProfileSwABorderPort,
       "cfprApVnicProfileSwABorderSlot": cfprApVnicProfileSwABorderSlot,
       "cfprApVnicProfileSwBBorderAggrPort": cfprApVnicProfileSwBBorderAggrPort,
       "cfprApVnicProfileSwBBorderPort": cfprApVnicProfileSwBBorderPort,
       "cfprApVnicProfileSwBBorderSlot": cfprApVnicProfileSwBBorderSlot,
       "cfprApVnicProfileType": cfprApVnicProfileType,
       "cfprApVnicProfileUplinkFailAction": cfprApVnicProfileUplinkFailAction,
       "cfprApVnicProfileAliasTable": cfprApVnicProfileAliasTable,
       "cfprApVnicProfileAliasEntry": cfprApVnicProfileAliasEntry,
       "cfprApVnicProfileAliasInstanceId": cfprApVnicProfileAliasInstanceId,
       "cfprApVnicProfileAliasDn": cfprApVnicProfileAliasDn,
       "cfprApVnicProfileAliasRn": cfprApVnicProfileAliasRn,
       "cfprApVnicProfileAliasAlias": cfprApVnicProfileAliasAlias,
       "cfprApVnicProfileAliasSwUuid": cfprApVnicProfileAliasSwUuid,
       "cfprApVnicProfileRefTable": cfprApVnicProfileRefTable,
       "cfprApVnicProfileRefEntry": cfprApVnicProfileRefEntry,
       "cfprApVnicProfileRefInstanceId": cfprApVnicProfileRefInstanceId,
       "cfprApVnicProfileRefDn": cfprApVnicProfileRefDn,
       "cfprApVnicProfileRefRn": cfprApVnicProfileRefRn,
       "cfprApVnicProfileRefName": cfprApVnicProfileRefName,
       "cfprApVnicProfileRefSourceDn": cfprApVnicProfileRefSourceDn,
       "cfprApVnicProfileSetTable": cfprApVnicProfileSetTable,
       "cfprApVnicProfileSetEntry": cfprApVnicProfileSetEntry,
       "cfprApVnicProfileSetInstanceId": cfprApVnicProfileSetInstanceId,
       "cfprApVnicProfileSetDn": cfprApVnicProfileSetDn,
       "cfprApVnicProfileSetRn": cfprApVnicProfileSetRn,
       "cfprApVnicProfileSetFltAggr": cfprApVnicProfileSetFltAggr,
       "cfprApVnicProfileSetGenNum": cfprApVnicProfileSetGenNum,
       "cfprApVnicRackServerDiscoveryProfileTable": cfprApVnicRackServerDiscoveryProfileTable,
       "cfprApVnicRackServerDiscoveryProfileEntry": cfprApVnicRackServerDiscoveryProfileEntry,
       "cfprApVnicRackServerDiscoveryProfileInstanceId": cfprApVnicRackServerDiscoveryProfileInstanceId,
       "cfprApVnicRackServerDiscoveryProfileDn": cfprApVnicRackServerDiscoveryProfileDn,
       "cfprApVnicRackServerDiscoveryProfileRn": cfprApVnicRackServerDiscoveryProfileRn,
       "cfprApVnicRackServerDiscoveryProfileDescr": cfprApVnicRackServerDiscoveryProfileDescr,
       "cfprApVnicRackServerDiscoveryProfileIntId": cfprApVnicRackServerDiscoveryProfileIntId,
       "cfprApVnicRackServerDiscoveryProfileMaxPorts": cfprApVnicRackServerDiscoveryProfileMaxPorts,
       "cfprApVnicRackServerDiscoveryProfileName": cfprApVnicRackServerDiscoveryProfileName,
       "cfprApVnicRackServerDiscoveryProfilePolicyLevel": cfprApVnicRackServerDiscoveryProfilePolicyLevel,
       "cfprApVnicRackServerDiscoveryProfilePolicyOwner": cfprApVnicRackServerDiscoveryProfilePolicyOwner,
       "cfprApVnicSanConnTemplTable": cfprApVnicSanConnTemplTable,
       "cfprApVnicSanConnTemplEntry": cfprApVnicSanConnTemplEntry,
       "cfprApVnicSanConnTemplInstanceId": cfprApVnicSanConnTemplInstanceId,
       "cfprApVnicSanConnTemplDn": cfprApVnicSanConnTemplDn,
       "cfprApVnicSanConnTemplRn": cfprApVnicSanConnTemplRn,
       "cfprApVnicSanConnTemplDescr": cfprApVnicSanConnTemplDescr,
       "cfprApVnicSanConnTemplIdentPoolName": cfprApVnicSanConnTemplIdentPoolName,
       "cfprApVnicSanConnTemplIntId": cfprApVnicSanConnTemplIntId,
       "cfprApVnicSanConnTemplMaxDataFieldSize": cfprApVnicSanConnTemplMaxDataFieldSize,
       "cfprApVnicSanConnTemplName": cfprApVnicSanConnTemplName,
       "cfprApVnicSanConnTemplNwCtrlPolicyName": cfprApVnicSanConnTemplNwCtrlPolicyName,
       "cfprApVnicSanConnTemplOperIdentPoolName": cfprApVnicSanConnTemplOperIdentPoolName,
       "cfprApVnicSanConnTemplOperQosPolicyName": cfprApVnicSanConnTemplOperQosPolicyName,
       "cfprApVnicSanConnTemplOperStatsPolicyName": cfprApVnicSanConnTemplOperStatsPolicyName,
       "cfprApVnicSanConnTemplPinToGroupName": cfprApVnicSanConnTemplPinToGroupName,
       "cfprApVnicSanConnTemplPolicyLevel": cfprApVnicSanConnTemplPolicyLevel,
       "cfprApVnicSanConnTemplPolicyOwner": cfprApVnicSanConnTemplPolicyOwner,
       "cfprApVnicSanConnTemplQosPolicyName": cfprApVnicSanConnTemplQosPolicyName,
       "cfprApVnicSanConnTemplStatsPolicyName": cfprApVnicSanConnTemplStatsPolicyName,
       "cfprApVnicSanConnTemplSwitchId": cfprApVnicSanConnTemplSwitchId,
       "cfprApVnicSanConnTemplTarget": cfprApVnicSanConnTemplTarget,
       "cfprApVnicSanConnTemplTemplType": cfprApVnicSanConnTemplTemplType,
       "cfprApVnicScsiTable": cfprApVnicScsiTable,
       "cfprApVnicScsiEntry": cfprApVnicScsiEntry,
       "cfprApVnicScsiInstanceId": cfprApVnicScsiInstanceId,
       "cfprApVnicScsiDn": cfprApVnicScsiDn,
       "cfprApVnicScsiRn": cfprApVnicScsiRn,
       "cfprApVnicScsiAdaptorProfileName": cfprApVnicScsiAdaptorProfileName,
       "cfprApVnicScsiAdminHostPort": cfprApVnicScsiAdminHostPort,
       "cfprApVnicScsiAdminVcon": cfprApVnicScsiAdminVcon,
       "cfprApVnicScsiAppRole": cfprApVnicScsiAppRole,
       "cfprApVnicScsiBootDev": cfprApVnicScsiBootDev,
       "cfprApVnicScsiConfigQualifier": cfprApVnicScsiConfigQualifier,
       "cfprApVnicScsiConfigState": cfprApVnicScsiConfigState,
       "cfprApVnicScsiEquipmentDn": cfprApVnicScsiEquipmentDn,
       "cfprApVnicScsiIdentPoolName": cfprApVnicScsiIdentPoolName,
       "cfprApVnicScsiInstType": cfprApVnicScsiInstType,
       "cfprApVnicScsiName": cfprApVnicScsiName,
       "cfprApVnicScsiNwTemplName": cfprApVnicScsiNwTemplName,
       "cfprApVnicScsiOperHostPort": cfprApVnicScsiOperHostPort,
       "cfprApVnicScsiOperOrder": cfprApVnicScsiOperOrder,
       "cfprApVnicScsiOperSpeed": cfprApVnicScsiOperSpeed,
       "cfprApVnicScsiOperStatsPolicyName": cfprApVnicScsiOperStatsPolicyName,
       "cfprApVnicScsiOperVcon": cfprApVnicScsiOperVcon,
       "cfprApVnicScsiOrder": cfprApVnicScsiOrder,
       "cfprApVnicScsiOwner": cfprApVnicScsiOwner,
       "cfprApVnicScsiPinToGroupName": cfprApVnicScsiPinToGroupName,
       "cfprApVnicScsiQosPolicyName": cfprApVnicScsiQosPolicyName,
       "cfprApVnicScsiStatsPolicyName": cfprApVnicScsiStatsPolicyName,
       "cfprApVnicScsiSwitchId": cfprApVnicScsiSwitchId,
       "cfprApVnicScsiType": cfprApVnicScsiType,
       "cfprApVnicScsiIfTable": cfprApVnicScsiIfTable,
       "cfprApVnicScsiIfEntry": cfprApVnicScsiIfEntry,
       "cfprApVnicScsiIfInstanceId": cfprApVnicScsiIfInstanceId,
       "cfprApVnicScsiIfDn": cfprApVnicScsiIfDn,
       "cfprApVnicScsiIfRn": cfprApVnicScsiIfRn,
       "cfprApVnicScsiIfAddr": cfprApVnicScsiIfAddr,
       "cfprApVnicScsiIfConfigQualifier": cfprApVnicScsiIfConfigQualifier,
       "cfprApVnicScsiIfName": cfprApVnicScsiIfName,
       "cfprApVnicScsiIfOperState": cfprApVnicScsiIfOperState,
       "cfprApVnicScsiIfOperVnetDn": cfprApVnicScsiIfOperVnetDn,
       "cfprApVnicScsiIfOperVnetName": cfprApVnicScsiIfOperVnetName,
       "cfprApVnicScsiIfOwner": cfprApVnicScsiIfOwner,
       "cfprApVnicScsiIfPubNwId": cfprApVnicScsiIfPubNwId,
       "cfprApVnicScsiIfSharing": cfprApVnicScsiIfSharing,
       "cfprApVnicScsiIfSwitchId": cfprApVnicScsiIfSwitchId,
       "cfprApVnicScsiIfType": cfprApVnicScsiIfType,
       "cfprApVnicScsiIfVnet": cfprApVnicScsiIfVnet,
       "cfprApVnicUsnicConPolicyTable": cfprApVnicUsnicConPolicyTable,
       "cfprApVnicUsnicConPolicyEntry": cfprApVnicUsnicConPolicyEntry,
       "cfprApVnicUsnicConPolicyInstanceId": cfprApVnicUsnicConPolicyInstanceId,
       "cfprApVnicUsnicConPolicyDn": cfprApVnicUsnicConPolicyDn,
       "cfprApVnicUsnicConPolicyRn": cfprApVnicUsnicConPolicyRn,
       "cfprApVnicUsnicConPolicyAdaptorProfileName": cfprApVnicUsnicConPolicyAdaptorProfileName,
       "cfprApVnicUsnicConPolicyDescr": cfprApVnicUsnicConPolicyDescr,
       "cfprApVnicUsnicConPolicyIntId": cfprApVnicUsnicConPolicyIntId,
       "cfprApVnicUsnicConPolicyName": cfprApVnicUsnicConPolicyName,
       "cfprApVnicUsnicConPolicyPolicyLevel": cfprApVnicUsnicConPolicyPolicyLevel,
       "cfprApVnicUsnicConPolicyPolicyOwner": cfprApVnicUsnicConPolicyPolicyOwner,
       "cfprApVnicUsnicConPolicyUsnicCount": cfprApVnicUsnicConPolicyUsnicCount,
       "cfprApVnicUsnicConPolicyRefTable": cfprApVnicUsnicConPolicyRefTable,
       "cfprApVnicUsnicConPolicyRefEntry": cfprApVnicUsnicConPolicyRefEntry,
       "cfprApVnicUsnicConPolicyRefInstanceId": cfprApVnicUsnicConPolicyRefInstanceId,
       "cfprApVnicUsnicConPolicyRefDn": cfprApVnicUsnicConPolicyRefDn,
       "cfprApVnicUsnicConPolicyRefRn": cfprApVnicUsnicConPolicyRefRn,
       "cfprApVnicUsnicConPolicyRefConPolicyName": cfprApVnicUsnicConPolicyRefConPolicyName,
       "cfprApVnicUsnicConPolicyRefOperConPolicyName": cfprApVnicUsnicConPolicyRefOperConPolicyName,
       "cfprApVnicVhbaBehPolicyTable": cfprApVnicVhbaBehPolicyTable,
       "cfprApVnicVhbaBehPolicyEntry": cfprApVnicVhbaBehPolicyEntry,
       "cfprApVnicVhbaBehPolicyInstanceId": cfprApVnicVhbaBehPolicyInstanceId,
       "cfprApVnicVhbaBehPolicyDn": cfprApVnicVhbaBehPolicyDn,
       "cfprApVnicVhbaBehPolicyRn": cfprApVnicVhbaBehPolicyRn,
       "cfprApVnicVhbaBehPolicyAction": cfprApVnicVhbaBehPolicyAction,
       "cfprApVnicVhbaBehPolicyDescr": cfprApVnicVhbaBehPolicyDescr,
       "cfprApVnicVhbaBehPolicyIntId": cfprApVnicVhbaBehPolicyIntId,
       "cfprApVnicVhbaBehPolicyName": cfprApVnicVhbaBehPolicyName,
       "cfprApVnicVhbaBehPolicyNwTemplName": cfprApVnicVhbaBehPolicyNwTemplName,
       "cfprApVnicVhbaBehPolicyPolicyLevel": cfprApVnicVhbaBehPolicyPolicyLevel,
       "cfprApVnicVhbaBehPolicyPolicyOwner": cfprApVnicVhbaBehPolicyPolicyOwner,
       "cfprApVnicVhbaBehPolicyType": cfprApVnicVhbaBehPolicyType,
       "cfprApVnicVlanTable": cfprApVnicVlanTable,
       "cfprApVnicVlanEntry": cfprApVnicVlanEntry,
       "cfprApVnicVlanInstanceId": cfprApVnicVlanInstanceId,
       "cfprApVnicVlanDn": cfprApVnicVlanDn,
       "cfprApVnicVlanRn": cfprApVnicVlanRn,
       "cfprApVnicVlanConfigQualifier": cfprApVnicVlanConfigQualifier,
       "cfprApVnicVlanFltAggr": cfprApVnicVlanFltAggr,
       "cfprApVnicVlanName": cfprApVnicVlanName,
       "cfprApVnicVlanOperState": cfprApVnicVlanOperState,
       "cfprApVnicVlanOperVnetDn": cfprApVnicVlanOperVnetDn,
       "cfprApVnicVlanOperVnetName": cfprApVnicVlanOperVnetName,
       "cfprApVnicVlanOwner": cfprApVnicVlanOwner,
       "cfprApVnicVlanPubNwId": cfprApVnicVlanPubNwId,
       "cfprApVnicVlanSharing": cfprApVnicVlanSharing,
       "cfprApVnicVlanSwitchId": cfprApVnicVlanSwitchId,
       "cfprApVnicVlanType": cfprApVnicVlanType,
       "cfprApVnicVlanVlanName": cfprApVnicVlanVlanName,
       "cfprApVnicVlanVnet": cfprApVnicVlanVnet,
       "cfprApVnicVmqConPolicyTable": cfprApVnicVmqConPolicyTable,
       "cfprApVnicVmqConPolicyEntry": cfprApVnicVmqConPolicyEntry,
       "cfprApVnicVmqConPolicyInstanceId": cfprApVnicVmqConPolicyInstanceId,
       "cfprApVnicVmqConPolicyDn": cfprApVnicVmqConPolicyDn,
       "cfprApVnicVmqConPolicyRn": cfprApVnicVmqConPolicyRn,
       "cfprApVnicVmqConPolicyDescr": cfprApVnicVmqConPolicyDescr,
       "cfprApVnicVmqConPolicyIntId": cfprApVnicVmqConPolicyIntId,
       "cfprApVnicVmqConPolicyIntrCount": cfprApVnicVmqConPolicyIntrCount,
       "cfprApVnicVmqConPolicyName": cfprApVnicVmqConPolicyName,
       "cfprApVnicVmqConPolicyPolicyLevel": cfprApVnicVmqConPolicyPolicyLevel,
       "cfprApVnicVmqConPolicyPolicyOwner": cfprApVnicVmqConPolicyPolicyOwner,
       "cfprApVnicVmqConPolicyVmqCount": cfprApVnicVmqConPolicyVmqCount,
       "cfprApVnicVmqConPolicyRefTable": cfprApVnicVmqConPolicyRefTable,
       "cfprApVnicVmqConPolicyRefEntry": cfprApVnicVmqConPolicyRefEntry,
       "cfprApVnicVmqConPolicyRefInstanceId": cfprApVnicVmqConPolicyRefInstanceId,
       "cfprApVnicVmqConPolicyRefDn": cfprApVnicVmqConPolicyRefDn,
       "cfprApVnicVmqConPolicyRefRn": cfprApVnicVmqConPolicyRefRn,
       "cfprApVnicVmqConPolicyRefConPolicyName": cfprApVnicVmqConPolicyRefConPolicyName,
       "cfprApVnicVmqConPolicyRefOperConPolicyName": cfprApVnicVmqConPolicyRefOperConPolicyName,
       "cfprApVnicVnicBehPolicyTable": cfprApVnicVnicBehPolicyTable,
       "cfprApVnicVnicBehPolicyEntry": cfprApVnicVnicBehPolicyEntry,
       "cfprApVnicVnicBehPolicyInstanceId": cfprApVnicVnicBehPolicyInstanceId,
       "cfprApVnicVnicBehPolicyDn": cfprApVnicVnicBehPolicyDn,
       "cfprApVnicVnicBehPolicyRn": cfprApVnicVnicBehPolicyRn,
       "cfprApVnicVnicBehPolicyAction": cfprApVnicVnicBehPolicyAction,
       "cfprApVnicVnicBehPolicyDescr": cfprApVnicVnicBehPolicyDescr,
       "cfprApVnicVnicBehPolicyIntId": cfprApVnicVnicBehPolicyIntId,
       "cfprApVnicVnicBehPolicyName": cfprApVnicVnicBehPolicyName,
       "cfprApVnicVnicBehPolicyNwTemplName": cfprApVnicVnicBehPolicyNwTemplName,
       "cfprApVnicVnicBehPolicyPolicyLevel": cfprApVnicVnicBehPolicyPolicyLevel,
       "cfprApVnicVnicBehPolicyPolicyOwner": cfprApVnicVnicBehPolicyPolicyOwner,
       "cfprApVnicVnicBehPolicyType": cfprApVnicVnicBehPolicyType,
       "cfprApVnicWwpnHistoryTable": cfprApVnicWwpnHistoryTable,
       "cfprApVnicWwpnHistoryEntry": cfprApVnicWwpnHistoryEntry,
       "cfprApVnicWwpnHistoryInstanceId": cfprApVnicWwpnHistoryInstanceId,
       "cfprApVnicWwpnHistoryDn": cfprApVnicWwpnHistoryDn,
       "cfprApVnicWwpnHistoryRn": cfprApVnicWwpnHistoryRn,
       "cfprApVnicWwpnHistoryOldaddr": cfprApVnicWwpnHistoryOldaddr}
)
