# SNMP MIB module (A3COM-HUAWEI-GRE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/3com_43/A3COM-HUAWEI-GRE-MIB.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 23:04:11 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

h3cGre = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 54)
)
if mibBuilder.loadTexts:
    h3cGre.setRevisions(
        ("2005-06-04 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cGreObjects_ObjectIdentity = ObjectIdentity
h3cGreObjects = _H3cGreObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 54, 1)
)
_H3cGreTable_Object = MibTable
h3cGreTable = _H3cGreTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 54, 1, 1)
)
if mibBuilder.loadTexts:
    h3cGreTable.setStatus("current")
_H3cGreEntry_Object = MibTableRow
h3cGreEntry = _H3cGreEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 54, 1, 1, 1)
)
h3cGreEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cGreEntry.setStatus("current")
_H3cGreKeyValue_Type = Unsigned32
_H3cGreKeyValue_Object = MibTableColumn
h3cGreKeyValue = _H3cGreKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 54, 1, 1, 1, 1),
    _H3cGreKeyValue_Type()
)
h3cGreKeyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cGreKeyValue.setStatus("current")


class _H3cGreKey_Type(Integer32):
    """Custom type h3cGreKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_H3cGreKey_Type.__name__ = "Integer32"
_H3cGreKey_Object = MibTableColumn
h3cGreKey = _H3cGreKey_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 54, 1, 1, 1, 2),
    _H3cGreKey_Type()
)
h3cGreKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cGreKey.setStatus("current")


class _H3cGreChecksum_Type(Integer32):
    """Custom type h3cGreChecksum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_H3cGreChecksum_Type.__name__ = "Integer32"
_H3cGreChecksum_Object = MibTableColumn
h3cGreChecksum = _H3cGreChecksum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 54, 1, 1, 1, 3),
    _H3cGreChecksum_Type()
)
h3cGreChecksum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cGreChecksum.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-GRE-MIB",
    **{"h3cGre": h3cGre,
       "h3cGreObjects": h3cGreObjects,
       "h3cGreTable": h3cGreTable,
       "h3cGreEntry": h3cGreEntry,
       "h3cGreKeyValue": h3cGreKeyValue,
       "h3cGreKey": h3cGreKey,
       "h3cGreChecksum": h3cGreChecksum}
)
