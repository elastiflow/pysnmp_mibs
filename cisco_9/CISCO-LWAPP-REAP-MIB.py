# SNMP MIB module (CISCO-LWAPP-REAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-LWAPP-REAP-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:55:05 2025
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

(cLApSysMacAddress,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-AP-MIB",
    "cLApSysMacAddress")

(cLWlanIndex,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-WLAN-MIB",
    "cLWlanIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappReapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 517)
)
if mibBuilder.loadTexts:
    ciscoLwappReapMIB.setRevisions(
        ("2020-09-22 00:00",
         "2020-06-11 00:00",
         "2018-04-24 00:00",
         "2017-04-20 00:00",
         "2010-10-06 00:00",
         "2010-02-06 00:00",
         "2007-11-01 00:00",
         "2007-04-19 00:00",
         "2006-04-19 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappReapMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappReapMIBNotifs = _CiscoLwappReapMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 0)
)
_CiscoLwappReapMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappReapMIBObjects = _CiscoLwappReapMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1)
)
_CiscoLwappReapWlanConfig_ObjectIdentity = ObjectIdentity
ciscoLwappReapWlanConfig = _CiscoLwappReapWlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 1)
)
_CLReapWlanConfigTable_Object = MibTable
cLReapWlanConfigTable = _CLReapWlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cLReapWlanConfigTable.setStatus("current")
_CLReapWlanConfigEntry_Object = MibTableRow
cLReapWlanConfigEntry = _CLReapWlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 1, 1, 1)
)
cLReapWlanConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLReapWlanConfigEntry.setStatus("current")


class _CLReapWlanEnLocalSwitching_Type(TruthValue):
    """Custom type cLReapWlanEnLocalSwitching based on TruthValue"""
    defaultValue = 2


_CLReapWlanEnLocalSwitching_Type.__name__ = "TruthValue"
_CLReapWlanEnLocalSwitching_Object = MibTableColumn
cLReapWlanEnLocalSwitching = _CLReapWlanEnLocalSwitching_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 1, 1, 1, 1),
    _CLReapWlanEnLocalSwitching_Type()
)
cLReapWlanEnLocalSwitching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapWlanEnLocalSwitching.setStatus("current")


class _CLReapWlanClientIpLearnEnable_Type(TruthValue):
    """Custom type cLReapWlanClientIpLearnEnable based on TruthValue"""
    defaultValue = 1


_CLReapWlanClientIpLearnEnable_Type.__name__ = "TruthValue"
_CLReapWlanClientIpLearnEnable_Object = MibTableColumn
cLReapWlanClientIpLearnEnable = _CLReapWlanClientIpLearnEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 1, 1, 1, 2),
    _CLReapWlanClientIpLearnEnable_Type()
)
cLReapWlanClientIpLearnEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapWlanClientIpLearnEnable.setStatus("current")


class _CLReapWlanApAuth_Type(TruthValue):
    """Custom type cLReapWlanApAuth based on TruthValue"""
    defaultValue = 2


_CLReapWlanApAuth_Type.__name__ = "TruthValue"
_CLReapWlanApAuth_Object = MibTableColumn
cLReapWlanApAuth = _CLReapWlanApAuth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 1, 1, 1, 3),
    _CLReapWlanApAuth_Type()
)
cLReapWlanApAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapWlanApAuth.setStatus("current")


class _CLReapWlanVlanCentralSwitching_Type(TruthValue):
    """Custom type cLReapWlanVlanCentralSwitching based on TruthValue"""
    defaultValue = 2


_CLReapWlanVlanCentralSwitching_Type.__name__ = "TruthValue"
_CLReapWlanVlanCentralSwitching_Object = MibTableColumn
cLReapWlanVlanCentralSwitching = _CLReapWlanVlanCentralSwitching_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 1, 1, 1, 4),
    _CLReapWlanVlanCentralSwitching_Type()
)
cLReapWlanVlanCentralSwitching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapWlanVlanCentralSwitching.setStatus("current")


class _CLReapWlanDhcpCentral_Type(TruthValue):
    """Custom type cLReapWlanDhcpCentral based on TruthValue"""
    defaultValue = 2


_CLReapWlanDhcpCentral_Type.__name__ = "TruthValue"
_CLReapWlanDhcpCentral_Object = MibTableColumn
cLReapWlanDhcpCentral = _CLReapWlanDhcpCentral_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 1, 1, 1, 5),
    _CLReapWlanDhcpCentral_Type()
)
cLReapWlanDhcpCentral.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapWlanDhcpCentral.setStatus("current")


class _CLReapWlanDhcpOverrideDNS_Type(TruthValue):
    """Custom type cLReapWlanDhcpOverrideDNS based on TruthValue"""
    defaultValue = 2


_CLReapWlanDhcpOverrideDNS_Type.__name__ = "TruthValue"
_CLReapWlanDhcpOverrideDNS_Object = MibTableColumn
cLReapWlanDhcpOverrideDNS = _CLReapWlanDhcpOverrideDNS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 1, 1, 1, 6),
    _CLReapWlanDhcpOverrideDNS_Type()
)
cLReapWlanDhcpOverrideDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapWlanDhcpOverrideDNS.setStatus("current")


class _CLReapWlanNatPatEnabled_Type(TruthValue):
    """Custom type cLReapWlanNatPatEnabled based on TruthValue"""
    defaultValue = 2


_CLReapWlanNatPatEnabled_Type.__name__ = "TruthValue"
_CLReapWlanNatPatEnabled_Object = MibTableColumn
cLReapWlanNatPatEnabled = _CLReapWlanNatPatEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 1, 1, 1, 7),
    _CLReapWlanNatPatEnabled_Type()
)
cLReapWlanNatPatEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapWlanNatPatEnabled.setStatus("current")


class _CLReapWlanAssocCentral_Type(TruthValue):
    """Custom type cLReapWlanAssocCentral based on TruthValue"""
    defaultValue = 2


_CLReapWlanAssocCentral_Type.__name__ = "TruthValue"
_CLReapWlanAssocCentral_Object = MibTableColumn
cLReapWlanAssocCentral = _CLReapWlanAssocCentral_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 1, 1, 1, 8),
    _CLReapWlanAssocCentral_Type()
)
cLReapWlanAssocCentral.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapWlanAssocCentral.setStatus("current")
_CiscoLwappReapApConfig_ObjectIdentity = ObjectIdentity
ciscoLwappReapApConfig = _CiscoLwappReapApConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2)
)
_CLReapApConfigTable_Object = MibTable
cLReapApConfigTable = _CLReapApConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cLReapApConfigTable.setStatus("current")
_CLReapApConfigEntry_Object = MibTableRow
cLReapApConfigEntry = _CLReapApConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 1, 1)
)
cLReapApConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    cLReapApConfigEntry.setStatus("current")


class _CLReapApNativeVlanId_Type(Unsigned32):
    """Custom type cLReapApNativeVlanId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_CLReapApNativeVlanId_Type.__name__ = "Unsigned32"
_CLReapApNativeVlanId_Object = MibTableColumn
cLReapApNativeVlanId = _CLReapApNativeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 1, 1, 1),
    _CLReapApNativeVlanId_Type()
)
cLReapApNativeVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapApNativeVlanId.setStatus("current")


class _CLReapApVlanEnable_Type(TruthValue):
    """Custom type cLReapApVlanEnable based on TruthValue"""
    defaultValue = 2


_CLReapApVlanEnable_Type.__name__ = "TruthValue"
_CLReapApVlanEnable_Object = MibTableColumn
cLReapApVlanEnable = _CLReapApVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 1, 1, 2),
    _CLReapApVlanEnable_Type()
)
cLReapApVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapApVlanEnable.setStatus("current")


class _CLReapHomeApEnable_Type(TruthValue):
    """Custom type cLReapHomeApEnable based on TruthValue"""
    defaultValue = 2


_CLReapHomeApEnable_Type.__name__ = "TruthValue"
_CLReapHomeApEnable_Object = MibTableColumn
cLReapHomeApEnable = _CLReapHomeApEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 1, 1, 3),
    _CLReapHomeApEnable_Type()
)
cLReapHomeApEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapHomeApEnable.setStatus("current")


class _CLReapApLeastLatencyJoinEnable_Type(TruthValue):
    """Custom type cLReapApLeastLatencyJoinEnable based on TruthValue"""
    defaultValue = 2


_CLReapApLeastLatencyJoinEnable_Type.__name__ = "TruthValue"
_CLReapApLeastLatencyJoinEnable_Object = MibTableColumn
cLReapApLeastLatencyJoinEnable = _CLReapApLeastLatencyJoinEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 1, 1, 4),
    _CLReapApLeastLatencyJoinEnable_Type()
)
cLReapApLeastLatencyJoinEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapApLeastLatencyJoinEnable.setStatus("current")


class _CLReapHomeApLocalSsidReset_Type(TruthValue):
    """Custom type cLReapHomeApLocalSsidReset based on TruthValue"""
    defaultValue = 2


_CLReapHomeApLocalSsidReset_Type.__name__ = "TruthValue"
_CLReapHomeApLocalSsidReset_Object = MibTableColumn
cLReapHomeApLocalSsidReset = _CLReapHomeApLocalSsidReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 1, 1, 5),
    _CLReapHomeApLocalSsidReset_Type()
)
cLReapHomeApLocalSsidReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapHomeApLocalSsidReset.setStatus("current")


class _CLReapInstallMappingRadioBackhaul_Type(TruthValue):
    """Custom type cLReapInstallMappingRadioBackhaul based on TruthValue"""
    defaultValue = 2


_CLReapInstallMappingRadioBackhaul_Type.__name__ = "TruthValue"
_CLReapInstallMappingRadioBackhaul_Object = MibTableColumn
cLReapInstallMappingRadioBackhaul = _CLReapInstallMappingRadioBackhaul_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 1, 1, 6),
    _CLReapInstallMappingRadioBackhaul_Type()
)
cLReapInstallMappingRadioBackhaul.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapInstallMappingRadioBackhaul.setStatus("current")


class _CLReapApResilientMode_Type(TruthValue):
    """Custom type cLReapApResilientMode based on TruthValue"""
    defaultValue = 2


_CLReapApResilientMode_Type.__name__ = "TruthValue"
_CLReapApResilientMode_Object = MibTableColumn
cLReapApResilientMode = _CLReapApResilientMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 1, 1, 7),
    _CLReapApResilientMode_Type()
)
cLReapApResilientMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapApResilientMode.setStatus("current")


class _CLReapApNativeVlanLevel_Type(TruthValue):
    """Custom type cLReapApNativeVlanLevel based on TruthValue"""
    defaultValue = 2


_CLReapApNativeVlanLevel_Type.__name__ = "TruthValue"
_CLReapApNativeVlanLevel_Object = MibTableColumn
cLReapApNativeVlanLevel = _CLReapApNativeVlanLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 1, 1, 8),
    _CLReapApNativeVlanLevel_Type()
)
cLReapApNativeVlanLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapApNativeVlanLevel.setStatus("current")
_CLReapApVlanIdTable_Object = MibTable
cLReapApVlanIdTable = _CLReapApVlanIdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cLReapApVlanIdTable.setStatus("current")
_CLReapApVlanIdEntry_Object = MibTableRow
cLReapApVlanIdEntry = _CLReapApVlanIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 2, 1)
)
cLReapApVlanIdEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLReapApVlanIdEntry.setStatus("current")


class _CLReapApVlanId_Type(Unsigned32):
    """Custom type cLReapApVlanId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_CLReapApVlanId_Type.__name__ = "Unsigned32"
_CLReapApVlanId_Object = MibTableColumn
cLReapApVlanId = _CLReapApVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 2, 1, 1),
    _CLReapApVlanId_Type()
)
cLReapApVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapApVlanId.setStatus("current")


class _CLReapApVlanInheritance_Type(Integer32):
    """Custom type cLReapApVlanInheritance based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ap", 1),
          ("hreapGroup", 2),
          ("wlan", 3))
    )


_CLReapApVlanInheritance_Type.__name__ = "Integer32"
_CLReapApVlanInheritance_Object = MibTableColumn
cLReapApVlanInheritance = _CLReapApVlanInheritance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 2, 1, 2),
    _CLReapApVlanInheritance_Type()
)
cLReapApVlanInheritance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapApVlanInheritance.setStatus("current")
_CLReapApVlanRowStatus_Type = RowStatus
_CLReapApVlanRowStatus_Object = MibTableColumn
cLReapApVlanRowStatus = _CLReapApVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 2, 1, 3),
    _CLReapApVlanRowStatus_Type()
)
cLReapApVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapApVlanRowStatus.setStatus("current")


class _CLReapApVlanUsedBySecEthInterface_Type(TruthValue):
    """Custom type cLReapApVlanUsedBySecEthInterface based on TruthValue"""
    defaultValue = 2


_CLReapApVlanUsedBySecEthInterface_Type.__name__ = "TruthValue"
_CLReapApVlanUsedBySecEthInterface_Object = MibTableColumn
cLReapApVlanUsedBySecEthInterface = _CLReapApVlanUsedBySecEthInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 2, 1, 4),
    _CLReapApVlanUsedBySecEthInterface_Type()
)
cLReapApVlanUsedBySecEthInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLReapApVlanUsedBySecEthInterface.setStatus("current")
_CLReapApVlanIdAclTable_Object = MibTable
cLReapApVlanIdAclTable = _CLReapApVlanIdAclTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cLReapApVlanIdAclTable.setStatus("current")
_CLReapApVlanIdAclEntry_Object = MibTableRow
cLReapApVlanIdAclEntry = _CLReapApVlanIdAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 3, 1)
)
cLReapApVlanIdAclEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapVlanId"),
)
if mibBuilder.loadTexts:
    cLReapApVlanIdAclEntry.setStatus("current")


class _CLReapVlanId_Type(Unsigned32):
    """Custom type cLReapVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_CLReapVlanId_Type.__name__ = "Unsigned32"
_CLReapVlanId_Object = MibTableColumn
cLReapVlanId = _CLReapVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 3, 1, 1),
    _CLReapVlanId_Type()
)
cLReapVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLReapVlanId.setStatus("current")


class _CLReapIngressAcl_Type(SnmpAdminString):
    """Custom type cLReapIngressAcl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLReapIngressAcl_Type.__name__ = "SnmpAdminString"
_CLReapIngressAcl_Object = MibTableColumn
cLReapIngressAcl = _CLReapIngressAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 3, 1, 2),
    _CLReapIngressAcl_Type()
)
cLReapIngressAcl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapIngressAcl.setStatus("current")


class _CLReapEgressAcl_Type(SnmpAdminString):
    """Custom type cLReapEgressAcl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLReapEgressAcl_Type.__name__ = "SnmpAdminString"
_CLReapEgressAcl_Object = MibTableColumn
cLReapEgressAcl = _CLReapEgressAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 3, 1, 3),
    _CLReapEgressAcl_Type()
)
cLReapEgressAcl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapEgressAcl.setStatus("current")
_CLReapApVlanIdAclRowStatus_Type = RowStatus
_CLReapApVlanIdAclRowStatus_Object = MibTableColumn
cLReapApVlanIdAclRowStatus = _CLReapApVlanIdAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 3, 1, 4),
    _CLReapApVlanIdAclRowStatus_Type()
)
cLReapApVlanIdAclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapApVlanIdAclRowStatus.setStatus("current")


class _CLReapVlanIdAclType_Type(Integer32):
    """Custom type cLReapVlanIdAclType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("apSource", 1),
          ("groupSource", 2))
    )


_CLReapVlanIdAclType_Type.__name__ = "Integer32"
_CLReapVlanIdAclType_Object = MibTableColumn
cLReapVlanIdAclType = _CLReapVlanIdAclType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 3, 1, 5),
    _CLReapVlanIdAclType_Type()
)
cLReapVlanIdAclType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLReapVlanIdAclType.setStatus("current")
_CLReapApWlanAclTable_Object = MibTable
cLReapApWlanAclTable = _CLReapApWlanAclTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cLReapApWlanAclTable.setStatus("current")
_CLReapApWlanAclEntry_Object = MibTableRow
cLReapApWlanAclEntry = _CLReapApWlanAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 4, 1)
)
cLReapApWlanAclEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLReapApWlanAclEntry.setStatus("current")


class _CLReapApWebAuthAcl_Type(SnmpAdminString):
    """Custom type cLReapApWebAuthAcl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLReapApWebAuthAcl_Type.__name__ = "SnmpAdminString"
_CLReapApWebAuthAcl_Object = MibTableColumn
cLReapApWebAuthAcl = _CLReapApWebAuthAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 4, 1, 1),
    _CLReapApWebAuthAcl_Type()
)
cLReapApWebAuthAcl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapApWebAuthAcl.setStatus("current")
_CLReapApWebAuthAclRowStatus_Type = RowStatus
_CLReapApWebAuthAclRowStatus_Object = MibTableColumn
cLReapApWebAuthAclRowStatus = _CLReapApWebAuthAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 4, 1, 2),
    _CLReapApWebAuthAclRowStatus_Type()
)
cLReapApWebAuthAclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapApWebAuthAclRowStatus.setStatus("current")
_CLReapWebPolicyAclTable_Object = MibTable
cLReapWebPolicyAclTable = _CLReapWebPolicyAclTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cLReapWebPolicyAclTable.setStatus("current")
_CLReapWebPolicyAclEntry_Object = MibTableRow
cLReapWebPolicyAclEntry = _CLReapWebPolicyAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 5, 1)
)
cLReapWebPolicyAclEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapWebPolicyAcl"),
)
if mibBuilder.loadTexts:
    cLReapWebPolicyAclEntry.setStatus("current")


class _CLReapWebPolicyAcl_Type(SnmpAdminString):
    """Custom type cLReapWebPolicyAcl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLReapWebPolicyAcl_Type.__name__ = "SnmpAdminString"
_CLReapWebPolicyAcl_Object = MibTableColumn
cLReapWebPolicyAcl = _CLReapWebPolicyAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 5, 1, 1),
    _CLReapWebPolicyAcl_Type()
)
cLReapWebPolicyAcl.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLReapWebPolicyAcl.setStatus("current")
_CLReapWebPolicyAclRowStatus_Type = RowStatus
_CLReapWebPolicyAclRowStatus_Object = MibTableColumn
cLReapWebPolicyAclRowStatus = _CLReapWebPolicyAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 5, 1, 2),
    _CLReapWebPolicyAclRowStatus_Type()
)
cLReapWebPolicyAclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapWebPolicyAclRowStatus.setStatus("current")
_CLReapApLocalSplitACLTable_Object = MibTable
cLReapApLocalSplitACLTable = _CLReapApLocalSplitACLTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 6)
)
if mibBuilder.loadTexts:
    cLReapApLocalSplitACLTable.setStatus("current")
_CLReapApLocalSplitACLEntry_Object = MibTableRow
cLReapApLocalSplitACLEntry = _CLReapApLocalSplitACLEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 6, 1)
)
cLReapApLocalSplitACLEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLReapApLocalSplitACLEntry.setStatus("current")


class _CLReapApLocalSplitAcl_Type(SnmpAdminString):
    """Custom type cLReapApLocalSplitAcl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLReapApLocalSplitAcl_Type.__name__ = "SnmpAdminString"
_CLReapApLocalSplitAcl_Object = MibTableColumn
cLReapApLocalSplitAcl = _CLReapApLocalSplitAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 6, 1, 1),
    _CLReapApLocalSplitAcl_Type()
)
cLReapApLocalSplitAcl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapApLocalSplitAcl.setStatus("current")
_CLReapApLocalSplitAclRowStatus_Type = RowStatus
_CLReapApLocalSplitAclRowStatus_Object = MibTableColumn
cLReapApLocalSplitAclRowStatus = _CLReapApLocalSplitAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 6, 1, 2),
    _CLReapApLocalSplitAclRowStatus_Type()
)
cLReapApLocalSplitAclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapApLocalSplitAclRowStatus.setStatus("current")
_CLReapApCentralDhcpTable_Object = MibTable
cLReapApCentralDhcpTable = _CLReapApCentralDhcpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 7)
)
if mibBuilder.loadTexts:
    cLReapApCentralDhcpTable.setStatus("current")
_CLReapApCentralDhcpEntry_Object = MibTableRow
cLReapApCentralDhcpEntry = _CLReapApCentralDhcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 7, 1)
)
cLReapApCentralDhcpEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLReapApCentralDhcpEntry.setStatus("current")


class _CLReapApDhcpCentral_Type(TruthValue):
    """Custom type cLReapApDhcpCentral based on TruthValue"""
    defaultValue = 2


_CLReapApDhcpCentral_Type.__name__ = "TruthValue"
_CLReapApDhcpCentral_Object = MibTableColumn
cLReapApDhcpCentral = _CLReapApDhcpCentral_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 7, 1, 1),
    _CLReapApDhcpCentral_Type()
)
cLReapApDhcpCentral.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapApDhcpCentral.setStatus("current")


class _CLReapApDhcpOverrideDNS_Type(TruthValue):
    """Custom type cLReapApDhcpOverrideDNS based on TruthValue"""
    defaultValue = 2


_CLReapApDhcpOverrideDNS_Type.__name__ = "TruthValue"
_CLReapApDhcpOverrideDNS_Object = MibTableColumn
cLReapApDhcpOverrideDNS = _CLReapApDhcpOverrideDNS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 7, 1, 2),
    _CLReapApDhcpOverrideDNS_Type()
)
cLReapApDhcpOverrideDNS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapApDhcpOverrideDNS.setStatus("current")


class _CLReapApNatPatEnabled_Type(TruthValue):
    """Custom type cLReapApNatPatEnabled based on TruthValue"""
    defaultValue = 2


_CLReapApNatPatEnabled_Type.__name__ = "TruthValue"
_CLReapApNatPatEnabled_Object = MibTableColumn
cLReapApNatPatEnabled = _CLReapApNatPatEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 7, 1, 3),
    _CLReapApNatPatEnabled_Type()
)
cLReapApNatPatEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapApNatPatEnabled.setStatus("current")
_CLReapApDhcpRowStatus_Type = RowStatus
_CLReapApDhcpRowStatus_Object = MibTableColumn
cLReapApDhcpRowStatus = _CLReapApDhcpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 7, 1, 4),
    _CLReapApDhcpRowStatus_Type()
)
cLReapApDhcpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapApDhcpRowStatus.setStatus("current")
_CLReapApInheritance_Type = SnmpAdminString
_CLReapApInheritance_Object = MibTableColumn
cLReapApInheritance = _CLReapApInheritance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 7, 1, 5),
    _CLReapApInheritance_Type()
)
cLReapApInheritance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLReapApInheritance.setStatus("current")
_CLReapApL2AclTable_Object = MibTable
cLReapApL2AclTable = _CLReapApL2AclTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 8)
)
if mibBuilder.loadTexts:
    cLReapApL2AclTable.setStatus("current")
