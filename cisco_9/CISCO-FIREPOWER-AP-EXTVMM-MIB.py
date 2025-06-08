# SNMP MIB module (CISCO-FIREPOWER-AP-EXTVMM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-EXTVMM-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:16:53 2025
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

(CfprApCommFilePathProtocol,
 CfprApExtvmmFabricNetworkType,
 CfprApExtvmmNetworkSetConfigQualifier,
 CfprApExtvmmProviderVendorType,
 CfprApExtvmmRefOperState,
 CfprApExtvmmVcVersion,
 CfprApExtvmmVnicType,
 CfprApPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApCommFilePathProtocol",
    "CfprApExtvmmFabricNetworkType",
    "CfprApExtvmmNetworkSetConfigQualifier",
    "CfprApExtvmmProviderVendorType",
    "CfprApExtvmmRefOperState",
    "CfprApExtvmmVcVersion",
    "CfprApExtvmmVnicType",
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

cfprApExtvmmObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApExtvmmEpTable_Object = MibTable
cfprApExtvmmEpTable = _CfprApExtvmmEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 1)
)
if mibBuilder.loadTexts:
    cfprApExtvmmEpTable.setStatus("current")
_CfprApExtvmmEpEntry_Object = MibTableRow
cfprApExtvmmEpEntry = _CfprApExtvmmEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 1, 1)
)
cfprApExtvmmEpEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTVMM-MIB", "cfprApExtvmmEpInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtvmmEpEntry.setStatus("current")
_CfprApExtvmmEpInstanceId_Type = CfprApManagedObjectId
_CfprApExtvmmEpInstanceId_Object = MibTableColumn
cfprApExtvmmEpInstanceId = _CfprApExtvmmEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 1, 1, 1),
    _CfprApExtvmmEpInstanceId_Type()
)
cfprApExtvmmEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtvmmEpInstanceId.setStatus("current")
_CfprApExtvmmEpDn_Type = CfprApManagedObjectDn
_CfprApExtvmmEpDn_Object = MibTableColumn
cfprApExtvmmEpDn = _CfprApExtvmmEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 1, 1, 2),
    _CfprApExtvmmEpDn_Type()
)
cfprApExtvmmEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmEpDn.setStatus("current")
_CfprApExtvmmEpRn_Type = SnmpAdminString
_CfprApExtvmmEpRn_Object = MibTableColumn
cfprApExtvmmEpRn = _CfprApExtvmmEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 1, 1, 3),
    _CfprApExtvmmEpRn_Type()
)
cfprApExtvmmEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmEpRn.setStatus("current")
_CfprApExtvmmEpGenNum_Type = Gauge32
_CfprApExtvmmEpGenNum_Object = MibTableColumn
cfprApExtvmmEpGenNum = _CfprApExtvmmEpGenNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 1, 1, 4),
    _CfprApExtvmmEpGenNum_Type()
)
cfprApExtvmmEpGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmEpGenNum.setStatus("current")
_CfprApExtvmmFNDReferenceTable_Object = MibTable
cfprApExtvmmFNDReferenceTable = _CfprApExtvmmFNDReferenceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 2)
)
if mibBuilder.loadTexts:
    cfprApExtvmmFNDReferenceTable.setStatus("current")
_CfprApExtvmmFNDReferenceEntry_Object = MibTableRow
cfprApExtvmmFNDReferenceEntry = _CfprApExtvmmFNDReferenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 2, 1)
)
cfprApExtvmmFNDReferenceEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTVMM-MIB", "cfprApExtvmmFNDReferenceInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtvmmFNDReferenceEntry.setStatus("current")
_CfprApExtvmmFNDReferenceInstanceId_Type = CfprApManagedObjectId
_CfprApExtvmmFNDReferenceInstanceId_Object = MibTableColumn
cfprApExtvmmFNDReferenceInstanceId = _CfprApExtvmmFNDReferenceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 2, 1, 1),
    _CfprApExtvmmFNDReferenceInstanceId_Type()
)
cfprApExtvmmFNDReferenceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtvmmFNDReferenceInstanceId.setStatus("current")
_CfprApExtvmmFNDReferenceDn_Type = CfprApManagedObjectDn
_CfprApExtvmmFNDReferenceDn_Object = MibTableColumn
cfprApExtvmmFNDReferenceDn = _CfprApExtvmmFNDReferenceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 2, 1, 2),
    _CfprApExtvmmFNDReferenceDn_Type()
)
cfprApExtvmmFNDReferenceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmFNDReferenceDn.setStatus("current")
_CfprApExtvmmFNDReferenceRn_Type = SnmpAdminString
_CfprApExtvmmFNDReferenceRn_Object = MibTableColumn
cfprApExtvmmFNDReferenceRn = _CfprApExtvmmFNDReferenceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 2, 1, 3),
    _CfprApExtvmmFNDReferenceRn_Type()
)
cfprApExtvmmFNDReferenceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmFNDReferenceRn.setStatus("current")
_CfprApExtvmmFNDReferenceDescr_Type = SnmpAdminString
_CfprApExtvmmFNDReferenceDescr_Object = MibTableColumn
cfprApExtvmmFNDReferenceDescr = _CfprApExtvmmFNDReferenceDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 2, 1, 4),
    _CfprApExtvmmFNDReferenceDescr_Type()
)
cfprApExtvmmFNDReferenceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmFNDReferenceDescr.setStatus("current")
_CfprApExtvmmFNDReferenceFnDefName_Type = SnmpAdminString
_CfprApExtvmmFNDReferenceFnDefName_Object = MibTableColumn
cfprApExtvmmFNDReferenceFnDefName = _CfprApExtvmmFNDReferenceFnDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 2, 1, 5),
    _CfprApExtvmmFNDReferenceFnDefName_Type()
)
cfprApExtvmmFNDReferenceFnDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmFNDReferenceFnDefName.setStatus("current")
_CfprApExtvmmFNDReferenceIntId_Type = SnmpAdminString
_CfprApExtvmmFNDReferenceIntId_Object = MibTableColumn
cfprApExtvmmFNDReferenceIntId = _CfprApExtvmmFNDReferenceIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 2, 1, 6),
    _CfprApExtvmmFNDReferenceIntId_Type()
)
cfprApExtvmmFNDReferenceIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmFNDReferenceIntId.setStatus("current")
_CfprApExtvmmFNDReferenceName_Type = SnmpAdminString
_CfprApExtvmmFNDReferenceName_Object = MibTableColumn
cfprApExtvmmFNDReferenceName = _CfprApExtvmmFNDReferenceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 2, 1, 7),
    _CfprApExtvmmFNDReferenceName_Type()
)
cfprApExtvmmFNDReferenceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmFNDReferenceName.setStatus("current")
_CfprApExtvmmFNDReferenceOperFnDefName_Type = SnmpAdminString
_CfprApExtvmmFNDReferenceOperFnDefName_Object = MibTableColumn
cfprApExtvmmFNDReferenceOperFnDefName = _CfprApExtvmmFNDReferenceOperFnDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 2, 1, 8),
    _CfprApExtvmmFNDReferenceOperFnDefName_Type()
)
cfprApExtvmmFNDReferenceOperFnDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmFNDReferenceOperFnDefName.setStatus("current")
_CfprApExtvmmFNDReferencePolicyLevel_Type = Gauge32
_CfprApExtvmmFNDReferencePolicyLevel_Object = MibTableColumn
cfprApExtvmmFNDReferencePolicyLevel = _CfprApExtvmmFNDReferencePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 2, 1, 9),
    _CfprApExtvmmFNDReferencePolicyLevel_Type()
)
cfprApExtvmmFNDReferencePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmFNDReferencePolicyLevel.setStatus("current")
_CfprApExtvmmFNDReferencePolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApExtvmmFNDReferencePolicyOwner_Object = MibTableColumn
cfprApExtvmmFNDReferencePolicyOwner = _CfprApExtvmmFNDReferencePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 2, 1, 10),
    _CfprApExtvmmFNDReferencePolicyOwner_Type()
)
cfprApExtvmmFNDReferencePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmFNDReferencePolicyOwner.setStatus("current")
_CfprApExtvmmFabricNetworkTable_Object = MibTable
cfprApExtvmmFabricNetworkTable = _CfprApExtvmmFabricNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 3)
)
if mibBuilder.loadTexts:
    cfprApExtvmmFabricNetworkTable.setStatus("current")
_CfprApExtvmmFabricNetworkEntry_Object = MibTableRow
cfprApExtvmmFabricNetworkEntry = _CfprApExtvmmFabricNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 3, 1)
)
cfprApExtvmmFabricNetworkEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTVMM-MIB", "cfprApExtvmmFabricNetworkInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtvmmFabricNetworkEntry.setStatus("current")
_CfprApExtvmmFabricNetworkInstanceId_Type = CfprApManagedObjectId
_CfprApExtvmmFabricNetworkInstanceId_Object = MibTableColumn
cfprApExtvmmFabricNetworkInstanceId = _CfprApExtvmmFabricNetworkInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 3, 1, 1),
    _CfprApExtvmmFabricNetworkInstanceId_Type()
)
cfprApExtvmmFabricNetworkInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtvmmFabricNetworkInstanceId.setStatus("current")
_CfprApExtvmmFabricNetworkDn_Type = CfprApManagedObjectDn
_CfprApExtvmmFabricNetworkDn_Object = MibTableColumn
cfprApExtvmmFabricNetworkDn = _CfprApExtvmmFabricNetworkDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 3, 1, 2),
    _CfprApExtvmmFabricNetworkDn_Type()
)
cfprApExtvmmFabricNetworkDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmFabricNetworkDn.setStatus("current")
_CfprApExtvmmFabricNetworkRn_Type = SnmpAdminString
_CfprApExtvmmFabricNetworkRn_Object = MibTableColumn
cfprApExtvmmFabricNetworkRn = _CfprApExtvmmFabricNetworkRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 3, 1, 3),
    _CfprApExtvmmFabricNetworkRn_Type()
)
cfprApExtvmmFabricNetworkRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmFabricNetworkRn.setStatus("current")
_CfprApExtvmmFabricNetworkDescr_Type = SnmpAdminString
_CfprApExtvmmFabricNetworkDescr_Object = MibTableColumn
cfprApExtvmmFabricNetworkDescr = _CfprApExtvmmFabricNetworkDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 3, 1, 4),
    _CfprApExtvmmFabricNetworkDescr_Type()
)
cfprApExtvmmFabricNetworkDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmFabricNetworkDescr.setStatus("current")
_CfprApExtvmmFabricNetworkGuid_Type = SnmpAdminString
_CfprApExtvmmFabricNetworkGuid_Object = MibTableColumn
cfprApExtvmmFabricNetworkGuid = _CfprApExtvmmFabricNetworkGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 3, 1, 5),
    _CfprApExtvmmFabricNetworkGuid_Type()
)
cfprApExtvmmFabricNetworkGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmFabricNetworkGuid.setStatus("current")
_CfprApExtvmmFabricNetworkIntId_Type = SnmpAdminString
_CfprApExtvmmFabricNetworkIntId_Object = MibTableColumn
cfprApExtvmmFabricNetworkIntId = _CfprApExtvmmFabricNetworkIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 3, 1, 6),
    _CfprApExtvmmFabricNetworkIntId_Type()
)
cfprApExtvmmFabricNetworkIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmFabricNetworkIntId.setStatus("current")
_CfprApExtvmmFabricNetworkName_Type = SnmpAdminString
_CfprApExtvmmFabricNetworkName_Object = MibTableColumn
cfprApExtvmmFabricNetworkName = _CfprApExtvmmFabricNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 3, 1, 7),
    _CfprApExtvmmFabricNetworkName_Type()
)
cfprApExtvmmFabricNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmFabricNetworkName.setStatus("current")
_CfprApExtvmmFabricNetworkNetworkType_Type = CfprApExtvmmFabricNetworkType
_CfprApExtvmmFabricNetworkNetworkType_Object = MibTableColumn
cfprApExtvmmFabricNetworkNetworkType = _CfprApExtvmmFabricNetworkNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 3, 1, 8),
    _CfprApExtvmmFabricNetworkNetworkType_Type()
)
cfprApExtvmmFabricNetworkNetworkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmFabricNetworkNetworkType.setStatus("current")
_CfprApExtvmmFabricNetworkPolicyLevel_Type = Gauge32
_CfprApExtvmmFabricNetworkPolicyLevel_Object = MibTableColumn
cfprApExtvmmFabricNetworkPolicyLevel = _CfprApExtvmmFabricNetworkPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 3, 1, 9),
    _CfprApExtvmmFabricNetworkPolicyLevel_Type()
)
cfprApExtvmmFabricNetworkPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmFabricNetworkPolicyLevel.setStatus("current")
_CfprApExtvmmFabricNetworkPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApExtvmmFabricNetworkPolicyOwner_Object = MibTableColumn
cfprApExtvmmFabricNetworkPolicyOwner = _CfprApExtvmmFabricNetworkPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 3, 1, 10),
    _CfprApExtvmmFabricNetworkPolicyOwner_Type()
)
cfprApExtvmmFabricNetworkPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmFabricNetworkPolicyOwner.setStatus("current")
_CfprApExtvmmFabricNetworkRefOperState_Type = CfprApExtvmmRefOperState
_CfprApExtvmmFabricNetworkRefOperState_Object = MibTableColumn
cfprApExtvmmFabricNetworkRefOperState = _CfprApExtvmmFabricNetworkRefOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 3, 1, 11),
    _CfprApExtvmmFabricNetworkRefOperState_Type()
)
cfprApExtvmmFabricNetworkRefOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmFabricNetworkRefOperState.setStatus("current")
_CfprApExtvmmFabricNetworkDefinitionTable_Object = MibTable
cfprApExtvmmFabricNetworkDefinitionTable = _CfprApExtvmmFabricNetworkDefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 4)
)
if mibBuilder.loadTexts:
    cfprApExtvmmFabricNetworkDefinitionTable.setStatus("current")
