# SNMP MIB module (ARUBAWIRED-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/hpe_47196/ARUBAWIRED-CHASSIS-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 21:59:27 2025
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

arubaWiredChassisMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11)
)
if mibBuilder.loadTexts:
    arubaWiredChassisMIB.setRevisions(
        ("2023-06-27 00:00",
         "2023-06-06 00:00",
         "2021-01-11 00:00",
         "2020-02-13 00:00",
         "2020-01-07 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ArubaWiredPowerSupply_ObjectIdentity = ObjectIdentity
arubaWiredPowerSupply = _ArubaWiredPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 2)
)
_ArubaWiredTempSensor_ObjectIdentity = ObjectIdentity
arubaWiredTempSensor = _ArubaWiredTempSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 3)
)
_ArubaWiredFanTray_ObjectIdentity = ObjectIdentity
arubaWiredFanTray = _ArubaWiredFanTray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 4)
)
_ArubaWiredFan_ObjectIdentity = ObjectIdentity
arubaWiredFan = _ArubaWiredFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 5)
)
_ArubaWiredModule_ObjectIdentity = ObjectIdentity
arubaWiredModule = _ArubaWiredModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 6)
)
_ArubaWiredLedLocator_ObjectIdentity = ObjectIdentity
arubaWiredLedLocator = _ArubaWiredLedLocator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 7)
)
_ArubaWiredPowerStat_ObjectIdentity = ObjectIdentity
arubaWiredPowerStat = _ArubaWiredPowerStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 11, 8)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBAWIRED-CHASSIS-MIB",
    **{"arubaWiredChassisMIB": arubaWiredChassisMIB,
       "arubaWiredPowerSupply": arubaWiredPowerSupply,
       "arubaWiredTempSensor": arubaWiredTempSensor,
       "arubaWiredFanTray": arubaWiredFanTray,
       "arubaWiredFan": arubaWiredFan,
       "arubaWiredModule": arubaWiredModule,
       "arubaWiredLedLocator": arubaWiredLedLocator,
       "arubaWiredPowerStat": arubaWiredPowerStat}
)
