# SNMP MIB module (CIENA-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_1271/CIENA-SMI.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:39:47 2025
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
        ("2018-06-13 01:25",
         "2018-06-13 01:25",
         "2018-06-13 01:25",
         "2018-06-13 01:25",
         "2018-06-13 01:25")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaCommon_ObjectIdentity = ObjectIdentity
cienaCommon = _CienaCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 1)
)
if mibBuilder.loadTexts:
    cienaCommon.setStatus("current")
_CienaProducts_ObjectIdentity = ObjectIdentity
cienaProducts = _CienaProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 1, 2)
)
if mibBuilder.loadTexts:
    cienaProducts.setStatus("current")
_CienaCes_ObjectIdentity = ObjectIdentity
cienaCes = _CienaCes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2)
)
if mibBuilder.loadTexts:
    cienaCes.setStatus("current")
_CienaCesConfig_ObjectIdentity = ObjectIdentity
cienaCesConfig = _CienaCesConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1)
)
if mibBuilder.loadTexts:
    cienaCesConfig.setStatus("current")
_CienaCesNotifications_ObjectIdentity = ObjectIdentity
cienaCesNotifications = _CienaCesNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2)
)
if mibBuilder.loadTexts:
    cienaCesNotifications.setStatus("current")
_CienaCesNotificationsControlModule_ObjectIdentity = ObjectIdentity
cienaCesNotificationsControlModule = _CienaCesNotificationsControlModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cienaCesNotificationsControlModule.setStatus("current")
_CienaCesStatistics_ObjectIdentity = ObjectIdentity
cienaCesStatistics = _CienaCesStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3)
)
if mibBuilder.loadTexts:
    cienaCesStatistics.setStatus("current")
_CienaGenericMIBs_ObjectIdentity = ObjectIdentity
cienaGenericMIBs = _CienaGenericMIBs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 29)
)
if mibBuilder.loadTexts:
    cienaGenericMIBs.setStatus("current")
_CienaOpterametro_ObjectIdentity = ObjectIdentity
cienaOpterametro = _CienaOpterametro_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 68)
)
if mibBuilder.loadTexts:
    cienaOpterametro.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-SMI",
    **{"ciena": ciena,
       "cienaCommon": cienaCommon,
       "cienaProducts": cienaProducts,
       "cienaCes": cienaCes,
       "cienaCesConfig": cienaCesConfig,
       "cienaCesNotifications": cienaCesNotifications,
       "cienaCesNotificationsControlModule": cienaCesNotificationsControlModule,
       "cienaCesStatistics": cienaCesStatistics,
       "cienaGenericMIBs": cienaGenericMIBs,
       "cienaOpterametro": cienaOpterametro}
)