_CfprApExtvmmFabricNetworkDefinitionEntry_Object = MibTableRow
cfprApExtvmmFabricNetworkDefinitionEntry = _CfprApExtvmmFabricNetworkDefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 4, 1)
)
cfprApExtvmmFabricNetworkDefinitionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTVMM-MIB", "cfprApExtvmmFabricNetworkDefinitionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtvmmFabricNetworkDefinitionEntry.setStatus("current")
_CfprApExtvmmFabricNetworkDefinitionInstanceId_Type = CfprApManagedObjectId
_CfprApExtvmmFabricNetworkDefinitionInstanceId_Object = MibTableColumn
cfprApExtvmmFabricNetworkDefinitionInstanceId = _CfprApExtvmmFabricNetworkDefinitionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 4, 1, 1),
    _CfprApExtvmmFabricNetworkDefinitionInstanceId_Type()
)
cfprApExtvmmFabricNetworkDefinitionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtvmmFabricNetworkDefinitionInstanceId.setStatus("current")
_CfprApExtvmmFabricNetworkDefinitionDn_Type = CfprApManagedObjectDn
_CfprApExtvmmFabricNetworkDefinitionDn_Object = MibTableColumn
cfprApExtvmmFabricNetworkDefinitionDn = _CfprApExtvmmFabricNetworkDefinitionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 4, 1, 2),
    _CfprApExtvmmFabricNetworkDefinitionDn_Type()
)
cfprApExtvmmFabricNetworkDefinitionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmFabricNetworkDefinitionDn.setStatus("current")
_CfprApExtvmmFabricNetworkDefinitionRn_Type = SnmpAdminString
_CfprApExtvmmFabricNetworkDefinitionRn_Object = MibTableColumn
cfprApExtvmmFabricNetworkDefinitionRn = _CfprApExtvmmFabricNetworkDefinitionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 4, 1, 3),
    _CfprApExtvmmFabricNetworkDefinitionRn_Type()
)
cfprApExtvmmFabricNetworkDefinitionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmFabricNetworkDefinitionRn.setStatus("current")
_CfprApExtvmmFabricNetworkDefinitionAllowedVnicType_Type = CfprApExtvmmVnicType
_CfprApExtvmmFabricNetworkDefinitionAllowedVnicType_Object = MibTableColumn
cfprApExtvmmFabricNetworkDefinitionAllowedVnicType = _CfprApExtvmmFabricNetworkDefinitionAllowedVnicType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 4, 1, 4),
    _CfprApExtvmmFabricNetworkDefinitionAllowedVnicType_Type()
)
cfprApExtvmmFabricNetworkDefinitionAllowedVnicType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmFabricNetworkDefinitionAllowedVnicType.setStatus("current")
_CfprApExtvmmFabricNetworkDefinitionDescr_Type = SnmpAdminString
_CfprApExtvmmFabricNetworkDefinitionDescr_Object = MibTableColumn
cfprApExtvmmFabricNetworkDefinitionDescr = _CfprApExtvmmFabricNetworkDefinitionDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 4, 1, 5),
    _CfprApExtvmmFabricNetworkDefinitionDescr_Type()
)
cfprApExtvmmFabricNetworkDefinitionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmFabricNetworkDefinitionDescr.setStatus("current")
_CfprApExtvmmFabricNetworkDefinitionGuid_Type = SnmpAdminString
_CfprApExtvmmFabricNetworkDefinitionGuid_Object = MibTableColumn
cfprApExtvmmFabricNetworkDefinitionGuid = _CfprApExtvmmFabricNetworkDefinitionGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 4, 1, 6),
    _CfprApExtvmmFabricNetworkDefinitionGuid_Type()
)
cfprApExtvmmFabricNetworkDefinitionGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmFabricNetworkDefinitionGuid.setStatus("current")
_CfprApExtvmmFabricNetworkDefinitionIntId_Type = SnmpAdminString
_CfprApExtvmmFabricNetworkDefinitionIntId_Object = MibTableColumn
cfprApExtvmmFabricNetworkDefinitionIntId = _CfprApExtvmmFabricNetworkDefinitionIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 4, 1, 7),
    _CfprApExtvmmFabricNetworkDefinitionIntId_Type()
)
cfprApExtvmmFabricNetworkDefinitionIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmFabricNetworkDefinitionIntId.setStatus("current")
_CfprApExtvmmFabricNetworkDefinitionName_Type = SnmpAdminString
_CfprApExtvmmFabricNetworkDefinitionName_Object = MibTableColumn
cfprApExtvmmFabricNetworkDefinitionName = _CfprApExtvmmFabricNetworkDefinitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 4, 1, 8),
    _CfprApExtvmmFabricNetworkDefinitionName_Type()
)
cfprApExtvmmFabricNetworkDefinitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmFabricNetworkDefinitionName.setStatus("current")
_CfprApExtvmmFabricNetworkDefinitionPolicyLevel_Type = Gauge32
_CfprApExtvmmFabricNetworkDefinitionPolicyLevel_Object = MibTableColumn
cfprApExtvmmFabricNetworkDefinitionPolicyLevel = _CfprApExtvmmFabricNetworkDefinitionPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 4, 1, 9),
    _CfprApExtvmmFabricNetworkDefinitionPolicyLevel_Type()
)
cfprApExtvmmFabricNetworkDefinitionPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmFabricNetworkDefinitionPolicyLevel.setStatus("current")
_CfprApExtvmmFabricNetworkDefinitionPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApExtvmmFabricNetworkDefinitionPolicyOwner_Object = MibTableColumn
cfprApExtvmmFabricNetworkDefinitionPolicyOwner = _CfprApExtvmmFabricNetworkDefinitionPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 4, 1, 10),
    _CfprApExtvmmFabricNetworkDefinitionPolicyOwner_Type()
)
cfprApExtvmmFabricNetworkDefinitionPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmFabricNetworkDefinitionPolicyOwner.setStatus("current")
_CfprApExtvmmFabricNetworkDefinitionPrimaryVlanId_Type = Gauge32
_CfprApExtvmmFabricNetworkDefinitionPrimaryVlanId_Object = MibTableColumn
cfprApExtvmmFabricNetworkDefinitionPrimaryVlanId = _CfprApExtvmmFabricNetworkDefinitionPrimaryVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 4, 1, 11),
    _CfprApExtvmmFabricNetworkDefinitionPrimaryVlanId_Type()
)
cfprApExtvmmFabricNetworkDefinitionPrimaryVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmFabricNetworkDefinitionPrimaryVlanId.setStatus("current")
_CfprApExtvmmFabricNetworkDefinitionRefOperState_Type = CfprApExtvmmRefOperState
_CfprApExtvmmFabricNetworkDefinitionRefOperState_Object = MibTableColumn
cfprApExtvmmFabricNetworkDefinitionRefOperState = _CfprApExtvmmFabricNetworkDefinitionRefOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 4, 1, 12),
    _CfprApExtvmmFabricNetworkDefinitionRefOperState_Type()
)
cfprApExtvmmFabricNetworkDefinitionRefOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmFabricNetworkDefinitionRefOperState.setStatus("current")
_CfprApExtvmmKeyInstTable_Object = MibTable
cfprApExtvmmKeyInstTable = _CfprApExtvmmKeyInstTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 5)
)
if mibBuilder.loadTexts:
    cfprApExtvmmKeyInstTable.setStatus("current")
_CfprApExtvmmKeyInstEntry_Object = MibTableRow
cfprApExtvmmKeyInstEntry = _CfprApExtvmmKeyInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 5, 1)
)
cfprApExtvmmKeyInstEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTVMM-MIB", "cfprApExtvmmKeyInstInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtvmmKeyInstEntry.setStatus("current")
_CfprApExtvmmKeyInstInstanceId_Type = CfprApManagedObjectId
_CfprApExtvmmKeyInstInstanceId_Object = MibTableColumn
cfprApExtvmmKeyInstInstanceId = _CfprApExtvmmKeyInstInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 5, 1, 1),
    _CfprApExtvmmKeyInstInstanceId_Type()
)
cfprApExtvmmKeyInstInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtvmmKeyInstInstanceId.setStatus("current")
_CfprApExtvmmKeyInstDn_Type = CfprApManagedObjectDn
_CfprApExtvmmKeyInstDn_Object = MibTableColumn
cfprApExtvmmKeyInstDn = _CfprApExtvmmKeyInstDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 5, 1, 2),
    _CfprApExtvmmKeyInstDn_Type()
)
cfprApExtvmmKeyInstDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmKeyInstDn.setStatus("current")
_CfprApExtvmmKeyInstRn_Type = SnmpAdminString
_CfprApExtvmmKeyInstRn_Object = MibTableColumn
cfprApExtvmmKeyInstRn = _CfprApExtvmmKeyInstRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 5, 1, 3),
    _CfprApExtvmmKeyInstRn_Type()
)
cfprApExtvmmKeyInstRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmKeyInstRn.setStatus("current")
_CfprApExtvmmKeyInstInst_Type = Gauge32
_CfprApExtvmmKeyInstInst_Object = MibTableColumn
cfprApExtvmmKeyInstInst = _CfprApExtvmmKeyInstInst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 5, 1, 4),
    _CfprApExtvmmKeyInstInst_Type()
)
cfprApExtvmmKeyInstInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmKeyInstInst.setStatus("current")
_CfprApExtvmmKeyInstKey_Type = SnmpAdminString
_CfprApExtvmmKeyInstKey_Object = MibTableColumn
cfprApExtvmmKeyInstKey = _CfprApExtvmmKeyInstKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 5, 1, 5),
    _CfprApExtvmmKeyInstKey_Type()
)
cfprApExtvmmKeyInstKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmKeyInstKey.setStatus("current")
_CfprApExtvmmKeyRingTable_Object = MibTable
cfprApExtvmmKeyRingTable = _CfprApExtvmmKeyRingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 6)
)
if mibBuilder.loadTexts:
    cfprApExtvmmKeyRingTable.setStatus("current")
_CfprApExtvmmKeyRingEntry_Object = MibTableRow
cfprApExtvmmKeyRingEntry = _CfprApExtvmmKeyRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 6, 1)
)
cfprApExtvmmKeyRingEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTVMM-MIB", "cfprApExtvmmKeyRingInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtvmmKeyRingEntry.setStatus("current")
_CfprApExtvmmKeyRingInstanceId_Type = CfprApManagedObjectId
_CfprApExtvmmKeyRingInstanceId_Object = MibTableColumn
cfprApExtvmmKeyRingInstanceId = _CfprApExtvmmKeyRingInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 6, 1, 1),
    _CfprApExtvmmKeyRingInstanceId_Type()
)
cfprApExtvmmKeyRingInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtvmmKeyRingInstanceId.setStatus("current")
_CfprApExtvmmKeyRingDn_Type = CfprApManagedObjectDn
_CfprApExtvmmKeyRingDn_Object = MibTableColumn
cfprApExtvmmKeyRingDn = _CfprApExtvmmKeyRingDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 6, 1, 2),
    _CfprApExtvmmKeyRingDn_Type()
)
cfprApExtvmmKeyRingDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmKeyRingDn.setStatus("current")
_CfprApExtvmmKeyRingRn_Type = SnmpAdminString
_CfprApExtvmmKeyRingRn_Object = MibTableColumn
cfprApExtvmmKeyRingRn = _CfprApExtvmmKeyRingRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 6, 1, 3),
    _CfprApExtvmmKeyRingRn_Type()
)
cfprApExtvmmKeyRingRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmKeyRingRn.setStatus("current")
_CfprApExtvmmKeyRingCertFile_Type = SnmpAdminString
_CfprApExtvmmKeyRingCertFile_Object = MibTableColumn
cfprApExtvmmKeyRingCertFile = _CfprApExtvmmKeyRingCertFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 6, 1, 4),
    _CfprApExtvmmKeyRingCertFile_Type()
)
cfprApExtvmmKeyRingCertFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmKeyRingCertFile.setStatus("current")
_CfprApExtvmmKeyRingLocation_Type = CfprApCommFilePathProtocol
_CfprApExtvmmKeyRingLocation_Object = MibTableColumn
cfprApExtvmmKeyRingLocation = _CfprApExtvmmKeyRingLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 6, 1, 5),
    _CfprApExtvmmKeyRingLocation_Type()
)
cfprApExtvmmKeyRingLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmKeyRingLocation.setStatus("current")
_CfprApExtvmmKeyRingName_Type = SnmpAdminString
_CfprApExtvmmKeyRingName_Object = MibTableColumn
cfprApExtvmmKeyRingName = _CfprApExtvmmKeyRingName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 6, 1, 6),
    _CfprApExtvmmKeyRingName_Type()
)
cfprApExtvmmKeyRingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmKeyRingName.setStatus("current")
_CfprApExtvmmKeyRingPath_Type = SnmpAdminString
_CfprApExtvmmKeyRingPath_Object = MibTableColumn
cfprApExtvmmKeyRingPath = _CfprApExtvmmKeyRingPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 6, 1, 7),
    _CfprApExtvmmKeyRingPath_Type()
)
cfprApExtvmmKeyRingPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmKeyRingPath.setStatus("current")
_CfprApExtvmmKeyStoreTable_Object = MibTable
cfprApExtvmmKeyStoreTable = _CfprApExtvmmKeyStoreTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 7)
)
if mibBuilder.loadTexts:
    cfprApExtvmmKeyStoreTable.setStatus("current")
