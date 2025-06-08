# SNMP MIB module (NDS-DTH3-MONITOR) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/news_digital_1855/NDS-DTH3-MONITOR.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:44:39 2025
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

ndsDTH3Encoder = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Monitor_ObjectIdentity = ObjectIdentity
monitor = _Monitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 14)
)


class _MonitorTargetIPAddress_Type(DisplayString):
    """Custom type monitorTargetIPAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MonitorTargetIPAddress_Type.__name__ = "DisplayString"
_MonitorTargetIPAddress_Object = MibScalar
monitorTargetIPAddress = _MonitorTargetIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 14, 1),
    _MonitorTargetIPAddress_Type()
)
monitorTargetIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorTargetIPAddress.setStatus("current")


class _MonitorTargetUDPPort_Type(Integer32):
    """Custom type monitorTargetUDPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 65535),
    )


_MonitorTargetUDPPort_Type.__name__ = "Integer32"
_MonitorTargetUDPPort_Object = MibScalar
monitorTargetUDPPort = _MonitorTargetUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 14, 2),
    _MonitorTargetUDPPort_Type()
)
monitorTargetUDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorTargetUDPPort.setStatus("current")


class _MonitorVideoFramesToSend_Type(Integer32):
    """Custom type monitorVideoFramesToSend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MonitorVideoFramesToSend_Type.__name__ = "Integer32"
_MonitorVideoFramesToSend_Object = MibScalar
monitorVideoFramesToSend = _MonitorVideoFramesToSend_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 14, 3),
    _MonitorVideoFramesToSend_Type()
)
monitorVideoFramesToSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorVideoFramesToSend.setStatus("current")


class _MonitorMaxPictureRate_Type(Integer32):
    """Custom type monitorMaxPictureRate based on Integer32"""
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
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("rate-1-per-minute", 0),
          ("rate-2-per-minute", 1),
          ("rate-5-per-minute", 2),
          ("rate-10-per-minute", 3),
          ("rate-15-per-minute", 4),
          ("rate-30-per-minute", 5),
          ("rate-60-per-minute", 6),
          ("rate-75-per-minute", 7),
          ("rate-100-per-minute", 8),
          ("rate-150-per-minute", 9),
          ("rate-300-per-minute", 10),
          ("rate-450-per-minute", 11))
    )


_MonitorMaxPictureRate_Type.__name__ = "Integer32"
_MonitorMaxPictureRate_Object = MibScalar
monitorMaxPictureRate = _MonitorMaxPictureRate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 14, 4),
    _MonitorMaxPictureRate_Type()
)
monitorMaxPictureRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorMaxPictureRate.setStatus("current")


class _MonitorActualPictureRate_Type(Integer32):
    """Custom type monitorActualPictureRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 450),
    )


_MonitorActualPictureRate_Type.__name__ = "Integer32"
_MonitorActualPictureRate_Object = MibScalar
monitorActualPictureRate = _MonitorActualPictureRate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 14, 5),
    _MonitorActualPictureRate_Type()
)
monitorActualPictureRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorActualPictureRate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NDS-DTH3-MONITOR",
    **{"ndsDTH3Encoder": ndsDTH3Encoder,
       "monitor": monitor,
       "monitorTargetIPAddress": monitorTargetIPAddress,
       "monitorTargetUDPPort": monitorTargetUDPPort,
       "monitorVideoFramesToSend": monitorVideoFramesToSend,
       "monitorMaxPictureRate": monitorMaxPictureRate,
       "monitorActualPictureRate": monitorActualPictureRate}
)
