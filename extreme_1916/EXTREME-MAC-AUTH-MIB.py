# SNMP MIB module (EXTREME-MAC-AUTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/extreme_1916/EXTREME-MAC-AUTH-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 16:23:18 2025
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

(extremeAgent,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

extremeMacAuthMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 44)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeMacAuthObjects_ObjectIdentity = ObjectIdentity
extremeMacAuthObjects = _ExtremeMacAuthObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 44, 1)
)
_ExtremeMacAuthClientTable_Object = MibTable
extremeMacAuthClientTable = _ExtremeMacAuthClientTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 44, 1, 1)
)
if mibBuilder.loadTexts:
    extremeMacAuthClientTable.setStatus("current")
_ExtremeMacAuthClientEntry_Object = MibTableRow
extremeMacAuthClientEntry = _ExtremeMacAuthClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 44, 1, 1, 1)
)
extremeMacAuthClientEntry.setIndexNames(
    (0, "EXTREME-MAC-AUTH-MIB", "extremeMacAuthClientAddress"),
)
if mibBuilder.loadTexts:
    extremeMacAuthClientEntry.setStatus("current")
_ExtremeMacAuthClientAddress_Type = MacAddress
_ExtremeMacAuthClientAddress_Object = MibTableColumn
extremeMacAuthClientAddress = _ExtremeMacAuthClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 44, 1, 1, 1, 1),
    _ExtremeMacAuthClientAddress_Type()
)
extremeMacAuthClientAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeMacAuthClientAddress.setStatus("current")
_ExtremeMacAuthClientInitialize_Type = TruthValue
_ExtremeMacAuthClientInitialize_Object = MibTableColumn
extremeMacAuthClientInitialize = _ExtremeMacAuthClientInitialize_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 44, 1, 1, 1, 2),
    _ExtremeMacAuthClientInitialize_Type()
)
extremeMacAuthClientInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeMacAuthClientInitialize.setStatus("current")
_ExtremeMacAuthClientReauthenticate_Type = TruthValue
_ExtremeMacAuthClientReauthenticate_Object = MibTableColumn
extremeMacAuthClientReauthenticate = _ExtremeMacAuthClientReauthenticate_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 44, 1, 1, 1, 3),
    _ExtremeMacAuthClientReauthenticate_Type()
)
extremeMacAuthClientReauthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeMacAuthClientReauthenticate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-MAC-AUTH-MIB",
    **{"extremeMacAuthMIB": extremeMacAuthMIB,
       "extremeMacAuthObjects": extremeMacAuthObjects,
       "extremeMacAuthClientTable": extremeMacAuthClientTable,
       "extremeMacAuthClientEntry": extremeMacAuthClientEntry,
       "extremeMacAuthClientAddress": extremeMacAuthClientAddress,
       "extremeMacAuthClientInitialize": extremeMacAuthClientInitialize,
       "extremeMacAuthClientReauthenticate": extremeMacAuthClientReauthenticate}
)
