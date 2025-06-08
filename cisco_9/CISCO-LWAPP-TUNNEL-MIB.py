# SNMP MIB module (CISCO-LWAPP-TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-LWAPP-TUNNEL-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:55:06 2025
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

(cLApIfMacAddress,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-AP-MIB",
    "cLApIfMacAddress")

(cLWlanIndex,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-WLAN-MIB",
    "cLWlanIndex")

(cLWlanWlanPolicyName,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-WLAN-POLICY-MIB",
    "cLWlanWlanPolicyName")

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

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappTunnelMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 848)
)
if mibBuilder.loadTexts:
    ciscoLwappTunnelMIB.setRevisions(
        ("2019-06-03 00:00",
         "2018-09-06 00:00",
         "2018-07-01 00:00",
         "2018-02-05 00:00",
         "2017-09-20 00:00",
         "2017-05-26 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappTunnelMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappTunnelMIBNotifs = _CiscoLwappTunnelMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 0)
)
_CiscoLwappTunnelMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappTunnelMIBObjects = _CiscoLwappTunnelMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 1)
)


class _CLWATunnelStatusChangeReasonCode_Type(Integer32):
    """Custom type cLWATunnelStatusChangeReasonCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2),
          ("progress", 3))
    )


_CLWATunnelStatusChangeReasonCode_Type.__name__ = "Integer32"
_CLWATunnelStatusChangeReasonCode_Object = MibScalar
cLWATunnelStatusChangeReasonCode = _CLWATunnelStatusChangeReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 1, 1),
    _CLWATunnelStatusChangeReasonCode_Type()
)
cLWATunnelStatusChangeReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLWATunnelStatusChangeReasonCode.setStatus("current")
_CLWATunnelGwIPType_Type = InetAddressType
_CLWATunnelGwIPType_Object = MibScalar
cLWATunnelGwIPType = _CLWATunnelGwIPType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 1, 2),
    _CLWATunnelGwIPType_Type()
)
cLWATunnelGwIPType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLWATunnelGwIPType.setStatus("current")
_CLWATunnelGwIP_Type = InetAddress
_CLWATunnelGwIP_Object = MibScalar
cLWATunnelGwIP = _CLWATunnelGwIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 1, 3),
    _CLWATunnelGwIP_Type()
)
cLWATunnelGwIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLWATunnelGwIP.setStatus("current")
_CLWATunnelGwName_Type = SnmpAdminString
_CLWATunnelGwName_Object = MibScalar
cLWATunnelGwName = _CLWATunnelGwName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 1, 4),
    _CLWATunnelGwName_Type()
)
cLWATunnelGwName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLWATunnelGwName.setStatus("current")


class _CLWATunnelType_Type(Integer32):
    """Custom type cLWATunnelType based on Integer32"""
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
        *(("none", 1),
          ("pmipv6", 2),
          ("gtpv2", 3),
          ("eogre", 4))
    )


_CLWATunnelType_Type.__name__ = "Integer32"
_CLWATunnelType_Object = MibScalar
cLWATunnelType = _CLWATunnelType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 1, 5),
    _CLWATunnelType_Type()
)
cLWATunnelType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLWATunnelType.setStatus("current")
_CLWATunnelDomainName_Type = SnmpAdminString
_CLWATunnelDomainName_Object = MibScalar
cLWATunnelDomainName = _CLWATunnelDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 1, 6),
    _CLWATunnelDomainName_Type()
)
cLWATunnelDomainName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLWATunnelDomainName.setStatus("current")
_CLWATunnelActiveGwIPType_Type = InetAddressType
_CLWATunnelActiveGwIPType_Object = MibScalar
cLWATunnelActiveGwIPType = _CLWATunnelActiveGwIPType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 1, 7),
    _CLWATunnelActiveGwIPType_Type()
)
cLWATunnelActiveGwIPType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLWATunnelActiveGwIPType.setStatus("current")
_CLWATunnelActiveGwIP_Type = InetAddress
_CLWATunnelActiveGwIP_Object = MibScalar
cLWATunnelActiveGwIP = _CLWATunnelActiveGwIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 1, 8),
    _CLWATunnelActiveGwIP_Type()
)
cLWATunnelActiveGwIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLWATunnelActiveGwIP.setStatus("current")
_CLWATunnelActiveGwName_Type = SnmpAdminString
_CLWATunnelActiveGwName_Object = MibScalar
cLWATunnelActiveGwName = _CLWATunnelActiveGwName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 1, 9),
    _CLWATunnelActiveGwName_Type()
)
cLWATunnelActiveGwName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLWATunnelActiveGwName.setStatus("current")
_CLWATunnelProfileName_Type = SnmpAdminString
_CLWATunnelProfileName_Object = MibScalar
cLWATunnelProfileName = _CLWATunnelProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 1, 10),
    _CLWATunnelProfileName_Type()
)
cLWATunnelProfileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLWATunnelProfileName.setStatus("current")
_CLWATunnelRealm_Type = SnmpAdminString
_CLWATunnelRealm_Object = MibScalar
cLWATunnelRealm = _CLWATunnelRealm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 1, 11),
    _CLWATunnelRealm_Type()
)
cLWATunnelRealm.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLWATunnelRealm.setStatus("current")
_CLWATunnelVlanId_Type = Unsigned32
_CLWATunnelVlanId_Object = MibScalar
cLWATunnelVlanId = _CLWATunnelVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 1, 12),
    _CLWATunnelVlanId_Type()
)
cLWATunnelVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLWATunnelVlanId.setStatus("current")
_CLWATunnelClientMacAddress_Type = MacAddress
_CLWATunnelClientMacAddress_Object = MibScalar
cLWATunnelClientMacAddress = _CLWATunnelClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 1, 13),
    _CLWATunnelClientMacAddress_Type()
)
cLWATunnelClientMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLWATunnelClientMacAddress.setStatus("current")


class _CLWATunnelClientTypeChangeReasonCode_Type(Integer32):
    """Custom type cLWATunnelClientTypeChangeReasonCode based on Integer32"""
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
        *(("staticProfile", 1),
          ("aaaOveride", 2),
          ("dot1xAuthentication", 3),
          ("mobilityHandoff", 4))
    )


_CLWATunnelClientTypeChangeReasonCode_Type.__name__ = "Integer32"
_CLWATunnelClientTypeChangeReasonCode_Object = MibScalar
cLWATunnelClientTypeChangeReasonCode = _CLWATunnelClientTypeChangeReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 1, 14),
    _CLWATunnelClientTypeChangeReasonCode_Type()
)
cLWATunnelClientTypeChangeReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLWATunnelClientTypeChangeReasonCode.setStatus("current")
_CiscoLwappTunnelMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappTunnelMIBConform = _CiscoLwappTunnelMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 2)
)
_CiscoLwappTunnelMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappTunnelMIBCompliances = _CiscoLwappTunnelMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 2, 1)
)
_CiscoLwappTunnelMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappTunnelMIBGroups = _CiscoLwappTunnelMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 2, 2)
)
_CiscoLwappGatewayTunnel_ObjectIdentity = ObjectIdentity
ciscoLwappGatewayTunnel = _CiscoLwappGatewayTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3)
)
_ClGatewayTunnelTable_Object = MibTable
clGatewayTunnelTable = _ClGatewayTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 1)
)
if mibBuilder.loadTexts:
    clGatewayTunnelTable.setStatus("current")
_ClGatewayTunnelEntry_Object = MibTableRow
clGatewayTunnelEntry = _ClGatewayTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 1, 1)
)
clGatewayTunnelEntry.setIndexNames(
    (0, "CISCO-LWAPP-TUNNEL-MIB", "clGatewayTunnelName"),
    (0, "CISCO-LWAPP-TUNNEL-MIB", "clGatewayTunnelType"),
)
if mibBuilder.loadTexts:
    clGatewayTunnelEntry.setStatus("current")


class _ClGatewayTunnelName_Type(OctetString):
    """Custom type clGatewayTunnelName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_ClGatewayTunnelName_Type.__name__ = "OctetString"
_ClGatewayTunnelName_Object = MibTableColumn
clGatewayTunnelName = _ClGatewayTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 1, 1, 1),
    _ClGatewayTunnelName_Type()
)
clGatewayTunnelName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clGatewayTunnelName.setStatus("current")


class _ClGatewayTunnelType_Type(Integer32):
    """Custom type clGatewayTunnelType based on Integer32"""
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
        *(("none", 1),
          ("pmipv6", 2),
          ("gtpv2", 3),
          ("eogre", 4))
    )


_ClGatewayTunnelType_Type.__name__ = "Integer32"
_ClGatewayTunnelType_Object = MibTableColumn
clGatewayTunnelType = _ClGatewayTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 1, 1, 2),
    _ClGatewayTunnelType_Type()
)
clGatewayTunnelType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clGatewayTunnelType.setStatus("current")
_ClGatewayTunnelAddressType_Type = InetAddressType
_ClGatewayTunnelAddressType_Object = MibTableColumn
clGatewayTunnelAddressType = _ClGatewayTunnelAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 1, 1, 3),
    _ClGatewayTunnelAddressType_Type()
)
clGatewayTunnelAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clGatewayTunnelAddressType.setStatus("current")
_ClGatewayTunnelAddress_Type = InetAddress
_ClGatewayTunnelAddress_Object = MibTableColumn
clGatewayTunnelAddress = _ClGatewayTunnelAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 1, 1, 4),
    _ClGatewayTunnelAddress_Type()
)
clGatewayTunnelAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clGatewayTunnelAddress.setStatus("current")


