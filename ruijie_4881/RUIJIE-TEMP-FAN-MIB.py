# SNMP MIB module (RUIJIE-TEMP-FAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-TEMP-FAN-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:59:06 2025
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

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(ruijieSystemTemperatureCurrent,) = mibBuilder.importSymbols(
    "RUIJIE-SYSTEM-MIB",
    "ruijieSystemTemperatureCurrent")

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

ruijieTempFanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 109)
)
if mibBuilder.loadTexts:
    ruijieTempFanMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieTempFanTraps_ObjectIdentity = ObjectIdentity
ruijieTempFanTraps = _RuijieTempFanTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 109, 1)
)

# Managed Objects groups


# Notification objects

temperatureTooHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 109, 1, 1)
)
temperatureTooHighTrap.setObjects(
    ("RUIJIE-SYSTEM-MIB", "ruijieSystemTemperatureCurrent")
)
if mibBuilder.loadTexts:
    temperatureTooHighTrap.setStatus(
        "current"
    )

temperTooHighRecovTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 109, 1, 2)
)
temperTooHighRecovTrap.setObjects(
    ("RUIJIE-SYSTEM-MIB", "ruijieSystemTemperatureCurrent")
)
if mibBuilder.loadTexts:
    temperTooHighRecovTrap.setStatus(
        "current"
    )

fanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 109, 1, 3)
)
if mibBuilder.loadTexts:
    fanFailure.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-TEMP-FAN-MIB",
    **{"ruijieTempFanMIB": ruijieTempFanMIB,
       "ruijieTempFanTraps": ruijieTempFanTraps,
       "temperatureTooHighTrap": temperatureTooHighTrap,
       "temperTooHighRecovTrap": temperTooHighRecovTrap,
       "fanFailure": fanFailure}
)
