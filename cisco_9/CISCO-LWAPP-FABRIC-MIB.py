# SNMP MIB module (CISCO-LWAPP-FABRIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-LWAPP-FABRIC-MIB.mib
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

(cLApIfMacAddress,
 cLApInetAddress,
 cLApSysMacAddress) = mibBuilder.importSymbols(
    "CISCO-LWAPP-AP-MIB",
    "cLApIfMacAddress",
    "cLApInetAddress",
    "cLApSysMacAddress")

(cldcClientMacAddress,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-DOT11-CLIENT-MIB",
    "cldcClientMacAddress")

(cLWlanIndex,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-WLAN-MIB",
    "cLWlanIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(Unsigned64,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "Unsigned64")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappFabricMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991)
)
if mibBuilder.loadTexts:
    ciscoLwappFabricMIB.setRevisions(
        ("2012-06-12 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappFabricMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappFabricMIBNotifs = _CiscoLwappFabricMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 0)
)
_CiscoLwappFabricNotifObjects_ObjectIdentity = ObjectIdentity
ciscoLwappFabricNotifObjects = _CiscoLwappFabricNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 0, 1)
)
_CLFabricCPPrimaryMapServerIPType_Type = InetAddressType
_CLFabricCPPrimaryMapServerIPType_Object = MibScalar
cLFabricCPPrimaryMapServerIPType = _CLFabricCPPrimaryMapServerIPType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 0, 1, 1),
    _CLFabricCPPrimaryMapServerIPType_Type()
)
cLFabricCPPrimaryMapServerIPType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLFabricCPPrimaryMapServerIPType.setStatus("current")
_CLFabricCPPrimaryMapServerIP_Type = InetAddress
_CLFabricCPPrimaryMapServerIP_Object = MibScalar
cLFabricCPPrimaryMapServerIP = _CLFabricCPPrimaryMapServerIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 0, 1, 2),
    _CLFabricCPPrimaryMapServerIP_Type()
)
cLFabricCPPrimaryMapServerIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLFabricCPPrimaryMapServerIP.setStatus("current")
_CLFabricCPSecondaryMapServerIPType_Type = InetAddressType
_CLFabricCPSecondaryMapServerIPType_Object = MibScalar
cLFabricCPSecondaryMapServerIPType = _CLFabricCPSecondaryMapServerIPType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 0, 1, 3),
    _CLFabricCPSecondaryMapServerIPType_Type()
)
cLFabricCPSecondaryMapServerIPType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLFabricCPSecondaryMapServerIPType.setStatus("current")
_CLFabricCPSecondaryMapServerIP_Type = InetAddress
_CLFabricCPSecondaryMapServerIP_Object = MibScalar
cLFabricCPSecondaryMapServerIP = _CLFabricCPSecondaryMapServerIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 0, 1, 4),
    _CLFabricCPSecondaryMapServerIP_Type()
)
cLFabricCPSecondaryMapServerIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLFabricCPSecondaryMapServerIP.setStatus("current")
_CiscoLwappFabricMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappFabricMIBObjects = _CiscoLwappFabricMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1)
)
_CiscoLwappFabricMIBTableObjects_ObjectIdentity = ObjectIdentity
ciscoLwappFabricMIBTableObjects = _CiscoLwappFabricMIBTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1)
)
_CLFabricControlplanePSKTable_Object = MibTable
cLFabricControlplanePSKTable = _CLFabricControlplanePSKTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cLFabricControlplanePSKTable.setStatus("current")
_CLFabricControlplanePSKEntry_Object = MibTableRow
cLFabricControlplanePSKEntry = _CLFabricControlplanePSKEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 1, 1)
)
cLFabricControlplanePSKEntry.setIndexNames(
    (0, "CISCO-LWAPP-FABRIC-MIB", "cLFabricControlplaneDomainType"),
    (0, "CISCO-LWAPP-FABRIC-MIB", "cLFabricControlplaneUnitType"),
    (0, "CISCO-LWAPP-FABRIC-MIB", "cLFabricControlplaneIPType"),
    (0, "CISCO-LWAPP-FABRIC-MIB", "cLFabricControlplaneIP"),
)
if mibBuilder.loadTexts:
    cLFabricControlplanePSKEntry.setStatus("current")


class _CLFabricControlplaneDomainType_Type(Integer32):
    """Custom type cLFabricControlplaneDomainType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enterpriseFabric", 1),
          ("guestFabric", 2))
    )


_CLFabricControlplaneDomainType_Type.__name__ = "Integer32"
_CLFabricControlplaneDomainType_Object = MibTableColumn
cLFabricControlplaneDomainType = _CLFabricControlplaneDomainType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 1, 1, 1),
    _CLFabricControlplaneDomainType_Type()
)
cLFabricControlplaneDomainType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLFabricControlplaneDomainType.setStatus("current")


class _CLFabricControlplaneUnitType_Type(Integer32):
    """Custom type cLFabricControlplaneUnitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_CLFabricControlplaneUnitType_Type.__name__ = "Integer32"
_CLFabricControlplaneUnitType_Object = MibTableColumn
cLFabricControlplaneUnitType = _CLFabricControlplaneUnitType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 1, 1, 2),
    _CLFabricControlplaneUnitType_Type()
)
cLFabricControlplaneUnitType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLFabricControlplaneUnitType.setStatus("current")
_CLFabricControlplaneIPType_Type = InetAddressType
_CLFabricControlplaneIPType_Object = MibTableColumn
cLFabricControlplaneIPType = _CLFabricControlplaneIPType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 1, 1, 3),
    _CLFabricControlplaneIPType_Type()
)
cLFabricControlplaneIPType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLFabricControlplaneIPType.setStatus("current")
_CLFabricControlplaneIP_Type = InetAddress
_CLFabricControlplaneIP_Object = MibTableColumn
cLFabricControlplaneIP = _CLFabricControlplaneIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 1, 1, 4),
    _CLFabricControlplaneIP_Type()
)
cLFabricControlplaneIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLFabricControlplaneIP.setStatus("current")


class _CLFabricControlplanePSKKey_Type(OctetString):
    """Custom type cLFabricControlplanePSKKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CLFabricControlplanePSKKey_Type.__name__ = "OctetString"
_CLFabricControlplanePSKKey_Object = MibTableColumn
cLFabricControlplanePSKKey = _CLFabricControlplanePSKKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 1, 1, 5),
    _CLFabricControlplanePSKKey_Type()
)
cLFabricControlplanePSKKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLFabricControlplanePSKKey.setStatus("current")
_CLFabricControlplaneRowStatus_Type = RowStatus
_CLFabricControlplaneRowStatus_Object = MibTableColumn
cLFabricControlplaneRowStatus = _CLFabricControlplaneRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 1, 1, 6),
    _CLFabricControlplaneRowStatus_Type()
)
cLFabricControlplaneRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLFabricControlplaneRowStatus.setStatus("current")
_CLFabricVnidTable_Object = MibTable
cLFabricVnidTable = _CLFabricVnidTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cLFabricVnidTable.setStatus("current")
_CLFabricVnidEntry_Object = MibTableRow
cLFabricVnidEntry = _CLFabricVnidEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 2, 1)
)
cLFabricVnidEntry.setIndexNames(
    (0, "CISCO-LWAPP-FABRIC-MIB", "cLFabricVnidName"),
)
if mibBuilder.loadTexts:
    cLFabricVnidEntry.setStatus("current")


class _CLFabricVnidName_Type(OctetString):
    """Custom type cLFabricVnidName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLFabricVnidName_Type.__name__ = "OctetString"
