# SNMP MIB module (A3COM-HUAWEI-AAA-NASID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/3com_43/A3COM-HUAWEI-AAA-NASID-MIB.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 23:05:02 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

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

h3cAAANasId = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 114)
)
if mibBuilder.loadTexts:
    h3cAAANasId.setRevisions(
        ("2011-03-09 09:45",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cAAANasIdObjects_ObjectIdentity = ObjectIdentity
h3cAAANasIdObjects = _H3cAAANasIdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 114, 1)
)
_H3cAAANasIdTable_Object = MibTable
h3cAAANasIdTable = _H3cAAANasIdTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 114, 1, 1)
)
if mibBuilder.loadTexts:
    h3cAAANasIdTable.setStatus("current")
_H3cAAANasIdEntry_Object = MibTableRow
h3cAAANasIdEntry = _H3cAAANasIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 114, 1, 1, 1)
)
h3cAAANasIdEntry.setIndexNames(
    (0, "A3COM-HUAWEI-AAA-NASID-MIB", "h3cAAANasIdName"),
)
if mibBuilder.loadTexts:
    h3cAAANasIdEntry.setStatus("current")


class _H3cAAANasIdName_Type(OctetString):
    """Custom type h3cAAANasIdName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_H3cAAANasIdName_Type.__name__ = "OctetString"
_H3cAAANasIdName_Object = MibTableColumn
h3cAAANasIdName = _H3cAAANasIdName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 114, 1, 1, 1, 1),
    _H3cAAANasIdName_Type()
)
h3cAAANasIdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAAANasIdName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-AAA-NASID-MIB",
    **{"h3cAAANasId": h3cAAANasId,
       "h3cAAANasIdObjects": h3cAAANasIdObjects,
       "h3cAAANasIdTable": h3cAAANasIdTable,
       "h3cAAANasIdEntry": h3cAAANasIdEntry,
       "h3cAAANasIdName": h3cAAANasIdName}
)
