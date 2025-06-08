# SNMP MIB module (CIENA-CES-IP-INTERFACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_1271/CIENA-CES-IP-INTERFACE-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:39:46 2025
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

(cienaGlobalMacAddress,
 cienaGlobalSeverity) = mibBuilder.importSymbols(
    "CIENA-GLOBAL-MIB",
    "cienaGlobalMacAddress",
    "cienaGlobalSeverity")

(cienaCesConfig,
 cienaCesNotifications) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig",
    "cienaCesNotifications")

(CienaGlobalState,) = mibBuilder.importSymbols(
    "CIENA-TC",
    "CienaGlobalState")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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

(DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cienaCesIpInterfaceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8)
)
if mibBuilder.loadTexts:
    cienaCesIpInterfaceMIB.setRevisions(
        ("2017-06-07 00:00",
         "2016-11-17 00:00",
         "2016-08-05 00:00",
         "2015-07-29 00:00",
         "2015-06-29 00:00",
         "2015-06-26 00:00",
         "2015-06-25 00:00",
         "2014-04-03 00:00",
         "2014-04-16 00:00",
         "2012-10-17 00:00",
         "2011-07-01 00:00",
         "2011-03-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaCesIpInterfaceMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesIpInterfaceMIBObjects = _CienaCesIpInterfaceMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1)
)
_CienaCesIpInterface_ObjectIdentity = ObjectIdentity
cienaCesIpInterface = _CienaCesIpInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1)
)
_CienaCesIpMgmtInterfaceTable_Object = MibTable
cienaCesIpMgmtInterfaceTable = _CienaCesIpMgmtInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cienaCesIpMgmtInterfaceTable.setStatus("current")
_CienaCesIpMgmtInterfaceEntry_Object = MibTableRow
cienaCesIpMgmtInterfaceEntry = _CienaCesIpMgmtInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 1, 1)
)
cienaCesIpMgmtInterfaceEntry.setIndexNames(
    (0, "CIENA-CES-IP-INTERFACE-MIB", "cienaCesIpMgmtInterfaceIndex"),
)
if mibBuilder.loadTexts:
    cienaCesIpMgmtInterfaceEntry.setStatus("current")


class _CienaCesIpMgmtInterfaceIndex_Type(Integer32):
    """Custom type cienaCesIpMgmtInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_CienaCesIpMgmtInterfaceIndex_Type.__name__ = "Integer32"
_CienaCesIpMgmtInterfaceIndex_Object = MibTableColumn
cienaCesIpMgmtInterfaceIndex = _CienaCesIpMgmtInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 1, 1, 1),
    _CienaCesIpMgmtInterfaceIndex_Type()
)
cienaCesIpMgmtInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesIpMgmtInterfaceIndex.setStatus("current")


class _CienaCesIpMgmtInterfaceName_Type(DisplayString):
    """Custom type cienaCesIpMgmtInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CienaCesIpMgmtInterfaceName_Type.__name__ = "DisplayString"
_CienaCesIpMgmtInterfaceName_Object = MibTableColumn
cienaCesIpMgmtInterfaceName = _CienaCesIpMgmtInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 1, 1, 2),
    _CienaCesIpMgmtInterfaceName_Type()
)
cienaCesIpMgmtInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpMgmtInterfaceName.setStatus("current")
_CienaCesIpMgmtInterfaceOperIpAddr_Type = IpAddress
_CienaCesIpMgmtInterfaceOperIpAddr_Object = MibTableColumn
cienaCesIpMgmtInterfaceOperIpAddr = _CienaCesIpMgmtInterfaceOperIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 1, 1, 3),
    _CienaCesIpMgmtInterfaceOperIpAddr_Type()
)
cienaCesIpMgmtInterfaceOperIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpMgmtInterfaceOperIpAddr.setStatus("current")
_CienaCesIpMgmtInterfaceOperSubnet_Type = IpAddress
_CienaCesIpMgmtInterfaceOperSubnet_Object = MibTableColumn
cienaCesIpMgmtInterfaceOperSubnet = _CienaCesIpMgmtInterfaceOperSubnet_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 1, 1, 4),
    _CienaCesIpMgmtInterfaceOperSubnet_Type()
)
cienaCesIpMgmtInterfaceOperSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpMgmtInterfaceOperSubnet.setStatus("current")