class _ClGatewayTunnelStatus_Type(TruthValue):
    """Custom type clGatewayTunnelStatus based on TruthValue"""
    defaultValue = 2


_ClGatewayTunnelStatus_Type.__name__ = "TruthValue"
_ClGatewayTunnelStatus_Object = MibTableColumn
clGatewayTunnelStatus = _ClGatewayTunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 1, 1, 5),
    _ClGatewayTunnelStatus_Type()
)
clGatewayTunnelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clGatewayTunnelStatus.setStatus("current")
_ClGatewayTunnelRowStatus_Type = RowStatus
_ClGatewayTunnelRowStatus_Object = MibTableColumn
clGatewayTunnelRowStatus = _ClGatewayTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 1, 1, 6),
    _ClGatewayTunnelRowStatus_Type()
)
clGatewayTunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clGatewayTunnelRowStatus.setStatus("current")


class _ClGatewayTunnelAdminStatus_Type(TruthValue):
    """Custom type clGatewayTunnelAdminStatus based on TruthValue"""
    defaultValue = 2


_ClGatewayTunnelAdminStatus_Type.__name__ = "TruthValue"
_ClGatewayTunnelAdminStatus_Object = MibTableColumn
clGatewayTunnelAdminStatus = _ClGatewayTunnelAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 1, 1, 7),
    _ClGatewayTunnelAdminStatus_Type()
)
clGatewayTunnelAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clGatewayTunnelAdminStatus.setStatus("current")


class _ClGatewayTunnelMtu_Type(Unsigned32):
    """Custom type clGatewayTunnelMtu based on Unsigned32"""
    defaultValue = 1476


_ClGatewayTunnelMtu_Type.__name__ = "Unsigned32"
_ClGatewayTunnelMtu_Object = MibTableColumn
clGatewayTunnelMtu = _ClGatewayTunnelMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 1, 1, 8),
    _ClGatewayTunnelMtu_Type()
)
clGatewayTunnelMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clGatewayTunnelMtu.setStatus("current")


class _ClGatewayTunnelFlapCount_Type(Unsigned32):
    """Custom type clGatewayTunnelFlapCount based on Unsigned32"""
    defaultValue = 0


_ClGatewayTunnelFlapCount_Type.__name__ = "Unsigned32"
_ClGatewayTunnelFlapCount_Object = MibTableColumn
clGatewayTunnelFlapCount = _ClGatewayTunnelFlapCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 1, 1, 9),
    _ClGatewayTunnelFlapCount_Type()
)
clGatewayTunnelFlapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clGatewayTunnelFlapCount.setStatus("current")


class _CLGatewayTunnelSourceInterface_Type(SnmpAdminString):
    """Custom type cLGatewayTunnelSourceInterface based on SnmpAdminString"""
    defaultValue = OctetString("")


_CLGatewayTunnelSourceInterface_Type.__name__ = "SnmpAdminString"
_CLGatewayTunnelSourceInterface_Object = MibTableColumn
cLGatewayTunnelSourceInterface = _CLGatewayTunnelSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 1, 1, 10),
    _CLGatewayTunnelSourceInterface_Type()
)
cLGatewayTunnelSourceInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLGatewayTunnelSourceInterface.setStatus("current")
_ClGatewayDomainTable_Object = MibTable
clGatewayDomainTable = _ClGatewayDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 2)
)
if mibBuilder.loadTexts:
    clGatewayDomainTable.setStatus("current")
_ClGatewayDomainEntry_Object = MibTableRow
clGatewayDomainEntry = _ClGatewayDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 2, 1)
)
clGatewayDomainEntry.setIndexNames(
    (0, "CISCO-LWAPP-TUNNEL-MIB", "clGatewayDomainName"),
    (0, "CISCO-LWAPP-TUNNEL-MIB", "clGatewayDomainTunnelType"),
)
if mibBuilder.loadTexts:
    clGatewayDomainEntry.setStatus("current")


class _ClGatewayDomainName_Type(OctetString):
    """Custom type clGatewayDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_ClGatewayDomainName_Type.__name__ = "OctetString"
_ClGatewayDomainName_Object = MibTableColumn
clGatewayDomainName = _ClGatewayDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 2, 1, 1),
    _ClGatewayDomainName_Type()
)
clGatewayDomainName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clGatewayDomainName.setStatus("current")


class _ClGatewayDomainTunnelType_Type(Integer32):
    """Custom type clGatewayDomainTunnelType based on Integer32"""
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
        *(("none", 1),
          ("pmipv6", 2),
          ("gtpv2", 3),
          ("eogre", 4))
    )


_ClGatewayDomainTunnelType_Type.__name__ = "Integer32"
_ClGatewayDomainTunnelType_Object = MibTableColumn
clGatewayDomainTunnelType = _ClGatewayDomainTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 2, 1, 2),
    _ClGatewayDomainTunnelType_Type()
)
clGatewayDomainTunnelType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clGatewayDomainTunnelType.setStatus("current")
_ClGatewayDomainActiveGateway_Type = OctetString
_ClGatewayDomainActiveGateway_Object = MibTableColumn
clGatewayDomainActiveGateway = _ClGatewayDomainActiveGateway_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 2, 1, 3),
    _ClGatewayDomainActiveGateway_Type()
)
clGatewayDomainActiveGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clGatewayDomainActiveGateway.setStatus("current")


class _ClGatewayDomainPrimaryGateway_Type(OctetString):
    """Custom type clGatewayDomainPrimaryGateway based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ClGatewayDomainPrimaryGateway_Type.__name__ = "OctetString"
_ClGatewayDomainPrimaryGateway_Object = MibTableColumn
clGatewayDomainPrimaryGateway = _ClGatewayDomainPrimaryGateway_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 2, 1, 4),
    _ClGatewayDomainPrimaryGateway_Type()
)
clGatewayDomainPrimaryGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clGatewayDomainPrimaryGateway.setStatus("current")


class _ClGatewayDomainSecondaryGateway_Type(OctetString):
    """Custom type clGatewayDomainSecondaryGateway based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ClGatewayDomainSecondaryGateway_Type.__name__ = "OctetString"
_ClGatewayDomainSecondaryGateway_Object = MibTableColumn
clGatewayDomainSecondaryGateway = _ClGatewayDomainSecondaryGateway_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 2, 1, 5),
    _ClGatewayDomainSecondaryGateway_Type()
)
clGatewayDomainSecondaryGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clGatewayDomainSecondaryGateway.setStatus("current")
_ClGatewayDomainRowStatus_Type = RowStatus
_ClGatewayDomainRowStatus_Object = MibTableColumn
clGatewayDomainRowStatus = _ClGatewayDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 2, 1, 6),
    _ClGatewayDomainRowStatus_Type()
)
clGatewayDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clGatewayDomainRowStatus.setStatus("current")


class _ClGatewayDomainAdminStatus_Type(Integer32):
    """Custom type clGatewayDomainAdminStatus based on Integer32"""
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


_ClGatewayDomainAdminStatus_Type.__name__ = "Integer32"
_ClGatewayDomainAdminStatus_Object = MibTableColumn
clGatewayDomainAdminStatus = _ClGatewayDomainAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 2, 1, 7),
    _ClGatewayDomainAdminStatus_Type()
)
clGatewayDomainAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clGatewayDomainAdminStatus.setStatus("current")


class _ClGatewayDomainRedundancyModel_Type(Integer32):
    """Custom type clGatewayDomainRedundancyModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nonrevertive", 0),
          ("revertive", 1))
    )


_ClGatewayDomainRedundancyModel_Type.__name__ = "Integer32"
_ClGatewayDomainRedundancyModel_Object = MibTableColumn
clGatewayDomainRedundancyModel = _ClGatewayDomainRedundancyModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 2, 1, 8),
    _ClGatewayDomainRedundancyModel_Type()
)
clGatewayDomainRedundancyModel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clGatewayDomainRedundancyModel.setStatus("current")
_ClGatewayDomainGatewayListTable_Object = MibTable
clGatewayDomainGatewayListTable = _ClGatewayDomainGatewayListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 3)
)
if mibBuilder.loadTexts:
    clGatewayDomainGatewayListTable.setStatus("current")
_ClGatewayDomainGatewayListEntry_Object = MibTableRow
clGatewayDomainGatewayListEntry = _ClGatewayDomainGatewayListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 3, 1)
)
clGatewayDomainGatewayListEntry.setIndexNames(
    (0, "CISCO-LWAPP-TUNNEL-MIB", "clGatewayDomainName"),
    (0, "CISCO-LWAPP-TUNNEL-MIB", "clGatewayDomainTunnelType"),
    (0, "CISCO-LWAPP-TUNNEL-MIB", "clGatewayTunnelName"),
)
if mibBuilder.loadTexts:
    clGatewayDomainGatewayListEntry.setStatus("current")
