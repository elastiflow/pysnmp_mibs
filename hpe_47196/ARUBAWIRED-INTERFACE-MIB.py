# SNMP MIB module (ARUBAWIRED-INTERFACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/hpe_47196/ARUBAWIRED-INTERFACE-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 22:01:04 2025
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

(wndFeatures,) = mibBuilder.importSymbols(
    "ARUBAWIRED-NETWORKING-OID",
    "wndFeatures")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

arubaWiredInterfaceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24)
)
if mibBuilder.loadTexts:
    arubaWiredInterfaceMIB.setRevisions(
        ("2021-11-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ArubaWiredInterfaceSettings_ObjectIdentity = ObjectIdentity
arubaWiredInterfaceSettings = _ArubaWiredInterfaceSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1)
)
_ArubaWiredInterfaceTable_Object = MibTable
arubaWiredInterfaceTable = _ArubaWiredInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1, 1)
)
if mibBuilder.loadTexts:
    arubaWiredInterfaceTable.setStatus("current")
_ArubaWiredInterfaceEntry_Object = MibTableRow
arubaWiredInterfaceEntry = _ArubaWiredInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1, 1, 1)
)
arubaWiredInterfaceEntry.setIndexNames(
    (0, "ARUBAWIRED-INTERFACE-MIB", "arubaWiredInterfaceIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredInterfaceEntry.setStatus("current")
_ArubaWiredInterfaceIndex_Type = InterfaceIndex
_ArubaWiredInterfaceIndex_Object = MibTableColumn
arubaWiredInterfaceIndex = _ArubaWiredInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1, 1, 1, 1),
    _ArubaWiredInterfaceIndex_Type()
)
arubaWiredInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredInterfaceIndex.setStatus("current")


class _ArubaWiredInterfaceAutoneg_Type(Integer32):
    """Custom type arubaWiredInterfaceAutoneg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_ArubaWiredInterfaceAutoneg_Type.__name__ = "Integer32"
_ArubaWiredInterfaceAutoneg_Object = MibTableColumn
arubaWiredInterfaceAutoneg = _ArubaWiredInterfaceAutoneg_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1, 1, 1, 2),
    _ArubaWiredInterfaceAutoneg_Type()
)
arubaWiredInterfaceAutoneg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredInterfaceAutoneg.setStatus("current")


class _ArubaWiredInterfaceDuplex_Type(Integer32):
    """Custom type arubaWiredInterfaceDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2))
    )


_ArubaWiredInterfaceDuplex_Type.__name__ = "Integer32"
_ArubaWiredInterfaceDuplex_Object = MibTableColumn
arubaWiredInterfaceDuplex = _ArubaWiredInterfaceDuplex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1, 1, 1, 3),
    _ArubaWiredInterfaceDuplex_Type()
)
arubaWiredInterfaceDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredInterfaceDuplex.setStatus("current")


class _ArubaWiredInterfaceSpeeds_Type(Bits):
    """Custom type arubaWiredInterfaceSpeeds based on Bits"""
    namedValues = NamedValues(
        *(("speed10M", 0),
          ("speed100M", 1),
          ("speed1G", 2),
          ("speed2p5G", 3),
          ("speed5G", 4),
          ("speed10G", 5),
          ("speed25G", 6),
          ("speed40G", 7),
          ("speed50G", 8),
          ("speed100G", 9),
          ("speed200G", 10),
          ("speed400G", 11),
          ("speed800G", 12))
    )

_ArubaWiredInterfaceSpeeds_Type.__name__ = "Bits"
_ArubaWiredInterfaceSpeeds_Object = MibTableColumn
arubaWiredInterfaceSpeeds = _ArubaWiredInterfaceSpeeds_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 1, 1, 1, 4),
    _ArubaWiredInterfaceSpeeds_Type()
)
arubaWiredInterfaceSpeeds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredInterfaceSpeeds.setStatus("current")
_ArubaWiredInterfaceConformance_ObjectIdentity = ObjectIdentity
arubaWiredInterfaceConformance = _ArubaWiredInterfaceConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 2)
)
_ArubaWiredInterfaceGroups_ObjectIdentity = ObjectIdentity
arubaWiredInterfaceGroups = _ArubaWiredInterfaceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 2, 1)
)
_ArubaWiredInterfaceCompliances_ObjectIdentity = ObjectIdentity
arubaWiredInterfaceCompliances = _ArubaWiredInterfaceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 2, 2)
)

# Managed Objects groups

arubaWiredInterfaceConfig = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 2, 1, 1)
)
arubaWiredInterfaceConfig.setObjects(
      *(("ARUBAWIRED-INTERFACE-MIB", "arubaWiredInterfaceAutoneg"),
        ("ARUBAWIRED-INTERFACE-MIB", "arubaWiredInterfaceDuplex"),
        ("ARUBAWIRED-INTERFACE-MIB", "arubaWiredInterfaceSpeeds"))
)
if mibBuilder.loadTexts:
    arubaWiredInterfaceConfig.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

arubaWiredInterfaceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 24, 2, 2, 1)
)
arubaWiredInterfaceCompliance.setObjects(
    ("ARUBAWIRED-INTERFACE-MIB", "arubaWiredInterfaceConfig")
)
if mibBuilder.loadTexts:
    arubaWiredInterfaceCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBAWIRED-INTERFACE-MIB",
    **{"arubaWiredInterfaceMIB": arubaWiredInterfaceMIB,
       "arubaWiredInterfaceSettings": arubaWiredInterfaceSettings,
       "arubaWiredInterfaceTable": arubaWiredInterfaceTable,
       "arubaWiredInterfaceEntry": arubaWiredInterfaceEntry,
       "arubaWiredInterfaceIndex": arubaWiredInterfaceIndex,
       "arubaWiredInterfaceAutoneg": arubaWiredInterfaceAutoneg,
       "arubaWiredInterfaceDuplex": arubaWiredInterfaceDuplex,
       "arubaWiredInterfaceSpeeds": arubaWiredInterfaceSpeeds,
       "arubaWiredInterfaceConformance": arubaWiredInterfaceConformance,
       "arubaWiredInterfaceGroups": arubaWiredInterfaceGroups,
       "arubaWiredInterfaceConfig": arubaWiredInterfaceConfig,
       "arubaWiredInterfaceCompliances": arubaWiredInterfaceCompliances,
       "arubaWiredInterfaceCompliance": arubaWiredInterfaceCompliance}
)