class _CienaCesIpMgmtInterfaceAdminState_Type(Integer32):
    """Custom type cienaCesIpMgmtInterfaceAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("shutdown", 3))
    )


_CienaCesIpMgmtInterfaceAdminState_Type.__name__ = "Integer32"
_CienaCesIpMgmtInterfaceAdminState_Object = MibTableColumn
cienaCesIpMgmtInterfaceAdminState = _CienaCesIpMgmtInterfaceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 1, 1, 5),
    _CienaCesIpMgmtInterfaceAdminState_Type()
)
cienaCesIpMgmtInterfaceAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpMgmtInterfaceAdminState.setStatus("current")


class _CienaCesIpMgmtInterfaceOperState_Type(Integer32):
    """Custom type cienaCesIpMgmtInterfaceOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_CienaCesIpMgmtInterfaceOperState_Type.__name__ = "Integer32"
_CienaCesIpMgmtInterfaceOperState_Object = MibTableColumn
cienaCesIpMgmtInterfaceOperState = _CienaCesIpMgmtInterfaceOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 1, 1, 6),
    _CienaCesIpMgmtInterfaceOperState_Type()
)
cienaCesIpMgmtInterfaceOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpMgmtInterfaceOperState.setStatus("current")


class _CienaCesIpMgmtInterfaceType_Type(Integer32):
    """Custom type cienaCesIpMgmtInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("ppp", 2),
          ("loop", 3),
          ("ether", 4),
          ("cpuVsMember", 5),
          ("remoteMgmt", 6),
          ("direct", 7),
          ("directPartner", 8),
          ("active", 9),
          ("directSecondary", 10),
          ("directPartnerSecondary", 11),
          ("es1", 12),
          ("es2", 13),
          ("unnumbered", 14))
    )


_CienaCesIpMgmtInterfaceType_Type.__name__ = "Integer32"
_CienaCesIpMgmtInterfaceType_Object = MibTableColumn
cienaCesIpMgmtInterfaceType = _CienaCesIpMgmtInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 1, 1, 7),
    _CienaCesIpMgmtInterfaceType_Type()
)
cienaCesIpMgmtInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpMgmtInterfaceType.setStatus("current")
_CienaCesIpMgmtInterfaceVirtualSwitchIndex_Type = Integer32
_CienaCesIpMgmtInterfaceVirtualSwitchIndex_Object = MibTableColumn
cienaCesIpMgmtInterfaceVirtualSwitchIndex = _CienaCesIpMgmtInterfaceVirtualSwitchIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 1, 1, 8),
    _CienaCesIpMgmtInterfaceVirtualSwitchIndex_Type()
)
cienaCesIpMgmtInterfaceVirtualSwitchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpMgmtInterfaceVirtualSwitchIndex.setStatus("current")
_CienaCesIpMgmtInterfaceParentInterfaceIndex_Type = Integer32
_CienaCesIpMgmtInterfaceParentInterfaceIndex_Object = MibTableColumn
cienaCesIpMgmtInterfaceParentInterfaceIndex = _CienaCesIpMgmtInterfaceParentInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 1, 1, 9),
    _CienaCesIpMgmtInterfaceParentInterfaceIndex_Type()
)
cienaCesIpMgmtInterfaceParentInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpMgmtInterfaceParentInterfaceIndex.setStatus("current")
_CienaCesIpGatewayAddr_Type = IpAddress
_CienaCesIpGatewayAddr_Object = MibScalar
cienaCesIpGatewayAddr = _CienaCesIpGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 2),
    _CienaCesIpGatewayAddr_Type()
)
cienaCesIpGatewayAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpGatewayAddr.setStatus("current")
_CienaCesIpDataInterfaceTable_Object = MibTable
cienaCesIpDataInterfaceTable = _CienaCesIpDataInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cienaCesIpDataInterfaceTable.setStatus("current")
_CienaCesIpDataInterfaceEntry_Object = MibTableRow
cienaCesIpDataInterfaceEntry = _CienaCesIpDataInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 3, 1)
)
cienaCesIpDataInterfaceEntry.setIndexNames(
    (0, "CIENA-CES-IP-INTERFACE-MIB", "cienaCesIpDataInterfaceIndex"),
)
if mibBuilder.loadTexts:
    cienaCesIpDataInterfaceEntry.setStatus("current")
_CienaCesIpDataInterfaceIndex_Type = Integer32
_CienaCesIpDataInterfaceIndex_Object = MibTableColumn
cienaCesIpDataInterfaceIndex = _CienaCesIpDataInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 3, 1, 1),
    _CienaCesIpDataInterfaceIndex_Type()
)
cienaCesIpDataInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesIpDataInterfaceIndex.setStatus("current")


class _CienaCesIpDataInterfaceName_Type(DisplayString):
    """Custom type cienaCesIpDataInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CienaCesIpDataInterfaceName_Type.__name__ = "DisplayString"