_CLFabricVnidName_Object = MibTableColumn
cLFabricVnidName = _CLFabricVnidName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 2, 1, 1),
    _CLFabricVnidName_Type()
)
cLFabricVnidName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLFabricVnidName.setStatus("current")
_CLFabricVnidNetworkIPType_Type = InetAddressType
_CLFabricVnidNetworkIPType_Object = MibTableColumn
cLFabricVnidNetworkIPType = _CLFabricVnidNetworkIPType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 2, 1, 2),
    _CLFabricVnidNetworkIPType_Type()
)
cLFabricVnidNetworkIPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLFabricVnidNetworkIPType.setStatus("current")
_CLFabricVnidNetworkIP_Type = InetAddress
_CLFabricVnidNetworkIP_Object = MibTableColumn
cLFabricVnidNetworkIP = _CLFabricVnidNetworkIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 2, 1, 3),
    _CLFabricVnidNetworkIP_Type()
)
cLFabricVnidNetworkIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLFabricVnidNetworkIP.setStatus("current")
_CLFabricVnidSubnetIPType_Type = InetAddressType
_CLFabricVnidSubnetIPType_Object = MibTableColumn
cLFabricVnidSubnetIPType = _CLFabricVnidSubnetIPType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 2, 1, 4),
    _CLFabricVnidSubnetIPType_Type()
)
cLFabricVnidSubnetIPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLFabricVnidSubnetIPType.setStatus("current")
_CLFabricVnidSubnetIP_Type = InetAddress
_CLFabricVnidSubnetIP_Object = MibTableColumn
cLFabricVnidSubnetIP = _CLFabricVnidSubnetIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 2, 1, 5),
    _CLFabricVnidSubnetIP_Type()
)
cLFabricVnidSubnetIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLFabricVnidSubnetIP.setStatus("current")
_CLFabricLayer2Vnid_Type = Unsigned32
_CLFabricLayer2Vnid_Object = MibTableColumn
cLFabricLayer2Vnid = _CLFabricLayer2Vnid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 2, 1, 6),
    _CLFabricLayer2Vnid_Type()
)
cLFabricLayer2Vnid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLFabricLayer2Vnid.setStatus("current")
_CLFabricLayer3Vnid_Type = Unsigned32
_CLFabricLayer3Vnid_Object = MibTableColumn
cLFabricLayer3Vnid = _CLFabricLayer3Vnid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 2, 1, 7),
    _CLFabricLayer3Vnid_Type()
)
cLFabricLayer3Vnid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLFabricLayer3Vnid.setStatus("current")
_CLFabricVnidRowStatus_Type = RowStatus
_CLFabricVnidRowStatus_Object = MibTableColumn
cLFabricVnidRowStatus = _CLFabricVnidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 2, 1, 8),
    _CLFabricVnidRowStatus_Type()
)
cLFabricVnidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLFabricVnidRowStatus.setStatus("current")
_CLFabricWlanTable_Object = MibTable
cLFabricWlanTable = _CLFabricWlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cLFabricWlanTable.setStatus("current")
_CLFabricWlanEntry_Object = MibTableRow
cLFabricWlanEntry = _CLFabricWlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 3, 1)
)
cLFabricWlanEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLFabricWlanEntry.setStatus("current")


class _CLFabricWlanFabricStatus_Type(TruthValue):
    """Custom type cLFabricWlanFabricStatus based on TruthValue"""
    defaultValue = 2


_CLFabricWlanFabricStatus_Type.__name__ = "TruthValue"
_CLFabricWlanFabricStatus_Object = MibTableColumn
cLFabricWlanFabricStatus = _CLFabricWlanFabricStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 3, 1, 1),
    _CLFabricWlanFabricStatus_Type()
)
cLFabricWlanFabricStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLFabricWlanFabricStatus.setStatus("current")
_CLFabricWlanAclName_Type = SnmpAdminString
_CLFabricWlanAclName_Object = MibTableColumn
cLFabricWlanAclName = _CLFabricWlanAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 3, 1, 2),
    _CLFabricWlanAclName_Type()
)
cLFabricWlanAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLFabricWlanAclName.setStatus("current")
_CLFabricWlanAvcName_Type = SnmpAdminString
_CLFabricWlanAvcName_Object = MibTableColumn
cLFabricWlanAvcName = _CLFabricWlanAvcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 3, 1, 3),
    _CLFabricWlanAvcName_Type()
)
cLFabricWlanAvcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLFabricWlanAvcName.setStatus("current")
_CLFabricWlanVnidName_Type = SnmpAdminString
_CLFabricWlanVnidName_Object = MibTableColumn
cLFabricWlanVnidName = _CLFabricWlanVnidName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 3, 1, 4),
    _CLFabricWlanVnidName_Type()
)
cLFabricWlanVnidName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLFabricWlanVnidName.setStatus("current")
_CLFabricWlanVnid_Type = Unsigned32
_CLFabricWlanVnid_Object = MibTableColumn
cLFabricWlanVnid = _CLFabricWlanVnid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 3, 1, 5),
    _CLFabricWlanVnid_Type()
)
cLFabricWlanVnid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLFabricWlanVnid.setStatus("current")
_CLFabricWlanSgt_Type = Unsigned32
_CLFabricWlanSgt_Object = MibTableColumn
cLFabricWlanSgt = _CLFabricWlanSgt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 3, 1, 6),
    _CLFabricWlanSgt_Type()
)
cLFabricWlanSgt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLFabricWlanSgt.setStatus("current")
_CLFabricWlanSwitchIpType_Type = InetAddressType
_CLFabricWlanSwitchIpType_Object = MibTableColumn
cLFabricWlanSwitchIpType = _CLFabricWlanSwitchIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 3, 1, 7),
    _CLFabricWlanSwitchIpType_Type()
)
cLFabricWlanSwitchIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLFabricWlanSwitchIpType.setStatus("current")
_CLFabricWlanSwitchIp_Type = InetAddress
_CLFabricWlanSwitchIp_Object = MibTableColumn
cLFabricWlanSwitchIp = _CLFabricWlanSwitchIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 3, 1, 8),
    _CLFabricWlanSwitchIp_Type()
)
cLFabricWlanSwitchIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLFabricWlanSwitchIp.setStatus("current")
_CLFabricControlplaneStatsTable_Object = MibTable
cLFabricControlplaneStatsTable = _CLFabricControlplaneStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cLFabricControlplaneStatsTable.setStatus("current")
_CLFabricControlplaneStatsEntry_Object = MibTableRow
cLFabricControlplaneStatsEntry = _CLFabricControlplaneStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1)
)
cLFabricControlplaneStatsEntry.setIndexNames(
    (0, "CISCO-LWAPP-FABRIC-MIB", "cLFabricControlplaneDomainType"),
    (0, "CISCO-LWAPP-FABRIC-MIB", "cLFabricControlplaneUnitType"),
    (0, "CISCO-LWAPP-FABRIC-MIB", "cLFabricControlplaneIPType"),
    (0, "CISCO-LWAPP-FABRIC-MIB", "cLFabricControlplaneIP"),
)
if mibBuilder.loadTexts:
    cLFabricControlplaneStatsEntry.setStatus("current")


class _CLFabricCPStatus_Type(Integer32):
    """Custom type cLFabricCPStatus based on Integer32"""
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
        *(("disconnected", 1),
          ("inprogress", 2),
          ("connected", 3))
    )


