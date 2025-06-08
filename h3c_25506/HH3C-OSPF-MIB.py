# SNMP MIB module (HH3C-OSPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/h3c_25506/HH3C-OSPF-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 18:41:55 2025
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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


# MODULE-IDENTITY

hh3cOspf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 161)
)
if mibBuilder.loadTexts:
    hh3cOspf.setRevisions(
        ("2014-12-17 17:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cOspfNetworkTable_Object = MibTable
hh3cOspfNetworkTable = _Hh3cOspfNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 161, 1)
)
if mibBuilder.loadTexts:
    hh3cOspfNetworkTable.setStatus("current")
_Hh3cOspfNetworkEntry_Object = MibTableRow
hh3cOspfNetworkEntry = _Hh3cOspfNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 161, 1, 1)
)
hh3cOspfNetworkEntry.setIndexNames(
    (0, "HH3C-OSPF-MIB", "hh3cOspfProcessId"),
    (0, "HH3C-OSPF-MIB", "hh3cOspfAreaId"),
    (0, "HH3C-OSPF-MIB", "hh3cOspfNetworkIpAddr"),
)
if mibBuilder.loadTexts:
    hh3cOspfNetworkEntry.setStatus("current")


class _Hh3cOspfProcessId_Type(Integer32):
    """Custom type hh3cOspfProcessId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cOspfProcessId_Type.__name__ = "Integer32"
_Hh3cOspfProcessId_Object = MibTableColumn
hh3cOspfProcessId = _Hh3cOspfProcessId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 161, 1, 1, 1),
    _Hh3cOspfProcessId_Type()
)
hh3cOspfProcessId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cOspfProcessId.setStatus("current")
_Hh3cOspfAreaId_Type = IpAddress
_Hh3cOspfAreaId_Object = MibTableColumn
hh3cOspfAreaId = _Hh3cOspfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 161, 1, 1, 2),
    _Hh3cOspfAreaId_Type()
)
hh3cOspfAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cOspfAreaId.setStatus("current")
_Hh3cOspfNetworkIpAddr_Type = IpAddress
_Hh3cOspfNetworkIpAddr_Object = MibTableColumn
hh3cOspfNetworkIpAddr = _Hh3cOspfNetworkIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 161, 1, 1, 3),
    _Hh3cOspfNetworkIpAddr_Type()
)
hh3cOspfNetworkIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cOspfNetworkIpAddr.setStatus("current")
_Hh3cOspfNetworkIpMask_Type = IpAddress
_Hh3cOspfNetworkIpMask_Object = MibTableColumn
hh3cOspfNetworkIpMask = _Hh3cOspfNetworkIpMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 161, 1, 1, 4),
    _Hh3cOspfNetworkIpMask_Type()
)
hh3cOspfNetworkIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cOspfNetworkIpMask.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-OSPF-MIB",
    **{"hh3cOspf": hh3cOspf,
       "hh3cOspfNetworkTable": hh3cOspfNetworkTable,
       "hh3cOspfNetworkEntry": hh3cOspfNetworkEntry,
       "hh3cOspfProcessId": hh3cOspfProcessId,
       "hh3cOspfAreaId": hh3cOspfAreaId,
       "hh3cOspfNetworkIpAddr": hh3cOspfNetworkIpAddr,
       "hh3cOspfNetworkIpMask": hh3cOspfNetworkIpMask}
)