_CienaCesIpDataInterfaceName_Object = MibTableColumn
cienaCesIpDataInterfaceName = _CienaCesIpDataInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 3, 1, 2),
    _CienaCesIpDataInterfaceName_Type()
)
cienaCesIpDataInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpDataInterfaceName.setStatus("current")
_CienaCesIpDataInterfaceIpAddr_Type = IpAddress
_CienaCesIpDataInterfaceIpAddr_Object = MibTableColumn
cienaCesIpDataInterfaceIpAddr = _CienaCesIpDataInterfaceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 3, 1, 3),
    _CienaCesIpDataInterfaceIpAddr_Type()
)
cienaCesIpDataInterfaceIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpDataInterfaceIpAddr.setStatus("deprecated")
_CienaCesIpDataInterfaceMask_Type = IpAddress
_CienaCesIpDataInterfaceMask_Object = MibTableColumn
cienaCesIpDataInterfaceMask = _CienaCesIpDataInterfaceMask_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 3, 1, 4),
    _CienaCesIpDataInterfaceMask_Type()
)
cienaCesIpDataInterfaceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpDataInterfaceMask.setStatus("deprecated")
_CienaCesIpDataInterfaceVsIndex_Type = Integer32
_CienaCesIpDataInterfaceVsIndex_Object = MibTableColumn
cienaCesIpDataInterfaceVsIndex = _CienaCesIpDataInterfaceVsIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 3, 1, 5),
    _CienaCesIpDataInterfaceVsIndex_Type()
)
cienaCesIpDataInterfaceVsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpDataInterfaceVsIndex.setStatus("current")


class _CienaCesIpDataInterfaceType_Type(Integer32):
    """Custom type cienaCesIpDataInterfaceType based on Integer32"""
    defaultValue = 1

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
        *(("broadcast", 1),
          ("pointToPoint", 2),
          ("loopBack", 3),
          ("cpuVsMember", 4))
    )


_CienaCesIpDataInterfaceType_Type.__name__ = "Integer32"
_CienaCesIpDataInterfaceType_Object = MibTableColumn
cienaCesIpDataInterfaceType = _CienaCesIpDataInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 3, 1, 6),
    _CienaCesIpDataInterfaceType_Type()
)
cienaCesIpDataInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpDataInterfaceType.setStatus("current")
_CienaCesIpDataInterfaceIfIndex_Type = Integer32
_CienaCesIpDataInterfaceIfIndex_Object = MibTableColumn
cienaCesIpDataInterfaceIfIndex = _CienaCesIpDataInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 3, 1, 7),
    _CienaCesIpDataInterfaceIfIndex_Type()
)
cienaCesIpDataInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpDataInterfaceIfIndex.setStatus("current")
_CienaCesIpDataInterfaceMac_Type = MacAddress
_CienaCesIpDataInterfaceMac_Object = MibTableColumn
cienaCesIpDataInterfaceMac = _CienaCesIpDataInterfaceMac_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 3, 1, 8),
    _CienaCesIpDataInterfaceMac_Type()
)
cienaCesIpDataInterfaceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpDataInterfaceMac.setStatus("current")


class _CienaCesIpDataInterfaceIfMtu_Type(Integer32):
    """Custom type cienaCesIpDataInterfaceIfMtu based on Integer32"""
    defaultValue = 1500


