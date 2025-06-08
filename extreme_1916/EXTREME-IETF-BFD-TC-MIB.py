# SNMP MIB module (EXTREME-IETF-BFD-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/extreme_1916/EXTREME-IETF-BFD-TC-MIB.mib
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

(extremeBfd,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeBfd")

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
 mib_2) = mibBuilder.importSymbols(
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
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

extremeIetfBfdTCMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 43, 1)
)
if mibBuilder.loadTexts:
    extremeIetfBfdTCMib.setRevisions(
        ("2012-06-14 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ExtremeBfdSessIndexTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class ExtremeBfdIntervalTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class ExtremeBfdMultiplierTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class ExtremeBfdDiagTC(TextualConvention, Integer32):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("noDiagnostic", 0),
          ("controlDetectionTimeExpired", 1),
          ("echoFunctionFailed", 2),
          ("neighborSignaledSessionDown", 3),
          ("forwardingPlaneReset", 4),
          ("pathDown", 5),
          ("concatenatedPathDown", 6),
          ("administrativelyDown", 7),
          ("reverseConcatenatedPathDown", 8))
    )



class ExtremeBfdSessTypeTC(TextualConvention, Integer32):
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
        *(("singleHop", 1),
          ("multiHopTotallyArbitraryPaths", 2),
          ("multiHopOutOfBandSignaling", 3),
          ("multiHopUnidirectionalLinks", 4),
          ("multiPointHead", 5),
          ("multiPointTail", 6))
    )



class ExtremeBfdSessOperModeTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("asyncModeWEchoFunction", 1),
          ("asynchModeWOEchoFunction", 2),
          ("demandModeWEchoFunction", 3),
          ("demandModeWOEchoFunction", 4))
    )



class ExtremeBfdCtrlDestPortNumberTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class ExtremeBfdCtrlSourcePortNumberTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class ExtremeBfdSessStateTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("adminDown", 1),
          ("down", 2),
          ("init", 3),
          ("up", 4),
          ("failing", 5))
    )



class ExtremeBfdSessAuthenticationTypeTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noAuthentication", -1),
          ("reserved", 0),
          ("simplePassword", 1),
          ("keyedMD5", 2),
          ("meticulousKeyedMD5", 3),
          ("keyedSHA1", 4),
          ("meticulousKeyedSHA1", 5))
    )



class ExtremeBfdSessionAuthenticationKeyTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x "
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 252),
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-IETF-BFD-TC-MIB",
    **{"ExtremeBfdSessIndexTC": ExtremeBfdSessIndexTC,
       "ExtremeBfdIntervalTC": ExtremeBfdIntervalTC,
       "ExtremeBfdMultiplierTC": ExtremeBfdMultiplierTC,
       "ExtremeBfdDiagTC": ExtremeBfdDiagTC,
       "ExtremeBfdSessTypeTC": ExtremeBfdSessTypeTC,
       "ExtremeBfdSessOperModeTC": ExtremeBfdSessOperModeTC,
       "ExtremeBfdCtrlDestPortNumberTC": ExtremeBfdCtrlDestPortNumberTC,
       "ExtremeBfdCtrlSourcePortNumberTC": ExtremeBfdCtrlSourcePortNumberTC,
       "ExtremeBfdSessStateTC": ExtremeBfdSessStateTC,
       "ExtremeBfdSessAuthenticationTypeTC": ExtremeBfdSessAuthenticationTypeTC,
       "ExtremeBfdSessionAuthenticationKeyTC": ExtremeBfdSessionAuthenticationKeyTC,
       "extremeIetfBfdTCMib": extremeIetfBfdTCMib}
)
