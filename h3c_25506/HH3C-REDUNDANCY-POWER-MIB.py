# SNMP MIB module (HH3C-REDUNDANCY-POWER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/h3c_25506/HH3C-REDUNDANCY-POWER-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 18:42:37 2025
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

(hh3cmlsr,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cmlsr")

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

hh3credundancyPower = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3credundancyPowerTable_Object = MibTable
hh3credundancyPowerTable = _Hh3credundancyPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 4, 1)
)
if mibBuilder.loadTexts:
    hh3credundancyPowerTable.setStatus("current")
_Hh3credundancyPowerEntry_Object = MibTableRow
hh3credundancyPowerEntry = _Hh3credundancyPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 4, 1, 1)
)
hh3credundancyPowerEntry.setIndexNames(
    (0, "HH3C-REDUNDANCY-POWER-MIB", "hh3credundancyPowerID"),
)
if mibBuilder.loadTexts:
    hh3credundancyPowerEntry.setStatus("current")
_Hh3credundancyPowerID_Type = Integer32
_Hh3credundancyPowerID_Object = MibTableColumn
hh3credundancyPowerID = _Hh3credundancyPowerID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 4, 1, 1, 1),
    _Hh3credundancyPowerID_Type()
)
hh3credundancyPowerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3credundancyPowerID.setStatus("current")


class _Hh3credundancyPowerStatus_Type(Integer32):
    """Custom type hh3credundancyPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("space", 1),
          ("normal", 2),
          ("fail", 3))
    )


_Hh3credundancyPowerStatus_Type.__name__ = "Integer32"
_Hh3credundancyPowerStatus_Object = MibTableColumn
hh3credundancyPowerStatus = _Hh3credundancyPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 4, 1, 1, 2),
    _Hh3credundancyPowerStatus_Type()
)
hh3credundancyPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3credundancyPowerStatus.setStatus("current")


class _Hh3credundancyPowerPreviousStatus_Type(Integer32):
    """Custom type hh3credundancyPowerPreviousStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("space", 1),
          ("normal", 2),
          ("fail", 3))
    )


_Hh3credundancyPowerPreviousStatus_Type.__name__ = "Integer32"
_Hh3credundancyPowerPreviousStatus_Object = MibTableColumn
hh3credundancyPowerPreviousStatus = _Hh3credundancyPowerPreviousStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 4, 1, 1, 3),
    _Hh3credundancyPowerPreviousStatus_Type()
)
hh3credundancyPowerPreviousStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3credundancyPowerPreviousStatus.setStatus("current")
_Hh3cpowerTraps_ObjectIdentity = ObjectIdentity
hh3cpowerTraps = _Hh3cpowerTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 4, 2)
)
_Hh3credundancyFan_ObjectIdentity = ObjectIdentity
hh3credundancyFan = _Hh3credundancyFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 5)
)
_Hh3credundancyFanTable_Object = MibTable
hh3credundancyFanTable = _Hh3credundancyFanTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 5, 1)
)
if mibBuilder.loadTexts:
    hh3credundancyFanTable.setStatus("current")
_Hh3credundancyFanEntry_Object = MibTableRow
hh3credundancyFanEntry = _Hh3credundancyFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 5, 1, 1)
)
hh3credundancyFanEntry.setIndexNames(
    (0, "HH3C-REDUNDANCY-POWER-MIB", "hh3credundancyFanID"),
)
if mibBuilder.loadTexts:
    hh3credundancyFanEntry.setStatus("current")
_Hh3credundancyFanID_Type = Integer32
_Hh3credundancyFanID_Object = MibTableColumn
hh3credundancyFanID = _Hh3credundancyFanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 5, 1, 1, 1),
    _Hh3credundancyFanID_Type()
)
hh3credundancyFanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3credundancyFanID.setStatus("current")


class _Hh3credundancyFanStatus_Type(Integer32):
    """Custom type hh3credundancyFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("fail", 2))
    )


_Hh3credundancyFanStatus_Type.__name__ = "Integer32"
_Hh3credundancyFanStatus_Object = MibTableColumn
hh3credundancyFanStatus = _Hh3credundancyFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 5, 1, 1, 2),
    _Hh3credundancyFanStatus_Type()
)
hh3credundancyFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3credundancyFanStatus.setStatus("current")
_Hh3cfanTraps_ObjectIdentity = ObjectIdentity
hh3cfanTraps = _Hh3cfanTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 5, 2)
)

# Managed Objects groups


# Notification objects

hh3cpowerStatusChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 4, 2, 1)
)
hh3cpowerStatusChangedTrap.setObjects(
      *(("HH3C-REDUNDANCY-POWER-MIB", "hh3credundancyPowerID"),
        ("HH3C-REDUNDANCY-POWER-MIB", "hh3credundancyPowerStatus"),
        ("HH3C-REDUNDANCY-POWER-MIB", "hh3credundancyPowerPreviousStatus"))
)
if mibBuilder.loadTexts:
    hh3cpowerStatusChangedTrap.setStatus(
        "current"
    )

hh3cfanStatusChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 5, 2, 1)
)
hh3cfanStatusChangedTrap.setObjects(
      *(("HH3C-REDUNDANCY-POWER-MIB", "hh3credundancyFanID"),
        ("HH3C-REDUNDANCY-POWER-MIB", "hh3credundancyFanStatus"))
)
if mibBuilder.loadTexts:
    hh3cfanStatusChangedTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-REDUNDANCY-POWER-MIB",
    **{"hh3credundancyPower": hh3credundancyPower,
       "hh3credundancyPowerTable": hh3credundancyPowerTable,
       "hh3credundancyPowerEntry": hh3credundancyPowerEntry,
       "hh3credundancyPowerID": hh3credundancyPowerID,
       "hh3credundancyPowerStatus": hh3credundancyPowerStatus,
       "hh3credundancyPowerPreviousStatus": hh3credundancyPowerPreviousStatus,
       "hh3cpowerTraps": hh3cpowerTraps,
       "hh3cpowerStatusChangedTrap": hh3cpowerStatusChangedTrap,
       "hh3credundancyFan": hh3credundancyFan,
       "hh3credundancyFanTable": hh3credundancyFanTable,
       "hh3credundancyFanEntry": hh3credundancyFanEntry,
       "hh3credundancyFanID": hh3credundancyFanID,
       "hh3credundancyFanStatus": hh3credundancyFanStatus,
       "hh3cfanTraps": hh3cfanTraps,
       "hh3cfanStatusChangedTrap": hh3cfanStatusChangedTrap}
)