_CfprApExtvmmKeyStoreEntry_Object = MibTableRow
cfprApExtvmmKeyStoreEntry = _CfprApExtvmmKeyStoreEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 7, 1)
)
cfprApExtvmmKeyStoreEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTVMM-MIB", "cfprApExtvmmKeyStoreInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtvmmKeyStoreEntry.setStatus("current")
_CfprApExtvmmKeyStoreInstanceId_Type = CfprApManagedObjectId
_CfprApExtvmmKeyStoreInstanceId_Object = MibTableColumn
cfprApExtvmmKeyStoreInstanceId = _CfprApExtvmmKeyStoreInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 7, 1, 1),
    _CfprApExtvmmKeyStoreInstanceId_Type()
)
cfprApExtvmmKeyStoreInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtvmmKeyStoreInstanceId.setStatus("current")
_CfprApExtvmmKeyStoreDn_Type = CfprApManagedObjectDn
_CfprApExtvmmKeyStoreDn_Object = MibTableColumn
cfprApExtvmmKeyStoreDn = _CfprApExtvmmKeyStoreDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 7, 1, 2),
    _CfprApExtvmmKeyStoreDn_Type()
)
cfprApExtvmmKeyStoreDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmKeyStoreDn.setStatus("current")
_CfprApExtvmmKeyStoreRn_Type = SnmpAdminString
_CfprApExtvmmKeyStoreRn_Object = MibTableColumn
cfprApExtvmmKeyStoreRn = _CfprApExtvmmKeyStoreRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 7, 1, 3),
    _CfprApExtvmmKeyStoreRn_Type()
)
cfprApExtvmmKeyStoreRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmKeyStoreRn.setStatus("current")
_CfprApExtvmmMasterExtKeyTable_Object = MibTable
cfprApExtvmmMasterExtKeyTable = _CfprApExtvmmMasterExtKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 8)
)
if mibBuilder.loadTexts:
    cfprApExtvmmMasterExtKeyTable.setStatus("current")
_CfprApExtvmmMasterExtKeyEntry_Object = MibTableRow
cfprApExtvmmMasterExtKeyEntry = _CfprApExtvmmMasterExtKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 8, 1)
)
cfprApExtvmmMasterExtKeyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTVMM-MIB", "cfprApExtvmmMasterExtKeyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtvmmMasterExtKeyEntry.setStatus("current")
_CfprApExtvmmMasterExtKeyInstanceId_Type = CfprApManagedObjectId
_CfprApExtvmmMasterExtKeyInstanceId_Object = MibTableColumn
cfprApExtvmmMasterExtKeyInstanceId = _CfprApExtvmmMasterExtKeyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 8, 1, 1),
    _CfprApExtvmmMasterExtKeyInstanceId_Type()
)
cfprApExtvmmMasterExtKeyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtvmmMasterExtKeyInstanceId.setStatus("current")
_CfprApExtvmmMasterExtKeyDn_Type = CfprApManagedObjectDn
_CfprApExtvmmMasterExtKeyDn_Object = MibTableColumn
cfprApExtvmmMasterExtKeyDn = _CfprApExtvmmMasterExtKeyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 8, 1, 2),
    _CfprApExtvmmMasterExtKeyDn_Type()
)
cfprApExtvmmMasterExtKeyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmMasterExtKeyDn.setStatus("current")
_CfprApExtvmmMasterExtKeyRn_Type = SnmpAdminString
_CfprApExtvmmMasterExtKeyRn_Object = MibTableColumn
cfprApExtvmmMasterExtKeyRn = _CfprApExtvmmMasterExtKeyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 8, 1, 3),
    _CfprApExtvmmMasterExtKeyRn_Type()
)
cfprApExtvmmMasterExtKeyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmMasterExtKeyRn.setStatus("current")
_CfprApExtvmmMasterExtKeyKey_Type = SnmpAdminString
_CfprApExtvmmMasterExtKeyKey_Object = MibTableColumn
cfprApExtvmmMasterExtKeyKey = _CfprApExtvmmMasterExtKeyKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 8, 1, 4),
    _CfprApExtvmmMasterExtKeyKey_Type()
)
cfprApExtvmmMasterExtKeyKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmMasterExtKeyKey.setStatus("current")
_CfprApExtvmmNetworkSetsTable_Object = MibTable
cfprApExtvmmNetworkSetsTable = _CfprApExtvmmNetworkSetsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 9)
)
if mibBuilder.loadTexts:
    cfprApExtvmmNetworkSetsTable.setStatus("current")
_CfprApExtvmmNetworkSetsEntry_Object = MibTableRow
cfprApExtvmmNetworkSetsEntry = _CfprApExtvmmNetworkSetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 9, 1)
)
cfprApExtvmmNetworkSetsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTVMM-MIB", "cfprApExtvmmNetworkSetsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtvmmNetworkSetsEntry.setStatus("current")
_CfprApExtvmmNetworkSetsInstanceId_Type = CfprApManagedObjectId
_CfprApExtvmmNetworkSetsInstanceId_Object = MibTableColumn
cfprApExtvmmNetworkSetsInstanceId = _CfprApExtvmmNetworkSetsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 9, 1, 1),
    _CfprApExtvmmNetworkSetsInstanceId_Type()
)
cfprApExtvmmNetworkSetsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtvmmNetworkSetsInstanceId.setStatus("current")
_CfprApExtvmmNetworkSetsDn_Type = CfprApManagedObjectDn
_CfprApExtvmmNetworkSetsDn_Object = MibTableColumn
cfprApExtvmmNetworkSetsDn = _CfprApExtvmmNetworkSetsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 9, 1, 2),
    _CfprApExtvmmNetworkSetsDn_Type()
)
cfprApExtvmmNetworkSetsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmNetworkSetsDn.setStatus("current")
_CfprApExtvmmNetworkSetsRn_Type = SnmpAdminString
_CfprApExtvmmNetworkSetsRn_Object = MibTableColumn
cfprApExtvmmNetworkSetsRn = _CfprApExtvmmNetworkSetsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 9, 1, 3),
    _CfprApExtvmmNetworkSetsRn_Type()
)
cfprApExtvmmNetworkSetsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmNetworkSetsRn.setStatus("current")
_CfprApExtvmmNetworkSetsFltAggr_Type = Unsigned64
_CfprApExtvmmNetworkSetsFltAggr_Object = MibTableColumn
cfprApExtvmmNetworkSetsFltAggr = _CfprApExtvmmNetworkSetsFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 9, 1, 4),
    _CfprApExtvmmNetworkSetsFltAggr_Type()
)
cfprApExtvmmNetworkSetsFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmNetworkSetsFltAggr.setStatus("current")
_CfprApExtvmmNetworkSetsGenNum_Type = Gauge32
_CfprApExtvmmNetworkSetsGenNum_Object = MibTableColumn
cfprApExtvmmNetworkSetsGenNum = _CfprApExtvmmNetworkSetsGenNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 9, 1, 5),
    _CfprApExtvmmNetworkSetsGenNum_Type()
)
cfprApExtvmmNetworkSetsGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmNetworkSetsGenNum.setStatus("current")
_CfprApExtvmmProviderTable_Object = MibTable
cfprApExtvmmProviderTable = _CfprApExtvmmProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 10)
)
if mibBuilder.loadTexts:
    cfprApExtvmmProviderTable.setStatus("current")
_CfprApExtvmmProviderEntry_Object = MibTableRow
cfprApExtvmmProviderEntry = _CfprApExtvmmProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 10, 1)
)
cfprApExtvmmProviderEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTVMM-MIB", "cfprApExtvmmProviderInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtvmmProviderEntry.setStatus("current")
_CfprApExtvmmProviderInstanceId_Type = CfprApManagedObjectId
_CfprApExtvmmProviderInstanceId_Object = MibTableColumn
cfprApExtvmmProviderInstanceId = _CfprApExtvmmProviderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 10, 1, 1),
    _CfprApExtvmmProviderInstanceId_Type()
)
cfprApExtvmmProviderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtvmmProviderInstanceId.setStatus("current")
_CfprApExtvmmProviderDn_Type = CfprApManagedObjectDn
_CfprApExtvmmProviderDn_Object = MibTableColumn
cfprApExtvmmProviderDn = _CfprApExtvmmProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 10, 1, 2),
    _CfprApExtvmmProviderDn_Type()
)
cfprApExtvmmProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmProviderDn.setStatus("current")
_CfprApExtvmmProviderRn_Type = SnmpAdminString
_CfprApExtvmmProviderRn_Object = MibTableColumn
cfprApExtvmmProviderRn = _CfprApExtvmmProviderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 10, 1, 3),
    _CfprApExtvmmProviderRn_Type()
)
cfprApExtvmmProviderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmProviderRn.setStatus("current")
_CfprApExtvmmProviderCert_Type = SnmpAdminString
_CfprApExtvmmProviderCert_Object = MibTableColumn
cfprApExtvmmProviderCert = _CfprApExtvmmProviderCert_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 10, 1, 4),
    _CfprApExtvmmProviderCert_Type()
)
cfprApExtvmmProviderCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmProviderCert.setStatus("current")
_CfprApExtvmmProviderDescr_Type = SnmpAdminString
_CfprApExtvmmProviderDescr_Object = MibTableColumn
cfprApExtvmmProviderDescr = _CfprApExtvmmProviderDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 10, 1, 5),
    _CfprApExtvmmProviderDescr_Type()
)
cfprApExtvmmProviderDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmProviderDescr.setStatus("current")
_CfprApExtvmmProviderHost_Type = SnmpAdminString
_CfprApExtvmmProviderHost_Object = MibTableColumn
cfprApExtvmmProviderHost = _CfprApExtvmmProviderHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 10, 1, 6),
    _CfprApExtvmmProviderHost_Type()
)
cfprApExtvmmProviderHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmProviderHost.setStatus("current")
_CfprApExtvmmProviderIntId_Type = SnmpAdminString
_CfprApExtvmmProviderIntId_Object = MibTableColumn
cfprApExtvmmProviderIntId = _CfprApExtvmmProviderIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 10, 1, 7),
    _CfprApExtvmmProviderIntId_Type()
)
cfprApExtvmmProviderIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmProviderIntId.setStatus("current")
_CfprApExtvmmProviderKey_Type = SnmpAdminString
_CfprApExtvmmProviderKey_Object = MibTableColumn
cfprApExtvmmProviderKey = _CfprApExtvmmProviderKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 10, 1, 8),
    _CfprApExtvmmProviderKey_Type()
)
cfprApExtvmmProviderKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmProviderKey.setStatus("current")
_CfprApExtvmmProviderName_Type = SnmpAdminString
_CfprApExtvmmProviderName_Object = MibTableColumn
cfprApExtvmmProviderName = _CfprApExtvmmProviderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 10, 1, 9),
    _CfprApExtvmmProviderName_Type()
)
cfprApExtvmmProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmProviderName.setStatus("current")
_CfprApExtvmmProviderPolicyLevel_Type = Gauge32
_CfprApExtvmmProviderPolicyLevel_Object = MibTableColumn
cfprApExtvmmProviderPolicyLevel = _CfprApExtvmmProviderPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 10, 1, 10),
    _CfprApExtvmmProviderPolicyLevel_Type()
)
cfprApExtvmmProviderPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmProviderPolicyLevel.setStatus("current")
_CfprApExtvmmProviderPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApExtvmmProviderPolicyOwner_Object = MibTableColumn
cfprApExtvmmProviderPolicyOwner = _CfprApExtvmmProviderPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 10, 1, 11),
    _CfprApExtvmmProviderPolicyOwner_Type()
)
cfprApExtvmmProviderPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmProviderPolicyOwner.setStatus("current")
_CfprApExtvmmProviderPortValue_Type = Gauge32
_CfprApExtvmmProviderPortValue_Object = MibTableColumn
cfprApExtvmmProviderPortValue = _CfprApExtvmmProviderPortValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 10, 1, 12),
    _CfprApExtvmmProviderPortValue_Type()
)
cfprApExtvmmProviderPortValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmProviderPortValue.setStatus("current")
_CfprApExtvmmProviderUuid_Type = SnmpAdminString
_CfprApExtvmmProviderUuid_Object = MibTableColumn
cfprApExtvmmProviderUuid = _CfprApExtvmmProviderUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 10, 1, 13),
    _CfprApExtvmmProviderUuid_Type()
)
cfprApExtvmmProviderUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmProviderUuid.setStatus("current")
_CfprApExtvmmProviderVendorType_Type = CfprApExtvmmProviderVendorType
_CfprApExtvmmProviderVendorType_Object = MibTableColumn
cfprApExtvmmProviderVendorType = _CfprApExtvmmProviderVendorType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 10, 1, 14),
    _CfprApExtvmmProviderVendorType_Type()
)
cfprApExtvmmProviderVendorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmProviderVendorType.setStatus("current")
_CfprApExtvmmProviderVer_Type = CfprApExtvmmVcVersion
_CfprApExtvmmProviderVer_Object = MibTableColumn
cfprApExtvmmProviderVer = _CfprApExtvmmProviderVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 10, 1, 15),
    _CfprApExtvmmProviderVer_Type()
)
cfprApExtvmmProviderVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmProviderVer.setStatus("current")
_CfprApExtvmmProviderVerRaw_Type = SnmpAdminString
_CfprApExtvmmProviderVerRaw_Object = MibTableColumn
cfprApExtvmmProviderVerRaw = _CfprApExtvmmProviderVerRaw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 10, 1, 16),
    _CfprApExtvmmProviderVerRaw_Type()
)
cfprApExtvmmProviderVerRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmProviderVerRaw.setStatus("current")
_CfprApExtvmmSwitchDelTaskTable_Object = MibTable
cfprApExtvmmSwitchDelTaskTable = _CfprApExtvmmSwitchDelTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 11)
)
if mibBuilder.loadTexts:
    cfprApExtvmmSwitchDelTaskTable.setStatus("current")
