# SNMP MIB module (ZYXEL-PRIVATE-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-PRIVATE-VLAN-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 08:35:51 2025
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

zyxelPrivateVlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 68)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelPrivateVlanSetup_ObjectIdentity = ObjectIdentity
zyxelPrivateVlanSetup = _ZyxelPrivateVlanSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 68, 1)
)
_ZyxelPrivateVlanTable_Object = MibTable
zyxelPrivateVlanTable = _ZyxelPrivateVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 68, 1, 1)
)
if mibBuilder.loadTexts:
    zyxelPrivateVlanTable.setStatus("current")
_ZyxelPrivateVlanEntry_Object = MibTableRow
zyxelPrivateVlanEntry = _ZyxelPrivateVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 68, 1, 1, 1)
)
zyxelPrivateVlanEntry.setIndexNames(
    (0, "ZYXEL-PRIVATE-VLAN-MIB", "zyPrivateVlanType"),
)
if mibBuilder.loadTexts:
    zyxelPrivateVlanEntry.setStatus("current")


class _ZyPrivateVlanType_Type(Integer32):
    """Custom type zyPrivateVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("primary", 1),
          ("isolated", 2),
          ("community", 3))
    )


_ZyPrivateVlanType_Type.__name__ = "Integer32"
_ZyPrivateVlanType_Object = MibTableColumn
zyPrivateVlanType = _ZyPrivateVlanType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 68, 1, 1, 1, 1),
    _ZyPrivateVlanType_Type()
)
zyPrivateVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPrivateVlanType.setStatus("current")


class _ZyPrivateVlanAssociatedVlanMap1k_Type(OctetString):
    """Custom type zyPrivateVlanAssociatedVlanMap1k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZyPrivateVlanAssociatedVlanMap1k_Type.__name__ = "OctetString"
_ZyPrivateVlanAssociatedVlanMap1k_Object = MibTableColumn
zyPrivateVlanAssociatedVlanMap1k = _ZyPrivateVlanAssociatedVlanMap1k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 68, 1, 1, 1, 2),
    _ZyPrivateVlanAssociatedVlanMap1k_Type()
)
zyPrivateVlanAssociatedVlanMap1k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPrivateVlanAssociatedVlanMap1k.setStatus("current")


class _ZyPrivateVlanAssociatedVlanMap2k_Type(OctetString):
    """Custom type zyPrivateVlanAssociatedVlanMap2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZyPrivateVlanAssociatedVlanMap2k_Type.__name__ = "OctetString"
_ZyPrivateVlanAssociatedVlanMap2k_Object = MibTableColumn
zyPrivateVlanAssociatedVlanMap2k = _ZyPrivateVlanAssociatedVlanMap2k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 68, 1, 1, 1, 3),
    _ZyPrivateVlanAssociatedVlanMap2k_Type()
)
zyPrivateVlanAssociatedVlanMap2k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPrivateVlanAssociatedVlanMap2k.setStatus("current")


class _ZyPrivateVlanAssociatedVlanMap3k_Type(OctetString):
    """Custom type zyPrivateVlanAssociatedVlanMap3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZyPrivateVlanAssociatedVlanMap3k_Type.__name__ = "OctetString"
_ZyPrivateVlanAssociatedVlanMap3k_Object = MibTableColumn
zyPrivateVlanAssociatedVlanMap3k = _ZyPrivateVlanAssociatedVlanMap3k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 68, 1, 1, 1, 4),
    _ZyPrivateVlanAssociatedVlanMap3k_Type()
)
zyPrivateVlanAssociatedVlanMap3k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPrivateVlanAssociatedVlanMap3k.setStatus("current")


class _ZyPrivateVlanAssociatedVlanMap4k_Type(OctetString):
    """Custom type zyPrivateVlanAssociatedVlanMap4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZyPrivateVlanAssociatedVlanMap4k_Type.__name__ = "OctetString"
_ZyPrivateVlanAssociatedVlanMap4k_Object = MibTableColumn
zyPrivateVlanAssociatedVlanMap4k = _ZyPrivateVlanAssociatedVlanMap4k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 68, 1, 1, 1, 5),
    _ZyPrivateVlanAssociatedVlanMap4k_Type()
)
zyPrivateVlanAssociatedVlanMap4k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyPrivateVlanAssociatedVlanMap4k.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-PRIVATE-VLAN-MIB",
    **{"zyxelPrivateVlan": zyxelPrivateVlan,
       "zyxelPrivateVlanSetup": zyxelPrivateVlanSetup,
       "zyxelPrivateVlanTable": zyxelPrivateVlanTable,
       "zyxelPrivateVlanEntry": zyxelPrivateVlanEntry,
       "zyPrivateVlanType": zyPrivateVlanType,
       "zyPrivateVlanAssociatedVlanMap1k": zyPrivateVlanAssociatedVlanMap1k,
       "zyPrivateVlanAssociatedVlanMap2k": zyPrivateVlanAssociatedVlanMap2k,
       "zyPrivateVlanAssociatedVlanMap3k": zyPrivateVlanAssociatedVlanMap3k,
       "zyPrivateVlanAssociatedVlanMap4k": zyPrivateVlanAssociatedVlanMap4k}
)