_CLReapApL2AclEntry_Object = MibTableRow
cLReapApL2AclEntry = _CLReapApL2AclEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 8, 1)
)
cLReapApL2AclEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLReapApL2AclEntry.setStatus("current")


class _CLReapApL2Acl_Type(SnmpAdminString):
    """Custom type cLReapApL2Acl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLReapApL2Acl_Type.__name__ = "SnmpAdminString"
_CLReapApL2Acl_Object = MibTableColumn
cLReapApL2Acl = _CLReapApL2Acl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 8, 1, 1),
    _CLReapApL2Acl_Type()
)
cLReapApL2Acl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapApL2Acl.setStatus("current")
_CLReapApL2AclRowStatus_Type = RowStatus
_CLReapApL2AclRowStatus_Object = MibTableColumn
cLReapApL2AclRowStatus = _CLReapApL2AclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 8, 1, 2),
    _CLReapApL2AclRowStatus_Type()
)
cLReapApL2AclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapApL2AclRowStatus.setStatus("current")
_CiscoLwappReapGroupConfig_ObjectIdentity = ObjectIdentity
ciscoLwappReapGroupConfig = _CiscoLwappReapGroupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3)
)
_CLReapGroupConfigTable_Object = MibTable
cLReapGroupConfigTable = _CLReapGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cLReapGroupConfigTable.setStatus("current")
_CLReapGroupConfigEntry_Object = MibTableRow
cLReapGroupConfigEntry = _CLReapGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1)
)
cLReapGroupConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapGroupName"),
)
if mibBuilder.loadTexts:
    cLReapGroupConfigEntry.setStatus("current")
_CLReapGroupName_Type = SnmpAdminString
_CLReapGroupName_Object = MibTableColumn
cLReapGroupName = _CLReapGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 1),
    _CLReapGroupName_Type()
)
cLReapGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLReapGroupName.setStatus("current")


class _CLReapGroupPrimaryRadiusIndex_Type(Unsigned32):
    """Custom type cLReapGroupPrimaryRadiusIndex based on Unsigned32"""
    defaultValue = 0


_CLReapGroupPrimaryRadiusIndex_Type.__name__ = "Unsigned32"
_CLReapGroupPrimaryRadiusIndex_Object = MibTableColumn
cLReapGroupPrimaryRadiusIndex = _CLReapGroupPrimaryRadiusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 2),
    _CLReapGroupPrimaryRadiusIndex_Type()
)
cLReapGroupPrimaryRadiusIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupPrimaryRadiusIndex.setStatus("current")


class _CLReapGroupSecondaryRadiusIndex_Type(Unsigned32):
    """Custom type cLReapGroupSecondaryRadiusIndex based on Unsigned32"""
    defaultValue = 0


_CLReapGroupSecondaryRadiusIndex_Type.__name__ = "Unsigned32"
_CLReapGroupSecondaryRadiusIndex_Object = MibTableColumn
cLReapGroupSecondaryRadiusIndex = _CLReapGroupSecondaryRadiusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 3),
    _CLReapGroupSecondaryRadiusIndex_Type()
)
cLReapGroupSecondaryRadiusIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupSecondaryRadiusIndex.setStatus("current")
_CLReapGroupStorageType_Type = StorageType
_CLReapGroupStorageType_Object = MibTableColumn
cLReapGroupStorageType = _CLReapGroupStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 4),
    _CLReapGroupStorageType_Type()
)
cLReapGroupStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupStorageType.setStatus("current")
_CLReapGroupRowStatus_Type = RowStatus
_CLReapGroupRowStatus_Object = MibTableColumn
cLReapGroupRowStatus = _CLReapGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 5),
    _CLReapGroupRowStatus_Type()
)
cLReapGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupRowStatus.setStatus("current")


class _CLReapGroupRadiusPacTimeout_Type(Unsigned32):
    """Custom type cLReapGroupRadiusPacTimeout based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CLReapGroupRadiusPacTimeout_Type.__name__ = "Unsigned32"
_CLReapGroupRadiusPacTimeout_Object = MibTableColumn
cLReapGroupRadiusPacTimeout = _CLReapGroupRadiusPacTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 6),
    _CLReapGroupRadiusPacTimeout_Type()
)
cLReapGroupRadiusPacTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupRadiusPacTimeout.setStatus("deprecated")
if mibBuilder.loadTexts:
    cLReapGroupRadiusPacTimeout.setUnits("Seconds")


class _CLReapGroupRadiusAuthorityId_Type(OctetString):
    """Custom type cLReapGroupRadiusAuthorityId based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLReapGroupRadiusAuthorityId_Type.__name__ = "OctetString"
_CLReapGroupRadiusAuthorityId_Object = MibTableColumn
cLReapGroupRadiusAuthorityId = _CLReapGroupRadiusAuthorityId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 7),
    _CLReapGroupRadiusAuthorityId_Type()
)
cLReapGroupRadiusAuthorityId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupRadiusAuthorityId.setStatus("current")


class _CLReapGroupRadiusAuthorityInfo_Type(OctetString):
    """Custom type cLReapGroupRadiusAuthorityInfo based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLReapGroupRadiusAuthorityInfo_Type.__name__ = "OctetString"
_CLReapGroupRadiusAuthorityInfo_Object = MibTableColumn
cLReapGroupRadiusAuthorityInfo = _CLReapGroupRadiusAuthorityInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 8),
    _CLReapGroupRadiusAuthorityInfo_Type()
)
cLReapGroupRadiusAuthorityInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupRadiusAuthorityInfo.setStatus("current")


class _CLReapGroupRadiusServerKey_Type(OctetString):
    """Custom type cLReapGroupRadiusServerKey based on OctetString"""
    defaultValue = OctetString("****")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLReapGroupRadiusServerKey_Type.__name__ = "OctetString"
_CLReapGroupRadiusServerKey_Object = MibTableColumn
cLReapGroupRadiusServerKey = _CLReapGroupRadiusServerKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 9),
    _CLReapGroupRadiusServerKey_Type()
)
cLReapGroupRadiusServerKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupRadiusServerKey.setStatus("current")


class _CLReapGroupRadiusIgnoreKey_Type(TruthValue):
    """Custom type cLReapGroupRadiusIgnoreKey based on TruthValue"""
    defaultValue = 1


_CLReapGroupRadiusIgnoreKey_Type.__name__ = "TruthValue"
_CLReapGroupRadiusIgnoreKey_Object = MibTableColumn
cLReapGroupRadiusIgnoreKey = _CLReapGroupRadiusIgnoreKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 10),
    _CLReapGroupRadiusIgnoreKey_Type()
)
cLReapGroupRadiusIgnoreKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupRadiusIgnoreKey.setStatus("current")


class _CLReapGroupRadiusEnable_Type(TruthValue):
    """Custom type cLReapGroupRadiusEnable based on TruthValue"""
    defaultValue = 2


_CLReapGroupRadiusEnable_Type.__name__ = "TruthValue"
_CLReapGroupRadiusEnable_Object = MibTableColumn
cLReapGroupRadiusEnable = _CLReapGroupRadiusEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 11),
    _CLReapGroupRadiusEnable_Type()
)
cLReapGroupRadiusEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupRadiusEnable.setStatus("current")


class _CLReapGroupRadiusLeapEnable_Type(TruthValue):
    """Custom type cLReapGroupRadiusLeapEnable based on TruthValue"""
    defaultValue = 2


_CLReapGroupRadiusLeapEnable_Type.__name__ = "TruthValue"
_CLReapGroupRadiusLeapEnable_Object = MibTableColumn
cLReapGroupRadiusLeapEnable = _CLReapGroupRadiusLeapEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 12),
    _CLReapGroupRadiusLeapEnable_Type()
)
cLReapGroupRadiusLeapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupRadiusLeapEnable.setStatus("current")


class _CLReapGroupRadiusEapFastEnable_Type(TruthValue):
    """Custom type cLReapGroupRadiusEapFastEnable based on TruthValue"""
    defaultValue = 2


_CLReapGroupRadiusEapFastEnable_Type.__name__ = "TruthValue"
_CLReapGroupRadiusEapFastEnable_Object = MibTableColumn
cLReapGroupRadiusEapFastEnable = _CLReapGroupRadiusEapFastEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 13),
    _CLReapGroupRadiusEapFastEnable_Type()
)
cLReapGroupRadiusEapFastEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupRadiusEapFastEnable.setStatus("current")


class _CLReapGroupRadiusPacTimeoutCtrl_Type(Unsigned32):
    """Custom type cLReapGroupRadiusPacTimeoutCtrl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CLReapGroupRadiusPacTimeoutCtrl_Type.__name__ = "Unsigned32"
_CLReapGroupRadiusPacTimeoutCtrl_Object = MibTableColumn
cLReapGroupRadiusPacTimeoutCtrl = _CLReapGroupRadiusPacTimeoutCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 14),
    _CLReapGroupRadiusPacTimeoutCtrl_Type()
)
cLReapGroupRadiusPacTimeoutCtrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupRadiusPacTimeoutCtrl.setStatus("current")
if mibBuilder.loadTexts:
    cLReapGroupRadiusPacTimeoutCtrl.setUnits("seconds")


class _CLReapGroupEfficientApUpgradeEnable_Type(TruthValue):
    """Custom type cLReapGroupEfficientApUpgradeEnable based on TruthValue"""
    defaultValue = 2


_CLReapGroupEfficientApUpgradeEnable_Type.__name__ = "TruthValue"
_CLReapGroupEfficientApUpgradeEnable_Object = MibTableColumn
cLReapGroupEfficientApUpgradeEnable = _CLReapGroupEfficientApUpgradeEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 15),
    _CLReapGroupEfficientApUpgradeEnable_Type()
)
cLReapGroupEfficientApUpgradeEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupEfficientApUpgradeEnable.setStatus("current")


class _CLReapGroupApUpgradeStart_Type(Integer32):
    """Custom type cLReapGroupApUpgradeStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("initiatePrimary", 1),
          ("initiateBackup", 2),
          ("abort", 3))
    )


_CLReapGroupApUpgradeStart_Type.__name__ = "Integer32"
_CLReapGroupApUpgradeStart_Object = MibTableColumn
cLReapGroupApUpgradeStart = _CLReapGroupApUpgradeStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 16),
    _CLReapGroupApUpgradeStart_Type()
)
cLReapGroupApUpgradeStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupApUpgradeStart.setStatus("current")
_CLReapGroupSlaveMaxRetryCount_Type = Unsigned32
_CLReapGroupSlaveMaxRetryCount_Object = MibTableColumn
cLReapGroupSlaveMaxRetryCount = _CLReapGroupSlaveMaxRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 17),
    _CLReapGroupSlaveMaxRetryCount_Type()
)
cLReapGroupSlaveMaxRetryCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupSlaveMaxRetryCount.setStatus("current")
_CLReapGroupPrimaryRadiusServerType_Type = InetAddressType
_CLReapGroupPrimaryRadiusServerType_Object = MibTableColumn
cLReapGroupPrimaryRadiusServerType = _CLReapGroupPrimaryRadiusServerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 18),
    _CLReapGroupPrimaryRadiusServerType_Type()
)
cLReapGroupPrimaryRadiusServerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupPrimaryRadiusServerType.setStatus("current")
_CLReapGroupPrimaryRadiusServerAddress_Type = InetAddress
_CLReapGroupPrimaryRadiusServerAddress_Object = MibTableColumn
cLReapGroupPrimaryRadiusServerAddress = _CLReapGroupPrimaryRadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 19),
    _CLReapGroupPrimaryRadiusServerAddress_Type()
)
cLReapGroupPrimaryRadiusServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupPrimaryRadiusServerAddress.setStatus("current")
_CLReapGroupPrimaryRadiusServerPort_Type = Unsigned32
_CLReapGroupPrimaryRadiusServerPort_Object = MibTableColumn
cLReapGroupPrimaryRadiusServerPort = _CLReapGroupPrimaryRadiusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 20),
    _CLReapGroupPrimaryRadiusServerPort_Type()
)
cLReapGroupPrimaryRadiusServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupPrimaryRadiusServerPort.setStatus("current")
_CLReapGroupPrimaryServerSecret_Type = SnmpAdminString
_CLReapGroupPrimaryServerSecret_Object = MibTableColumn
cLReapGroupPrimaryServerSecret = _CLReapGroupPrimaryServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 21),
    _CLReapGroupPrimaryServerSecret_Type()
)
cLReapGroupPrimaryServerSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupPrimaryServerSecret.setStatus("current")
_CLReapGroupSecRadiusServerType_Type = InetAddressType
_CLReapGroupSecRadiusServerType_Object = MibTableColumn
cLReapGroupSecRadiusServerType = _CLReapGroupSecRadiusServerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 22),
    _CLReapGroupSecRadiusServerType_Type()
)
cLReapGroupSecRadiusServerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupSecRadiusServerType.setStatus("current")
_CLReapGroupSecRadiusServerAddress_Type = InetAddress
_CLReapGroupSecRadiusServerAddress_Object = MibTableColumn
cLReapGroupSecRadiusServerAddress = _CLReapGroupSecRadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 23),
    _CLReapGroupSecRadiusServerAddress_Type()
)
cLReapGroupSecRadiusServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupSecRadiusServerAddress.setStatus("current")
_CLReapGroupSecRadiusServerPort_Type = Unsigned32
_CLReapGroupSecRadiusServerPort_Object = MibTableColumn
cLReapGroupSecRadiusServerPort = _CLReapGroupSecRadiusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 24),
    _CLReapGroupSecRadiusServerPort_Type()
)
cLReapGroupSecRadiusServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupSecRadiusServerPort.setStatus("current")
_CLReapGroupSecServerSecret_Type = SnmpAdminString
_CLReapGroupSecServerSecret_Object = MibTableColumn
cLReapGroupSecServerSecret = _CLReapGroupSecServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 25),
    _CLReapGroupSecServerSecret_Type()
)
cLReapGroupSecServerSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupSecServerSecret.setStatus("current")


class _CLReapGroupRadiusPeapEnable_Type(TruthValue):
    """Custom type cLReapGroupRadiusPeapEnable based on TruthValue"""
    defaultValue = 2


_CLReapGroupRadiusPeapEnable_Type.__name__ = "TruthValue"
_CLReapGroupRadiusPeapEnable_Object = MibTableColumn
cLReapGroupRadiusPeapEnable = _CLReapGroupRadiusPeapEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 26),
    _CLReapGroupRadiusPeapEnable_Type()
)
cLReapGroupRadiusPeapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupRadiusPeapEnable.setStatus("current")


class _CLReapGroupRadiusEapTlsEnable_Type(TruthValue):
    """Custom type cLReapGroupRadiusEapTlsEnable based on TruthValue"""
    defaultValue = 2


_CLReapGroupRadiusEapTlsEnable_Type.__name__ = "TruthValue"
_CLReapGroupRadiusEapTlsEnable_Object = MibTableColumn
cLReapGroupRadiusEapTlsEnable = _CLReapGroupRadiusEapTlsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 27),
    _CLReapGroupRadiusEapTlsEnable_Type()
)
cLReapGroupRadiusEapTlsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupRadiusEapTlsEnable.setStatus("current")


class _CLReapGroupCertificateEapTlsEnable_Type(TruthValue):
    """Custom type cLReapGroupCertificateEapTlsEnable based on TruthValue"""
    defaultValue = 2


_CLReapGroupCertificateEapTlsEnable_Type.__name__ = "TruthValue"
_CLReapGroupCertificateEapTlsEnable_Object = MibTableColumn
cLReapGroupCertificateEapTlsEnable = _CLReapGroupCertificateEapTlsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 28),
    _CLReapGroupCertificateEapTlsEnable_Type()
)
cLReapGroupCertificateEapTlsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupCertificateEapTlsEnable.setStatus("current")


class _CLReapGroupNativeVlanId_Type(Unsigned32):
    """Custom type cLReapGroupNativeVlanId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_CLReapGroupNativeVlanId_Type.__name__ = "Unsigned32"
_CLReapGroupNativeVlanId_Object = MibTableColumn
cLReapGroupNativeVlanId = _CLReapGroupNativeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 29),
    _CLReapGroupNativeVlanId_Type()
)
cLReapGroupNativeVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupNativeVlanId.setStatus("current")


class _CLReapGroupVlanEnable_Type(TruthValue):
    """Custom type cLReapGroupVlanEnable based on TruthValue"""
    defaultValue = 2


_CLReapGroupVlanEnable_Type.__name__ = "TruthValue"
_CLReapGroupVlanEnable_Object = MibTableColumn
cLReapGroupVlanEnable = _CLReapGroupVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 30),
    _CLReapGroupVlanEnable_Type()
)
cLReapGroupVlanEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupVlanEnable.setStatus("current")


class _CLReapGroupOverrideVlanEnable_Type(TruthValue):
    """Custom type cLReapGroupOverrideVlanEnable based on TruthValue"""
    defaultValue = 2


_CLReapGroupOverrideVlanEnable_Type.__name__ = "TruthValue"
_CLReapGroupOverrideVlanEnable_Object = MibTableColumn
cLReapGroupOverrideVlanEnable = _CLReapGroupOverrideVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 31),
    _CLReapGroupOverrideVlanEnable_Type()
)
cLReapGroupOverrideVlanEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupOverrideVlanEnable.setStatus("current")
_CLReapGroupHttpProxyIpType_Type = InetAddressType
_CLReapGroupHttpProxyIpType_Object = MibTableColumn
cLReapGroupHttpProxyIpType = _CLReapGroupHttpProxyIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 32),
    _CLReapGroupHttpProxyIpType_Type()
)
cLReapGroupHttpProxyIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupHttpProxyIpType.setStatus("current")
_CLReapGroupHttpProxyIp_Type = InetAddress
_CLReapGroupHttpProxyIp_Object = MibTableColumn
cLReapGroupHttpProxyIp = _CLReapGroupHttpProxyIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 33),
    _CLReapGroupHttpProxyIp_Type()
)
cLReapGroupHttpProxyIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupHttpProxyIp.setStatus("current")
_CLReapGroupHttpProxyPort_Type = Unsigned32
_CLReapGroupHttpProxyPort_Object = MibTableColumn
cLReapGroupHttpProxyPort = _CLReapGroupHttpProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 34),
    _CLReapGroupHttpProxyPort_Type()
)
cLReapGroupHttpProxyPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupHttpProxyPort.setStatus("current")


class _CLReapGroupVlanTemplateName_Type(SnmpAdminString):
    """Custom type cLReapGroupVlanTemplateName based on SnmpAdminString"""
    defaultValue = OctetString("")


_CLReapGroupVlanTemplateName_Type.__name__ = "SnmpAdminString"
_CLReapGroupVlanTemplateName_Object = MibTableColumn
cLReapGroupVlanTemplateName = _CLReapGroupVlanTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 35),
    _CLReapGroupVlanTemplateName_Type()
)
cLReapGroupVlanTemplateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupVlanTemplateName.setStatus("current")


class _CLReapGroupEfficientApJoinEnable_Type(TruthValue):
    """Custom type cLReapGroupEfficientApJoinEnable based on TruthValue"""
    defaultValue = 1


_CLReapGroupEfficientApJoinEnable_Type.__name__ = "TruthValue"
_CLReapGroupEfficientApJoinEnable_Object = MibTableColumn
cLReapGroupEfficientApJoinEnable = _CLReapGroupEfficientApJoinEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 36),
    _CLReapGroupEfficientApJoinEnable_Type()
)
cLReapGroupEfficientApJoinEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupEfficientApJoinEnable.setStatus("current")
_CLReapGroupRadiusServerGroupName_Type = SnmpAdminString
_CLReapGroupRadiusServerGroupName_Object = MibTableColumn
cLReapGroupRadiusServerGroupName = _CLReapGroupRadiusServerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 37),
    _CLReapGroupRadiusServerGroupName_Type()
)
cLReapGroupRadiusServerGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapGroupRadiusServerGroupName.setStatus("current")
_CLReapGroupEapFastProfileName_Type = SnmpAdminString
_CLReapGroupEapFastProfileName_Object = MibTableColumn
cLReapGroupEapFastProfileName = _CLReapGroupEapFastProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 38),
    _CLReapGroupEapFastProfileName_Type()
)
cLReapGroupEapFastProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapGroupEapFastProfileName.setStatus("current")
_CLReapGroupArpCacheEnabled_Type = TruthValue
_CLReapGroupArpCacheEnabled_Object = MibTableColumn
cLReapGroupArpCacheEnabled = _CLReapGroupArpCacheEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 39),
    _CLReapGroupArpCacheEnabled_Type()
)
cLReapGroupArpCacheEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapGroupArpCacheEnabled.setStatus("current")


class _CLReapGroupHomeApEnable_Type(TruthValue):
    """Custom type cLReapGroupHomeApEnable based on TruthValue"""
    defaultValue = 2


_CLReapGroupHomeApEnable_Type.__name__ = "TruthValue"
_CLReapGroupHomeApEnable_Object = MibTableColumn
cLReapGroupHomeApEnable = _CLReapGroupHomeApEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 40),
    _CLReapGroupHomeApEnable_Type()
)
cLReapGroupHomeApEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapGroupHomeApEnable.setStatus("current")


class _CLReapGroupLeastLatencyJoinEnable_Type(TruthValue):
    """Custom type cLReapGroupLeastLatencyJoinEnable based on TruthValue"""
    defaultValue = 2


_CLReapGroupLeastLatencyJoinEnable_Type.__name__ = "TruthValue"
_CLReapGroupLeastLatencyJoinEnable_Object = MibTableColumn
cLReapGroupLeastLatencyJoinEnable = _CLReapGroupLeastLatencyJoinEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 41),
    _CLReapGroupLeastLatencyJoinEnable_Type()
)
cLReapGroupLeastLatencyJoinEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapGroupLeastLatencyJoinEnable.setStatus("current")


class _CLReapGroupHomeApLocalSsidReset_Type(TruthValue):
    """Custom type cLReapGroupHomeApLocalSsidReset based on TruthValue"""
    defaultValue = 2


_CLReapGroupHomeApLocalSsidReset_Type.__name__ = "TruthValue"
_CLReapGroupHomeApLocalSsidReset_Object = MibTableColumn
cLReapGroupHomeApLocalSsidReset = _CLReapGroupHomeApLocalSsidReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 42),
    _CLReapGroupHomeApLocalSsidReset_Type()
)
cLReapGroupHomeApLocalSsidReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapGroupHomeApLocalSsidReset.setStatus("current")


class _CLReapGroupInstallMappingRadioBackhaul_Type(TruthValue):
    """Custom type cLReapGroupInstallMappingRadioBackhaul based on TruthValue"""
    defaultValue = 2


_CLReapGroupInstallMappingRadioBackhaul_Type.__name__ = "TruthValue"
_CLReapGroupInstallMappingRadioBackhaul_Object = MibTableColumn
cLReapGroupInstallMappingRadioBackhaul = _CLReapGroupInstallMappingRadioBackhaul_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 43),
    _CLReapGroupInstallMappingRadioBackhaul_Type()
)
cLReapGroupInstallMappingRadioBackhaul.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapGroupInstallMappingRadioBackhaul.setStatus("current")


class _CLReapGroupResilientMode_Type(TruthValue):
    """Custom type cLReapGroupResilientMode based on TruthValue"""
    defaultValue = 2


_CLReapGroupResilientMode_Type.__name__ = "TruthValue"
_CLReapGroupResilientMode_Object = MibTableColumn
cLReapGroupResilientMode = _CLReapGroupResilientMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 44),
    _CLReapGroupResilientMode_Type()
)
cLReapGroupResilientMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapGroupResilientMode.setStatus("current")


class _CLReapGroupDescription_Type(OctetString):
    """Custom type cLReapGroupDescription based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLReapGroupDescription_Type.__name__ = "OctetString"
