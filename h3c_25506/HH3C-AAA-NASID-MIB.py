# SNMP MIB module (HH3C-AAA-NASID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/h3c_25506/HH3C-AAA-NASID-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 18:27:38 2025
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

hh3cAAANasId = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 114)
)
if mibBuilder.loadTexts:
    hh3cAAANasId.setRevisions(
        ("2011-03-09 09:45",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cAAANasIdObjects_ObjectIdentity = ObjectIdentity
hh3cAAANasIdObjects = _Hh3cAAANasIdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 114, 1)
)
_Hh3cAAANasIdTable_Object = MibTable
hh3cAAANasIdTable = _Hh3cAAANasIdTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 114, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cAAANasIdTable.setStatus("current")
_Hh3cAAANasIdEntry_Object = MibTableRow
hh3cAAANasIdEntry = _Hh3cAAANasIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 114, 1, 1, 1)
)
hh3cAAANasIdEntry.setIndexNames(
    (0, "HH3C-AAA-NASID-MIB", "hh3cAAANasIdName"),
)
if mibBuilder.loadTexts:
    hh3cAAANasIdEntry.setStatus("current")


class _Hh3cAAANasIdName_Type(OctetString):
    """Custom type hh3cAAANasIdName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cAAANasIdName_Type.__name__ = "OctetString"
_Hh3cAAANasIdName_Object = MibTableColumn
hh3cAAANasIdName = _Hh3cAAANasIdName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 114, 1, 1, 1, 1),
    _Hh3cAAANasIdName_Type()
)
hh3cAAANasIdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAAANasIdName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-AAA-NASID-MIB",
    **{"hh3cAAANasId": hh3cAAANasId,
       "hh3cAAANasIdObjects": hh3cAAANasIdObjects,
       "hh3cAAANasIdTable": hh3cAAANasIdTable,
       "hh3cAAANasIdEntry": hh3cAAANasIdEntry,
       "hh3cAAANasIdName": hh3cAAANasIdName}
)