_CfprApExtvmmSwitchDelTaskEntry_Object = MibTableRow
cfprApExtvmmSwitchDelTaskEntry = _CfprApExtvmmSwitchDelTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 11, 1)
)
cfprApExtvmmSwitchDelTaskEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTVMM-MIB", "cfprApExtvmmSwitchDelTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtvmmSwitchDelTaskEntry.setStatus("current")
_CfprApExtvmmSwitchDelTaskInstanceId_Type = CfprApManagedObjectId
_CfprApExtvmmSwitchDelTaskInstanceId_Object = MibTableColumn
cfprApExtvmmSwitchDelTaskInstanceId = _CfprApExtvmmSwitchDelTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 11, 1, 1),
    _CfprApExtvmmSwitchDelTaskInstanceId_Type()
)
cfprApExtvmmSwitchDelTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtvmmSwitchDelTaskInstanceId.setStatus("current")
_CfprApExtvmmSwitchDelTaskDn_Type = CfprApManagedObjectDn
_CfprApExtvmmSwitchDelTaskDn_Object = MibTableColumn
cfprApExtvmmSwitchDelTaskDn = _CfprApExtvmmSwitchDelTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 11, 1, 2),
    _CfprApExtvmmSwitchDelTaskDn_Type()
)
cfprApExtvmmSwitchDelTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmSwitchDelTaskDn.setStatus("current")
_CfprApExtvmmSwitchDelTaskRn_Type = SnmpAdminString
_CfprApExtvmmSwitchDelTaskRn_Object = MibTableColumn
cfprApExtvmmSwitchDelTaskRn = _CfprApExtvmmSwitchDelTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 11, 1, 3),
    _CfprApExtvmmSwitchDelTaskRn_Type()
)
cfprApExtvmmSwitchDelTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmSwitchDelTaskRn.setStatus("current")
_CfprApExtvmmSwitchDelTaskCertFile_Type = SnmpAdminString
_CfprApExtvmmSwitchDelTaskCertFile_Object = MibTableColumn
cfprApExtvmmSwitchDelTaskCertFile = _CfprApExtvmmSwitchDelTaskCertFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 11, 1, 4),
    _CfprApExtvmmSwitchDelTaskCertFile_Type()
)
cfprApExtvmmSwitchDelTaskCertFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmSwitchDelTaskCertFile.setStatus("current")
_CfprApExtvmmSwitchDelTaskDcName_Type = SnmpAdminString
_CfprApExtvmmSwitchDelTaskDcName_Object = MibTableColumn
cfprApExtvmmSwitchDelTaskDcName = _CfprApExtvmmSwitchDelTaskDcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 11, 1, 5),
    _CfprApExtvmmSwitchDelTaskDcName_Type()
)
cfprApExtvmmSwitchDelTaskDcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmSwitchDelTaskDcName.setStatus("current")
_CfprApExtvmmSwitchDelTaskDcOrg_Type = SnmpAdminString
_CfprApExtvmmSwitchDelTaskDcOrg_Object = MibTableColumn
cfprApExtvmmSwitchDelTaskDcOrg = _CfprApExtvmmSwitchDelTaskDcOrg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 11, 1, 6),
    _CfprApExtvmmSwitchDelTaskDcOrg_Type()
)
cfprApExtvmmSwitchDelTaskDcOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmSwitchDelTaskDcOrg.setStatus("current")
_CfprApExtvmmSwitchDelTaskDescr_Type = SnmpAdminString
_CfprApExtvmmSwitchDelTaskDescr_Object = MibTableColumn
cfprApExtvmmSwitchDelTaskDescr = _CfprApExtvmmSwitchDelTaskDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 11, 1, 7),
    _CfprApExtvmmSwitchDelTaskDescr_Type()
)
cfprApExtvmmSwitchDelTaskDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmSwitchDelTaskDescr.setStatus("current")
_CfprApExtvmmSwitchDelTaskExtKey_Type = SnmpAdminString
_CfprApExtvmmSwitchDelTaskExtKey_Object = MibTableColumn
cfprApExtvmmSwitchDelTaskExtKey = _CfprApExtvmmSwitchDelTaskExtKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 11, 1, 8),
    _CfprApExtvmmSwitchDelTaskExtKey_Type()
)
cfprApExtvmmSwitchDelTaskExtKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmSwitchDelTaskExtKey.setStatus("current")
_CfprApExtvmmSwitchDelTaskHost_Type = SnmpAdminString
_CfprApExtvmmSwitchDelTaskHost_Object = MibTableColumn
cfprApExtvmmSwitchDelTaskHost = _CfprApExtvmmSwitchDelTaskHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 11, 1, 9),
    _CfprApExtvmmSwitchDelTaskHost_Type()
)
cfprApExtvmmSwitchDelTaskHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmSwitchDelTaskHost.setStatus("current")
_CfprApExtvmmSwitchDelTaskIntId_Type = SnmpAdminString
_CfprApExtvmmSwitchDelTaskIntId_Object = MibTableColumn
cfprApExtvmmSwitchDelTaskIntId = _CfprApExtvmmSwitchDelTaskIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 11, 1, 10),
    _CfprApExtvmmSwitchDelTaskIntId_Type()
)
cfprApExtvmmSwitchDelTaskIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmSwitchDelTaskIntId.setStatus("current")
_CfprApExtvmmSwitchDelTaskKeyInst_Type = Gauge32
_CfprApExtvmmSwitchDelTaskKeyInst_Object = MibTableColumn
cfprApExtvmmSwitchDelTaskKeyInst = _CfprApExtvmmSwitchDelTaskKeyInst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 11, 1, 11),
    _CfprApExtvmmSwitchDelTaskKeyInst_Type()
)
cfprApExtvmmSwitchDelTaskKeyInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmSwitchDelTaskKeyInst.setStatus("current")
_CfprApExtvmmSwitchDelTaskName_Type = SnmpAdminString
_CfprApExtvmmSwitchDelTaskName_Object = MibTableColumn
cfprApExtvmmSwitchDelTaskName = _CfprApExtvmmSwitchDelTaskName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 11, 1, 12),
    _CfprApExtvmmSwitchDelTaskName_Type()
)
cfprApExtvmmSwitchDelTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmSwitchDelTaskName.setStatus("current")
_CfprApExtvmmSwitchDelTaskOrgPath_Type = SnmpAdminString
_CfprApExtvmmSwitchDelTaskOrgPath_Object = MibTableColumn
cfprApExtvmmSwitchDelTaskOrgPath = _CfprApExtvmmSwitchDelTaskOrgPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 11, 1, 13),
    _CfprApExtvmmSwitchDelTaskOrgPath_Type()
)
cfprApExtvmmSwitchDelTaskOrgPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmSwitchDelTaskOrgPath.setStatus("current")
_CfprApExtvmmSwitchDelTaskPolicyLevel_Type = Gauge32
_CfprApExtvmmSwitchDelTaskPolicyLevel_Object = MibTableColumn
cfprApExtvmmSwitchDelTaskPolicyLevel = _CfprApExtvmmSwitchDelTaskPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 11, 1, 14),
    _CfprApExtvmmSwitchDelTaskPolicyLevel_Type()
)
cfprApExtvmmSwitchDelTaskPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmSwitchDelTaskPolicyLevel.setStatus("current")
_CfprApExtvmmSwitchDelTaskPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApExtvmmSwitchDelTaskPolicyOwner_Object = MibTableColumn
cfprApExtvmmSwitchDelTaskPolicyOwner = _CfprApExtvmmSwitchDelTaskPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 11, 1, 15),
    _CfprApExtvmmSwitchDelTaskPolicyOwner_Type()
)
cfprApExtvmmSwitchDelTaskPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmSwitchDelTaskPolicyOwner.setStatus("current")
_CfprApExtvmmSwitchDelTaskPortValue_Type = Gauge32
_CfprApExtvmmSwitchDelTaskPortValue_Object = MibTableColumn
cfprApExtvmmSwitchDelTaskPortValue = _CfprApExtvmmSwitchDelTaskPortValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 11, 1, 16),
    _CfprApExtvmmSwitchDelTaskPortValue_Type()
)
cfprApExtvmmSwitchDelTaskPortValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmSwitchDelTaskPortValue.setStatus("current")
_CfprApExtvmmSwitchDelTaskProvIntId_Type = SnmpAdminString
_CfprApExtvmmSwitchDelTaskProvIntId_Object = MibTableColumn
cfprApExtvmmSwitchDelTaskProvIntId = _CfprApExtvmmSwitchDelTaskProvIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 11, 1, 17),
    _CfprApExtvmmSwitchDelTaskProvIntId_Type()
)
cfprApExtvmmSwitchDelTaskProvIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmSwitchDelTaskProvIntId.setStatus("current")
_CfprApExtvmmSwitchDelTaskProvider_Type = SnmpAdminString
_CfprApExtvmmSwitchDelTaskProvider_Object = MibTableColumn
cfprApExtvmmSwitchDelTaskProvider = _CfprApExtvmmSwitchDelTaskProvider_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 11, 1, 18),
    _CfprApExtvmmSwitchDelTaskProvider_Type()
)
cfprApExtvmmSwitchDelTaskProvider.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmSwitchDelTaskProvider.setStatus("current")
_CfprApExtvmmSwitchDelTaskSwIntId_Type = SnmpAdminString
_CfprApExtvmmSwitchDelTaskSwIntId_Object = MibTableColumn
cfprApExtvmmSwitchDelTaskSwIntId = _CfprApExtvmmSwitchDelTaskSwIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 11, 1, 19),
    _CfprApExtvmmSwitchDelTaskSwIntId_Type()
)
cfprApExtvmmSwitchDelTaskSwIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmSwitchDelTaskSwIntId.setStatus("current")
_CfprApExtvmmSwitchDelTaskSwName_Type = SnmpAdminString
_CfprApExtvmmSwitchDelTaskSwName_Object = MibTableColumn
cfprApExtvmmSwitchDelTaskSwName = _CfprApExtvmmSwitchDelTaskSwName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 11, 1, 20),
    _CfprApExtvmmSwitchDelTaskSwName_Type()
)
cfprApExtvmmSwitchDelTaskSwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmSwitchDelTaskSwName.setStatus("current")
_CfprApExtvmmSwitchSetTable_Object = MibTable
cfprApExtvmmSwitchSetTable = _CfprApExtvmmSwitchSetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 12)
)
if mibBuilder.loadTexts:
    cfprApExtvmmSwitchSetTable.setStatus("current")