_CLFabricCPStatus_Type.__name__ = "Integer32"
_CLFabricCPStatus_Object = MibTableColumn
cLFabricCPStatus = _CLFabricCPStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 1),
    _CLFabricCPStatus_Type()
)
cLFabricCPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPStatus.setStatus("current")


class _CLFabricCPUptime_Type(TimeTicks):
    """Custom type cLFabricCPUptime based on TimeTicks"""
    defaultValue = 0


_CLFabricCPUptime_Type.__name__ = "TimeTicks"
_CLFabricCPUptime_Object = MibTableColumn
cLFabricCPUptime = _CLFabricCPUptime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 2),
    _CLFabricCPUptime_Type()
)
cLFabricCPUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPUptime.setStatus("current")


class _CLFabricCPRegnSent_Type(Unsigned64):
    """Custom type cLFabricCPRegnSent based on Unsigned64"""
    defaultValue = 0


_CLFabricCPRegnSent_Type.__name__ = "Unsigned64"
_CLFabricCPRegnSent_Object = MibTableColumn
cLFabricCPRegnSent = _CLFabricCPRegnSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 3),
    _CLFabricCPRegnSent_Type()
)
cLFabricCPRegnSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPRegnSent.setStatus("current")


class _CLFabricCPDeRegnSent_Type(Unsigned64):
    """Custom type cLFabricCPDeRegnSent based on Unsigned64"""
    defaultValue = 0


_CLFabricCPDeRegnSent_Type.__name__ = "Unsigned64"
_CLFabricCPDeRegnSent_Object = MibTableColumn
cLFabricCPDeRegnSent = _CLFabricCPDeRegnSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 4),
    _CLFabricCPDeRegnSent_Type()
)
cLFabricCPDeRegnSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPDeRegnSent.setStatus("current")


class _CLFabricCPRegnConnUpSent_Type(Unsigned64):
    """Custom type cLFabricCPRegnConnUpSent based on Unsigned64"""
    defaultValue = 0


_CLFabricCPRegnConnUpSent_Type.__name__ = "Unsigned64"
_CLFabricCPRegnConnUpSent_Object = MibTableColumn
cLFabricCPRegnConnUpSent = _CLFabricCPRegnConnUpSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 5),
    _CLFabricCPRegnConnUpSent_Type()
)
cLFabricCPRegnConnUpSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPRegnConnUpSent.setStatus("current")


class _CLFabricCPDeRegnConnUpSent_Type(Unsigned64):
    """Custom type cLFabricCPDeRegnConnUpSent based on Unsigned64"""
    defaultValue = 0


_CLFabricCPDeRegnConnUpSent_Type.__name__ = "Unsigned64"
_CLFabricCPDeRegnConnUpSent_Object = MibTableColumn
cLFabricCPDeRegnConnUpSent = _CLFabricCPDeRegnConnUpSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 6),
    _CLFabricCPDeRegnConnUpSent_Type()
)
cLFabricCPDeRegnConnUpSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPDeRegnConnUpSent.setStatus("current")


class _CLFabricCPRegnSuccess_Type(Unsigned64):
    """Custom type cLFabricCPRegnSuccess based on Unsigned64"""
    defaultValue = 0


_CLFabricCPRegnSuccess_Type.__name__ = "Unsigned64"
_CLFabricCPRegnSuccess_Object = MibTableColumn
cLFabricCPRegnSuccess = _CLFabricCPRegnSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 7),
    _CLFabricCPRegnSuccess_Type()
)
cLFabricCPRegnSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPRegnSuccess.setStatus("current")


class _CLFabricCPDeRegnSuccess_Type(Unsigned64):
    """Custom type cLFabricCPDeRegnSuccess based on Unsigned64"""
    defaultValue = 0


_CLFabricCPDeRegnSuccess_Type.__name__ = "Unsigned64"
_CLFabricCPDeRegnSuccess_Object = MibTableColumn
cLFabricCPDeRegnSuccess = _CLFabricCPDeRegnSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 8),
    _CLFabricCPDeRegnSuccess_Type()
)
cLFabricCPDeRegnSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPDeRegnSuccess.setStatus("current")


class _CLFabricCPRegnConnUpSuccess_Type(Unsigned64):
    """Custom type cLFabricCPRegnConnUpSuccess based on Unsigned64"""
    defaultValue = 0


_CLFabricCPRegnConnUpSuccess_Type.__name__ = "Unsigned64"
_CLFabricCPRegnConnUpSuccess_Object = MibTableColumn
cLFabricCPRegnConnUpSuccess = _CLFabricCPRegnConnUpSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 9),
    _CLFabricCPRegnConnUpSuccess_Type()
)
cLFabricCPRegnConnUpSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPRegnConnUpSuccess.setStatus("current")


class _CLFabricCPDeRegnConnUpSuccess_Type(Unsigned64):
    """Custom type cLFabricCPDeRegnConnUpSuccess based on Unsigned64"""
    defaultValue = 0


_CLFabricCPDeRegnConnUpSuccess_Type.__name__ = "Unsigned64"
_CLFabricCPDeRegnConnUpSuccess_Object = MibTableColumn
cLFabricCPDeRegnConnUpSuccess = _CLFabricCPDeRegnConnUpSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 10),
    _CLFabricCPDeRegnConnUpSuccess_Type()
)
cLFabricCPDeRegnConnUpSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPDeRegnConnUpSuccess.setStatus("current")


class _CLFabricCPRegnRej_Type(Unsigned64):
    """Custom type cLFabricCPRegnRej based on Unsigned64"""
    defaultValue = 0


_CLFabricCPRegnRej_Type.__name__ = "Unsigned64"
_CLFabricCPRegnRej_Object = MibTableColumn
cLFabricCPRegnRej = _CLFabricCPRegnRej_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 11),
    _CLFabricCPRegnRej_Type()
)
cLFabricCPRegnRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPRegnRej.setStatus("current")


class _CLFabricCPDeRegnRej_Type(Unsigned64):
    """Custom type cLFabricCPDeRegnRej based on Unsigned64"""
    defaultValue = 0


_CLFabricCPDeRegnRej_Type.__name__ = "Unsigned64"
_CLFabricCPDeRegnRej_Object = MibTableColumn
cLFabricCPDeRegnRej = _CLFabricCPDeRegnRej_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 12),
    _CLFabricCPDeRegnRej_Type()
)
cLFabricCPDeRegnRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPDeRegnRej.setStatus("current")


class _CLFabricCPRegnConnUpRej_Type(Unsigned64):
    """Custom type cLFabricCPRegnConnUpRej based on Unsigned64"""
    defaultValue = 0


_CLFabricCPRegnConnUpRej_Type.__name__ = "Unsigned64"
_CLFabricCPRegnConnUpRej_Object = MibTableColumn
cLFabricCPRegnConnUpRej = _CLFabricCPRegnConnUpRej_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 13),
    _CLFabricCPRegnConnUpRej_Type()
)
cLFabricCPRegnConnUpRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPRegnConnUpRej.setStatus("current")


class _CLFabricCPDeRegnConnUpRej_Type(Unsigned64):
    """Custom type cLFabricCPDeRegnConnUpRej based on Unsigned64"""
    defaultValue = 0