_ClGatewayDomainGatewayListRowStatus_Type = RowStatus
_ClGatewayDomainGatewayListRowStatus_Object = MibTableColumn
clGatewayDomainGatewayListRowStatus = _ClGatewayDomainGatewayListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 3, 1, 1),
    _ClGatewayDomainGatewayListRowStatus_Type()
)
clGatewayDomainGatewayListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clGatewayDomainGatewayListRowStatus.setStatus("current")
_ClGatewayProfileTable_Object = MibTable
clGatewayProfileTable = _ClGatewayProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 4)
)
if mibBuilder.loadTexts:
    clGatewayProfileTable.setStatus("current")
_ClGatewayProfileEntry_Object = MibTableRow
clGatewayProfileEntry = _ClGatewayProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 4, 1)
)
clGatewayProfileEntry.setIndexNames(
    (0, "CISCO-LWAPP-TUNNEL-MIB", "clGatewayProfileName"),
)
if mibBuilder.loadTexts:
    clGatewayProfileEntry.setStatus("current")


class _ClGatewayProfileName_Type(OctetString):
    """Custom type clGatewayProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_ClGatewayProfileName_Type.__name__ = "OctetString"
_ClGatewayProfileName_Object = MibTableColumn
clGatewayProfileName = _ClGatewayProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 4, 1, 1),
    _ClGatewayProfileName_Type()
)
clGatewayProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clGatewayProfileName.setStatus("current")


class _ClGatewayProfileDhcpOpt82Status_Type(TruthValue):
    """Custom type clGatewayProfileDhcpOpt82Status based on TruthValue"""
    defaultValue = 2


_ClGatewayProfileDhcpOpt82Status_Type.__name__ = "TruthValue"
_ClGatewayProfileDhcpOpt82Status_Object = MibTableColumn
clGatewayProfileDhcpOpt82Status = _ClGatewayProfileDhcpOpt82Status_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 4, 1, 2),
    _ClGatewayProfileDhcpOpt82Status_Type()
)
clGatewayProfileDhcpOpt82Status.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clGatewayProfileDhcpOpt82Status.setStatus("current")
_ClGatewayProfileDhcpOpt82Format_Type = Unsigned32
_ClGatewayProfileDhcpOpt82Format_Object = MibTableColumn
clGatewayProfileDhcpOpt82Format = _ClGatewayProfileDhcpOpt82Format_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 4, 1, 3),
    _ClGatewayProfileDhcpOpt82Format_Type()
)
clGatewayProfileDhcpOpt82Format.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clGatewayProfileDhcpOpt82Format.setStatus("current")
_ClGatewayProfileDhcpOpt82Delimiter_Type = OctetString
_ClGatewayProfileDhcpOpt82Delimiter_Object = MibTableColumn
clGatewayProfileDhcpOpt82Delimiter = _ClGatewayProfileDhcpOpt82Delimiter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 4, 1, 4),
    _ClGatewayProfileDhcpOpt82Delimiter_Type()
)
clGatewayProfileDhcpOpt82Delimiter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clGatewayProfileDhcpOpt82Delimiter.setStatus("current")
_ClGatewayProfileCircuitId_Type = OctetString
_ClGatewayProfileCircuitId_Object = MibTableColumn
clGatewayProfileCircuitId = _ClGatewayProfileCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 4, 1, 5),
    _ClGatewayProfileCircuitId_Type()
)
clGatewayProfileCircuitId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clGatewayProfileCircuitId.setStatus("current")
_ClGatewayProfileRemoteId_Type = OctetString
_ClGatewayProfileRemoteId_Object = MibTableColumn
clGatewayProfileRemoteId = _ClGatewayProfileRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 4, 1, 6),
    _ClGatewayProfileRemoteId_Type()
)
clGatewayProfileRemoteId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clGatewayProfileRemoteId.setStatus("current")


class _ClGatewayProfileRadiusProxyStatus_Type(TruthValue):
    """Custom type clGatewayProfileRadiusProxyStatus based on TruthValue"""
    defaultValue = 2


_ClGatewayProfileRadiusProxyStatus_Type.__name__ = "TruthValue"
_ClGatewayProfileRadiusProxyStatus_Object = MibTableColumn
clGatewayProfileRadiusProxyStatus = _ClGatewayProfileRadiusProxyStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 4, 1, 7),
    _ClGatewayProfileRadiusProxyStatus_Type()
)
clGatewayProfileRadiusProxyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clGatewayProfileRadiusProxyStatus.setStatus("current")


class _ClGatewayProfileRadiusProxyAccounting_Type(TruthValue):
    """Custom type clGatewayProfileRadiusProxyAccounting based on TruthValue"""
    defaultValue = 2


_ClGatewayProfileRadiusProxyAccounting_Type.__name__ = "TruthValue"
_ClGatewayProfileRadiusProxyAccounting_Object = MibTableColumn
clGatewayProfileRadiusProxyAccounting = _ClGatewayProfileRadiusProxyAccounting_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 4, 1, 8),
    _ClGatewayProfileRadiusProxyAccounting_Type()
)
clGatewayProfileRadiusProxyAccounting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clGatewayProfileRadiusProxyAccounting.setStatus("current")
_ClGatewayProfileRowStatus_Type = RowStatus
_ClGatewayProfileRowStatus_Object = MibTableColumn
clGatewayProfileRowStatus = _ClGatewayProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 4, 1, 9),
    _ClGatewayProfileRowStatus_Type()
)
clGatewayProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clGatewayProfileRowStatus.setStatus("current")


class _ClGatewayProfileAdminStatus_Type(Integer32):
    """Custom type clGatewayProfileAdminStatus based on Integer32"""
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


_ClGatewayProfileAdminStatus_Type.__name__ = "Integer32"
_ClGatewayProfileAdminStatus_Object = MibTableColumn
clGatewayProfileAdminStatus = _ClGatewayProfileAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 4, 1, 10),
    _ClGatewayProfileAdminStatus_Type()
)
clGatewayProfileAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clGatewayProfileAdminStatus.setStatus("current")


class _ClGatewayProfileAAAOverride_Type(TruthValue):
    """Custom type clGatewayProfileAAAOverride based on TruthValue"""
    defaultValue = 2


_ClGatewayProfileAAAOverride_Type.__name__ = "TruthValue"
_ClGatewayProfileAAAOverride_Object = MibTableColumn
clGatewayProfileAAAOverride = _ClGatewayProfileAAAOverride_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 4, 1, 11),
    _ClGatewayProfileAAAOverride_Type()
)
clGatewayProfileAAAOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clGatewayProfileAAAOverride.setStatus("current")
_ClGatewayRuleTable_Object = MibTable
clGatewayRuleTable = _ClGatewayRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 5)
)
if mibBuilder.loadTexts:
    clGatewayRuleTable.setStatus("current")
_ClGatewayRuleEntry_Object = MibTableRow
clGatewayRuleEntry = _ClGatewayRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 5, 1)
)
clGatewayRuleEntry.setIndexNames(
    (0, "CISCO-LWAPP-TUNNEL-MIB", "clGatewayProfileName"),
    (0, "CISCO-LWAPP-TUNNEL-MIB", "clGatewayRuleName"),
)
if mibBuilder.loadTexts:
    clGatewayRuleEntry.setStatus("current")


class _ClGatewayRuleName_Type(OctetString):
    """Custom type clGatewayRuleName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_ClGatewayRuleName_Type.__name__ = "OctetString"
_ClGatewayRuleName_Object = MibTableColumn
clGatewayRuleName = _ClGatewayRuleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 5, 1, 1),
    _ClGatewayRuleName_Type()
)
clGatewayRuleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clGatewayRuleName.setStatus("current")


class _ClGatewayRuleTunnelType_Type(Integer32):
    """Custom type clGatewayRuleTunnelType based on Integer32"""
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
        *(("none", 1),
          ("pmipv6", 2),
          ("gtpv2", 3),
          ("eogre", 4))
    )


_ClGatewayRuleTunnelType_Type.__name__ = "Integer32"
_ClGatewayRuleTunnelType_Object = MibTableColumn
clGatewayRuleTunnelType = _ClGatewayRuleTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 5, 1, 2),
    _ClGatewayRuleTunnelType_Type()
)
clGatewayRuleTunnelType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clGatewayRuleTunnelType.setStatus("current")
_ClGatewayRuleVlanId_Type = Unsigned32
_ClGatewayRuleVlanId_Object = MibTableColumn
clGatewayRuleVlanId = _ClGatewayRuleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 5, 1, 3),
    _ClGatewayRuleVlanId_Type()
)
clGatewayRuleVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clGatewayRuleVlanId.setStatus("current")
_ClGatewayRuleDomainName_Type = OctetString
_ClGatewayRuleDomainName_Object = MibTableColumn
clGatewayRuleDomainName = _ClGatewayRuleDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 5, 1, 4),
    _ClGatewayRuleDomainName_Type()
)
clGatewayRuleDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clGatewayRuleDomainName.setStatus("current")
_ClGatewayRuleRowStatus_Type = RowStatus
_ClGatewayRuleRowStatus_Object = MibTableColumn
clGatewayRuleRowStatus = _ClGatewayRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 5, 1, 5),
    _ClGatewayRuleRowStatus_Type()
)
clGatewayRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clGatewayRuleRowStatus.setStatus("current")
_ClGatewayRuleRealm_Type = SnmpAdminString
_ClGatewayRuleRealm_Object = MibTableColumn
clGatewayRuleRealm = _ClGatewayRuleRealm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 5, 1, 6),
    _ClGatewayRuleRealm_Type()
)
clGatewayRuleRealm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clGatewayRuleRealm.setStatus("current")
_ClApGatewayTunnelTable_Object = MibTable
clApGatewayTunnelTable = _ClApGatewayTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 6)
)
if mibBuilder.loadTexts:
    clApGatewayTunnelTable.setStatus("current")
