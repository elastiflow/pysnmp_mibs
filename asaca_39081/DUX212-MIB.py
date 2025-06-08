# SNMP MIB module (DUX212-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/asaca_39081/DUX212-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 09:35:25 2025
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

(DuxAlarmStatus,
 DuxTrapMask,
 dux) = mibBuilder.importSymbols(
    "DUX-MIB",
    "DuxAlarmStatus",
    "DuxTrapMask",
    "dux")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

dux212 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39081, 12, 212)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dux212Table_Object = MibTable
dux212Table = _Dux212Table_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 212, 1)
)
if mibBuilder.loadTexts:
    dux212Table.setStatus("current")
_Dux212Entry_Object = MibTableRow
dux212Entry = _Dux212Entry_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 212, 1, 1)
)
dux212Entry.setIndexNames(
    (0, "DUX212-MIB", "dux212Index"),
)
if mibBuilder.loadTexts:
    dux212Entry.setStatus("current")


class _Dux212Index_Type(Integer32):
    """Custom type dux212Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Dux212Index_Type.__name__ = "Integer32"
_Dux212Index_Object = MibTableColumn
dux212Index = _Dux212Index_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 212, 1, 1, 1),
    _Dux212Index_Type()
)
dux212Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dux212Index.setStatus("current")


class _Dux212Version_Type(OctetString):
    """Custom type dux212Version based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Dux212Version_Type.__name__ = "OctetString"
_Dux212Version_Object = MibTableColumn
dux212Version = _Dux212Version_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 212, 1, 1, 2),
    _Dux212Version_Type()
)
dux212Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dux212Version.setStatus("current")


class _Dux212Ch1StandbyEventID_Type(OctetString):
    """Custom type dux212Ch1StandbyEventID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Dux212Ch1StandbyEventID_Type.__name__ = "OctetString"
_Dux212Ch1StandbyEventID_Object = MibTableColumn
dux212Ch1StandbyEventID = _Dux212Ch1StandbyEventID_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 212, 1, 1, 3),
    _Dux212Ch1StandbyEventID_Type()
)
dux212Ch1StandbyEventID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dux212Ch1StandbyEventID.setStatus("current")


class _Dux212Ch2StandbyEventID_Type(OctetString):
    """Custom type dux212Ch2StandbyEventID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Dux212Ch2StandbyEventID_Type.__name__ = "OctetString"
_Dux212Ch2StandbyEventID_Object = MibTableColumn
dux212Ch2StandbyEventID = _Dux212Ch2StandbyEventID_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 212, 1, 1, 4),
    _Dux212Ch2StandbyEventID_Type()
)
dux212Ch2StandbyEventID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dux212Ch2StandbyEventID.setStatus("current")
_Dux212Ch1SuperStatus_Type = Integer32
_Dux212Ch1SuperStatus_Object = MibTableColumn
dux212Ch1SuperStatus = _Dux212Ch1SuperStatus_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 212, 1, 1, 5),
    _Dux212Ch1SuperStatus_Type()
)
dux212Ch1SuperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dux212Ch1SuperStatus.setStatus("current")
_Dux212Ch2SuperStatus_Type = Integer32
_Dux212Ch2SuperStatus_Object = MibTableColumn
dux212Ch2SuperStatus = _Dux212Ch2SuperStatus_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 212, 1, 1, 6),
    _Dux212Ch2SuperStatus_Type()
)
dux212Ch2SuperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dux212Ch2SuperStatus.setStatus("current")
_Dux212BoardTemperature_Type = Integer32
_Dux212BoardTemperature_Object = MibTableColumn
dux212BoardTemperature = _Dux212BoardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 212, 1, 1, 8),
    _Dux212BoardTemperature_Type()
)
dux212BoardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dux212BoardTemperature.setStatus("current")
_Dux212WdtStatus_Type = DuxAlarmStatus
_Dux212WdtStatus_Object = MibTableColumn
dux212WdtStatus = _Dux212WdtStatus_Object(
    (1, 3, 6, 1, 4, 1, 39081, 12, 212, 1, 1, 10),
    _Dux212WdtStatus_Type()
)
dux212WdtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dux212WdtStatus.setStatus("current")
_Dux212Traps_ObjectIdentity = ObjectIdentity
dux212Traps = _Dux212Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39081, 12, 212, 2)
)

# Managed Objects groups


# Notification objects

dux212BoardTemperatureOverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39081, 12, 212, 2, 3)
)
dux212BoardTemperatureOverTrap.setObjects(
      *(("DUX212-MIB", "dux212Index"),
        ("DUX212-MIB", "dux212BoardTemperature"))
)
if mibBuilder.loadTexts:
    dux212BoardTemperatureOverTrap.setStatus(
        "current"
    )

dux212BoardTemperatureNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39081, 12, 212, 2, 4)
)
dux212BoardTemperatureNormalTrap.setObjects(
      *(("DUX212-MIB", "dux212Index"),
        ("DUX212-MIB", "dux212BoardTemperature"))
)
if mibBuilder.loadTexts:
    dux212BoardTemperatureNormalTrap.setStatus(
        "current"
    )

dux212WdtFailedTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 39081, 12, 212, 2, 7)
)
dux212WdtFailedTraps.setObjects(
      *(("DUX212-MIB", "dux212Index"),
        ("DUX212-MIB", "dux212WdtStatus"))
)
if mibBuilder.loadTexts:
    dux212WdtFailedTraps.setStatus(
        "current"
    )

dux212WdtNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 39081, 12, 212, 2, 8)
)
dux212WdtNormalTrap.setObjects(
      *(("DUX212-MIB", "dux212Index"),
        ("DUX212-MIB", "dux212WdtStatus"))
)
if mibBuilder.loadTexts:
    dux212WdtNormalTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DUX212-MIB",
    **{"dux212": dux212,
       "dux212Table": dux212Table,
       "dux212Entry": dux212Entry,
       "dux212Index": dux212Index,
       "dux212Version": dux212Version,
       "dux212Ch1StandbyEventID": dux212Ch1StandbyEventID,
       "dux212Ch2StandbyEventID": dux212Ch2StandbyEventID,
       "dux212Ch1SuperStatus": dux212Ch1SuperStatus,
       "dux212Ch2SuperStatus": dux212Ch2SuperStatus,
       "dux212BoardTemperature": dux212BoardTemperature,
       "dux212WdtStatus": dux212WdtStatus,
       "dux212Traps": dux212Traps,
       "dux212BoardTemperatureOverTrap": dux212BoardTemperatureOverTrap,
       "dux212BoardTemperatureNormalTrap": dux212BoardTemperatureNormalTrap,
       "dux212WdtFailedTraps": dux212WdtFailedTraps,
       "dux212WdtNormalTrap": dux212WdtNormalTrap}
)