_CLReapGroupDescription_Object = MibTableColumn
cLReapGroupDescription = _CLReapGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 45),
    _CLReapGroupDescription_Type()
)
cLReapGroupDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapGroupDescription.setStatus("current")


class _CLReapGroupFallbackRadioShutEnabled_Type(TruthValue):
    """Custom type cLReapGroupFallbackRadioShutEnabled based on TruthValue"""
    defaultValue = 2


_CLReapGroupFallbackRadioShutEnabled_Type.__name__ = "TruthValue"
_CLReapGroupFallbackRadioShutEnabled_Object = MibTableColumn
cLReapGroupFallbackRadioShutEnabled = _CLReapGroupFallbackRadioShutEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 46),
    _CLReapGroupFallbackRadioShutEnabled_Type()
)
cLReapGroupFallbackRadioShutEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapGroupFallbackRadioShutEnabled.setStatus("current")


class _CLReapCtsInlineTagging_Type(TruthValue):
    """Custom type cLReapCtsInlineTagging based on TruthValue"""
    defaultValue = 2


_CLReapCtsInlineTagging_Type.__name__ = "TruthValue"
_CLReapCtsInlineTagging_Object = MibTableColumn
cLReapCtsInlineTagging = _CLReapCtsInlineTagging_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 48),
    _CLReapCtsInlineTagging_Type()
)
cLReapCtsInlineTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapCtsInlineTagging.setStatus("current")


class _CLReapIsHomeApEnable_Type(TruthValue):
    """Custom type cLReapIsHomeApEnable based on TruthValue"""
    defaultValue = 2


_CLReapIsHomeApEnable_Type.__name__ = "TruthValue"
_CLReapIsHomeApEnable_Object = MibTableColumn
cLReapIsHomeApEnable = _CLReapIsHomeApEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 49),
    _CLReapIsHomeApEnable_Type()
)
cLReapIsHomeApEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapIsHomeApEnable.setStatus("current")


class _CLReapCtsRolebasedEnforcement_Type(TruthValue):
    """Custom type cLReapCtsRolebasedEnforcement based on TruthValue"""
    defaultValue = 2


_CLReapCtsRolebasedEnforcement_Type.__name__ = "TruthValue"
_CLReapCtsRolebasedEnforcement_Object = MibTableColumn
cLReapCtsRolebasedEnforcement = _CLReapCtsRolebasedEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 50),
    _CLReapCtsRolebasedEnforcement_Type()
)
cLReapCtsRolebasedEnforcement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapCtsRolebasedEnforcement.setStatus("current")
_CLReapCtsSxpAttachedProfileName_Type = SnmpAdminString
_CLReapCtsSxpAttachedProfileName_Object = MibTableColumn
cLReapCtsSxpAttachedProfileName = _CLReapCtsSxpAttachedProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 51),
    _CLReapCtsSxpAttachedProfileName_Type()
)
cLReapCtsSxpAttachedProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapCtsSxpAttachedProfileName.setStatus("current")
_CLReapGroupAccountingRadiusServerGroupName_Type = SnmpAdminString
_CLReapGroupAccountingRadiusServerGroupName_Object = MibTableColumn
cLReapGroupAccountingRadiusServerGroupName = _CLReapGroupAccountingRadiusServerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 52),
    _CLReapGroupAccountingRadiusServerGroupName_Type()
)
cLReapGroupAccountingRadiusServerGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapGroupAccountingRadiusServerGroupName.setStatus("current")


class _CLReapLocalRoaming_Type(TruthValue):
    """Custom type cLReapLocalRoaming based on TruthValue"""
    defaultValue = 2


_CLReapLocalRoaming_Type.__name__ = "TruthValue"
_CLReapLocalRoaming_Object = MibTableColumn
cLReapLocalRoaming = _CLReapLocalRoaming_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 53),
    _CLReapLocalRoaming_Type()
)
cLReapLocalRoaming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapLocalRoaming.setStatus("current")
_CLReapGroupMdnsFlexProfileName_Type = SnmpAdminString
_CLReapGroupMdnsFlexProfileName_Object = MibTableColumn
cLReapGroupMdnsFlexProfileName = _CLReapGroupMdnsFlexProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 54),
    _CLReapGroupMdnsFlexProfileName_Type()
)
cLReapGroupMdnsFlexProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapGroupMdnsFlexProfileName.setStatus("current")


class _CLReapIpOverlap_Type(TruthValue):
    """Custom type cLReapIpOverlap based on TruthValue"""
    defaultValue = 2


_CLReapIpOverlap_Type.__name__ = "TruthValue"
_CLReapIpOverlap_Object = MibTableColumn
cLReapIpOverlap = _CLReapIpOverlap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 55),
    _CLReapIpOverlap_Type()
)
cLReapIpOverlap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapIpOverlap.setStatus("current")


class _CLReapGroupDhcpBroadcastEnable_Type(TruthValue):
    """Custom type cLReapGroupDhcpBroadcastEnable based on TruthValue"""
    defaultValue = 2


_CLReapGroupDhcpBroadcastEnable_Type.__name__ = "TruthValue"
_CLReapGroupDhcpBroadcastEnable_Object = MibTableColumn
cLReapGroupDhcpBroadcastEnable = _CLReapGroupDhcpBroadcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 56),
    _CLReapGroupDhcpBroadcastEnable_Type()
)
cLReapGroupDhcpBroadcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapGroupDhcpBroadcastEnable.setStatus("current")
_CLReapGroupApConfigTable_Object = MibTable
cLReapGroupApConfigTable = _CLReapGroupApConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cLReapGroupApConfigTable.setStatus("current")
_CLReapGroupApConfigEntry_Object = MibTableRow
cLReapGroupApConfigEntry = _CLReapGroupApConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 2, 1)
)
cLReapGroupApConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapGroupName"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    cLReapGroupApConfigEntry.setStatus("current")
_CLReapGroupApStorageType_Type = StorageType
_CLReapGroupApStorageType_Object = MibTableColumn
cLReapGroupApStorageType = _CLReapGroupApStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 2, 1, 1),
    _CLReapGroupApStorageType_Type()
)
cLReapGroupApStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupApStorageType.setStatus("current")
_CLReapGroupApRowStatus_Type = RowStatus
_CLReapGroupApRowStatus_Object = MibTableColumn
cLReapGroupApRowStatus = _CLReapGroupApRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 2, 1, 2),
    _CLReapGroupApRowStatus_Type()
)
cLReapGroupApRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupApRowStatus.setStatus("current")


class _CLReapGroupApEntryType_Type(Integer32):
    """Custom type cLReapGroupApEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("admin", 1),
          ("cloud", 2))
    )


_CLReapGroupApEntryType_Type.__name__ = "Integer32"
_CLReapGroupApEntryType_Object = MibTableColumn
cLReapGroupApEntryType = _CLReapGroupApEntryType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 2, 1, 3),
    _CLReapGroupApEntryType_Type()
)
cLReapGroupApEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLReapGroupApEntryType.setStatus("current")
_CLReapGroupApPnPConflict_Type = TruthValue
_CLReapGroupApPnPConflict_Object = MibTableColumn
cLReapGroupApPnPConflict = _CLReapGroupApPnPConflict_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 2, 1, 4),
    _CLReapGroupApPnPConflict_Type()
)
cLReapGroupApPnPConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLReapGroupApPnPConflict.setStatus("current")
_CLReapGroupUserConfigTable_Object = MibTable
cLReapGroupUserConfigTable = _CLReapGroupUserConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cLReapGroupUserConfigTable.setStatus("current")
_CLReapGroupUserConfigEntry_Object = MibTableRow
cLReapGroupUserConfigEntry = _CLReapGroupUserConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 3, 1)
)
cLReapGroupUserConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapGroupName"),
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapGroupUserName"),
)
if mibBuilder.loadTexts:
    cLReapGroupUserConfigEntry.setStatus("current")


class _CLReapGroupUserName_Type(SnmpAdminString):
    """Custom type cLReapGroupUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_CLReapGroupUserName_Type.__name__ = "SnmpAdminString"
_CLReapGroupUserName_Object = MibTableColumn
cLReapGroupUserName = _CLReapGroupUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 3, 1, 1),
    _CLReapGroupUserName_Type()
)
cLReapGroupUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLReapGroupUserName.setStatus("current")


class _CLReapGroupUserPassword_Type(SnmpAdminString):
    """Custom type cLReapGroupUserPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CLReapGroupUserPassword_Type.__name__ = "SnmpAdminString"
_CLReapGroupUserPassword_Object = MibTableColumn
cLReapGroupUserPassword = _CLReapGroupUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 3, 1, 2),
    _CLReapGroupUserPassword_Type()
)
cLReapGroupUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupUserPassword.setStatus("current")
_CLReapGroupUserStorageType_Type = StorageType
_CLReapGroupUserStorageType_Object = MibTableColumn
cLReapGroupUserStorageType = _CLReapGroupUserStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 3, 1, 3),
    _CLReapGroupUserStorageType_Type()
)
cLReapGroupUserStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupUserStorageType.setStatus("current")
_CLReapGroupUserRowStatus_Type = RowStatus
_CLReapGroupUserRowStatus_Object = MibTableColumn
cLReapGroupUserRowStatus = _CLReapGroupUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 3, 1, 4),
    _CLReapGroupUserRowStatus_Type()
)
cLReapGroupUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupUserRowStatus.setStatus("current")
_CLReapGroupVlanAclTable_Object = MibTable
cLReapGroupVlanAclTable = _CLReapGroupVlanAclTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 4)
)
if mibBuilder.loadTexts:
    cLReapGroupVlanAclTable.setStatus("current")
_CLReapGroupVlanAclEntry_Object = MibTableRow
cLReapGroupVlanAclEntry = _CLReapGroupVlanAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 4, 1)
)
cLReapGroupVlanAclEntry.setIndexNames(
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapGroupName"),
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapGroupVlanId"),
)
if mibBuilder.loadTexts:
    cLReapGroupVlanAclEntry.setStatus("current")


class _CLReapGroupVlanId_Type(Unsigned32):
    """Custom type cLReapGroupVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_CLReapGroupVlanId_Type.__name__ = "Unsigned32"
_CLReapGroupVlanId_Object = MibTableColumn
cLReapGroupVlanId = _CLReapGroupVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 4, 1, 1),
    _CLReapGroupVlanId_Type()
)
cLReapGroupVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLReapGroupVlanId.setStatus("current")


class _CLReapGroupIngressAcl_Type(SnmpAdminString):
    """Custom type cLReapGroupIngressAcl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLReapGroupIngressAcl_Type.__name__ = "SnmpAdminString"
_CLReapGroupIngressAcl_Object = MibTableColumn
cLReapGroupIngressAcl = _CLReapGroupIngressAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 4, 1, 2),
    _CLReapGroupIngressAcl_Type()
)
cLReapGroupIngressAcl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupIngressAcl.setStatus("current")


class _CLReapGroupEgressAcl_Type(SnmpAdminString):
    """Custom type cLReapGroupEgressAcl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLReapGroupEgressAcl_Type.__name__ = "SnmpAdminString"
_CLReapGroupEgressAcl_Object = MibTableColumn
cLReapGroupEgressAcl = _CLReapGroupEgressAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 4, 1, 3),
    _CLReapGroupEgressAcl_Type()
)
cLReapGroupEgressAcl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupEgressAcl.setStatus("current")
_CLReapGroupVlanAclRowStatus_Type = RowStatus
_CLReapGroupVlanAclRowStatus_Object = MibTableColumn
cLReapGroupVlanAclRowStatus = _CLReapGroupVlanAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 4, 1, 4),
    _CLReapGroupVlanAclRowStatus_Type()
)
cLReapGroupVlanAclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupVlanAclRowStatus.setStatus("current")
_CLReapGroupVlanOrder_Type = Unsigned32
_CLReapGroupVlanOrder_Object = MibTableColumn
cLReapGroupVlanOrder = _CLReapGroupVlanOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 4, 1, 5),
    _CLReapGroupVlanOrder_Type()
)
cLReapGroupVlanOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLReapGroupVlanOrder.setStatus("current")
_CLReapGroupAclTable_Object = MibTable
cLReapGroupAclTable = _CLReapGroupAclTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 5)
)
if mibBuilder.loadTexts:
    cLReapGroupAclTable.setStatus("current")
_CLReapGroupAclEntry_Object = MibTableRow
cLReapGroupAclEntry = _CLReapGroupAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 5, 1)
)
cLReapGroupAclEntry.setIndexNames(
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapGroupName"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLReapGroupAclEntry.setStatus("current")


class _CLReapGroupWebAuthAcl_Type(SnmpAdminString):
    """Custom type cLReapGroupWebAuthAcl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLReapGroupWebAuthAcl_Type.__name__ = "SnmpAdminString"
_CLReapGroupWebAuthAcl_Object = MibTableColumn
cLReapGroupWebAuthAcl = _CLReapGroupWebAuthAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 5, 1, 1),
    _CLReapGroupWebAuthAcl_Type()
)
cLReapGroupWebAuthAcl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupWebAuthAcl.setStatus("current")
_CLReapGroupAclRowStatus_Type = RowStatus
_CLReapGroupAclRowStatus_Object = MibTableColumn
cLReapGroupAclRowStatus = _CLReapGroupAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 5, 1, 2),
    _CLReapGroupAclRowStatus_Type()
)
cLReapGroupAclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupAclRowStatus.setStatus("current")


class _CLReapGroupWebAuthIpv6Acl_Type(SnmpAdminString):
    """Custom type cLReapGroupWebAuthIpv6Acl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLReapGroupWebAuthIpv6Acl_Type.__name__ = "SnmpAdminString"
_CLReapGroupWebAuthIpv6Acl_Object = MibTableColumn
cLReapGroupWebAuthIpv6Acl = _CLReapGroupWebAuthIpv6Acl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 5, 1, 3),
    _CLReapGroupWebAuthIpv6Acl_Type()
)
cLReapGroupWebAuthIpv6Acl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupWebAuthIpv6Acl.setStatus("current")
_CLReapGroupWebPolicyAclTable_Object = MibTable
cLReapGroupWebPolicyAclTable = _CLReapGroupWebPolicyAclTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 6)
)
if mibBuilder.loadTexts:
    cLReapGroupWebPolicyAclTable.setStatus("current")
_CLReapGroupWebPolicyAclEntry_Object = MibTableRow
cLReapGroupWebPolicyAclEntry = _CLReapGroupWebPolicyAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 6, 1)
)
cLReapGroupWebPolicyAclEntry.setIndexNames(
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapGroupName"),
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapGroupWebPolicyAcl"),
)
if mibBuilder.loadTexts:
    cLReapGroupWebPolicyAclEntry.setStatus("current")


class _CLReapGroupWebPolicyAcl_Type(SnmpAdminString):
    """Custom type cLReapGroupWebPolicyAcl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLReapGroupWebPolicyAcl_Type.__name__ = "SnmpAdminString"
_CLReapGroupWebPolicyAcl_Object = MibTableColumn
cLReapGroupWebPolicyAcl = _CLReapGroupWebPolicyAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 6, 1, 1),
    _CLReapGroupWebPolicyAcl_Type()
)
cLReapGroupWebPolicyAcl.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLReapGroupWebPolicyAcl.setStatus("current")
_CLReapGroupWebPolicyAclRowStatus_Type = RowStatus
_CLReapGroupWebPolicyAclRowStatus_Object = MibTableColumn
cLReapGroupWebPolicyAclRowStatus = _CLReapGroupWebPolicyAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 6, 1, 2),
    _CLReapGroupWebPolicyAclRowStatus_Type()
)
cLReapGroupWebPolicyAclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupWebPolicyAclRowStatus.setStatus("current")


class _CLReapGroupWebPolicyAclType_Type(Integer32):
    """Custom type cLReapGroupWebPolicyAclType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_CLReapGroupWebPolicyAclType_Type.__name__ = "Integer32"
_CLReapGroupWebPolicyAclType_Object = MibTableColumn
cLReapGroupWebPolicyAclType = _CLReapGroupWebPolicyAclType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 6, 1, 3),
    _CLReapGroupWebPolicyAclType_Type()
)
cLReapGroupWebPolicyAclType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupWebPolicyAclType.setStatus("current")


class _CLReapGroupWebPolicyAclCentWebAuth_Type(TruthValue):
    """Custom type cLReapGroupWebPolicyAclCentWebAuth based on TruthValue"""
    defaultValue = 2


_CLReapGroupWebPolicyAclCentWebAuth_Type.__name__ = "TruthValue"
_CLReapGroupWebPolicyAclCentWebAuth_Object = MibTableColumn
cLReapGroupWebPolicyAclCentWebAuth = _CLReapGroupWebPolicyAclCentWebAuth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 6, 1, 4),
    _CLReapGroupWebPolicyAclCentWebAuth_Type()
)
cLReapGroupWebPolicyAclCentWebAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapGroupWebPolicyAclCentWebAuth.setStatus("current")
_CLReapGroupLocalSplitAclTable_Object = MibTable
cLReapGroupLocalSplitAclTable = _CLReapGroupLocalSplitAclTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 7)
)
if mibBuilder.loadTexts:
    cLReapGroupLocalSplitAclTable.setStatus("current")
_CLReapGroupLocalSplitAclEntry_Object = MibTableRow
cLReapGroupLocalSplitAclEntry = _CLReapGroupLocalSplitAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 7, 1)
)
cLReapGroupLocalSplitAclEntry.setIndexNames(
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapGroupName"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLReapGroupLocalSplitAclEntry.setStatus("current")


class _CLReapGroupLocalSplitAcl_Type(SnmpAdminString):
    """Custom type cLReapGroupLocalSplitAcl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLReapGroupLocalSplitAcl_Type.__name__ = "SnmpAdminString"
_CLReapGroupLocalSplitAcl_Object = MibTableColumn
cLReapGroupLocalSplitAcl = _CLReapGroupLocalSplitAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 7, 1, 1),
    _CLReapGroupLocalSplitAcl_Type()
)
cLReapGroupLocalSplitAcl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupLocalSplitAcl.setStatus("current")
_CLReapGroupLocalSplitAclRowStatus_Type = RowStatus
_CLReapGroupLocalSplitAclRowStatus_Object = MibTableColumn
cLReapGroupLocalSplitAclRowStatus = _CLReapGroupLocalSplitAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 7, 1, 2),
    _CLReapGroupLocalSplitAclRowStatus_Type()
)
cLReapGroupLocalSplitAclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupLocalSplitAclRowStatus.setStatus("current")
_CLReapGroupCentralDhcpTable_Object = MibTable
cLReapGroupCentralDhcpTable = _CLReapGroupCentralDhcpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 8)
)
if mibBuilder.loadTexts:
    cLReapGroupCentralDhcpTable.setStatus("current")
_CLReapGroupCentralDhcpEntry_Object = MibTableRow
cLReapGroupCentralDhcpEntry = _CLReapGroupCentralDhcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 8, 1)
)
cLReapGroupCentralDhcpEntry.setIndexNames(
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapGroupName"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLReapGroupCentralDhcpEntry.setStatus("current")


class _CLReapGroupDhcpCentral_Type(TruthValue):
    """Custom type cLReapGroupDhcpCentral based on TruthValue"""
    defaultValue = 2


_CLReapGroupDhcpCentral_Type.__name__ = "TruthValue"
_CLReapGroupDhcpCentral_Object = MibTableColumn
cLReapGroupDhcpCentral = _CLReapGroupDhcpCentral_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 8, 1, 1),
    _CLReapGroupDhcpCentral_Type()
)
cLReapGroupDhcpCentral.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupDhcpCentral.setStatus("current")


class _CLReapGroupDhcpOverrideDNS_Type(TruthValue):
    """Custom type cLReapGroupDhcpOverrideDNS based on TruthValue"""
    defaultValue = 2


_CLReapGroupDhcpOverrideDNS_Type.__name__ = "TruthValue"
_CLReapGroupDhcpOverrideDNS_Object = MibTableColumn
cLReapGroupDhcpOverrideDNS = _CLReapGroupDhcpOverrideDNS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 8, 1, 2),
    _CLReapGroupDhcpOverrideDNS_Type()
)
cLReapGroupDhcpOverrideDNS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupDhcpOverrideDNS.setStatus("current")


class _CLReapGroupNatPatEnabled_Type(TruthValue):
    """Custom type cLReapGroupNatPatEnabled based on TruthValue"""
    defaultValue = 2


_CLReapGroupNatPatEnabled_Type.__name__ = "TruthValue"
_CLReapGroupNatPatEnabled_Object = MibTableColumn
cLReapGroupNatPatEnabled = _CLReapGroupNatPatEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 8, 1, 3),
    _CLReapGroupNatPatEnabled_Type()
)
cLReapGroupNatPatEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupNatPatEnabled.setStatus("current")
_CLReapGroupDhcpRowStatus_Type = RowStatus
_CLReapGroupDhcpRowStatus_Object = MibTableColumn
cLReapGroupDhcpRowStatus = _CLReapGroupDhcpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 8, 1, 4),
    _CLReapGroupDhcpRowStatus_Type()
)
cLReapGroupDhcpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupDhcpRowStatus.setStatus("current")
_CLReapGroupVlanIdTable_Object = MibTable
cLReapGroupVlanIdTable = _CLReapGroupVlanIdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 9)
)
if mibBuilder.loadTexts:
    cLReapGroupVlanIdTable.setStatus("current")
_CLReapGroupVlanIdEntry_Object = MibTableRow
cLReapGroupVlanIdEntry = _CLReapGroupVlanIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 9, 1)
)
cLReapGroupVlanIdEntry.setIndexNames(
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapGroupName"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLReapGroupVlanIdEntry.setStatus("current")


class _CLReapGroupWlanVlanId_Type(Unsigned32):
    """Custom type cLReapGroupWlanVlanId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_CLReapGroupWlanVlanId_Type.__name__ = "Unsigned32"
_CLReapGroupWlanVlanId_Object = MibTableColumn
cLReapGroupWlanVlanId = _CLReapGroupWlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 9, 1, 1),
    _CLReapGroupWlanVlanId_Type()
)
cLReapGroupWlanVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupWlanVlanId.setStatus("current")
_CLReapGroupVlanRowStatus_Type = RowStatus
_CLReapGroupVlanRowStatus_Object = MibTableColumn
cLReapGroupVlanRowStatus = _CLReapGroupVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 9, 1, 2),
    _CLReapGroupVlanRowStatus_Type()
)
cLReapGroupVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupVlanRowStatus.setStatus("current")
_CLReapGroupAVCFlexTable_Object = MibTable
cLReapGroupAVCFlexTable = _CLReapGroupAVCFlexTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 10)
)
if mibBuilder.loadTexts:
    cLReapGroupAVCFlexTable.setStatus("current")