_ClApGatewayTunnelEntry_Object = MibTableRow
clApGatewayTunnelEntry = _ClApGatewayTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 6, 1)
)
clApGatewayTunnelEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApIfMacAddress"),
    (0, "CISCO-LWAPP-TUNNEL-MIB", "clGatewayTunnelName"),
)
if mibBuilder.loadTexts:
    clApGatewayTunnelEntry.setStatus("current")


class _ClApGatewayTunnelStatus_Type(TruthValue):
    """Custom type clApGatewayTunnelStatus based on TruthValue"""
    defaultValue = 2


_ClApGatewayTunnelStatus_Type.__name__ = "TruthValue"
_ClApGatewayTunnelStatus_Object = MibTableColumn
clApGatewayTunnelStatus = _ClApGatewayTunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 6, 1, 1),
    _ClApGatewayTunnelStatus_Type()
)
clApGatewayTunnelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clApGatewayTunnelStatus.setStatus("current")


class _ClApGatewayTunnelClientCount_Type(Unsigned32):
    """Custom type clApGatewayTunnelClientCount based on Unsigned32"""
    defaultValue = 0


_ClApGatewayTunnelClientCount_Type.__name__ = "Unsigned32"
_ClApGatewayTunnelClientCount_Object = MibTableColumn
clApGatewayTunnelClientCount = _ClApGatewayTunnelClientCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 6, 1, 2),
    _ClApGatewayTunnelClientCount_Type()
)
clApGatewayTunnelClientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clApGatewayTunnelClientCount.setStatus("current")


class _ClApGatewayTunnelMtu_Type(Unsigned32):
    """Custom type clApGatewayTunnelMtu based on Unsigned32"""
    defaultValue = 1476


_ClApGatewayTunnelMtu_Type.__name__ = "Unsigned32"
_ClApGatewayTunnelMtu_Object = MibTableColumn
clApGatewayTunnelMtu = _ClApGatewayTunnelMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 6, 1, 3),
    _ClApGatewayTunnelMtu_Type()
)
clApGatewayTunnelMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clApGatewayTunnelMtu.setStatus("current")


class _ClApGatewayTunnelFlapCount_Type(Unsigned32):
    """Custom type clApGatewayTunnelFlapCount based on Unsigned32"""
    defaultValue = 0


_ClApGatewayTunnelFlapCount_Type.__name__ = "Unsigned32"
_ClApGatewayTunnelFlapCount_Object = MibTableColumn
clApGatewayTunnelFlapCount = _ClApGatewayTunnelFlapCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 6, 1, 4),
    _ClApGatewayTunnelFlapCount_Type()
)
clApGatewayTunnelFlapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clApGatewayTunnelFlapCount.setStatus("current")
_ClApGatewayDomainTable_Object = MibTable
clApGatewayDomainTable = _ClApGatewayDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 7)
)
if mibBuilder.loadTexts:
    clApGatewayDomainTable.setStatus("current")
_ClApGatewayDomainEntry_Object = MibTableRow
clApGatewayDomainEntry = _ClApGatewayDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 7, 1)
)
clApGatewayDomainEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApIfMacAddress"),
    (0, "CISCO-LWAPP-TUNNEL-MIB", "clGatewayDomainName"),
)
if mibBuilder.loadTexts:
    clApGatewayDomainEntry.setStatus("current")
_ClApGatewayDomainActiveGateway_Type = OctetString
_ClApGatewayDomainActiveGateway_Object = MibTableColumn
clApGatewayDomainActiveGateway = _ClApGatewayDomainActiveGateway_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 7, 1, 1),
    _ClApGatewayDomainActiveGateway_Type()
)
clApGatewayDomainActiveGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clApGatewayDomainActiveGateway.setStatus("current")
_ClGatewayTunnelStatsTable_Object = MibTable
clGatewayTunnelStatsTable = _ClGatewayTunnelStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 8)
)
if mibBuilder.loadTexts:
    clGatewayTunnelStatsTable.setStatus("current")
_ClGatewayTunnelStatsEntry_Object = MibTableRow
clGatewayTunnelStatsEntry = _ClGatewayTunnelStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 8, 1)
)
clGatewayTunnelStatsEntry.setIndexNames(
    (0, "CISCO-LWAPP-TUNNEL-MIB", "clGatewayTunnelName"),
    (0, "CISCO-LWAPP-TUNNEL-MIB", "clGatewayTunnelType"),
)
if mibBuilder.loadTexts:
    clGatewayTunnelStatsEntry.setStatus("current")
_ClGatewayTunnelStatsClientCount_Type = Unsigned32
_ClGatewayTunnelStatsClientCount_Object = MibTableColumn
clGatewayTunnelStatsClientCount = _ClGatewayTunnelStatsClientCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 8, 1, 1),
    _ClGatewayTunnelStatsClientCount_Type()
)
clGatewayTunnelStatsClientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clGatewayTunnelStatsClientCount.setStatus("current")
_ClGatewayTunnelStatsTunnelUpTime_Type = Unsigned32
_ClGatewayTunnelStatsTunnelUpTime_Object = MibTableColumn
clGatewayTunnelStatsTunnelUpTime = _ClGatewayTunnelStatsTunnelUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 8, 1, 2),
    _ClGatewayTunnelStatsTunnelUpTime_Type()
)
clGatewayTunnelStatsTunnelUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clGatewayTunnelStatsTunnelUpTime.setStatus("current")
_ClGatewayTunnelStatsKeepaliveLoss_Type = Unsigned32
_ClGatewayTunnelStatsKeepaliveLoss_Object = MibTableColumn
clGatewayTunnelStatsKeepaliveLoss = _ClGatewayTunnelStatsKeepaliveLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 8, 1, 3),
    _ClGatewayTunnelStatsKeepaliveLoss_Type()
)
clGatewayTunnelStatsKeepaliveLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clGatewayTunnelStatsKeepaliveLoss.setStatus("current")
_ClGatewayTunnelStatsTunnelRxBytes_Type = Unsigned64
_ClGatewayTunnelStatsTunnelRxBytes_Object = MibTableColumn
clGatewayTunnelStatsTunnelRxBytes = _ClGatewayTunnelStatsTunnelRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 8, 1, 4),
    _ClGatewayTunnelStatsTunnelRxBytes_Type()
)
clGatewayTunnelStatsTunnelRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clGatewayTunnelStatsTunnelRxBytes.setStatus("current")
_ClGatewayTunnelStatsTunnelTxBytes_Type = Unsigned64
_ClGatewayTunnelStatsTunnelTxBytes_Object = MibTableColumn
clGatewayTunnelStatsTunnelTxBytes = _ClGatewayTunnelStatsTunnelTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 8, 1, 5),
    _ClGatewayTunnelStatsTunnelTxBytes_Type()
)
clGatewayTunnelStatsTunnelTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clGatewayTunnelStatsTunnelTxBytes.setStatus("current")
_ClGatewayTunnelStatsTunnelRxPkts_Type = Unsigned64
_ClGatewayTunnelStatsTunnelRxPkts_Object = MibTableColumn
clGatewayTunnelStatsTunnelRxPkts = _ClGatewayTunnelStatsTunnelRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 8, 1, 6),
    _ClGatewayTunnelStatsTunnelRxPkts_Type()
)
clGatewayTunnelStatsTunnelRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clGatewayTunnelStatsTunnelRxPkts.setStatus("current")
_ClGatewayTunnelStatsTunnelTxPkts_Type = Unsigned64
_ClGatewayTunnelStatsTunnelTxPkts_Object = MibTableColumn
clGatewayTunnelStatsTunnelTxPkts = _ClGatewayTunnelStatsTunnelTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 8, 1, 7),
    _ClGatewayTunnelStatsTunnelTxPkts_Type()
)
clGatewayTunnelStatsTunnelTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clGatewayTunnelStatsTunnelTxPkts.setStatus("current")
_ClApGatewayTunnelStatsTable_Object = MibTable
clApGatewayTunnelStatsTable = _ClApGatewayTunnelStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 9)
)
if mibBuilder.loadTexts:
    clApGatewayTunnelStatsTable.setStatus("current")
_ClApGatewayTunnelStatsEntry_Object = MibTableRow
clApGatewayTunnelStatsEntry = _ClApGatewayTunnelStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 9, 1)
)
clApGatewayTunnelStatsEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApIfMacAddress"),
    (0, "CISCO-LWAPP-TUNNEL-MIB", "clGatewayTunnelName"),
)
if mibBuilder.loadTexts:
    clApGatewayTunnelStatsEntry.setStatus("current")
