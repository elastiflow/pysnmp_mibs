# SNMP MIB module (TIMA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/mergedk_47924/TIMA-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:24:05 2025
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

tima = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47924, 100)
)
if mibBuilder.loadTexts:
    tima.setRevisions(
        ("2016-08-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mergedk_ObjectIdentity = ObjectIdentity
mergedk = _Mergedk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47924)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47924, 100, 0)
)
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47924, 100, 1)
)
_Sku_Type = DisplayString
_Sku_Object = MibScalar
sku = _Sku_Object(
    (1, 3, 6, 1, 4, 1, 47924, 100, 1, 1),
    _Sku_Type()
)
sku.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sku.setStatus("current")
_SerialNr_Type = DisplayString
_SerialNr_Object = MibScalar
serialNr = _SerialNr_Object(
    (1, 3, 6, 1, 4, 1, 47924, 100, 1, 2),
    _SerialNr_Type()
)
serialNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNr.setStatus("current")
_UserId_Type = DisplayString
_UserId_Object = MibScalar
userId = _UserId_Object(
    (1, 3, 6, 1, 4, 1, 47924, 100, 1, 3),
    _UserId_Type()
)
userId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userId.setStatus("current")
_FwVersion_Type = DisplayString
_FwVersion_Object = MibScalar
fwVersion = _FwVersion_Object(
    (1, 3, 6, 1, 4, 1, 47924, 100, 1, 4),
    _FwVersion_Type()
)
fwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwVersion.setStatus("current")


class _UsedSV_Type(Integer32):
    """Custom type usedSV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_UsedSV_Type.__name__ = "Integer32"
_UsedSV_Object = MibScalar
usedSV = _UsedSV_Object(
    (1, 3, 6, 1, 4, 1, 47924, 100, 1, 5),
    _UsedSV_Type()
)
usedSV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usedSV.setStatus("current")


class _LockedSV_Type(Integer32):
    """Custom type lockedSV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_LockedSV_Type.__name__ = "Integer32"
_LockedSV_Object = MibScalar
lockedSV = _LockedSV_Object(
    (1, 3, 6, 1, 4, 1, 47924, 100, 1, 6),
    _LockedSV_Type()
)
lockedSV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lockedSV.setStatus("current")


class _TrackedSV_Type(Integer32):
    """Custom type trackedSV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_TrackedSV_Type.__name__ = "Integer32"
_TrackedSV_Object = MibScalar
trackedSV = _TrackedSV_Object(
    (1, 3, 6, 1, 4, 1, 47924, 100, 1, 7),
    _TrackedSV_Type()
)
trackedSV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trackedSV.setStatus("current")


class _AntState_Type(Integer32):
    """Custom type antState based on Integer32"""
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
        *(("ok", 1),
          ("open", 2),
          ("short", 3),
          ("unknown", 4))
    )


_AntState_Type.__name__ = "Integer32"
_AntState_Object = MibScalar
antState = _AntState_Object(
    (1, 3, 6, 1, 4, 1, 47924, 100, 1, 8),
    _AntState_Type()
)
antState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    antState.setStatus("current")


class _GpsState_Type(Integer32):
    """Custom type gpsState based on Integer32"""
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
        *(("notime", 1),
          ("gpsfix", 2),
          ("locked", 3),
          ("holdover", 4),
          ("lowquality", 5),
          ("badtime", 6))
    )


_GpsState_Type.__name__ = "Integer32"
_GpsState_Object = MibScalar
gpsState = _GpsState_Object(
    (1, 3, 6, 1, 4, 1, 47924, 100, 1, 9),
    _GpsState_Type()
)
gpsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsState.setStatus("current")

# Managed Objects groups

statusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47924, 100, 91)
)
statusGroup.setObjects(
      *(("TIMA-MIB", "sku"),
        ("TIMA-MIB", "serialNr"),
        ("TIMA-MIB", "userId"),
        ("TIMA-MIB", "fwVersion"),
        ("TIMA-MIB", "usedSV"),
        ("TIMA-MIB", "lockedSV"),
        ("TIMA-MIB", "trackedSV"),
        ("TIMA-MIB", "antState"),
        ("TIMA-MIB", "gpsState"))
)
if mibBuilder.loadTexts:
    statusGroup.setStatus("current")


# Notification objects

trapAntOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 47924, 100, 0, 1)
)
if mibBuilder.loadTexts:
    trapAntOpen.setStatus(
        "current"
    )

trapAntShort = NotificationType(
    (1, 3, 6, 1, 4, 1, 47924, 100, 0, 2)
)
if mibBuilder.loadTexts:
    trapAntShort.setStatus(
        "current"
    )

trapLowQuality = NotificationType(
    (1, 3, 6, 1, 4, 1, 47924, 100, 0, 3)
)
if mibBuilder.loadTexts:
    trapLowQuality.setStatus(
        "current"
    )

trapBadTime = NotificationType(
    (1, 3, 6, 1, 4, 1, 47924, 100, 0, 4)
)
if mibBuilder.loadTexts:
    trapBadTime.setStatus(
        "current"
    )

trapPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 47924, 100, 0, 5)
)
if mibBuilder.loadTexts:
    trapPowerSupplyFailure.setStatus(
        "current"
    )


# Notifications groups

trapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 47924, 100, 90)
)
trapsGroup.setObjects(
      *(("TIMA-MIB", "trapAntOpen"),
        ("TIMA-MIB", "trapAntShort"),
        ("TIMA-MIB", "trapLowQuality"),
        ("TIMA-MIB", "trapBadTime"),
        ("TIMA-MIB", "trapPowerSupplyFailure"))
)
if mibBuilder.loadTexts:
    trapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMA-MIB",
    **{"mergedk": mergedk,
       "tima": tima,
       "traps": traps,
       "trapAntOpen": trapAntOpen,
       "trapAntShort": trapAntShort,
       "trapLowQuality": trapLowQuality,
       "trapBadTime": trapBadTime,
       "trapPowerSupplyFailure": trapPowerSupplyFailure,
       "status": status,
       "sku": sku,
       "serialNr": serialNr,
       "userId": userId,
       "fwVersion": fwVersion,
       "usedSV": usedSV,
       "lockedSV": lockedSV,
       "trackedSV": trackedSV,
       "antState": antState,
       "gpsState": gpsState,
       "trapsGroup": trapsGroup,
       "statusGroup": statusGroup}
)
