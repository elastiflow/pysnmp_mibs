# SNMP MIB module (ACMEPACKET-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/acmepacket_9148/ACMEPACKET-TC.mib
# Produced by pysmi-1.5.11 at Fri May 30 15:10:25 2025
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

(acmepacket,) = mibBuilder.importSymbols(
    "ACMEPACKET-SMI",
    "acmepacket")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

apTextualConventions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 0)
)
if mibBuilder.loadTexts:
    apTextualConventions.setRevisions(
        ("2012-02-06 23:05",
         "2012-05-05 23:05",
         "2014-06-26 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ApHardwareModuleFamily(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              17,
              18,
              19,
              24,
              25,
              26,
              240,
              241,
              242)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("spu", 17),
          ("npu", 18),
          ("tcu", 19),
          ("niuCopper", 24),
          ("niuFiber", 25),
          ("miu", 26),
          ("fanTray", 240),
          ("powerSupply", 241),
          ("niu10g", 242))
    )



class ApRedundancyState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("initial", 1),
          ("active", 2),
          ("standby", 3),
          ("outOfService", 4),
          ("unassigned", 5),
          ("activePending", 6),
          ("standbyPending", 7),
          ("outOfServicePending", 8),
          ("recovery", 9))
    )



class ApPhyPortType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("sfp", 1))
    )



class ApPresence(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("inserted", 1),
          ("removed", 2))
    )



class ApTransportType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("tcp", 1),
          ("sctp", 2))
    )



class ApServerStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inservice", 0),
          ("lowerpriority", 1),
          ("oosunreachable", 2))
    )



class ApDiamResultCode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1001,
              2001,
              2002,
              3001,
              3002,
              3003,
              3004,
              3005,
              3006,
              3007,
              3008,
              3009,
              3010,
              4001,
              4002,
              4003,
              5001,
              5002,
              5003,
              5004,
              5005,
              5006,
              5007,
              5008,
              5009,
              5010,
              5011,
              5012,
              5013,
              5014,
              5015,
              5016,
              5017)
        )
    )
    namedValues = NamedValues(
        *(("diameterMultiRoundAuth", 1001),
          ("diameterSuccess", 2001),
          ("diameterLimitedSuccess", 2002),
          ("diameterCommandUnsupported", 3001),
          ("diameterUnableToDeliver", 3002),
          ("diameterRealmNotServed", 3003),
          ("diameterTooBusy", 3004),
          ("diameterLoopDetected", 3005),
          ("diameterRedirectIndicatoion", 3006),
          ("diameterApplicationUnsupported", 3007),
          ("diameterInvalidHdrBits", 3008),
          ("diameterInvalidAvpBits", 3009),
          ("diameterUnknownPeer", 3010),
          ("diameterAuthenticationRejected", 4001),
          ("diameterOutOfSpace", 4002),
          ("electionLost", 4003),
          ("diameterAvpUnsupported", 5001),
          ("diameterUnknownSessionId", 5002),
          ("diameterAuthoriszationRejected", 5003),
          ("diameterInvalidAvpValue", 5004),
          ("diameterMissingAvp", 5005),
          ("diameterResourcesExceeded", 5006),
          ("diameterContradictingAvps", 5007),
          ("diameterAvpNotAllowed", 5008),
          ("diameterAvpTooManyTimes", 5009),
          ("diameterNoCommonApplication", 5010),
          ("diameterUnsupportedVersion", 5011),
          ("diameterUnableToComply", 5012),
          ("diameterInvalidBitInHeader", 5013),
          ("diameterInvalidAvpLength", 5014),
          ("diameterInvalidMessageLength", 5015),
          ("diameterInvalidAvpBitCombo", 5016),
          ("diameterNoCommonSecurity", 5017))
    )



class ApPercentage(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class ApSipMethod(TextualConvention, Integer32):
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("invite", 2),
          ("ack", 3),
          ("bye", 4),
          ("register", 5),
          ("cancel", 6),
          ("prack", 7),
          ("options", 8),
          ("info", 9),
          ("subscribe", 10),
          ("notify", 11),
          ("refer", 12),
          ("update", 13),
          ("message", 14),
          ("publish", 15))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACMEPACKET-TC",
    **{"ApHardwareModuleFamily": ApHardwareModuleFamily,
       "ApRedundancyState": ApRedundancyState,
       "ApPhyPortType": ApPhyPortType,
       "ApPresence": ApPresence,
       "ApTransportType": ApTransportType,
       "ApServerStatus": ApServerStatus,
       "ApDiamResultCode": ApDiamResultCode,
       "ApPercentage": ApPercentage,
       "ApSipMethod": ApSipMethod,
       "apTextualConventions": apTextualConventions}
)