_CienaCesIpDataInterfaceIfMtu_Type.__name__ = "Integer32"
_CienaCesIpDataInterfaceIfMtu_Object = MibTableColumn
cienaCesIpDataInterfaceIfMtu = _CienaCesIpDataInterfaceIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 3, 1, 9),
    _CienaCesIpDataInterfaceIfMtu_Type()
)
cienaCesIpDataInterfaceIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpDataInterfaceIfMtu.setStatus("current")
_CienaCesIpDataInterfaceAdminState_Type = CienaGlobalState
_CienaCesIpDataInterfaceAdminState_Object = MibTableColumn
cienaCesIpDataInterfaceAdminState = _CienaCesIpDataInterfaceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 3, 1, 10),
    _CienaCesIpDataInterfaceAdminState_Type()
)
cienaCesIpDataInterfaceAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpDataInterfaceAdminState.setStatus("current")


class _CienaCesIpDataInterfaceOperState_Type(CienaGlobalState):
    """Custom type cienaCesIpDataInterfaceOperState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesIpDataInterfaceOperState_Type.__name__ = "CienaGlobalState"
_CienaCesIpDataInterfaceOperState_Object = MibTableColumn
cienaCesIpDataInterfaceOperState = _CienaCesIpDataInterfaceOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 3, 1, 11),
    _CienaCesIpDataInterfaceOperState_Type()
)
cienaCesIpDataInterfaceOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpDataInterfaceOperState.setStatus("current")


class _CienaCesIpDataInterfaceIpForwarding_Type(TruthValue):
    """Custom type cienaCesIpDataInterfaceIpForwarding based on TruthValue"""
    defaultValue = 1


_CienaCesIpDataInterfaceIpForwarding_Type.__name__ = "TruthValue"
_CienaCesIpDataInterfaceIpForwarding_Object = MibTableColumn
cienaCesIpDataInterfaceIpForwarding = _CienaCesIpDataInterfaceIpForwarding_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 3, 1, 12),
    _CienaCesIpDataInterfaceIpForwarding_Type()
)
cienaCesIpDataInterfaceIpForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpDataInterfaceIpForwarding.setStatus("current")
_CienaCesIpDataInterfaceLdpEnable_Type = TruthValue
_CienaCesIpDataInterfaceLdpEnable_Object = MibTableColumn
cienaCesIpDataInterfaceLdpEnable = _CienaCesIpDataInterfaceLdpEnable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 3, 1, 13),
    _CienaCesIpDataInterfaceLdpEnable_Type()
)
cienaCesIpDataInterfaceLdpEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpDataInterfaceLdpEnable.setStatus("current")
_CienaCesIpDataInterfaceRsvpEnable_Type = TruthValue
_CienaCesIpDataInterfaceRsvpEnable_Object = MibTableColumn
cienaCesIpDataInterfaceRsvpEnable = _CienaCesIpDataInterfaceRsvpEnable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 3, 1, 14),
    _CienaCesIpDataInterfaceRsvpEnable_Type()
)
cienaCesIpDataInterfaceRsvpEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpDataInterfaceRsvpEnable.setStatus("current")
_CienaCesIpDataInterfaceTunnelDependency_Type = TruthValue
_CienaCesIpDataInterfaceTunnelDependency_Object = MibTableColumn
cienaCesIpDataInterfaceTunnelDependency = _CienaCesIpDataInterfaceTunnelDependency_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 3, 1, 15),
    _CienaCesIpDataInterfaceTunnelDependency_Type()
)
cienaCesIpDataInterfaceTunnelDependency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpDataInterfaceTunnelDependency.setStatus("current")
_CienaCesIpDataInterfaceL2VpnDependency_Type = TruthValue
_CienaCesIpDataInterfaceL2VpnDependency_Object = MibTableColumn
cienaCesIpDataInterfaceL2VpnDependency = _CienaCesIpDataInterfaceL2VpnDependency_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 3, 1, 16),
    _CienaCesIpDataInterfaceL2VpnDependency_Type()
)
cienaCesIpDataInterfaceL2VpnDependency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpDataInterfaceL2VpnDependency.setStatus("current")
_CienaCesIpDataInterfaceOspfEnable_Type = TruthValue
_CienaCesIpDataInterfaceOspfEnable_Object = MibTableColumn
cienaCesIpDataInterfaceOspfEnable = _CienaCesIpDataInterfaceOspfEnable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 3, 1, 17),
    _CienaCesIpDataInterfaceOspfEnable_Type()
)
cienaCesIpDataInterfaceOspfEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpDataInterfaceOspfEnable.setStatus("current")
_CienaCesIpDataInterfaceIsisEnable_Type = TruthValue
_CienaCesIpDataInterfaceIsisEnable_Object = MibTableColumn
cienaCesIpDataInterfaceIsisEnable = _CienaCesIpDataInterfaceIsisEnable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 3, 1, 18),
    _CienaCesIpDataInterfaceIsisEnable_Type()
)
cienaCesIpDataInterfaceIsisEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpDataInterfaceIsisEnable.setStatus("current")
_CienaCesIpDataInterfaceStaticArpEnable_Type = TruthValue
_CienaCesIpDataInterfaceStaticArpEnable_Object = MibTableColumn
cienaCesIpDataInterfaceStaticArpEnable = _CienaCesIpDataInterfaceStaticArpEnable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 3, 1, 19),
    _CienaCesIpDataInterfaceStaticArpEnable_Type()
)
cienaCesIpDataInterfaceStaticArpEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpDataInterfaceStaticArpEnable.setStatus("current")
_CienaCesIpDataInterfaceVccvDependency_Type = TruthValue
_CienaCesIpDataInterfaceVccvDependency_Object = MibTableColumn
cienaCesIpDataInterfaceVccvDependency = _CienaCesIpDataInterfaceVccvDependency_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 3, 1, 20),
    _CienaCesIpDataInterfaceVccvDependency_Type()
)
cienaCesIpDataInterfaceVccvDependency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpDataInterfaceVccvDependency.setStatus("current")
_CienaCesIpDataInterfacePtpEnable_Type = TruthValue
_CienaCesIpDataInterfacePtpEnable_Object = MibTableColumn
cienaCesIpDataInterfacePtpEnable = _CienaCesIpDataInterfacePtpEnable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 3, 1, 21),
    _CienaCesIpDataInterfacePtpEnable_Type()
)
cienaCesIpDataInterfacePtpEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpDataInterfacePtpEnable.setStatus("current")
_CienaCesIpDataInterfaceIfNum_Type = Unsigned32
_CienaCesIpDataInterfaceIfNum_Object = MibTableColumn
cienaCesIpDataInterfaceIfNum = _CienaCesIpDataInterfaceIfNum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 3, 1, 22),
    _CienaCesIpDataInterfaceIfNum_Type()
)
cienaCesIpDataInterfaceIfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpDataInterfaceIfNum.setStatus("current")
_CienaCesIpDataInterfaceStaticArpDestinationIp_Type = IpAddress
_CienaCesIpDataInterfaceStaticArpDestinationIp_Object = MibTableColumn
cienaCesIpDataInterfaceStaticArpDestinationIp = _CienaCesIpDataInterfaceStaticArpDestinationIp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 3, 1, 23),
    _CienaCesIpDataInterfaceStaticArpDestinationIp_Type()
)
cienaCesIpDataInterfaceStaticArpDestinationIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpDataInterfaceStaticArpDestinationIp.setStatus("current")
_CienaCesIpDataInterfaceStaticArpDestinationMac_Type = MacAddress
_CienaCesIpDataInterfaceStaticArpDestinationMac_Object = MibTableColumn
cienaCesIpDataInterfaceStaticArpDestinationMac = _CienaCesIpDataInterfaceStaticArpDestinationMac_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 3, 1, 24),
    _CienaCesIpDataInterfaceStaticArpDestinationMac_Type()
)
cienaCesIpDataInterfaceStaticArpDestinationMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpDataInterfaceStaticArpDestinationMac.setStatus("current")


class _CienaCesIpDataInterfaceRole_Type(Integer32):
    """Custom type cienaCesIpDataInterfaceRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("controlplane", 1),
          ("connectivity", 2),
          ("benchmark", 3))
    )