_CLFabricCPDeRegnConnUpRej_Type.__name__ = "Unsigned64"
_CLFabricCPDeRegnConnUpRej_Object = MibTableColumn
cLFabricCPDeRegnConnUpRej = _CLFabricCPDeRegnConnUpRej_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 14),
    _CLFabricCPDeRegnConnUpRej_Type()
)
cLFabricCPDeRegnConnUpRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPDeRegnConnUpRej.setStatus("current")


class _CLFabricCPRegnErr_Type(Unsigned64):
    """Custom type cLFabricCPRegnErr based on Unsigned64"""
    defaultValue = 0


_CLFabricCPRegnErr_Type.__name__ = "Unsigned64"
_CLFabricCPRegnErr_Object = MibTableColumn
cLFabricCPRegnErr = _CLFabricCPRegnErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 15),
    _CLFabricCPRegnErr_Type()
)
cLFabricCPRegnErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPRegnErr.setStatus("current")


class _CLFabricCPDeRegnErr_Type(Unsigned64):
    """Custom type cLFabricCPDeRegnErr based on Unsigned64"""
    defaultValue = 0


_CLFabricCPDeRegnErr_Type.__name__ = "Unsigned64"
_CLFabricCPDeRegnErr_Object = MibTableColumn
cLFabricCPDeRegnErr = _CLFabricCPDeRegnErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 16),
    _CLFabricCPDeRegnErr_Type()
)
cLFabricCPDeRegnErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPDeRegnErr.setStatus("current")


class _CLFabricCPRegnConnUpErr_Type(Unsigned64):
    """Custom type cLFabricCPRegnConnUpErr based on Unsigned64"""
    defaultValue = 0


_CLFabricCPRegnConnUpErr_Type.__name__ = "Unsigned64"
_CLFabricCPRegnConnUpErr_Object = MibTableColumn
cLFabricCPRegnConnUpErr = _CLFabricCPRegnConnUpErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 17),
    _CLFabricCPRegnConnUpErr_Type()
)
cLFabricCPRegnConnUpErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPRegnConnUpErr.setStatus("current")


class _CLFabricCPDeRegnConnUpErr_Type(Unsigned64):
    """Custom type cLFabricCPDeRegnConnUpErr based on Unsigned64"""
    defaultValue = 0


_CLFabricCPDeRegnConnUpErr_Type.__name__ = "Unsigned64"
_CLFabricCPDeRegnConnUpErr_Object = MibTableColumn
cLFabricCPDeRegnConnUpErr = _CLFabricCPDeRegnConnUpErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 18),
    _CLFabricCPDeRegnConnUpErr_Type()
)
cLFabricCPDeRegnConnUpErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPDeRegnConnUpErr.setStatus("current")


class _CLFabricCPRefreshMsgRcv_Type(Unsigned64):
    """Custom type cLFabricCPRefreshMsgRcv based on Unsigned64"""
    defaultValue = 0


_CLFabricCPRefreshMsgRcv_Type.__name__ = "Unsigned64"
_CLFabricCPRefreshMsgRcv_Object = MibTableColumn
cLFabricCPRefreshMsgRcv = _CLFabricCPRefreshMsgRcv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 19),
    _CLFabricCPRefreshMsgRcv_Type()
)
cLFabricCPRefreshMsgRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPRefreshMsgRcv.setStatus("current")


class _CLFabricCPRejRegnReTrans_Type(Unsigned64):
    """Custom type cLFabricCPRejRegnReTrans based on Unsigned64"""
    defaultValue = 0


_CLFabricCPRejRegnReTrans_Type.__name__ = "Unsigned64"
_CLFabricCPRejRegnReTrans_Object = MibTableColumn
cLFabricCPRejRegnReTrans = _CLFabricCPRejRegnReTrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 20),
    _CLFabricCPRejRegnReTrans_Type()
)
cLFabricCPRejRegnReTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPRejRegnReTrans.setStatus("current")


class _CLFabricCPDeRejRegnReTrans_Type(Unsigned64):
    """Custom type cLFabricCPDeRejRegnReTrans based on Unsigned64"""
    defaultValue = 0


_CLFabricCPDeRejRegnReTrans_Type.__name__ = "Unsigned64"
_CLFabricCPDeRejRegnReTrans_Object = MibTableColumn
cLFabricCPDeRejRegnReTrans = _CLFabricCPDeRejRegnReTrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 21),
    _CLFabricCPDeRejRegnReTrans_Type()
)
cLFabricCPDeRejRegnReTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPDeRejRegnReTrans.setStatus("current")


class _CLFabricCPRejRegnConnUpReTrans_Type(Unsigned64):
    """Custom type cLFabricCPRejRegnConnUpReTrans based on Unsigned64"""
    defaultValue = 0


_CLFabricCPRejRegnConnUpReTrans_Type.__name__ = "Unsigned64"
_CLFabricCPRejRegnConnUpReTrans_Object = MibTableColumn
cLFabricCPRejRegnConnUpReTrans = _CLFabricCPRejRegnConnUpReTrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 22),
    _CLFabricCPRejRegnConnUpReTrans_Type()
)
cLFabricCPRejRegnConnUpReTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPRejRegnConnUpReTrans.setStatus("current")


class _CLFabricCPDeRejRegnConnUpReTrans_Type(Unsigned64):
    """Custom type cLFabricCPDeRejRegnConnUpReTrans based on Unsigned64"""
    defaultValue = 0


_CLFabricCPDeRejRegnConnUpReTrans_Type.__name__ = "Unsigned64"
_CLFabricCPDeRejRegnConnUpReTrans_Object = MibTableColumn
cLFabricCPDeRejRegnConnUpReTrans = _CLFabricCPDeRejRegnConnUpReTrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 23),
    _CLFabricCPDeRejRegnConnUpReTrans_Type()
)
cLFabricCPDeRejRegnConnUpReTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPDeRejRegnConnUpReTrans.setStatus("current")


class _CLFabricCPConnLossCnt_Type(Unsigned64):
    """Custom type cLFabricCPConnLossCnt based on Unsigned64"""
    defaultValue = 0


_CLFabricCPConnLossCnt_Type.__name__ = "Unsigned64"
_CLFabricCPConnLossCnt_Object = MibTableColumn
cLFabricCPConnLossCnt = _CLFabricCPConnLossCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 24),
    _CLFabricCPConnLossCnt_Type()
)
cLFabricCPConnLossCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPConnLossCnt.setStatus("current")


class _CLFabricCPConnRestoreCnt_Type(Unsigned64):
    """Custom type cLFabricCPConnRestoreCnt based on Unsigned64"""
    defaultValue = 0


_CLFabricCPConnRestoreCnt_Type.__name__ = "Unsigned64"
_CLFabricCPConnRestoreCnt_Object = MibTableColumn
cLFabricCPConnRestoreCnt = _CLFabricCPConnRestoreCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 25),
    _CLFabricCPConnRestoreCnt_Type()
)
cLFabricCPConnRestoreCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPConnRestoreCnt.setStatus("current")


class _CLFabricCPBulkRegnSent_Type(Unsigned64):
    """Custom type cLFabricCPBulkRegnSent based on Unsigned64"""
    defaultValue = 0


_CLFabricCPBulkRegnSent_Type.__name__ = "Unsigned64"
_CLFabricCPBulkRegnSent_Object = MibTableColumn
cLFabricCPBulkRegnSent = _CLFabricCPBulkRegnSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 26),
    _CLFabricCPBulkRegnSent_Type()
)
cLFabricCPBulkRegnSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPBulkRegnSent.setStatus("current")


