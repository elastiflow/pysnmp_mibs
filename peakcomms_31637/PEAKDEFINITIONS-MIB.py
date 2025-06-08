# SNMP MIB module (PEAKDEFINITIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/peakcomms_31637/PEAKDEFINITIONS-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:49:02 2025
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

peakNode = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31637)
)
if mibBuilder.loadTexts:
    peakNode.setRevisions(
        ("2015-09-15 09:00",
         "2014-03-18 12:00",
         "2013-04-04 12:00",
         "2012-07-30 12:00",
         "2012-07-02 12:00",
         "2011-06-30 12:00",
         "2011-03-08 09:00",
         "2010-05-27 09:00",
         "2009-12-16 09:00",
         "2008-12-03 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FaultType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("fault", 2))
    )



class OnOffType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )



class OnlineOfflineType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 1),
          ("online", 2))
    )



class YesNoType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )



class MuteType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unMuted", 1),
          ("muted", 2),
          ("unknown", 3))
    )



class EnableType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )



class MissingType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notMissing", 1),
          ("missing", 2))
    )



class RemoteLocalType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("remote", 1),
          ("local", 2))
    )



class RedundancyTypeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("r1for1", 1),
          ("r1for2", 2),
          ("r1forN", 3))
    )



class RedundancyModeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("auto", 2),
          ("notAvailable", 3))
    )



class RedundancyPriorityType(TextualConvention, Integer32):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("priority1", 1),
          ("priority2", 2),
          ("priority3", 3),
          ("priority4", 4),
          ("priority5", 5),
          ("priority6", 6),
          ("priority7", 7),
          ("priority8", 8),
          ("notAvailable", 9))
    )



class ChannelType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notUsed", 1),
          ("internal", 2),
          ("external", 3))
    )



class ChannelModeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("automatic", 2),
          ("manual", 3))
    )



class ChannelExpectedType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notExpected", 1),
          ("expected", 2))
    )



class ChannelMissingType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notMissing", 1),
          ("missing", 2))
    )



class ChannelInternalStateType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stateNormal", 1),
          ("stateUPC", 2),
          ("stateLimbo", 3))
    )



class ChannelNumberType(TextualConvention, Integer32):
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("channelOFF", 1),
          ("channel1", 2),
          ("channel2", 3),
          ("channel3", 4),
          ("channel4", 5),
          ("channel5", 6),
          ("channel6", 7),
          ("channel7", 8),
          ("channel8", 9),
          ("channel9", 10),
          ("channel10", 11),
          ("channel11", 12),
          ("channel12", 13),
          ("channel13", 14),
          ("channel14", 15),
          ("channel15", 16),
          ("channel16", 17))
    )



# MIB Managed Objects in the order of their OIDs

_ConfStat_ObjectIdentity = ObjectIdentity
confStat = _ConfStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1)
)
_Converters_ObjectIdentity = ObjectIdentity
converters = _Converters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1)
)
_NsConverters_ObjectIdentity = ObjectIdentity
nsConverters = _NsConverters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100)
)
_Unit_ObjectIdentity = ObjectIdentity
unit = _Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 2)
)
_IndvUnits_ObjectIdentity = ObjectIdentity
indvUnits = _IndvUnits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEAKDEFINITIONS-MIB",
    **{"FaultType": FaultType,
       "OnOffType": OnOffType,
       "OnlineOfflineType": OnlineOfflineType,
       "YesNoType": YesNoType,
       "MuteType": MuteType,
       "EnableType": EnableType,
       "MissingType": MissingType,
       "RemoteLocalType": RemoteLocalType,
       "RedundancyTypeType": RedundancyTypeType,
       "RedundancyModeType": RedundancyModeType,
       "RedundancyPriorityType": RedundancyPriorityType,
       "ChannelType": ChannelType,
       "ChannelModeType": ChannelModeType,
       "ChannelExpectedType": ChannelExpectedType,
       "ChannelMissingType": ChannelMissingType,
       "ChannelInternalStateType": ChannelInternalStateType,
       "ChannelNumberType": ChannelNumberType,
       "peakNode": peakNode,
       "confStat": confStat,
       "converters": converters,
       "nsConverters": nsConverters,
       "unit": unit,
       "indvUnits": indvUnits}
)
