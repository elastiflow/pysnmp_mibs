# SNMP MIB module (ZHONE-COM-IP-ROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zhone_5504/ZHONE-COM-IP-ROUTE-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:11:27 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(rdEntry,
 rdIndex) = mibBuilder.importSymbols(
    "ZHONE-COM-IP-RD-MIB",
    "rdEntry",
    "rdIndex")

(zhoneIp,
 zhoneModules) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneIp",
    "zhoneModules")


# MODULE-IDENTITY

comIpRoute = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 57)
)
if mibBuilder.loadTexts:
    comIpRoute.setRevisions(
        ("2000-09-11 16:33",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Route_ObjectIdentity = ObjectIdentity
route = _Route_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 7)
)
if mibBuilder.loadTexts:
    route.setStatus("current")
_ZhoneRouteInfoTable_Object = MibTable
zhoneRouteInfoTable = _ZhoneRouteInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 7, 1)
)
if mibBuilder.loadTexts:
    zhoneRouteInfoTable.setStatus("current")
_ZhoneRouteInfoEntry_Object = MibTableRow
zhoneRouteInfoEntry = _ZhoneRouteInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    zhoneRouteInfoEntry.setStatus("current")
_ZhIpCidrRouteNumber_Type = Gauge32
_ZhIpCidrRouteNumber_Object = MibTableColumn
zhIpCidrRouteNumber = _ZhIpCidrRouteNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 7, 1, 1, 1),
    _ZhIpCidrRouteNumber_Type()
)
zhIpCidrRouteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIpCidrRouteNumber.setStatus("current")
_ZhoneIpCidrRouteTable_Object = MibTable
zhoneIpCidrRouteTable = _ZhoneIpCidrRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 7, 3)
)
if mibBuilder.loadTexts:
    zhoneIpCidrRouteTable.setStatus("current")
_ZhoneIpCidrRouteEntry_Object = MibTableRow
zhoneIpCidrRouteEntry = _ZhoneIpCidrRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 7, 3, 1)
)
zhoneIpCidrRouteEntry.setIndexNames(
    (0, "ZHONE-COM-IP-RD-MIB", "rdIndex"),
    (0, "ZHONE-COM-IP-ROUTE-MIB", "zhIpCidrRouteDest"),
    (0, "ZHONE-COM-IP-ROUTE-MIB", "zhIpCidrRouteMask"),
    (0, "ZHONE-COM-IP-ROUTE-MIB", "zhIpCidrRouteNextHop"),
)
if mibBuilder.loadTexts:
    zhoneIpCidrRouteEntry.setStatus("current")
_ZhIpCidrRouteDest_Type = IpAddress
_ZhIpCidrRouteDest_Object = MibTableColumn
zhIpCidrRouteDest = _ZhIpCidrRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 7, 3, 1, 1),
    _ZhIpCidrRouteDest_Type()
)
zhIpCidrRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhIpCidrRouteDest.setStatus("current")
_ZhIpCidrRouteMask_Type = IpAddress
_ZhIpCidrRouteMask_Object = MibTableColumn
zhIpCidrRouteMask = _ZhIpCidrRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 7, 3, 1, 2),
    _ZhIpCidrRouteMask_Type()
)
zhIpCidrRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhIpCidrRouteMask.setStatus("current")
_ZhIpCidrRouteNextHop_Type = IpAddress
_ZhIpCidrRouteNextHop_Object = MibTableColumn
zhIpCidrRouteNextHop = _ZhIpCidrRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 7, 3, 1, 3),
    _ZhIpCidrRouteNextHop_Type()
)
zhIpCidrRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhIpCidrRouteNextHop.setStatus("current")
_ZhIpCidrRouteIfIndex_Type = InterfaceIndexOrZero
_ZhIpCidrRouteIfIndex_Object = MibTableColumn
zhIpCidrRouteIfIndex = _ZhIpCidrRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 7, 3, 1, 4),
    _ZhIpCidrRouteIfIndex_Type()
)
zhIpCidrRouteIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhIpCidrRouteIfIndex.setStatus("current")


