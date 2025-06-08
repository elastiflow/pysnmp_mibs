# SNMP MIB module (JUNIPER-WX-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/juniper_2636/JUNIPER-WX-EVENT-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 31 15:31:35 2025
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

(jnxWxGrpEvents,) = mibBuilder.importSymbols(
    "JUNIPER-WX-GLOBAL-MIB",
    "jnxWxGrpEvents")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxWxGrpEventV2_ObjectIdentity = ObjectIdentity
jnxWxGrpEventV2 = _JnxWxGrpEventV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 3, 0)
)
if mibBuilder.loadTexts:
    jnxWxGrpEventV2.setStatus("current")
_JnxWxGrpEventDescr_Type = DisplayString
_JnxWxGrpEventDescr_Object = MibScalar
jnxWxGrpEventDescr = _JnxWxGrpEventDescr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 3, 1),
    _JnxWxGrpEventDescr_Type()
)
jnxWxGrpEventDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxWxGrpEventDescr.setStatus("current")

# Managed Objects groups


# Notification objects

jnxWxGrpEventPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 3, 0, 1)
)
if mibBuilder.loadTexts:
    jnxWxGrpEventPowerSupplyFailure.setStatus(
        "current"
    )

jnxWxGrpEventPowerSupplyOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 3, 0, 2)
)
if mibBuilder.loadTexts:
    jnxWxGrpEventPowerSupplyOk.setStatus(
        "current"
    )

jnxWxGrpEventLicenseWillExpire = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 3, 0, 3)
)
jnxWxGrpEventLicenseWillExpire.setObjects(
    ("JUNIPER-WX-EVENT-MIB", "jnxWxGrpEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxGrpEventLicenseWillExpire.setStatus(
        "current"
    )

jnxWxGrpEventThruputLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 3, 0, 4)
)
jnxWxGrpEventThruputLimitExceeded.setObjects(
    ("JUNIPER-WX-EVENT-MIB", "jnxWxGrpEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxGrpEventThruputLimitExceeded.setStatus(
        "current"
    )

jnxWxGrpEventLicenseExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 3, 0, 5)
)
jnxWxGrpEventLicenseExpired.setObjects(
    ("JUNIPER-WX-EVENT-MIB", "jnxWxGrpEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxGrpEventLicenseExpired.setStatus(
        "current"
    )

jnxWxGrpEventClientLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 3, 0, 6)
)
jnxWxGrpEventClientLimitExceeded.setObjects(
    ("JUNIPER-WX-EVENT-MIB", "jnxWxGrpEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxGrpEventClientLimitExceeded.setStatus(
        "current"
    )

jnxWxGrpEventInFailSafeMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 3, 0, 7)
)
if mibBuilder.loadTexts:
    jnxWxGrpEventInFailSafeMode.setStatus(
        "current"
    )

jnxWxGrpEventInterfaceSpeedMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 3, 0, 8)
)
jnxWxGrpEventInterfaceSpeedMismatch.setObjects(
    ("JUNIPER-WX-EVENT-MIB", "jnxWxGrpEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxGrpEventInterfaceSpeedMismatch.setStatus(
        "current"
    )

jnxWxGrpEventInterfaceSpeedOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 3, 0, 9)
)
jnxWxGrpEventInterfaceSpeedOk.setObjects(
    ("JUNIPER-WX-EVENT-MIB", "jnxWxGrpEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxGrpEventInterfaceSpeedOk.setStatus(
        "current"
    )

jnxWxGrpEventInterfaceDuplexMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 3, 0, 10)
)
jnxWxGrpEventInterfaceDuplexMismatch.setObjects(
    ("JUNIPER-WX-EVENT-MIB", "jnxWxGrpEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxGrpEventInterfaceDuplexMismatch.setStatus(
        "current"
    )

jnxWxGrpEventLoginFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 3, 0, 11)
)
jnxWxGrpEventLoginFailure.setObjects(
    ("JUNIPER-WX-EVENT-MIB", "jnxWxGrpEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxGrpEventLoginFailure.setStatus(
        "current"
    )

jnxWxGrpEventDiskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 41, 1, 1, 3, 0, 12)
)
jnxWxGrpEventDiskFailure.setObjects(
    ("JUNIPER-WX-EVENT-MIB", "jnxWxGrpEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxGrpEventDiskFailure.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-WX-EVENT-MIB",
    **{"jnxWxGrpEventV2": jnxWxGrpEventV2,
       "jnxWxGrpEventPowerSupplyFailure": jnxWxGrpEventPowerSupplyFailure,
       "jnxWxGrpEventPowerSupplyOk": jnxWxGrpEventPowerSupplyOk,
       "jnxWxGrpEventLicenseWillExpire": jnxWxGrpEventLicenseWillExpire,
       "jnxWxGrpEventThruputLimitExceeded": jnxWxGrpEventThruputLimitExceeded,
       "jnxWxGrpEventLicenseExpired": jnxWxGrpEventLicenseExpired,
       "jnxWxGrpEventClientLimitExceeded": jnxWxGrpEventClientLimitExceeded,
       "jnxWxGrpEventInFailSafeMode": jnxWxGrpEventInFailSafeMode,
       "jnxWxGrpEventInterfaceSpeedMismatch": jnxWxGrpEventInterfaceSpeedMismatch,
       "jnxWxGrpEventInterfaceSpeedOk": jnxWxGrpEventInterfaceSpeedOk,
       "jnxWxGrpEventInterfaceDuplexMismatch": jnxWxGrpEventInterfaceDuplexMismatch,
       "jnxWxGrpEventLoginFailure": jnxWxGrpEventLoginFailure,
       "jnxWxGrpEventDiskFailure": jnxWxGrpEventDiskFailure,
       "jnxWxGrpEventDescr": jnxWxGrpEventDescr}
)
