# SNMP MIB module (CONEL-GPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/advantech_30140/CONEL-GPS-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 00:15:05 2025
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Conel_ObjectIdentity = ObjectIdentity
conel = _Conel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140)
)
_Gps_ObjectIdentity = ObjectIdentity
gps = _Gps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30140, 7)
)
_GpsTimeUTC_Type = OctetString
_GpsTimeUTC_Object = MibScalar
gpsTimeUTC = _GpsTimeUTC_Object(
    (1, 3, 6, 1, 4, 1, 30140, 7, 1),
    _GpsTimeUTC_Type()
)
gpsTimeUTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsTimeUTC.setStatus("current")
_GpsLatitude_Type = OctetString
_GpsLatitude_Object = MibScalar
gpsLatitude = _GpsLatitude_Object(
    (1, 3, 6, 1, 4, 1, 30140, 7, 2),
    _GpsLatitude_Type()
)
gpsLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsLatitude.setStatus("current")
_GpsLongitude_Type = OctetString
_GpsLongitude_Object = MibScalar
gpsLongitude = _GpsLongitude_Object(
    (1, 3, 6, 1, 4, 1, 30140, 7, 3),
    _GpsLongitude_Type()
)
gpsLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsLongitude.setStatus("current")
_GpsAltitude_Type = OctetString
_GpsAltitude_Object = MibScalar
gpsAltitude = _GpsAltitude_Object(
    (1, 3, 6, 1, 4, 1, 30140, 7, 4),
    _GpsAltitude_Type()
)
gpsAltitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsAltitude.setStatus("current")
_GpsSatellites_Type = Integer32
_GpsSatellites_Object = MibScalar
gpsSatellites = _GpsSatellites_Object(
    (1, 3, 6, 1, 4, 1, 30140, 7, 5),
    _GpsSatellites_Type()
)
gpsSatellites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsSatellites.setStatus("current")
_GpsFixStatus_Type = OctetString
_GpsFixStatus_Object = MibScalar
gpsFixStatus = _GpsFixStatus_Object(
    (1, 3, 6, 1, 4, 1, 30140, 7, 6),
    _GpsFixStatus_Type()
)
gpsFixStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsFixStatus.setStatus("current")
_GpsSpeedOverGround_Type = OctetString
_GpsSpeedOverGround_Object = MibScalar
gpsSpeedOverGround = _GpsSpeedOverGround_Object(
    (1, 3, 6, 1, 4, 1, 30140, 7, 7),
    _GpsSpeedOverGround_Type()
)
gpsSpeedOverGround.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsSpeedOverGround.setStatus("current")
_GpsCourseOverGround_Type = OctetString
_GpsCourseOverGround_Object = MibScalar
gpsCourseOverGround = _GpsCourseOverGround_Object(
    (1, 3, 6, 1, 4, 1, 30140, 7, 8),
    _GpsCourseOverGround_Type()
)
gpsCourseOverGround.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsCourseOverGround.setStatus("current")
_GpsDate_Type = OctetString
_GpsDate_Object = MibScalar
gpsDate = _GpsDate_Object(
    (1, 3, 6, 1, 4, 1, 30140, 7, 9),
    _GpsDate_Type()
)
gpsDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsDate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CONEL-GPS-MIB",
    **{"conel": conel,
       "gps": gps,
       "gpsTimeUTC": gpsTimeUTC,
       "gpsLatitude": gpsLatitude,
       "gpsLongitude": gpsLongitude,
       "gpsAltitude": gpsAltitude,
       "gpsSatellites": gpsSatellites,
       "gpsFixStatus": gpsFixStatus,
       "gpsSpeedOverGround": gpsSpeedOverGround,
       "gpsCourseOverGround": gpsCourseOverGround,
       "gpsDate": gpsDate}
)
