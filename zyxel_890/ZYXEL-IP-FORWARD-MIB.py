# SNMP MIB module (ZYXEL-IP-FORWARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-IP-FORWARD-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 08:46:21 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelIpForward = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 32)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelRouteDomainStatus_ObjectIdentity = ObjectIdentity
zyxelRouteDomainStatus = _ZyxelRouteDomainStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 32, 1)
)
_ZyxelRouteDomainTable_Object = MibTable
zyxelRouteDomainTable = _ZyxelRouteDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 32, 1, 1)
)
if mibBuilder.loadTexts:
    zyxelRouteDomainTable.setStatus("current")
_ZyxelRouteDomainEntry_Object = MibTableRow
zyxelRouteDomainEntry = _ZyxelRouteDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 32, 1, 1, 1)
)
zyxelRouteDomainEntry.setIndexNames(
    (0, "ZYXEL-IP-FORWARD-MIB", "zyRouteDomainIpAddress"),
    (0, "ZYXEL-IP-FORWARD-MIB", "zyRouteDomainIpMaskBits"),
)
if mibBuilder.loadTexts:
    zyxelRouteDomainEntry.setStatus("current")
_ZyRouteDomainIpAddress_Type = IpAddress
_ZyRouteDomainIpAddress_Object = MibTableColumn
zyRouteDomainIpAddress = _ZyRouteDomainIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 32, 1, 1, 1, 1),
    _ZyRouteDomainIpAddress_Type()
)
zyRouteDomainIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyRouteDomainIpAddress.setStatus("current")
_ZyRouteDomainIpMaskBits_Type = Integer32
_ZyRouteDomainIpMaskBits_Object = MibTableColumn
zyRouteDomainIpMaskBits = _ZyRouteDomainIpMaskBits_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 32, 1, 1, 1, 2),
    _ZyRouteDomainIpMaskBits_Type()
)
zyRouteDomainIpMaskBits.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyRouteDomainIpMaskBits.setStatus("current")
_ZyRouteDomainVid_Type = Integer32
_ZyRouteDomainVid_Object = MibTableColumn
zyRouteDomainVid = _ZyRouteDomainVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 32, 1, 1, 1, 3),
    _ZyRouteDomainVid_Type()
)
zyRouteDomainVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyRouteDomainVid.setStatus("current")
_ZyxelHostStatus_ObjectIdentity = ObjectIdentity
zyxelHostStatus = _ZyxelHostStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 32, 2)
)
_ZyxelHostTable_Object = MibTable
zyxelHostTable = _ZyxelHostTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 32, 2, 1)
)
if mibBuilder.loadTexts:
    zyxelHostTable.setStatus("current")
_ZyxelHostEntry_Object = MibTableRow
zyxelHostEntry = _ZyxelHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 32, 2, 1, 1)
)
zyxelHostEntry.setIndexNames(
    (0, "ZYXEL-IP-FORWARD-MIB", "zyHostIpAddress"),
    (0, "ZYXEL-IP-FORWARD-MIB", "zyHostVid"),
)
if mibBuilder.loadTexts:
    zyxelHostEntry.setStatus("current")
_ZyHostIpAddress_Type = IpAddress
_ZyHostIpAddress_Object = MibTableColumn
zyHostIpAddress = _ZyHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 32, 2, 1, 1, 1),
    _ZyHostIpAddress_Type()
)
zyHostIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyHostIpAddress.setStatus("current")
_ZyHostVid_Type = Integer32
_ZyHostVid_Object = MibTableColumn
zyHostVid = _ZyHostVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 32, 2, 1, 1, 2),
    _ZyHostVid_Type()
)
zyHostVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyHostVid.setStatus("current")
_ZyHostPort_Type = DisplayString
_ZyHostPort_Object = MibTableColumn
zyHostPort = _ZyHostPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 32, 2, 1, 1, 3),
    _ZyHostPort_Type()
)
zyHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyHostPort.setStatus("current")