_CfprApExtvmmSwitchSetEntry_Object = MibTableRow
cfprApExtvmmSwitchSetEntry = _CfprApExtvmmSwitchSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 12, 1)
)
cfprApExtvmmSwitchSetEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTVMM-MIB", "cfprApExtvmmSwitchSetInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtvmmSwitchSetEntry.setStatus("current")
_CfprApExtvmmSwitchSetInstanceId_Type = CfprApManagedObjectId
_CfprApExtvmmSwitchSetInstanceId_Object = MibTableColumn
cfprApExtvmmSwitchSetInstanceId = _CfprApExtvmmSwitchSetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 12, 1, 1),
    _CfprApExtvmmSwitchSetInstanceId_Type()
)
cfprApExtvmmSwitchSetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtvmmSwitchSetInstanceId.setStatus("current")
_CfprApExtvmmSwitchSetDn_Type = CfprApManagedObjectDn
_CfprApExtvmmSwitchSetDn_Object = MibTableColumn
cfprApExtvmmSwitchSetDn = _CfprApExtvmmSwitchSetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 12, 1, 2),
    _CfprApExtvmmSwitchSetDn_Type()
)
cfprApExtvmmSwitchSetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmSwitchSetDn.setStatus("current")
_CfprApExtvmmSwitchSetRn_Type = SnmpAdminString
_CfprApExtvmmSwitchSetRn_Object = MibTableColumn
cfprApExtvmmSwitchSetRn = _CfprApExtvmmSwitchSetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 12, 1, 3),
    _CfprApExtvmmSwitchSetRn_Type()
)
cfprApExtvmmSwitchSetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmSwitchSetRn.setStatus("current")
_CfprApExtvmmUpLinkPPTable_Object = MibTable
cfprApExtvmmUpLinkPPTable = _CfprApExtvmmUpLinkPPTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 13)
)
if mibBuilder.loadTexts:
    cfprApExtvmmUpLinkPPTable.setStatus("current")
_CfprApExtvmmUpLinkPPEntry_Object = MibTableRow
cfprApExtvmmUpLinkPPEntry = _CfprApExtvmmUpLinkPPEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 13, 1)
)
cfprApExtvmmUpLinkPPEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTVMM-MIB", "cfprApExtvmmUpLinkPPInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtvmmUpLinkPPEntry.setStatus("current")
_CfprApExtvmmUpLinkPPInstanceId_Type = CfprApManagedObjectId
_CfprApExtvmmUpLinkPPInstanceId_Object = MibTableColumn
cfprApExtvmmUpLinkPPInstanceId = _CfprApExtvmmUpLinkPPInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 13, 1, 1),
    _CfprApExtvmmUpLinkPPInstanceId_Type()
)
cfprApExtvmmUpLinkPPInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtvmmUpLinkPPInstanceId.setStatus("current")
_CfprApExtvmmUpLinkPPDn_Type = CfprApManagedObjectDn
_CfprApExtvmmUpLinkPPDn_Object = MibTableColumn
cfprApExtvmmUpLinkPPDn = _CfprApExtvmmUpLinkPPDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 13, 1, 2),
    _CfprApExtvmmUpLinkPPDn_Type()
)
cfprApExtvmmUpLinkPPDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmUpLinkPPDn.setStatus("current")
_CfprApExtvmmUpLinkPPRn_Type = SnmpAdminString
_CfprApExtvmmUpLinkPPRn_Object = MibTableColumn
cfprApExtvmmUpLinkPPRn = _CfprApExtvmmUpLinkPPRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 13, 1, 3),
    _CfprApExtvmmUpLinkPPRn_Type()
)
cfprApExtvmmUpLinkPPRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmUpLinkPPRn.setStatus("current")
_CfprApExtvmmUpLinkPPDescr_Type = SnmpAdminString
_CfprApExtvmmUpLinkPPDescr_Object = MibTableColumn
cfprApExtvmmUpLinkPPDescr = _CfprApExtvmmUpLinkPPDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 13, 1, 4),
    _CfprApExtvmmUpLinkPPDescr_Type()
)
cfprApExtvmmUpLinkPPDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmUpLinkPPDescr.setStatus("current")
_CfprApExtvmmUpLinkPPFltAggr_Type = Unsigned64
_CfprApExtvmmUpLinkPPFltAggr_Object = MibTableColumn
cfprApExtvmmUpLinkPPFltAggr = _CfprApExtvmmUpLinkPPFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 13, 1, 5),
    _CfprApExtvmmUpLinkPPFltAggr_Type()
)
cfprApExtvmmUpLinkPPFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmUpLinkPPFltAggr.setStatus("current")
_CfprApExtvmmUpLinkPPGuid_Type = SnmpAdminString
_CfprApExtvmmUpLinkPPGuid_Object = MibTableColumn
cfprApExtvmmUpLinkPPGuid = _CfprApExtvmmUpLinkPPGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 13, 1, 6),
    _CfprApExtvmmUpLinkPPGuid_Type()
)
cfprApExtvmmUpLinkPPGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmUpLinkPPGuid.setStatus("current")
_CfprApExtvmmUpLinkPPIntId_Type = SnmpAdminString
_CfprApExtvmmUpLinkPPIntId_Object = MibTableColumn
cfprApExtvmmUpLinkPPIntId = _CfprApExtvmmUpLinkPPIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 13, 1, 7),
    _CfprApExtvmmUpLinkPPIntId_Type()
)
cfprApExtvmmUpLinkPPIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmUpLinkPPIntId.setStatus("current")
_CfprApExtvmmUpLinkPPName_Type = SnmpAdminString
_CfprApExtvmmUpLinkPPName_Object = MibTableColumn
cfprApExtvmmUpLinkPPName = _CfprApExtvmmUpLinkPPName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 13, 1, 8),
    _CfprApExtvmmUpLinkPPName_Type()
)
cfprApExtvmmUpLinkPPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmUpLinkPPName.setStatus("current")
_CfprApExtvmmUpLinkPPPolicyLevel_Type = Gauge32
_CfprApExtvmmUpLinkPPPolicyLevel_Object = MibTableColumn
cfprApExtvmmUpLinkPPPolicyLevel = _CfprApExtvmmUpLinkPPPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 13, 1, 9),
    _CfprApExtvmmUpLinkPPPolicyLevel_Type()
)
cfprApExtvmmUpLinkPPPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmUpLinkPPPolicyLevel.setStatus("current")
_CfprApExtvmmUpLinkPPPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApExtvmmUpLinkPPPolicyOwner_Object = MibTableColumn
cfprApExtvmmUpLinkPPPolicyOwner = _CfprApExtvmmUpLinkPPPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 13, 1, 10),
    _CfprApExtvmmUpLinkPPPolicyOwner_Type()
)
cfprApExtvmmUpLinkPPPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmUpLinkPPPolicyOwner.setStatus("current")
_CfprApExtvmmUpLinkPPRefOperState_Type = CfprApExtvmmRefOperState
_CfprApExtvmmUpLinkPPRefOperState_Object = MibTableColumn
cfprApExtvmmUpLinkPPRefOperState = _CfprApExtvmmUpLinkPPRefOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 13, 1, 11),
    _CfprApExtvmmUpLinkPPRefOperState_Type()
)
cfprApExtvmmUpLinkPPRefOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmUpLinkPPRefOperState.setStatus("current")
_CfprApExtvmmVMNDRefTable_Object = MibTable
cfprApExtvmmVMNDRefTable = _CfprApExtvmmVMNDRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 14)
)
if mibBuilder.loadTexts:
    cfprApExtvmmVMNDRefTable.setStatus("current")
