# SNMP MIB module (JUNIPER-MBG-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/juniper_2636/JUNIPER-MBG-SMI.mib
# Produced by pysmi-1.5.11 at Sat May 31 15:28:20 2025
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

(jnxJunosSpace,
 jnxMobileGatewayMibRoot) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxJunosSpace",
    "jnxMobileGatewayMibRoot")

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

_JnxJunosSpaceMobility_ObjectIdentity = ObjectIdentity
jnxJunosSpaceMobility = _JnxJunosSpaceMobility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 3, 2)
)
_JnxJunosSpaceMobilityNotifications_ObjectIdentity = ObjectIdentity
jnxJunosSpaceMobilityNotifications = _JnxJunosSpaceMobilityNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 3, 2, 1)
)
_JnxJunosSpaceMobilityObjects_ObjectIdentity = ObjectIdentity
jnxJunosSpaceMobilityObjects = _JnxJunosSpaceMobilityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 3, 2, 2)
)
_JnxJunosSpaceMobilityNotificationvars_ObjectIdentity = ObjectIdentity
jnxJunosSpaceMobilityNotificationvars = _JnxJunosSpaceMobilityNotificationvars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 3, 2, 2, 1)
)
_JnxJunosSpaceMobilityMCM_ObjectIdentity = ObjectIdentity
jnxJunosSpaceMobilityMCM = _JnxJunosSpaceMobilityMCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 3, 2, 3)
)
_JnxJunosSpaceMobilityMTM_ObjectIdentity = ObjectIdentity
jnxJunosSpaceMobilityMTM = _JnxJunosSpaceMobilityMTM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 3, 2, 4)
)
_JnxMobileGatewayPgwGgsn_ObjectIdentity = ObjectIdentity
jnxMobileGatewayPgwGgsn = _JnxMobileGatewayPgwGgsn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1)
)
_JnxMobileGatewaySgw_ObjectIdentity = ObjectIdentity
jnxMobileGatewaySgw = _JnxMobileGatewaySgw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-MBG-SMI",
    **{"jnxJunosSpaceMobility": jnxJunosSpaceMobility,
       "jnxJunosSpaceMobilityNotifications": jnxJunosSpaceMobilityNotifications,
       "jnxJunosSpaceMobilityObjects": jnxJunosSpaceMobilityObjects,
       "jnxJunosSpaceMobilityNotificationvars": jnxJunosSpaceMobilityNotificationvars,
       "jnxJunosSpaceMobilityMCM": jnxJunosSpaceMobilityMCM,
       "jnxJunosSpaceMobilityMTM": jnxJunosSpaceMobilityMTM,
       "jnxMobileGatewayPgwGgsn": jnxMobileGatewayPgwGgsn,
       "jnxMobileGatewaySgw": jnxMobileGatewaySgw}
)
