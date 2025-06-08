# SNMP MIB module (Giax-nodeInfo-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/giax_48671/Giax-nodeInfo-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 23:14:41 2025
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

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Giax_ObjectIdentity = ObjectIdentity
giax = _Giax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48671)
)
_Hfc_ObjectIdentity = ObjectIdentity
hfc = _Hfc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48671, 2)
)
_Hphy_ObjectIdentity = ObjectIdentity
hphy = _Hphy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48671, 2, 2)
)
_HphyPorts_Type = Integer32
_HphyPorts_Object = MibScalar
hphyPorts = _HphyPorts_Object(
    (1, 3, 6, 1, 4, 1, 48671, 2, 2, 1),
    _HphyPorts_Type()
)
hphyPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hphyPorts.setStatus("mandatory")
_HphyTable_Object = MibTable
hphyTable = _HphyTable_Object(
    (1, 3, 6, 1, 4, 1, 48671, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hphyTable.setStatus("mandatory")
_HphyEntry_Object = MibTableRow
hphyEntry = _HphyEntry_Object(
    (1, 3, 6, 1, 4, 1, 48671, 2, 2, 2, 1)
)
hphyEntry.setIndexNames(
    (0, "Giax-nodeInfo-MIB", "hphyPort"),
)
if mibBuilder.loadTexts:
    hphyEntry.setStatus("mandatory")


class _HphyPort_Type(Integer32):
    """Custom type hphyPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_HphyPort_Type.__name__ = "Integer32"
_HphyPort_Object = MibTableColumn
hphyPort = _HphyPort_Object(
    (1, 3, 6, 1, 4, 1, 48671, 2, 2, 2, 1, 1),
    _HphyPort_Type()
)
hphyPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hphyPort.setStatus("mandatory")
_HphyName_Type = DisplayString
_HphyName_Object = MibTableColumn
hphyName = _HphyName_Object(
    (1, 3, 6, 1, 4, 1, 48671, 2, 2, 2, 1, 2),
    _HphyName_Type()
)
hphyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hphyName.setStatus("mandatory")
_HphyDescr_Type = DisplayString
_HphyDescr_Object = MibTableColumn
hphyDescr = _HphyDescr_Object(
    (1, 3, 6, 1, 4, 1, 48671, 2, 2, 2, 1, 3),
    _HphyDescr_Type()
)
hphyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hphyDescr.setStatus("mandatory")
_Phy10g_ObjectIdentity = ObjectIdentity
phy10g = _Phy10g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48671, 2, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Giax-nodeInfo-MIB",
    **{"giax": giax,
       "hfc": hfc,
       "hphy": hphy,
       "hphyPorts": hphyPorts,
       "hphyTable": hphyTable,
       "hphyEntry": hphyEntry,
       "hphyPort": hphyPort,
       "hphyName": hphyName,
       "hphyDescr": hphyDescr,
       "phy10g": phy10g}
)
