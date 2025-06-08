# SNMP MIB module (CISCO-FLOW-MONITOR-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FLOW-MONITOR-TC-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:28:30 2025
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

ciscoFlowMonitorTcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 688)
)
if mibBuilder.loadTexts:
    ciscoFlowMonitorTcMIB.setRevisions(
        ("2008-12-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FlowMonitorIdentifier(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class FlowIdentifier(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class FlowPointType(TextualConvention, Integer32):
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
        *(("other", 1),
          ("unknown", 2),
          ("none", 3),
          ("interface", 4),
          ("dot1qVlan", 5))
    )



class FlowPointIdentifier(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class FlowPointInterface(TextualConvention, OctetString):
    status = "current"
    displayHint = "4d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixedLength = 4



class FlowPointDot1qVlan(TextualConvention, OctetString):
    status = "current"
    displayHint = "4d,2d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixedLength = 6



class FlowMetrics(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("mdi", 0),
          ("rtp", 1),
          ("ipCbr", 2))
    )


class FlowCfgRateType(TextualConvention, Integer32):
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
        *(("auto", 1),
          ("ipPktRate", 2),
          ("ipBitRate", 3),
          ("mediaRate", 4))
    )



class FlowBitRateUnits(TextualConvention, Integer32):
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
        *(("bps", 1),
          ("kbps", 2),
          ("mbps", 3),
          ("gbps", 4))
    )



class FlowMetricScale(TextualConvention, Integer32):
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
        *(("yocto", 1),
          ("zepto", 2),
          ("atto", 3),
          ("femto", 4),
          ("pico", 5),
          ("nano", 6),
          ("micro", 7),
          ("milli", 8),
          ("units", 9),
          ("kilo", 10),
          ("mega", 11),
          ("giga", 12),
          ("tera", 13),
          ("exa", 14),
          ("peta", 15),
          ("zetta", 16),
          ("yotta", 17))
    )



class FlowMetricPrecision(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-8, -1),
        ValueRangeConstraint(1, 9),
    )



class FlowMetricValue(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000000, 1000000000),
    )



class FlowMonitorConditions(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class FlowMonitorConditionsProfile(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class FlowMonitorConditionsProfileOrZero(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class FlowMonitorConditionIdentifier(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2039),
    )



class FlowMonitorAlarmGroupIdentifier(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class FlowSetIdentifier(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FLOW-MONITOR-TC-MIB",
    **{"FlowMonitorIdentifier": FlowMonitorIdentifier,
       "FlowIdentifier": FlowIdentifier,
       "FlowPointType": FlowPointType,
       "FlowPointIdentifier": FlowPointIdentifier,
       "FlowPointInterface": FlowPointInterface,
       "FlowPointDot1qVlan": FlowPointDot1qVlan,
       "FlowMetrics": FlowMetrics,
       "FlowCfgRateType": FlowCfgRateType,
       "FlowBitRateUnits": FlowBitRateUnits,
       "FlowMetricScale": FlowMetricScale,
       "FlowMetricPrecision": FlowMetricPrecision,
       "FlowMetricValue": FlowMetricValue,
       "FlowMonitorConditions": FlowMonitorConditions,
       "FlowMonitorConditionsProfile": FlowMonitorConditionsProfile,
       "FlowMonitorConditionsProfileOrZero": FlowMonitorConditionsProfileOrZero,
       "FlowMonitorConditionIdentifier": FlowMonitorConditionIdentifier,
       "FlowMonitorAlarmGroupIdentifier": FlowMonitorAlarmGroupIdentifier,
       "FlowSetIdentifier": FlowSetIdentifier,
       "ciscoFlowMonitorTcMIB": ciscoFlowMonitorTcMIB}
)