class _CLFabricCPBulkDeRegnSent_Type(Unsigned64):
    """Custom type cLFabricCPBulkDeRegnSent based on Unsigned64"""
    defaultValue = 0


_CLFabricCPBulkDeRegnSent_Type.__name__ = "Unsigned64"
_CLFabricCPBulkDeRegnSent_Object = MibTableColumn
cLFabricCPBulkDeRegnSent = _CLFabricCPBulkDeRegnSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 27),
    _CLFabricCPBulkDeRegnSent_Type()
)
cLFabricCPBulkDeRegnSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPBulkDeRegnSent.setStatus("current")


class _CLFabricCPBulkRegnConnUpSent_Type(Unsigned64):
    """Custom type cLFabricCPBulkRegnConnUpSent based on Unsigned64"""
    defaultValue = 0


_CLFabricCPBulkRegnConnUpSent_Type.__name__ = "Unsigned64"
_CLFabricCPBulkRegnConnUpSent_Object = MibTableColumn
cLFabricCPBulkRegnConnUpSent = _CLFabricCPBulkRegnConnUpSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 28),
    _CLFabricCPBulkRegnConnUpSent_Type()
)
cLFabricCPBulkRegnConnUpSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPBulkRegnConnUpSent.setStatus("current")


class _CLFabricCPBulkDeRegnConnUpSent_Type(Unsigned64):
    """Custom type cLFabricCPBulkDeRegnConnUpSent based on Unsigned64"""
    defaultValue = 0


_CLFabricCPBulkDeRegnConnUpSent_Type.__name__ = "Unsigned64"
_CLFabricCPBulkDeRegnConnUpSent_Object = MibTableColumn
cLFabricCPBulkDeRegnConnUpSent = _CLFabricCPBulkDeRegnConnUpSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 29),
    _CLFabricCPBulkDeRegnConnUpSent_Type()
)
cLFabricCPBulkDeRegnConnUpSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPBulkDeRegnConnUpSent.setStatus("current")


class _CLFabricCPMapReqSent_Type(Unsigned64):
    """Custom type cLFabricCPMapReqSent based on Unsigned64"""
    defaultValue = 0


_CLFabricCPMapReqSent_Type.__name__ = "Unsigned64"
_CLFabricCPMapReqSent_Object = MibTableColumn
cLFabricCPMapReqSent = _CLFabricCPMapReqSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 30),
    _CLFabricCPMapReqSent_Type()
)
cLFabricCPMapReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPMapReqSent.setStatus("current")


class _CLFabricCPMapReqRetry_Type(Unsigned64):
    """Custom type cLFabricCPMapReqRetry based on Unsigned64"""
    defaultValue = 0


_CLFabricCPMapReqRetry_Type.__name__ = "Unsigned64"
_CLFabricCPMapReqRetry_Object = MibTableColumn
cLFabricCPMapReqRetry = _CLFabricCPMapReqRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 31),
    _CLFabricCPMapReqRetry_Type()
)
cLFabricCPMapReqRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPMapReqRetry.setStatus("current")


class _CLFabricCPMapReplyRcv_Type(Unsigned64):
    """Custom type cLFabricCPMapReplyRcv based on Unsigned64"""
    defaultValue = 0


_CLFabricCPMapReplyRcv_Type.__name__ = "Unsigned64"
_CLFabricCPMapReplyRcv_Object = MibTableColumn
cLFabricCPMapReplyRcv = _CLFabricCPMapReplyRcv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 32),
    _CLFabricCPMapReplyRcv_Type()
)
cLFabricCPMapReplyRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPMapReplyRcv.setStatus("current")


class _CLFabricCPMapReplyAckRcv_Type(Unsigned64):
    """Custom type cLFabricCPMapReplyAckRcv based on Unsigned64"""
    defaultValue = 0


_CLFabricCPMapReplyAckRcv_Type.__name__ = "Unsigned64"
_CLFabricCPMapReplyAckRcv_Object = MibTableColumn
cLFabricCPMapReplyAckRcv = _CLFabricCPMapReplyAckRcv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 33),
    _CLFabricCPMapReplyAckRcv_Type()
)
cLFabricCPMapReplyAckRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPMapReplyAckRcv.setStatus("current")


class _CLFabricCPMapReplyNackRcv_Type(Unsigned64):
    """Custom type cLFabricCPMapReplyNackRcv based on Unsigned64"""
    defaultValue = 0


_CLFabricCPMapReplyNackRcv_Type.__name__ = "Unsigned64"
_CLFabricCPMapReplyNackRcv_Object = MibTableColumn
cLFabricCPMapReplyNackRcv = _CLFabricCPMapReplyNackRcv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 34),
    _CLFabricCPMapReplyNackRcv_Type()
)
cLFabricCPMapReplyNackRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPMapReplyNackRcv.setStatus("current")


class _CLFabricCPBulkSyncInProg_Type(TruthValue):
    """Custom type cLFabricCPBulkSyncInProg based on TruthValue"""
    defaultValue = 2


_CLFabricCPBulkSyncInProg_Type.__name__ = "TruthValue"
_CLFabricCPBulkSyncInProg_Object = MibTableColumn
cLFabricCPBulkSyncInProg = _CLFabricCPBulkSyncInProg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 35),
    _CLFabricCPBulkSyncInProg_Type()
)
cLFabricCPBulkSyncInProg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPBulkSyncInProg.setStatus("current")


class _CLFabricCPApBulkSyncInProg_Type(TruthValue):
    """Custom type cLFabricCPApBulkSyncInProg based on TruthValue"""
    defaultValue = 2


_CLFabricCPApBulkSyncInProg_Type.__name__ = "TruthValue"
_CLFabricCPApBulkSyncInProg_Object = MibTableColumn
cLFabricCPApBulkSyncInProg = _CLFabricCPApBulkSyncInProg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 36),
    _CLFabricCPApBulkSyncInProg_Type()
)
cLFabricCPApBulkSyncInProg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPApBulkSyncInProg.setStatus("current")


class _CLFabricCPRegnRejRefrshInProg_Type(TruthValue):
    """Custom type cLFabricCPRegnRejRefrshInProg based on TruthValue"""
    defaultValue = 2


_CLFabricCPRegnRejRefrshInProg_Type.__name__ = "TruthValue"
_CLFabricCPRegnRejRefrshInProg_Object = MibTableColumn
cLFabricCPRegnRejRefrshInProg = _CLFabricCPRegnRejRefrshInProg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 4, 1, 37),
    _CLFabricCPRegnRejRefrshInProg_Type()
)
cLFabricCPRegnRejRefrshInProg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCPRegnRejRefrshInProg.setStatus("current")
_CLFabricApTable_Object = MibTable
cLFabricApTable = _CLFabricApTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cLFabricApTable.setStatus("current")
_CLFabricApEntry_Object = MibTableRow
cLFabricApEntry = _CLFabricApEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 5, 1)
)
cLFabricApEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    cLFabricApEntry.setStatus("current")


class _CLFabricApFabricStatus_Type(TruthValue):
    """Custom type cLFabricApFabricStatus based on TruthValue"""
    defaultValue = 2


