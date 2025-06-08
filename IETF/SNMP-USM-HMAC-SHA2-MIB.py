# SNMP MIB module (SNMP-USM-HMAC-SHA2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/SNMP-USM-HMAC-SHA2-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 15:06:10 2025
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

(snmpAuthProtocols,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "snmpAuthProtocols")

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
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "snmpModules")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

snmpUsmHmacSha2MIB = ModuleIdentity(
    (1, 3, 6, 1, 6, 3, 235)
)
if mibBuilder.loadTexts:
    snmpUsmHmacSha2MIB.setRevisions(
        ("2015-08-13 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsmHMAC128SHA224AuthProtocol_ObjectIdentity = ObjectIdentity
usmHMAC128SHA224AuthProtocol = _UsmHMAC128SHA224AuthProtocol_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 10, 1, 1, 4)
)
if mibBuilder.loadTexts:
    usmHMAC128SHA224AuthProtocol.setStatus("current")
_UsmHMAC192SHA256AuthProtocol_ObjectIdentity = ObjectIdentity
usmHMAC192SHA256AuthProtocol = _UsmHMAC192SHA256AuthProtocol_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 10, 1, 1, 5)
)
if mibBuilder.loadTexts:
    usmHMAC192SHA256AuthProtocol.setStatus("current")
_UsmHMAC256SHA384AuthProtocol_ObjectIdentity = ObjectIdentity
usmHMAC256SHA384AuthProtocol = _UsmHMAC256SHA384AuthProtocol_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 10, 1, 1, 6)
)
if mibBuilder.loadTexts:
    usmHMAC256SHA384AuthProtocol.setStatus("current")
_UsmHMAC384SHA512AuthProtocol_ObjectIdentity = ObjectIdentity
usmHMAC384SHA512AuthProtocol = _UsmHMAC384SHA512AuthProtocol_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 10, 1, 1, 7)
)
if mibBuilder.loadTexts:
    usmHMAC384SHA512AuthProtocol.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNMP-USM-HMAC-SHA2-MIB",
    **{"usmHMAC128SHA224AuthProtocol": usmHMAC128SHA224AuthProtocol,
       "usmHMAC192SHA256AuthProtocol": usmHMAC192SHA256AuthProtocol,
       "usmHMAC256SHA384AuthProtocol": usmHMAC256SHA384AuthProtocol,
       "usmHMAC384SHA512AuthProtocol": usmHMAC384SHA512AuthProtocol,
       "snmpUsmHmacSha2MIB": snmpUsmHmacSha2MIB}
)