_CienaCesIpDataInterfaceRole_Type.__name__ = "Integer32"
_CienaCesIpDataInterfaceRole_Object = MibTableColumn
cienaCesIpDataInterfaceRole = _CienaCesIpDataInterfaceRole_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 3, 1, 25),
    _CienaCesIpDataInterfaceRole_Type()
)
cienaCesIpDataInterfaceRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpDataInterfaceRole.setStatus("current")
_CienaCesIpInterfaceL3InterfaceBaseMac_Type = MacAddress
_CienaCesIpInterfaceL3InterfaceBaseMac_Object = MibScalar
cienaCesIpInterfaceL3InterfaceBaseMac = _CienaCesIpInterfaceL3InterfaceBaseMac_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 4),
    _CienaCesIpInterfaceL3InterfaceBaseMac_Type()
)
cienaCesIpInterfaceL3InterfaceBaseMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpInterfaceL3InterfaceBaseMac.setStatus("current")
_CienaCesIpDataInterfaceInetTable_Object = MibTable
cienaCesIpDataInterfaceInetTable = _CienaCesIpDataInterfaceInetTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cienaCesIpDataInterfaceInetTable.setStatus("current")
_CienaCesIpDataInterfaceInetEntry_Object = MibTableRow
cienaCesIpDataInterfaceInetEntry = _CienaCesIpDataInterfaceInetEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 5, 1)
)
cienaCesIpDataInterfaceInetEntry.setIndexNames(
    (0, "CIENA-CES-IP-INTERFACE-MIB", "cienaCesIpDataInterfaceIndex"),
    (0, "CIENA-CES-IP-INTERFACE-MIB", "cienaCesIpDataInterfaceInetIndexAddrType"),
    (0, "CIENA-CES-IP-INTERFACE-MIB", "cienaCesIpDataInterfaceInetIndexAddr"),
)
if mibBuilder.loadTexts:
    cienaCesIpDataInterfaceInetEntry.setStatus("current")