_ClApGatewayTunnelStatsTunnelUpTime_Type = Unsigned32
_ClApGatewayTunnelStatsTunnelUpTime_Object = MibTableColumn
clApGatewayTunnelStatsTunnelUpTime = _ClApGatewayTunnelStatsTunnelUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 9, 1, 1),
    _ClApGatewayTunnelStatsTunnelUpTime_Type()
)
clApGatewayTunnelStatsTunnelUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clApGatewayTunnelStatsTunnelUpTime.setStatus("current")
_ClApGatewayTunnelStatsKeepaliveLoss_Type = Unsigned32
_ClApGatewayTunnelStatsKeepaliveLoss_Object = MibTableColumn
clApGatewayTunnelStatsKeepaliveLoss = _ClApGatewayTunnelStatsKeepaliveLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 9, 1, 2),
    _ClApGatewayTunnelStatsKeepaliveLoss_Type()
)
clApGatewayTunnelStatsKeepaliveLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clApGatewayTunnelStatsKeepaliveLoss.setStatus("current")
_ClApGatewayTunnelStatsTunnelRxBytes_Type = Unsigned32
_ClApGatewayTunnelStatsTunnelRxBytes_Object = MibTableColumn
clApGatewayTunnelStatsTunnelRxBytes = _ClApGatewayTunnelStatsTunnelRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 9, 1, 3),
    _ClApGatewayTunnelStatsTunnelRxBytes_Type()
)
clApGatewayTunnelStatsTunnelRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clApGatewayTunnelStatsTunnelRxBytes.setStatus("deprecated")
_ClApGatewayTunnelStatsTunnelTxBytes_Type = Unsigned32
_ClApGatewayTunnelStatsTunnelTxBytes_Object = MibTableColumn
clApGatewayTunnelStatsTunnelTxBytes = _ClApGatewayTunnelStatsTunnelTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 9, 1, 4),
    _ClApGatewayTunnelStatsTunnelTxBytes_Type()
)
clApGatewayTunnelStatsTunnelTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clApGatewayTunnelStatsTunnelTxBytes.setStatus("deprecated")
_ClApGatewayTunnelStatsTunnelRxPkts_Type = Unsigned32
_ClApGatewayTunnelStatsTunnelRxPkts_Object = MibTableColumn
clApGatewayTunnelStatsTunnelRxPkts = _ClApGatewayTunnelStatsTunnelRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 9, 1, 5),
    _ClApGatewayTunnelStatsTunnelRxPkts_Type()
)
clApGatewayTunnelStatsTunnelRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clApGatewayTunnelStatsTunnelRxPkts.setStatus("deprecated")
_ClApGatewayTunnelStatsTunnelTxPkts_Type = Unsigned32
_ClApGatewayTunnelStatsTunnelTxPkts_Object = MibTableColumn
clApGatewayTunnelStatsTunnelTxPkts = _ClApGatewayTunnelStatsTunnelTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 9, 1, 6),
    _ClApGatewayTunnelStatsTunnelTxPkts_Type()
)
clApGatewayTunnelStatsTunnelTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clApGatewayTunnelStatsTunnelTxPkts.setStatus("deprecated")
_ClApGatewayTunnelStatsTunnelRxBytes64_Type = Unsigned64
_ClApGatewayTunnelStatsTunnelRxBytes64_Object = MibTableColumn
clApGatewayTunnelStatsTunnelRxBytes64 = _ClApGatewayTunnelStatsTunnelRxBytes64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 9, 1, 7),
    _ClApGatewayTunnelStatsTunnelRxBytes64_Type()
)
clApGatewayTunnelStatsTunnelRxBytes64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clApGatewayTunnelStatsTunnelRxBytes64.setStatus("current")
_ClApGatewayTunnelStatsTunnelTxBytes64_Type = Unsigned64
_ClApGatewayTunnelStatsTunnelTxBytes64_Object = MibTableColumn
clApGatewayTunnelStatsTunnelTxBytes64 = _ClApGatewayTunnelStatsTunnelTxBytes64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 9, 1, 8),
    _ClApGatewayTunnelStatsTunnelTxBytes64_Type()
)
clApGatewayTunnelStatsTunnelTxBytes64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clApGatewayTunnelStatsTunnelTxBytes64.setStatus("current")
_ClApGatewayTunnelStatsTunnelRxPkts64_Type = Unsigned64
_ClApGatewayTunnelStatsTunnelRxPkts64_Object = MibTableColumn
clApGatewayTunnelStatsTunnelRxPkts64 = _ClApGatewayTunnelStatsTunnelRxPkts64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 9, 1, 9),
    _ClApGatewayTunnelStatsTunnelRxPkts64_Type()
)
clApGatewayTunnelStatsTunnelRxPkts64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clApGatewayTunnelStatsTunnelRxPkts64.setStatus("current")
_ClApGatewayTunnelStatsTunnelTxPkts64_Type = Unsigned64
_ClApGatewayTunnelStatsTunnelTxPkts64_Object = MibTableColumn
clApGatewayTunnelStatsTunnelTxPkts64 = _ClApGatewayTunnelStatsTunnelTxPkts64_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 3, 9, 1, 10),
    _ClApGatewayTunnelStatsTunnelTxPkts64_Type()
)
clApGatewayTunnelStatsTunnelTxPkts64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clApGatewayTunnelStatsTunnelTxPkts64.setStatus("current")
_ClGatewayGlobalInterface_ObjectIdentity = ObjectIdentity
clGatewayGlobalInterface = _ClGatewayGlobalInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 4)
)


class _CLGatewayInterface_Type(OctetString):
    """Custom type cLGatewayInterface based on OctetString"""
    defaultValue = OctetString("management")


_CLGatewayInterface_Type.__name__ = "OctetString"
_CLGatewayInterface_Object = MibScalar
cLGatewayInterface = _CLGatewayInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 4, 1),
    _CLGatewayInterface_Type()
)
cLGatewayInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLGatewayInterface.setStatus("current")
_ClGatewayGlobalHeartbeatInterval_ObjectIdentity = ObjectIdentity
clGatewayGlobalHeartbeatInterval = _ClGatewayGlobalHeartbeatInterval_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 5)
)


class _CLGatewayHeartbeatInterval_Type(Unsigned32):
    """Custom type cLGatewayHeartbeatInterval based on Unsigned32"""
    defaultValue = 60


_CLGatewayHeartbeatInterval_Type.__name__ = "Unsigned32"
_CLGatewayHeartbeatInterval_Object = MibScalar
cLGatewayHeartbeatInterval = _CLGatewayHeartbeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 5, 1),
    _CLGatewayHeartbeatInterval_Type()
)
cLGatewayHeartbeatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLGatewayHeartbeatInterval.setStatus("current")
_ClGatewayGlobalHeartbeatMaxSkipCount_ObjectIdentity = ObjectIdentity
clGatewayGlobalHeartbeatMaxSkipCount = _ClGatewayGlobalHeartbeatMaxSkipCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 6)
)


class _CLGatewayHeartbeatMaxSkipCount_Type(Unsigned32):
    """Custom type cLGatewayHeartbeatMaxSkipCount based on Unsigned32"""
    defaultValue = 3


_CLGatewayHeartbeatMaxSkipCount_Type.__name__ = "Unsigned32"
_CLGatewayHeartbeatMaxSkipCount_Object = MibScalar
cLGatewayHeartbeatMaxSkipCount = _CLGatewayHeartbeatMaxSkipCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 6, 1),
    _CLGatewayHeartbeatMaxSkipCount_Type()
)
cLGatewayHeartbeatMaxSkipCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLGatewayHeartbeatMaxSkipCount.setStatus("current")
_ClGatewayWlanConfig_ObjectIdentity = ObjectIdentity
clGatewayWlanConfig = _ClGatewayWlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 7)
)
_CLGatewayWlanConfigTable_Object = MibTable
cLGatewayWlanConfigTable = _CLGatewayWlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 7, 1)
)
if mibBuilder.loadTexts:
    cLGatewayWlanConfigTable.setStatus("current")
_CLGatewayWlanConfigEntry_Object = MibTableRow
cLGatewayWlanConfigEntry = _CLGatewayWlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 7, 1, 1)
)
cLGatewayWlanConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLGatewayWlanConfigEntry.setStatus("current")


class _CLGatewayWlanVlanOverrideEnable_Type(TruthValue):
    """Custom type cLGatewayWlanVlanOverrideEnable based on TruthValue"""
    defaultValue = 2


_CLGatewayWlanVlanOverrideEnable_Type.__name__ = "TruthValue"
_CLGatewayWlanVlanOverrideEnable_Object = MibTableColumn
cLGatewayWlanVlanOverrideEnable = _CLGatewayWlanVlanOverrideEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 7, 1, 1, 1),
    _CLGatewayWlanVlanOverrideEnable_Type()
)
cLGatewayWlanVlanOverrideEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLGatewayWlanVlanOverrideEnable.setStatus("current")


class _CLGatewayWlanVlanId_Type(Unsigned32):
    """Custom type cLGatewayWlanVlanId based on Unsigned32"""
    defaultValue = 0


