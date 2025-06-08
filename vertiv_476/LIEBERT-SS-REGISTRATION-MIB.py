# SNMP MIB module (LIEBERT-SS-REGISTRATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/vertiv_476/LIEBERT-SS-REGISTRATION-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 20:21:43 2025
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

liebertSiteScanRegistrationModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 999, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Emerson_ObjectIdentity = ObjectIdentity
emerson = _Emerson_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476)
)
if mibBuilder.loadTexts:
    emerson.setStatus("current")
_LiebertCorp_ObjectIdentity = ObjectIdentity
liebertCorp = _LiebertCorp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1)
)
if mibBuilder.loadTexts:
    liebertCorp.setStatus("current")
_LiebertSiteScan_ObjectIdentity = ObjectIdentity
liebertSiteScan = _LiebertSiteScan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 999)
)
if mibBuilder.loadTexts:
    liebertSiteScan.setStatus("current")
_LssModuleReg_ObjectIdentity = ObjectIdentity
lssModuleReg = _LssModuleReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 999, 1)
)
if mibBuilder.loadTexts:
    lssModuleReg.setStatus("current")
_LiebertSiteScanNotificationsModuleReg_ObjectIdentity = ObjectIdentity
liebertSiteScanNotificationsModuleReg = _LiebertSiteScanNotificationsModuleReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 999, 1, 4)
)
if mibBuilder.loadTexts:
    liebertSiteScanNotificationsModuleReg.setStatus("current")
_LssFoundation_ObjectIdentity = ObjectIdentity
lssFoundation = _LssFoundation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 999, 3)
)
if mibBuilder.loadTexts:
    lssFoundation.setStatus("current")
_LssNotifications_ObjectIdentity = ObjectIdentity
lssNotifications = _LssNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 999, 3, 3)
)
if mibBuilder.loadTexts:
    lssNotifications.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LIEBERT-SS-REGISTRATION-MIB",
    **{"emerson": emerson,
       "liebertCorp": liebertCorp,
       "liebertSiteScan": liebertSiteScan,
       "lssModuleReg": lssModuleReg,
       "liebertSiteScanRegistrationModule": liebertSiteScanRegistrationModule,
       "liebertSiteScanNotificationsModuleReg": liebertSiteScanNotificationsModuleReg,
       "lssFoundation": lssFoundation,
       "lssNotifications": lssNotifications}
)