class _ZyHostType_Type(Integer32):
    """Custom type zyHostType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_ZyHostType_Type.__name__ = "Integer32"
_ZyHostType_Object = MibTableColumn
zyHostType = _ZyHostType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 32, 2, 1, 1, 4),
    _ZyHostType_Type()
)
zyHostType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyHostType.setStatus("current")
_ZyxelIpRouteStatus_ObjectIdentity = ObjectIdentity
zyxelIpRouteStatus = _ZyxelIpRouteStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 32, 3)
)
_ZyxelIpRouteTable_Object = MibTable
zyxelIpRouteTable = _ZyxelIpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 32, 3, 1)
)
if mibBuilder.loadTexts:
    zyxelIpRouteTable.setStatus("current")
_ZyxelIpRouteEntry_Object = MibTableRow
zyxelIpRouteEntry = _ZyxelIpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 32, 3, 1, 1)
)
zyxelIpRouteEntry.setIndexNames(
    (0, "ZYXEL-IP-FORWARD-MIB", "zyIpRouteDestinationIpAddress"),
    (0, "ZYXEL-IP-FORWARD-MIB", "zyIpRouteDestinationMaskBits"),
    (0, "ZYXEL-IP-FORWARD-MIB", "zyIpRouteGateway"),
)
if mibBuilder.loadTexts:
    zyxelIpRouteEntry.setStatus("current")
_ZyIpRouteDestinationIpAddress_Type = IpAddress
_ZyIpRouteDestinationIpAddress_Object = MibTableColumn
zyIpRouteDestinationIpAddress = _ZyIpRouteDestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 32, 3, 1, 1, 1),
    _ZyIpRouteDestinationIpAddress_Type()
)
zyIpRouteDestinationIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIpRouteDestinationIpAddress.setStatus("current")
_ZyIpRouteDestinationMaskBits_Type = Integer32
_ZyIpRouteDestinationMaskBits_Object = MibTableColumn
zyIpRouteDestinationMaskBits = _ZyIpRouteDestinationMaskBits_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 32, 3, 1, 1, 2),
    _ZyIpRouteDestinationMaskBits_Type()
)
zyIpRouteDestinationMaskBits.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIpRouteDestinationMaskBits.setStatus("current")
_ZyIpRouteGateway_Type = IpAddress
_ZyIpRouteGateway_Object = MibTableColumn
zyIpRouteGateway = _ZyIpRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 32, 3, 1, 1, 3),
    _ZyIpRouteGateway_Type()
)
zyIpRouteGateway.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIpRouteGateway.setStatus("current")
_ZyIpRouteIf_Type = IpAddress
_ZyIpRouteIf_Object = MibTableColumn
zyIpRouteIf = _ZyIpRouteIf_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 32, 3, 1, 1, 4),
    _ZyIpRouteIf_Type()
)
zyIpRouteIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIpRouteIf.setStatus("current")
_ZyIpRouteMetric_Type = Integer32
_ZyIpRouteMetric_Object = MibTableColumn
zyIpRouteMetric = _ZyIpRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 32, 3, 1, 1, 5),
    _ZyIpRouteMetric_Type()
)
zyIpRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIpRouteMetric.setStatus("current")


class _ZyIpRouteType_Type(Integer32):
    """Custom type zyIpRouteType based on Integer32"""
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
        *(("rip", 1),
          ("bgp", 2),
          ("ospf", 3),
          ("static", 4))
    )


_ZyIpRouteType_Type.__name__ = "Integer32"
_ZyIpRouteType_Object = MibTableColumn
zyIpRouteType = _ZyIpRouteType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 32, 3, 1, 1, 6),
    _ZyIpRouteType_Type()
)
zyIpRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIpRouteType.setStatus("current")
_ZyIpRouteUptime_Type = TimeTicks
_ZyIpRouteUptime_Object = MibTableColumn
zyIpRouteUptime = _ZyIpRouteUptime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 32, 3, 1, 1, 7),
    _ZyIpRouteUptime_Type()
)
zyIpRouteUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIpRouteUptime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-IP-FORWARD-MIB",
    **{"zyxelIpForward": zyxelIpForward,
       "zyxelRouteDomainStatus": zyxelRouteDomainStatus,
       "zyxelRouteDomainTable": zyxelRouteDomainTable,
       "zyxelRouteDomainEntry": zyxelRouteDomainEntry,
       "zyRouteDomainIpAddress": zyRouteDomainIpAddress,
       "zyRouteDomainIpMaskBits": zyRouteDomainIpMaskBits,
       "zyRouteDomainVid": zyRouteDomainVid,
       "zyxelHostStatus": zyxelHostStatus,
       "zyxelHostTable": zyxelHostTable,
       "zyxelHostEntry": zyxelHostEntry,
       "zyHostIpAddress": zyHostIpAddress,
       "zyHostVid": zyHostVid,
       "zyHostPort": zyHostPort,
       "zyHostType": zyHostType,
       "zyxelIpRouteStatus": zyxelIpRouteStatus,
       "zyxelIpRouteTable": zyxelIpRouteTable,
       "zyxelIpRouteEntry": zyxelIpRouteEntry,
       "zyIpRouteDestinationIpAddress": zyIpRouteDestinationIpAddress,
       "zyIpRouteDestinationMaskBits": zyIpRouteDestinationMaskBits,
       "zyIpRouteGateway": zyIpRouteGateway,
       "zyIpRouteIf": zyIpRouteIf,
       "zyIpRouteMetric": zyIpRouteMetric,
       "zyIpRouteType": zyIpRouteType,
       "zyIpRouteUptime": zyIpRouteUptime}
)