_CLGatewayWlanVlanId_Type.__name__ = "Unsigned32"
_CLGatewayWlanVlanId_Object = MibTableColumn
cLGatewayWlanVlanId = _CLGatewayWlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 7, 1, 1, 2),
    _CLGatewayWlanVlanId_Type()
)
cLGatewayWlanVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLGatewayWlanVlanId.setStatus("current")
_ClGatewayWlanProfileConfig_ObjectIdentity = ObjectIdentity
clGatewayWlanProfileConfig = _ClGatewayWlanProfileConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 8)
)
_CLGatewayWlanProfileConfigTable_Object = MibTable
cLGatewayWlanProfileConfigTable = _CLGatewayWlanProfileConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 8, 1)
)
if mibBuilder.loadTexts:
    cLGatewayWlanProfileConfigTable.setStatus("current")
_CLGatewayWlanProfileConfigEntry_Object = MibTableRow
cLGatewayWlanProfileConfigEntry = _CLGatewayWlanProfileConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 8, 1, 1)
)
cLGatewayWlanProfileConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-POLICY-MIB", "cLWlanWlanPolicyName"),
)
if mibBuilder.loadTexts:
    cLGatewayWlanProfileConfigEntry.setStatus("current")
_CLGatewayWlanProfileTunnelProfile_Type = OctetString
_CLGatewayWlanProfileTunnelProfile_Object = MibTableColumn
cLGatewayWlanProfileTunnelProfile = _CLGatewayWlanProfileTunnelProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 8, 1, 1, 1),
    _CLGatewayWlanProfileTunnelProfile_Type()
)
cLGatewayWlanProfileTunnelProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLGatewayWlanProfileTunnelProfile.setStatus("current")
_ClGatewayAAAProxyConfig_ObjectIdentity = ObjectIdentity
clGatewayAAAProxyConfig = _ClGatewayAAAProxyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 9)
)
_CLGatewayAAAProxyConfigTable_Object = MibTable
cLGatewayAAAProxyConfigTable = _CLGatewayAAAProxyConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 9, 1)
)
if mibBuilder.loadTexts:
    cLGatewayAAAProxyConfigTable.setStatus("current")
_CLGatewayAAAProxyConfigEntry_Object = MibTableRow
cLGatewayAAAProxyConfigEntry = _CLGatewayAAAProxyConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 9, 1, 1)
)
cLGatewayAAAProxyConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-TUNNEL-MIB", "clGatewayTunnelName"),
)
if mibBuilder.loadTexts:
    cLGatewayAAAProxyConfigEntry.setStatus("current")
_CLGatewayAAAProxyKey_Type = SnmpAdminString
_CLGatewayAAAProxyKey_Object = MibTableColumn
cLGatewayAAAProxyKey = _CLGatewayAAAProxyKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 9, 1, 1, 1),
    _CLGatewayAAAProxyKey_Type()
)
cLGatewayAAAProxyKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLGatewayAAAProxyKey.setStatus("current")
_CLGatewayAAAProxyRowStatus_Type = RowStatus
_CLGatewayAAAProxyRowStatus_Object = MibTableColumn
cLGatewayAAAProxyRowStatus = _CLGatewayAAAProxyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 9, 1, 1, 2),
    _CLGatewayAAAProxyRowStatus_Type()
)
cLGatewayAAAProxyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLGatewayAAAProxyRowStatus.setStatus("current")


class _CLGatewayAAAProxyKeyType_Type(Integer32):
    """Custom type cLGatewayAAAProxyKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("aes", 2))
    )


_CLGatewayAAAProxyKeyType_Type.__name__ = "Integer32"
_CLGatewayAAAProxyKeyType_Object = MibTableColumn
cLGatewayAAAProxyKeyType = _CLGatewayAAAProxyKeyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 9, 1, 1, 3),
    _CLGatewayAAAProxyKeyType_Type()
)
cLGatewayAAAProxyKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLGatewayAAAProxyKeyType.setStatus("current")


class _CLGatewayAAAProxyPort_Type(Unsigned32):
    """Custom type cLGatewayAAAProxyPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CLGatewayAAAProxyPort_Type.__name__ = "Unsigned32"
_CLGatewayAAAProxyPort_Object = MibTableColumn
cLGatewayAAAProxyPort = _CLGatewayAAAProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 9, 1, 1, 4),
    _CLGatewayAAAProxyPort_Type()
)
cLGatewayAAAProxyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLGatewayAAAProxyPort.setStatus("current")

# Managed Objects groups

cLTunnelConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 2, 2, 1)
)
cLTunnelConfigGroup.setObjects(
      *(("CISCO-LWAPP-TUNNEL-MIB", "clGatewayTunnelAddressType"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayTunnelAddress"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayTunnelStatus"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayTunnelRowStatus"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayDomainActiveGateway"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayDomainRowStatus"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayDomainGatewayListRowStatus"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayProfileDhcpOpt82Status"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayProfileDhcpOpt82Format"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayProfileDhcpOpt82Delimiter"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayProfileCircuitId"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayProfileRemoteId"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayProfileRadiusProxyStatus"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayProfileRadiusProxyAccounting"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayProfileRowStatus"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayRuleTunnelType"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayRuleVlanId"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayRuleDomainName"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayRuleRowStatus"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clApGatewayTunnelStatus"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clApGatewayTunnelClientCount"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clApGatewayDomainActiveGateway"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLGatewayInterface"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLGatewayHeartbeatInterval"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLGatewayHeartbeatMaxSkipCount"))
)
if mibBuilder.loadTexts:
    cLTunnelConfigGroup.setStatus("current")

cLTunnelNotificationObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 2, 2, 2)
)
cLTunnelNotificationObjectsGroup.setObjects(
      *(("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelStatusChangeReasonCode"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelGwName"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelGwIPType"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelGwIP"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelType"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelDomainName"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelActiveGwIPType"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelActiveGwIP"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelActiveGwName"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelProfileName"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelClientMacAddress"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelRealm"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelVlanId"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelClientTypeChangeReasonCode"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayTunnelStatsClientCount"))
)
if mibBuilder.loadTexts:
    cLTunnelNotificationObjectsGroup.setStatus("current")

cLTunnelConfigGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 2, 2, 4)
)
cLTunnelConfigGroupRev1.setObjects(
      *(("CISCO-LWAPP-TUNNEL-MIB", "clGatewayTunnelAdminStatus"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayTunnelMtu"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayTunnelFlapCount"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clApGatewayTunnelMtu"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clApGatewayTunnelFlapCount"))
)
if mibBuilder.loadTexts:
    cLTunnelConfigGroupRev1.setStatus("current")

clGatewayWlanConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 2, 2, 5)
)
clGatewayWlanConfigGroup.setObjects(
      *(("CISCO-LWAPP-TUNNEL-MIB", "cLGatewayWlanVlanOverrideEnable"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLGatewayWlanVlanId"))
)
if mibBuilder.loadTexts:
    clGatewayWlanConfigGroup.setStatus("current")

cLTunnelConfigGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 2, 2, 6)
)
cLTunnelConfigGroupRev2.setObjects(
      *(("CISCO-LWAPP-TUNNEL-MIB", "clGatewayTunnelAddressType"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayTunnelAddress"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayTunnelStatus"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayTunnelRowStatus"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayDomainActiveGateway"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayDomainPrimaryGateway"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayDomainSecondaryGateway"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayDomainRowStatus"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayProfileDhcpOpt82Status"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayProfileDhcpOpt82Format"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayProfileDhcpOpt82Delimiter"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayProfileCircuitId"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayProfileRemoteId"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayProfileRadiusProxyStatus"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayProfileRadiusProxyAccounting"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayProfileRowStatus"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayRuleTunnelType"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayRuleVlanId"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayRuleDomainName"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayRuleRowStatus"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clApGatewayTunnelStatus"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clApGatewayTunnelClientCount"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clApGatewayDomainActiveGateway"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLGatewayInterface"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLGatewayHeartbeatInterval"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLGatewayHeartbeatMaxSkipCount"))
)
if mibBuilder.loadTexts:
    cLTunnelConfigGroupRev2.setStatus("current")

clGatewayWlanProfileConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 2, 2, 7)
)
clGatewayWlanProfileConfigGroup.setObjects(
    ("CISCO-LWAPP-TUNNEL-MIB", "cLGatewayWlanProfileTunnelProfile")
)
if mibBuilder.loadTexts:
    clGatewayWlanProfileConfigGroup.setStatus("current")

clApGatewayTunnelStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 2, 2, 8)
)
clApGatewayTunnelStatsGroup.setObjects(
      *(("CISCO-LWAPP-TUNNEL-MIB", "clApGatewayTunnelStatsTunnelRxBytes64"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clApGatewayTunnelStatsTunnelTxBytes64"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clApGatewayTunnelStatsTunnelRxPkts64"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clApGatewayTunnelStatsTunnelTxPkts64"))
)
if mibBuilder.loadTexts:
    clApGatewayTunnelStatsGroup.setStatus("current")

cLGatewayAAAProxyConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 2, 2, 9)
)
cLGatewayAAAProxyConfigGroup.setObjects(
      *(("CISCO-LWAPP-TUNNEL-MIB", "cLGatewayAAAProxyKey"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLGatewayAAAProxyKeyType"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLGatewayAAAProxyRowStatus"))
)
if mibBuilder.loadTexts:
    cLGatewayAAAProxyConfigGroup.setStatus("current")

cLTunnelConfigGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 2, 2, 10)
)
cLTunnelConfigGroupRev3.setObjects(
      *(("CISCO-LWAPP-TUNNEL-MIB", "clGatewayTunnelAddressType"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayTunnelAddress"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayTunnelStatus"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayTunnelAdminStatus"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLGatewayTunnelSourceInterface"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayTunnelRowStatus"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayDomainActiveGateway"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayDomainPrimaryGateway"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayDomainSecondaryGateway"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayDomainAdminStatus"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayDomainRedundancyModel"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayDomainRowStatus"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayProfileDhcpOpt82Status"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayProfileDhcpOpt82Format"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayProfileDhcpOpt82Delimiter"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayProfileCircuitId"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayProfileRemoteId"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayProfileRadiusProxyStatus"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayProfileRadiusProxyAccounting"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayProfileRowStatus"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayProfileAdminStatus"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayProfileAAAOverride"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayRuleTunnelType"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayRuleVlanId"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayRuleDomainName"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayRuleRowStatus"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clApGatewayTunnelStatus"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clApGatewayTunnelClientCount"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clApGatewayDomainActiveGateway"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLGatewayInterface"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLGatewayHeartbeatInterval"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLGatewayHeartbeatMaxSkipCount"))
)
if mibBuilder.loadTexts:
    cLTunnelConfigGroupRev3.setStatus("current")


# Notification objects

cLWATunnelStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 0, 1)
)
cLWATunnelStatusChange.setObjects(
      *(("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelGwName"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelGwIPType"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelGwIP"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelType"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelStatusChangeReasonCode"))
)
if mibBuilder.loadTexts:
    cLWATunnelStatusChange.setStatus(
        "current"
    )

cLWATunnelDomainStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 0, 2)
)
cLWATunnelDomainStatusChange.setObjects(
      *(("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelDomainName"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelType"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelActiveGwIPType"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelActiveGwIP"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelActiveGwName"))
)
if mibBuilder.loadTexts:
    cLWATunnelDomainStatusChange.setStatus(
        "current"
    )

cLWATunnelClientTypeChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 0, 3)
)
cLWATunnelClientTypeChange.setObjects(
      *(("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelClientMacAddress"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelProfileName"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelRealm"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelVlanId"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelDomainName"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelType"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelActiveGwIPType"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelActiveGwIP"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelActiveGwName"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelClientTypeChangeReasonCode"))
)
if mibBuilder.loadTexts:
    cLWATunnelClientTypeChange.setStatus(
        "current"
    )


# Notifications groups

cLTunnelNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 2, 2, 3)
)
cLTunnelNotificationGroup.setObjects(
      *(("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelStatusChange"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelDomainStatusChange"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLWATunnelClientTypeChange"))
)
if mibBuilder.loadTexts:
    cLTunnelNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLwappTunnelMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 2, 1, 1)
)
ciscoLwappTunnelMIBCompliance.setObjects(
      *(("CISCO-LWAPP-TUNNEL-MIB", "cLTunnelConfigGroup"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLTunnelNotificationObjectsGroup"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLTunnelNotificationGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappTunnelMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappTunnelMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 2, 1, 2)
)
ciscoLwappTunnelMIBComplianceRev1.setObjects(
      *(("CISCO-LWAPP-TUNNEL-MIB", "cLTunnelConfigGroup"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLTunnelNotificationObjectsGroup"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLTunnelNotificationGroup"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLTunnelConfigGroupRev1"))
)
if mibBuilder.loadTexts:
    ciscoLwappTunnelMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoLwappTunnelMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 2, 1, 3)
)
ciscoLwappTunnelMIBComplianceRev2.setObjects(
      *(("CISCO-LWAPP-TUNNEL-MIB", "cLTunnelConfigGroup"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLTunnelNotificationObjectsGroup"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLTunnelNotificationGroup"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLTunnelConfigGroupRev1"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayWlanConfigGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappTunnelMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoLwappTunnelMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 2, 1, 4)
)
ciscoLwappTunnelMIBComplianceRev3.setObjects(
      *(("CISCO-LWAPP-TUNNEL-MIB", "cLTunnelConfigGroupRev2"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLTunnelNotificationObjectsGroup"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLTunnelNotificationGroup"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayWlanProfileConfigGroup"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLTunnelConfigGroupRev1"))
)
if mibBuilder.loadTexts:
    ciscoLwappTunnelMIBComplianceRev3.setStatus(
        "deprecated"
    )

ciscoLwappTunnelMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 2, 1, 5)
)
ciscoLwappTunnelMIBComplianceRev4.setObjects(
      *(("CISCO-LWAPP-TUNNEL-MIB", "cLTunnelConfigGroupRev2"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLTunnelNotificationObjectsGroup"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLTunnelNotificationGroup"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayWlanProfileConfigGroup"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLGatewayAAAProxyConfigGroup"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLTunnelConfigGroupRev1"))
)
if mibBuilder.loadTexts:
    ciscoLwappTunnelMIBComplianceRev4.setStatus(
        "deprecated"
    )

ciscoLwappTunnelMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 848, 2, 1, 6)
)
ciscoLwappTunnelMIBComplianceRev5.setObjects(
      *(("CISCO-LWAPP-TUNNEL-MIB", "cLTunnelConfigGroupRev3"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLTunnelNotificationObjectsGroup"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLTunnelNotificationGroup"),
        ("CISCO-LWAPP-TUNNEL-MIB", "clGatewayWlanProfileConfigGroup"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLGatewayAAAProxyConfigGroup"),
        ("CISCO-LWAPP-TUNNEL-MIB", "cLTunnelConfigGroupRev1"))
)
if mibBuilder.loadTexts:
    ciscoLwappTunnelMIBComplianceRev5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-TUNNEL-MIB",
    **{"ciscoLwappTunnelMIB": ciscoLwappTunnelMIB,
       "ciscoLwappTunnelMIBNotifs": ciscoLwappTunnelMIBNotifs,
       "cLWATunnelStatusChange": cLWATunnelStatusChange,
       "cLWATunnelDomainStatusChange": cLWATunnelDomainStatusChange,
       "cLWATunnelClientTypeChange": cLWATunnelClientTypeChange,
       "ciscoLwappTunnelMIBObjects": ciscoLwappTunnelMIBObjects,
       "cLWATunnelStatusChangeReasonCode": cLWATunnelStatusChangeReasonCode,
       "cLWATunnelGwIPType": cLWATunnelGwIPType,
       "cLWATunnelGwIP": cLWATunnelGwIP,
       "cLWATunnelGwName": cLWATunnelGwName,
       "cLWATunnelType": cLWATunnelType,
       "cLWATunnelDomainName": cLWATunnelDomainName,
       "cLWATunnelActiveGwIPType": cLWATunnelActiveGwIPType,
       "cLWATunnelActiveGwIP": cLWATunnelActiveGwIP,
       "cLWATunnelActiveGwName": cLWATunnelActiveGwName,
       "cLWATunnelProfileName": cLWATunnelProfileName,
       "cLWATunnelRealm": cLWATunnelRealm,
       "cLWATunnelVlanId": cLWATunnelVlanId,
       "cLWATunnelClientMacAddress": cLWATunnelClientMacAddress,
       "cLWATunnelClientTypeChangeReasonCode": cLWATunnelClientTypeChangeReasonCode,
       "ciscoLwappTunnelMIBConform": ciscoLwappTunnelMIBConform,
       "ciscoLwappTunnelMIBCompliances": ciscoLwappTunnelMIBCompliances,
       "ciscoLwappTunnelMIBCompliance": ciscoLwappTunnelMIBCompliance,
       "ciscoLwappTunnelMIBComplianceRev1": ciscoLwappTunnelMIBComplianceRev1,
       "ciscoLwappTunnelMIBComplianceRev2": ciscoLwappTunnelMIBComplianceRev2,
       "ciscoLwappTunnelMIBComplianceRev3": ciscoLwappTunnelMIBComplianceRev3,
       "ciscoLwappTunnelMIBComplianceRev4": ciscoLwappTunnelMIBComplianceRev4,
       "ciscoLwappTunnelMIBComplianceRev5": ciscoLwappTunnelMIBComplianceRev5,
       "ciscoLwappTunnelMIBGroups": ciscoLwappTunnelMIBGroups,
       "cLTunnelConfigGroup": cLTunnelConfigGroup,
       "cLTunnelNotificationObjectsGroup": cLTunnelNotificationObjectsGroup,
       "cLTunnelNotificationGroup": cLTunnelNotificationGroup,
       "cLTunnelConfigGroupRev1": cLTunnelConfigGroupRev1,
       "clGatewayWlanConfigGroup": clGatewayWlanConfigGroup,
       "cLTunnelConfigGroupRev2": cLTunnelConfigGroupRev2,
       "clGatewayWlanProfileConfigGroup": clGatewayWlanProfileConfigGroup,
       "clApGatewayTunnelStatsGroup": clApGatewayTunnelStatsGroup,
       "cLGatewayAAAProxyConfigGroup": cLGatewayAAAProxyConfigGroup,
       "cLTunnelConfigGroupRev3": cLTunnelConfigGroupRev3,
       "ciscoLwappGatewayTunnel": ciscoLwappGatewayTunnel,
       "clGatewayTunnelTable": clGatewayTunnelTable,
       "clGatewayTunnelEntry": clGatewayTunnelEntry,
       "clGatewayTunnelName": clGatewayTunnelName,
       "clGatewayTunnelType": clGatewayTunnelType,
       "clGatewayTunnelAddressType": clGatewayTunnelAddressType,
       "clGatewayTunnelAddress": clGatewayTunnelAddress,
       "clGatewayTunnelStatus": clGatewayTunnelStatus,
       "clGatewayTunnelRowStatus": clGatewayTunnelRowStatus,
       "clGatewayTunnelAdminStatus": clGatewayTunnelAdminStatus,
       "clGatewayTunnelMtu": clGatewayTunnelMtu,
       "clGatewayTunnelFlapCount": clGatewayTunnelFlapCount,
       "cLGatewayTunnelSourceInterface": cLGatewayTunnelSourceInterface,
       "clGatewayDomainTable": clGatewayDomainTable,
       "clGatewayDomainEntry": clGatewayDomainEntry,
       "clGatewayDomainName": clGatewayDomainName,
       "clGatewayDomainTunnelType": clGatewayDomainTunnelType,
       "clGatewayDomainActiveGateway": clGatewayDomainActiveGateway,
       "clGatewayDomainPrimaryGateway": clGatewayDomainPrimaryGateway,
       "clGatewayDomainSecondaryGateway": clGatewayDomainSecondaryGateway,
       "clGatewayDomainRowStatus": clGatewayDomainRowStatus,
       "clGatewayDomainAdminStatus": clGatewayDomainAdminStatus,
       "clGatewayDomainRedundancyModel": clGatewayDomainRedundancyModel,
       "clGatewayDomainGatewayListTable": clGatewayDomainGatewayListTable,
       "clGatewayDomainGatewayListEntry": clGatewayDomainGatewayListEntry,
       "clGatewayDomainGatewayListRowStatus": clGatewayDomainGatewayListRowStatus,
       "clGatewayProfileTable": clGatewayProfileTable,
       "clGatewayProfileEntry": clGatewayProfileEntry,
       "clGatewayProfileName": clGatewayProfileName,
       "clGatewayProfileDhcpOpt82Status": clGatewayProfileDhcpOpt82Status,
       "clGatewayProfileDhcpOpt82Format": clGatewayProfileDhcpOpt82Format,
       "clGatewayProfileDhcpOpt82Delimiter": clGatewayProfileDhcpOpt82Delimiter,
       "clGatewayProfileCircuitId": clGatewayProfileCircuitId,
       "clGatewayProfileRemoteId": clGatewayProfileRemoteId,
       "clGatewayProfileRadiusProxyStatus": clGatewayProfileRadiusProxyStatus,
       "clGatewayProfileRadiusProxyAccounting": clGatewayProfileRadiusProxyAccounting,
       "clGatewayProfileRowStatus": clGatewayProfileRowStatus,
       "clGatewayProfileAdminStatus": clGatewayProfileAdminStatus,
       "clGatewayProfileAAAOverride": clGatewayProfileAAAOverride,
       "clGatewayRuleTable": clGatewayRuleTable,
       "clGatewayRuleEntry": clGatewayRuleEntry,
       "clGatewayRuleName": clGatewayRuleName,
       "clGatewayRuleTunnelType": clGatewayRuleTunnelType,
       "clGatewayRuleVlanId": clGatewayRuleVlanId,
       "clGatewayRuleDomainName": clGatewayRuleDomainName,
       "clGatewayRuleRowStatus": clGatewayRuleRowStatus,
       "clGatewayRuleRealm": clGatewayRuleRealm,
       "clApGatewayTunnelTable": clApGatewayTunnelTable,
       "clApGatewayTunnelEntry": clApGatewayTunnelEntry,
       "clApGatewayTunnelStatus": clApGatewayTunnelStatus,
       "clApGatewayTunnelClientCount": clApGatewayTunnelClientCount,
       "clApGatewayTunnelMtu": clApGatewayTunnelMtu,
       "clApGatewayTunnelFlapCount": clApGatewayTunnelFlapCount,
       "clApGatewayDomainTable": clApGatewayDomainTable,
       "clApGatewayDomainEntry": clApGatewayDomainEntry,
       "clApGatewayDomainActiveGateway": clApGatewayDomainActiveGateway,
       "clGatewayTunnelStatsTable": clGatewayTunnelStatsTable,
       "clGatewayTunnelStatsEntry": clGatewayTunnelStatsEntry,
       "clGatewayTunnelStatsClientCount": clGatewayTunnelStatsClientCount,
       "clGatewayTunnelStatsTunnelUpTime": clGatewayTunnelStatsTunnelUpTime,
       "clGatewayTunnelStatsKeepaliveLoss": clGatewayTunnelStatsKeepaliveLoss,
       "clGatewayTunnelStatsTunnelRxBytes": clGatewayTunnelStatsTunnelRxBytes,
       "clGatewayTunnelStatsTunnelTxBytes": clGatewayTunnelStatsTunnelTxBytes,
       "clGatewayTunnelStatsTunnelRxPkts": clGatewayTunnelStatsTunnelRxPkts,
       "clGatewayTunnelStatsTunnelTxPkts": clGatewayTunnelStatsTunnelTxPkts,
       "clApGatewayTunnelStatsTable": clApGatewayTunnelStatsTable,
       "clApGatewayTunnelStatsEntry": clApGatewayTunnelStatsEntry,
       "clApGatewayTunnelStatsTunnelUpTime": clApGatewayTunnelStatsTunnelUpTime,
       "clApGatewayTunnelStatsKeepaliveLoss": clApGatewayTunnelStatsKeepaliveLoss,
       "clApGatewayTunnelStatsTunnelRxBytes": clApGatewayTunnelStatsTunnelRxBytes,
       "clApGatewayTunnelStatsTunnelTxBytes": clApGatewayTunnelStatsTunnelTxBytes,
       "clApGatewayTunnelStatsTunnelRxPkts": clApGatewayTunnelStatsTunnelRxPkts,
       "clApGatewayTunnelStatsTunnelTxPkts": clApGatewayTunnelStatsTunnelTxPkts,
       "clApGatewayTunnelStatsTunnelRxBytes64": clApGatewayTunnelStatsTunnelRxBytes64,
       "clApGatewayTunnelStatsTunnelTxBytes64": clApGatewayTunnelStatsTunnelTxBytes64,
       "clApGatewayTunnelStatsTunnelRxPkts64": clApGatewayTunnelStatsTunnelRxPkts64,
       "clApGatewayTunnelStatsTunnelTxPkts64": clApGatewayTunnelStatsTunnelTxPkts64,
       "clGatewayGlobalInterface": clGatewayGlobalInterface,
       "cLGatewayInterface": cLGatewayInterface,
       "clGatewayGlobalHeartbeatInterval": clGatewayGlobalHeartbeatInterval,
       "cLGatewayHeartbeatInterval": cLGatewayHeartbeatInterval,
       "clGatewayGlobalHeartbeatMaxSkipCount": clGatewayGlobalHeartbeatMaxSkipCount,
       "cLGatewayHeartbeatMaxSkipCount": cLGatewayHeartbeatMaxSkipCount,
       "clGatewayWlanConfig": clGatewayWlanConfig,
       "cLGatewayWlanConfigTable": cLGatewayWlanConfigTable,
       "cLGatewayWlanConfigEntry": cLGatewayWlanConfigEntry,
       "cLGatewayWlanVlanOverrideEnable": cLGatewayWlanVlanOverrideEnable,
       "cLGatewayWlanVlanId": cLGatewayWlanVlanId,
       "clGatewayWlanProfileConfig": clGatewayWlanProfileConfig,
       "cLGatewayWlanProfileConfigTable": cLGatewayWlanProfileConfigTable,
       "cLGatewayWlanProfileConfigEntry": cLGatewayWlanProfileConfigEntry,
       "cLGatewayWlanProfileTunnelProfile": cLGatewayWlanProfileTunnelProfile,
       "clGatewayAAAProxyConfig": clGatewayAAAProxyConfig,
       "cLGatewayAAAProxyConfigTable": cLGatewayAAAProxyConfigTable,
       "cLGatewayAAAProxyConfigEntry": cLGatewayAAAProxyConfigEntry,
       "cLGatewayAAAProxyKey": cLGatewayAAAProxyKey,
       "cLGatewayAAAProxyRowStatus": cLGatewayAAAProxyRowStatus,
       "cLGatewayAAAProxyKeyType": cLGatewayAAAProxyKeyType,
       "cLGatewayAAAProxyPort": cLGatewayAAAProxyPort}
)