_CienaCesIpDataInterfaceInetIndexAddrType_Type = InetAddressType
_CienaCesIpDataInterfaceInetIndexAddrType_Object = MibTableColumn
cienaCesIpDataInterfaceInetIndexAddrType = _CienaCesIpDataInterfaceInetIndexAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 5, 1, 1),
    _CienaCesIpDataInterfaceInetIndexAddrType_Type()
)
cienaCesIpDataInterfaceInetIndexAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesIpDataInterfaceInetIndexAddrType.setStatus("current")
_CienaCesIpDataInterfaceInetIndexAddr_Type = InetAddress
_CienaCesIpDataInterfaceInetIndexAddr_Object = MibTableColumn
cienaCesIpDataInterfaceInetIndexAddr = _CienaCesIpDataInterfaceInetIndexAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 5, 1, 2),
    _CienaCesIpDataInterfaceInetIndexAddr_Type()
)
cienaCesIpDataInterfaceInetIndexAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesIpDataInterfaceInetIndexAddr.setStatus("current")
_CienaCesIpDataInterfaceInetAddrPrefixLength_Type = InetAddressPrefixLength
_CienaCesIpDataInterfaceInetAddrPrefixLength_Object = MibTableColumn
cienaCesIpDataInterfaceInetAddrPrefixLength = _CienaCesIpDataInterfaceInetAddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 5, 1, 3),
    _CienaCesIpDataInterfaceInetAddrPrefixLength_Type()
)
cienaCesIpDataInterfaceInetAddrPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpDataInterfaceInetAddrPrefixLength.setStatus("current")
_CienaCesIpDataInterfaceInetAddrType_Type = InetAddressType
_CienaCesIpDataInterfaceInetAddrType_Object = MibTableColumn
cienaCesIpDataInterfaceInetAddrType = _CienaCesIpDataInterfaceInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 5, 1, 4),
    _CienaCesIpDataInterfaceInetAddrType_Type()
)
cienaCesIpDataInterfaceInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpDataInterfaceInetAddrType.setStatus("current")
_CienaCesIpDataInterfaceInetAddr_Type = InetAddress
_CienaCesIpDataInterfaceInetAddr_Object = MibTableColumn
cienaCesIpDataInterfaceInetAddr = _CienaCesIpDataInterfaceInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 1, 1, 5, 1, 5),
    _CienaCesIpDataInterfaceInetAddr_Type()
)
cienaCesIpDataInterfaceInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIpDataInterfaceInetAddr.setStatus("current")
_CienaCesIpInterfaceMIBConformance_ObjectIdentity = ObjectIdentity
cienaCesIpInterfaceMIBConformance = _CienaCesIpInterfaceMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 3)
)
_CienaCesIpInterfaceMIBCompliances_ObjectIdentity = ObjectIdentity
cienaCesIpInterfaceMIBCompliances = _CienaCesIpInterfaceMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 3, 1)
)
_CienaCesIpInterfaceMIBGroups_ObjectIdentity = ObjectIdentity
cienaCesIpInterfaceMIBGroups = _CienaCesIpInterfaceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 8, 3, 2)
)
_CienaCesIpInterfaceMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cienaCesIpInterfaceMIBNotificationPrefix = _CienaCesIpInterfaceMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 8)
)
_CienaCesIpInterfaceMIBNotifications_ObjectIdentity = ObjectIdentity
cienaCesIpInterfaceMIBNotifications = _CienaCesIpInterfaceMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 8, 0)
)

