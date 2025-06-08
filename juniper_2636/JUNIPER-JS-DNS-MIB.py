# SNMP MIB module (JUNIPER-JS-DNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/juniper_2636/JUNIPER-JS-DNS-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:49:54 2025
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

(jnxJsDnsRoot,) = mibBuilder.importSymbols(
    "JUNIPER-JS-SMI",
    "jnxJsDnsRoot")

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

jnxJsDns = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 10, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxJsDnsProxyDataObjects_ObjectIdentity = ObjectIdentity
jnxJsDnsProxyDataObjects = _JnxJsDnsProxyDataObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 10, 1, 1)
)
_JnxJsDNSProxyQueriesReceived_Type = Counter64
_JnxJsDNSProxyQueriesReceived_Object = MibScalar
jnxJsDNSProxyQueriesReceived = _JnxJsDNSProxyQueriesReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 10, 1, 1, 1),
    _JnxJsDNSProxyQueriesReceived_Type()
)
jnxJsDNSProxyQueriesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsDNSProxyQueriesReceived.setStatus("current")
_JnxJsDnsProxyResponsesSent_Type = Counter64
_JnxJsDnsProxyResponsesSent_Object = MibScalar
jnxJsDnsProxyResponsesSent = _JnxJsDnsProxyResponsesSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 10, 1, 1, 2),
    _JnxJsDnsProxyResponsesSent_Type()
)
jnxJsDnsProxyResponsesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsDnsProxyResponsesSent.setStatus("current")
_JnxJsDnsProxyQueriesForwarded_Type = Counter64
_JnxJsDnsProxyQueriesForwarded_Object = MibScalar
jnxJsDnsProxyQueriesForwarded = _JnxJsDnsProxyQueriesForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 10, 1, 1, 3),
    _JnxJsDnsProxyQueriesForwarded_Type()
)
jnxJsDnsProxyQueriesForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsDnsProxyQueriesForwarded.setStatus("current")
_JnxJsDnsProxyNegativeResponses_Type = Counter64
_JnxJsDnsProxyNegativeResponses_Object = MibScalar
jnxJsDnsProxyNegativeResponses = _JnxJsDnsProxyNegativeResponses_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 10, 1, 1, 4),
    _JnxJsDnsProxyNegativeResponses_Type()
)
jnxJsDnsProxyNegativeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsDnsProxyNegativeResponses.setStatus("current")
_JnxJsDnsProxyRetryRequests_Type = Counter64
_JnxJsDnsProxyRetryRequests_Object = MibScalar
jnxJsDnsProxyRetryRequests = _JnxJsDnsProxyRetryRequests_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 10, 1, 1, 5),
    _JnxJsDnsProxyRetryRequests_Type()
)
jnxJsDnsProxyRetryRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsDnsProxyRetryRequests.setStatus("current")
_JnxJsDnsProxyPendingRequests_Type = Counter64
_JnxJsDnsProxyPendingRequests_Object = MibScalar
jnxJsDnsProxyPendingRequests = _JnxJsDnsProxyPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 10, 1, 1, 6),
    _JnxJsDnsProxyPendingRequests_Type()
)
jnxJsDnsProxyPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsDnsProxyPendingRequests.setStatus("current")
_JnxJsDnsProxyServerFailures_Type = Counter64
_JnxJsDnsProxyServerFailures_Object = MibScalar
jnxJsDnsProxyServerFailures = _JnxJsDnsProxyServerFailures_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 10, 1, 1, 7),
    _JnxJsDnsProxyServerFailures_Type()
)
jnxJsDnsProxyServerFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsDnsProxyServerFailures.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-JS-DNS-MIB",
    **{"jnxJsDns": jnxJsDns,
       "jnxJsDnsProxyDataObjects": jnxJsDnsProxyDataObjects,
       "jnxJsDNSProxyQueriesReceived": jnxJsDNSProxyQueriesReceived,
       "jnxJsDnsProxyResponsesSent": jnxJsDnsProxyResponsesSent,
       "jnxJsDnsProxyQueriesForwarded": jnxJsDnsProxyQueriesForwarded,
       "jnxJsDnsProxyNegativeResponses": jnxJsDnsProxyNegativeResponses,
       "jnxJsDnsProxyRetryRequests": jnxJsDnsProxyRetryRequests,
       "jnxJsDnsProxyPendingRequests": jnxJsDnsProxyPendingRequests,
       "jnxJsDnsProxyServerFailures": jnxJsDnsProxyServerFailures}
)
