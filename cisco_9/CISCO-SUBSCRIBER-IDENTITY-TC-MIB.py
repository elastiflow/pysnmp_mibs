# SNMP MIB module (CISCO-SUBSCRIBER-IDENTITY-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-SUBSCRIBER-IDENTITY-TC-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:55:05 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoSubscriberIdentityTcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 782)
)
if mibBuilder.loadTexts:
    ciscoSubscriberIdentityTcMIB.setRevisions(
        ("2011-12-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SubSessionIdentity(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("ifIndex", 2),
          ("subscriberLabel", 3),
          ("macAddress", 4),
          ("nativeVrf", 5),
          ("nativeIpAddress", 6),
          ("domainVrf", 7),
          ("domainIpAddress", 8),
          ("pbhk", 9),
          ("remoteId", 10),
          ("circuitId", 11),
          ("nasPort", 12),
          ("domain", 13),
          ("username", 14),
          ("acctSessionId", 15),
          ("dnis", 16),
          ("media", 17),
          ("mlpNegotiated", 18),
          ("protocol", 19),
          ("serviceName", 20),
          ("dhcpClass", 21),
          ("tunnelName", 22))
    )



class SubSessionIdentities(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("ifIndex", 0),
          ("subscriberLabel", 1),
          ("macAddress", 2),
          ("nativeVrf", 3),
          ("nativeIpAddress", 4),
          ("domainVrf", 5),
          ("domainIpAddress", 6),
          ("pbhk", 7),
          ("remoteId", 8),
          ("circuitId", 9),
          ("nasPort", 10),
          ("domain", 11),
          ("username", 12),
          ("acctSessionId", 13),
          ("dnis", 14),
          ("media", 15),
          ("mlpNegotiated", 16),
          ("protocol", 17),
          ("serviceName", 18),
          ("dhcpClass", 19),
          ("tunnelName", 20))
    )


class SubscriberLabel(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "x"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class SubscriberVRF(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class SubscriberPbhk(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixedLength = 6



class SubscriberRemoteId(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class SubscriberCircuitId(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class SubscriberNasPort(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class SubscriberDomain(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class SubscriberUsername(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class SubscriberAcctSessionId(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "x"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class SubscriberDnis(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class SubscriberMediaType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("async", 2),
          ("atm", 3),
          ("ethernet", 4),
          ("ip", 5),
          ("isdn", 6),
          ("mpls", 7),
          ("sync", 8))
    )



class SubscriberProtocolType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("atom", 2),
          ("ip", 3),
          ("psdn", 4),
          ("ppp", 5),
          ("vpdn", 6))
    )



class SubscriberDhcpClass(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class SubscriberTunnelName(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class SubscriberLocationName(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class SubscriberServiceName(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SUBSCRIBER-IDENTITY-TC-MIB",
    **{"SubSessionIdentity": SubSessionIdentity,
       "SubSessionIdentities": SubSessionIdentities,
       "SubscriberLabel": SubscriberLabel,
       "SubscriberVRF": SubscriberVRF,
       "SubscriberPbhk": SubscriberPbhk,
       "SubscriberRemoteId": SubscriberRemoteId,
       "SubscriberCircuitId": SubscriberCircuitId,
       "SubscriberNasPort": SubscriberNasPort,
       "SubscriberDomain": SubscriberDomain,
       "SubscriberUsername": SubscriberUsername,
       "SubscriberAcctSessionId": SubscriberAcctSessionId,
       "SubscriberDnis": SubscriberDnis,
       "SubscriberMediaType": SubscriberMediaType,
       "SubscriberProtocolType": SubscriberProtocolType,
       "SubscriberDhcpClass": SubscriberDhcpClass,
       "SubscriberTunnelName": SubscriberTunnelName,
       "SubscriberLocationName": SubscriberLocationName,
       "SubscriberServiceName": SubscriberServiceName,
       "ciscoSubscriberIdentityTcMIB": ciscoSubscriberIdentityTcMIB}
)