_CfprApExtvmmVMNDRefEntry_Object = MibTableRow
cfprApExtvmmVMNDRefEntry = _CfprApExtvmmVMNDRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 14, 1)
)
cfprApExtvmmVMNDRefEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTVMM-MIB", "cfprApExtvmmVMNDRefInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtvmmVMNDRefEntry.setStatus("current")
_CfprApExtvmmVMNDRefInstanceId_Type = CfprApManagedObjectId
_CfprApExtvmmVMNDRefInstanceId_Object = MibTableColumn
cfprApExtvmmVMNDRefInstanceId = _CfprApExtvmmVMNDRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 14, 1, 1),
    _CfprApExtvmmVMNDRefInstanceId_Type()
)
cfprApExtvmmVMNDRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNDRefInstanceId.setStatus("current")
_CfprApExtvmmVMNDRefDn_Type = CfprApManagedObjectDn
_CfprApExtvmmVMNDRefDn_Object = MibTableColumn
cfprApExtvmmVMNDRefDn = _CfprApExtvmmVMNDRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 14, 1, 2),
    _CfprApExtvmmVMNDRefDn_Type()
)
cfprApExtvmmVMNDRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNDRefDn.setStatus("current")
_CfprApExtvmmVMNDRefRn_Type = SnmpAdminString
_CfprApExtvmmVMNDRefRn_Object = MibTableColumn
cfprApExtvmmVMNDRefRn = _CfprApExtvmmVMNDRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 14, 1, 3),
    _CfprApExtvmmVMNDRefRn_Type()
)
cfprApExtvmmVMNDRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNDRefRn.setStatus("current")
_CfprApExtvmmVMNDRefConfigQualifier_Type = CfprApExtvmmNetworkSetConfigQualifier
_CfprApExtvmmVMNDRefConfigQualifier_Object = MibTableColumn
cfprApExtvmmVMNDRefConfigQualifier = _CfprApExtvmmVMNDRefConfigQualifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 14, 1, 4),
    _CfprApExtvmmVMNDRefConfigQualifier_Type()
)
cfprApExtvmmVMNDRefConfigQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNDRefConfigQualifier.setStatus("current")
_CfprApExtvmmVMNDRefDescr_Type = SnmpAdminString
_CfprApExtvmmVMNDRefDescr_Object = MibTableColumn
cfprApExtvmmVMNDRefDescr = _CfprApExtvmmVMNDRefDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 14, 1, 5),
    _CfprApExtvmmVMNDRefDescr_Type()
)
cfprApExtvmmVMNDRefDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNDRefDescr.setStatus("current")
_CfprApExtvmmVMNDRefFnDefName_Type = SnmpAdminString
_CfprApExtvmmVMNDRefFnDefName_Object = MibTableColumn
cfprApExtvmmVMNDRefFnDefName = _CfprApExtvmmVMNDRefFnDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 14, 1, 6),
    _CfprApExtvmmVMNDRefFnDefName_Type()
)
cfprApExtvmmVMNDRefFnDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNDRefFnDefName.setStatus("current")
_CfprApExtvmmVMNDRefFnName_Type = SnmpAdminString
_CfprApExtvmmVMNDRefFnName_Object = MibTableColumn
cfprApExtvmmVMNDRefFnName = _CfprApExtvmmVMNDRefFnName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 14, 1, 7),
    _CfprApExtvmmVMNDRefFnName_Type()
)
cfprApExtvmmVMNDRefFnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNDRefFnName.setStatus("current")
_CfprApExtvmmVMNDRefIntId_Type = SnmpAdminString
_CfprApExtvmmVMNDRefIntId_Object = MibTableColumn
cfprApExtvmmVMNDRefIntId = _CfprApExtvmmVMNDRefIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 14, 1, 8),
    _CfprApExtvmmVMNDRefIntId_Type()
)
cfprApExtvmmVMNDRefIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNDRefIntId.setStatus("current")
_CfprApExtvmmVMNDRefName_Type = SnmpAdminString
_CfprApExtvmmVMNDRefName_Object = MibTableColumn
cfprApExtvmmVMNDRefName = _CfprApExtvmmVMNDRefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 14, 1, 9),
    _CfprApExtvmmVMNDRefName_Type()
)
cfprApExtvmmVMNDRefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNDRefName.setStatus("current")
_CfprApExtvmmVMNDRefOperVmNetworkDefName_Type = SnmpAdminString
_CfprApExtvmmVMNDRefOperVmNetworkDefName_Object = MibTableColumn
cfprApExtvmmVMNDRefOperVmNetworkDefName = _CfprApExtvmmVMNDRefOperVmNetworkDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 14, 1, 10),
    _CfprApExtvmmVMNDRefOperVmNetworkDefName_Type()
)
cfprApExtvmmVMNDRefOperVmNetworkDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNDRefOperVmNetworkDefName.setStatus("current")
_CfprApExtvmmVMNDRefPolicyLevel_Type = Gauge32
_CfprApExtvmmVMNDRefPolicyLevel_Object = MibTableColumn
cfprApExtvmmVMNDRefPolicyLevel = _CfprApExtvmmVMNDRefPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 14, 1, 11),
    _CfprApExtvmmVMNDRefPolicyLevel_Type()
)
cfprApExtvmmVMNDRefPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNDRefPolicyLevel.setStatus("current")
_CfprApExtvmmVMNDRefPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApExtvmmVMNDRefPolicyOwner_Object = MibTableColumn
cfprApExtvmmVMNDRefPolicyOwner = _CfprApExtvmmVMNDRefPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 14, 1, 12),
    _CfprApExtvmmVMNDRefPolicyOwner_Type()
)
cfprApExtvmmVMNDRefPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNDRefPolicyOwner.setStatus("current")
_CfprApExtvmmVMNDRefVmNetworkDefName_Type = SnmpAdminString
_CfprApExtvmmVMNDRefVmNetworkDefName_Object = MibTableColumn
cfprApExtvmmVMNDRefVmNetworkDefName = _CfprApExtvmmVMNDRefVmNetworkDefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 14, 1, 13),
    _CfprApExtvmmVMNDRefVmNetworkDefName_Type()
)
cfprApExtvmmVMNDRefVmNetworkDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNDRefVmNetworkDefName.setStatus("current")
_CfprApExtvmmVMNetworkTable_Object = MibTable
cfprApExtvmmVMNetworkTable = _CfprApExtvmmVMNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 15)
)
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkTable.setStatus("current")
_CfprApExtvmmVMNetworkEntry_Object = MibTableRow
cfprApExtvmmVMNetworkEntry = _CfprApExtvmmVMNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 15, 1)
)
cfprApExtvmmVMNetworkEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTVMM-MIB", "cfprApExtvmmVMNetworkInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkEntry.setStatus("current")
_CfprApExtvmmVMNetworkInstanceId_Type = CfprApManagedObjectId
_CfprApExtvmmVMNetworkInstanceId_Object = MibTableColumn
cfprApExtvmmVMNetworkInstanceId = _CfprApExtvmmVMNetworkInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 15, 1, 1),
    _CfprApExtvmmVMNetworkInstanceId_Type()
)
cfprApExtvmmVMNetworkInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkInstanceId.setStatus("current")
_CfprApExtvmmVMNetworkDn_Type = CfprApManagedObjectDn
_CfprApExtvmmVMNetworkDn_Object = MibTableColumn
cfprApExtvmmVMNetworkDn = _CfprApExtvmmVMNetworkDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 15, 1, 2),
    _CfprApExtvmmVMNetworkDn_Type()
)
cfprApExtvmmVMNetworkDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkDn.setStatus("current")
_CfprApExtvmmVMNetworkRn_Type = SnmpAdminString
_CfprApExtvmmVMNetworkRn_Object = MibTableColumn
cfprApExtvmmVMNetworkRn = _CfprApExtvmmVMNetworkRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 15, 1, 3),
    _CfprApExtvmmVMNetworkRn_Type()
)
cfprApExtvmmVMNetworkRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkRn.setStatus("current")
_CfprApExtvmmVMNetworkDescr_Type = SnmpAdminString
_CfprApExtvmmVMNetworkDescr_Object = MibTableColumn
cfprApExtvmmVMNetworkDescr = _CfprApExtvmmVMNetworkDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 15, 1, 4),
    _CfprApExtvmmVMNetworkDescr_Type()
)
cfprApExtvmmVMNetworkDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkDescr.setStatus("current")
_CfprApExtvmmVMNetworkFabricNetworkName_Type = SnmpAdminString
_CfprApExtvmmVMNetworkFabricNetworkName_Object = MibTableColumn
cfprApExtvmmVMNetworkFabricNetworkName = _CfprApExtvmmVMNetworkFabricNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 15, 1, 5),
    _CfprApExtvmmVMNetworkFabricNetworkName_Type()
)
cfprApExtvmmVMNetworkFabricNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkFabricNetworkName.setStatus("current")
_CfprApExtvmmVMNetworkFltAggr_Type = Unsigned64
_CfprApExtvmmVMNetworkFltAggr_Object = MibTableColumn
cfprApExtvmmVMNetworkFltAggr = _CfprApExtvmmVMNetworkFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 15, 1, 6),
    _CfprApExtvmmVMNetworkFltAggr_Type()
)
cfprApExtvmmVMNetworkFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkFltAggr.setStatus("current")
_CfprApExtvmmVMNetworkGuid_Type = SnmpAdminString
_CfprApExtvmmVMNetworkGuid_Object = MibTableColumn
cfprApExtvmmVMNetworkGuid = _CfprApExtvmmVMNetworkGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 15, 1, 7),
    _CfprApExtvmmVMNetworkGuid_Type()
)
cfprApExtvmmVMNetworkGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkGuid.setStatus("current")
_CfprApExtvmmVMNetworkIntId_Type = SnmpAdminString
_CfprApExtvmmVMNetworkIntId_Object = MibTableColumn
cfprApExtvmmVMNetworkIntId = _CfprApExtvmmVMNetworkIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 15, 1, 8),
    _CfprApExtvmmVMNetworkIntId_Type()
)
cfprApExtvmmVMNetworkIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkIntId.setStatus("current")
_CfprApExtvmmVMNetworkName_Type = SnmpAdminString
_CfprApExtvmmVMNetworkName_Object = MibTableColumn
cfprApExtvmmVMNetworkName = _CfprApExtvmmVMNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 15, 1, 9),
    _CfprApExtvmmVMNetworkName_Type()
)
cfprApExtvmmVMNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkName.setStatus("current")
_CfprApExtvmmVMNetworkOperFabricNetworkName_Type = SnmpAdminString
_CfprApExtvmmVMNetworkOperFabricNetworkName_Object = MibTableColumn
cfprApExtvmmVMNetworkOperFabricNetworkName = _CfprApExtvmmVMNetworkOperFabricNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 15, 1, 10),
    _CfprApExtvmmVMNetworkOperFabricNetworkName_Type()
)
cfprApExtvmmVMNetworkOperFabricNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkOperFabricNetworkName.setStatus("current")
_CfprApExtvmmVMNetworkPolicyLevel_Type = Gauge32
_CfprApExtvmmVMNetworkPolicyLevel_Object = MibTableColumn
cfprApExtvmmVMNetworkPolicyLevel = _CfprApExtvmmVMNetworkPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 15, 1, 11),
    _CfprApExtvmmVMNetworkPolicyLevel_Type()
)
cfprApExtvmmVMNetworkPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkPolicyLevel.setStatus("current")
_CfprApExtvmmVMNetworkPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApExtvmmVMNetworkPolicyOwner_Object = MibTableColumn
cfprApExtvmmVMNetworkPolicyOwner = _CfprApExtvmmVMNetworkPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 15, 1, 12),
    _CfprApExtvmmVMNetworkPolicyOwner_Type()
)
cfprApExtvmmVMNetworkPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkPolicyOwner.setStatus("current")
_CfprApExtvmmVMNetworkDefinitionTable_Object = MibTable
cfprApExtvmmVMNetworkDefinitionTable = _CfprApExtvmmVMNetworkDefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 16)
)
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkDefinitionTable.setStatus("current")
_CfprApExtvmmVMNetworkDefinitionEntry_Object = MibTableRow
cfprApExtvmmVMNetworkDefinitionEntry = _CfprApExtvmmVMNetworkDefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 16, 1)
)
cfprApExtvmmVMNetworkDefinitionEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTVMM-MIB", "cfprApExtvmmVMNetworkDefinitionInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkDefinitionEntry.setStatus("current")
_CfprApExtvmmVMNetworkDefinitionInstanceId_Type = CfprApManagedObjectId
_CfprApExtvmmVMNetworkDefinitionInstanceId_Object = MibTableColumn
cfprApExtvmmVMNetworkDefinitionInstanceId = _CfprApExtvmmVMNetworkDefinitionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 16, 1, 1),
    _CfprApExtvmmVMNetworkDefinitionInstanceId_Type()
)
cfprApExtvmmVMNetworkDefinitionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkDefinitionInstanceId.setStatus("current")
_CfprApExtvmmVMNetworkDefinitionDn_Type = CfprApManagedObjectDn
_CfprApExtvmmVMNetworkDefinitionDn_Object = MibTableColumn
cfprApExtvmmVMNetworkDefinitionDn = _CfprApExtvmmVMNetworkDefinitionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 16, 1, 2),
    _CfprApExtvmmVMNetworkDefinitionDn_Type()
)
cfprApExtvmmVMNetworkDefinitionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkDefinitionDn.setStatus("current")
_CfprApExtvmmVMNetworkDefinitionRn_Type = SnmpAdminString
_CfprApExtvmmVMNetworkDefinitionRn_Object = MibTableColumn
cfprApExtvmmVMNetworkDefinitionRn = _CfprApExtvmmVMNetworkDefinitionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 16, 1, 3),
    _CfprApExtvmmVMNetworkDefinitionRn_Type()
)
cfprApExtvmmVMNetworkDefinitionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkDefinitionRn.setStatus("current")
_CfprApExtvmmVMNetworkDefinitionDescr_Type = SnmpAdminString
_CfprApExtvmmVMNetworkDefinitionDescr_Object = MibTableColumn
cfprApExtvmmVMNetworkDefinitionDescr = _CfprApExtvmmVMNetworkDefinitionDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 16, 1, 4),
    _CfprApExtvmmVMNetworkDefinitionDescr_Type()
)
cfprApExtvmmVMNetworkDefinitionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkDefinitionDescr.setStatus("current")
_CfprApExtvmmVMNetworkDefinitionExtIpPoolName_Type = SnmpAdminString
_CfprApExtvmmVMNetworkDefinitionExtIpPoolName_Object = MibTableColumn
cfprApExtvmmVMNetworkDefinitionExtIpPoolName = _CfprApExtvmmVMNetworkDefinitionExtIpPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 16, 1, 5),
    _CfprApExtvmmVMNetworkDefinitionExtIpPoolName_Type()
)
cfprApExtvmmVMNetworkDefinitionExtIpPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkDefinitionExtIpPoolName.setStatus("current")
_CfprApExtvmmVMNetworkDefinitionGuid_Type = SnmpAdminString
_CfprApExtvmmVMNetworkDefinitionGuid_Object = MibTableColumn
cfprApExtvmmVMNetworkDefinitionGuid = _CfprApExtvmmVMNetworkDefinitionGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 16, 1, 6),
    _CfprApExtvmmVMNetworkDefinitionGuid_Type()
)
cfprApExtvmmVMNetworkDefinitionGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkDefinitionGuid.setStatus("current")
_CfprApExtvmmVMNetworkDefinitionIntId_Type = SnmpAdminString
_CfprApExtvmmVMNetworkDefinitionIntId_Object = MibTableColumn
cfprApExtvmmVMNetworkDefinitionIntId = _CfprApExtvmmVMNetworkDefinitionIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 16, 1, 7),
    _CfprApExtvmmVMNetworkDefinitionIntId_Type()
)
cfprApExtvmmVMNetworkDefinitionIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkDefinitionIntId.setStatus("current")
_CfprApExtvmmVMNetworkDefinitionIpPoolGuid_Type = SnmpAdminString
_CfprApExtvmmVMNetworkDefinitionIpPoolGuid_Object = MibTableColumn
cfprApExtvmmVMNetworkDefinitionIpPoolGuid = _CfprApExtvmmVMNetworkDefinitionIpPoolGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 16, 1, 8),
    _CfprApExtvmmVMNetworkDefinitionIpPoolGuid_Type()
)
cfprApExtvmmVMNetworkDefinitionIpPoolGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkDefinitionIpPoolGuid.setStatus("current")
_CfprApExtvmmVMNetworkDefinitionMaxPorts_Type = Gauge32
_CfprApExtvmmVMNetworkDefinitionMaxPorts_Object = MibTableColumn
cfprApExtvmmVMNetworkDefinitionMaxPorts = _CfprApExtvmmVMNetworkDefinitionMaxPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 16, 1, 9),
    _CfprApExtvmmVMNetworkDefinitionMaxPorts_Type()
)
cfprApExtvmmVMNetworkDefinitionMaxPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkDefinitionMaxPorts.setStatus("current")
_CfprApExtvmmVMNetworkDefinitionName_Type = SnmpAdminString
_CfprApExtvmmVMNetworkDefinitionName_Object = MibTableColumn
cfprApExtvmmVMNetworkDefinitionName = _CfprApExtvmmVMNetworkDefinitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 16, 1, 10),
    _CfprApExtvmmVMNetworkDefinitionName_Type()
)
cfprApExtvmmVMNetworkDefinitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkDefinitionName.setStatus("current")
_CfprApExtvmmVMNetworkDefinitionOperExtIpPoolName_Type = SnmpAdminString
_CfprApExtvmmVMNetworkDefinitionOperExtIpPoolName_Object = MibTableColumn
cfprApExtvmmVMNetworkDefinitionOperExtIpPoolName = _CfprApExtvmmVMNetworkDefinitionOperExtIpPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 16, 1, 11),
    _CfprApExtvmmVMNetworkDefinitionOperExtIpPoolName_Type()
)
cfprApExtvmmVMNetworkDefinitionOperExtIpPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkDefinitionOperExtIpPoolName.setStatus("current")
_CfprApExtvmmVMNetworkDefinitionPolicyLevel_Type = Gauge32
_CfprApExtvmmVMNetworkDefinitionPolicyLevel_Object = MibTableColumn
cfprApExtvmmVMNetworkDefinitionPolicyLevel = _CfprApExtvmmVMNetworkDefinitionPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 16, 1, 12),
    _CfprApExtvmmVMNetworkDefinitionPolicyLevel_Type()
)
cfprApExtvmmVMNetworkDefinitionPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkDefinitionPolicyLevel.setStatus("current")
_CfprApExtvmmVMNetworkDefinitionPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApExtvmmVMNetworkDefinitionPolicyOwner_Object = MibTableColumn
cfprApExtvmmVMNetworkDefinitionPolicyOwner = _CfprApExtvmmVMNetworkDefinitionPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 16, 1, 13),
    _CfprApExtvmmVMNetworkDefinitionPolicyOwner_Type()
)
cfprApExtvmmVMNetworkDefinitionPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkDefinitionPolicyOwner.setStatus("current")
_CfprApExtvmmVMNetworkDefinitionPrimaryVlanId_Type = Gauge32
_CfprApExtvmmVMNetworkDefinitionPrimaryVlanId_Object = MibTableColumn
cfprApExtvmmVMNetworkDefinitionPrimaryVlanId = _CfprApExtvmmVMNetworkDefinitionPrimaryVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 16, 1, 14),
    _CfprApExtvmmVMNetworkDefinitionPrimaryVlanId_Type()
)
cfprApExtvmmVMNetworkDefinitionPrimaryVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkDefinitionPrimaryVlanId.setStatus("current")
_CfprApExtvmmVMNetworkDefinitionRefOperState_Type = CfprApExtvmmRefOperState
_CfprApExtvmmVMNetworkDefinitionRefOperState_Object = MibTableColumn
cfprApExtvmmVMNetworkDefinitionRefOperState = _CfprApExtvmmVMNetworkDefinitionRefOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 16, 1, 15),
    _CfprApExtvmmVMNetworkDefinitionRefOperState_Type()
)
cfprApExtvmmVMNetworkDefinitionRefOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkDefinitionRefOperState.setStatus("current")
_CfprApExtvmmVMNetworkDefinitionVlanName_Type = SnmpAdminString
_CfprApExtvmmVMNetworkDefinitionVlanName_Object = MibTableColumn
cfprApExtvmmVMNetworkDefinitionVlanName = _CfprApExtvmmVMNetworkDefinitionVlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 16, 1, 16),
    _CfprApExtvmmVMNetworkDefinitionVlanName_Type()
)
cfprApExtvmmVMNetworkDefinitionVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkDefinitionVlanName.setStatus("current")
_CfprApExtvmmVMNetworkSetsTable_Object = MibTable
cfprApExtvmmVMNetworkSetsTable = _CfprApExtvmmVMNetworkSetsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 17)
)
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkSetsTable.setStatus("current")
_CfprApExtvmmVMNetworkSetsEntry_Object = MibTableRow
cfprApExtvmmVMNetworkSetsEntry = _CfprApExtvmmVMNetworkSetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 17, 1)
)
cfprApExtvmmVMNetworkSetsEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-EXTVMM-MIB", "cfprApExtvmmVMNetworkSetsInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkSetsEntry.setStatus("current")
_CfprApExtvmmVMNetworkSetsInstanceId_Type = CfprApManagedObjectId
_CfprApExtvmmVMNetworkSetsInstanceId_Object = MibTableColumn
cfprApExtvmmVMNetworkSetsInstanceId = _CfprApExtvmmVMNetworkSetsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 17, 1, 1),
    _CfprApExtvmmVMNetworkSetsInstanceId_Type()
)
cfprApExtvmmVMNetworkSetsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkSetsInstanceId.setStatus("current")
_CfprApExtvmmVMNetworkSetsDn_Type = CfprApManagedObjectDn
_CfprApExtvmmVMNetworkSetsDn_Object = MibTableColumn
cfprApExtvmmVMNetworkSetsDn = _CfprApExtvmmVMNetworkSetsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 17, 1, 2),
    _CfprApExtvmmVMNetworkSetsDn_Type()
)
cfprApExtvmmVMNetworkSetsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkSetsDn.setStatus("current")
_CfprApExtvmmVMNetworkSetsRn_Type = SnmpAdminString
_CfprApExtvmmVMNetworkSetsRn_Object = MibTableColumn
cfprApExtvmmVMNetworkSetsRn = _CfprApExtvmmVMNetworkSetsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 17, 1, 3),
    _CfprApExtvmmVMNetworkSetsRn_Type()
)
cfprApExtvmmVMNetworkSetsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkSetsRn.setStatus("current")
_CfprApExtvmmVMNetworkSetsFltAggr_Type = Unsigned64
_CfprApExtvmmVMNetworkSetsFltAggr_Object = MibTableColumn
cfprApExtvmmVMNetworkSetsFltAggr = _CfprApExtvmmVMNetworkSetsFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 17, 1, 4),
    _CfprApExtvmmVMNetworkSetsFltAggr_Type()
)
cfprApExtvmmVMNetworkSetsFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkSetsFltAggr.setStatus("current")
_CfprApExtvmmVMNetworkSetsGenNum_Type = Gauge32
_CfprApExtvmmVMNetworkSetsGenNum_Object = MibTableColumn
cfprApExtvmmVMNetworkSetsGenNum = _CfprApExtvmmVMNetworkSetsGenNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 25, 17, 1, 5),
    _CfprApExtvmmVMNetworkSetsGenNum_Type()
)
cfprApExtvmmVMNetworkSetsGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApExtvmmVMNetworkSetsGenNum.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-EXTVMM-MIB",
    **{"cfprApExtvmmObjects": cfprApExtvmmObjects,
       "cfprApExtvmmEpTable": cfprApExtvmmEpTable,
       "cfprApExtvmmEpEntry": cfprApExtvmmEpEntry,
       "cfprApExtvmmEpInstanceId": cfprApExtvmmEpInstanceId,
       "cfprApExtvmmEpDn": cfprApExtvmmEpDn,
       "cfprApExtvmmEpRn": cfprApExtvmmEpRn,
       "cfprApExtvmmEpGenNum": cfprApExtvmmEpGenNum,
       "cfprApExtvmmFNDReferenceTable": cfprApExtvmmFNDReferenceTable,
       "cfprApExtvmmFNDReferenceEntry": cfprApExtvmmFNDReferenceEntry,
       "cfprApExtvmmFNDReferenceInstanceId": cfprApExtvmmFNDReferenceInstanceId,
       "cfprApExtvmmFNDReferenceDn": cfprApExtvmmFNDReferenceDn,
       "cfprApExtvmmFNDReferenceRn": cfprApExtvmmFNDReferenceRn,
       "cfprApExtvmmFNDReferenceDescr": cfprApExtvmmFNDReferenceDescr,
       "cfprApExtvmmFNDReferenceFnDefName": cfprApExtvmmFNDReferenceFnDefName,
       "cfprApExtvmmFNDReferenceIntId": cfprApExtvmmFNDReferenceIntId,
       "cfprApExtvmmFNDReferenceName": cfprApExtvmmFNDReferenceName,
       "cfprApExtvmmFNDReferenceOperFnDefName": cfprApExtvmmFNDReferenceOperFnDefName,
       "cfprApExtvmmFNDReferencePolicyLevel": cfprApExtvmmFNDReferencePolicyLevel,
       "cfprApExtvmmFNDReferencePolicyOwner": cfprApExtvmmFNDReferencePolicyOwner,
       "cfprApExtvmmFabricNetworkTable": cfprApExtvmmFabricNetworkTable,
       "cfprApExtvmmFabricNetworkEntry": cfprApExtvmmFabricNetworkEntry,
       "cfprApExtvmmFabricNetworkInstanceId": cfprApExtvmmFabricNetworkInstanceId,
       "cfprApExtvmmFabricNetworkDn": cfprApExtvmmFabricNetworkDn,
       "cfprApExtvmmFabricNetworkRn": cfprApExtvmmFabricNetworkRn,
       "cfprApExtvmmFabricNetworkDescr": cfprApExtvmmFabricNetworkDescr,
       "cfprApExtvmmFabricNetworkGuid": cfprApExtvmmFabricNetworkGuid,
       "cfprApExtvmmFabricNetworkIntId": cfprApExtvmmFabricNetworkIntId,
       "cfprApExtvmmFabricNetworkName": cfprApExtvmmFabricNetworkName,
       "cfprApExtvmmFabricNetworkNetworkType": cfprApExtvmmFabricNetworkNetworkType,
       "cfprApExtvmmFabricNetworkPolicyLevel": cfprApExtvmmFabricNetworkPolicyLevel,
       "cfprApExtvmmFabricNetworkPolicyOwner": cfprApExtvmmFabricNetworkPolicyOwner,
       "cfprApExtvmmFabricNetworkRefOperState": cfprApExtvmmFabricNetworkRefOperState,
       "cfprApExtvmmFabricNetworkDefinitionTable": cfprApExtvmmFabricNetworkDefinitionTable,
       "cfprApExtvmmFabricNetworkDefinitionEntry": cfprApExtvmmFabricNetworkDefinitionEntry,
       "cfprApExtvmmFabricNetworkDefinitionInstanceId": cfprApExtvmmFabricNetworkDefinitionInstanceId,
       "cfprApExtvmmFabricNetworkDefinitionDn": cfprApExtvmmFabricNetworkDefinitionDn,
       "cfprApExtvmmFabricNetworkDefinitionRn": cfprApExtvmmFabricNetworkDefinitionRn,
       "cfprApExtvmmFabricNetworkDefinitionAllowedVnicType": cfprApExtvmmFabricNetworkDefinitionAllowedVnicType,
       "cfprApExtvmmFabricNetworkDefinitionDescr": cfprApExtvmmFabricNetworkDefinitionDescr,
       "cfprApExtvmmFabricNetworkDefinitionGuid": cfprApExtvmmFabricNetworkDefinitionGuid,
       "cfprApExtvmmFabricNetworkDefinitionIntId": cfprApExtvmmFabricNetworkDefinitionIntId,
       "cfprApExtvmmFabricNetworkDefinitionName": cfprApExtvmmFabricNetworkDefinitionName,
       "cfprApExtvmmFabricNetworkDefinitionPolicyLevel": cfprApExtvmmFabricNetworkDefinitionPolicyLevel,
       "cfprApExtvmmFabricNetworkDefinitionPolicyOwner": cfprApExtvmmFabricNetworkDefinitionPolicyOwner,
       "cfprApExtvmmFabricNetworkDefinitionPrimaryVlanId": cfprApExtvmmFabricNetworkDefinitionPrimaryVlanId,
       "cfprApExtvmmFabricNetworkDefinitionRefOperState": cfprApExtvmmFabricNetworkDefinitionRefOperState,
       "cfprApExtvmmKeyInstTable": cfprApExtvmmKeyInstTable,
       "cfprApExtvmmKeyInstEntry": cfprApExtvmmKeyInstEntry,
       "cfprApExtvmmKeyInstInstanceId": cfprApExtvmmKeyInstInstanceId,
       "cfprApExtvmmKeyInstDn": cfprApExtvmmKeyInstDn,
       "cfprApExtvmmKeyInstRn": cfprApExtvmmKeyInstRn,
       "cfprApExtvmmKeyInstInst": cfprApExtvmmKeyInstInst,
       "cfprApExtvmmKeyInstKey": cfprApExtvmmKeyInstKey,
       "cfprApExtvmmKeyRingTable": cfprApExtvmmKeyRingTable,
       "cfprApExtvmmKeyRingEntry": cfprApExtvmmKeyRingEntry,
       "cfprApExtvmmKeyRingInstanceId": cfprApExtvmmKeyRingInstanceId,
       "cfprApExtvmmKeyRingDn": cfprApExtvmmKeyRingDn,
       "cfprApExtvmmKeyRingRn": cfprApExtvmmKeyRingRn,
       "cfprApExtvmmKeyRingCertFile": cfprApExtvmmKeyRingCertFile,
       "cfprApExtvmmKeyRingLocation": cfprApExtvmmKeyRingLocation,
       "cfprApExtvmmKeyRingName": cfprApExtvmmKeyRingName,
       "cfprApExtvmmKeyRingPath": cfprApExtvmmKeyRingPath,
       "cfprApExtvmmKeyStoreTable": cfprApExtvmmKeyStoreTable,
       "cfprApExtvmmKeyStoreEntry": cfprApExtvmmKeyStoreEntry,
       "cfprApExtvmmKeyStoreInstanceId": cfprApExtvmmKeyStoreInstanceId,
       "cfprApExtvmmKeyStoreDn": cfprApExtvmmKeyStoreDn,
       "cfprApExtvmmKeyStoreRn": cfprApExtvmmKeyStoreRn,
       "cfprApExtvmmMasterExtKeyTable": cfprApExtvmmMasterExtKeyTable,
       "cfprApExtvmmMasterExtKeyEntry": cfprApExtvmmMasterExtKeyEntry,
       "cfprApExtvmmMasterExtKeyInstanceId": cfprApExtvmmMasterExtKeyInstanceId,
       "cfprApExtvmmMasterExtKeyDn": cfprApExtvmmMasterExtKeyDn,
       "cfprApExtvmmMasterExtKeyRn": cfprApExtvmmMasterExtKeyRn,
       "cfprApExtvmmMasterExtKeyKey": cfprApExtvmmMasterExtKeyKey,
       "cfprApExtvmmNetworkSetsTable": cfprApExtvmmNetworkSetsTable,
       "cfprApExtvmmNetworkSetsEntry": cfprApExtvmmNetworkSetsEntry,
       "cfprApExtvmmNetworkSetsInstanceId": cfprApExtvmmNetworkSetsInstanceId,
       "cfprApExtvmmNetworkSetsDn": cfprApExtvmmNetworkSetsDn,
       "cfprApExtvmmNetworkSetsRn": cfprApExtvmmNetworkSetsRn,
       "cfprApExtvmmNetworkSetsFltAggr": cfprApExtvmmNetworkSetsFltAggr,
       "cfprApExtvmmNetworkSetsGenNum": cfprApExtvmmNetworkSetsGenNum,
       "cfprApExtvmmProviderTable": cfprApExtvmmProviderTable,
       "cfprApExtvmmProviderEntry": cfprApExtvmmProviderEntry,
       "cfprApExtvmmProviderInstanceId": cfprApExtvmmProviderInstanceId,
       "cfprApExtvmmProviderDn": cfprApExtvmmProviderDn,
       "cfprApExtvmmProviderRn": cfprApExtvmmProviderRn,
       "cfprApExtvmmProviderCert": cfprApExtvmmProviderCert,
       "cfprApExtvmmProviderDescr": cfprApExtvmmProviderDescr,
       "cfprApExtvmmProviderHost": cfprApExtvmmProviderHost,
       "cfprApExtvmmProviderIntId": cfprApExtvmmProviderIntId,
       "cfprApExtvmmProviderKey": cfprApExtvmmProviderKey,
       "cfprApExtvmmProviderName": cfprApExtvmmProviderName,
       "cfprApExtvmmProviderPolicyLevel": cfprApExtvmmProviderPolicyLevel,
       "cfprApExtvmmProviderPolicyOwner": cfprApExtvmmProviderPolicyOwner,
       "cfprApExtvmmProviderPortValue": cfprApExtvmmProviderPortValue,
       "cfprApExtvmmProviderUuid": cfprApExtvmmProviderUuid,
       "cfprApExtvmmProviderVendorType": cfprApExtvmmProviderVendorType,
       "cfprApExtvmmProviderVer": cfprApExtvmmProviderVer,
       "cfprApExtvmmProviderVerRaw": cfprApExtvmmProviderVerRaw,
       "cfprApExtvmmSwitchDelTaskTable": cfprApExtvmmSwitchDelTaskTable,
       "cfprApExtvmmSwitchDelTaskEntry": cfprApExtvmmSwitchDelTaskEntry,
       "cfprApExtvmmSwitchDelTaskInstanceId": cfprApExtvmmSwitchDelTaskInstanceId,
       "cfprApExtvmmSwitchDelTaskDn": cfprApExtvmmSwitchDelTaskDn,
       "cfprApExtvmmSwitchDelTaskRn": cfprApExtvmmSwitchDelTaskRn,
       "cfprApExtvmmSwitchDelTaskCertFile": cfprApExtvmmSwitchDelTaskCertFile,
       "cfprApExtvmmSwitchDelTaskDcName": cfprApExtvmmSwitchDelTaskDcName,
       "cfprApExtvmmSwitchDelTaskDcOrg": cfprApExtvmmSwitchDelTaskDcOrg,
       "cfprApExtvmmSwitchDelTaskDescr": cfprApExtvmmSwitchDelTaskDescr,
       "cfprApExtvmmSwitchDelTaskExtKey": cfprApExtvmmSwitchDelTaskExtKey,
       "cfprApExtvmmSwitchDelTaskHost": cfprApExtvmmSwitchDelTaskHost,
       "cfprApExtvmmSwitchDelTaskIntId": cfprApExtvmmSwitchDelTaskIntId,
       "cfprApExtvmmSwitchDelTaskKeyInst": cfprApExtvmmSwitchDelTaskKeyInst,
       "cfprApExtvmmSwitchDelTaskName": cfprApExtvmmSwitchDelTaskName,
       "cfprApExtvmmSwitchDelTaskOrgPath": cfprApExtvmmSwitchDelTaskOrgPath,
       "cfprApExtvmmSwitchDelTaskPolicyLevel": cfprApExtvmmSwitchDelTaskPolicyLevel,
       "cfprApExtvmmSwitchDelTaskPolicyOwner": cfprApExtvmmSwitchDelTaskPolicyOwner,
       "cfprApExtvmmSwitchDelTaskPortValue": cfprApExtvmmSwitchDelTaskPortValue,
       "cfprApExtvmmSwitchDelTaskProvIntId": cfprApExtvmmSwitchDelTaskProvIntId,
       "cfprApExtvmmSwitchDelTaskProvider": cfprApExtvmmSwitchDelTaskProvider,
       "cfprApExtvmmSwitchDelTaskSwIntId": cfprApExtvmmSwitchDelTaskSwIntId,
       "cfprApExtvmmSwitchDelTaskSwName": cfprApExtvmmSwitchDelTaskSwName,
       "cfprApExtvmmSwitchSetTable": cfprApExtvmmSwitchSetTable,
       "cfprApExtvmmSwitchSetEntry": cfprApExtvmmSwitchSetEntry,
       "cfprApExtvmmSwitchSetInstanceId": cfprApExtvmmSwitchSetInstanceId,
       "cfprApExtvmmSwitchSetDn": cfprApExtvmmSwitchSetDn,
       "cfprApExtvmmSwitchSetRn": cfprApExtvmmSwitchSetRn,
       "cfprApExtvmmUpLinkPPTable": cfprApExtvmmUpLinkPPTable,
       "cfprApExtvmmUpLinkPPEntry": cfprApExtvmmUpLinkPPEntry,
       "cfprApExtvmmUpLinkPPInstanceId": cfprApExtvmmUpLinkPPInstanceId,
       "cfprApExtvmmUpLinkPPDn": cfprApExtvmmUpLinkPPDn,
       "cfprApExtvmmUpLinkPPRn": cfprApExtvmmUpLinkPPRn,
       "cfprApExtvmmUpLinkPPDescr": cfprApExtvmmUpLinkPPDescr,
       "cfprApExtvmmUpLinkPPFltAggr": cfprApExtvmmUpLinkPPFltAggr,
       "cfprApExtvmmUpLinkPPGuid": cfprApExtvmmUpLinkPPGuid,
       "cfprApExtvmmUpLinkPPIntId": cfprApExtvmmUpLinkPPIntId,
       "cfprApExtvmmUpLinkPPName": cfprApExtvmmUpLinkPPName,
       "cfprApExtvmmUpLinkPPPolicyLevel": cfprApExtvmmUpLinkPPPolicyLevel,
       "cfprApExtvmmUpLinkPPPolicyOwner": cfprApExtvmmUpLinkPPPolicyOwner,
       "cfprApExtvmmUpLinkPPRefOperState": cfprApExtvmmUpLinkPPRefOperState,
       "cfprApExtvmmVMNDRefTable": cfprApExtvmmVMNDRefTable,
       "cfprApExtvmmVMNDRefEntry": cfprApExtvmmVMNDRefEntry,
       "cfprApExtvmmVMNDRefInstanceId": cfprApExtvmmVMNDRefInstanceId,
       "cfprApExtvmmVMNDRefDn": cfprApExtvmmVMNDRefDn,
       "cfprApExtvmmVMNDRefRn": cfprApExtvmmVMNDRefRn,
       "cfprApExtvmmVMNDRefConfigQualifier": cfprApExtvmmVMNDRefConfigQualifier,
       "cfprApExtvmmVMNDRefDescr": cfprApExtvmmVMNDRefDescr,
       "cfprApExtvmmVMNDRefFnDefName": cfprApExtvmmVMNDRefFnDefName,
       "cfprApExtvmmVMNDRefFnName": cfprApExtvmmVMNDRefFnName,
       "cfprApExtvmmVMNDRefIntId": cfprApExtvmmVMNDRefIntId,
       "cfprApExtvmmVMNDRefName": cfprApExtvmmVMNDRefName,
       "cfprApExtvmmVMNDRefOperVmNetworkDefName": cfprApExtvmmVMNDRefOperVmNetworkDefName,
       "cfprApExtvmmVMNDRefPolicyLevel": cfprApExtvmmVMNDRefPolicyLevel,
       "cfprApExtvmmVMNDRefPolicyOwner": cfprApExtvmmVMNDRefPolicyOwner,
       "cfprApExtvmmVMNDRefVmNetworkDefName": cfprApExtvmmVMNDRefVmNetworkDefName,
       "cfprApExtvmmVMNetworkTable": cfprApExtvmmVMNetworkTable,
       "cfprApExtvmmVMNetworkEntry": cfprApExtvmmVMNetworkEntry,
       "cfprApExtvmmVMNetworkInstanceId": cfprApExtvmmVMNetworkInstanceId,
       "cfprApExtvmmVMNetworkDn": cfprApExtvmmVMNetworkDn,
       "cfprApExtvmmVMNetworkRn": cfprApExtvmmVMNetworkRn,
       "cfprApExtvmmVMNetworkDescr": cfprApExtvmmVMNetworkDescr,
       "cfprApExtvmmVMNetworkFabricNetworkName": cfprApExtvmmVMNetworkFabricNetworkName,
       "cfprApExtvmmVMNetworkFltAggr": cfprApExtvmmVMNetworkFltAggr,
       "cfprApExtvmmVMNetworkGuid": cfprApExtvmmVMNetworkGuid,
       "cfprApExtvmmVMNetworkIntId": cfprApExtvmmVMNetworkIntId,
       "cfprApExtvmmVMNetworkName": cfprApExtvmmVMNetworkName,
       "cfprApExtvmmVMNetworkOperFabricNetworkName": cfprApExtvmmVMNetworkOperFabricNetworkName,
       "cfprApExtvmmVMNetworkPolicyLevel": cfprApExtvmmVMNetworkPolicyLevel,
       "cfprApExtvmmVMNetworkPolicyOwner": cfprApExtvmmVMNetworkPolicyOwner,
       "cfprApExtvmmVMNetworkDefinitionTable": cfprApExtvmmVMNetworkDefinitionTable,
       "cfprApExtvmmVMNetworkDefinitionEntry": cfprApExtvmmVMNetworkDefinitionEntry,
       "cfprApExtvmmVMNetworkDefinitionInstanceId": cfprApExtvmmVMNetworkDefinitionInstanceId,
       "cfprApExtvmmVMNetworkDefinitionDn": cfprApExtvmmVMNetworkDefinitionDn,
       "cfprApExtvmmVMNetworkDefinitionRn": cfprApExtvmmVMNetworkDefinitionRn,
       "cfprApExtvmmVMNetworkDefinitionDescr": cfprApExtvmmVMNetworkDefinitionDescr,
       "cfprApExtvmmVMNetworkDefinitionExtIpPoolName": cfprApExtvmmVMNetworkDefinitionExtIpPoolName,
       "cfprApExtvmmVMNetworkDefinitionGuid": cfprApExtvmmVMNetworkDefinitionGuid,
       "cfprApExtvmmVMNetworkDefinitionIntId": cfprApExtvmmVMNetworkDefinitionIntId,
       "cfprApExtvmmVMNetworkDefinitionIpPoolGuid": cfprApExtvmmVMNetworkDefinitionIpPoolGuid,
       "cfprApExtvmmVMNetworkDefinitionMaxPorts": cfprApExtvmmVMNetworkDefinitionMaxPorts,
       "cfprApExtvmmVMNetworkDefinitionName": cfprApExtvmmVMNetworkDefinitionName,
       "cfprApExtvmmVMNetworkDefinitionOperExtIpPoolName": cfprApExtvmmVMNetworkDefinitionOperExtIpPoolName,
       "cfprApExtvmmVMNetworkDefinitionPolicyLevel": cfprApExtvmmVMNetworkDefinitionPolicyLevel,
       "cfprApExtvmmVMNetworkDefinitionPolicyOwner": cfprApExtvmmVMNetworkDefinitionPolicyOwner,
       "cfprApExtvmmVMNetworkDefinitionPrimaryVlanId": cfprApExtvmmVMNetworkDefinitionPrimaryVlanId,
       "cfprApExtvmmVMNetworkDefinitionRefOperState": cfprApExtvmmVMNetworkDefinitionRefOperState,
       "cfprApExtvmmVMNetworkDefinitionVlanName": cfprApExtvmmVMNetworkDefinitionVlanName,
       "cfprApExtvmmVMNetworkSetsTable": cfprApExtvmmVMNetworkSetsTable,
       "cfprApExtvmmVMNetworkSetsEntry": cfprApExtvmmVMNetworkSetsEntry,
       "cfprApExtvmmVMNetworkSetsInstanceId": cfprApExtvmmVMNetworkSetsInstanceId,
       "cfprApExtvmmVMNetworkSetsDn": cfprApExtvmmVMNetworkSetsDn,
       "cfprApExtvmmVMNetworkSetsRn": cfprApExtvmmVMNetworkSetsRn,
       "cfprApExtvmmVMNetworkSetsFltAggr": cfprApExtvmmVMNetworkSetsFltAggr,
       "cfprApExtvmmVMNetworkSetsGenNum": cfprApExtvmmVMNetworkSetsGenNum}
)