_CLReapGroupAVCFlexEntry_Object = MibTableRow
cLReapGroupAVCFlexEntry = _CLReapGroupAVCFlexEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 10, 1)
)
cLReapGroupAVCFlexEntry.setIndexNames(
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapGroupName"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLReapGroupAVCFlexEntry.setStatus("current")


class _CLReapGroupAVCFlexProfileName_Type(SnmpAdminString):
    """Custom type cLReapGroupAVCFlexProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLReapGroupAVCFlexProfileName_Type.__name__ = "SnmpAdminString"
_CLReapGroupAVCFlexProfileName_Object = MibTableColumn
cLReapGroupAVCFlexProfileName = _CLReapGroupAVCFlexProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 10, 1, 1),
    _CLReapGroupAVCFlexProfileName_Type()
)
cLReapGroupAVCFlexProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupAVCFlexProfileName.setStatus("current")


class _CLReapGroupNbarStatsVisibilityEnable_Type(Integer32):
    """Custom type cLReapGroupNbarStatsVisibilityEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("wlan-specific", 3))
    )


_CLReapGroupNbarStatsVisibilityEnable_Type.__name__ = "Integer32"
_CLReapGroupNbarStatsVisibilityEnable_Object = MibTableColumn
cLReapGroupNbarStatsVisibilityEnable = _CLReapGroupNbarStatsVisibilityEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 10, 1, 2),
    _CLReapGroupNbarStatsVisibilityEnable_Type()
)
cLReapGroupNbarStatsVisibilityEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupNbarStatsVisibilityEnable.setStatus("current")
_CLReapGroupAVCFlexRowStatus_Type = RowStatus
_CLReapGroupAVCFlexRowStatus_Object = MibTableColumn
cLReapGroupAVCFlexRowStatus = _CLReapGroupAVCFlexRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 10, 1, 3),
    _CLReapGroupAVCFlexRowStatus_Type()
)
cLReapGroupAVCFlexRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupAVCFlexRowStatus.setStatus("current")
_CLReapGroupVlanNameAclTable_Object = MibTable
cLReapGroupVlanNameAclTable = _CLReapGroupVlanNameAclTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 11)
)
if mibBuilder.loadTexts:
    cLReapGroupVlanNameAclTable.setStatus("current")
_CLReapGroupVlanNameAclEntry_Object = MibTableRow
cLReapGroupVlanNameAclEntry = _CLReapGroupVlanNameAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 11, 1)
)
cLReapGroupVlanNameAclEntry.setIndexNames(
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapGroupName"),
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapGroupVlanName"),
)
if mibBuilder.loadTexts:
    cLReapGroupVlanNameAclEntry.setStatus("current")


class _CLReapGroupVlanName_Type(SnmpAdminString):
    """Custom type cLReapGroupVlanName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLReapGroupVlanName_Type.__name__ = "SnmpAdminString"
_CLReapGroupVlanName_Object = MibTableColumn
cLReapGroupVlanName = _CLReapGroupVlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 11, 1, 1),
    _CLReapGroupVlanName_Type()
)
cLReapGroupVlanName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLReapGroupVlanName.setStatus("current")


class _CLReapGroupVlanIdentifier_Type(Unsigned32):
    """Custom type cLReapGroupVlanIdentifier based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_CLReapGroupVlanIdentifier_Type.__name__ = "Unsigned32"
_CLReapGroupVlanIdentifier_Object = MibTableColumn
cLReapGroupVlanIdentifier = _CLReapGroupVlanIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 11, 1, 2),
    _CLReapGroupVlanIdentifier_Type()
)
cLReapGroupVlanIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapGroupVlanIdentifier.setStatus("current")


class _CLReapGroupAcl_Type(SnmpAdminString):
    """Custom type cLReapGroupAcl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLReapGroupAcl_Type.__name__ = "SnmpAdminString"
_CLReapGroupAcl_Object = MibTableColumn
cLReapGroupAcl = _CLReapGroupAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 11, 1, 3),
    _CLReapGroupAcl_Type()
)
cLReapGroupAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapGroupAcl.setStatus("current")


class _CLReapGroupVlanNameAclType_Type(Integer32):
    """Custom type cLReapGroupVlanNameAclType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("apSource", 1),
          ("groupSource", 2))
    )


_CLReapGroupVlanNameAclType_Type.__name__ = "Integer32"
_CLReapGroupVlanNameAclType_Object = MibTableColumn
cLReapGroupVlanNameAclType = _CLReapGroupVlanNameAclType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 11, 1, 4),
    _CLReapGroupVlanNameAclType_Type()
)
cLReapGroupVlanNameAclType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLReapGroupVlanNameAclType.setStatus("current")
_CLReapGroupVlanNameAclRowStatus_Type = RowStatus
_CLReapGroupVlanNameAclRowStatus_Object = MibTableColumn
cLReapGroupVlanNameAclRowStatus = _CLReapGroupVlanNameAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 11, 1, 5),
    _CLReapGroupVlanNameAclRowStatus_Type()
)
cLReapGroupVlanNameAclRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapGroupVlanNameAclRowStatus.setStatus("current")


class _CLReapGroupAclIn_Type(SnmpAdminString):
    """Custom type cLReapGroupAclIn based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLReapGroupAclIn_Type.__name__ = "SnmpAdminString"
_CLReapGroupAclIn_Object = MibTableColumn
cLReapGroupAclIn = _CLReapGroupAclIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 11, 1, 6),
    _CLReapGroupAclIn_Type()
)
cLReapGroupAclIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapGroupAclIn.setStatus("current")


class _CLReapGroupAclOut_Type(SnmpAdminString):
    """Custom type cLReapGroupAclOut based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLReapGroupAclOut_Type.__name__ = "SnmpAdminString"
_CLReapGroupAclOut_Object = MibTableColumn
cLReapGroupAclOut = _CLReapGroupAclOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 11, 1, 7),
    _CLReapGroupAclOut_Type()
)
cLReapGroupAclOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapGroupAclOut.setStatus("current")
_CLReapGroupCtsSxpTable_Object = MibTable
cLReapGroupCtsSxpTable = _CLReapGroupCtsSxpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 12)
)
if mibBuilder.loadTexts:
    cLReapGroupCtsSxpTable.setStatus("current")
_CLReapGroupCtsSxpEntry_Object = MibTableRow
cLReapGroupCtsSxpEntry = _CLReapGroupCtsSxpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 12, 1)
)
cLReapGroupCtsSxpEntry.setIndexNames(
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapCtsSxpConfigProfileName"),
)
if mibBuilder.loadTexts:
    cLReapGroupCtsSxpEntry.setStatus("current")


class _CLReapCtsSxpConfigProfileName_Type(SnmpAdminString):
    """Custom type cLReapCtsSxpConfigProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLReapCtsSxpConfigProfileName_Type.__name__ = "SnmpAdminString"
_CLReapCtsSxpConfigProfileName_Object = MibTableColumn
cLReapCtsSxpConfigProfileName = _CLReapCtsSxpConfigProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 12, 1, 1),
    _CLReapCtsSxpConfigProfileName_Type()
)
cLReapCtsSxpConfigProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLReapCtsSxpConfigProfileName.setStatus("current")
_CLReapCtsSxpDefaultPassword_Type = SnmpAdminString
_CLReapCtsSxpDefaultPassword_Object = MibTableColumn
cLReapCtsSxpDefaultPassword = _CLReapCtsSxpDefaultPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 12, 1, 2),
    _CLReapCtsSxpDefaultPassword_Type()
)
cLReapCtsSxpDefaultPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapCtsSxpDefaultPassword.setStatus("current")
_CLReapCtsSxpState_Type = TruthValue
_CLReapCtsSxpState_Object = MibTableColumn
cLReapCtsSxpState = _CLReapCtsSxpState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 12, 1, 3),
    _CLReapCtsSxpState_Type()
)
cLReapCtsSxpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapCtsSxpState.setStatus("current")


class _CLReapCtsSxpListenerMinHoldTime_Type(Unsigned32):
    """Custom type cLReapCtsSxpListenerMinHoldTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_CLReapCtsSxpListenerMinHoldTime_Type.__name__ = "Unsigned32"
_CLReapCtsSxpListenerMinHoldTime_Object = MibTableColumn
cLReapCtsSxpListenerMinHoldTime = _CLReapCtsSxpListenerMinHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 12, 1, 4),
    _CLReapCtsSxpListenerMinHoldTime_Type()
)
cLReapCtsSxpListenerMinHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapCtsSxpListenerMinHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    cLReapCtsSxpListenerMinHoldTime.setUnits("seconds")


class _CLReapCtsSxpListenerMaxHoldTime_Type(Unsigned32):
    """Custom type cLReapCtsSxpListenerMaxHoldTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_CLReapCtsSxpListenerMaxHoldTime_Type.__name__ = "Unsigned32"
_CLReapCtsSxpListenerMaxHoldTime_Object = MibTableColumn
cLReapCtsSxpListenerMaxHoldTime = _CLReapCtsSxpListenerMaxHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 12, 1, 5),
    _CLReapCtsSxpListenerMaxHoldTime_Type()
)
cLReapCtsSxpListenerMaxHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapCtsSxpListenerMaxHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    cLReapCtsSxpListenerMaxHoldTime.setUnits("seconds")


class _CLReapCtsSxpReconcilePeriod_Type(Unsigned32):
    """Custom type cLReapCtsSxpReconcilePeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000),
    )


_CLReapCtsSxpReconcilePeriod_Type.__name__ = "Unsigned32"
_CLReapCtsSxpReconcilePeriod_Object = MibTableColumn
cLReapCtsSxpReconcilePeriod = _CLReapCtsSxpReconcilePeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 12, 1, 6),
    _CLReapCtsSxpReconcilePeriod_Type()
)
cLReapCtsSxpReconcilePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapCtsSxpReconcilePeriod.setStatus("current")
if mibBuilder.loadTexts:
    cLReapCtsSxpReconcilePeriod.setUnits("seconds")


class _CLReapCtsSxpRetryPeriod_Type(Unsigned32):
    """Custom type cLReapCtsSxpRetryPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000),
    )


_CLReapCtsSxpRetryPeriod_Type.__name__ = "Unsigned32"
_CLReapCtsSxpRetryPeriod_Object = MibTableColumn
cLReapCtsSxpRetryPeriod = _CLReapCtsSxpRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 12, 1, 7),
    _CLReapCtsSxpRetryPeriod_Type()
)
cLReapCtsSxpRetryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapCtsSxpRetryPeriod.setStatus("current")
if mibBuilder.loadTexts:
    cLReapCtsSxpRetryPeriod.setUnits("seconds")


class _CLReapCtsSxpSpeakerMinHoldTime_Type(Unsigned32):
    """Custom type cLReapCtsSxpSpeakerMinHoldTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_CLReapCtsSxpSpeakerMinHoldTime_Type.__name__ = "Unsigned32"
_CLReapCtsSxpSpeakerMinHoldTime_Object = MibTableColumn
cLReapCtsSxpSpeakerMinHoldTime = _CLReapCtsSxpSpeakerMinHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 12, 1, 8),
    _CLReapCtsSxpSpeakerMinHoldTime_Type()
)
cLReapCtsSxpSpeakerMinHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapCtsSxpSpeakerMinHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    cLReapCtsSxpSpeakerMinHoldTime.setUnits("seconds")
_CLReapCtsSxpRowStatus_Type = RowStatus
_CLReapCtsSxpRowStatus_Object = MibTableColumn
cLReapCtsSxpRowStatus = _CLReapCtsSxpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 12, 1, 9),
    _CLReapCtsSxpRowStatus_Type()
)
cLReapCtsSxpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapCtsSxpRowStatus.setStatus("current")
_CLReapCtsSxpPeerTable_Object = MibTable
cLReapCtsSxpPeerTable = _CLReapCtsSxpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 13)
)
if mibBuilder.loadTexts:
    cLReapCtsSxpPeerTable.setStatus("current")
_CLReapCtsSxpPeerEntry_Object = MibTableRow
cLReapCtsSxpPeerEntry = _CLReapCtsSxpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 13, 1)
)
cLReapCtsSxpPeerEntry.setIndexNames(
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapCtsSxpConfigProfileName"),
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapCtsSxpPeerIpType"),
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapCtsSxpPeerIp"),
)
if mibBuilder.loadTexts:
    cLReapCtsSxpPeerEntry.setStatus("current")
_CLReapCtsSxpPeerIpType_Type = InetAddressType
_CLReapCtsSxpPeerIpType_Object = MibTableColumn
cLReapCtsSxpPeerIpType = _CLReapCtsSxpPeerIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 13, 1, 1),
    _CLReapCtsSxpPeerIpType_Type()
)
cLReapCtsSxpPeerIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLReapCtsSxpPeerIpType.setStatus("current")


class _CLReapCtsSxpPeerIp_Type(InetAddress):
    """Custom type cLReapCtsSxpPeerIp based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CLReapCtsSxpPeerIp_Type.__name__ = "InetAddress"
_CLReapCtsSxpPeerIp_Object = MibTableColumn
cLReapCtsSxpPeerIp = _CLReapCtsSxpPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 13, 1, 2),
    _CLReapCtsSxpPeerIp_Type()
)
cLReapCtsSxpPeerIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLReapCtsSxpPeerIp.setStatus("current")


class _CLReapCtsSxpMode_Type(Integer32):
    """Custom type cLReapCtsSxpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("speaker", 1),
          ("listener", 2),
          ("both", 3))
    )


_CLReapCtsSxpMode_Type.__name__ = "Integer32"
_CLReapCtsSxpMode_Object = MibTableColumn
cLReapCtsSxpMode = _CLReapCtsSxpMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 13, 1, 3),
    _CLReapCtsSxpMode_Type()
)
cLReapCtsSxpMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapCtsSxpMode.setStatus("current")


class _CLReapCtsSxpPeerPassword_Type(Integer32):
    """Custom type cLReapCtsSxpPeerPassword based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notRequired", 0),
          ("default", 2))
    )


_CLReapCtsSxpPeerPassword_Type.__name__ = "Integer32"
_CLReapCtsSxpPeerPassword_Object = MibTableColumn
cLReapCtsSxpPeerPassword = _CLReapCtsSxpPeerPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 13, 1, 4),
    _CLReapCtsSxpPeerPassword_Type()
)
cLReapCtsSxpPeerPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapCtsSxpPeerPassword.setStatus("current")
_CLReapCtsSxpPeerRowStatus_Type = RowStatus
_CLReapCtsSxpPeerRowStatus_Object = MibTableColumn
cLReapCtsSxpPeerRowStatus = _CLReapCtsSxpPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 13, 1, 5),
    _CLReapCtsSxpPeerRowStatus_Type()
)
cLReapCtsSxpPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapCtsSxpPeerRowStatus.setStatus("current")
_CiscoLwappReapAclConfig_ObjectIdentity = ObjectIdentity
ciscoLwappReapAclConfig = _CiscoLwappReapAclConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4)
)
_CLReapAclTable_Object = MibTable
cLReapAclTable = _CLReapAclTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cLReapAclTable.setStatus("current")
_CLReapAclEntry_Object = MibTableRow
cLReapAclEntry = _CLReapAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 1, 1)
)
cLReapAclEntry.setIndexNames(
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapAclName"),
)
if mibBuilder.loadTexts:
    cLReapAclEntry.setStatus("current")


class _CLReapAclName_Type(SnmpAdminString):
    """Custom type cLReapAclName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLReapAclName_Type.__name__ = "SnmpAdminString"
_CLReapAclName_Object = MibTableColumn
cLReapAclName = _CLReapAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 1, 1, 1),
    _CLReapAclName_Type()
)
cLReapAclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLReapAclName.setStatus("current")


class _CLReapAclApplyMode_Type(Integer32):
    """Custom type cLReapAclApplyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notapplied", 0),
          ("applied", 1))
    )


_CLReapAclApplyMode_Type.__name__ = "Integer32"
_CLReapAclApplyMode_Object = MibTableColumn
cLReapAclApplyMode = _CLReapAclApplyMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 1, 1, 2),
    _CLReapAclApplyMode_Type()
)
cLReapAclApplyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLReapAclApplyMode.setStatus("current")
_CLReapAclRowStatus_Type = RowStatus
_CLReapAclRowStatus_Object = MibTableColumn
cLReapAclRowStatus = _CLReapAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 1, 1, 3),
    _CLReapAclRowStatus_Type()
)
cLReapAclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapAclRowStatus.setStatus("current")


class _CLReapAclUrlDomainListType_Type(Integer32):
    """Custom type cLReapAclUrlDomainListType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blackList", 1),
          ("whiteList", 2))
    )


_CLReapAclUrlDomainListType_Type.__name__ = "Integer32"
_CLReapAclUrlDomainListType_Object = MibTableColumn
cLReapAclUrlDomainListType = _CLReapAclUrlDomainListType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 1, 1, 4),
    _CLReapAclUrlDomainListType_Type()
)
cLReapAclUrlDomainListType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapAclUrlDomainListType.setStatus("deprecated")
_CLReapAclRuleTable_Object = MibTable
cLReapAclRuleTable = _CLReapAclRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cLReapAclRuleTable.setStatus("current")
_CLReapAclRuleEntry_Object = MibTableRow
cLReapAclRuleEntry = _CLReapAclRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 2, 1)
)
cLReapAclRuleEntry.setIndexNames(
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapAclName"),
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapAclRuleIndex"),
)
if mibBuilder.loadTexts:
    cLReapAclRuleEntry.setStatus("current")


class _CLReapAclRuleIndex_Type(Unsigned32):
    """Custom type cLReapAclRuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_CLReapAclRuleIndex_Type.__name__ = "Unsigned32"
_CLReapAclRuleIndex_Object = MibTableColumn
cLReapAclRuleIndex = _CLReapAclRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 2, 1, 1),
    _CLReapAclRuleIndex_Type()
)
cLReapAclRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLReapAclRuleIndex.setStatus("current")


class _CLReapAclRuleAction_Type(Integer32):
    """Custom type cLReapAclRuleAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )


_CLReapAclRuleAction_Type.__name__ = "Integer32"
_CLReapAclRuleAction_Object = MibTableColumn
cLReapAclRuleAction = _CLReapAclRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 2, 1, 2),
    _CLReapAclRuleAction_Type()
)
cLReapAclRuleAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapAclRuleAction.setStatus("current")
_CLReapAclRuleSourceIpAddressType_Type = InetAddressType
_CLReapAclRuleSourceIpAddressType_Object = MibTableColumn
cLReapAclRuleSourceIpAddressType = _CLReapAclRuleSourceIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 2, 1, 3),
    _CLReapAclRuleSourceIpAddressType_Type()
)
cLReapAclRuleSourceIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapAclRuleSourceIpAddressType.setStatus("current")
_CLReapAclRuleSourceIpAddress_Type = InetAddress
_CLReapAclRuleSourceIpAddress_Object = MibTableColumn
cLReapAclRuleSourceIpAddress = _CLReapAclRuleSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 2, 1, 4),
    _CLReapAclRuleSourceIpAddress_Type()
)
cLReapAclRuleSourceIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapAclRuleSourceIpAddress.setStatus("current")
_CLReapAclRuleSourceIpNetmaskType_Type = InetAddressType
_CLReapAclRuleSourceIpNetmaskType_Object = MibTableColumn
cLReapAclRuleSourceIpNetmaskType = _CLReapAclRuleSourceIpNetmaskType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 2, 1, 5),
    _CLReapAclRuleSourceIpNetmaskType_Type()
)
cLReapAclRuleSourceIpNetmaskType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapAclRuleSourceIpNetmaskType.setStatus("current")
_CLReapAclRuleSourceIpNetmask_Type = InetAddress
_CLReapAclRuleSourceIpNetmask_Object = MibTableColumn
cLReapAclRuleSourceIpNetmask = _CLReapAclRuleSourceIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 2, 1, 6),
    _CLReapAclRuleSourceIpNetmask_Type()
)
cLReapAclRuleSourceIpNetmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapAclRuleSourceIpNetmask.setStatus("current")
_CLReapAclRuleDestinationIpAddressType_Type = InetAddressType
_CLReapAclRuleDestinationIpAddressType_Object = MibTableColumn
cLReapAclRuleDestinationIpAddressType = _CLReapAclRuleDestinationIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 2, 1, 7),
    _CLReapAclRuleDestinationIpAddressType_Type()
)
cLReapAclRuleDestinationIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapAclRuleDestinationIpAddressType.setStatus("current")
_CLReapAclRuleDestinationIpAddress_Type = InetAddress
_CLReapAclRuleDestinationIpAddress_Object = MibTableColumn
cLReapAclRuleDestinationIpAddress = _CLReapAclRuleDestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 2, 1, 8),
    _CLReapAclRuleDestinationIpAddress_Type()
)
cLReapAclRuleDestinationIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapAclRuleDestinationIpAddress.setStatus("current")
_CLReapAclRuleDestinationIpNetmaskType_Type = InetAddressType
_CLReapAclRuleDestinationIpNetmaskType_Object = MibTableColumn
cLReapAclRuleDestinationIpNetmaskType = _CLReapAclRuleDestinationIpNetmaskType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 2, 1, 9),
    _CLReapAclRuleDestinationIpNetmaskType_Type()
)
cLReapAclRuleDestinationIpNetmaskType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapAclRuleDestinationIpNetmaskType.setStatus("current")
_CLReapAclRuleDestinationIpNetmask_Type = InetAddress
_CLReapAclRuleDestinationIpNetmask_Object = MibTableColumn
cLReapAclRuleDestinationIpNetmask = _CLReapAclRuleDestinationIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 2, 1, 10),
    _CLReapAclRuleDestinationIpNetmask_Type()
)
cLReapAclRuleDestinationIpNetmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapAclRuleDestinationIpNetmask.setStatus("current")