_CLFabricApFabricStatus_Type.__name__ = "TruthValue"
_CLFabricApFabricStatus_Object = MibTableColumn
cLFabricApFabricStatus = _CLFabricApFabricStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 5, 1, 1),
    _CLFabricApFabricStatus_Type()
)
cLFabricApFabricStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricApFabricStatus.setStatus("current")
_CLFabricApPeerSwitchIpType_Type = InetAddressType
_CLFabricApPeerSwitchIpType_Object = MibTableColumn
cLFabricApPeerSwitchIpType = _CLFabricApPeerSwitchIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 5, 1, 2),
    _CLFabricApPeerSwitchIpType_Type()
)
cLFabricApPeerSwitchIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricApPeerSwitchIpType.setStatus("current")
_CLFabricApPeerSwitchIp_Type = InetAddress
_CLFabricApPeerSwitchIp_Object = MibTableColumn
cLFabricApPeerSwitchIp = _CLFabricApPeerSwitchIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 5, 1, 3),
    _CLFabricApPeerSwitchIp_Type()
)
cLFabricApPeerSwitchIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricApPeerSwitchIp.setStatus("current")
_CLFabricApLayer2Vnid_Type = Unsigned32
_CLFabricApLayer2Vnid_Object = MibTableColumn
cLFabricApLayer2Vnid = _CLFabricApLayer2Vnid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 5, 1, 4),
    _CLFabricApLayer2Vnid_Type()
)
cLFabricApLayer2Vnid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricApLayer2Vnid.setStatus("current")
_CLFabricApLayer3Vnid_Type = Unsigned32
_CLFabricApLayer3Vnid_Object = MibTableColumn
cLFabricApLayer3Vnid = _CLFabricApLayer3Vnid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 5, 1, 5),
    _CLFabricApLayer3Vnid_Type()
)
cLFabricApLayer3Vnid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricApLayer3Vnid.setStatus("current")


class _CLFabricAPMapReqSent_Type(Unsigned32):
    """Custom type cLFabricAPMapReqSent based on Unsigned32"""
    defaultValue = 0


_CLFabricAPMapReqSent_Type.__name__ = "Unsigned32"
_CLFabricAPMapReqSent_Object = MibTableColumn
cLFabricAPMapReqSent = _CLFabricAPMapReqSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 5, 1, 6),
    _CLFabricAPMapReqSent_Type()
)
cLFabricAPMapReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricAPMapReqSent.setStatus("current")


class _CLFabricAPMapReqRetry_Type(Unsigned32):
    """Custom type cLFabricAPMapReqRetry based on Unsigned32"""
    defaultValue = 0


_CLFabricAPMapReqRetry_Type.__name__ = "Unsigned32"
_CLFabricAPMapReqRetry_Object = MibTableColumn
cLFabricAPMapReqRetry = _CLFabricAPMapReqRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 5, 1, 7),
    _CLFabricAPMapReqRetry_Type()
)
cLFabricAPMapReqRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricAPMapReqRetry.setStatus("current")


class _CLFabricAPMapReplyRcvd_Type(Unsigned32):
    """Custom type cLFabricAPMapReplyRcvd based on Unsigned32"""
    defaultValue = 0


_CLFabricAPMapReplyRcvd_Type.__name__ = "Unsigned32"
_CLFabricAPMapReplyRcvd_Object = MibTableColumn
cLFabricAPMapReplyRcvd = _CLFabricAPMapReplyRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 5, 1, 8),
    _CLFabricAPMapReplyRcvd_Type()
)
cLFabricAPMapReplyRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricAPMapReplyRcvd.setStatus("current")


class _CLFabricAPMapReplyAckRcvd_Type(Unsigned32):
    """Custom type cLFabricAPMapReplyAckRcvd based on Unsigned32"""
    defaultValue = 0


_CLFabricAPMapReplyAckRcvd_Type.__name__ = "Unsigned32"
_CLFabricAPMapReplyAckRcvd_Object = MibTableColumn
cLFabricAPMapReplyAckRcvd = _CLFabricAPMapReplyAckRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 5, 1, 9),
    _CLFabricAPMapReplyAckRcvd_Type()
)
cLFabricAPMapReplyAckRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricAPMapReplyAckRcvd.setStatus("current")


class _CLFabricAPMapReplyNackRcvd_Type(Unsigned32):
    """Custom type cLFabricAPMapReplyNackRcvd based on Unsigned32"""
    defaultValue = 0


_CLFabricAPMapReplyNackRcvd_Type.__name__ = "Unsigned32"
_CLFabricAPMapReplyNackRcvd_Object = MibTableColumn
cLFabricAPMapReplyNackRcvd = _CLFabricAPMapReplyNackRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 5, 1, 10),
    _CLFabricAPMapReplyNackRcvd_Type()
)
cLFabricAPMapReplyNackRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricAPMapReplyNackRcvd.setStatus("current")


class _CLFabricAPRegnSuccess_Type(Unsigned32):
    """Custom type cLFabricAPRegnSuccess based on Unsigned32"""
    defaultValue = 0


_CLFabricAPRegnSuccess_Type.__name__ = "Unsigned32"
_CLFabricAPRegnSuccess_Object = MibTableColumn
cLFabricAPRegnSuccess = _CLFabricAPRegnSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 5, 1, 11),
    _CLFabricAPRegnSuccess_Type()
)
cLFabricAPRegnSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricAPRegnSuccess.setStatus("current")


class _CLFabricAPRegnRej_Type(Unsigned32):
    """Custom type cLFabricAPRegnRej based on Unsigned32"""
    defaultValue = 0


_CLFabricAPRegnRej_Type.__name__ = "Unsigned32"
_CLFabricAPRegnRej_Object = MibTableColumn
cLFabricAPRegnRej = _CLFabricAPRegnRej_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 5, 1, 12),
    _CLFabricAPRegnRej_Type()
)
cLFabricAPRegnRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricAPRegnRej.setStatus("current")
_CLFabricClientTable_Object = MibTable
cLFabricClientTable = _CLFabricClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cLFabricClientTable.setStatus("current")
_CLFabricClientEntry_Object = MibTableRow
cLFabricClientEntry = _CLFabricClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 6, 1)
)
cLFabricClientEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cLFabricClientEntry.setStatus("current")


class _CLFabricClientFabricStatus_Type(TruthValue):
    """Custom type cLFabricClientFabricStatus based on TruthValue"""
    defaultValue = 2


_CLFabricClientFabricStatus_Type.__name__ = "TruthValue"
_CLFabricClientFabricStatus_Object = MibTableColumn
cLFabricClientFabricStatus = _CLFabricClientFabricStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 6, 1, 1),
    _CLFabricClientFabricStatus_Type()
)
cLFabricClientFabricStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricClientFabricStatus.setStatus("current")
_CLFabricClientVnid_Type = Unsigned32
_CLFabricClientVnid_Object = MibTableColumn
cLFabricClientVnid = _CLFabricClientVnid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 6, 1, 2),
    _CLFabricClientVnid_Type()
)
cLFabricClientVnid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricClientVnid.setStatus("current")
_CLFabricClientSwitchIpType_Type = InetAddressType
_CLFabricClientSwitchIpType_Object = MibTableColumn
cLFabricClientSwitchIpType = _CLFabricClientSwitchIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 6, 1, 3),
    _CLFabricClientSwitchIpType_Type()
)
cLFabricClientSwitchIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricClientSwitchIpType.setStatus("current")
_CLFabricCleintSwitchIp_Type = InetAddress
_CLFabricCleintSwitchIp_Object = MibTableColumn
cLFabricCleintSwitchIp = _CLFabricCleintSwitchIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 6, 1, 4),
    _CLFabricCleintSwitchIp_Type()
)
cLFabricCleintSwitchIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricCleintSwitchIp.setStatus("current")


