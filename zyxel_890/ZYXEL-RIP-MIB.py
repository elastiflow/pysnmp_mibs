# SNMP MIB module (ZYXEL-RIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-RIP-MIB.mib
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

(zyRouteDomainIpAddress,
 zyRouteDomainIpMaskBits) = mibBuilder.importSymbols(
    "ZYXEL-IP-FORWARD-MIB",
    "zyRouteDomainIpAddress",
    "zyRouteDomainIpMaskBits")


# MODULE-IDENTITY

zyxelRip = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 74)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelRipSetup_ObjectIdentity = ObjectIdentity
zyxelRipSetup = _ZyxelRipSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 74, 1)
)
_ZyRipState_Type = EnabledStatus
_ZyRipState_Object = MibScalar
zyRipState = _ZyRipState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 74, 1, 1),
    _ZyRipState_Type()
)
zyRipState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyRipState.setStatus("current")
_ZyRipDistance_Type = Integer32
_ZyRipDistance_Object = MibScalar
zyRipDistance = _ZyRipDistance_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 74, 1, 2),
    _ZyRipDistance_Type()
)
zyRipDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyRipDistance.setStatus("current")
_ZyxelRipRouteDomainTable_Object = MibTable
zyxelRipRouteDomainTable = _ZyxelRipRouteDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 74, 1, 3)
)
if mibBuilder.loadTexts:
    zyxelRipRouteDomainTable.setStatus("current")
_ZyxelRipRouteDomainEntry_Object = MibTableRow
zyxelRipRouteDomainEntry = _ZyxelRipRouteDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 74, 1, 3, 1)
)
zyxelRipRouteDomainEntry.setIndexNames(
    (0, "ZYXEL-IP-FORWARD-MIB", "zyRouteDomainIpAddress"),
    (0, "ZYXEL-IP-FORWARD-MIB", "zyRouteDomainIpMaskBits"),
)
if mibBuilder.loadTexts:
    zyxelRipRouteDomainEntry.setStatus("current")


class _ZyRipRouteDomainDirection_Type(Integer32):
    """Custom type zyRipRouteDomainDirection based on Integer32"""
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
        *(("none", 0),
          ("outgoing", 1),
          ("incoming", 2),
          ("both", 3))
    )


_ZyRipRouteDomainDirection_Type.__name__ = "Integer32"
_ZyRipRouteDomainDirection_Object = MibTableColumn
zyRipRouteDomainDirection = _ZyRipRouteDomainDirection_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 74, 1, 3, 1, 1),
    _ZyRipRouteDomainDirection_Type()
)
zyRipRouteDomainDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyRipRouteDomainDirection.setStatus("current")


class _ZyRipRouteDomainVersion_Type(Integer32):
    """Custom type zyRipRouteDomainVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 0),
          ("v2b", 1),
          ("v2m", 2))
    )


_ZyRipRouteDomainVersion_Type.__name__ = "Integer32"
_ZyRipRouteDomainVersion_Object = MibTableColumn
zyRipRouteDomainVersion = _ZyRipRouteDomainVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 74, 1, 3, 1, 2),
    _ZyRipRouteDomainVersion_Type()
)
zyRipRouteDomainVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyRipRouteDomainVersion.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-RIP-MIB",
    **{"zyxelRip": zyxelRip,
       "zyxelRipSetup": zyxelRipSetup,
       "zyRipState": zyRipState,
       "zyRipDistance": zyRipDistance,
       "zyxelRipRouteDomainTable": zyxelRipRouteDomainTable,
       "zyxelRipRouteDomainEntry": zyxelRipRouteDomainEntry,
       "zyRipRouteDomainDirection": zyRipRouteDomainDirection,
       "zyRipRouteDomainVersion": zyRipRouteDomainVersion}
)