class _CLReapAclRuleProtocol_Type(Unsigned32):
    """Custom type cLReapAclRuleProtocol based on Unsigned32"""
    defaultValue = 256

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_CLReapAclRuleProtocol_Type.__name__ = "Unsigned32"
_CLReapAclRuleProtocol_Object = MibTableColumn
cLReapAclRuleProtocol = _CLReapAclRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 2, 1, 11),
    _CLReapAclRuleProtocol_Type()
)
cLReapAclRuleProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapAclRuleProtocol.setStatus("current")


class _CLReapAclRuleStartSourcePort_Type(Unsigned32):
    """Custom type cLReapAclRuleStartSourcePort based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CLReapAclRuleStartSourcePort_Type.__name__ = "Unsigned32"
_CLReapAclRuleStartSourcePort_Object = MibTableColumn
cLReapAclRuleStartSourcePort = _CLReapAclRuleStartSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 2, 1, 12),
    _CLReapAclRuleStartSourcePort_Type()
)
cLReapAclRuleStartSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapAclRuleStartSourcePort.setStatus("current")


class _CLReapAclRuleEndSourcePort_Type(Unsigned32):
    """Custom type cLReapAclRuleEndSourcePort based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CLReapAclRuleEndSourcePort_Type.__name__ = "Unsigned32"
_CLReapAclRuleEndSourcePort_Object = MibTableColumn
cLReapAclRuleEndSourcePort = _CLReapAclRuleEndSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 2, 1, 13),
    _CLReapAclRuleEndSourcePort_Type()
)
cLReapAclRuleEndSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapAclRuleEndSourcePort.setStatus("current")


class _CLReapAclRuleStartDestinationPort_Type(Unsigned32):
    """Custom type cLReapAclRuleStartDestinationPort based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CLReapAclRuleStartDestinationPort_Type.__name__ = "Unsigned32"
_CLReapAclRuleStartDestinationPort_Object = MibTableColumn
cLReapAclRuleStartDestinationPort = _CLReapAclRuleStartDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 2, 1, 14),
    _CLReapAclRuleStartDestinationPort_Type()
)
cLReapAclRuleStartDestinationPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapAclRuleStartDestinationPort.setStatus("current")


class _CLReapAclRuleEndDestinationPort_Type(Unsigned32):
    """Custom type cLReapAclRuleEndDestinationPort based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CLReapAclRuleEndDestinationPort_Type.__name__ = "Unsigned32"
_CLReapAclRuleEndDestinationPort_Object = MibTableColumn
cLReapAclRuleEndDestinationPort = _CLReapAclRuleEndDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 2, 1, 15),
    _CLReapAclRuleEndDestinationPort_Type()
)
cLReapAclRuleEndDestinationPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapAclRuleEndDestinationPort.setStatus("current")


class _CLReapAclRuleDscp_Type(Unsigned32):
    """Custom type cLReapAclRuleDscp based on Unsigned32"""
    defaultValue = 256

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_CLReapAclRuleDscp_Type.__name__ = "Unsigned32"
_CLReapAclRuleDscp_Object = MibTableColumn
cLReapAclRuleDscp = _CLReapAclRuleDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 2, 1, 16),
    _CLReapAclRuleDscp_Type()
)
cLReapAclRuleDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapAclRuleDscp.setStatus("current")


class _CLReapAclNewRuleIndex_Type(Unsigned32):
    """Custom type cLReapAclNewRuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_CLReapAclNewRuleIndex_Type.__name__ = "Unsigned32"
_CLReapAclNewRuleIndex_Object = MibTableColumn
cLReapAclNewRuleIndex = _CLReapAclNewRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 2, 1, 17),
    _CLReapAclNewRuleIndex_Type()
)
cLReapAclNewRuleIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapAclNewRuleIndex.setStatus("current")
_CLReapAclRuleRowStatus_Type = RowStatus
_CLReapAclRuleRowStatus_Object = MibTableColumn
cLReapAclRuleRowStatus = _CLReapAclRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 2, 1, 18),
    _CLReapAclRuleRowStatus_Type()
)
cLReapAclRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapAclRuleRowStatus.setStatus("current")
_CLReapL2AclTable_Object = MibTable
cLReapL2AclTable = _CLReapL2AclTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 3)
)
if mibBuilder.loadTexts:
    cLReapL2AclTable.setStatus("current")
_CLReapL2AclEntry_Object = MibTableRow
cLReapL2AclEntry = _CLReapL2AclEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 3, 1)
)
cLReapL2AclEntry.setIndexNames(
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapL2AclName"),
)
if mibBuilder.loadTexts:
    cLReapL2AclEntry.setStatus("current")


class _CLReapL2AclName_Type(SnmpAdminString):
    """Custom type cLReapL2AclName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLReapL2AclName_Type.__name__ = "SnmpAdminString"
_CLReapL2AclName_Object = MibTableColumn
cLReapL2AclName = _CLReapL2AclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 3, 1, 1),
    _CLReapL2AclName_Type()
)
cLReapL2AclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLReapL2AclName.setStatus("current")


class _CLReapL2AclApplyMode_Type(Integer32):
    """Custom type cLReapL2AclApplyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notapplied", 1),
          ("applied", 2))
    )


_CLReapL2AclApplyMode_Type.__name__ = "Integer32"
_CLReapL2AclApplyMode_Object = MibTableColumn
cLReapL2AclApplyMode = _CLReapL2AclApplyMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 3, 1, 2),
    _CLReapL2AclApplyMode_Type()
)
cLReapL2AclApplyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLReapL2AclApplyMode.setStatus("current")
_CLReapL2AclRowStatus_Type = RowStatus
_CLReapL2AclRowStatus_Object = MibTableColumn
cLReapL2AclRowStatus = _CLReapL2AclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 3, 1, 3),
    _CLReapL2AclRowStatus_Type()
)
cLReapL2AclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapL2AclRowStatus.setStatus("current")
_CLReapL2AclRuleTable_Object = MibTable
cLReapL2AclRuleTable = _CLReapL2AclRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 4)
)
if mibBuilder.loadTexts:
    cLReapL2AclRuleTable.setStatus("current")
_CLReapL2AclRuleEntry_Object = MibTableRow
cLReapL2AclRuleEntry = _CLReapL2AclRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 4, 1)
)
cLReapL2AclRuleEntry.setIndexNames(
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapL2AclName"),
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapL2AclRuleIndex"),
)
if mibBuilder.loadTexts:
    cLReapL2AclRuleEntry.setStatus("current")
_CLReapL2AclRuleIndex_Type = Unsigned32
_CLReapL2AclRuleIndex_Object = MibTableColumn
cLReapL2AclRuleIndex = _CLReapL2AclRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 4, 1, 1),
    _CLReapL2AclRuleIndex_Type()
)
cLReapL2AclRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLReapL2AclRuleIndex.setStatus("current")


class _CLReapL2AclRuleAction_Type(Integer32):
    """Custom type cLReapL2AclRuleAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_CLReapL2AclRuleAction_Type.__name__ = "Integer32"
_CLReapL2AclRuleAction_Object = MibTableColumn
cLReapL2AclRuleAction = _CLReapL2AclRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 4, 1, 2),
    _CLReapL2AclRuleAction_Type()
)
cLReapL2AclRuleAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapL2AclRuleAction.setStatus("current")


class _CLReapL2AclRuleEthertype_Type(Unsigned32):
    """Custom type cLReapL2AclRuleEthertype based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CLReapL2AclRuleEthertype_Type.__name__ = "Unsigned32"
_CLReapL2AclRuleEthertype_Object = MibTableColumn
cLReapL2AclRuleEthertype = _CLReapL2AclRuleEthertype_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 4, 1, 3),
    _CLReapL2AclRuleEthertype_Type()
)
cLReapL2AclRuleEthertype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapL2AclRuleEthertype.setStatus("current")


class _CLReapL2AclRuleEthertypeMask_Type(Unsigned32):
    """Custom type cLReapL2AclRuleEthertypeMask based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CLReapL2AclRuleEthertypeMask_Type.__name__ = "Unsigned32"
_CLReapL2AclRuleEthertypeMask_Object = MibTableColumn
cLReapL2AclRuleEthertypeMask = _CLReapL2AclRuleEthertypeMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 4, 1, 4),
    _CLReapL2AclRuleEthertypeMask_Type()
)
cLReapL2AclRuleEthertypeMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapL2AclRuleEthertypeMask.setStatus("current")


class _CLReapL2AclRuleDirection_Type(Integer32):
    """Custom type cLReapL2AclRuleDirection based on Integer32"""
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
        *(("inbound", 1),
          ("outbound", 2),
          ("any", 3))
    )


_CLReapL2AclRuleDirection_Type.__name__ = "Integer32"
_CLReapL2AclRuleDirection_Object = MibTableColumn
cLReapL2AclRuleDirection = _CLReapL2AclRuleDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 4, 1, 5),
    _CLReapL2AclRuleDirection_Type()
)
cLReapL2AclRuleDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapL2AclRuleDirection.setStatus("current")


class _CLReapL2AclNewRuleIndex_Type(Unsigned32):
    """Custom type cLReapL2AclNewRuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_CLReapL2AclNewRuleIndex_Type.__name__ = "Unsigned32"
_CLReapL2AclNewRuleIndex_Object = MibTableColumn
cLReapL2AclNewRuleIndex = _CLReapL2AclNewRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 4, 1, 6),
    _CLReapL2AclNewRuleIndex_Type()
)
cLReapL2AclNewRuleIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapL2AclNewRuleIndex.setStatus("current")
_CLReapL2AclRuleRowStatus_Type = RowStatus
_CLReapL2AclRuleRowStatus_Object = MibTableColumn
cLReapL2AclRuleRowStatus = _CLReapL2AclRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 4, 1, 7),
    _CLReapL2AclRuleRowStatus_Type()
)
cLReapL2AclRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapL2AclRuleRowStatus.setStatus("current")
_CLReapAclUrlDomainRuleTable_Object = MibTable
cLReapAclUrlDomainRuleTable = _CLReapAclUrlDomainRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 5)
)
if mibBuilder.loadTexts:
    cLReapAclUrlDomainRuleTable.setStatus("current")
_CLReapAclUrlDomainRuleEntry_Object = MibTableRow
cLReapAclUrlDomainRuleEntry = _CLReapAclUrlDomainRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 5, 1)
)
cLReapAclUrlDomainRuleEntry.setIndexNames(
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapAclName"),
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapAclUrlDomainRuleIndex"),
)
if mibBuilder.loadTexts:
    cLReapAclUrlDomainRuleEntry.setStatus("current")


class _CLReapAclUrlDomainRuleIndex_Type(Unsigned32):
    """Custom type cLReapAclUrlDomainRuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CLReapAclUrlDomainRuleIndex_Type.__name__ = "Unsigned32"
_CLReapAclUrlDomainRuleIndex_Object = MibTableColumn
cLReapAclUrlDomainRuleIndex = _CLReapAclUrlDomainRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 5, 1, 1),
    _CLReapAclUrlDomainRuleIndex_Type()
)
cLReapAclUrlDomainRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLReapAclUrlDomainRuleIndex.setStatus("current")
_CLReapAclUrlDomainRuleUrl_Type = SnmpAdminString
_CLReapAclUrlDomainRuleUrl_Object = MibTableColumn
cLReapAclUrlDomainRuleUrl = _CLReapAclUrlDomainRuleUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 5, 1, 2),
    _CLReapAclUrlDomainRuleUrl_Type()
)
cLReapAclUrlDomainRuleUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapAclUrlDomainRuleUrl.setStatus("current")


class _CLReapAclUrlDomainRuleAction_Type(Integer32):
    """Custom type cLReapAclUrlDomainRuleAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_CLReapAclUrlDomainRuleAction_Type.__name__ = "Integer32"
_CLReapAclUrlDomainRuleAction_Object = MibTableColumn
cLReapAclUrlDomainRuleAction = _CLReapAclUrlDomainRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 5, 1, 3),
    _CLReapAclUrlDomainRuleAction_Type()
)
cLReapAclUrlDomainRuleAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapAclUrlDomainRuleAction.setStatus("current")
_CLReapAclUrlDomainRuleRowStatus_Type = RowStatus
_CLReapAclUrlDomainRuleRowStatus_Object = MibTableColumn
cLReapAclUrlDomainRuleRowStatus = _CLReapAclUrlDomainRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 5, 1, 4),
    _CLReapAclUrlDomainRuleRowStatus_Type()
)
cLReapAclUrlDomainRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapAclUrlDomainRuleRowStatus.setStatus("current")
_CLReapUrlDomainListTable_Object = MibTable
cLReapUrlDomainListTable = _CLReapUrlDomainListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 6)
)
if mibBuilder.loadTexts:
    cLReapUrlDomainListTable.setStatus("current")
_CLReapUrlDomainListEntry_Object = MibTableRow
cLReapUrlDomainListEntry = _CLReapUrlDomainListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 6, 1)
)
cLReapUrlDomainListEntry.setIndexNames(
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapUrlListName"),
)
if mibBuilder.loadTexts:
    cLReapUrlDomainListEntry.setStatus("current")


class _CLReapUrlListName_Type(SnmpAdminString):
    """Custom type cLReapUrlListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLReapUrlListName_Type.__name__ = "SnmpAdminString"
_CLReapUrlListName_Object = MibTableColumn
cLReapUrlListName = _CLReapUrlListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 6, 1, 1),
    _CLReapUrlListName_Type()
)
cLReapUrlListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLReapUrlListName.setStatus("current")


class _CLReapUrlDomainRuleAction_Type(Integer32):
    """Custom type cLReapUrlDomainRuleAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_CLReapUrlDomainRuleAction_Type.__name__ = "Integer32"
_CLReapUrlDomainRuleAction_Object = MibTableColumn
cLReapUrlDomainRuleAction = _CLReapUrlDomainRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 6, 1, 2),
    _CLReapUrlDomainRuleAction_Type()
)
cLReapUrlDomainRuleAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLReapUrlDomainRuleAction.setStatus("current")
_CLReapUrlRedirectServerIpv4Type_Type = InetAddressType
_CLReapUrlRedirectServerIpv4Type_Object = MibTableColumn
cLReapUrlRedirectServerIpv4Type = _CLReapUrlRedirectServerIpv4Type_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 6, 1, 3),
    _CLReapUrlRedirectServerIpv4Type_Type()
)
cLReapUrlRedirectServerIpv4Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapUrlRedirectServerIpv4Type.setStatus("current")
_CLReapUrlRedirectServerIpv4_Type = InetAddress
_CLReapUrlRedirectServerIpv4_Object = MibTableColumn
cLReapUrlRedirectServerIpv4 = _CLReapUrlRedirectServerIpv4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 6, 1, 4),
    _CLReapUrlRedirectServerIpv4_Type()
)
cLReapUrlRedirectServerIpv4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapUrlRedirectServerIpv4.setStatus("current")
_CLReapUrlRedirectServerIpv6Type_Type = InetAddressType
_CLReapUrlRedirectServerIpv6Type_Object = MibTableColumn
cLReapUrlRedirectServerIpv6Type = _CLReapUrlRedirectServerIpv6Type_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 6, 1, 5),
    _CLReapUrlRedirectServerIpv6Type_Type()
)
cLReapUrlRedirectServerIpv6Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapUrlRedirectServerIpv6Type.setStatus("current")
_CLReapUrlRedirectServerIpv6_Type = InetAddress
_CLReapUrlRedirectServerIpv6_Object = MibTableColumn
cLReapUrlRedirectServerIpv6 = _CLReapUrlRedirectServerIpv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 6, 1, 6),
    _CLReapUrlRedirectServerIpv6_Type()
)
cLReapUrlRedirectServerIpv6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapUrlRedirectServerIpv6.setStatus("current")
_CLReapUrlDomainRuleRowStatus_Type = RowStatus
_CLReapUrlDomainRuleRowStatus_Object = MibTableColumn
cLReapUrlDomainRuleRowStatus = _CLReapUrlDomainRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 6, 1, 7),
    _CLReapUrlDomainRuleRowStatus_Type()
)
cLReapUrlDomainRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapUrlDomainRuleRowStatus.setStatus("current")


class _CLReapUrlFilterID_Type(Unsigned32):
    """Custom type cLReapUrlFilterID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CLReapUrlFilterID_Type.__name__ = "Unsigned32"
_CLReapUrlFilterID_Object = MibTableColumn
cLReapUrlFilterID = _CLReapUrlFilterID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 6, 1, 8),
    _CLReapUrlFilterID_Type()
)
cLReapUrlFilterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLReapUrlFilterID.setStatus("current")
_CLReapUrlDomainRulesTable_Object = MibTable
cLReapUrlDomainRulesTable = _CLReapUrlDomainRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 7)
)
if mibBuilder.loadTexts:
    cLReapUrlDomainRulesTable.setStatus("current")
_CLReapUrlDomainRulesEntry_Object = MibTableRow
cLReapUrlDomainRulesEntry = _CLReapUrlDomainRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 7, 1)
)
cLReapUrlDomainRulesEntry.setIndexNames(
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapUrlListName"),
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapUrlDomainRuleUrl"),
)
if mibBuilder.loadTexts:
    cLReapUrlDomainRulesEntry.setStatus("current")


class _CLReapUrlDomainRuleUrl_Type(SnmpAdminString):
    """Custom type cLReapUrlDomainRuleUrl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CLReapUrlDomainRuleUrl_Type.__name__ = "SnmpAdminString"
_CLReapUrlDomainRuleUrl_Object = MibTableColumn
cLReapUrlDomainRuleUrl = _CLReapUrlDomainRuleUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 7, 1, 1),
    _CLReapUrlDomainRuleUrl_Type()
)
cLReapUrlDomainRuleUrl.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLReapUrlDomainRuleUrl.setStatus("current")
_CLReapUrlRowStatus_Type = RowStatus
_CLReapUrlRowStatus_Object = MibTableColumn
cLReapUrlRowStatus = _CLReapUrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 7, 1, 2),
    _CLReapUrlRowStatus_Type()
)
cLReapUrlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapUrlRowStatus.setStatus("current")
_CLReapEnhancedUrlDomainListTable_Object = MibTable
cLReapEnhancedUrlDomainListTable = _CLReapEnhancedUrlDomainListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 8)
)
if mibBuilder.loadTexts:
    cLReapEnhancedUrlDomainListTable.setStatus("current")
_CLReapEnhancedUrlDomainListEntry_Object = MibTableRow
cLReapEnhancedUrlDomainListEntry = _CLReapEnhancedUrlDomainListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 8, 1)
)
cLReapEnhancedUrlDomainListEntry.setIndexNames(
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapEnhancedUrlDomainListName"),
)
if mibBuilder.loadTexts:
    cLReapEnhancedUrlDomainListEntry.setStatus("current")


class _CLReapEnhancedUrlDomainListName_Type(SnmpAdminString):
    """Custom type cLReapEnhancedUrlDomainListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLReapEnhancedUrlDomainListName_Type.__name__ = "SnmpAdminString"
_CLReapEnhancedUrlDomainListName_Object = MibTableColumn
cLReapEnhancedUrlDomainListName = _CLReapEnhancedUrlDomainListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 8, 1, 1),
    _CLReapEnhancedUrlDomainListName_Type()
)
cLReapEnhancedUrlDomainListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLReapEnhancedUrlDomainListName.setStatus("current")
_CLReapEnhancedUrlDomainListRowStatus_Type = RowStatus
_CLReapEnhancedUrlDomainListRowStatus_Object = MibTableColumn
cLReapEnhancedUrlDomainListRowStatus = _CLReapEnhancedUrlDomainListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 8, 1, 2),
    _CLReapEnhancedUrlDomainListRowStatus_Type()
)
cLReapEnhancedUrlDomainListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapEnhancedUrlDomainListRowStatus.setStatus("current")
_CLReapEnhancedUrlDomainRulesTable_Object = MibTable
cLReapEnhancedUrlDomainRulesTable = _CLReapEnhancedUrlDomainRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 9)
)
if mibBuilder.loadTexts:
    cLReapEnhancedUrlDomainRulesTable.setStatus("current")
_CLReapEnhancedUrlDomainRulesEntry_Object = MibTableRow
cLReapEnhancedUrlDomainRulesEntry = _CLReapEnhancedUrlDomainRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 9, 1)
)
cLReapEnhancedUrlDomainRulesEntry.setIndexNames(
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapEnhancedUrlDomainListName"),
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapEnhancedUrlDomainRuleUrl"),
)
if mibBuilder.loadTexts:
    cLReapEnhancedUrlDomainRulesEntry.setStatus("current")


class _CLReapEnhancedUrlDomainRuleUrl_Type(SnmpAdminString):
    """Custom type cLReapEnhancedUrlDomainRuleUrl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CLReapEnhancedUrlDomainRuleUrl_Type.__name__ = "SnmpAdminString"
_CLReapEnhancedUrlDomainRuleUrl_Object = MibTableColumn
cLReapEnhancedUrlDomainRuleUrl = _CLReapEnhancedUrlDomainRuleUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 9, 1, 1),
    _CLReapEnhancedUrlDomainRuleUrl_Type()
)
cLReapEnhancedUrlDomainRuleUrl.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLReapEnhancedUrlDomainRuleUrl.setStatus("current")


class _CLReapEnhancedUrlDomainRuleAction_Type(Integer32):
    """Custom type cLReapEnhancedUrlDomainRuleAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_CLReapEnhancedUrlDomainRuleAction_Type.__name__ = "Integer32"
