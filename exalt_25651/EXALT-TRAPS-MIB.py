# SNMP MIB module (EXALT-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/exalt_25651/EXALT-TRAPS-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:22:49 2025
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

(productsMIBNotifications,) = mibBuilder.importSymbols(
    "ExaltComProducts",
    "productsMIBNotifications")

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



# MIB Managed Objects in the order of their OIDs

_Exaltnotifs_ObjectIdentity = ObjectIdentity
exaltnotifs = _Exaltnotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 1, 1)
)
_ExaltnotifObjects_ObjectIdentity = ObjectIdentity
exaltnotifObjects = _ExaltnotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 1, 2)
)
_LocRadioStat_Type = Integer32
_LocRadioStat_Object = MibScalar
locRadioStat = _LocRadioStat_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 1, 2, 1),
    _LocRadioStat_Type()
)
locRadioStat.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    locRadioStat.setStatus("current")
_RemRadioStat_Type = Integer32
_RemRadioStat_Object = MibScalar
remRadioStat = _RemRadioStat_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 1, 2, 2),
    _RemRadioStat_Type()
)
remRadioStat.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    remRadioStat.setStatus("current")
_LocRSLStat_Type = Integer32
_LocRSLStat_Object = MibScalar
locRSLStat = _LocRSLStat_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 1, 2, 3),
    _LocRSLStat_Type()
)
locRSLStat.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    locRSLStat.setStatus("current")
_LocTempStat_Type = Integer32
_LocTempStat_Object = MibScalar
locTempStat = _LocTempStat_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 1, 2, 4),
    _LocTempStat_Type()
)
locTempStat.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    locTempStat.setStatus("current")

# Managed Objects groups


# Notification objects

exalt_cold_start_notif = NotificationType(
    (1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 1)
)
exalt_cold_start_notif.setObjects(
    ("EXALT-TRAPS-MIB", "modelName")
)
if mibBuilder.loadTexts:
    exalt_cold_start_notif.setStatus(
        "current"
    )

radio_syn_alm_notif = NotificationType(
    (1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 2)
)
radio_syn_alm_notif.setObjects(
    ("EXALT-TRAPS-MIB", "locLinkState")
)
if mibBuilder.loadTexts:
    radio_syn_alm_notif.setStatus(
        "current"
    )

loc_radio_stat_notif = NotificationType(
    (1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 3)
)
loc_radio_stat_notif.setObjects(
    ("EXALT-TRAPS-MIB", "locRadioStat")
)
if mibBuilder.loadTexts:
    loc_radio_stat_notif.setStatus(
        "current"
    )

rem_radio_stat_notif = NotificationType(
    (1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 4)
)
rem_radio_stat_notif.setObjects(
    ("EXALT-TRAPS-MIB", "remRadioStat")
)
if mibBuilder.loadTexts:
    rem_radio_stat_notif.setStatus(
        "current"
    )

loc_rsl_stat_notif = NotificationType(
    (1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 5)
)
loc_rsl_stat_notif.setObjects(
    ("EXALT-TRAPS-MIB", "locRSLStat")
)
if mibBuilder.loadTexts:
    loc_rsl_stat_notif.setStatus(
        "current"
    )

loc_temp_stat_notif = NotificationType(
    (1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 6)
)
loc_temp_stat_notif.setObjects(
    ("EXALT-TRAPS-MIB", "locTempStat")
)
if mibBuilder.loadTexts:
    loc_temp_stat_notif.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXALT-TRAPS-MIB",
    **{"exaltnotifs": exaltnotifs,
       "exalt-cold-start-notif": exalt_cold_start_notif,
       "radio-syn-alm-notif": radio_syn_alm_notif,
       "loc-radio-stat-notif": loc_radio_stat_notif,
       "rem-radio-stat-notif": rem_radio_stat_notif,
       "loc-rsl-stat-notif": loc_rsl_stat_notif,
       "loc-temp-stat-notif": loc_temp_stat_notif,
       "exaltnotifObjects": exaltnotifObjects,
       "locRadioStat": locRadioStat,
       "remRadioStat": remRadioStat,
       "locRSLStat": locRSLStat,
       "locTempStat": locTempStat}
)