# Managed Objects groups


# Notification objects

cienaCesIpMgmtInterfaceAddrChgNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 8, 0, 1)
)
cienaCesIpMgmtInterfaceAddrChgNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-IP-INTERFACE-MIB", "cienaCesIpMgmtInterfaceName"),
        ("CIENA-CES-IP-INTERFACE-MIB", "cienaCesIpMgmtInterfaceOperIpAddr"),
        ("CIENA-CES-IP-INTERFACE-MIB", "cienaCesIpMgmtInterfaceOperSubnet"))
)
if mibBuilder.loadTexts:
    cienaCesIpMgmtInterfaceAddrChgNotification.setStatus(
        "current"
    )

cienaCesIpMgmtInterfaceGatewayChgNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 8, 0, 2)
)
cienaCesIpMgmtInterfaceGatewayChgNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-IP-INTERFACE-MIB", "cienaCesIpGatewayAddr"))
)
if mibBuilder.loadTexts:
    cienaCesIpMgmtInterfaceGatewayChgNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-IP-INTERFACE-MIB",
    **{"cienaCesIpInterfaceMIB": cienaCesIpInterfaceMIB,
       "cienaCesIpInterfaceMIBObjects": cienaCesIpInterfaceMIBObjects,
       "cienaCesIpInterface": cienaCesIpInterface,
       "cienaCesIpMgmtInterfaceTable": cienaCesIpMgmtInterfaceTable,
       "cienaCesIpMgmtInterfaceEntry": cienaCesIpMgmtInterfaceEntry,
       "cienaCesIpMgmtInterfaceIndex": cienaCesIpMgmtInterfaceIndex,
       "cienaCesIpMgmtInterfaceName": cienaCesIpMgmtInterfaceName,
       "cienaCesIpMgmtInterfaceOperIpAddr": cienaCesIpMgmtInterfaceOperIpAddr,
       "cienaCesIpMgmtInterfaceOperSubnet": cienaCesIpMgmtInterfaceOperSubnet,
       "cienaCesIpMgmtInterfaceAdminState": cienaCesIpMgmtInterfaceAdminState,
       "cienaCesIpMgmtInterfaceOperState": cienaCesIpMgmtInterfaceOperState,
       "cienaCesIpMgmtInterfaceType": cienaCesIpMgmtInterfaceType,
       "cienaCesIpMgmtInterfaceVirtualSwitchIndex": cienaCesIpMgmtInterfaceVirtualSwitchIndex,
       "cienaCesIpMgmtInterfaceParentInterfaceIndex": cienaCesIpMgmtInterfaceParentInterfaceIndex,
       "cienaCesIpGatewayAddr": cienaCesIpGatewayAddr,
       "cienaCesIpDataInterfaceTable": cienaCesIpDataInterfaceTable,
       "cienaCesIpDataInterfaceEntry": cienaCesIpDataInterfaceEntry,
       "cienaCesIpDataInterfaceIndex": cienaCesIpDataInterfaceIndex,
       "cienaCesIpDataInterfaceName": cienaCesIpDataInterfaceName,
       "cienaCesIpDataInterfaceIpAddr": cienaCesIpDataInterfaceIpAddr,
       "cienaCesIpDataInterfaceMask": cienaCesIpDataInterfaceMask,
       "cienaCesIpDataInterfaceVsIndex": cienaCesIpDataInterfaceVsIndex,
       "cienaCesIpDataInterfaceType": cienaCesIpDataInterfaceType,
       "cienaCesIpDataInterfaceIfIndex": cienaCesIpDataInterfaceIfIndex,
       "cienaCesIpDataInterfaceMac": cienaCesIpDataInterfaceMac,
       "cienaCesIpDataInterfaceIfMtu": cienaCesIpDataInterfaceIfMtu,
       "cienaCesIpDataInterfaceAdminState": cienaCesIpDataInterfaceAdminState,
       "cienaCesIpDataInterfaceOperState": cienaCesIpDataInterfaceOperState,
       "cienaCesIpDataInterfaceIpForwarding": cienaCesIpDataInterfaceIpForwarding,
       "cienaCesIpDataInterfaceLdpEnable": cienaCesIpDataInterfaceLdpEnable,
       "cienaCesIpDataInterfaceRsvpEnable": cienaCesIpDataInterfaceRsvpEnable,
       "cienaCesIpDataInterfaceTunnelDependency": cienaCesIpDataInterfaceTunnelDependency,
       "cienaCesIpDataInterfaceL2VpnDependency": cienaCesIpDataInterfaceL2VpnDependency,
       "cienaCesIpDataInterfaceOspfEnable": cienaCesIpDataInterfaceOspfEnable,
       "cienaCesIpDataInterfaceIsisEnable": cienaCesIpDataInterfaceIsisEnable,
       "cienaCesIpDataInterfaceStaticArpEnable": cienaCesIpDataInterfaceStaticArpEnable,
       "cienaCesIpDataInterfaceVccvDependency": cienaCesIpDataInterfaceVccvDependency,
       "cienaCesIpDataInterfacePtpEnable": cienaCesIpDataInterfacePtpEnable,
       "cienaCesIpDataInterfaceIfNum": cienaCesIpDataInterfaceIfNum,
       "cienaCesIpDataInterfaceStaticArpDestinationIp": cienaCesIpDataInterfaceStaticArpDestinationIp,
       "cienaCesIpDataInterfaceStaticArpDestinationMac": cienaCesIpDataInterfaceStaticArpDestinationMac,
       "cienaCesIpDataInterfaceRole": cienaCesIpDataInterfaceRole,
       "cienaCesIpInterfaceL3InterfaceBaseMac": cienaCesIpInterfaceL3InterfaceBaseMac,
       "cienaCesIpDataInterfaceInetTable": cienaCesIpDataInterfaceInetTable,
       "cienaCesIpDataInterfaceInetEntry": cienaCesIpDataInterfaceInetEntry,
       "cienaCesIpDataInterfaceInetIndexAddrType": cienaCesIpDataInterfaceInetIndexAddrType,
       "cienaCesIpDataInterfaceInetIndexAddr": cienaCesIpDataInterfaceInetIndexAddr,
       "cienaCesIpDataInterfaceInetAddrPrefixLength": cienaCesIpDataInterfaceInetAddrPrefixLength,
       "cienaCesIpDataInterfaceInetAddrType": cienaCesIpDataInterfaceInetAddrType,
       "cienaCesIpDataInterfaceInetAddr": cienaCesIpDataInterfaceInetAddr,
       "cienaCesIpInterfaceMIBConformance": cienaCesIpInterfaceMIBConformance,
       "cienaCesIpInterfaceMIBCompliances": cienaCesIpInterfaceMIBCompliances,
       "cienaCesIpInterfaceMIBGroups": cienaCesIpInterfaceMIBGroups,
       "cienaCesIpInterfaceMIBNotificationPrefix": cienaCesIpInterfaceMIBNotificationPrefix,
       "cienaCesIpInterfaceMIBNotifications": cienaCesIpInterfaceMIBNotifications,
       "cienaCesIpMgmtInterfaceAddrChgNotification": cienaCesIpMgmtInterfaceAddrChgNotification,
       "cienaCesIpMgmtInterfaceGatewayChgNotification": cienaCesIpMgmtInterfaceGatewayChgNotification}
)