class _ZhIpCidrRouteType_Type(Integer32):
    """Custom type zhIpCidrRouteType based on Integer32"""
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
        *(("other", 1),
          ("reject", 2),
          ("local", 3),
          ("remote", 4))
    )


_ZhIpCidrRouteType_Type.__name__ = "Integer32"
_ZhIpCidrRouteType_Object = MibTableColumn
zhIpCidrRouteType = _ZhIpCidrRouteType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 7, 3, 1, 5),
    _ZhIpCidrRouteType_Type()
)
zhIpCidrRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhIpCidrRouteType.setStatus("current")


class _ZhIpCidrRouteProto_Type(Integer32):
    """Custom type zhIpCidrRouteProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8,
              9,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("local", 2),
          ("netmgmt", 3),
          ("icmp", 4),
          ("rip", 8),
          ("isIs", 9),
          ("ospf", 13),
          ("bgp", 14),
          ("idpr", 15))
    )


_ZhIpCidrRouteProto_Type.__name__ = "Integer32"
_ZhIpCidrRouteProto_Object = MibTableColumn
zhIpCidrRouteProto = _ZhIpCidrRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 7, 3, 1, 6),
    _ZhIpCidrRouteProto_Type()
)
zhIpCidrRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIpCidrRouteProto.setStatus("current")
_ZhIpCidrRouteAge_Type = Unsigned32
_ZhIpCidrRouteAge_Object = MibTableColumn
zhIpCidrRouteAge = _ZhIpCidrRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 7, 3, 1, 7),
    _ZhIpCidrRouteAge_Type()
)
zhIpCidrRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhIpCidrRouteAge.setStatus("current")
if mibBuilder.loadTexts:
    zhIpCidrRouteAge.setUnits("seconds")
_ZhIpCidrRouteInfo_Type = ObjectIdentifier
_ZhIpCidrRouteInfo_Object = MibTableColumn
zhIpCidrRouteInfo = _ZhIpCidrRouteInfo_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 7, 3, 1, 8),
    _ZhIpCidrRouteInfo_Type()
)
zhIpCidrRouteInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhIpCidrRouteInfo.setStatus("current")


class _ZhIpCidrRouteNextHopAS_Type(Integer32):
    """Custom type zhIpCidrRouteNextHopAS based on Integer32"""
    defaultValue = 0


_ZhIpCidrRouteNextHopAS_Type.__name__ = "Integer32"
_ZhIpCidrRouteNextHopAS_Object = MibTableColumn
zhIpCidrRouteNextHopAS = _ZhIpCidrRouteNextHopAS_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 7, 3, 1, 9),
    _ZhIpCidrRouteNextHopAS_Type()
)
zhIpCidrRouteNextHopAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhIpCidrRouteNextHopAS.setStatus("current")


class _ZhIpCidrRouteMetric1_Type(Integer32):
    """Custom type zhIpCidrRouteMetric1 based on Integer32"""
    defaultValue = -1


_ZhIpCidrRouteMetric1_Type.__name__ = "Integer32"
_ZhIpCidrRouteMetric1_Object = MibTableColumn
zhIpCidrRouteMetric1 = _ZhIpCidrRouteMetric1_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 7, 3, 1, 10),
    _ZhIpCidrRouteMetric1_Type()
)
zhIpCidrRouteMetric1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhIpCidrRouteMetric1.setStatus("current")


class _ZhIpCidrRouteMetric2_Type(Integer32):
    """Custom type zhIpCidrRouteMetric2 based on Integer32"""
    defaultValue = -1


_ZhIpCidrRouteMetric2_Type.__name__ = "Integer32"
_ZhIpCidrRouteMetric2_Object = MibTableColumn
zhIpCidrRouteMetric2 = _ZhIpCidrRouteMetric2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 7, 3, 1, 11),
    _ZhIpCidrRouteMetric2_Type()
)
zhIpCidrRouteMetric2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhIpCidrRouteMetric2.setStatus("current")


class _ZhIpCidrRouteMetric3_Type(Integer32):
    """Custom type zhIpCidrRouteMetric3 based on Integer32"""
    defaultValue = -1


_ZhIpCidrRouteMetric3_Type.__name__ = "Integer32"
_ZhIpCidrRouteMetric3_Object = MibTableColumn
zhIpCidrRouteMetric3 = _ZhIpCidrRouteMetric3_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 7, 3, 1, 12),
    _ZhIpCidrRouteMetric3_Type()
)
zhIpCidrRouteMetric3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhIpCidrRouteMetric3.setStatus("current")


class _ZhIpCidrRouteMetric4_Type(Integer32):
    """Custom type zhIpCidrRouteMetric4 based on Integer32"""
    defaultValue = -1


_ZhIpCidrRouteMetric4_Type.__name__ = "Integer32"
_ZhIpCidrRouteMetric4_Object = MibTableColumn
zhIpCidrRouteMetric4 = _ZhIpCidrRouteMetric4_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 7, 3, 1, 13),
    _ZhIpCidrRouteMetric4_Type()
)
zhIpCidrRouteMetric4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhIpCidrRouteMetric4.setStatus("current")


class _ZhIpCidrRouteMetric5_Type(Integer32):
    """Custom type zhIpCidrRouteMetric5 based on Integer32"""
    defaultValue = -1


_ZhIpCidrRouteMetric5_Type.__name__ = "Integer32"
_ZhIpCidrRouteMetric5_Object = MibTableColumn
zhIpCidrRouteMetric5 = _ZhIpCidrRouteMetric5_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 7, 3, 1, 14),
    _ZhIpCidrRouteMetric5_Type()
)
zhIpCidrRouteMetric5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhIpCidrRouteMetric5.setStatus("current")
rdEntry.registerAugmentions(
    ("ZHONE-COM-IP-ROUTE-MIB",
     "zhoneRouteInfoEntry")
)
zhoneRouteInfoEntry.setIndexNames(*rdEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-COM-IP-ROUTE-MIB",
    **{"route": route,
       "zhoneRouteInfoTable": zhoneRouteInfoTable,
       "zhoneRouteInfoEntry": zhoneRouteInfoEntry,
       "zhIpCidrRouteNumber": zhIpCidrRouteNumber,
       "zhoneIpCidrRouteTable": zhoneIpCidrRouteTable,
       "zhoneIpCidrRouteEntry": zhoneIpCidrRouteEntry,
       "zhIpCidrRouteDest": zhIpCidrRouteDest,
       "zhIpCidrRouteMask": zhIpCidrRouteMask,
       "zhIpCidrRouteNextHop": zhIpCidrRouteNextHop,
       "zhIpCidrRouteIfIndex": zhIpCidrRouteIfIndex,
       "zhIpCidrRouteType": zhIpCidrRouteType,
       "zhIpCidrRouteProto": zhIpCidrRouteProto,
       "zhIpCidrRouteAge": zhIpCidrRouteAge,
       "zhIpCidrRouteInfo": zhIpCidrRouteInfo,
       "zhIpCidrRouteNextHopAS": zhIpCidrRouteNextHopAS,
       "zhIpCidrRouteMetric1": zhIpCidrRouteMetric1,
       "zhIpCidrRouteMetric2": zhIpCidrRouteMetric2,
       "zhIpCidrRouteMetric3": zhIpCidrRouteMetric3,
       "zhIpCidrRouteMetric4": zhIpCidrRouteMetric4,
       "zhIpCidrRouteMetric5": zhIpCidrRouteMetric5,
       "comIpRoute": comIpRoute}
)
