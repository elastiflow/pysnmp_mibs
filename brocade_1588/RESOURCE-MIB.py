# SNMP MIB module (RESOURCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/brocade_1588/RESOURCE-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:12:33 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(sw,) = mibBuilder.importSymbols(
    "SWBASE-MIB",
    "sw")


# MODULE-IDENTITY

swCpuOrMemoryUsage = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 26)
)
if mibBuilder.loadTexts:
    swCpuOrMemoryUsage.setRevisions(
        ("1911-04-15 18:30",
         "1913-06-05 11:30")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _SwCpuUsage_Type(Integer32):
    """Custom type swCpuUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SwCpuUsage_Type.__name__ = "Integer32"
_SwCpuUsage_Object = MibScalar
swCpuUsage = _SwCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 26, 1),
    _SwCpuUsage_Type()
)
swCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCpuUsage.setStatus("current")


class _SwCpuNoOfRetries_Type(Integer32):
    """Custom type swCpuNoOfRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SwCpuNoOfRetries_Type.__name__ = "Integer32"
_SwCpuNoOfRetries_Object = MibScalar
swCpuNoOfRetries = _SwCpuNoOfRetries_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 26, 2),
    _SwCpuNoOfRetries_Type()
)
swCpuNoOfRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCpuNoOfRetries.setStatus("current")


class _SwCpuUsageLimit_Type(Integer32):
    """Custom type swCpuUsageLimit based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SwCpuUsageLimit_Type.__name__ = "Integer32"
_SwCpuUsageLimit_Object = MibScalar
swCpuUsageLimit = _SwCpuUsageLimit_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 26, 3),
    _SwCpuUsageLimit_Type()
)
swCpuUsageLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCpuUsageLimit.setStatus("current")


class _SwCpuPollingInterval_Type(Integer32):
    """Custom type swCpuPollingInterval based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_SwCpuPollingInterval_Type.__name__ = "Integer32"
_SwCpuPollingInterval_Object = MibScalar
swCpuPollingInterval = _SwCpuPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 26, 4),
    _SwCpuPollingInterval_Type()
)
swCpuPollingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCpuPollingInterval.setStatus("current")
if mibBuilder.loadTexts:
    swCpuPollingInterval.setUnits("seconds")


class _SwCpuAction_Type(Integer32):
    """Custom type swCpuAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("raslog", 1),
          ("snmp", 2),
          ("raslogandSnmp", 3))
    )


_SwCpuAction_Type.__name__ = "Integer32"
_SwCpuAction_Object = MibScalar
swCpuAction = _SwCpuAction_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 26, 5),
    _SwCpuAction_Type()
)
swCpuAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCpuAction.setStatus("current")
_SwMemUsage_Type = Integer32
_SwMemUsage_Object = MibScalar
swMemUsage = _SwMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 26, 6),
    _SwMemUsage_Type()
)
swMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMemUsage.setStatus("current")


class _SwMemNoOfRetries_Type(Integer32):
    """Custom type swMemNoOfRetries based on Integer32"""
    defaultValue = 3


_SwMemNoOfRetries_Type.__name__ = "Integer32"
_SwMemNoOfRetries_Object = MibScalar
swMemNoOfRetries = _SwMemNoOfRetries_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 26, 7),
    _SwMemNoOfRetries_Type()
)
swMemNoOfRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMemNoOfRetries.setStatus("current")


class _SwMemUsageLimit_Type(Integer32):
    """Custom type swMemUsageLimit based on Integer32"""
    defaultValue = 60


_SwMemUsageLimit_Type.__name__ = "Integer32"
_SwMemUsageLimit_Object = MibScalar
swMemUsageLimit = _SwMemUsageLimit_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 26, 8),
    _SwMemUsageLimit_Type()
)
swMemUsageLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMemUsageLimit.setStatus("current")


class _SwMemPollingInterval_Type(Integer32):
    """Custom type swMemPollingInterval based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_SwMemPollingInterval_Type.__name__ = "Integer32"
_SwMemPollingInterval_Object = MibScalar
swMemPollingInterval = _SwMemPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 26, 9),
    _SwMemPollingInterval_Type()
)
swMemPollingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMemPollingInterval.setStatus("current")
if mibBuilder.loadTexts:
    swMemPollingInterval.setUnits("seconds")


class _SwMemAction_Type(Integer32):
    """Custom type swMemAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("raslog", 1),
          ("snmp", 2),
          ("raslogandSnmp", 3))
    )


_SwMemAction_Type.__name__ = "Integer32"
_SwMemAction_Object = MibScalar
swMemAction = _SwMemAction_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 26, 10),
    _SwMemAction_Type()
)
swMemAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMemAction.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RESOURCE-MIB",
    **{"swCpuOrMemoryUsage": swCpuOrMemoryUsage,
       "swCpuUsage": swCpuUsage,
       "swCpuNoOfRetries": swCpuNoOfRetries,
       "swCpuUsageLimit": swCpuUsageLimit,
       "swCpuPollingInterval": swCpuPollingInterval,
       "swCpuAction": swCpuAction,
       "swMemUsage": swMemUsage,
       "swMemNoOfRetries": swMemNoOfRetries,
       "swMemUsageLimit": swMemUsageLimit,
       "swMemPollingInterval": swMemPollingInterval,
       "swMemAction": swMemAction}
)