_CLReapEnhancedUrlDomainRuleAction_Object = MibTableColumn
cLReapEnhancedUrlDomainRuleAction = _CLReapEnhancedUrlDomainRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 9, 1, 2),
    _CLReapEnhancedUrlDomainRuleAction_Type()
)
cLReapEnhancedUrlDomainRuleAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapEnhancedUrlDomainRuleAction.setStatus("current")
_CLReapEnhancedUrlDomainRulePreference_Type = Unsigned32
_CLReapEnhancedUrlDomainRulePreference_Object = MibTableColumn
cLReapEnhancedUrlDomainRulePreference = _CLReapEnhancedUrlDomainRulePreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 9, 1, 3),
    _CLReapEnhancedUrlDomainRulePreference_Type()
)
cLReapEnhancedUrlDomainRulePreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapEnhancedUrlDomainRulePreference.setStatus("current")
_CLReapEnhancedUrlDomainRuleRowStatus_Type = RowStatus
_CLReapEnhancedUrlDomainRuleRowStatus_Object = MibTableColumn
cLReapEnhancedUrlDomainRuleRowStatus = _CLReapEnhancedUrlDomainRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 4, 9, 1, 4),
    _CLReapEnhancedUrlDomainRuleRowStatus_Type()
)
cLReapEnhancedUrlDomainRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapEnhancedUrlDomainRuleRowStatus.setStatus("current")
_CiscoLwappReapMasterApConfig_ObjectIdentity = ObjectIdentity
ciscoLwappReapMasterApConfig = _CiscoLwappReapMasterApConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 5)
)
_CLReapMasterApConfigTable_Object = MibTable
cLReapMasterApConfigTable = _CLReapMasterApConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cLReapMasterApConfigTable.setStatus("current")
_CLReapMasterApConfigEntry_Object = MibTableRow
cLReapMasterApConfigEntry = _CLReapMasterApConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 5, 1, 1)
)
cLReapMasterApConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapGroupName"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    cLReapMasterApConfigEntry.setStatus("current")
_CLReapMasterApModel_Type = SnmpAdminString
_CLReapMasterApModel_Object = MibTableColumn
cLReapMasterApModel = _CLReapMasterApModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 5, 1, 1, 1),
    _CLReapMasterApModel_Type()
)
cLReapMasterApModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLReapMasterApModel.setStatus("current")
_CLReapMasterApManual_Type = TruthValue
_CLReapMasterApManual_Object = MibTableColumn
cLReapMasterApManual = _CLReapMasterApManual_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 5, 1, 1, 2),
    _CLReapMasterApManual_Type()
)
cLReapMasterApManual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLReapMasterApManual.setStatus("current")
_CLReapMasterApRowStatus_Type = RowStatus
_CLReapMasterApRowStatus_Object = MibTableColumn
cLReapMasterApRowStatus = _CLReapMasterApRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 5, 1, 1, 3),
    _CLReapMasterApRowStatus_Type()
)
cLReapMasterApRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapMasterApRowStatus.setStatus("current")
_CiscoLwappReapGlobalConfig_ObjectIdentity = ObjectIdentity
ciscoLwappReapGlobalConfig = _CiscoLwappReapGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 6)
)
_CLReapArpCaheEnabled_Type = TruthValue
_CLReapArpCaheEnabled_Object = MibScalar
cLReapArpCaheEnabled = _CLReapArpCaheEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 6, 1),
    _CLReapArpCaheEnabled_Type()
)
cLReapArpCaheEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapArpCaheEnabled.setStatus("current")
_CiscoLwappReapIpv6AclConfig_ObjectIdentity = ObjectIdentity
ciscoLwappReapIpv6AclConfig = _CiscoLwappReapIpv6AclConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 7)
)
_CLReapIpv6AclTable_Object = MibTable
cLReapIpv6AclTable = _CLReapIpv6AclTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 7, 1)
)
if mibBuilder.loadTexts:
    cLReapIpv6AclTable.setStatus("current")
_CLReapIpv6AclEntry_Object = MibTableRow
cLReapIpv6AclEntry = _CLReapIpv6AclEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 7, 1, 1)
)
cLReapIpv6AclEntry.setIndexNames(
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapIpv6AclName"),
)
if mibBuilder.loadTexts:
    cLReapIpv6AclEntry.setStatus("current")


class _CLReapIpv6AclName_Type(SnmpAdminString):
    """Custom type cLReapIpv6AclName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLReapIpv6AclName_Type.__name__ = "SnmpAdminString"
_CLReapIpv6AclName_Object = MibTableColumn
cLReapIpv6AclName = _CLReapIpv6AclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 7, 1, 1, 1),
    _CLReapIpv6AclName_Type()
)
cLReapIpv6AclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLReapIpv6AclName.setStatus("current")


class _CLReapIpv6AclApplyMode_Type(Integer32):
    """Custom type cLReapIpv6AclApplyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notapplied", 1),
          ("applied", 2))
    )


_CLReapIpv6AclApplyMode_Type.__name__ = "Integer32"
_CLReapIpv6AclApplyMode_Object = MibTableColumn
cLReapIpv6AclApplyMode = _CLReapIpv6AclApplyMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 7, 1, 1, 2),
    _CLReapIpv6AclApplyMode_Type()
)
cLReapIpv6AclApplyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLReapIpv6AclApplyMode.setStatus("current")
_CLReapIpv6AclRowStatus_Type = RowStatus
_CLReapIpv6AclRowStatus_Object = MibTableColumn
cLReapIpv6AclRowStatus = _CLReapIpv6AclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 7, 1, 1, 3),
    _CLReapIpv6AclRowStatus_Type()
)
cLReapIpv6AclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapIpv6AclRowStatus.setStatus("current")
_CLReapIpv6AclRuleTable_Object = MibTable
cLReapIpv6AclRuleTable = _CLReapIpv6AclRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 7, 2)
)
if mibBuilder.loadTexts:
    cLReapIpv6AclRuleTable.setStatus("current")
_CLReapIpv6AclRuleEntry_Object = MibTableRow
cLReapIpv6AclRuleEntry = _CLReapIpv6AclRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 7, 2, 1)
)
cLReapIpv6AclRuleEntry.setIndexNames(
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapIpv6AclName"),
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapIpv6AclRuleIndex"),
)
if mibBuilder.loadTexts:
    cLReapIpv6AclRuleEntry.setStatus("current")


class _CLReapIpv6AclRuleIndex_Type(Unsigned32):
    """Custom type cLReapIpv6AclRuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_CLReapIpv6AclRuleIndex_Type.__name__ = "Unsigned32"
_CLReapIpv6AclRuleIndex_Object = MibTableColumn
cLReapIpv6AclRuleIndex = _CLReapIpv6AclRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 7, 2, 1, 1),
    _CLReapIpv6AclRuleIndex_Type()
)
cLReapIpv6AclRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLReapIpv6AclRuleIndex.setStatus("current")


class _CLReapIpv6AclRuleAction_Type(Integer32):
    """Custom type cLReapIpv6AclRuleAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_CLReapIpv6AclRuleAction_Type.__name__ = "Integer32"
_CLReapIpv6AclRuleAction_Object = MibTableColumn
cLReapIpv6AclRuleAction = _CLReapIpv6AclRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 7, 2, 1, 2),
    _CLReapIpv6AclRuleAction_Type()
)
cLReapIpv6AclRuleAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapIpv6AclRuleAction.setStatus("current")
_CLReapIpv6AclRuleSourceAddressType_Type = InetAddressType
_CLReapIpv6AclRuleSourceAddressType_Object = MibTableColumn
cLReapIpv6AclRuleSourceAddressType = _CLReapIpv6AclRuleSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 7, 2, 1, 3),
    _CLReapIpv6AclRuleSourceAddressType_Type()
)
cLReapIpv6AclRuleSourceAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapIpv6AclRuleSourceAddressType.setStatus("current")
_CLReapIpv6AclRuleSourceAddress_Type = InetAddress
_CLReapIpv6AclRuleSourceAddress_Object = MibTableColumn
cLReapIpv6AclRuleSourceAddress = _CLReapIpv6AclRuleSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 7, 2, 1, 4),
    _CLReapIpv6AclRuleSourceAddress_Type()
)
cLReapIpv6AclRuleSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapIpv6AclRuleSourceAddress.setStatus("current")
_CLReapIpv6AclRuleSourcePrefixLength_Type = InetAddressPrefixLength
_CLReapIpv6AclRuleSourcePrefixLength_Object = MibTableColumn
cLReapIpv6AclRuleSourcePrefixLength = _CLReapIpv6AclRuleSourcePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 7, 2, 1, 5),
    _CLReapIpv6AclRuleSourcePrefixLength_Type()
)
cLReapIpv6AclRuleSourcePrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapIpv6AclRuleSourcePrefixLength.setStatus("current")
_CLReapIpv6AclRuleDestinationAddressType_Type = InetAddressType
_CLReapIpv6AclRuleDestinationAddressType_Object = MibTableColumn
cLReapIpv6AclRuleDestinationAddressType = _CLReapIpv6AclRuleDestinationAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 7, 2, 1, 6),
    _CLReapIpv6AclRuleDestinationAddressType_Type()
)
cLReapIpv6AclRuleDestinationAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapIpv6AclRuleDestinationAddressType.setStatus("current")
_CLReapIpv6AclRuleDestinationAddress_Type = InetAddress
_CLReapIpv6AclRuleDestinationAddress_Object = MibTableColumn
cLReapIpv6AclRuleDestinationAddress = _CLReapIpv6AclRuleDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 7, 2, 1, 7),
    _CLReapIpv6AclRuleDestinationAddress_Type()
)
cLReapIpv6AclRuleDestinationAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapIpv6AclRuleDestinationAddress.setStatus("current")
_CLReapIpv6AclRuleDestinationPrefixLength_Type = InetAddressPrefixLength
_CLReapIpv6AclRuleDestinationPrefixLength_Object = MibTableColumn
cLReapIpv6AclRuleDestinationPrefixLength = _CLReapIpv6AclRuleDestinationPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 7, 2, 1, 8),
    _CLReapIpv6AclRuleDestinationPrefixLength_Type()
)
cLReapIpv6AclRuleDestinationPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapIpv6AclRuleDestinationPrefixLength.setStatus("current")


class _CLReapIpv6AclRuleProtocol_Type(Unsigned32):
    """Custom type cLReapIpv6AclRuleProtocol based on Unsigned32"""
    defaultValue = 256

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_CLReapIpv6AclRuleProtocol_Type.__name__ = "Unsigned32"
_CLReapIpv6AclRuleProtocol_Object = MibTableColumn
cLReapIpv6AclRuleProtocol = _CLReapIpv6AclRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 7, 2, 1, 9),
    _CLReapIpv6AclRuleProtocol_Type()
)
cLReapIpv6AclRuleProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapIpv6AclRuleProtocol.setStatus("current")


class _CLReapIpv6AclRuleStartSourcePort_Type(InetPortNumber):
    """Custom type cLReapIpv6AclRuleStartSourcePort based on InetPortNumber"""
    defaultValue = 0


_CLReapIpv6AclRuleStartSourcePort_Type.__name__ = "InetPortNumber"
_CLReapIpv6AclRuleStartSourcePort_Object = MibTableColumn
cLReapIpv6AclRuleStartSourcePort = _CLReapIpv6AclRuleStartSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 7, 2, 1, 10),
    _CLReapIpv6AclRuleStartSourcePort_Type()
)
cLReapIpv6AclRuleStartSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapIpv6AclRuleStartSourcePort.setStatus("current")


class _CLReapIpv6AclRuleEndSourcePort_Type(InetPortNumber):
    """Custom type cLReapIpv6AclRuleEndSourcePort based on InetPortNumber"""
    defaultValue = 65535


_CLReapIpv6AclRuleEndSourcePort_Type.__name__ = "InetPortNumber"
_CLReapIpv6AclRuleEndSourcePort_Object = MibTableColumn
cLReapIpv6AclRuleEndSourcePort = _CLReapIpv6AclRuleEndSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 7, 2, 1, 11),
    _CLReapIpv6AclRuleEndSourcePort_Type()
)
cLReapIpv6AclRuleEndSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapIpv6AclRuleEndSourcePort.setStatus("current")


class _CLReapIpv6AclRuleStartDestinationPort_Type(InetPortNumber):
    """Custom type cLReapIpv6AclRuleStartDestinationPort based on InetPortNumber"""
    defaultValue = 0


_CLReapIpv6AclRuleStartDestinationPort_Type.__name__ = "InetPortNumber"
_CLReapIpv6AclRuleStartDestinationPort_Object = MibTableColumn
cLReapIpv6AclRuleStartDestinationPort = _CLReapIpv6AclRuleStartDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 7, 2, 1, 12),
    _CLReapIpv6AclRuleStartDestinationPort_Type()
)
cLReapIpv6AclRuleStartDestinationPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapIpv6AclRuleStartDestinationPort.setStatus("current")


class _CLReapIpv6AclRuleEndDestinationPort_Type(InetPortNumber):
    """Custom type cLReapIpv6AclRuleEndDestinationPort based on InetPortNumber"""
    defaultValue = 65535


_CLReapIpv6AclRuleEndDestinationPort_Type.__name__ = "InetPortNumber"
_CLReapIpv6AclRuleEndDestinationPort_Object = MibTableColumn
cLReapIpv6AclRuleEndDestinationPort = _CLReapIpv6AclRuleEndDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 7, 2, 1, 13),
    _CLReapIpv6AclRuleEndDestinationPort_Type()
)
cLReapIpv6AclRuleEndDestinationPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapIpv6AclRuleEndDestinationPort.setStatus("current")


class _CLReapIpv6AclRuleDscp_Type(Unsigned32):
    """Custom type cLReapIpv6AclRuleDscp based on Unsigned32"""
    defaultValue = 256

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_CLReapIpv6AclRuleDscp_Type.__name__ = "Unsigned32"
_CLReapIpv6AclRuleDscp_Object = MibTableColumn
cLReapIpv6AclRuleDscp = _CLReapIpv6AclRuleDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 7, 2, 1, 14),
    _CLReapIpv6AclRuleDscp_Type()
)
cLReapIpv6AclRuleDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapIpv6AclRuleDscp.setStatus("current")


class _CLReapIpv6AclNewRuleIndex_Type(Unsigned32):
    """Custom type cLReapIpv6AclNewRuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_CLReapIpv6AclNewRuleIndex_Type.__name__ = "Unsigned32"
_CLReapIpv6AclNewRuleIndex_Object = MibTableColumn
cLReapIpv6AclNewRuleIndex = _CLReapIpv6AclNewRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 7, 2, 1, 15),
    _CLReapIpv6AclNewRuleIndex_Type()
)
cLReapIpv6AclNewRuleIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapIpv6AclNewRuleIndex.setStatus("current")
_CLReapIpv6AclRuleRowStatus_Type = RowStatus
_CLReapIpv6AclRuleRowStatus_Object = MibTableColumn
cLReapIpv6AclRuleRowStatus = _CLReapIpv6AclRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 7, 2, 1, 16),
    _CLReapIpv6AclRuleRowStatus_Type()
)
cLReapIpv6AclRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapIpv6AclRuleRowStatus.setStatus("current")
_CLReapIpv6AclUrlDomainRuleTable_Object = MibTable
cLReapIpv6AclUrlDomainRuleTable = _CLReapIpv6AclUrlDomainRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 7, 3)
)
if mibBuilder.loadTexts:
    cLReapIpv6AclUrlDomainRuleTable.setStatus("current")
_CLReapIpv6AclUrlDomainRuleEntry_Object = MibTableRow
cLReapIpv6AclUrlDomainRuleEntry = _CLReapIpv6AclUrlDomainRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 7, 3, 1)
)
cLReapIpv6AclUrlDomainRuleEntry.setIndexNames(
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapIpv6AclName"),
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapIpv6AclUrlDomainRuleIndex"),
)
if mibBuilder.loadTexts:
    cLReapIpv6AclUrlDomainRuleEntry.setStatus("current")


class _CLReapIpv6AclUrlDomainRuleIndex_Type(Unsigned32):
    """Custom type cLReapIpv6AclUrlDomainRuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CLReapIpv6AclUrlDomainRuleIndex_Type.__name__ = "Unsigned32"
_CLReapIpv6AclUrlDomainRuleIndex_Object = MibTableColumn
cLReapIpv6AclUrlDomainRuleIndex = _CLReapIpv6AclUrlDomainRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 7, 3, 1, 1),
    _CLReapIpv6AclUrlDomainRuleIndex_Type()
)
cLReapIpv6AclUrlDomainRuleIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapIpv6AclUrlDomainRuleIndex.setStatus("current")
_CLReapIpv6AclUrlDomainRuleUrl_Type = SnmpAdminString
_CLReapIpv6AclUrlDomainRuleUrl_Object = MibTableColumn
cLReapIpv6AclUrlDomainRuleUrl = _CLReapIpv6AclUrlDomainRuleUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 7, 3, 1, 2),
    _CLReapIpv6AclUrlDomainRuleUrl_Type()
)
cLReapIpv6AclUrlDomainRuleUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapIpv6AclUrlDomainRuleUrl.setStatus("current")


class _CLReapIpv6AclUrlDomainRuleAction_Type(Integer32):
    """Custom type cLReapIpv6AclUrlDomainRuleAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_CLReapIpv6AclUrlDomainRuleAction_Type.__name__ = "Integer32"
_CLReapIpv6AclUrlDomainRuleAction_Object = MibTableColumn
cLReapIpv6AclUrlDomainRuleAction = _CLReapIpv6AclUrlDomainRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 7, 3, 1, 3),
    _CLReapIpv6AclUrlDomainRuleAction_Type()
)
cLReapIpv6AclUrlDomainRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapIpv6AclUrlDomainRuleAction.setStatus("current")
_CLReapIpv6AclUrlDomainRuleRowStatus_Type = RowStatus
_CLReapIpv6AclUrlDomainRuleRowStatus_Object = MibTableColumn
cLReapIpv6AclUrlDomainRuleRowStatus = _CLReapIpv6AclUrlDomainRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 7, 3, 1, 4),
    _CLReapIpv6AclUrlDomainRuleRowStatus_Type()
)
cLReapIpv6AclUrlDomainRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapIpv6AclUrlDomainRuleRowStatus.setStatus("current")
_CiscoLwappReapVlanConfig_ObjectIdentity = ObjectIdentity
ciscoLwappReapVlanConfig = _CiscoLwappReapVlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 8)
)
_CLReapVlanIdNameMapTable_Object = MibTable
cLReapVlanIdNameMapTable = _CLReapVlanIdNameMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 8, 1)
)
if mibBuilder.loadTexts:
    cLReapVlanIdNameMapTable.setStatus("current")
_CLReapVlanIdNameMapEntry_Object = MibTableRow
cLReapVlanIdNameMapEntry = _CLReapVlanIdNameMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 8, 1, 1)
)
cLReapVlanIdNameMapEntry.setIndexNames(
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapGroupVlanTemplateName"),
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapVlanName"),
)
if mibBuilder.loadTexts:
    cLReapVlanIdNameMapEntry.setStatus("current")


class _CLReapVlanName_Type(SnmpAdminString):
    """Custom type cLReapVlanName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLReapVlanName_Type.__name__ = "SnmpAdminString"
_CLReapVlanName_Object = MibTableColumn
cLReapVlanName = _CLReapVlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 8, 1, 1, 1),
    _CLReapVlanName_Type()
)
cLReapVlanName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLReapVlanName.setStatus("current")


class _CLReapVlanMapId_Type(Unsigned32):
    """Custom type cLReapVlanMapId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_CLReapVlanMapId_Type.__name__ = "Unsigned32"
_CLReapVlanMapId_Object = MibTableColumn
cLReapVlanMapId = _CLReapVlanMapId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 8, 1, 1, 2),
    _CLReapVlanMapId_Type()
)
cLReapVlanMapId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapVlanMapId.setStatus("current")
_CLReapVlanIdNameMapRowStatus_Type = RowStatus
_CLReapVlanIdNameMapRowStatus_Object = MibTableColumn
cLReapVlanIdNameMapRowStatus = _CLReapVlanIdNameMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 8, 1, 1, 3),
    _CLReapVlanIdNameMapRowStatus_Type()
)
cLReapVlanIdNameMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapVlanIdNameMapRowStatus.setStatus("current")
_CLReapVlanTemplateTable_Object = MibTable
cLReapVlanTemplateTable = _CLReapVlanTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 8, 2)
)
if mibBuilder.loadTexts:
    cLReapVlanTemplateTable.setStatus("current")
_CLReapVlanTemplateEntry_Object = MibTableRow
cLReapVlanTemplateEntry = _CLReapVlanTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 8, 2, 1)
)
cLReapVlanTemplateEntry.setIndexNames(
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapGroupVlanTemplateName"),
)
if mibBuilder.loadTexts:
    cLReapVlanTemplateEntry.setStatus("current")


class _CLReapVlanTemplateDescription_Type(SnmpAdminString):
    """Custom type cLReapVlanTemplateDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLReapVlanTemplateDescription_Type.__name__ = "SnmpAdminString"
_CLReapVlanTemplateDescription_Object = MibTableColumn
cLReapVlanTemplateDescription = _CLReapVlanTemplateDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 8, 2, 1, 1),
    _CLReapVlanTemplateDescription_Type()
)
cLReapVlanTemplateDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapVlanTemplateDescription.setStatus("current")
_CLReapVlanTemplateRowStatus_Type = RowStatus
_CLReapVlanTemplateRowStatus_Object = MibTableColumn
cLReapVlanTemplateRowStatus = _CLReapVlanTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 8, 2, 1, 2),
    _CLReapVlanTemplateRowStatus_Type()
)
cLReapVlanTemplateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapVlanTemplateRowStatus.setStatus("current")
_CiscoLwappReapMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappReapMIBConform = _CiscoLwappReapMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2)
)
_CiscoLwappReapMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappReapMIBCompliances = _CiscoLwappReapMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 1)
)
_CiscoLwappReapMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappReapMIBGroups = _CiscoLwappReapMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 2)
)

# Managed Objects groups

ciscoLwappReapWlanConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 2, 1)
)
ciscoLwappReapWlanConfigGroup.setObjects(
      *(("CISCO-LWAPP-REAP-MIB", "cLReapWlanEnLocalSwitching"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapWlanVlanCentralSwitching"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapWlanDhcpCentral"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapWlanDhcpOverrideDNS"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapWlanNatPatEnabled"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapWlanAssocCentral"))
)
if mibBuilder.loadTexts:
    ciscoLwappReapWlanConfigGroup.setStatus("current")

ciscoLwappReapApConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 2, 2)
)
ciscoLwappReapApConfigGroup.setObjects(
      *(("CISCO-LWAPP-REAP-MIB", "cLReapApNativeVlanId"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapApVlanId"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapApVlanEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapInstallMappingRadioBackhaul"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapApResilientMode"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapApNativeVlanLevel"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapApVlanInheritance"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapApVlanRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapApVlanUsedBySecEthInterface"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapIngressAcl"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapEgressAcl"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapApVlanIdAclRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapVlanIdAclType"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapApWebAuthAcl"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapApWebAuthAclRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapWebPolicyAclRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapApLocalSplitAcl"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapApLocalSplitAclRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapApDhcpCentral"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapApDhcpOverrideDNS"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapApNatPatEnabled"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapApDhcpRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapApInheritance"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapApL2Acl"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapApL2AclRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapArpCaheEnabled"))
)
if mibBuilder.loadTexts:
    ciscoLwappReapApConfigGroup.setStatus("current")

ciscoLwappReapGroupConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 2, 3)
)
ciscoLwappReapGroupConfigGroup.setObjects(
      *(("CISCO-LWAPP-REAP-MIB", "cLReapGroupPrimaryRadiusIndex"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupSecondaryRadiusIndex"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupStorageType"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupApStorageType"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupApRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupApPnPConflict"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupEfficientApUpgradeEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupApUpgradeStart"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupSlaveMaxRetryCount"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupPrimaryRadiusServerType"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupPrimaryRadiusServerAddress"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupPrimaryRadiusServerPort"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupPrimaryServerSecret"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupSecRadiusServerType"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupSecRadiusServerAddress"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupSecRadiusServerPort"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupSecServerSecret"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusPeapEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusEapTlsEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupCertificateEapTlsEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupNativeVlanId"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupVlanEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupOverrideVlanEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupHttpProxyIpType"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupHttpProxyIp"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupHttpProxyPort"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupVlanTemplateName"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupApEntryType"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupIngressAcl"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupEgressAcl"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupVlanAclRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupVlanOrder"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupWebAuthAcl"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupAclRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupWebAuthIpv6Acl"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupWebPolicyAclRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupWebPolicyAclType"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupLocalSplitAcl"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupLocalSplitAclRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupDhcpCentral"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupDhcpOverrideDNS"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupNatPatEnabled"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupDhcpRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupWlanVlanId"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupVlanRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupAVCFlexProfileName"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupNbarStatsVisibilityEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupAVCFlexRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapMasterApModel"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapMasterApManual"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapMasterApRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapL2AclApplyMode"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapL2AclRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapL2AclRuleAction"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapL2AclRuleEthertype"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapL2AclRuleEthertypeMask"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapL2AclRuleDirection"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapL2AclNewRuleIndex"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapL2AclRuleRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupPrimaryRadiusIndex"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupSecondaryRadiusIndex"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupStorageType"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupEfficientApUpgradeEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupApUpgradeStart"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupEfficientApJoinEnable"))
)
if mibBuilder.loadTexts:
    ciscoLwappReapGroupConfigGroup.setStatus("deprecated")

ciscoLwappReapGroupConfigRadiusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 2, 4)
)
ciscoLwappReapGroupConfigRadiusGroup.setObjects(
      *(("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusPacTimeout"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusAuthorityId"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusAuthorityInfo"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusServerKey"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusIgnoreKey"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusLeapEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusEapFastEnable"))
)
if mibBuilder.loadTexts:
    ciscoLwappReapGroupConfigRadiusGroup.setStatus("deprecated")

ciscoLwappReapGroupConfigUserAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 2, 5)
)
ciscoLwappReapGroupConfigUserAuthGroup.setObjects(
      *(("CISCO-LWAPP-REAP-MIB", "cLReapGroupUserPassword"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupUserStorageType"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupUserRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappReapGroupConfigUserAuthGroup.setStatus("current")

ciscoLwappReapApConfigGroupHomeAp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 2, 6)
)
ciscoLwappReapApConfigGroupHomeAp.setObjects(
      *(("CISCO-LWAPP-REAP-MIB", "cLReapHomeApEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapApLeastLatencyJoinEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapWlanClientIpLearnEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapHomeApLocalSsidReset"))
)
if mibBuilder.loadTexts:
    ciscoLwappReapApConfigGroupHomeAp.setStatus("current")

ciscoLwappReapGroupConfigRadiusGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 2, 7)
)
ciscoLwappReapGroupConfigRadiusGroup1.setObjects(
      *(("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusAuthorityId"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusAuthorityInfo"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusServerKey"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusIgnoreKey"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusLeapEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusEapFastEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusPacTimeoutCtrl"))
)
if mibBuilder.loadTexts:
    ciscoLwappReapGroupConfigRadiusGroup1.setStatus("current")

ciscoLwappReapWlanConfigGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 2, 8)
)
ciscoLwappReapWlanConfigGroupSup1.setObjects(
    ("CISCO-LWAPP-REAP-MIB", "cLReapWlanApAuth")
)
if mibBuilder.loadTexts:
    ciscoLwappReapWlanConfigGroupSup1.setStatus("current")

ciscoLwappReapAclConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 2, 9)
)
ciscoLwappReapAclConfigGroup.setObjects(
      *(("CISCO-LWAPP-REAP-MIB", "cLReapAclName"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclApplyMode"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclRuleIndex"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclRuleAction"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclRuleSourceIpAddressType"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclRuleSourceIpAddress"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclRuleSourceIpNetmaskType"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclRuleSourceIpNetmask"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclRuleDestinationIpAddressType"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclRuleDestinationIpAddress"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclRuleDestinationIpNetmaskType"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclRuleDestinationIpNetmask"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclRuleProtocol"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclRuleStartSourcePort"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclRuleEndSourcePort"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclRuleStartDestinationPort"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclRuleEndDestinationPort"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclRuleDscp"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclNewRuleIndex"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclRuleRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappReapAclConfigGroup.setStatus("deprecated")

ciscoLwappReapAclConfigGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 2, 10)
)
ciscoLwappReapAclConfigGroupRev1.setObjects(
      *(("CISCO-LWAPP-REAP-MIB", "cLReapAclName"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclApplyMode"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclRuleIndex"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclRuleAction"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclRuleSourceIpAddressType"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclRuleSourceIpAddress"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclRuleSourceIpNetmaskType"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclRuleSourceIpNetmask"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclRuleDestinationIpAddressType"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclRuleDestinationIpAddress"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclRuleDestinationIpNetmaskType"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclRuleDestinationIpNetmask"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclRuleProtocol"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclRuleStartSourcePort"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclRuleEndSourcePort"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclRuleStartDestinationPort"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclRuleEndDestinationPort"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclRuleDscp"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclNewRuleIndex"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclRuleRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclUrlDomainRuleIndex"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclUrlDomainRuleUrl"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclUrlDomainRuleAction"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapAclUrlDomainRuleRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappReapAclConfigGroupRev1.setStatus("current")

ciscoLwappReapIpv6AclConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 2, 11)
)
ciscoLwappReapIpv6AclConfigGroup.setObjects(
      *(("CISCO-LWAPP-REAP-MIB", "cLReapIpv6AclName"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapIpv6AclApplyMode"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapIpv6AclRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapIpv6AclRuleIndex"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapIpv6AclRuleAction"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapIpv6AclRuleSourceAddressType"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapIpv6AclRuleSourceAddress"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapIpv6AclRuleSourcePrefixLength"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapIpv6AclRuleDestinationAddressType"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapIpv6AclRuleDestinationAddress"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapIpv6AclRuleDestinationPrefixLength"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapIpv6AclRuleProtocol"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapIpv6AclRuleStartSourcePort"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapIpv6AclRuleEndSourcePort"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapIpv6AclRuleStartDestinationPort"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapIpv6AclRuleEndDestinationPort"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapIpv6AclRuleDscp"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapIpv6AclNewRuleIndex"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapIpv6AclRuleRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapIpv6AclUrlDomainRuleIndex"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapIpv6AclUrlDomainRuleUrl"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapIpv6AclUrlDomainRuleAction"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapIpv6AclUrlDomainRuleRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappReapIpv6AclConfigGroup.setStatus("current")

ciscoLwappReapVlanConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 2, 12)
)
ciscoLwappReapVlanConfigGroup.setObjects(
      *(("CISCO-LWAPP-REAP-MIB", "cLReapGroupVlanIdentifier"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupAcl"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupVlanNameAclType"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupVlanNameAclRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapVlanMapId"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapVlanIdNameMapRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapVlanTemplateDescription"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapVlanTemplateRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupAclIn"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupAclOut"))
)
if mibBuilder.loadTexts:
    ciscoLwappReapVlanConfigGroup.setStatus("current")

ciscoLwappReapUrlDomainConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 2, 13)
)
ciscoLwappReapUrlDomainConfigGroup.setObjects(
      *(("CISCO-LWAPP-REAP-MIB", "cLReapUrlDomainRuleAction"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapUrlRedirectServerIpv4Type"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapUrlRedirectServerIpv4"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapUrlRedirectServerIpv6Type"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapUrlRedirectServerIpv6"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapUrlDomainRuleRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapUrlFilterID"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapUrlRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapEnhancedUrlDomainListRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapEnhancedUrlDomainRuleAction"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapEnhancedUrlDomainRulePreference"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapEnhancedUrlDomainRuleRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappReapUrlDomainConfigGroup.setStatus("current")

ciscoLwappReapCtsSxpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 2, 14)
)
ciscoLwappReapCtsSxpConfigGroup.setObjects(
      *(("CISCO-LWAPP-REAP-MIB", "cLReapCtsSxpDefaultPassword"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapCtsSxpState"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapCtsSxpListenerMinHoldTime"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapCtsSxpListenerMaxHoldTime"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapCtsSxpReconcilePeriod"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapCtsSxpRetryPeriod"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapCtsSxpSpeakerMinHoldTime"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapCtsSxpRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapCtsSxpMode"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapCtsSxpPeerPassword"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapCtsSxpPeerRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappReapCtsSxpConfigGroup.setStatus("current")

ciscoLwappReapGroupConfigGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 2, 15)
)
ciscoLwappReapGroupConfigGroupRev2.setObjects(
      *(("CISCO-LWAPP-REAP-MIB", "cLReapGroupPrimaryRadiusIndex"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupSecondaryRadiusIndex"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupStorageType"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupApStorageType"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupApRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupApPnPConflict"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupEfficientApUpgradeEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupApUpgradeStart"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupSlaveMaxRetryCount"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupPrimaryRadiusServerType"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupPrimaryRadiusServerAddress"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupPrimaryRadiusServerPort"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupPrimaryServerSecret"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupSecRadiusServerType"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupSecRadiusServerAddress"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupSecRadiusServerPort"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupSecServerSecret"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusPeapEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusEapTlsEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupCertificateEapTlsEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupNativeVlanId"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupVlanEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupOverrideVlanEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupHttpProxyIpType"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupHttpProxyIp"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupHttpProxyPort"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupVlanTemplateName"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupApEntryType"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupIngressAcl"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupEgressAcl"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupVlanAclRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupVlanOrder"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupWebAuthAcl"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupAclRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupWebAuthIpv6Acl"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupWebPolicyAclRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupWebPolicyAclType"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupWebPolicyAclCentWebAuth"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupLocalSplitAcl"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupLocalSplitAclRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupDhcpCentral"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupDhcpOverrideDNS"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupNatPatEnabled"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupDhcpRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupWlanVlanId"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupVlanRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupAVCFlexProfileName"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupNbarStatsVisibilityEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupAVCFlexRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapMasterApModel"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapMasterApManual"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapMasterApRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapL2AclApplyMode"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapL2AclRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapL2AclRuleAction"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapL2AclRuleEthertype"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapL2AclRuleEthertypeMask"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapL2AclRuleDirection"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapL2AclNewRuleIndex"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapL2AclRuleRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupPrimaryRadiusIndex"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupSecondaryRadiusIndex"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupStorageType"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupEfficientApUpgradeEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupApUpgradeStart"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupEfficientApJoinEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusServerGroupName"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupEapFastProfileName"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupArpCacheEnabled"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupHomeApEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupLeastLatencyJoinEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupHomeApLocalSsidReset"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupInstallMappingRadioBackhaul"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupResilientMode"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupDescription"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupFallbackRadioShutEnabled"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapIsHomeApEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupWebPolicyAclCentWebAuth"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupEfficientApJoinEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapCtsInlineTagging"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapCtsRolebasedEnforcement"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapCtsSxpAttachedProfileName"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupAccountingRadiusServerGroupName"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapLocalRoaming"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupMdnsFlexProfileName"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapIpOverlap"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupDhcpBroadcastEnable"))
)
if mibBuilder.loadTexts:
    ciscoLwappReapGroupConfigGroupRev2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoLwappReapMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 1, 1)
)
ciscoLwappReapMIBCompliance.setObjects(
      *(("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapWlanConfigGroup"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapApConfigGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappReapMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappReapMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 1, 2)
)
ciscoLwappReapMIBComplianceRev1.setObjects(
      *(("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapWlanConfigGroup"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapApConfigGroup"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapGroupConfigGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappReapMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoLwappReapMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 1, 3)
)
ciscoLwappReapMIBComplianceRev2.setObjects(
      *(("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapWlanConfigGroup"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapApConfigGroup"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapGroupConfigGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappReapMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoLwappReapMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 1, 4)
)
ciscoLwappReapMIBComplianceRev3.setObjects(
      *(("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapWlanConfigGroup"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapApConfigGroup"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapGroupConfigGroup"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapGroupConfigRadiusGroup"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapGroupConfigUserAuthGroup"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapApConfigGroupHomeAp"))
)
if mibBuilder.loadTexts:
    ciscoLwappReapMIBComplianceRev3.setStatus(
        "deprecated"
    )

ciscoLwappReapMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 1, 5)
)
ciscoLwappReapMIBComplianceRev4.setObjects(
      *(("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapWlanConfigGroup"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapApConfigGroup"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapGroupConfigGroup"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapGroupConfigUserAuthGroup"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapApConfigGroupHomeAp"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapGroupConfigRadiusGroup1"))
)
if mibBuilder.loadTexts:
    ciscoLwappReapMIBComplianceRev4.setStatus(
        "deprecated"
    )

ciscoLwappReapMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 1, 6)
)
ciscoLwappReapMIBComplianceRev5.setObjects(
      *(("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapWlanConfigGroup"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapApConfigGroup"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapGroupConfigGroup"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapGroupConfigUserAuthGroup"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapApConfigGroupHomeAp"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapGroupConfigRadiusGroup1"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapWlanConfigGroupSup1"))
)
if mibBuilder.loadTexts:
    ciscoLwappReapMIBComplianceRev5.setStatus(
        "deprecated"
    )

ciscoLwappReapMIBComplianceRev6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 1, 7)
)
ciscoLwappReapMIBComplianceRev6.setObjects(
      *(("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapWlanConfigGroup"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapApConfigGroup"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapGroupConfigGroup"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapGroupConfigUserAuthGroup"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapApConfigGroupHomeAp"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapGroupConfigRadiusGroup1"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapWlanConfigGroupSup1"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapAclConfigGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappReapMIBComplianceRev6.setStatus(
        "deprecated"
    )

ciscoLwappReapMIBComplianceRev7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 1, 8)
)
ciscoLwappReapMIBComplianceRev7.setObjects(
      *(("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapWlanConfigGroup"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapApConfigGroup"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapGroupConfigGroup"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapGroupConfigUserAuthGroup"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapApConfigGroupHomeAp"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapGroupConfigRadiusGroup1"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapWlanConfigGroupSup1"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapAclConfigGroupRev1"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapIpv6AclConfigGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappReapMIBComplianceRev7.setStatus(
        "deprecated"
    )

ciscoLwappReapMIBComplianceRev8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 1, 9)
)
ciscoLwappReapMIBComplianceRev8.setObjects(
      *(("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapWlanConfigGroup"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapApConfigGroup"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapGroupConfigGroupRev2"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapGroupConfigUserAuthGroup"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapApConfigGroupHomeAp"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapGroupConfigRadiusGroup1"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapWlanConfigGroupSup1"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapAclConfigGroupRev1"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapIpv6AclConfigGroup"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapVlanConfigGroup"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapUrlDomainConfigGroup"),
        ("CISCO-LWAPP-REAP-MIB", "ciscoLwappReapCtsSxpConfigGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappReapMIBComplianceRev8.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-REAP-MIB",
    **{"ciscoLwappReapMIB": ciscoLwappReapMIB,
       "ciscoLwappReapMIBNotifs": ciscoLwappReapMIBNotifs,
       "ciscoLwappReapMIBObjects": ciscoLwappReapMIBObjects,
       "ciscoLwappReapWlanConfig": ciscoLwappReapWlanConfig,
       "cLReapWlanConfigTable": cLReapWlanConfigTable,
       "cLReapWlanConfigEntry": cLReapWlanConfigEntry,
       "cLReapWlanEnLocalSwitching": cLReapWlanEnLocalSwitching,
       "cLReapWlanClientIpLearnEnable": cLReapWlanClientIpLearnEnable,
       "cLReapWlanApAuth": cLReapWlanApAuth,
       "cLReapWlanVlanCentralSwitching": cLReapWlanVlanCentralSwitching,
       "cLReapWlanDhcpCentral": cLReapWlanDhcpCentral,
       "cLReapWlanDhcpOverrideDNS": cLReapWlanDhcpOverrideDNS,
       "cLReapWlanNatPatEnabled": cLReapWlanNatPatEnabled,
       "cLReapWlanAssocCentral": cLReapWlanAssocCentral,
       "ciscoLwappReapApConfig": ciscoLwappReapApConfig,
       "cLReapApConfigTable": cLReapApConfigTable,
       "cLReapApConfigEntry": cLReapApConfigEntry,
       "cLReapApNativeVlanId": cLReapApNativeVlanId,
       "cLReapApVlanEnable": cLReapApVlanEnable,
       "cLReapHomeApEnable": cLReapHomeApEnable,
       "cLReapApLeastLatencyJoinEnable": cLReapApLeastLatencyJoinEnable,
       "cLReapHomeApLocalSsidReset": cLReapHomeApLocalSsidReset,
       "cLReapInstallMappingRadioBackhaul": cLReapInstallMappingRadioBackhaul,
       "cLReapApResilientMode": cLReapApResilientMode,
       "cLReapApNativeVlanLevel": cLReapApNativeVlanLevel,
       "cLReapApVlanIdTable": cLReapApVlanIdTable,
       "cLReapApVlanIdEntry": cLReapApVlanIdEntry,
       "cLReapApVlanId": cLReapApVlanId,
       "cLReapApVlanInheritance": cLReapApVlanInheritance,
       "cLReapApVlanRowStatus": cLReapApVlanRowStatus,
       "cLReapApVlanUsedBySecEthInterface": cLReapApVlanUsedBySecEthInterface,
       "cLReapApVlanIdAclTable": cLReapApVlanIdAclTable,
       "cLReapApVlanIdAclEntry": cLReapApVlanIdAclEntry,
       "cLReapVlanId": cLReapVlanId,
       "cLReapIngressAcl": cLReapIngressAcl,
       "cLReapEgressAcl": cLReapEgressAcl,
       "cLReapApVlanIdAclRowStatus": cLReapApVlanIdAclRowStatus,
       "cLReapVlanIdAclType": cLReapVlanIdAclType,
       "cLReapApWlanAclTable": cLReapApWlanAclTable,
       "cLReapApWlanAclEntry": cLReapApWlanAclEntry,
       "cLReapApWebAuthAcl": cLReapApWebAuthAcl,
       "cLReapApWebAuthAclRowStatus": cLReapApWebAuthAclRowStatus,
       "cLReapWebPolicyAclTable": cLReapWebPolicyAclTable,
       "cLReapWebPolicyAclEntry": cLReapWebPolicyAclEntry,
       "cLReapWebPolicyAcl": cLReapWebPolicyAcl,
       "cLReapWebPolicyAclRowStatus": cLReapWebPolicyAclRowStatus,
       "cLReapApLocalSplitACLTable": cLReapApLocalSplitACLTable,
       "cLReapApLocalSplitACLEntry": cLReapApLocalSplitACLEntry,
       "cLReapApLocalSplitAcl": cLReapApLocalSplitAcl,
       "cLReapApLocalSplitAclRowStatus": cLReapApLocalSplitAclRowStatus,
       "cLReapApCentralDhcpTable": cLReapApCentralDhcpTable,
       "cLReapApCentralDhcpEntry": cLReapApCentralDhcpEntry,
       "cLReapApDhcpCentral": cLReapApDhcpCentral,
       "cLReapApDhcpOverrideDNS": cLReapApDhcpOverrideDNS,
       "cLReapApNatPatEnabled": cLReapApNatPatEnabled,
       "cLReapApDhcpRowStatus": cLReapApDhcpRowStatus,
       "cLReapApInheritance": cLReapApInheritance,
       "cLReapApL2AclTable": cLReapApL2AclTable,
       "cLReapApL2AclEntry": cLReapApL2AclEntry,
       "cLReapApL2Acl": cLReapApL2Acl,
       "cLReapApL2AclRowStatus": cLReapApL2AclRowStatus,
       "ciscoLwappReapGroupConfig": ciscoLwappReapGroupConfig,
       "cLReapGroupConfigTable": cLReapGroupConfigTable,
       "cLReapGroupConfigEntry": cLReapGroupConfigEntry,
       "cLReapGroupName": cLReapGroupName,
       "cLReapGroupPrimaryRadiusIndex": cLReapGroupPrimaryRadiusIndex,
       "cLReapGroupSecondaryRadiusIndex": cLReapGroupSecondaryRadiusIndex,
       "cLReapGroupStorageType": cLReapGroupStorageType,
       "cLReapGroupRowStatus": cLReapGroupRowStatus,
       "cLReapGroupRadiusPacTimeout": cLReapGroupRadiusPacTimeout,
       "cLReapGroupRadiusAuthorityId": cLReapGroupRadiusAuthorityId,
       "cLReapGroupRadiusAuthorityInfo": cLReapGroupRadiusAuthorityInfo,
       "cLReapGroupRadiusServerKey": cLReapGroupRadiusServerKey,
       "cLReapGroupRadiusIgnoreKey": cLReapGroupRadiusIgnoreKey,
       "cLReapGroupRadiusEnable": cLReapGroupRadiusEnable,
       "cLReapGroupRadiusLeapEnable": cLReapGroupRadiusLeapEnable,
       "cLReapGroupRadiusEapFastEnable": cLReapGroupRadiusEapFastEnable,
       "cLReapGroupRadiusPacTimeoutCtrl": cLReapGroupRadiusPacTimeoutCtrl,
       "cLReapGroupEfficientApUpgradeEnable": cLReapGroupEfficientApUpgradeEnable,
       "cLReapGroupApUpgradeStart": cLReapGroupApUpgradeStart,
       "cLReapGroupSlaveMaxRetryCount": cLReapGroupSlaveMaxRetryCount,
       "cLReapGroupPrimaryRadiusServerType": cLReapGroupPrimaryRadiusServerType,
       "cLReapGroupPrimaryRadiusServerAddress": cLReapGroupPrimaryRadiusServerAddress,
       "cLReapGroupPrimaryRadiusServerPort": cLReapGroupPrimaryRadiusServerPort,
       "cLReapGroupPrimaryServerSecret": cLReapGroupPrimaryServerSecret,
       "cLReapGroupSecRadiusServerType": cLReapGroupSecRadiusServerType,
       "cLReapGroupSecRadiusServerAddress": cLReapGroupSecRadiusServerAddress,
       "cLReapGroupSecRadiusServerPort": cLReapGroupSecRadiusServerPort,
       "cLReapGroupSecServerSecret": cLReapGroupSecServerSecret,
       "cLReapGroupRadiusPeapEnable": cLReapGroupRadiusPeapEnable,
       "cLReapGroupRadiusEapTlsEnable": cLReapGroupRadiusEapTlsEnable,
       "cLReapGroupCertificateEapTlsEnable": cLReapGroupCertificateEapTlsEnable,
       "cLReapGroupNativeVlanId": cLReapGroupNativeVlanId,
       "cLReapGroupVlanEnable": cLReapGroupVlanEnable,
       "cLReapGroupOverrideVlanEnable": cLReapGroupOverrideVlanEnable,
       "cLReapGroupHttpProxyIpType": cLReapGroupHttpProxyIpType,
       "cLReapGroupHttpProxyIp": cLReapGroupHttpProxyIp,
       "cLReapGroupHttpProxyPort": cLReapGroupHttpProxyPort,
       "cLReapGroupVlanTemplateName": cLReapGroupVlanTemplateName,
       "cLReapGroupEfficientApJoinEnable": cLReapGroupEfficientApJoinEnable,
       "cLReapGroupRadiusServerGroupName": cLReapGroupRadiusServerGroupName,
       "cLReapGroupEapFastProfileName": cLReapGroupEapFastProfileName,
       "cLReapGroupArpCacheEnabled": cLReapGroupArpCacheEnabled,
       "cLReapGroupHomeApEnable": cLReapGroupHomeApEnable,
       "cLReapGroupLeastLatencyJoinEnable": cLReapGroupLeastLatencyJoinEnable,
       "cLReapGroupHomeApLocalSsidReset": cLReapGroupHomeApLocalSsidReset,
       "cLReapGroupInstallMappingRadioBackhaul": cLReapGroupInstallMappingRadioBackhaul,
       "cLReapGroupResilientMode": cLReapGroupResilientMode,
       "cLReapGroupDescription": cLReapGroupDescription,
       "cLReapGroupFallbackRadioShutEnabled": cLReapGroupFallbackRadioShutEnabled,
       "cLReapCtsInlineTagging": cLReapCtsInlineTagging,
       "cLReapIsHomeApEnable": cLReapIsHomeApEnable,
       "cLReapCtsRolebasedEnforcement": cLReapCtsRolebasedEnforcement,
       "cLReapCtsSxpAttachedProfileName": cLReapCtsSxpAttachedProfileName,
       "cLReapGroupAccountingRadiusServerGroupName": cLReapGroupAccountingRadiusServerGroupName,
       "cLReapLocalRoaming": cLReapLocalRoaming,
       "cLReapGroupMdnsFlexProfileName": cLReapGroupMdnsFlexProfileName,
       "cLReapIpOverlap": cLReapIpOverlap,
       "cLReapGroupDhcpBroadcastEnable": cLReapGroupDhcpBroadcastEnable,
       "cLReapGroupApConfigTable": cLReapGroupApConfigTable,
       "cLReapGroupApConfigEntry": cLReapGroupApConfigEntry,
       "cLReapGroupApStorageType": cLReapGroupApStorageType,
       "cLReapGroupApRowStatus": cLReapGroupApRowStatus,
       "cLReapGroupApEntryType": cLReapGroupApEntryType,
       "cLReapGroupApPnPConflict": cLReapGroupApPnPConflict,
       "cLReapGroupUserConfigTable": cLReapGroupUserConfigTable,
       "cLReapGroupUserConfigEntry": cLReapGroupUserConfigEntry,
       "cLReapGroupUserName": cLReapGroupUserName,
       "cLReapGroupUserPassword": cLReapGroupUserPassword,
       "cLReapGroupUserStorageType": cLReapGroupUserStorageType,
       "cLReapGroupUserRowStatus": cLReapGroupUserRowStatus,
       "cLReapGroupVlanAclTable": cLReapGroupVlanAclTable,
       "cLReapGroupVlanAclEntry": cLReapGroupVlanAclEntry,
       "cLReapGroupVlanId": cLReapGroupVlanId,
       "cLReapGroupIngressAcl": cLReapGroupIngressAcl,
       "cLReapGroupEgressAcl": cLReapGroupEgressAcl,
       "cLReapGroupVlanAclRowStatus": cLReapGroupVlanAclRowStatus,
       "cLReapGroupVlanOrder": cLReapGroupVlanOrder,
       "cLReapGroupAclTable": cLReapGroupAclTable,
       "cLReapGroupAclEntry": cLReapGroupAclEntry,
       "cLReapGroupWebAuthAcl": cLReapGroupWebAuthAcl,
       "cLReapGroupAclRowStatus": cLReapGroupAclRowStatus,
       "cLReapGroupWebAuthIpv6Acl": cLReapGroupWebAuthIpv6Acl,
       "cLReapGroupWebPolicyAclTable": cLReapGroupWebPolicyAclTable,
       "cLReapGroupWebPolicyAclEntry": cLReapGroupWebPolicyAclEntry,
       "cLReapGroupWebPolicyAcl": cLReapGroupWebPolicyAcl,
       "cLReapGroupWebPolicyAclRowStatus": cLReapGroupWebPolicyAclRowStatus,
       "cLReapGroupWebPolicyAclType": cLReapGroupWebPolicyAclType,
       "cLReapGroupWebPolicyAclCentWebAuth": cLReapGroupWebPolicyAclCentWebAuth,
       "cLReapGroupLocalSplitAclTable": cLReapGroupLocalSplitAclTable,
       "cLReapGroupLocalSplitAclEntry": cLReapGroupLocalSplitAclEntry,
       "cLReapGroupLocalSplitAcl": cLReapGroupLocalSplitAcl,
       "cLReapGroupLocalSplitAclRowStatus": cLReapGroupLocalSplitAclRowStatus,
       "cLReapGroupCentralDhcpTable": cLReapGroupCentralDhcpTable,
       "cLReapGroupCentralDhcpEntry": cLReapGroupCentralDhcpEntry,
       "cLReapGroupDhcpCentral": cLReapGroupDhcpCentral,
       "cLReapGroupDhcpOverrideDNS": cLReapGroupDhcpOverrideDNS,
       "cLReapGroupNatPatEnabled": cLReapGroupNatPatEnabled,
       "cLReapGroupDhcpRowStatus": cLReapGroupDhcpRowStatus,
       "cLReapGroupVlanIdTable": cLReapGroupVlanIdTable,
       "cLReapGroupVlanIdEntry": cLReapGroupVlanIdEntry,
       "cLReapGroupWlanVlanId": cLReapGroupWlanVlanId,
       "cLReapGroupVlanRowStatus": cLReapGroupVlanRowStatus,
       "cLReapGroupAVCFlexTable": cLReapGroupAVCFlexTable,
       "cLReapGroupAVCFlexEntry": cLReapGroupAVCFlexEntry,
       "cLReapGroupAVCFlexProfileName": cLReapGroupAVCFlexProfileName,
       "cLReapGroupNbarStatsVisibilityEnable": cLReapGroupNbarStatsVisibilityEnable,
       "cLReapGroupAVCFlexRowStatus": cLReapGroupAVCFlexRowStatus,
       "cLReapGroupVlanNameAclTable": cLReapGroupVlanNameAclTable,
       "cLReapGroupVlanNameAclEntry": cLReapGroupVlanNameAclEntry,
       "cLReapGroupVlanName": cLReapGroupVlanName,
       "cLReapGroupVlanIdentifier": cLReapGroupVlanIdentifier,
       "cLReapGroupAcl": cLReapGroupAcl,
       "cLReapGroupVlanNameAclType": cLReapGroupVlanNameAclType,
       "cLReapGroupVlanNameAclRowStatus": cLReapGroupVlanNameAclRowStatus,
       "cLReapGroupAclIn": cLReapGroupAclIn,
       "cLReapGroupAclOut": cLReapGroupAclOut,
       "cLReapGroupCtsSxpTable": cLReapGroupCtsSxpTable,
       "cLReapGroupCtsSxpEntry": cLReapGroupCtsSxpEntry,
       "cLReapCtsSxpConfigProfileName": cLReapCtsSxpConfigProfileName,
       "cLReapCtsSxpDefaultPassword": cLReapCtsSxpDefaultPassword,
       "cLReapCtsSxpState": cLReapCtsSxpState,
       "cLReapCtsSxpListenerMinHoldTime": cLReapCtsSxpListenerMinHoldTime,
       "cLReapCtsSxpListenerMaxHoldTime": cLReapCtsSxpListenerMaxHoldTime,
       "cLReapCtsSxpReconcilePeriod": cLReapCtsSxpReconcilePeriod,
       "cLReapCtsSxpRetryPeriod": cLReapCtsSxpRetryPeriod,
       "cLReapCtsSxpSpeakerMinHoldTime": cLReapCtsSxpSpeakerMinHoldTime,
       "cLReapCtsSxpRowStatus": cLReapCtsSxpRowStatus,
       "cLReapCtsSxpPeerTable": cLReapCtsSxpPeerTable,
       "cLReapCtsSxpPeerEntry": cLReapCtsSxpPeerEntry,
       "cLReapCtsSxpPeerIpType": cLReapCtsSxpPeerIpType,
       "cLReapCtsSxpPeerIp": cLReapCtsSxpPeerIp,
       "cLReapCtsSxpMode": cLReapCtsSxpMode,
       "cLReapCtsSxpPeerPassword": cLReapCtsSxpPeerPassword,
       "cLReapCtsSxpPeerRowStatus": cLReapCtsSxpPeerRowStatus,
       "ciscoLwappReapAclConfig": ciscoLwappReapAclConfig,
       "cLReapAclTable": cLReapAclTable,
       "cLReapAclEntry": cLReapAclEntry,
       "cLReapAclName": cLReapAclName,
       "cLReapAclApplyMode": cLReapAclApplyMode,
       "cLReapAclRowStatus": cLReapAclRowStatus,
       "cLReapAclUrlDomainListType": cLReapAclUrlDomainListType,
       "cLReapAclRuleTable": cLReapAclRuleTable,
       "cLReapAclRuleEntry": cLReapAclRuleEntry,
       "cLReapAclRuleIndex": cLReapAclRuleIndex,
       "cLReapAclRuleAction": cLReapAclRuleAction,
       "cLReapAclRuleSourceIpAddressType": cLReapAclRuleSourceIpAddressType,
       "cLReapAclRuleSourceIpAddress": cLReapAclRuleSourceIpAddress,
       "cLReapAclRuleSourceIpNetmaskType": cLReapAclRuleSourceIpNetmaskType,
       "cLReapAclRuleSourceIpNetmask": cLReapAclRuleSourceIpNetmask,
       "cLReapAclRuleDestinationIpAddressType": cLReapAclRuleDestinationIpAddressType,
       "cLReapAclRuleDestinationIpAddress": cLReapAclRuleDestinationIpAddress,
       "cLReapAclRuleDestinationIpNetmaskType": cLReapAclRuleDestinationIpNetmaskType,
       "cLReapAclRuleDestinationIpNetmask": cLReapAclRuleDestinationIpNetmask,
       "cLReapAclRuleProtocol": cLReapAclRuleProtocol,
       "cLReapAclRuleStartSourcePort": cLReapAclRuleStartSourcePort,
       "cLReapAclRuleEndSourcePort": cLReapAclRuleEndSourcePort,
       "cLReapAclRuleStartDestinationPort": cLReapAclRuleStartDestinationPort,
       "cLReapAclRuleEndDestinationPort": cLReapAclRuleEndDestinationPort,
       "cLReapAclRuleDscp": cLReapAclRuleDscp,
       "cLReapAclNewRuleIndex": cLReapAclNewRuleIndex,
       "cLReapAclRuleRowStatus": cLReapAclRuleRowStatus,
       "cLReapL2AclTable": cLReapL2AclTable,
       "cLReapL2AclEntry": cLReapL2AclEntry,
       "cLReapL2AclName": cLReapL2AclName,
       "cLReapL2AclApplyMode": cLReapL2AclApplyMode,
       "cLReapL2AclRowStatus": cLReapL2AclRowStatus,
       "cLReapL2AclRuleTable": cLReapL2AclRuleTable,
       "cLReapL2AclRuleEntry": cLReapL2AclRuleEntry,
       "cLReapL2AclRuleIndex": cLReapL2AclRuleIndex,
       "cLReapL2AclRuleAction": cLReapL2AclRuleAction,
       "cLReapL2AclRuleEthertype": cLReapL2AclRuleEthertype,
       "cLReapL2AclRuleEthertypeMask": cLReapL2AclRuleEthertypeMask,
       "cLReapL2AclRuleDirection": cLReapL2AclRuleDirection,
       "cLReapL2AclNewRuleIndex": cLReapL2AclNewRuleIndex,
       "cLReapL2AclRuleRowStatus": cLReapL2AclRuleRowStatus,
       "cLReapAclUrlDomainRuleTable": cLReapAclUrlDomainRuleTable,
       "cLReapAclUrlDomainRuleEntry": cLReapAclUrlDomainRuleEntry,
       "cLReapAclUrlDomainRuleIndex": cLReapAclUrlDomainRuleIndex,
       "cLReapAclUrlDomainRuleUrl": cLReapAclUrlDomainRuleUrl,
       "cLReapAclUrlDomainRuleAction": cLReapAclUrlDomainRuleAction,
       "cLReapAclUrlDomainRuleRowStatus": cLReapAclUrlDomainRuleRowStatus,
       "cLReapUrlDomainListTable": cLReapUrlDomainListTable,
       "cLReapUrlDomainListEntry": cLReapUrlDomainListEntry,
       "cLReapUrlListName": cLReapUrlListName,
       "cLReapUrlDomainRuleAction": cLReapUrlDomainRuleAction,
       "cLReapUrlRedirectServerIpv4Type": cLReapUrlRedirectServerIpv4Type,
       "cLReapUrlRedirectServerIpv4": cLReapUrlRedirectServerIpv4,
       "cLReapUrlRedirectServerIpv6Type": cLReapUrlRedirectServerIpv6Type,
       "cLReapUrlRedirectServerIpv6": cLReapUrlRedirectServerIpv6,
       "cLReapUrlDomainRuleRowStatus": cLReapUrlDomainRuleRowStatus,
       "cLReapUrlFilterID": cLReapUrlFilterID,
       "cLReapUrlDomainRulesTable": cLReapUrlDomainRulesTable,
       "cLReapUrlDomainRulesEntry": cLReapUrlDomainRulesEntry,
       "cLReapUrlDomainRuleUrl": cLReapUrlDomainRuleUrl,
       "cLReapUrlRowStatus": cLReapUrlRowStatus,
       "cLReapEnhancedUrlDomainListTable": cLReapEnhancedUrlDomainListTable,
       "cLReapEnhancedUrlDomainListEntry": cLReapEnhancedUrlDomainListEntry,
       "cLReapEnhancedUrlDomainListName": cLReapEnhancedUrlDomainListName,
       "cLReapEnhancedUrlDomainListRowStatus": cLReapEnhancedUrlDomainListRowStatus,
       "cLReapEnhancedUrlDomainRulesTable": cLReapEnhancedUrlDomainRulesTable,
       "cLReapEnhancedUrlDomainRulesEntry": cLReapEnhancedUrlDomainRulesEntry,
       "cLReapEnhancedUrlDomainRuleUrl": cLReapEnhancedUrlDomainRuleUrl,
       "cLReapEnhancedUrlDomainRuleAction": cLReapEnhancedUrlDomainRuleAction,
       "cLReapEnhancedUrlDomainRulePreference": cLReapEnhancedUrlDomainRulePreference,
       "cLReapEnhancedUrlDomainRuleRowStatus": cLReapEnhancedUrlDomainRuleRowStatus,
       "ciscoLwappReapMasterApConfig": ciscoLwappReapMasterApConfig,
       "cLReapMasterApConfigTable": cLReapMasterApConfigTable,
       "cLReapMasterApConfigEntry": cLReapMasterApConfigEntry,
       "cLReapMasterApModel": cLReapMasterApModel,
       "cLReapMasterApManual": cLReapMasterApManual,
       "cLReapMasterApRowStatus": cLReapMasterApRowStatus,
       "ciscoLwappReapGlobalConfig": ciscoLwappReapGlobalConfig,
       "cLReapArpCaheEnabled": cLReapArpCaheEnabled,
       "ciscoLwappReapIpv6AclConfig": ciscoLwappReapIpv6AclConfig,
       "cLReapIpv6AclTable": cLReapIpv6AclTable,
       "cLReapIpv6AclEntry": cLReapIpv6AclEntry,
       "cLReapIpv6AclName": cLReapIpv6AclName,
       "cLReapIpv6AclApplyMode": cLReapIpv6AclApplyMode,
       "cLReapIpv6AclRowStatus": cLReapIpv6AclRowStatus,
       "cLReapIpv6AclRuleTable": cLReapIpv6AclRuleTable,
       "cLReapIpv6AclRuleEntry": cLReapIpv6AclRuleEntry,
       "cLReapIpv6AclRuleIndex": cLReapIpv6AclRuleIndex,
       "cLReapIpv6AclRuleAction": cLReapIpv6AclRuleAction,
       "cLReapIpv6AclRuleSourceAddressType": cLReapIpv6AclRuleSourceAddressType,
       "cLReapIpv6AclRuleSourceAddress": cLReapIpv6AclRuleSourceAddress,
       "cLReapIpv6AclRuleSourcePrefixLength": cLReapIpv6AclRuleSourcePrefixLength,
       "cLReapIpv6AclRuleDestinationAddressType": cLReapIpv6AclRuleDestinationAddressType,
       "cLReapIpv6AclRuleDestinationAddress": cLReapIpv6AclRuleDestinationAddress,
       "cLReapIpv6AclRuleDestinationPrefixLength": cLReapIpv6AclRuleDestinationPrefixLength,
       "cLReapIpv6AclRuleProtocol": cLReapIpv6AclRuleProtocol,
       "cLReapIpv6AclRuleStartSourcePort": cLReapIpv6AclRuleStartSourcePort,
       "cLReapIpv6AclRuleEndSourcePort": cLReapIpv6AclRuleEndSourcePort,
       "cLReapIpv6AclRuleStartDestinationPort": cLReapIpv6AclRuleStartDestinationPort,
       "cLReapIpv6AclRuleEndDestinationPort": cLReapIpv6AclRuleEndDestinationPort,
       "cLReapIpv6AclRuleDscp": cLReapIpv6AclRuleDscp,
       "cLReapIpv6AclNewRuleIndex": cLReapIpv6AclNewRuleIndex,
       "cLReapIpv6AclRuleRowStatus": cLReapIpv6AclRuleRowStatus,
       "cLReapIpv6AclUrlDomainRuleTable": cLReapIpv6AclUrlDomainRuleTable,
       "cLReapIpv6AclUrlDomainRuleEntry": cLReapIpv6AclUrlDomainRuleEntry,
       "cLReapIpv6AclUrlDomainRuleIndex": cLReapIpv6AclUrlDomainRuleIndex,
       "cLReapIpv6AclUrlDomainRuleUrl": cLReapIpv6AclUrlDomainRuleUrl,
       "cLReapIpv6AclUrlDomainRuleAction": cLReapIpv6AclUrlDomainRuleAction,
       "cLReapIpv6AclUrlDomainRuleRowStatus": cLReapIpv6AclUrlDomainRuleRowStatus,
       "ciscoLwappReapVlanConfig": ciscoLwappReapVlanConfig,
       "cLReapVlanIdNameMapTable": cLReapVlanIdNameMapTable,
       "cLReapVlanIdNameMapEntry": cLReapVlanIdNameMapEntry,
       "cLReapVlanName": cLReapVlanName,
       "cLReapVlanMapId": cLReapVlanMapId,
       "cLReapVlanIdNameMapRowStatus": cLReapVlanIdNameMapRowStatus,
       "cLReapVlanTemplateTable": cLReapVlanTemplateTable,
       "cLReapVlanTemplateEntry": cLReapVlanTemplateEntry,
       "cLReapVlanTemplateDescription": cLReapVlanTemplateDescription,
       "cLReapVlanTemplateRowStatus": cLReapVlanTemplateRowStatus,
       "ciscoLwappReapMIBConform": ciscoLwappReapMIBConform,
       "ciscoLwappReapMIBCompliances": ciscoLwappReapMIBCompliances,
       "ciscoLwappReapMIBCompliance": ciscoLwappReapMIBCompliance,
       "ciscoLwappReapMIBComplianceRev1": ciscoLwappReapMIBComplianceRev1,
       "ciscoLwappReapMIBComplianceRev2": ciscoLwappReapMIBComplianceRev2,
       "ciscoLwappReapMIBComplianceRev3": ciscoLwappReapMIBComplianceRev3,
       "ciscoLwappReapMIBComplianceRev4": ciscoLwappReapMIBComplianceRev4,
       "ciscoLwappReapMIBComplianceRev5": ciscoLwappReapMIBComplianceRev5,
       "ciscoLwappReapMIBComplianceRev6": ciscoLwappReapMIBComplianceRev6,
       "ciscoLwappReapMIBComplianceRev7": ciscoLwappReapMIBComplianceRev7,
       "ciscoLwappReapMIBComplianceRev8": ciscoLwappReapMIBComplianceRev8,
       "ciscoLwappReapMIBGroups": ciscoLwappReapMIBGroups,
       "ciscoLwappReapWlanConfigGroup": ciscoLwappReapWlanConfigGroup,
       "ciscoLwappReapApConfigGroup": ciscoLwappReapApConfigGroup,
       "ciscoLwappReapGroupConfigGroup": ciscoLwappReapGroupConfigGroup,
       "ciscoLwappReapGroupConfigRadiusGroup": ciscoLwappReapGroupConfigRadiusGroup,
       "ciscoLwappReapGroupConfigUserAuthGroup": ciscoLwappReapGroupConfigUserAuthGroup,
       "ciscoLwappReapApConfigGroupHomeAp": ciscoLwappReapApConfigGroupHomeAp,
       "ciscoLwappReapGroupConfigRadiusGroup1": ciscoLwappReapGroupConfigRadiusGroup1,
       "ciscoLwappReapWlanConfigGroupSup1": ciscoLwappReapWlanConfigGroupSup1,
       "ciscoLwappReapAclConfigGroup": ciscoLwappReapAclConfigGroup,
       "ciscoLwappReapAclConfigGroupRev1": ciscoLwappReapAclConfigGroupRev1,
       "ciscoLwappReapIpv6AclConfigGroup": ciscoLwappReapIpv6AclConfigGroup,
       "ciscoLwappReapVlanConfigGroup": ciscoLwappReapVlanConfigGroup,
       "ciscoLwappReapUrlDomainConfigGroup": ciscoLwappReapUrlDomainConfigGroup,
       "ciscoLwappReapCtsSxpConfigGroup": ciscoLwappReapCtsSxpConfigGroup,
       "ciscoLwappReapGroupConfigGroupRev2": ciscoLwappReapGroupConfigGroupRev2}
)
