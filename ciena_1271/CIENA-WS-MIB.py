# SNMP MIB module (CIENA-WS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_1271/CIENA-WS-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:39:48 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ciena = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271)
)
if mibBuilder.loadTexts:
    ciena.setRevisions(
        ("2018-04-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Waveserver_ObjectIdentity = ObjectIdentity
waveserver = _Waveserver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3)
)
if mibBuilder.loadTexts:
    waveserver.setStatus("current")
_CienaWsConfigV1_ObjectIdentity = ObjectIdentity
cienaWsConfigV1 = _CienaWsConfigV1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 1)
)
if mibBuilder.loadTexts:
    cienaWsConfigV1.setStatus("current")
_CienaWsNotifications_ObjectIdentity = ObjectIdentity
cienaWsNotifications = _CienaWsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2)
)
if mibBuilder.loadTexts:
    cienaWsNotifications.setStatus("current")
_CienaWsNotificationsControlModule_ObjectIdentity = ObjectIdentity
cienaWsNotificationsControlModule = _CienaWsNotificationsControlModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cienaWsNotificationsControlModule.setStatus("current")
_CienaWsStatistics_ObjectIdentity = ObjectIdentity
cienaWsStatistics = _CienaWsStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 3)
)
if mibBuilder.loadTexts:
    cienaWsStatistics.setStatus("obsolete")
_CienaWsConfig_ObjectIdentity = ObjectIdentity
cienaWsConfig = _CienaWsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4)
)
if mibBuilder.loadTexts:
    cienaWsConfig.setStatus("current")
_CienaWsPlatformConfig_ObjectIdentity = ObjectIdentity
cienaWsPlatformConfig = _CienaWsPlatformConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5)
)
if mibBuilder.loadTexts:
    cienaWsPlatformConfig.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-WS-MIB",
    **{"ciena": ciena,
       "waveserver": waveserver,
       "cienaWsConfigV1": cienaWsConfigV1,
       "cienaWsNotifications": cienaWsNotifications,
       "cienaWsNotificationsControlModule": cienaWsNotificationsControlModule,
       "cienaWsStatistics": cienaWsStatistics,
       "cienaWsConfig": cienaWsConfig,
       "cienaWsPlatformConfig": cienaWsPlatformConfig}
)
