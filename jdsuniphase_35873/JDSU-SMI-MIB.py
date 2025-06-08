# SNMP MIB module (JDSU-SMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/jdsuniphase_35873/JDSU-SMI-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 10:53:14 2025
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

jdsuRoot = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35873)
)
if mibBuilder.loadTexts:
    jdsuRoot.setRevisions(
        ("2010-06-08 09:53",
         "2014-01-22 08:51")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JdsuAccessNetworkTest_ObjectIdentity = ObjectIdentity
jdsuAccessNetworkTest = _JdsuAccessNetworkTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 1)
)
_JdsuCableNetworkTest_ObjectIdentity = ObjectIdentity
jdsuCableNetworkTest = _JdsuCableNetworkTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 2)
)
_JdsuDataIPTest_ObjectIdentity = ObjectIdentity
jdsuDataIPTest = _JdsuDataIPTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 3)
)
_JdsuDigitalVideoTest_ObjectIdentity = ObjectIdentity
jdsuDigitalVideoTest = _JdsuDigitalVideoTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 4)
)
_JdsuFiberFieldTestSystems_ObjectIdentity = ObjectIdentity
jdsuFiberFieldTestSystems = _JdsuFiberFieldTestSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5)
)
_JdsuRemoteFiberTest_ObjectIdentity = ObjectIdentity
jdsuRemoteFiberTest = _JdsuRemoteFiberTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1)
)
_JdsuOnmsi_ObjectIdentity = ObjectIdentity
jdsuOnmsi = _JdsuOnmsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 1)
)
_JdsuOtu_ObjectIdentity = ObjectIdentity
jdsuOtu = _JdsuOtu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 5, 1, 2)
)
_JdsuLabManufacturingTest_ObjectIdentity = ObjectIdentity
jdsuLabManufacturingTest = _JdsuLabManufacturingTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 6)
)
_JdsuMetroNetworkTest_ObjectIdentity = ObjectIdentity
jdsuMetroNetworkTest = _JdsuMetroNetworkTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 7)
)
_JdsuNetworkEnterpriseTest_ObjectIdentity = ObjectIdentity
jdsuNetworkEnterpriseTest = _JdsuNetworkEnterpriseTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 8)
)
_JdsuServiceAssurance_ObjectIdentity = ObjectIdentity
jdsuServiceAssurance = _JdsuServiceAssurance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 9)
)
_JdsuStorageProtocolTest_ObjectIdentity = ObjectIdentity
jdsuStorageProtocolTest = _JdsuStorageProtocolTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 10)
)
_JdsuWirelessTest_ObjectIdentity = ObjectIdentity
jdsuWirelessTest = _JdsuWirelessTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35873, 11)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JDSU-SMI-MIB",
    **{"jdsuRoot": jdsuRoot,
       "jdsuAccessNetworkTest": jdsuAccessNetworkTest,
       "jdsuCableNetworkTest": jdsuCableNetworkTest,
       "jdsuDataIPTest": jdsuDataIPTest,
       "jdsuDigitalVideoTest": jdsuDigitalVideoTest,
       "jdsuFiberFieldTestSystems": jdsuFiberFieldTestSystems,
       "jdsuRemoteFiberTest": jdsuRemoteFiberTest,
       "jdsuOnmsi": jdsuOnmsi,
       "jdsuOtu": jdsuOtu,
       "jdsuLabManufacturingTest": jdsuLabManufacturingTest,
       "jdsuMetroNetworkTest": jdsuMetroNetworkTest,
       "jdsuNetworkEnterpriseTest": jdsuNetworkEnterpriseTest,
       "jdsuServiceAssurance": jdsuServiceAssurance,
       "jdsuStorageProtocolTest": jdsuStorageProtocolTest,
       "jdsuWirelessTest": jdsuWirelessTest}
)