class _CLFabricClientRegnSuccess_Type(Unsigned32):
    """Custom type cLFabricClientRegnSuccess based on Unsigned32"""
    defaultValue = 0


_CLFabricClientRegnSuccess_Type.__name__ = "Unsigned32"
_CLFabricClientRegnSuccess_Object = MibTableColumn
cLFabricClientRegnSuccess = _CLFabricClientRegnSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 6, 1, 5),
    _CLFabricClientRegnSuccess_Type()
)
cLFabricClientRegnSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricClientRegnSuccess.setStatus("current")


class _CLFabricClientRegnRej_Type(Unsigned32):
    """Custom type cLFabricClientRegnRej based on Unsigned32"""
    defaultValue = 0


_CLFabricClientRegnRej_Type.__name__ = "Unsigned32"
_CLFabricClientRegnRej_Object = MibTableColumn
cLFabricClientRegnRej = _CLFabricClientRegnRej_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 1, 6, 1, 6),
    _CLFabricClientRegnRej_Type()
)
cLFabricClientRegnRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLFabricClientRegnRej.setStatus("current")
_CiscoLwappFabricMIBGlobalObjects_ObjectIdentity = ObjectIdentity
ciscoLwappFabricMIBGlobalObjects = _CiscoLwappFabricMIBGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 2)
)


class _CLFabricGlobalStatus_Type(TruthValue):
    """Custom type cLFabricGlobalStatus based on TruthValue"""
    defaultValue = 2


_CLFabricGlobalStatus_Type.__name__ = "TruthValue"
_CLFabricGlobalStatus_Object = MibScalar
cLFabricGlobalStatus = _CLFabricGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 2, 1),
    _CLFabricGlobalStatus_Type()
)
cLFabricGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLFabricGlobalStatus.setStatus("current")


class _CLFabricApVnid_Type(Unsigned32):
    """Custom type cLFabricApVnid based on Unsigned32"""
    defaultValue = 0


_CLFabricApVnid_Type.__name__ = "Unsigned32"
_CLFabricApVnid_Object = MibScalar
cLFabricApVnid = _CLFabricApVnid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 1, 2, 2),
    _CLFabricApVnid_Type()
)
cLFabricApVnid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLFabricApVnid.setStatus("current")
_CiscoLwappFabricMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappFabricMIBConform = _CiscoLwappFabricMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 2)
)
_CiscoLwappFabricMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappFabricMIBCompliances = _CiscoLwappFabricMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 2, 1)
)
_CiscoLwappFabricMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappFabricMIBGroups = _CiscoLwappFabricMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 2, 2)
)

# Managed Objects groups

cLFabricConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 2, 2, 1)
)
cLFabricConfigGroup.setObjects(
      *(("CISCO-LWAPP-FABRIC-MIB", "cLFabricGlobalStatus"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricApVnid"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricControlplaneDomainType"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricControlplaneUnitType"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricControlplaneIPType"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricControlplaneIP"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricControlplanePSKKey"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricControlplaneRowStatus"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricVnidName"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricVnidNetworkIPType"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricVnidNetworkIP"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricVnidSubnetIPType"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricVnidSubnetIP"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricLayer2Vnid"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricLayer3Vnid"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricVnidRowStatus"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricWlanFabricStatus"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricWlanAclName"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricWlanAvcName"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricWlanVnidName"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricWlanVnid"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricWlanSgt"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricWlanSwitchIpType"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricWlanSwitchIp"))
)
if mibBuilder.loadTexts:
    cLFabricConfigGroup.setStatus("current")


# Notification objects

cLFabricMapRequestNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 0, 2)
)
cLFabricMapRequestNotify.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApIfMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApInetAddress"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricApLayer2Vnid"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricCPPrimaryMapServerIPType"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricCPPrimaryMapServerIP"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricCPSecondaryMapServerIPType"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricCPSecondaryMapServerIP"))
)
if mibBuilder.loadTexts:
    cLFabricMapRequestNotify.setStatus(
        "current"
    )

cLFabricMapResponseNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 0, 3)
)
cLFabricMapResponseNotify.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApIfMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApInetAddress"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricApLayer2Vnid"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricApPeerSwitchIpType"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricApPeerSwitchIp"))
)
if mibBuilder.loadTexts:
    cLFabricMapResponseNotify.setStatus(
        "current"
    )

cLFabricRegistrationReqNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 0, 4)
)
cLFabricRegistrationReqNotify.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricClientVnid"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricCPPrimaryMapServerIPType"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricCPPrimaryMapServerIP"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricCPSecondaryMapServerIPType"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricCPSecondaryMapServerIP"))
)
if mibBuilder.loadTexts:
    cLFabricRegistrationReqNotify.setStatus(
        "current"
    )

cLFabricDeRegistrationReqNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 0, 5)
)
cLFabricDeRegistrationReqNotify.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricClientVnid"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricCPPrimaryMapServerIPType"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricCPPrimaryMapServerIP"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricCPSecondaryMapServerIPType"),
        ("CISCO-LWAPP-FABRIC-MIB", "cLFabricCPSecondaryMapServerIP"))
)
if mibBuilder.loadTexts:
    cLFabricDeRegistrationReqNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ciscoLwappFabricMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 99991, 2, 1, 1)
)
ciscoLwappFabricMIBCompliance.setObjects(
    ("CISCO-LWAPP-FABRIC-MIB", "cLFabricConfigGroup")
)
if mibBuilder.loadTexts:
    ciscoLwappFabricMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-FABRIC-MIB",
    **{"ciscoLwappFabricMIB": ciscoLwappFabricMIB,
       "ciscoLwappFabricMIBNotifs": ciscoLwappFabricMIBNotifs,
       "ciscoLwappFabricNotifObjects": ciscoLwappFabricNotifObjects,
       "cLFabricCPPrimaryMapServerIPType": cLFabricCPPrimaryMapServerIPType,
       "cLFabricCPPrimaryMapServerIP": cLFabricCPPrimaryMapServerIP,
       "cLFabricCPSecondaryMapServerIPType": cLFabricCPSecondaryMapServerIPType,
       "cLFabricCPSecondaryMapServerIP": cLFabricCPSecondaryMapServerIP,
       "cLFabricMapRequestNotify": cLFabricMapRequestNotify,
       "cLFabricMapResponseNotify": cLFabricMapResponseNotify,
       "cLFabricRegistrationReqNotify": cLFabricRegistrationReqNotify,
       "cLFabricDeRegistrationReqNotify": cLFabricDeRegistrationReqNotify,
       "ciscoLwappFabricMIBObjects": ciscoLwappFabricMIBObjects,
       "ciscoLwappFabricMIBTableObjects": ciscoLwappFabricMIBTableObjects,
       "cLFabricControlplanePSKTable": cLFabricControlplanePSKTable,
       "cLFabricControlplanePSKEntry": cLFabricControlplanePSKEntry,
       "cLFabricControlplaneDomainType": cLFabricControlplaneDomainType,
       "cLFabricControlplaneUnitType": cLFabricControlplaneUnitType,
       "cLFabricControlplaneIPType": cLFabricControlplaneIPType,
       "cLFabricControlplaneIP": cLFabricControlplaneIP,
       "cLFabricControlplanePSKKey": cLFabricControlplanePSKKey,
       "cLFabricControlplaneRowStatus": cLFabricControlplaneRowStatus,
       "cLFabricVnidTable": cLFabricVnidTable,
       "cLFabricVnidEntry": cLFabricVnidEntry,
       "cLFabricVnidName": cLFabricVnidName,
       "cLFabricVnidNetworkIPType": cLFabricVnidNetworkIPType,
       "cLFabricVnidNetworkIP": cLFabricVnidNetworkIP,
       "cLFabricVnidSubnetIPType": cLFabricVnidSubnetIPType,
       "cLFabricVnidSubnetIP": cLFabricVnidSubnetIP,
       "cLFabricLayer2Vnid": cLFabricLayer2Vnid,
       "cLFabricLayer3Vnid": cLFabricLayer3Vnid,
       "cLFabricVnidRowStatus": cLFabricVnidRowStatus,
       "cLFabricWlanTable": cLFabricWlanTable,
       "cLFabricWlanEntry": cLFabricWlanEntry,
       "cLFabricWlanFabricStatus": cLFabricWlanFabricStatus,
       "cLFabricWlanAclName": cLFabricWlanAclName,
       "cLFabricWlanAvcName": cLFabricWlanAvcName,
       "cLFabricWlanVnidName": cLFabricWlanVnidName,
       "cLFabricWlanVnid": cLFabricWlanVnid,
       "cLFabricWlanSgt": cLFabricWlanSgt,
       "cLFabricWlanSwitchIpType": cLFabricWlanSwitchIpType,
       "cLFabricWlanSwitchIp": cLFabricWlanSwitchIp,
       "cLFabricControlplaneStatsTable": cLFabricControlplaneStatsTable,
       "cLFabricControlplaneStatsEntry": cLFabricControlplaneStatsEntry,
       "cLFabricCPStatus": cLFabricCPStatus,
       "cLFabricCPUptime": cLFabricCPUptime,
       "cLFabricCPRegnSent": cLFabricCPRegnSent,
       "cLFabricCPDeRegnSent": cLFabricCPDeRegnSent,
       "cLFabricCPRegnConnUpSent": cLFabricCPRegnConnUpSent,
       "cLFabricCPDeRegnConnUpSent": cLFabricCPDeRegnConnUpSent,
       "cLFabricCPRegnSuccess": cLFabricCPRegnSuccess,
       "cLFabricCPDeRegnSuccess": cLFabricCPDeRegnSuccess,
       "cLFabricCPRegnConnUpSuccess": cLFabricCPRegnConnUpSuccess,
       "cLFabricCPDeRegnConnUpSuccess": cLFabricCPDeRegnConnUpSuccess,
       "cLFabricCPRegnRej": cLFabricCPRegnRej,
       "cLFabricCPDeRegnRej": cLFabricCPDeRegnRej,
       "cLFabricCPRegnConnUpRej": cLFabricCPRegnConnUpRej,
       "cLFabricCPDeRegnConnUpRej": cLFabricCPDeRegnConnUpRej,
       "cLFabricCPRegnErr": cLFabricCPRegnErr,
       "cLFabricCPDeRegnErr": cLFabricCPDeRegnErr,
       "cLFabricCPRegnConnUpErr": cLFabricCPRegnConnUpErr,
       "cLFabricCPDeRegnConnUpErr": cLFabricCPDeRegnConnUpErr,
       "cLFabricCPRefreshMsgRcv": cLFabricCPRefreshMsgRcv,
       "cLFabricCPRejRegnReTrans": cLFabricCPRejRegnReTrans,
       "cLFabricCPDeRejRegnReTrans": cLFabricCPDeRejRegnReTrans,
       "cLFabricCPRejRegnConnUpReTrans": cLFabricCPRejRegnConnUpReTrans,
       "cLFabricCPDeRejRegnConnUpReTrans": cLFabricCPDeRejRegnConnUpReTrans,
       "cLFabricCPConnLossCnt": cLFabricCPConnLossCnt,
       "cLFabricCPConnRestoreCnt": cLFabricCPConnRestoreCnt,
       "cLFabricCPBulkRegnSent": cLFabricCPBulkRegnSent,
       "cLFabricCPBulkDeRegnSent": cLFabricCPBulkDeRegnSent,
       "cLFabricCPBulkRegnConnUpSent": cLFabricCPBulkRegnConnUpSent,
       "cLFabricCPBulkDeRegnConnUpSent": cLFabricCPBulkDeRegnConnUpSent,
       "cLFabricCPMapReqSent": cLFabricCPMapReqSent,
       "cLFabricCPMapReqRetry": cLFabricCPMapReqRetry,
       "cLFabricCPMapReplyRcv": cLFabricCPMapReplyRcv,
       "cLFabricCPMapReplyAckRcv": cLFabricCPMapReplyAckRcv,
       "cLFabricCPMapReplyNackRcv": cLFabricCPMapReplyNackRcv,
       "cLFabricCPBulkSyncInProg": cLFabricCPBulkSyncInProg,
       "cLFabricCPApBulkSyncInProg": cLFabricCPApBulkSyncInProg,
       "cLFabricCPRegnRejRefrshInProg": cLFabricCPRegnRejRefrshInProg,
       "cLFabricApTable": cLFabricApTable,
       "cLFabricApEntry": cLFabricApEntry,
       "cLFabricApFabricStatus": cLFabricApFabricStatus,
       "cLFabricApPeerSwitchIpType": cLFabricApPeerSwitchIpType,
       "cLFabricApPeerSwitchIp": cLFabricApPeerSwitchIp,
       "cLFabricApLayer2Vnid": cLFabricApLayer2Vnid,
       "cLFabricApLayer3Vnid": cLFabricApLayer3Vnid,
       "cLFabricAPMapReqSent": cLFabricAPMapReqSent,
       "cLFabricAPMapReqRetry": cLFabricAPMapReqRetry,
       "cLFabricAPMapReplyRcvd": cLFabricAPMapReplyRcvd,
       "cLFabricAPMapReplyAckRcvd": cLFabricAPMapReplyAckRcvd,
       "cLFabricAPMapReplyNackRcvd": cLFabricAPMapReplyNackRcvd,
       "cLFabricAPRegnSuccess": cLFabricAPRegnSuccess,
       "cLFabricAPRegnRej": cLFabricAPRegnRej,
       "cLFabricClientTable": cLFabricClientTable,
       "cLFabricClientEntry": cLFabricClientEntry,
       "cLFabricClientFabricStatus": cLFabricClientFabricStatus,
       "cLFabricClientVnid": cLFabricClientVnid,
       "cLFabricClientSwitchIpType": cLFabricClientSwitchIpType,
       "cLFabricCleintSwitchIp": cLFabricCleintSwitchIp,
       "cLFabricClientRegnSuccess": cLFabricClientRegnSuccess,
       "cLFabricClientRegnRej": cLFabricClientRegnRej,
       "ciscoLwappFabricMIBGlobalObjects": ciscoLwappFabricMIBGlobalObjects,
       "cLFabricGlobalStatus": cLFabricGlobalStatus,
       "cLFabricApVnid": cLFabricApVnid,
       "ciscoLwappFabricMIBConform": ciscoLwappFabricMIBConform,
       "ciscoLwappFabricMIBCompliances": ciscoLwappFabricMIBCompliances,
       "ciscoLwappFabricMIBCompliance": ciscoLwappFabricMIBCompliance,
       "ciscoLwappFabricMIBGroups": ciscoLwappFabricMIBGroups,
       "cLFabricConfigGroup": cLFabricConfigGroup}
)
