# SNMP MIB module (ZYXEL-STATIC-ROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-STATIC-ROUTE-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 08:33:34 2025
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelStaticRoute = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 77)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelStaticRouteSetup_ObjectIdentity = ObjectIdentity
zyxelStaticRouteSetup = _ZyxelStaticRouteSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 77, 1)
)
_ZyStaticRouteMaxNumberOfRoutes_Type = Integer32
_ZyStaticRouteMaxNumberOfRoutes_Object = MibScalar
zyStaticRouteMaxNumberOfRoutes = _ZyStaticRouteMaxNumberOfRoutes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 77, 1, 1),
    _ZyStaticRouteMaxNumberOfRoutes_Type()
)
zyStaticRouteMaxNumberOfRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyStaticRouteMaxNumberOfRoutes.setStatus("current")
_ZyxelStaticRouteTable_Object = MibTable
zyxelStaticRouteTable = _ZyxelStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 77, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelStaticRouteTable.setStatus("current")
_ZyxelStaticRouteEntry_Object = MibTableRow
zyxelStaticRouteEntry = _ZyxelStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 77, 1, 2, 1)
)
zyxelStaticRouteEntry.setIndexNames(
    (0, "ZYXEL-STATIC-ROUTE-MIB", "zyStaticRouteIpAddress"),
    (0, "ZYXEL-STATIC-ROUTE-MIB", "zyStaticRouteSubnetMask"),
    (0, "ZYXEL-STATIC-ROUTE-MIB", "zyStaticRouteGateway"),
)
if mibBuilder.loadTexts:
    zyxelStaticRouteEntry.setStatus("current")
_ZyStaticRouteName_Type = DisplayString
_ZyStaticRouteName_Object = MibTableColumn
zyStaticRouteName = _ZyStaticRouteName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 77, 1, 2, 1, 1),
    _ZyStaticRouteName_Type()
)
zyStaticRouteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyStaticRouteName.setStatus("current")
_ZyStaticRouteIpAddress_Type = IpAddress
_ZyStaticRouteIpAddress_Object = MibTableColumn
zyStaticRouteIpAddress = _ZyStaticRouteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 77, 1, 2, 1, 2),
    _ZyStaticRouteIpAddress_Type()
)
zyStaticRouteIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyStaticRouteIpAddress.setStatus("current")
_ZyStaticRouteSubnetMask_Type = IpAddress
_ZyStaticRouteSubnetMask_Object = MibTableColumn
zyStaticRouteSubnetMask = _ZyStaticRouteSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 77, 1, 2, 1, 3),
    _ZyStaticRouteSubnetMask_Type()
)
zyStaticRouteSubnetMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyStaticRouteSubnetMask.setStatus("current")
_ZyStaticRouteGateway_Type = IpAddress
_ZyStaticRouteGateway_Object = MibTableColumn
zyStaticRouteGateway = _ZyStaticRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 77, 1, 2, 1, 4),
    _ZyStaticRouteGateway_Type()
)
zyStaticRouteGateway.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyStaticRouteGateway.setStatus("current")
_ZyStaticRouteMetric_Type = Integer32
_ZyStaticRouteMetric_Object = MibTableColumn
zyStaticRouteMetric = _ZyStaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 77, 1, 2, 1, 5),
    _ZyStaticRouteMetric_Type()
)
zyStaticRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyStaticRouteMetric.setStatus("current")
_ZyStaticRouteRowStatus_Type = RowStatus
_ZyStaticRouteRowStatus_Object = MibTableColumn
zyStaticRouteRowStatus = _ZyStaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 77, 1, 2, 1, 6),
    _ZyStaticRouteRowStatus_Type()
)
zyStaticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyStaticRouteRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-STATIC-ROUTE-MIB",
    **{"zyxelStaticRoute": zyxelStaticRoute,
       "zyxelStaticRouteSetup": zyxelStaticRouteSetup,
       "zyStaticRouteMaxNumberOfRoutes": zyStaticRouteMaxNumberOfRoutes,
       "zyxelStaticRouteTable": zyxelStaticRouteTable,
       "zyxelStaticRouteEntry": zyxelStaticRouteEntry,
       "zyStaticRouteName": zyStaticRouteName,
       "zyStaticRouteIpAddress": zyStaticRouteIpAddress,
       "zyStaticRouteSubnetMask": zyStaticRouteSubnetMask,
       "zyStaticRouteGateway": zyStaticRouteGateway,
       "zyStaticRouteMetric": zyStaticRouteMetric,
       "zyStaticRouteRowStatus": zyStaticRouteRowStatus}
)
