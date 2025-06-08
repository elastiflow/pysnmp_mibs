# SNMP MIB module (ME1200-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-TC.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:05:31 2025
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



class ME1200Integer8(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )



class ME1200Integer16(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )



class ME1200Integer64(TextualConvention, OctetString):
    status = "current"
    displayHint = "8x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8



class ME1200Unsigned8(TextualConvention, Gauge32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class ME1200Unsigned16(TextualConvention, Gauge32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class ME1200Unsigned64(TextualConvention, OctetString):
    status = "current"
    displayHint = "8x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8



class ME1200TimeStamp(TextualConvention, OctetString):
    status = "current"
    displayHint = "8x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8



class ME1200EtherType(TextualConvention, Gauge32):
    status = "current"
    displayHint = "x"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class ME1200InterfaceIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class ME1200RowEditorState(TextualConvention, Gauge32):
    status = "current"
    displayHint = "d"


class ME1200Percent(TextualConvention, Gauge32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class ME1200PortList(TextualConvention, OctetString):
    status = "current"
    displayHint = "8x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8



class ME1200PortListStackable(TextualConvention, OctetString):
    status = "current"
    displayHint = "128x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixedLength = 128



class ME1200Vlan(TextualConvention, Gauge32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )



class ME1200VlanOrZero(TextualConvention, Gauge32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )



class ME1200VlanListQuarter(TextualConvention, OctetString):
    status = "current"
    displayHint = "128x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixedLength = 128



class ME1200DisplayString(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class ME1200InetAddress(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 253),
    )



class ME1200VclProtoEncap(TextualConvention, OctetString):
    status = "current"
    displayHint = "6x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 6),
    )



class ME1200MepDmTimeUnit(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("microSeconds", 0),
          ("nanoSeconds", 1))
    )



class ME1200MepInstanceDirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )



class ME1200MepTxRate(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("frames300PerSecond", 1),
          ("frames100PerSecond", 2),
          ("frames10PerSecond", 3),
          ("frames1PerSecond", 4),
          ("frames6PerMinute", 5),
          ("frames1PerMinute", 6),
          ("frames6PerHour", 7))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-TC",
    **{"ME1200Integer8": ME1200Integer8,
       "ME1200Integer16": ME1200Integer16,
       "ME1200Integer64": ME1200Integer64,
       "ME1200Unsigned8": ME1200Unsigned8,
       "ME1200Unsigned16": ME1200Unsigned16,
       "ME1200Unsigned64": ME1200Unsigned64,
       "ME1200TimeStamp": ME1200TimeStamp,
       "ME1200EtherType": ME1200EtherType,
       "ME1200InterfaceIndex": ME1200InterfaceIndex,
       "ME1200RowEditorState": ME1200RowEditorState,
       "ME1200Percent": ME1200Percent,
       "ME1200PortList": ME1200PortList,
       "ME1200PortListStackable": ME1200PortListStackable,
       "ME1200Vlan": ME1200Vlan,
       "ME1200VlanOrZero": ME1200VlanOrZero,
       "ME1200VlanListQuarter": ME1200VlanListQuarter,
       "ME1200DisplayString": ME1200DisplayString,
       "ME1200InetAddress": ME1200InetAddress,
       "ME1200VclProtoEncap": ME1200VclProtoEncap,
       "ME1200MepDmTimeUnit": ME1200MepDmTimeUnit,
       "ME1200MepInstanceDirection": ME1200MepInstanceDirection,
       "ME1200MepTxRate": ME1200MepTxRate}
)
