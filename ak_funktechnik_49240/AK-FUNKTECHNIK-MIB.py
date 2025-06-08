# SNMP MIB module (AK-FUNKTECHNIK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ak_funktechnik_49240/AK-FUNKTECHNIK-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 09:19:57 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ak_mib_i = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1)
)
if mibBuilder.loadTexts:
    ak_mib_i.setRevisions(
        ("2016-12-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ak_funktechnik_ObjectIdentity = ObjectIdentity
ak_funktechnik = _Ak_funktechnik_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240)
)
_Ak_devices_i_ObjectIdentity = ObjectIdentity
ak_devices_i = _Ak_devices_i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1)
)
_Ak_ofu_i_ObjectIdentity = ObjectIdentity
ak_ofu_i = _Ak_ofu_i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1)
)
_Ak_info_i_ObjectIdentity = ObjectIdentity
ak_info_i = _Ak_info_i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1)
)
_Ak_device_name_Type = DisplayString
_Ak_device_name_Object = MibScalar
ak_device_name = _Ak_device_name_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 1),
    _Ak_device_name_Type()
)
ak_device_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ak_device_name.setStatus("current")
_Ak_custom_name_Type = DisplayString
_Ak_custom_name_Object = MibScalar
ak_custom_name = _Ak_custom_name_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 2),
    _Ak_custom_name_Type()
)
ak_custom_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ak_custom_name.setStatus("current")
_Ak_location_name_Type = DisplayString
_Ak_location_name_Object = MibScalar
ak_location_name = _Ak_location_name_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 3),
    _Ak_location_name_Type()
)
ak_location_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ak_location_name.setStatus("current")
_Ak_master_slave_parameter_ObjectIdentity = ObjectIdentity
ak_master_slave_parameter = _Ak_master_slave_parameter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 4)
)
_Ak_antennenkabel_ueberwachung_1_Type = DisplayString
_Ak_antennenkabel_ueberwachung_1_Object = MibScalar
ak_antennenkabel_ueberwachung_1 = _Ak_antennenkabel_ueberwachung_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 4, 1),
    _Ak_antennenkabel_ueberwachung_1_Type()
)
ak_antennenkabel_ueberwachung_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ak_antennenkabel_ueberwachung_1.setStatus("current")
_Ak_antennenkabel_ueberwachung_2_Type = DisplayString
_Ak_antennenkabel_ueberwachung_2_Object = MibScalar
ak_antennenkabel_ueberwachung_2 = _Ak_antennenkabel_ueberwachung_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 4, 2),
    _Ak_antennenkabel_ueberwachung_2_Type()
)
ak_antennenkabel_ueberwachung_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ak_antennenkabel_ueberwachung_2.setStatus("current")
_Ak_antennenkabel_ueberwachung_3_Type = DisplayString
_Ak_antennenkabel_ueberwachung_3_Object = MibScalar
ak_antennenkabel_ueberwachung_3 = _Ak_antennenkabel_ueberwachung_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 4, 3),
    _Ak_antennenkabel_ueberwachung_3_Type()
)
ak_antennenkabel_ueberwachung_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ak_antennenkabel_ueberwachung_3.setStatus("current")
_Ak_schranktemperatur_ueberwachung_Type = DisplayString
_Ak_schranktemperatur_ueberwachung_Object = MibScalar
ak_schranktemperatur_ueberwachung = _Ak_schranktemperatur_ueberwachung_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 4, 4),
    _Ak_schranktemperatur_ueberwachung_Type()
)
ak_schranktemperatur_ueberwachung.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ak_schranktemperatur_ueberwachung.setStatus("current")
_Ak_datum_zeit_Type = DisplayString
_Ak_datum_zeit_Object = MibScalar
ak_datum_zeit = _Ak_datum_zeit_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 4, 5),
    _Ak_datum_zeit_Type()
)
ak_datum_zeit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ak_datum_zeit.setStatus("current")
_Ak_status_informationen_ObjectIdentity = ObjectIdentity
ak_status_informationen = _Ak_status_informationen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5)
)
_Info_interne_master_module_ObjectIdentity = ObjectIdentity
info_interne_master_module = _Info_interne_master_module_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1)
)
_MasterTable_basisinfo_Object = MibTable
masterTable_basisinfo = _MasterTable_basisinfo_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    masterTable_basisinfo.setStatus("current")
_ModulEntry_basis_master_Object = MibTableRow
modulEntry_basis_master = _ModulEntry_basis_master_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1, 1)
)
modulEntry_basis_master.setIndexNames(
    (0, "AK-FUNKTECHNIK-MIB", "modulindex-master"),
)
if mibBuilder.loadTexts:
    modulEntry_basis_master.setStatus("current")
_Modulindex_master_Type = DisplayString
_Modulindex_master_Object = MibTableColumn
modulindex_master = _Modulindex_master_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1, 1, 1),
    _Modulindex_master_Type()
)
modulindex_master.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulindex_master.setStatus("current")
_Ska_fehlerstat_master_Type = DisplayString
_Ska_fehlerstat_master_Object = MibTableColumn
ska_fehlerstat_master = _Ska_fehlerstat_master_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1, 1, 2),
    _Ska_fehlerstat_master_Type()
)
ska_fehlerstat_master.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ska_fehlerstat_master.setStatus("current")
_Ska_betriebsstat_master_Type = DisplayString
_Ska_betriebsstat_master_Object = MibTableColumn
ska_betriebsstat_master = _Ska_betriebsstat_master_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1, 1, 3),
    _Ska_betriebsstat_master_Type()
)
ska_betriebsstat_master.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ska_betriebsstat_master.setStatus("current")
_Ska_betriebsstat_quelle_master_Type = DisplayString
_Ska_betriebsstat_quelle_master_Object = MibTableColumn
ska_betriebsstat_quelle_master = _Ska_betriebsstat_quelle_master_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1, 1, 4),
    _Ska_betriebsstat_quelle_master_Type()
)
ska_betriebsstat_quelle_master.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ska_betriebsstat_quelle_master.setStatus("current")
_Ska_autom_abschaltzeit_master_Type = DisplayString
_Ska_autom_abschaltzeit_master_Object = MibTableColumn
ska_autom_abschaltzeit_master = _Ska_autom_abschaltzeit_master_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1, 1, 5),
    _Ska_autom_abschaltzeit_master_Type()
)
ska_autom_abschaltzeit_master.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ska_autom_abschaltzeit_master.setStatus("current")
_Skb_fehlerstat_master_Type = DisplayString
_Skb_fehlerstat_master_Object = MibTableColumn
skb_fehlerstat_master = _Skb_fehlerstat_master_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1, 1, 6),
    _Skb_fehlerstat_master_Type()
)
skb_fehlerstat_master.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skb_fehlerstat_master.setStatus("current")
_Skb_betriebsstat_master_Type = DisplayString
_Skb_betriebsstat_master_Object = MibTableColumn
skb_betriebsstat_master = _Skb_betriebsstat_master_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1, 1, 7),
    _Skb_betriebsstat_master_Type()
)
skb_betriebsstat_master.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skb_betriebsstat_master.setStatus("current")
_Skb_betriebsstat_quelle_master_Type = DisplayString
_Skb_betriebsstat_quelle_master_Object = MibTableColumn
skb_betriebsstat_quelle_master = _Skb_betriebsstat_quelle_master_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1, 1, 8),
    _Skb_betriebsstat_quelle_master_Type()
)
skb_betriebsstat_quelle_master.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skb_betriebsstat_quelle_master.setStatus("current")
_Skb_autom_abschaltzeit_master_Type = DisplayString
_Skb_autom_abschaltzeit_master_Object = MibTableColumn
skb_autom_abschaltzeit_master = _Skb_autom_abschaltzeit_master_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1, 1, 9),
    _Skb_autom_abschaltzeit_master_Type()
)
skb_autom_abschaltzeit_master.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skb_autom_abschaltzeit_master.setStatus("current")
_Skc_fehlerstat_master_Type = DisplayString
_Skc_fehlerstat_master_Object = MibTableColumn
skc_fehlerstat_master = _Skc_fehlerstat_master_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1, 1, 10),
    _Skc_fehlerstat_master_Type()
)
skc_fehlerstat_master.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skc_fehlerstat_master.setStatus("current")
_Skc_betriebsstat_master_Type = DisplayString
_Skc_betriebsstat_master_Object = MibTableColumn
skc_betriebsstat_master = _Skc_betriebsstat_master_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1, 1, 11),
    _Skc_betriebsstat_master_Type()
)
skc_betriebsstat_master.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skc_betriebsstat_master.setStatus("current")
_Skc_betriebsstat_quelle_master_Type = DisplayString
_Skc_betriebsstat_quelle_master_Object = MibTableColumn
skc_betriebsstat_quelle_master = _Skc_betriebsstat_quelle_master_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1, 1, 12),
    _Skc_betriebsstat_quelle_master_Type()
)
skc_betriebsstat_quelle_master.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skc_betriebsstat_quelle_master.setStatus("current")
_Skc_autom_abschaltzeit_master_Type = DisplayString
_Skc_autom_abschaltzeit_master_Object = MibTableColumn
skc_autom_abschaltzeit_master = _Skc_autom_abschaltzeit_master_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1, 1, 13),
    _Skc_autom_abschaltzeit_master_Type()
)
skc_autom_abschaltzeit_master.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skc_autom_abschaltzeit_master.setStatus("current")
_Fehlerausgang_rel_1_master_Type = DisplayString
_Fehlerausgang_rel_1_master_Object = MibTableColumn
fehlerausgang_rel_1_master = _Fehlerausgang_rel_1_master_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1, 1, 14),
    _Fehlerausgang_rel_1_master_Type()
)
fehlerausgang_rel_1_master.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fehlerausgang_rel_1_master.setStatus("current")
_Fehlerausgang_rel_2_master_Type = DisplayString
_Fehlerausgang_rel_2_master_Object = MibTableColumn
fehlerausgang_rel_2_master = _Fehlerausgang_rel_2_master_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1, 1, 15),
    _Fehlerausgang_rel_2_master_Type()
)
fehlerausgang_rel_2_master.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fehlerausgang_rel_2_master.setStatus("current")
_Steuerausgang_x1000_master_Type = DisplayString
_Steuerausgang_x1000_master_Object = MibTableColumn
steuerausgang_x1000_master = _Steuerausgang_x1000_master_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1, 1, 16),
    _Steuerausgang_x1000_master_Type()
)
steuerausgang_x1000_master.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steuerausgang_x1000_master.setStatus("current")
_Steuerausgang_x1002_master_Type = DisplayString
_Steuerausgang_x1002_master_Object = MibTableColumn
steuerausgang_x1002_master = _Steuerausgang_x1002_master_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1, 1, 17),
    _Steuerausgang_x1002_master_Type()
)
steuerausgang_x1002_master.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steuerausgang_x1002_master.setStatus("current")
_Steuerausgang_x2001_8_master_Type = DisplayString
_Steuerausgang_x2001_8_master_Object = MibTableColumn
steuerausgang_x2001_8_master = _Steuerausgang_x2001_8_master_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1, 1, 18),
    _Steuerausgang_x2001_8_master_Type()
)
steuerausgang_x2001_8_master.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steuerausgang_x2001_8_master.setStatus("current")
_Steuerausgang_x2001_10_master_Type = DisplayString
_Steuerausgang_x2001_10_master_Object = MibTableColumn
steuerausgang_x2001_10_master = _Steuerausgang_x2001_10_master_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1, 1, 19),
    _Steuerausgang_x2001_10_master_Type()
)
steuerausgang_x2001_10_master.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steuerausgang_x2001_10_master.setStatus("current")
_Serviceschalter_master_Type = DisplayString
_Serviceschalter_master_Object = MibTableColumn
serviceschalter_master = _Serviceschalter_master_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1, 1, 20),
    _Serviceschalter_master_Type()
)
serviceschalter_master.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceschalter_master.setStatus("current")
_Steuereingang_bma_master_Type = DisplayString
_Steuereingang_bma_master_Object = MibTableColumn
steuereingang_bma_master = _Steuereingang_bma_master_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1, 1, 21),
    _Steuereingang_bma_master_Type()
)
steuereingang_bma_master.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steuereingang_bma_master.setStatus("current")
_Steuereingang_opt1_master_Type = DisplayString
_Steuereingang_opt1_master_Object = MibTableColumn
steuereingang_opt1_master = _Steuereingang_opt1_master_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1, 1, 22),
    _Steuereingang_opt1_master_Type()
)
steuereingang_opt1_master.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steuereingang_opt1_master.setStatus("current")
_Steuereingang_opt2_master_Type = DisplayString
_Steuereingang_opt2_master_Object = MibTableColumn
steuereingang_opt2_master = _Steuereingang_opt2_master_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1, 1, 23),
    _Steuereingang_opt2_master_Type()
)
steuereingang_opt2_master.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steuereingang_opt2_master.setStatus("current")
_Antennenleitungs_ueberwachung_1_master_Type = DisplayString
_Antennenleitungs_ueberwachung_1_master_Object = MibTableColumn
antennenleitungs_ueberwachung_1_master = _Antennenleitungs_ueberwachung_1_master_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1, 1, 24),
    _Antennenleitungs_ueberwachung_1_master_Type()
)
antennenleitungs_ueberwachung_1_master.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    antennenleitungs_ueberwachung_1_master.setStatus("current")
_Antennenleitungs_ueberwachung_2_master_Type = DisplayString
_Antennenleitungs_ueberwachung_2_master_Object = MibTableColumn
antennenleitungs_ueberwachung_2_master = _Antennenleitungs_ueberwachung_2_master_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1, 1, 25),
    _Antennenleitungs_ueberwachung_2_master_Type()
)
antennenleitungs_ueberwachung_2_master.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    antennenleitungs_ueberwachung_2_master.setStatus("current")
_Antennenleitungs_ueberwachung_3_master_Type = DisplayString
_Antennenleitungs_ueberwachung_3_master_Object = MibTableColumn
antennenleitungs_ueberwachung_3_master = _Antennenleitungs_ueberwachung_3_master_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1, 1, 26),
    _Antennenleitungs_ueberwachung_3_master_Type()
)
antennenleitungs_ueberwachung_3_master.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    antennenleitungs_ueberwachung_3_master.setStatus("current")
_Interne_temp_ueberwachung_master_Type = DisplayString
_Interne_temp_ueberwachung_master_Object = MibTableColumn
interne_temp_ueberwachung_master = _Interne_temp_ueberwachung_master_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1, 1, 27),
    _Interne_temp_ueberwachung_master_Type()
)
interne_temp_ueberwachung_master.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interne_temp_ueberwachung_master.setStatus("current")
_Ueberwachung_ov_1_master_Type = DisplayString
_Ueberwachung_ov_1_master_Object = MibTableColumn
ueberwachung_ov_1_master = _Ueberwachung_ov_1_master_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1, 1, 28),
    _Ueberwachung_ov_1_master_Type()
)
ueberwachung_ov_1_master.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ueberwachung_ov_1_master.setStatus("current")
_Ueberwachung_ov_2_master_Type = DisplayString
_Ueberwachung_ov_2_master_Object = MibTableColumn
ueberwachung_ov_2_master = _Ueberwachung_ov_2_master_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1, 1, 29),
    _Ueberwachung_ov_2_master_Type()
)
ueberwachung_ov_2_master.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ueberwachung_ov_2_master.setStatus("current")
_Zustand_gesamtsystem_master_Type = DisplayString
_Zustand_gesamtsystem_master_Object = MibTableColumn
zustand_gesamtsystem_master = _Zustand_gesamtsystem_master_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1, 1, 30),
    _Zustand_gesamtsystem_master_Type()
)
zustand_gesamtsystem_master.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zustand_gesamtsystem_master.setStatus("current")
_Zustand_netzversorgung_master_Type = DisplayString
_Zustand_netzversorgung_master_Object = MibTableColumn
zustand_netzversorgung_master = _Zustand_netzversorgung_master_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1, 1, 31),
    _Zustand_netzversorgung_master_Type()
)
zustand_netzversorgung_master.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zustand_netzversorgung_master.setStatus("current")
_Zustand_fernwirkmodule_master_Type = DisplayString
_Zustand_fernwirkmodule_master_Object = MibTableColumn
zustand_fernwirkmodule_master = _Zustand_fernwirkmodule_master_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1, 1, 32),
    _Zustand_fernwirkmodule_master_Type()
)
zustand_fernwirkmodule_master.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zustand_fernwirkmodule_master.setStatus("current")
_Zustand_ofu_modulbaugruppen_master_Type = DisplayString
_Zustand_ofu_modulbaugruppen_master_Object = MibTableColumn
zustand_ofu_modulbaugruppen_master = _Zustand_ofu_modulbaugruppen_master_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1, 1, 33),
    _Zustand_ofu_modulbaugruppen_master_Type()
)
zustand_ofu_modulbaugruppen_master.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zustand_ofu_modulbaugruppen_master.setStatus("current")
_Zustand_ofu_fgb_master_Type = DisplayString
_Zustand_ofu_fgb_master_Object = MibTableColumn
zustand_ofu_fgb_master = _Zustand_ofu_fgb_master_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1, 1, 34),
    _Zustand_ofu_fgb_master_Type()
)
zustand_ofu_fgb_master.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zustand_ofu_fgb_master.setStatus("current")
_Zustand_ofu_slaves_master_Type = DisplayString
_Zustand_ofu_slaves_master_Object = MibTableColumn
zustand_ofu_slaves_master = _Zustand_ofu_slaves_master_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 1, 1, 35),
    _Zustand_ofu_slaves_master_Type()
)
zustand_ofu_slaves_master.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zustand_ofu_slaves_master.setStatus("current")
_ModulTable_mod_m_1_Object = MibTable
modulTable_mod_m_1 = _ModulTable_mod_m_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    modulTable_mod_m_1.setStatus("current")
_ModulEntry_mod_m_1_Object = MibTableRow
modulEntry_mod_m_1 = _ModulEntry_mod_m_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 2, 1)
)
modulEntry_mod_m_1.setIndexNames(
    (0, "AK-FUNKTECHNIK-MIB", "modulindex-mod-m-1"),
)
if mibBuilder.loadTexts:
    modulEntry_mod_m_1.setStatus("current")
_Modulindex_mod_m_1_Type = DisplayString
_Modulindex_mod_m_1_Object = MibTableColumn
modulindex_mod_m_1 = _Modulindex_mod_m_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 2, 1, 1),
    _Modulindex_mod_m_1_Type()
)
modulindex_mod_m_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulindex_mod_m_1.setStatus("current")
_Modul_typ_mod_m_1_Type = DisplayString
_Modul_typ_mod_m_1_Object = MibTableColumn
modul_typ_mod_m_1 = _Modul_typ_mod_m_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 2, 1, 2),
    _Modul_typ_mod_m_1_Type()
)
modul_typ_mod_m_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_typ_mod_m_1.setStatus("current")
_Seriennummer_mod_m_1_Type = DisplayString
_Seriennummer_mod_m_1_Object = MibTableColumn
seriennummer_mod_m_1 = _Seriennummer_mod_m_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 2, 1, 3),
    _Seriennummer_mod_m_1_Type()
)
seriennummer_mod_m_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seriennummer_mod_m_1.setStatus("current")
_Firmware_version_mod_m_1_Type = DisplayString
_Firmware_version_mod_m_1_Object = MibTableColumn
firmware_version_mod_m_1 = _Firmware_version_mod_m_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 2, 1, 4),
    _Firmware_version_mod_m_1_Type()
)
firmware_version_mod_m_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmware_version_mod_m_1.setStatus("current")
_Hardware_zustand_mod_m_1_Type = DisplayString
_Hardware_zustand_mod_m_1_Object = MibTableColumn
hardware_zustand_mod_m_1 = _Hardware_zustand_mod_m_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 2, 1, 5),
    _Hardware_zustand_mod_m_1_Type()
)
hardware_zustand_mod_m_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardware_zustand_mod_m_1.setStatus("current")
_Betriebs_status_mod_m_1_Type = DisplayString
_Betriebs_status_mod_m_1_Object = MibTableColumn
betriebs_status_mod_m_1 = _Betriebs_status_mod_m_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 2, 1, 6),
    _Betriebs_status_mod_m_1_Type()
)
betriebs_status_mod_m_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    betriebs_status_mod_m_1.setStatus("current")
_Modul_var_para_1_mod_m_1_Type = DisplayString
_Modul_var_para_1_mod_m_1_Object = MibTableColumn
modul_var_para_1_mod_m_1 = _Modul_var_para_1_mod_m_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 2, 1, 7),
    _Modul_var_para_1_mod_m_1_Type()
)
modul_var_para_1_mod_m_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_1_mod_m_1.setStatus("current")
_Modul_var_para_2_mod_m_1_Type = DisplayString
_Modul_var_para_2_mod_m_1_Object = MibTableColumn
modul_var_para_2_mod_m_1 = _Modul_var_para_2_mod_m_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 2, 1, 8),
    _Modul_var_para_2_mod_m_1_Type()
)
modul_var_para_2_mod_m_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_2_mod_m_1.setStatus("current")
_Modul_var_para_3_mod_m_1_Type = DisplayString
_Modul_var_para_3_mod_m_1_Object = MibTableColumn
modul_var_para_3_mod_m_1 = _Modul_var_para_3_mod_m_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 2, 1, 9),
    _Modul_var_para_3_mod_m_1_Type()
)
modul_var_para_3_mod_m_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_3_mod_m_1.setStatus("current")
_Modul_var_para_4_mod_m_1_Type = DisplayString
_Modul_var_para_4_mod_m_1_Object = MibTableColumn
modul_var_para_4_mod_m_1 = _Modul_var_para_4_mod_m_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 2, 1, 10),
    _Modul_var_para_4_mod_m_1_Type()
)
modul_var_para_4_mod_m_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_4_mod_m_1.setStatus("current")
_Modul_var_para_5_mod_m_1_Type = DisplayString
_Modul_var_para_5_mod_m_1_Object = MibTableColumn
modul_var_para_5_mod_m_1 = _Modul_var_para_5_mod_m_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 2, 1, 11),
    _Modul_var_para_5_mod_m_1_Type()
)
modul_var_para_5_mod_m_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_5_mod_m_1.setStatus("current")
_Modul_var_para_6_mod_m_1_Type = DisplayString
_Modul_var_para_6_mod_m_1_Object = MibTableColumn
modul_var_para_6_mod_m_1 = _Modul_var_para_6_mod_m_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 2, 1, 12),
    _Modul_var_para_6_mod_m_1_Type()
)
modul_var_para_6_mod_m_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_6_mod_m_1.setStatus("current")
_Modul_var_para_7_mod_m_1_Type = DisplayString
_Modul_var_para_7_mod_m_1_Object = MibTableColumn
modul_var_para_7_mod_m_1 = _Modul_var_para_7_mod_m_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 2, 1, 13),
    _Modul_var_para_7_mod_m_1_Type()
)
modul_var_para_7_mod_m_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_7_mod_m_1.setStatus("current")
_Modul_var_para_8_mod_m_1_Type = DisplayString
_Modul_var_para_8_mod_m_1_Object = MibTableColumn
modul_var_para_8_mod_m_1 = _Modul_var_para_8_mod_m_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 2, 1, 14),
    _Modul_var_para_8_mod_m_1_Type()
)
modul_var_para_8_mod_m_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_8_mod_m_1.setStatus("current")
_Modul_var_para_9_mod_m_1_Type = DisplayString
_Modul_var_para_9_mod_m_1_Object = MibTableColumn
modul_var_para_9_mod_m_1 = _Modul_var_para_9_mod_m_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 2, 1, 15),
    _Modul_var_para_9_mod_m_1_Type()
)
modul_var_para_9_mod_m_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_9_mod_m_1.setStatus("current")
_Modul_var_para_10_mod_m_1_Type = DisplayString
_Modul_var_para_10_mod_m_1_Object = MibTableColumn
modul_var_para_10_mod_m_1 = _Modul_var_para_10_mod_m_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 2, 1, 16),
    _Modul_var_para_10_mod_m_1_Type()
)
modul_var_para_10_mod_m_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_10_mod_m_1.setStatus("current")
_Modul_var_para_11_mod_m_1_Type = DisplayString
_Modul_var_para_11_mod_m_1_Object = MibTableColumn
modul_var_para_11_mod_m_1 = _Modul_var_para_11_mod_m_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 2, 1, 17),
    _Modul_var_para_11_mod_m_1_Type()
)
modul_var_para_11_mod_m_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_11_mod_m_1.setStatus("current")
_Modul_var_para_12_mod_m_1_Type = DisplayString
_Modul_var_para_12_mod_m_1_Object = MibTableColumn
modul_var_para_12_mod_m_1 = _Modul_var_para_12_mod_m_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 2, 1, 18),
    _Modul_var_para_12_mod_m_1_Type()
)
modul_var_para_12_mod_m_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_12_mod_m_1.setStatus("current")
_Modul_var_para_13_mod_m_1_Type = DisplayString
_Modul_var_para_13_mod_m_1_Object = MibTableColumn
modul_var_para_13_mod_m_1 = _Modul_var_para_13_mod_m_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 2, 1, 19),
    _Modul_var_para_13_mod_m_1_Type()
)
modul_var_para_13_mod_m_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_13_mod_m_1.setStatus("current")
_Modul_var_para_14_mod_m_1_Type = DisplayString
_Modul_var_para_14_mod_m_1_Object = MibTableColumn
modul_var_para_14_mod_m_1 = _Modul_var_para_14_mod_m_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 2, 1, 20),
    _Modul_var_para_14_mod_m_1_Type()
)
modul_var_para_14_mod_m_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_14_mod_m_1.setStatus("current")
_Modul_var_para_15_mod_m_1_Type = DisplayString
_Modul_var_para_15_mod_m_1_Object = MibTableColumn
modul_var_para_15_mod_m_1 = _Modul_var_para_15_mod_m_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 2, 1, 21),
    _Modul_var_para_15_mod_m_1_Type()
)
modul_var_para_15_mod_m_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_15_mod_m_1.setStatus("current")
_Modul_var_para_16_mod_m_1_Type = DisplayString
_Modul_var_para_16_mod_m_1_Object = MibTableColumn
modul_var_para_16_mod_m_1 = _Modul_var_para_16_mod_m_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 2, 1, 23),
    _Modul_var_para_16_mod_m_1_Type()
)
modul_var_para_16_mod_m_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_16_mod_m_1.setStatus("current")
_Modul_var_para_17_mod_m_1_Type = DisplayString
_Modul_var_para_17_mod_m_1_Object = MibTableColumn
modul_var_para_17_mod_m_1 = _Modul_var_para_17_mod_m_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 2, 1, 24),
    _Modul_var_para_17_mod_m_1_Type()
)
modul_var_para_17_mod_m_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_17_mod_m_1.setStatus("current")
_Modul_var_para_18_mod_m_1_Type = DisplayString
_Modul_var_para_18_mod_m_1_Object = MibTableColumn
modul_var_para_18_mod_m_1 = _Modul_var_para_18_mod_m_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 2, 1, 25),
    _Modul_var_para_18_mod_m_1_Type()
)
modul_var_para_18_mod_m_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_18_mod_m_1.setStatus("current")
_Modul_var_para_19_mod_m_1_Type = DisplayString
_Modul_var_para_19_mod_m_1_Object = MibTableColumn
modul_var_para_19_mod_m_1 = _Modul_var_para_19_mod_m_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 1, 2, 1, 26),
    _Modul_var_para_19_mod_m_1_Type()
)
modul_var_para_19_mod_m_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_19_mod_m_1.setStatus("current")
_Info_externe_slave_module_ObjectIdentity = ObjectIdentity
info_externe_slave_module = _Info_externe_slave_module_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2)
)
_SlaveTable_basisinfo_Object = MibTable
slaveTable_basisinfo = _SlaveTable_basisinfo_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    slaveTable_basisinfo.setStatus("current")
_ModulEntry_basis_slave_1_Object = MibTableRow
modulEntry_basis_slave_1 = _ModulEntry_basis_slave_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1, 1)
)
modulEntry_basis_slave_1.setIndexNames(
    (0, "AK-FUNKTECHNIK-MIB", "modulindex-basis-slave-1"),
)
if mibBuilder.loadTexts:
    modulEntry_basis_slave_1.setStatus("current")
_Modulindex_basis_slave_1_Type = DisplayString
_Modulindex_basis_slave_1_Object = MibTableColumn
modulindex_basis_slave_1 = _Modulindex_basis_slave_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1, 1, 1),
    _Modulindex_basis_slave_1_Type()
)
modulindex_basis_slave_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulindex_basis_slave_1.setStatus("current")
_Ska_fehlerstat_basis_slave_1_Type = DisplayString
_Ska_fehlerstat_basis_slave_1_Object = MibTableColumn
ska_fehlerstat_basis_slave_1 = _Ska_fehlerstat_basis_slave_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1, 1, 2),
    _Ska_fehlerstat_basis_slave_1_Type()
)
ska_fehlerstat_basis_slave_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ska_fehlerstat_basis_slave_1.setStatus("current")
_Ska_betriebsstat_basis_slave_1_Type = DisplayString
_Ska_betriebsstat_basis_slave_1_Object = MibTableColumn
ska_betriebsstat_basis_slave_1 = _Ska_betriebsstat_basis_slave_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1, 1, 3),
    _Ska_betriebsstat_basis_slave_1_Type()
)
ska_betriebsstat_basis_slave_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ska_betriebsstat_basis_slave_1.setStatus("current")
_Ska_betriebsstat_quelle_basis_slave_1_Type = DisplayString
_Ska_betriebsstat_quelle_basis_slave_1_Object = MibTableColumn
ska_betriebsstat_quelle_basis_slave_1 = _Ska_betriebsstat_quelle_basis_slave_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1, 1, 4),
    _Ska_betriebsstat_quelle_basis_slave_1_Type()
)
ska_betriebsstat_quelle_basis_slave_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ska_betriebsstat_quelle_basis_slave_1.setStatus("current")
_Ska_autom_abschaltzeit_basis_slave_1_Type = DisplayString
_Ska_autom_abschaltzeit_basis_slave_1_Object = MibTableColumn
ska_autom_abschaltzeit_basis_slave_1 = _Ska_autom_abschaltzeit_basis_slave_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1, 1, 5),
    _Ska_autom_abschaltzeit_basis_slave_1_Type()
)
ska_autom_abschaltzeit_basis_slave_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ska_autom_abschaltzeit_basis_slave_1.setStatus("current")
_Skb_fehlerstat_basis_slave_1_Type = DisplayString
_Skb_fehlerstat_basis_slave_1_Object = MibTableColumn
skb_fehlerstat_basis_slave_1 = _Skb_fehlerstat_basis_slave_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1, 1, 6),
    _Skb_fehlerstat_basis_slave_1_Type()
)
skb_fehlerstat_basis_slave_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skb_fehlerstat_basis_slave_1.setStatus("current")
_Skb_betriebsstat_basis_slave_1_Type = DisplayString
_Skb_betriebsstat_basis_slave_1_Object = MibTableColumn
skb_betriebsstat_basis_slave_1 = _Skb_betriebsstat_basis_slave_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1, 1, 7),
    _Skb_betriebsstat_basis_slave_1_Type()
)
skb_betriebsstat_basis_slave_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skb_betriebsstat_basis_slave_1.setStatus("current")
_Skb_betriebsstat_quelle_basis_slave_1_Type = DisplayString
_Skb_betriebsstat_quelle_basis_slave_1_Object = MibTableColumn
skb_betriebsstat_quelle_basis_slave_1 = _Skb_betriebsstat_quelle_basis_slave_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1, 1, 8),
    _Skb_betriebsstat_quelle_basis_slave_1_Type()
)
skb_betriebsstat_quelle_basis_slave_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skb_betriebsstat_quelle_basis_slave_1.setStatus("current")
_Skb_autom_abschaltzeit_basis_slave_1_Type = DisplayString
_Skb_autom_abschaltzeit_basis_slave_1_Object = MibTableColumn
skb_autom_abschaltzeit_basis_slave_1 = _Skb_autom_abschaltzeit_basis_slave_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1, 1, 9),
    _Skb_autom_abschaltzeit_basis_slave_1_Type()
)
skb_autom_abschaltzeit_basis_slave_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skb_autom_abschaltzeit_basis_slave_1.setStatus("current")
_Skc_fehlerstat_basis_slave_1_Type = DisplayString
_Skc_fehlerstat_basis_slave_1_Object = MibTableColumn
skc_fehlerstat_basis_slave_1 = _Skc_fehlerstat_basis_slave_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1, 1, 10),
    _Skc_fehlerstat_basis_slave_1_Type()
)
skc_fehlerstat_basis_slave_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skc_fehlerstat_basis_slave_1.setStatus("current")
_Skc_betriebsstat_basis_slave_1_Type = DisplayString
_Skc_betriebsstat_basis_slave_1_Object = MibTableColumn
skc_betriebsstat_basis_slave_1 = _Skc_betriebsstat_basis_slave_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1, 1, 11),
    _Skc_betriebsstat_basis_slave_1_Type()
)
skc_betriebsstat_basis_slave_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skc_betriebsstat_basis_slave_1.setStatus("current")
_Skc_betriebsstat_quelle_basis_slave_1_Type = DisplayString
_Skc_betriebsstat_quelle_basis_slave_1_Object = MibTableColumn
skc_betriebsstat_quelle_basis_slave_1 = _Skc_betriebsstat_quelle_basis_slave_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1, 1, 12),
    _Skc_betriebsstat_quelle_basis_slave_1_Type()
)
skc_betriebsstat_quelle_basis_slave_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skc_betriebsstat_quelle_basis_slave_1.setStatus("current")
_Skc_autom_abschaltzeit_basis_slave_1_Type = DisplayString
_Skc_autom_abschaltzeit_basis_slave_1_Object = MibTableColumn
skc_autom_abschaltzeit_basis_slave_1 = _Skc_autom_abschaltzeit_basis_slave_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1, 1, 13),
    _Skc_autom_abschaltzeit_basis_slave_1_Type()
)
skc_autom_abschaltzeit_basis_slave_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skc_autom_abschaltzeit_basis_slave_1.setStatus("current")
_Fehlerausgang_rel_1_basis_slave_1_Type = DisplayString
_Fehlerausgang_rel_1_basis_slave_1_Object = MibTableColumn
fehlerausgang_rel_1_basis_slave_1 = _Fehlerausgang_rel_1_basis_slave_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1, 1, 14),
    _Fehlerausgang_rel_1_basis_slave_1_Type()
)
fehlerausgang_rel_1_basis_slave_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fehlerausgang_rel_1_basis_slave_1.setStatus("current")
_Fehlerausgang_rel_2_basis_slave_1_Type = DisplayString
_Fehlerausgang_rel_2_basis_slave_1_Object = MibTableColumn
fehlerausgang_rel_2_basis_slave_1 = _Fehlerausgang_rel_2_basis_slave_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1, 1, 15),
    _Fehlerausgang_rel_2_basis_slave_1_Type()
)
fehlerausgang_rel_2_basis_slave_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fehlerausgang_rel_2_basis_slave_1.setStatus("current")
_Steuerausgang_x1000_basis_slave_1_Type = DisplayString
_Steuerausgang_x1000_basis_slave_1_Object = MibTableColumn
steuerausgang_x1000_basis_slave_1 = _Steuerausgang_x1000_basis_slave_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1, 1, 16),
    _Steuerausgang_x1000_basis_slave_1_Type()
)
steuerausgang_x1000_basis_slave_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steuerausgang_x1000_basis_slave_1.setStatus("current")
_Steuerausgang_x1002_basis_slave_1_Type = DisplayString
_Steuerausgang_x1002_basis_slave_1_Object = MibTableColumn
steuerausgang_x1002_basis_slave_1 = _Steuerausgang_x1002_basis_slave_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1, 1, 17),
    _Steuerausgang_x1002_basis_slave_1_Type()
)
steuerausgang_x1002_basis_slave_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steuerausgang_x1002_basis_slave_1.setStatus("current")
_Steuerausgang_x2001_8_basis_slave_1_Type = DisplayString
_Steuerausgang_x2001_8_basis_slave_1_Object = MibTableColumn
steuerausgang_x2001_8_basis_slave_1 = _Steuerausgang_x2001_8_basis_slave_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1, 1, 18),
    _Steuerausgang_x2001_8_basis_slave_1_Type()
)
steuerausgang_x2001_8_basis_slave_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steuerausgang_x2001_8_basis_slave_1.setStatus("current")
_Steuerausgang_x2001_10_basis_slave_1_Type = DisplayString
_Steuerausgang_x2001_10_basis_slave_1_Object = MibTableColumn
steuerausgang_x2001_10_basis_slave_1 = _Steuerausgang_x2001_10_basis_slave_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1, 1, 19),
    _Steuerausgang_x2001_10_basis_slave_1_Type()
)
steuerausgang_x2001_10_basis_slave_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steuerausgang_x2001_10_basis_slave_1.setStatus("current")
_Serviceschalter_basis_slave_1_Type = DisplayString
_Serviceschalter_basis_slave_1_Object = MibTableColumn
serviceschalter_basis_slave_1 = _Serviceschalter_basis_slave_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1, 1, 20),
    _Serviceschalter_basis_slave_1_Type()
)
serviceschalter_basis_slave_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceschalter_basis_slave_1.setStatus("current")
_Steuereingang_bma_basis_slave_1_Type = DisplayString
_Steuereingang_bma_basis_slave_1_Object = MibTableColumn
steuereingang_bma_basis_slave_1 = _Steuereingang_bma_basis_slave_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1, 1, 21),
    _Steuereingang_bma_basis_slave_1_Type()
)
steuereingang_bma_basis_slave_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steuereingang_bma_basis_slave_1.setStatus("current")
_Steuereingang_opt1_basis_slave_1_Type = DisplayString
_Steuereingang_opt1_basis_slave_1_Object = MibTableColumn
steuereingang_opt1_basis_slave_1 = _Steuereingang_opt1_basis_slave_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1, 1, 22),
    _Steuereingang_opt1_basis_slave_1_Type()
)
steuereingang_opt1_basis_slave_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steuereingang_opt1_basis_slave_1.setStatus("current")
_Steuereingang_opt2_basis_slave_1_Type = DisplayString
_Steuereingang_opt2_basis_slave_1_Object = MibTableColumn
steuereingang_opt2_basis_slave_1 = _Steuereingang_opt2_basis_slave_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1, 1, 23),
    _Steuereingang_opt2_basis_slave_1_Type()
)
steuereingang_opt2_basis_slave_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    steuereingang_opt2_basis_slave_1.setStatus("current")
_Antennenleitungs_ueberwachung_1_basis_slave_1_Type = DisplayString
_Antennenleitungs_ueberwachung_1_basis_slave_1_Object = MibTableColumn
antennenleitungs_ueberwachung_1_basis_slave_1 = _Antennenleitungs_ueberwachung_1_basis_slave_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1, 1, 24),
    _Antennenleitungs_ueberwachung_1_basis_slave_1_Type()
)
antennenleitungs_ueberwachung_1_basis_slave_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    antennenleitungs_ueberwachung_1_basis_slave_1.setStatus("current")
_Antennenleitungs_ueberwachung_2_basis_slave_1_Type = DisplayString
_Antennenleitungs_ueberwachung_2_basis_slave_1_Object = MibTableColumn
antennenleitungs_ueberwachung_2_basis_slave_1 = _Antennenleitungs_ueberwachung_2_basis_slave_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1, 1, 25),
    _Antennenleitungs_ueberwachung_2_basis_slave_1_Type()
)
antennenleitungs_ueberwachung_2_basis_slave_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    antennenleitungs_ueberwachung_2_basis_slave_1.setStatus("current")
_Antennenleitungs_ueberwachung_3_basis_slave_1_Type = DisplayString
_Antennenleitungs_ueberwachung_3_basis_slave_1_Object = MibTableColumn
antennenleitungs_ueberwachung_3_basis_slave_1 = _Antennenleitungs_ueberwachung_3_basis_slave_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1, 1, 26),
    _Antennenleitungs_ueberwachung_3_basis_slave_1_Type()
)
antennenleitungs_ueberwachung_3_basis_slave_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    antennenleitungs_ueberwachung_3_basis_slave_1.setStatus("current")
_Interne_temp_ueberwachung_basis_slave_1_Type = DisplayString
_Interne_temp_ueberwachung_basis_slave_1_Object = MibTableColumn
interne_temp_ueberwachung_basis_slave_1 = _Interne_temp_ueberwachung_basis_slave_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1, 1, 27),
    _Interne_temp_ueberwachung_basis_slave_1_Type()
)
interne_temp_ueberwachung_basis_slave_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interne_temp_ueberwachung_basis_slave_1.setStatus("current")
_Ueberwachung_ov_1_basis_slave_1_Type = DisplayString
_Ueberwachung_ov_1_basis_slave_1_Object = MibTableColumn
ueberwachung_ov_1_basis_slave_1 = _Ueberwachung_ov_1_basis_slave_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1, 1, 28),
    _Ueberwachung_ov_1_basis_slave_1_Type()
)
ueberwachung_ov_1_basis_slave_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ueberwachung_ov_1_basis_slave_1.setStatus("current")
_Ueberwachung_ov_2_basis_slave_1_Type = DisplayString
_Ueberwachung_ov_2_basis_slave_1_Object = MibTableColumn
ueberwachung_ov_2_basis_slave_1 = _Ueberwachung_ov_2_basis_slave_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1, 1, 29),
    _Ueberwachung_ov_2_basis_slave_1_Type()
)
ueberwachung_ov_2_basis_slave_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ueberwachung_ov_2_basis_slave_1.setStatus("current")
_Zustand_gesamtsystem_basis_slave_1_Type = DisplayString
_Zustand_gesamtsystem_basis_slave_1_Object = MibTableColumn
zustand_gesamtsystem_basis_slave_1 = _Zustand_gesamtsystem_basis_slave_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1, 1, 30),
    _Zustand_gesamtsystem_basis_slave_1_Type()
)
zustand_gesamtsystem_basis_slave_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zustand_gesamtsystem_basis_slave_1.setStatus("current")
_Zustand_netzversorgung_basis_slave_1_Type = DisplayString
_Zustand_netzversorgung_basis_slave_1_Object = MibTableColumn
zustand_netzversorgung_basis_slave_1 = _Zustand_netzversorgung_basis_slave_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1, 1, 31),
    _Zustand_netzversorgung_basis_slave_1_Type()
)
zustand_netzversorgung_basis_slave_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zustand_netzversorgung_basis_slave_1.setStatus("current")
_Zustand_fernwirkmodule_basis_slave_1_Type = DisplayString
_Zustand_fernwirkmodule_basis_slave_1_Object = MibTableColumn
zustand_fernwirkmodule_basis_slave_1 = _Zustand_fernwirkmodule_basis_slave_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1, 1, 32),
    _Zustand_fernwirkmodule_basis_slave_1_Type()
)
zustand_fernwirkmodule_basis_slave_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zustand_fernwirkmodule_basis_slave_1.setStatus("current")
_Zustand_ofu_modulbaugruppen_basis_slave_1_Type = DisplayString
_Zustand_ofu_modulbaugruppen_basis_slave_1_Object = MibTableColumn
zustand_ofu_modulbaugruppen_basis_slave_1 = _Zustand_ofu_modulbaugruppen_basis_slave_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1, 1, 33),
    _Zustand_ofu_modulbaugruppen_basis_slave_1_Type()
)
zustand_ofu_modulbaugruppen_basis_slave_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zustand_ofu_modulbaugruppen_basis_slave_1.setStatus("current")
_Zustand_ofu_fgb_basis_slave_1_Type = DisplayString
_Zustand_ofu_fgb_basis_slave_1_Object = MibTableColumn
zustand_ofu_fgb_basis_slave_1 = _Zustand_ofu_fgb_basis_slave_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1, 1, 34),
    _Zustand_ofu_fgb_basis_slave_1_Type()
)
zustand_ofu_fgb_basis_slave_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zustand_ofu_fgb_basis_slave_1.setStatus("current")
_Zustand_ofu_slaves_basis_slave_1_Type = DisplayString
_Zustand_ofu_slaves_basis_slave_1_Object = MibTableColumn
zustand_ofu_slaves_basis_slave_1 = _Zustand_ofu_slaves_basis_slave_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 1, 1, 35),
    _Zustand_ofu_slaves_basis_slave_1_Type()
)
zustand_ofu_slaves_basis_slave_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zustand_ofu_slaves_basis_slave_1.setStatus("current")
_ModulTable_mod_s_1_Object = MibTable
modulTable_mod_s_1 = _ModulTable_mod_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    modulTable_mod_s_1.setStatus("current")
_ModulEntry_mod_s_1_Object = MibTableRow
modulEntry_mod_s_1 = _ModulEntry_mod_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 2, 1)
)
modulEntry_mod_s_1.setIndexNames(
    (0, "AK-FUNKTECHNIK-MIB", "modulindex-mod-s-1"),
)
if mibBuilder.loadTexts:
    modulEntry_mod_s_1.setStatus("current")
_Modulindex_mod_s_1_Type = DisplayString
_Modulindex_mod_s_1_Object = MibTableColumn
modulindex_mod_s_1 = _Modulindex_mod_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 2, 1, 1),
    _Modulindex_mod_s_1_Type()
)
modulindex_mod_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulindex_mod_s_1.setStatus("current")
_Modul_typ_mod_s_1_Type = DisplayString
_Modul_typ_mod_s_1_Object = MibTableColumn
modul_typ_mod_s_1 = _Modul_typ_mod_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 2, 1, 2),
    _Modul_typ_mod_s_1_Type()
)
modul_typ_mod_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_typ_mod_s_1.setStatus("current")
_Seriennummer_mod_s_1_Type = DisplayString
_Seriennummer_mod_s_1_Object = MibTableColumn
seriennummer_mod_s_1 = _Seriennummer_mod_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 2, 1, 3),
    _Seriennummer_mod_s_1_Type()
)
seriennummer_mod_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seriennummer_mod_s_1.setStatus("current")
_Firmware_version_mod_s_1_Type = DisplayString
_Firmware_version_mod_s_1_Object = MibTableColumn
firmware_version_mod_s_1 = _Firmware_version_mod_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 2, 1, 4),
    _Firmware_version_mod_s_1_Type()
)
firmware_version_mod_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmware_version_mod_s_1.setStatus("current")
_Hardware_zustand_mod_s_1_Type = DisplayString
_Hardware_zustand_mod_s_1_Object = MibTableColumn
hardware_zustand_mod_s_1 = _Hardware_zustand_mod_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 2, 1, 5),
    _Hardware_zustand_mod_s_1_Type()
)
hardware_zustand_mod_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardware_zustand_mod_s_1.setStatus("current")
_Betriebs_status_mod_s_1_Type = DisplayString
_Betriebs_status_mod_s_1_Object = MibTableColumn
betriebs_status_mod_s_1 = _Betriebs_status_mod_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 2, 1, 6),
    _Betriebs_status_mod_s_1_Type()
)
betriebs_status_mod_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    betriebs_status_mod_s_1.setStatus("current")
_Modul_var_para_1_mod_s_1_Type = DisplayString
_Modul_var_para_1_mod_s_1_Object = MibTableColumn
modul_var_para_1_mod_s_1 = _Modul_var_para_1_mod_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 2, 1, 7),
    _Modul_var_para_1_mod_s_1_Type()
)
modul_var_para_1_mod_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_1_mod_s_1.setStatus("current")
_Modul_var_para_2_mod_s_1_Type = DisplayString
_Modul_var_para_2_mod_s_1_Object = MibTableColumn
modul_var_para_2_mod_s_1 = _Modul_var_para_2_mod_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 2, 1, 8),
    _Modul_var_para_2_mod_s_1_Type()
)
modul_var_para_2_mod_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_2_mod_s_1.setStatus("current")
_Modul_var_para_3_mod_s_1_Type = DisplayString
_Modul_var_para_3_mod_s_1_Object = MibTableColumn
modul_var_para_3_mod_s_1 = _Modul_var_para_3_mod_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 2, 1, 9),
    _Modul_var_para_3_mod_s_1_Type()
)
modul_var_para_3_mod_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_3_mod_s_1.setStatus("current")
_Modul_var_para_4_mod_s_1_Type = DisplayString
_Modul_var_para_4_mod_s_1_Object = MibTableColumn
modul_var_para_4_mod_s_1 = _Modul_var_para_4_mod_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 2, 1, 10),
    _Modul_var_para_4_mod_s_1_Type()
)
modul_var_para_4_mod_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_4_mod_s_1.setStatus("current")
_Modul_var_para_5_mod_s_1_Type = DisplayString
_Modul_var_para_5_mod_s_1_Object = MibTableColumn
modul_var_para_5_mod_s_1 = _Modul_var_para_5_mod_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 2, 1, 11),
    _Modul_var_para_5_mod_s_1_Type()
)
modul_var_para_5_mod_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_5_mod_s_1.setStatus("current")
_Modul_var_para_6_mod_s_1_Type = DisplayString
_Modul_var_para_6_mod_s_1_Object = MibTableColumn
modul_var_para_6_mod_s_1 = _Modul_var_para_6_mod_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 2, 1, 12),
    _Modul_var_para_6_mod_s_1_Type()
)
modul_var_para_6_mod_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_6_mod_s_1.setStatus("current")
_Modul_var_para_7_mod_s_1_Type = DisplayString
_Modul_var_para_7_mod_s_1_Object = MibTableColumn
modul_var_para_7_mod_s_1 = _Modul_var_para_7_mod_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 2, 1, 13),
    _Modul_var_para_7_mod_s_1_Type()
)
modul_var_para_7_mod_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_7_mod_s_1.setStatus("current")
_Modul_var_para_8_mod_s_1_Type = DisplayString
_Modul_var_para_8_mod_s_1_Object = MibTableColumn
modul_var_para_8_mod_s_1 = _Modul_var_para_8_mod_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 2, 1, 14),
    _Modul_var_para_8_mod_s_1_Type()
)
modul_var_para_8_mod_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_8_mod_s_1.setStatus("current")
_Modul_var_para_9_mod_s_1_Type = DisplayString
_Modul_var_para_9_mod_s_1_Object = MibTableColumn
modul_var_para_9_mod_s_1 = _Modul_var_para_9_mod_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 2, 1, 15),
    _Modul_var_para_9_mod_s_1_Type()
)
modul_var_para_9_mod_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_9_mod_s_1.setStatus("current")
_Modul_var_para_10_mod_s_1_Type = DisplayString
_Modul_var_para_10_mod_s_1_Object = MibTableColumn
modul_var_para_10_mod_s_1 = _Modul_var_para_10_mod_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 2, 1, 16),
    _Modul_var_para_10_mod_s_1_Type()
)
modul_var_para_10_mod_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_10_mod_s_1.setStatus("current")
_Modul_var_para_11_mod_s_1_Type = DisplayString
_Modul_var_para_11_mod_s_1_Object = MibTableColumn
modul_var_para_11_mod_s_1 = _Modul_var_para_11_mod_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 2, 1, 17),
    _Modul_var_para_11_mod_s_1_Type()
)
modul_var_para_11_mod_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_11_mod_s_1.setStatus("current")
_Modul_var_para_12_mod_s_1_Type = DisplayString
_Modul_var_para_12_mod_s_1_Object = MibTableColumn
modul_var_para_12_mod_s_1 = _Modul_var_para_12_mod_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 2, 1, 18),
    _Modul_var_para_12_mod_s_1_Type()
)
modul_var_para_12_mod_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_12_mod_s_1.setStatus("current")
_Modul_var_para_13_mod_s_1_Type = DisplayString
_Modul_var_para_13_mod_s_1_Object = MibTableColumn
modul_var_para_13_mod_s_1 = _Modul_var_para_13_mod_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 2, 1, 19),
    _Modul_var_para_13_mod_s_1_Type()
)
modul_var_para_13_mod_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_13_mod_s_1.setStatus("current")
_Modul_var_para_14_mod_s_1_Type = DisplayString
_Modul_var_para_14_mod_s_1_Object = MibTableColumn
modul_var_para_14_mod_s_1 = _Modul_var_para_14_mod_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 2, 1, 20),
    _Modul_var_para_14_mod_s_1_Type()
)
modul_var_para_14_mod_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_14_mod_s_1.setStatus("current")
_Modul_var_para_15_mod_s_1_Type = DisplayString
_Modul_var_para_15_mod_s_1_Object = MibTableColumn
modul_var_para_15_mod_s_1 = _Modul_var_para_15_mod_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 2, 1, 21),
    _Modul_var_para_15_mod_s_1_Type()
)
modul_var_para_15_mod_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_15_mod_s_1.setStatus("current")
_Modul_var_para_16_mod_s_1_Type = DisplayString
_Modul_var_para_16_mod_s_1_Object = MibTableColumn
modul_var_para_16_mod_s_1 = _Modul_var_para_16_mod_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 2, 1, 22),
    _Modul_var_para_16_mod_s_1_Type()
)
modul_var_para_16_mod_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_16_mod_s_1.setStatus("current")
_Modul_var_para_17_mod_s_1_Type = DisplayString
_Modul_var_para_17_mod_s_1_Object = MibTableColumn
modul_var_para_17_mod_s_1 = _Modul_var_para_17_mod_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 2, 1, 23),
    _Modul_var_para_17_mod_s_1_Type()
)
modul_var_para_17_mod_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_17_mod_s_1.setStatus("current")
_Modul_var_para_18_mod_s_1_Type = DisplayString
_Modul_var_para_18_mod_s_1_Object = MibTableColumn
modul_var_para_18_mod_s_1 = _Modul_var_para_18_mod_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 2, 1, 24),
    _Modul_var_para_18_mod_s_1_Type()
)
modul_var_para_18_mod_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_18_mod_s_1.setStatus("current")
_Modul_var_para_19_mod_s_1_Type = DisplayString
_Modul_var_para_19_mod_s_1_Object = MibTableColumn
modul_var_para_19_mod_s_1 = _Modul_var_para_19_mod_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 2, 1, 25),
    _Modul_var_para_19_mod_s_1_Type()
)
modul_var_para_19_mod_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_19_mod_s_1.setStatus("current")
_ModulTable_mod_s_2_Object = MibTable
modulTable_mod_s_2 = _ModulTable_mod_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 3)
)
if mibBuilder.loadTexts:
    modulTable_mod_s_2.setStatus("current")
_ModulEntry_mod_s_2_Object = MibTableRow
modulEntry_mod_s_2 = _ModulEntry_mod_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 3, 1)
)
modulEntry_mod_s_2.setIndexNames(
    (0, "AK-FUNKTECHNIK-MIB", "modulindex-mod-s-2"),
)
if mibBuilder.loadTexts:
    modulEntry_mod_s_2.setStatus("current")
_Modulindex_mod_s_2_Type = DisplayString
_Modulindex_mod_s_2_Object = MibTableColumn
modulindex_mod_s_2 = _Modulindex_mod_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 3, 1, 1),
    _Modulindex_mod_s_2_Type()
)
modulindex_mod_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulindex_mod_s_2.setStatus("current")
_Modul_typ_mod_s_2_Type = DisplayString
_Modul_typ_mod_s_2_Object = MibTableColumn
modul_typ_mod_s_2 = _Modul_typ_mod_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 3, 1, 2),
    _Modul_typ_mod_s_2_Type()
)
modul_typ_mod_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_typ_mod_s_2.setStatus("current")
_Seriennummer_mod_s_2_Type = DisplayString
_Seriennummer_mod_s_2_Object = MibTableColumn
seriennummer_mod_s_2 = _Seriennummer_mod_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 3, 1, 3),
    _Seriennummer_mod_s_2_Type()
)
seriennummer_mod_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seriennummer_mod_s_2.setStatus("current")
_Firmware_version_mod_s_2_Type = DisplayString
_Firmware_version_mod_s_2_Object = MibTableColumn
firmware_version_mod_s_2 = _Firmware_version_mod_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 3, 1, 4),
    _Firmware_version_mod_s_2_Type()
)
firmware_version_mod_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmware_version_mod_s_2.setStatus("current")
_Hardware_zustand_mod_s_2_Type = DisplayString
_Hardware_zustand_mod_s_2_Object = MibTableColumn
hardware_zustand_mod_s_2 = _Hardware_zustand_mod_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 3, 1, 5),
    _Hardware_zustand_mod_s_2_Type()
)
hardware_zustand_mod_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardware_zustand_mod_s_2.setStatus("current")
_Betriebs_status_mod_s_2_Type = DisplayString
_Betriebs_status_mod_s_2_Object = MibTableColumn
betriebs_status_mod_s_2 = _Betriebs_status_mod_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 3, 1, 6),
    _Betriebs_status_mod_s_2_Type()
)
betriebs_status_mod_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    betriebs_status_mod_s_2.setStatus("current")
_Modul_var_para_1_mod_s_2_Type = DisplayString
_Modul_var_para_1_mod_s_2_Object = MibTableColumn
modul_var_para_1_mod_s_2 = _Modul_var_para_1_mod_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 3, 1, 7),
    _Modul_var_para_1_mod_s_2_Type()
)
modul_var_para_1_mod_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_1_mod_s_2.setStatus("current")
_Modul_var_para_2_mod_s_2_Type = DisplayString
_Modul_var_para_2_mod_s_2_Object = MibTableColumn
modul_var_para_2_mod_s_2 = _Modul_var_para_2_mod_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 3, 1, 8),
    _Modul_var_para_2_mod_s_2_Type()
)
modul_var_para_2_mod_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_2_mod_s_2.setStatus("current")
_Modul_var_para_3_mod_s_2_Type = DisplayString
_Modul_var_para_3_mod_s_2_Object = MibTableColumn
modul_var_para_3_mod_s_2 = _Modul_var_para_3_mod_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 3, 1, 9),
    _Modul_var_para_3_mod_s_2_Type()
)
modul_var_para_3_mod_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_3_mod_s_2.setStatus("current")
_Modul_var_para_4_mod_s_2_Type = DisplayString
_Modul_var_para_4_mod_s_2_Object = MibTableColumn
modul_var_para_4_mod_s_2 = _Modul_var_para_4_mod_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 3, 1, 10),
    _Modul_var_para_4_mod_s_2_Type()
)
modul_var_para_4_mod_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_4_mod_s_2.setStatus("current")
_Modul_var_para_5_mod_s_2_Type = DisplayString
_Modul_var_para_5_mod_s_2_Object = MibTableColumn
modul_var_para_5_mod_s_2 = _Modul_var_para_5_mod_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 3, 1, 11),
    _Modul_var_para_5_mod_s_2_Type()
)
modul_var_para_5_mod_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_5_mod_s_2.setStatus("current")
_Modul_var_para_6_mod_s_2_Type = DisplayString
_Modul_var_para_6_mod_s_2_Object = MibTableColumn
modul_var_para_6_mod_s_2 = _Modul_var_para_6_mod_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 3, 1, 12),
    _Modul_var_para_6_mod_s_2_Type()
)
modul_var_para_6_mod_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_6_mod_s_2.setStatus("current")
_Modul_var_para_7_mod_s_2_Type = DisplayString
_Modul_var_para_7_mod_s_2_Object = MibTableColumn
modul_var_para_7_mod_s_2 = _Modul_var_para_7_mod_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 3, 1, 13),
    _Modul_var_para_7_mod_s_2_Type()
)
modul_var_para_7_mod_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_7_mod_s_2.setStatus("current")
_Modul_var_para_8_mod_s_2_Type = DisplayString
_Modul_var_para_8_mod_s_2_Object = MibTableColumn
modul_var_para_8_mod_s_2 = _Modul_var_para_8_mod_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 3, 1, 14),
    _Modul_var_para_8_mod_s_2_Type()
)
modul_var_para_8_mod_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_8_mod_s_2.setStatus("current")
_Modul_var_para_9_mod_s_2_Type = DisplayString
_Modul_var_para_9_mod_s_2_Object = MibTableColumn
modul_var_para_9_mod_s_2 = _Modul_var_para_9_mod_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 3, 1, 15),
    _Modul_var_para_9_mod_s_2_Type()
)
modul_var_para_9_mod_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_9_mod_s_2.setStatus("current")
_Modul_var_para_10_mod_s_2_Type = DisplayString
_Modul_var_para_10_mod_s_2_Object = MibTableColumn
modul_var_para_10_mod_s_2 = _Modul_var_para_10_mod_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 3, 1, 16),
    _Modul_var_para_10_mod_s_2_Type()
)
modul_var_para_10_mod_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_10_mod_s_2.setStatus("current")
_Modul_var_para_11_mod_s_2_Type = DisplayString
_Modul_var_para_11_mod_s_2_Object = MibTableColumn
modul_var_para_11_mod_s_2 = _Modul_var_para_11_mod_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 3, 1, 17),
    _Modul_var_para_11_mod_s_2_Type()
)
modul_var_para_11_mod_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_11_mod_s_2.setStatus("current")
_Modul_var_para_12_mod_s_2_Type = DisplayString
_Modul_var_para_12_mod_s_2_Object = MibTableColumn
modul_var_para_12_mod_s_2 = _Modul_var_para_12_mod_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 3, 1, 18),
    _Modul_var_para_12_mod_s_2_Type()
)
modul_var_para_12_mod_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_12_mod_s_2.setStatus("current")
_Modul_var_para_13_mod_s_2_Type = DisplayString
_Modul_var_para_13_mod_s_2_Object = MibTableColumn
modul_var_para_13_mod_s_2 = _Modul_var_para_13_mod_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 3, 1, 19),
    _Modul_var_para_13_mod_s_2_Type()
)
modul_var_para_13_mod_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_13_mod_s_2.setStatus("current")
_Modul_var_para_14_mod_s_2_Type = DisplayString
_Modul_var_para_14_mod_s_2_Object = MibTableColumn
modul_var_para_14_mod_s_2 = _Modul_var_para_14_mod_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 3, 1, 20),
    _Modul_var_para_14_mod_s_2_Type()
)
modul_var_para_14_mod_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_14_mod_s_2.setStatus("current")
_Modul_var_para_15_mod_s_2_Type = DisplayString
_Modul_var_para_15_mod_s_2_Object = MibTableColumn
modul_var_para_15_mod_s_2 = _Modul_var_para_15_mod_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 3, 1, 21),
    _Modul_var_para_15_mod_s_2_Type()
)
modul_var_para_15_mod_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_15_mod_s_2.setStatus("current")
_Modul_var_para_16_mod_s_2_Type = DisplayString
_Modul_var_para_16_mod_s_2_Object = MibTableColumn
modul_var_para_16_mod_s_2 = _Modul_var_para_16_mod_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 3, 1, 22),
    _Modul_var_para_16_mod_s_2_Type()
)
modul_var_para_16_mod_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_16_mod_s_2.setStatus("current")
_Modul_var_para_17_mod_s_2_Type = DisplayString
_Modul_var_para_17_mod_s_2_Object = MibTableColumn
modul_var_para_17_mod_s_2 = _Modul_var_para_17_mod_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 3, 1, 23),
    _Modul_var_para_17_mod_s_2_Type()
)
modul_var_para_17_mod_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_17_mod_s_2.setStatus("current")
_Modul_var_para_18_mod_s_2_Type = DisplayString
_Modul_var_para_18_mod_s_2_Object = MibTableColumn
modul_var_para_18_mod_s_2 = _Modul_var_para_18_mod_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 3, 1, 24),
    _Modul_var_para_18_mod_s_2_Type()
)
modul_var_para_18_mod_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_18_mod_s_2.setStatus("current")
_Modul_var_para_19_mod_s_2_Type = DisplayString
_Modul_var_para_19_mod_s_2_Object = MibTableColumn
modul_var_para_19_mod_s_2 = _Modul_var_para_19_mod_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 3, 1, 25),
    _Modul_var_para_19_mod_s_2_Type()
)
modul_var_para_19_mod_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_19_mod_s_2.setStatus("current")
_ModulTable_mod_s_3_Object = MibTable
modulTable_mod_s_3 = _ModulTable_mod_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 4)
)
if mibBuilder.loadTexts:
    modulTable_mod_s_3.setStatus("current")
_ModulEntry_mod_s_3_Object = MibTableRow
modulEntry_mod_s_3 = _ModulEntry_mod_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 4, 1)
)
modulEntry_mod_s_3.setIndexNames(
    (0, "AK-FUNKTECHNIK-MIB", "modulindex-mod-s-3"),
)
if mibBuilder.loadTexts:
    modulEntry_mod_s_3.setStatus("current")
_Modulindex_mod_s_3_Type = DisplayString
_Modulindex_mod_s_3_Object = MibTableColumn
modulindex_mod_s_3 = _Modulindex_mod_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 4, 1, 1),
    _Modulindex_mod_s_3_Type()
)
modulindex_mod_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulindex_mod_s_3.setStatus("current")
_Modul_typ_mod_s_3_Type = DisplayString
_Modul_typ_mod_s_3_Object = MibTableColumn
modul_typ_mod_s_3 = _Modul_typ_mod_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 4, 1, 2),
    _Modul_typ_mod_s_3_Type()
)
modul_typ_mod_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_typ_mod_s_3.setStatus("current")
_Seriennummer_mod_s_3_Type = DisplayString
_Seriennummer_mod_s_3_Object = MibTableColumn
seriennummer_mod_s_3 = _Seriennummer_mod_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 4, 1, 3),
    _Seriennummer_mod_s_3_Type()
)
seriennummer_mod_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seriennummer_mod_s_3.setStatus("current")
_Firmware_version_mod_s_3_Type = DisplayString
_Firmware_version_mod_s_3_Object = MibTableColumn
firmware_version_mod_s_3 = _Firmware_version_mod_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 4, 1, 4),
    _Firmware_version_mod_s_3_Type()
)
firmware_version_mod_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmware_version_mod_s_3.setStatus("current")
_Hardware_zustand_mod_s_3_Type = DisplayString
_Hardware_zustand_mod_s_3_Object = MibTableColumn
hardware_zustand_mod_s_3 = _Hardware_zustand_mod_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 4, 1, 5),
    _Hardware_zustand_mod_s_3_Type()
)
hardware_zustand_mod_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardware_zustand_mod_s_3.setStatus("current")
_Betriebs_status_mod_s_3_Type = DisplayString
_Betriebs_status_mod_s_3_Object = MibTableColumn
betriebs_status_mod_s_3 = _Betriebs_status_mod_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 4, 1, 6),
    _Betriebs_status_mod_s_3_Type()
)
betriebs_status_mod_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    betriebs_status_mod_s_3.setStatus("current")
_Modul_var_para_1_mod_s_3_Type = DisplayString
_Modul_var_para_1_mod_s_3_Object = MibTableColumn
modul_var_para_1_mod_s_3 = _Modul_var_para_1_mod_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 4, 1, 7),
    _Modul_var_para_1_mod_s_3_Type()
)
modul_var_para_1_mod_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_1_mod_s_3.setStatus("current")
_Modul_var_para_2_mod_s_3_Type = DisplayString
_Modul_var_para_2_mod_s_3_Object = MibTableColumn
modul_var_para_2_mod_s_3 = _Modul_var_para_2_mod_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 4, 1, 8),
    _Modul_var_para_2_mod_s_3_Type()
)
modul_var_para_2_mod_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_2_mod_s_3.setStatus("current")
_Modul_var_para_3_mod_s_3_Type = DisplayString
_Modul_var_para_3_mod_s_3_Object = MibTableColumn
modul_var_para_3_mod_s_3 = _Modul_var_para_3_mod_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 4, 1, 9),
    _Modul_var_para_3_mod_s_3_Type()
)
modul_var_para_3_mod_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_3_mod_s_3.setStatus("current")
_Modul_var_para_4_mod_s_3_Type = DisplayString
_Modul_var_para_4_mod_s_3_Object = MibTableColumn
modul_var_para_4_mod_s_3 = _Modul_var_para_4_mod_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 4, 1, 10),
    _Modul_var_para_4_mod_s_3_Type()
)
modul_var_para_4_mod_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_4_mod_s_3.setStatus("current")
_Modul_var_para_5_mod_s_3_Type = DisplayString
_Modul_var_para_5_mod_s_3_Object = MibTableColumn
modul_var_para_5_mod_s_3 = _Modul_var_para_5_mod_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 4, 1, 11),
    _Modul_var_para_5_mod_s_3_Type()
)
modul_var_para_5_mod_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_5_mod_s_3.setStatus("current")
_Modul_var_para_6_mod_s_3_Type = DisplayString
_Modul_var_para_6_mod_s_3_Object = MibTableColumn
modul_var_para_6_mod_s_3 = _Modul_var_para_6_mod_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 4, 1, 12),
    _Modul_var_para_6_mod_s_3_Type()
)
modul_var_para_6_mod_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_6_mod_s_3.setStatus("current")
_Modul_var_para_7_mod_s_3_Type = DisplayString
_Modul_var_para_7_mod_s_3_Object = MibTableColumn
modul_var_para_7_mod_s_3 = _Modul_var_para_7_mod_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 4, 1, 13),
    _Modul_var_para_7_mod_s_3_Type()
)
modul_var_para_7_mod_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_7_mod_s_3.setStatus("current")
_Modul_var_para_8_mod_s_3_Type = DisplayString
_Modul_var_para_8_mod_s_3_Object = MibTableColumn
modul_var_para_8_mod_s_3 = _Modul_var_para_8_mod_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 4, 1, 14),
    _Modul_var_para_8_mod_s_3_Type()
)
modul_var_para_8_mod_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_8_mod_s_3.setStatus("current")
_Modul_var_para_9_mod_s_3_Type = DisplayString
_Modul_var_para_9_mod_s_3_Object = MibTableColumn
modul_var_para_9_mod_s_3 = _Modul_var_para_9_mod_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 4, 1, 15),
    _Modul_var_para_9_mod_s_3_Type()
)
modul_var_para_9_mod_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_9_mod_s_3.setStatus("current")
_Modul_var_para_10_mod_s_3_Type = DisplayString
_Modul_var_para_10_mod_s_3_Object = MibTableColumn
modul_var_para_10_mod_s_3 = _Modul_var_para_10_mod_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 4, 1, 16),
    _Modul_var_para_10_mod_s_3_Type()
)
modul_var_para_10_mod_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_10_mod_s_3.setStatus("current")
_Modul_var_para_11_mod_s_3_Type = DisplayString
_Modul_var_para_11_mod_s_3_Object = MibTableColumn
modul_var_para_11_mod_s_3 = _Modul_var_para_11_mod_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 4, 1, 17),
    _Modul_var_para_11_mod_s_3_Type()
)
modul_var_para_11_mod_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_11_mod_s_3.setStatus("current")
_Modul_var_para_12_mod_s_3_Type = DisplayString
_Modul_var_para_12_mod_s_3_Object = MibTableColumn
modul_var_para_12_mod_s_3 = _Modul_var_para_12_mod_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 4, 1, 18),
    _Modul_var_para_12_mod_s_3_Type()
)
modul_var_para_12_mod_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_12_mod_s_3.setStatus("current")
_Modul_var_para_13_mod_s_3_Type = DisplayString
_Modul_var_para_13_mod_s_3_Object = MibTableColumn
modul_var_para_13_mod_s_3 = _Modul_var_para_13_mod_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 4, 1, 19),
    _Modul_var_para_13_mod_s_3_Type()
)
modul_var_para_13_mod_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_13_mod_s_3.setStatus("current")
_Modul_var_para_14_mod_s_3_Type = DisplayString
_Modul_var_para_14_mod_s_3_Object = MibTableColumn
modul_var_para_14_mod_s_3 = _Modul_var_para_14_mod_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 4, 1, 20),
    _Modul_var_para_14_mod_s_3_Type()
)
modul_var_para_14_mod_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_14_mod_s_3.setStatus("current")
_Modul_var_para_15_mod_s_3_Type = DisplayString
_Modul_var_para_15_mod_s_3_Object = MibTableColumn
modul_var_para_15_mod_s_3 = _Modul_var_para_15_mod_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 4, 1, 21),
    _Modul_var_para_15_mod_s_3_Type()
)
modul_var_para_15_mod_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_15_mod_s_3.setStatus("current")
_Modul_var_para_16_mod_s_3_Type = DisplayString
_Modul_var_para_16_mod_s_3_Object = MibTableColumn
modul_var_para_16_mod_s_3 = _Modul_var_para_16_mod_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 4, 1, 22),
    _Modul_var_para_16_mod_s_3_Type()
)
modul_var_para_16_mod_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_16_mod_s_3.setStatus("current")
_Modul_var_para_17_mod_s_3_Type = DisplayString
_Modul_var_para_17_mod_s_3_Object = MibTableColumn
modul_var_para_17_mod_s_3 = _Modul_var_para_17_mod_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 4, 1, 23),
    _Modul_var_para_17_mod_s_3_Type()
)
modul_var_para_17_mod_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_17_mod_s_3.setStatus("current")
_Modul_var_para_18_mod_s_3_Type = DisplayString
_Modul_var_para_18_mod_s_3_Object = MibTableColumn
modul_var_para_18_mod_s_3 = _Modul_var_para_18_mod_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 4, 1, 24),
    _Modul_var_para_18_mod_s_3_Type()
)
modul_var_para_18_mod_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_18_mod_s_3.setStatus("current")
_Modul_var_para_19_mod_s_3_Type = DisplayString
_Modul_var_para_19_mod_s_3_Object = MibTableColumn
modul_var_para_19_mod_s_3 = _Modul_var_para_19_mod_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 4, 1, 25),
    _Modul_var_para_19_mod_s_3_Type()
)
modul_var_para_19_mod_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_19_mod_s_3.setStatus("current")
_ModulTable_mod_s_4_Object = MibTable
modulTable_mod_s_4 = _ModulTable_mod_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 5)
)
if mibBuilder.loadTexts:
    modulTable_mod_s_4.setStatus("current")
_ModulEntry_mod_s_4_Object = MibTableRow
modulEntry_mod_s_4 = _ModulEntry_mod_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 5, 1)
)
modulEntry_mod_s_4.setIndexNames(
    (0, "AK-FUNKTECHNIK-MIB", "modulindex-mod-s-4"),
)
if mibBuilder.loadTexts:
    modulEntry_mod_s_4.setStatus("current")
_Modulindex_mod_s_4_Type = DisplayString
_Modulindex_mod_s_4_Object = MibTableColumn
modulindex_mod_s_4 = _Modulindex_mod_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 5, 1, 1),
    _Modulindex_mod_s_4_Type()
)
modulindex_mod_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulindex_mod_s_4.setStatus("current")
_Modul_typ_mod_s_4_Type = DisplayString
_Modul_typ_mod_s_4_Object = MibTableColumn
modul_typ_mod_s_4 = _Modul_typ_mod_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 5, 1, 2),
    _Modul_typ_mod_s_4_Type()
)
modul_typ_mod_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_typ_mod_s_4.setStatus("current")
_Seriennummer_mod_s_4_Type = DisplayString
_Seriennummer_mod_s_4_Object = MibTableColumn
seriennummer_mod_s_4 = _Seriennummer_mod_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 5, 1, 3),
    _Seriennummer_mod_s_4_Type()
)
seriennummer_mod_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seriennummer_mod_s_4.setStatus("current")
_Firmware_version_mod_s_4_Type = DisplayString
_Firmware_version_mod_s_4_Object = MibTableColumn
firmware_version_mod_s_4 = _Firmware_version_mod_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 5, 1, 4),
    _Firmware_version_mod_s_4_Type()
)
firmware_version_mod_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmware_version_mod_s_4.setStatus("current")
_Hardware_zustand_mod_s_4_Type = DisplayString
_Hardware_zustand_mod_s_4_Object = MibTableColumn
hardware_zustand_mod_s_4 = _Hardware_zustand_mod_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 5, 1, 5),
    _Hardware_zustand_mod_s_4_Type()
)
hardware_zustand_mod_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardware_zustand_mod_s_4.setStatus("current")
_Betriebs_status_mod_s_4_Type = DisplayString
_Betriebs_status_mod_s_4_Object = MibTableColumn
betriebs_status_mod_s_4 = _Betriebs_status_mod_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 5, 1, 6),
    _Betriebs_status_mod_s_4_Type()
)
betriebs_status_mod_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    betriebs_status_mod_s_4.setStatus("current")
_Modul_var_para_1_mod_s_4_Type = DisplayString
_Modul_var_para_1_mod_s_4_Object = MibTableColumn
modul_var_para_1_mod_s_4 = _Modul_var_para_1_mod_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 5, 1, 7),
    _Modul_var_para_1_mod_s_4_Type()
)
modul_var_para_1_mod_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_1_mod_s_4.setStatus("current")
_Modul_var_para_2_mod_s_4_Type = DisplayString
_Modul_var_para_2_mod_s_4_Object = MibTableColumn
modul_var_para_2_mod_s_4 = _Modul_var_para_2_mod_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 5, 1, 8),
    _Modul_var_para_2_mod_s_4_Type()
)
modul_var_para_2_mod_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_2_mod_s_4.setStatus("current")
_Modul_var_para_3_mod_s_4_Type = DisplayString
_Modul_var_para_3_mod_s_4_Object = MibTableColumn
modul_var_para_3_mod_s_4 = _Modul_var_para_3_mod_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 5, 1, 9),
    _Modul_var_para_3_mod_s_4_Type()
)
modul_var_para_3_mod_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_3_mod_s_4.setStatus("current")
_Modul_var_para_4_mod_s_4_Type = DisplayString
_Modul_var_para_4_mod_s_4_Object = MibTableColumn
modul_var_para_4_mod_s_4 = _Modul_var_para_4_mod_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 5, 1, 10),
    _Modul_var_para_4_mod_s_4_Type()
)
modul_var_para_4_mod_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_4_mod_s_4.setStatus("current")
_Modul_var_para_5_mod_s_4_Type = DisplayString
_Modul_var_para_5_mod_s_4_Object = MibTableColumn
modul_var_para_5_mod_s_4 = _Modul_var_para_5_mod_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 5, 1, 11),
    _Modul_var_para_5_mod_s_4_Type()
)
modul_var_para_5_mod_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_5_mod_s_4.setStatus("current")
_Modul_var_para_6_mod_s_4_Type = DisplayString
_Modul_var_para_6_mod_s_4_Object = MibTableColumn
modul_var_para_6_mod_s_4 = _Modul_var_para_6_mod_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 5, 1, 12),
    _Modul_var_para_6_mod_s_4_Type()
)
modul_var_para_6_mod_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_6_mod_s_4.setStatus("current")
_Modul_var_para_7_mod_s_4_Type = DisplayString
_Modul_var_para_7_mod_s_4_Object = MibTableColumn
modul_var_para_7_mod_s_4 = _Modul_var_para_7_mod_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 5, 1, 13),
    _Modul_var_para_7_mod_s_4_Type()
)
modul_var_para_7_mod_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_7_mod_s_4.setStatus("current")
_Modul_var_para_8_mod_s_4_Type = DisplayString
_Modul_var_para_8_mod_s_4_Object = MibTableColumn
modul_var_para_8_mod_s_4 = _Modul_var_para_8_mod_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 5, 1, 14),
    _Modul_var_para_8_mod_s_4_Type()
)
modul_var_para_8_mod_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_8_mod_s_4.setStatus("current")
_Modul_var_para_9_mod_s_4_Type = DisplayString
_Modul_var_para_9_mod_s_4_Object = MibTableColumn
modul_var_para_9_mod_s_4 = _Modul_var_para_9_mod_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 5, 1, 15),
    _Modul_var_para_9_mod_s_4_Type()
)
modul_var_para_9_mod_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_9_mod_s_4.setStatus("current")
_Modul_var_para_10_mod_s_4_Type = DisplayString
_Modul_var_para_10_mod_s_4_Object = MibTableColumn
modul_var_para_10_mod_s_4 = _Modul_var_para_10_mod_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 5, 1, 16),
    _Modul_var_para_10_mod_s_4_Type()
)
modul_var_para_10_mod_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_10_mod_s_4.setStatus("current")
_Modul_var_para_11_mod_s_4_Type = DisplayString
_Modul_var_para_11_mod_s_4_Object = MibTableColumn
modul_var_para_11_mod_s_4 = _Modul_var_para_11_mod_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 5, 1, 17),
    _Modul_var_para_11_mod_s_4_Type()
)
modul_var_para_11_mod_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_11_mod_s_4.setStatus("current")
_Modul_var_para_12_mod_s_4_Type = DisplayString
_Modul_var_para_12_mod_s_4_Object = MibTableColumn
modul_var_para_12_mod_s_4 = _Modul_var_para_12_mod_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 5, 1, 18),
    _Modul_var_para_12_mod_s_4_Type()
)
modul_var_para_12_mod_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_12_mod_s_4.setStatus("current")
_Modul_var_para_13_mod_s_4_Type = DisplayString
_Modul_var_para_13_mod_s_4_Object = MibTableColumn
modul_var_para_13_mod_s_4 = _Modul_var_para_13_mod_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 5, 1, 19),
    _Modul_var_para_13_mod_s_4_Type()
)
modul_var_para_13_mod_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_13_mod_s_4.setStatus("current")
_Modul_var_para_14_mod_s_4_Type = DisplayString
_Modul_var_para_14_mod_s_4_Object = MibTableColumn
modul_var_para_14_mod_s_4 = _Modul_var_para_14_mod_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 5, 1, 20),
    _Modul_var_para_14_mod_s_4_Type()
)
modul_var_para_14_mod_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_14_mod_s_4.setStatus("current")
_Modul_var_para_15_mod_s_4_Type = DisplayString
_Modul_var_para_15_mod_s_4_Object = MibTableColumn
modul_var_para_15_mod_s_4 = _Modul_var_para_15_mod_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 5, 1, 21),
    _Modul_var_para_15_mod_s_4_Type()
)
modul_var_para_15_mod_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_15_mod_s_4.setStatus("current")
_Modul_var_para_16_mod_s_4_Type = DisplayString
_Modul_var_para_16_mod_s_4_Object = MibTableColumn
modul_var_para_16_mod_s_4 = _Modul_var_para_16_mod_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 5, 1, 22),
    _Modul_var_para_16_mod_s_4_Type()
)
modul_var_para_16_mod_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_16_mod_s_4.setStatus("current")
_Modul_var_para_17_mod_s_4_Type = DisplayString
_Modul_var_para_17_mod_s_4_Object = MibTableColumn
modul_var_para_17_mod_s_4 = _Modul_var_para_17_mod_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 5, 1, 23),
    _Modul_var_para_17_mod_s_4_Type()
)
modul_var_para_17_mod_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_17_mod_s_4.setStatus("current")
_Modul_var_para_18_mod_s_4_Type = DisplayString
_Modul_var_para_18_mod_s_4_Object = MibTableColumn
modul_var_para_18_mod_s_4 = _Modul_var_para_18_mod_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 5, 1, 24),
    _Modul_var_para_18_mod_s_4_Type()
)
modul_var_para_18_mod_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_18_mod_s_4.setStatus("current")
_Modul_var_para_19_mod_s_4_Type = DisplayString
_Modul_var_para_19_mod_s_4_Object = MibTableColumn
modul_var_para_19_mod_s_4 = _Modul_var_para_19_mod_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 5, 1, 25),
    _Modul_var_para_19_mod_s_4_Type()
)
modul_var_para_19_mod_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_19_mod_s_4.setStatus("current")
_ModulTable_mod_s_5_Object = MibTable
modulTable_mod_s_5 = _ModulTable_mod_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 6)
)
if mibBuilder.loadTexts:
    modulTable_mod_s_5.setStatus("current")
_ModulEntry_mod_s_5_Object = MibTableRow
modulEntry_mod_s_5 = _ModulEntry_mod_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 6, 1)
)
modulEntry_mod_s_5.setIndexNames(
    (0, "AK-FUNKTECHNIK-MIB", "modulindex-mod-s-5"),
)
if mibBuilder.loadTexts:
    modulEntry_mod_s_5.setStatus("current")
_Modulindex_mod_s_5_Type = DisplayString
_Modulindex_mod_s_5_Object = MibTableColumn
modulindex_mod_s_5 = _Modulindex_mod_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 6, 1, 1),
    _Modulindex_mod_s_5_Type()
)
modulindex_mod_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulindex_mod_s_5.setStatus("current")
_Modul_typ_mod_s_5_Type = DisplayString
_Modul_typ_mod_s_5_Object = MibTableColumn
modul_typ_mod_s_5 = _Modul_typ_mod_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 6, 1, 2),
    _Modul_typ_mod_s_5_Type()
)
modul_typ_mod_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_typ_mod_s_5.setStatus("current")
_Seriennummer_mod_s_5_Type = DisplayString
_Seriennummer_mod_s_5_Object = MibTableColumn
seriennummer_mod_s_5 = _Seriennummer_mod_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 6, 1, 3),
    _Seriennummer_mod_s_5_Type()
)
seriennummer_mod_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seriennummer_mod_s_5.setStatus("current")
_Firmware_version_mod_s_5_Type = DisplayString
_Firmware_version_mod_s_5_Object = MibTableColumn
firmware_version_mod_s_5 = _Firmware_version_mod_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 6, 1, 4),
    _Firmware_version_mod_s_5_Type()
)
firmware_version_mod_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmware_version_mod_s_5.setStatus("current")
_Hardware_zustand_mod_s_5_Type = DisplayString
_Hardware_zustand_mod_s_5_Object = MibTableColumn
hardware_zustand_mod_s_5 = _Hardware_zustand_mod_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 6, 1, 5),
    _Hardware_zustand_mod_s_5_Type()
)
hardware_zustand_mod_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardware_zustand_mod_s_5.setStatus("current")
_Betriebs_status_mod_s_5_Type = DisplayString
_Betriebs_status_mod_s_5_Object = MibTableColumn
betriebs_status_mod_s_5 = _Betriebs_status_mod_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 6, 1, 6),
    _Betriebs_status_mod_s_5_Type()
)
betriebs_status_mod_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    betriebs_status_mod_s_5.setStatus("current")
_Modul_var_para_1_mod_s_5_Type = DisplayString
_Modul_var_para_1_mod_s_5_Object = MibTableColumn
modul_var_para_1_mod_s_5 = _Modul_var_para_1_mod_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 6, 1, 7),
    _Modul_var_para_1_mod_s_5_Type()
)
modul_var_para_1_mod_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_1_mod_s_5.setStatus("current")
_Modul_var_para_2_mod_s_5_Type = DisplayString
_Modul_var_para_2_mod_s_5_Object = MibTableColumn
modul_var_para_2_mod_s_5 = _Modul_var_para_2_mod_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 6, 1, 8),
    _Modul_var_para_2_mod_s_5_Type()
)
modul_var_para_2_mod_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_2_mod_s_5.setStatus("current")
_Modul_var_para_3_mod_s_5_Type = DisplayString
_Modul_var_para_3_mod_s_5_Object = MibTableColumn
modul_var_para_3_mod_s_5 = _Modul_var_para_3_mod_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 6, 1, 9),
    _Modul_var_para_3_mod_s_5_Type()
)
modul_var_para_3_mod_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_3_mod_s_5.setStatus("current")
_Modul_var_para_4_mod_s_5_Type = DisplayString
_Modul_var_para_4_mod_s_5_Object = MibTableColumn
modul_var_para_4_mod_s_5 = _Modul_var_para_4_mod_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 6, 1, 10),
    _Modul_var_para_4_mod_s_5_Type()
)
modul_var_para_4_mod_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_4_mod_s_5.setStatus("current")
_Modul_var_para_5_mod_s_5_Type = DisplayString
_Modul_var_para_5_mod_s_5_Object = MibTableColumn
modul_var_para_5_mod_s_5 = _Modul_var_para_5_mod_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 6, 1, 11),
    _Modul_var_para_5_mod_s_5_Type()
)
modul_var_para_5_mod_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_5_mod_s_5.setStatus("current")
_Modul_var_para_6_mod_s_5_Type = DisplayString
_Modul_var_para_6_mod_s_5_Object = MibTableColumn
modul_var_para_6_mod_s_5 = _Modul_var_para_6_mod_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 6, 1, 12),
    _Modul_var_para_6_mod_s_5_Type()
)
modul_var_para_6_mod_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_6_mod_s_5.setStatus("current")
_Modul_var_para_7_mod_s_5_Type = DisplayString
_Modul_var_para_7_mod_s_5_Object = MibTableColumn
modul_var_para_7_mod_s_5 = _Modul_var_para_7_mod_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 6, 1, 13),
    _Modul_var_para_7_mod_s_5_Type()
)
modul_var_para_7_mod_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_7_mod_s_5.setStatus("current")
_Modul_var_para_8_mod_s_5_Type = DisplayString
_Modul_var_para_8_mod_s_5_Object = MibTableColumn
modul_var_para_8_mod_s_5 = _Modul_var_para_8_mod_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 6, 1, 14),
    _Modul_var_para_8_mod_s_5_Type()
)
modul_var_para_8_mod_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_8_mod_s_5.setStatus("current")
_Modul_var_para_9_mod_s_5_Type = DisplayString
_Modul_var_para_9_mod_s_5_Object = MibTableColumn
modul_var_para_9_mod_s_5 = _Modul_var_para_9_mod_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 6, 1, 15),
    _Modul_var_para_9_mod_s_5_Type()
)
modul_var_para_9_mod_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_9_mod_s_5.setStatus("current")
_Modul_var_para_10_mod_s_5_Type = DisplayString
_Modul_var_para_10_mod_s_5_Object = MibTableColumn
modul_var_para_10_mod_s_5 = _Modul_var_para_10_mod_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 6, 1, 16),
    _Modul_var_para_10_mod_s_5_Type()
)
modul_var_para_10_mod_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_10_mod_s_5.setStatus("current")
_Modul_var_para_11_mod_s_5_Type = DisplayString
_Modul_var_para_11_mod_s_5_Object = MibTableColumn
modul_var_para_11_mod_s_5 = _Modul_var_para_11_mod_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 6, 1, 17),
    _Modul_var_para_11_mod_s_5_Type()
)
modul_var_para_11_mod_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_11_mod_s_5.setStatus("current")
_Modul_var_para_12_mod_s_5_Type = DisplayString
_Modul_var_para_12_mod_s_5_Object = MibTableColumn
modul_var_para_12_mod_s_5 = _Modul_var_para_12_mod_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 6, 1, 18),
    _Modul_var_para_12_mod_s_5_Type()
)
modul_var_para_12_mod_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_12_mod_s_5.setStatus("current")
_Modul_var_para_13_mod_s_5_Type = DisplayString
_Modul_var_para_13_mod_s_5_Object = MibTableColumn
modul_var_para_13_mod_s_5 = _Modul_var_para_13_mod_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 6, 1, 19),
    _Modul_var_para_13_mod_s_5_Type()
)
modul_var_para_13_mod_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_13_mod_s_5.setStatus("current")
_Modul_var_para_14_mod_s_5_Type = DisplayString
_Modul_var_para_14_mod_s_5_Object = MibTableColumn
modul_var_para_14_mod_s_5 = _Modul_var_para_14_mod_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 6, 1, 20),
    _Modul_var_para_14_mod_s_5_Type()
)
modul_var_para_14_mod_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_14_mod_s_5.setStatus("current")
_Modul_var_para_15_mod_s_5_Type = DisplayString
_Modul_var_para_15_mod_s_5_Object = MibTableColumn
modul_var_para_15_mod_s_5 = _Modul_var_para_15_mod_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 6, 1, 21),
    _Modul_var_para_15_mod_s_5_Type()
)
modul_var_para_15_mod_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_15_mod_s_5.setStatus("current")
_Modul_var_para_16_mod_s_5_Type = DisplayString
_Modul_var_para_16_mod_s_5_Object = MibTableColumn
modul_var_para_16_mod_s_5 = _Modul_var_para_16_mod_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 6, 1, 22),
    _Modul_var_para_16_mod_s_5_Type()
)
modul_var_para_16_mod_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_16_mod_s_5.setStatus("current")
_Modul_var_para_17_mod_s_5_Type = DisplayString
_Modul_var_para_17_mod_s_5_Object = MibTableColumn
modul_var_para_17_mod_s_5 = _Modul_var_para_17_mod_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 6, 1, 23),
    _Modul_var_para_17_mod_s_5_Type()
)
modul_var_para_17_mod_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_17_mod_s_5.setStatus("current")
_Modul_var_para_18_mod_s_5_Type = DisplayString
_Modul_var_para_18_mod_s_5_Object = MibTableColumn
modul_var_para_18_mod_s_5 = _Modul_var_para_18_mod_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 6, 1, 24),
    _Modul_var_para_18_mod_s_5_Type()
)
modul_var_para_18_mod_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_18_mod_s_5.setStatus("current")
_Modul_var_para_19_mod_s_5_Type = DisplayString
_Modul_var_para_19_mod_s_5_Object = MibTableColumn
modul_var_para_19_mod_s_5 = _Modul_var_para_19_mod_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 6, 1, 25),
    _Modul_var_para_19_mod_s_5_Type()
)
modul_var_para_19_mod_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_19_mod_s_5.setStatus("current")
_ModulTable_mod_s_6_Object = MibTable
modulTable_mod_s_6 = _ModulTable_mod_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 7)
)
if mibBuilder.loadTexts:
    modulTable_mod_s_6.setStatus("current")
_ModulEntry_mod_s_6_Object = MibTableRow
modulEntry_mod_s_6 = _ModulEntry_mod_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 7, 1)
)
modulEntry_mod_s_6.setIndexNames(
    (0, "AK-FUNKTECHNIK-MIB", "modulindex-mod-s-6"),
)
if mibBuilder.loadTexts:
    modulEntry_mod_s_6.setStatus("current")
_Modulindex_mod_s_6_Type = DisplayString
_Modulindex_mod_s_6_Object = MibTableColumn
modulindex_mod_s_6 = _Modulindex_mod_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 7, 1, 1),
    _Modulindex_mod_s_6_Type()
)
modulindex_mod_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulindex_mod_s_6.setStatus("current")
_Modul_typ_mod_s_6_Type = DisplayString
_Modul_typ_mod_s_6_Object = MibTableColumn
modul_typ_mod_s_6 = _Modul_typ_mod_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 7, 1, 2),
    _Modul_typ_mod_s_6_Type()
)
modul_typ_mod_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_typ_mod_s_6.setStatus("current")
_Seriennummer_mod_s_6_Type = DisplayString
_Seriennummer_mod_s_6_Object = MibTableColumn
seriennummer_mod_s_6 = _Seriennummer_mod_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 7, 1, 3),
    _Seriennummer_mod_s_6_Type()
)
seriennummer_mod_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seriennummer_mod_s_6.setStatus("current")
_Firmware_version_mod_s_6_Type = DisplayString
_Firmware_version_mod_s_6_Object = MibTableColumn
firmware_version_mod_s_6 = _Firmware_version_mod_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 7, 1, 4),
    _Firmware_version_mod_s_6_Type()
)
firmware_version_mod_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmware_version_mod_s_6.setStatus("current")
_Hardware_zustand_mod_s_6_Type = DisplayString
_Hardware_zustand_mod_s_6_Object = MibTableColumn
hardware_zustand_mod_s_6 = _Hardware_zustand_mod_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 7, 1, 5),
    _Hardware_zustand_mod_s_6_Type()
)
hardware_zustand_mod_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardware_zustand_mod_s_6.setStatus("current")
_Betriebs_status_mod_s_6_Type = DisplayString
_Betriebs_status_mod_s_6_Object = MibTableColumn
betriebs_status_mod_s_6 = _Betriebs_status_mod_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 7, 1, 6),
    _Betriebs_status_mod_s_6_Type()
)
betriebs_status_mod_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    betriebs_status_mod_s_6.setStatus("current")
_Modul_var_para_1_mod_s_6_Type = DisplayString
_Modul_var_para_1_mod_s_6_Object = MibTableColumn
modul_var_para_1_mod_s_6 = _Modul_var_para_1_mod_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 7, 1, 7),
    _Modul_var_para_1_mod_s_6_Type()
)
modul_var_para_1_mod_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_1_mod_s_6.setStatus("current")
_Modul_var_para_2_mod_s_6_Type = DisplayString
_Modul_var_para_2_mod_s_6_Object = MibTableColumn
modul_var_para_2_mod_s_6 = _Modul_var_para_2_mod_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 7, 1, 8),
    _Modul_var_para_2_mod_s_6_Type()
)
modul_var_para_2_mod_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_2_mod_s_6.setStatus("current")
_Modul_var_para_3_mod_s_6_Type = DisplayString
_Modul_var_para_3_mod_s_6_Object = MibTableColumn
modul_var_para_3_mod_s_6 = _Modul_var_para_3_mod_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 7, 1, 9),
    _Modul_var_para_3_mod_s_6_Type()
)
modul_var_para_3_mod_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_3_mod_s_6.setStatus("current")
_Modul_var_para_4_mod_s_6_Type = DisplayString
_Modul_var_para_4_mod_s_6_Object = MibTableColumn
modul_var_para_4_mod_s_6 = _Modul_var_para_4_mod_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 7, 1, 10),
    _Modul_var_para_4_mod_s_6_Type()
)
modul_var_para_4_mod_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_4_mod_s_6.setStatus("current")
_Modul_var_para_5_mod_s_6_Type = DisplayString
_Modul_var_para_5_mod_s_6_Object = MibTableColumn
modul_var_para_5_mod_s_6 = _Modul_var_para_5_mod_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 7, 1, 11),
    _Modul_var_para_5_mod_s_6_Type()
)
modul_var_para_5_mod_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_5_mod_s_6.setStatus("current")
_Modul_var_para_6_mod_s_6_Type = DisplayString
_Modul_var_para_6_mod_s_6_Object = MibTableColumn
modul_var_para_6_mod_s_6 = _Modul_var_para_6_mod_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 7, 1, 12),
    _Modul_var_para_6_mod_s_6_Type()
)
modul_var_para_6_mod_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_6_mod_s_6.setStatus("current")
_Modul_var_para_7_mod_s_6_Type = DisplayString
_Modul_var_para_7_mod_s_6_Object = MibTableColumn
modul_var_para_7_mod_s_6 = _Modul_var_para_7_mod_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 7, 1, 13),
    _Modul_var_para_7_mod_s_6_Type()
)
modul_var_para_7_mod_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_7_mod_s_6.setStatus("current")
_Modul_var_para_8_mod_s_6_Type = DisplayString
_Modul_var_para_8_mod_s_6_Object = MibTableColumn
modul_var_para_8_mod_s_6 = _Modul_var_para_8_mod_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 7, 1, 14),
    _Modul_var_para_8_mod_s_6_Type()
)
modul_var_para_8_mod_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_8_mod_s_6.setStatus("current")
_Modul_var_para_9_mod_s_6_Type = DisplayString
_Modul_var_para_9_mod_s_6_Object = MibTableColumn
modul_var_para_9_mod_s_6 = _Modul_var_para_9_mod_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 7, 1, 15),
    _Modul_var_para_9_mod_s_6_Type()
)
modul_var_para_9_mod_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_9_mod_s_6.setStatus("current")
_Modul_var_para_10_mod_s_6_Type = DisplayString
_Modul_var_para_10_mod_s_6_Object = MibTableColumn
modul_var_para_10_mod_s_6 = _Modul_var_para_10_mod_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 7, 1, 16),
    _Modul_var_para_10_mod_s_6_Type()
)
modul_var_para_10_mod_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_10_mod_s_6.setStatus("current")
_Modul_var_para_11_mod_s_6_Type = DisplayString
_Modul_var_para_11_mod_s_6_Object = MibTableColumn
modul_var_para_11_mod_s_6 = _Modul_var_para_11_mod_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 7, 1, 17),
    _Modul_var_para_11_mod_s_6_Type()
)
modul_var_para_11_mod_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_11_mod_s_6.setStatus("current")
_Modul_var_para_12_mod_s_6_Type = DisplayString
_Modul_var_para_12_mod_s_6_Object = MibTableColumn
modul_var_para_12_mod_s_6 = _Modul_var_para_12_mod_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 7, 1, 18),
    _Modul_var_para_12_mod_s_6_Type()
)
modul_var_para_12_mod_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_12_mod_s_6.setStatus("current")
_Modul_var_para_13_mod_s_6_Type = DisplayString
_Modul_var_para_13_mod_s_6_Object = MibTableColumn
modul_var_para_13_mod_s_6 = _Modul_var_para_13_mod_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 7, 1, 19),
    _Modul_var_para_13_mod_s_6_Type()
)
modul_var_para_13_mod_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_13_mod_s_6.setStatus("current")
_Modul_var_para_14_mod_s_6_Type = DisplayString
_Modul_var_para_14_mod_s_6_Object = MibTableColumn
modul_var_para_14_mod_s_6 = _Modul_var_para_14_mod_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 7, 1, 20),
    _Modul_var_para_14_mod_s_6_Type()
)
modul_var_para_14_mod_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_14_mod_s_6.setStatus("current")
_Modul_var_para_15_mod_s_6_Type = DisplayString
_Modul_var_para_15_mod_s_6_Object = MibTableColumn
modul_var_para_15_mod_s_6 = _Modul_var_para_15_mod_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 7, 1, 21),
    _Modul_var_para_15_mod_s_6_Type()
)
modul_var_para_15_mod_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_15_mod_s_6.setStatus("current")
_Modul_var_para_16_mod_s_6_Type = DisplayString
_Modul_var_para_16_mod_s_6_Object = MibTableColumn
modul_var_para_16_mod_s_6 = _Modul_var_para_16_mod_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 7, 1, 22),
    _Modul_var_para_16_mod_s_6_Type()
)
modul_var_para_16_mod_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_16_mod_s_6.setStatus("current")
_Modul_var_para_17_mod_s_6_Type = DisplayString
_Modul_var_para_17_mod_s_6_Object = MibTableColumn
modul_var_para_17_mod_s_6 = _Modul_var_para_17_mod_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 7, 1, 23),
    _Modul_var_para_17_mod_s_6_Type()
)
modul_var_para_17_mod_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_17_mod_s_6.setStatus("current")
_Modul_var_para_18_mod_s_6_Type = DisplayString
_Modul_var_para_18_mod_s_6_Object = MibTableColumn
modul_var_para_18_mod_s_6 = _Modul_var_para_18_mod_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 7, 1, 24),
    _Modul_var_para_18_mod_s_6_Type()
)
modul_var_para_18_mod_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_18_mod_s_6.setStatus("current")
_Modul_var_para_19_mod_s_6_Type = DisplayString
_Modul_var_para_19_mod_s_6_Object = MibTableColumn
modul_var_para_19_mod_s_6 = _Modul_var_para_19_mod_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 7, 1, 25),
    _Modul_var_para_19_mod_s_6_Type()
)
modul_var_para_19_mod_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_19_mod_s_6.setStatus("current")
_ModulTable_mod_s_7_Object = MibTable
modulTable_mod_s_7 = _ModulTable_mod_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 8)
)
if mibBuilder.loadTexts:
    modulTable_mod_s_7.setStatus("current")
_ModulEntry_mod_s_7_Object = MibTableRow
modulEntry_mod_s_7 = _ModulEntry_mod_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 8, 1)
)
modulEntry_mod_s_7.setIndexNames(
    (0, "AK-FUNKTECHNIK-MIB", "modulindex-mod-s-7"),
)
if mibBuilder.loadTexts:
    modulEntry_mod_s_7.setStatus("current")
_Modulindex_mod_s_7_Type = DisplayString
_Modulindex_mod_s_7_Object = MibTableColumn
modulindex_mod_s_7 = _Modulindex_mod_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 8, 1, 1),
    _Modulindex_mod_s_7_Type()
)
modulindex_mod_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulindex_mod_s_7.setStatus("current")
_Modul_typ_mod_s_7_Type = DisplayString
_Modul_typ_mod_s_7_Object = MibTableColumn
modul_typ_mod_s_7 = _Modul_typ_mod_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 8, 1, 2),
    _Modul_typ_mod_s_7_Type()
)
modul_typ_mod_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_typ_mod_s_7.setStatus("current")
_Seriennummer_mod_s_7_Type = DisplayString
_Seriennummer_mod_s_7_Object = MibTableColumn
seriennummer_mod_s_7 = _Seriennummer_mod_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 8, 1, 3),
    _Seriennummer_mod_s_7_Type()
)
seriennummer_mod_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seriennummer_mod_s_7.setStatus("current")
_Firmware_version_mod_s_7_Type = DisplayString
_Firmware_version_mod_s_7_Object = MibTableColumn
firmware_version_mod_s_7 = _Firmware_version_mod_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 8, 1, 4),
    _Firmware_version_mod_s_7_Type()
)
firmware_version_mod_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmware_version_mod_s_7.setStatus("current")
_Hardware_zustand_mod_s_7_Type = DisplayString
_Hardware_zustand_mod_s_7_Object = MibTableColumn
hardware_zustand_mod_s_7 = _Hardware_zustand_mod_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 8, 1, 5),
    _Hardware_zustand_mod_s_7_Type()
)
hardware_zustand_mod_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardware_zustand_mod_s_7.setStatus("current")
_Betriebs_status_mod_s_7_Type = DisplayString
_Betriebs_status_mod_s_7_Object = MibTableColumn
betriebs_status_mod_s_7 = _Betriebs_status_mod_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 8, 1, 6),
    _Betriebs_status_mod_s_7_Type()
)
betriebs_status_mod_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    betriebs_status_mod_s_7.setStatus("current")
_Modul_var_para_1_mod_s_7_Type = DisplayString
_Modul_var_para_1_mod_s_7_Object = MibTableColumn
modul_var_para_1_mod_s_7 = _Modul_var_para_1_mod_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 8, 1, 7),
    _Modul_var_para_1_mod_s_7_Type()
)
modul_var_para_1_mod_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_1_mod_s_7.setStatus("current")
_Modul_var_para_2_mod_s_7_Type = DisplayString
_Modul_var_para_2_mod_s_7_Object = MibTableColumn
modul_var_para_2_mod_s_7 = _Modul_var_para_2_mod_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 8, 1, 8),
    _Modul_var_para_2_mod_s_7_Type()
)
modul_var_para_2_mod_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_2_mod_s_7.setStatus("current")
_Modul_var_para_3_mod_s_7_Type = DisplayString
_Modul_var_para_3_mod_s_7_Object = MibTableColumn
modul_var_para_3_mod_s_7 = _Modul_var_para_3_mod_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 8, 1, 9),
    _Modul_var_para_3_mod_s_7_Type()
)
modul_var_para_3_mod_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_3_mod_s_7.setStatus("current")
_Modul_var_para_4_mod_s_7_Type = DisplayString
_Modul_var_para_4_mod_s_7_Object = MibTableColumn
modul_var_para_4_mod_s_7 = _Modul_var_para_4_mod_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 8, 1, 10),
    _Modul_var_para_4_mod_s_7_Type()
)
modul_var_para_4_mod_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_4_mod_s_7.setStatus("current")
_Modul_var_para_5_mod_s_7_Type = DisplayString
_Modul_var_para_5_mod_s_7_Object = MibTableColumn
modul_var_para_5_mod_s_7 = _Modul_var_para_5_mod_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 8, 1, 11),
    _Modul_var_para_5_mod_s_7_Type()
)
modul_var_para_5_mod_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_5_mod_s_7.setStatus("current")
_Modul_var_para_6_mod_s_7_Type = DisplayString
_Modul_var_para_6_mod_s_7_Object = MibTableColumn
modul_var_para_6_mod_s_7 = _Modul_var_para_6_mod_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 8, 1, 12),
    _Modul_var_para_6_mod_s_7_Type()
)
modul_var_para_6_mod_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_6_mod_s_7.setStatus("current")
_Modul_var_para_7_mod_s_7_Type = DisplayString
_Modul_var_para_7_mod_s_7_Object = MibTableColumn
modul_var_para_7_mod_s_7 = _Modul_var_para_7_mod_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 8, 1, 13),
    _Modul_var_para_7_mod_s_7_Type()
)
modul_var_para_7_mod_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_7_mod_s_7.setStatus("current")
_Modul_var_para_8_mod_s_7_Type = DisplayString
_Modul_var_para_8_mod_s_7_Object = MibTableColumn
modul_var_para_8_mod_s_7 = _Modul_var_para_8_mod_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 8, 1, 14),
    _Modul_var_para_8_mod_s_7_Type()
)
modul_var_para_8_mod_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_8_mod_s_7.setStatus("current")
_Modul_var_para_9_mod_s_7_Type = DisplayString
_Modul_var_para_9_mod_s_7_Object = MibTableColumn
modul_var_para_9_mod_s_7 = _Modul_var_para_9_mod_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 8, 1, 15),
    _Modul_var_para_9_mod_s_7_Type()
)
modul_var_para_9_mod_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_9_mod_s_7.setStatus("current")
_Modul_var_para_10_mod_s_7_Type = DisplayString
_Modul_var_para_10_mod_s_7_Object = MibTableColumn
modul_var_para_10_mod_s_7 = _Modul_var_para_10_mod_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 8, 1, 16),
    _Modul_var_para_10_mod_s_7_Type()
)
modul_var_para_10_mod_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_10_mod_s_7.setStatus("current")
_Modul_var_para_11_mod_s_7_Type = DisplayString
_Modul_var_para_11_mod_s_7_Object = MibTableColumn
modul_var_para_11_mod_s_7 = _Modul_var_para_11_mod_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 8, 1, 17),
    _Modul_var_para_11_mod_s_7_Type()
)
modul_var_para_11_mod_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_11_mod_s_7.setStatus("current")
_Modul_var_para_12_mod_s_7_Type = DisplayString
_Modul_var_para_12_mod_s_7_Object = MibTableColumn
modul_var_para_12_mod_s_7 = _Modul_var_para_12_mod_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 8, 1, 18),
    _Modul_var_para_12_mod_s_7_Type()
)
modul_var_para_12_mod_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_12_mod_s_7.setStatus("current")
_Modul_var_para_13_mod_s_7_Type = DisplayString
_Modul_var_para_13_mod_s_7_Object = MibTableColumn
modul_var_para_13_mod_s_7 = _Modul_var_para_13_mod_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 8, 1, 19),
    _Modul_var_para_13_mod_s_7_Type()
)
modul_var_para_13_mod_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_13_mod_s_7.setStatus("current")
_Modul_var_para_14_mod_s_7_Type = DisplayString
_Modul_var_para_14_mod_s_7_Object = MibTableColumn
modul_var_para_14_mod_s_7 = _Modul_var_para_14_mod_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 8, 1, 20),
    _Modul_var_para_14_mod_s_7_Type()
)
modul_var_para_14_mod_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_14_mod_s_7.setStatus("current")
_Modul_var_para_15_mod_s_7_Type = DisplayString
_Modul_var_para_15_mod_s_7_Object = MibTableColumn
modul_var_para_15_mod_s_7 = _Modul_var_para_15_mod_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 8, 1, 21),
    _Modul_var_para_15_mod_s_7_Type()
)
modul_var_para_15_mod_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_15_mod_s_7.setStatus("current")
_Modul_var_para_16_mod_s_7_Type = DisplayString
_Modul_var_para_16_mod_s_7_Object = MibTableColumn
modul_var_para_16_mod_s_7 = _Modul_var_para_16_mod_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 8, 1, 22),
    _Modul_var_para_16_mod_s_7_Type()
)
modul_var_para_16_mod_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_16_mod_s_7.setStatus("current")
_Modul_var_para_17_mod_s_7_Type = DisplayString
_Modul_var_para_17_mod_s_7_Object = MibTableColumn
modul_var_para_17_mod_s_7 = _Modul_var_para_17_mod_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 8, 1, 23),
    _Modul_var_para_17_mod_s_7_Type()
)
modul_var_para_17_mod_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_17_mod_s_7.setStatus("current")
_Modul_var_para_18_mod_s_7_Type = DisplayString
_Modul_var_para_18_mod_s_7_Object = MibTableColumn
modul_var_para_18_mod_s_7 = _Modul_var_para_18_mod_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 8, 1, 24),
    _Modul_var_para_18_mod_s_7_Type()
)
modul_var_para_18_mod_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_18_mod_s_7.setStatus("current")
_Modul_var_para_19_mod_s_7_Type = DisplayString
_Modul_var_para_19_mod_s_7_Object = MibTableColumn
modul_var_para_19_mod_s_7 = _Modul_var_para_19_mod_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 8, 1, 25),
    _Modul_var_para_19_mod_s_7_Type()
)
modul_var_para_19_mod_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_19_mod_s_7.setStatus("current")
_ModulTable_mod_s_8_Object = MibTable
modulTable_mod_s_8 = _ModulTable_mod_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 9)
)
if mibBuilder.loadTexts:
    modulTable_mod_s_8.setStatus("current")
_ModulEntry_mod_s_8_Object = MibTableRow
modulEntry_mod_s_8 = _ModulEntry_mod_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 9, 1)
)
modulEntry_mod_s_8.setIndexNames(
    (0, "AK-FUNKTECHNIK-MIB", "modulindex-mod-s-8"),
)
if mibBuilder.loadTexts:
    modulEntry_mod_s_8.setStatus("current")
_Modulindex_mod_s_8_Type = DisplayString
_Modulindex_mod_s_8_Object = MibTableColumn
modulindex_mod_s_8 = _Modulindex_mod_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 9, 1, 1),
    _Modulindex_mod_s_8_Type()
)
modulindex_mod_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulindex_mod_s_8.setStatus("current")
_Modul_typ_mod_s_8_Type = DisplayString
_Modul_typ_mod_s_8_Object = MibTableColumn
modul_typ_mod_s_8 = _Modul_typ_mod_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 9, 1, 2),
    _Modul_typ_mod_s_8_Type()
)
modul_typ_mod_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_typ_mod_s_8.setStatus("current")
_Seriennummer_mod_s_8_Type = DisplayString
_Seriennummer_mod_s_8_Object = MibTableColumn
seriennummer_mod_s_8 = _Seriennummer_mod_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 9, 1, 3),
    _Seriennummer_mod_s_8_Type()
)
seriennummer_mod_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seriennummer_mod_s_8.setStatus("current")
_Firmware_version_mod_s_8_Type = DisplayString
_Firmware_version_mod_s_8_Object = MibTableColumn
firmware_version_mod_s_8 = _Firmware_version_mod_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 9, 1, 4),
    _Firmware_version_mod_s_8_Type()
)
firmware_version_mod_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmware_version_mod_s_8.setStatus("current")
_Hardware_zustand_mod_s_8_Type = DisplayString
_Hardware_zustand_mod_s_8_Object = MibTableColumn
hardware_zustand_mod_s_8 = _Hardware_zustand_mod_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 9, 1, 5),
    _Hardware_zustand_mod_s_8_Type()
)
hardware_zustand_mod_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardware_zustand_mod_s_8.setStatus("current")
_Betriebs_status_mod_s_8_Type = DisplayString
_Betriebs_status_mod_s_8_Object = MibTableColumn
betriebs_status_mod_s_8 = _Betriebs_status_mod_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 9, 1, 6),
    _Betriebs_status_mod_s_8_Type()
)
betriebs_status_mod_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    betriebs_status_mod_s_8.setStatus("current")
_Modul_var_para_1_mod_s_8_Type = DisplayString
_Modul_var_para_1_mod_s_8_Object = MibTableColumn
modul_var_para_1_mod_s_8 = _Modul_var_para_1_mod_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 9, 1, 7),
    _Modul_var_para_1_mod_s_8_Type()
)
modul_var_para_1_mod_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_1_mod_s_8.setStatus("current")
_Modul_var_para_2_mod_s_8_Type = DisplayString
_Modul_var_para_2_mod_s_8_Object = MibTableColumn
modul_var_para_2_mod_s_8 = _Modul_var_para_2_mod_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 9, 1, 8),
    _Modul_var_para_2_mod_s_8_Type()
)
modul_var_para_2_mod_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_2_mod_s_8.setStatus("current")
_Modul_var_para_3_mod_s_8_Type = DisplayString
_Modul_var_para_3_mod_s_8_Object = MibTableColumn
modul_var_para_3_mod_s_8 = _Modul_var_para_3_mod_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 9, 1, 9),
    _Modul_var_para_3_mod_s_8_Type()
)
modul_var_para_3_mod_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_3_mod_s_8.setStatus("current")
_Modul_var_para_4_mod_s_8_Type = DisplayString
_Modul_var_para_4_mod_s_8_Object = MibTableColumn
modul_var_para_4_mod_s_8 = _Modul_var_para_4_mod_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 9, 1, 10),
    _Modul_var_para_4_mod_s_8_Type()
)
modul_var_para_4_mod_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_4_mod_s_8.setStatus("current")
_Modul_var_para_5_mod_s_8_Type = DisplayString
_Modul_var_para_5_mod_s_8_Object = MibTableColumn
modul_var_para_5_mod_s_8 = _Modul_var_para_5_mod_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 9, 1, 11),
    _Modul_var_para_5_mod_s_8_Type()
)
modul_var_para_5_mod_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_5_mod_s_8.setStatus("current")
_Modul_var_para_6_mod_s_8_Type = DisplayString
_Modul_var_para_6_mod_s_8_Object = MibTableColumn
modul_var_para_6_mod_s_8 = _Modul_var_para_6_mod_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 9, 1, 12),
    _Modul_var_para_6_mod_s_8_Type()
)
modul_var_para_6_mod_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_6_mod_s_8.setStatus("current")
_Modul_var_para_7_mod_s_8_Type = DisplayString
_Modul_var_para_7_mod_s_8_Object = MibTableColumn
modul_var_para_7_mod_s_8 = _Modul_var_para_7_mod_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 9, 1, 13),
    _Modul_var_para_7_mod_s_8_Type()
)
modul_var_para_7_mod_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_7_mod_s_8.setStatus("current")
_Modul_var_para_8_mod_s_8_Type = DisplayString
_Modul_var_para_8_mod_s_8_Object = MibTableColumn
modul_var_para_8_mod_s_8 = _Modul_var_para_8_mod_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 9, 1, 14),
    _Modul_var_para_8_mod_s_8_Type()
)
modul_var_para_8_mod_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_8_mod_s_8.setStatus("current")
_Modul_var_para_9_mod_s_8_Type = DisplayString
_Modul_var_para_9_mod_s_8_Object = MibTableColumn
modul_var_para_9_mod_s_8 = _Modul_var_para_9_mod_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 9, 1, 15),
    _Modul_var_para_9_mod_s_8_Type()
)
modul_var_para_9_mod_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_9_mod_s_8.setStatus("current")
_Modul_var_para_10_mod_s_8_Type = DisplayString
_Modul_var_para_10_mod_s_8_Object = MibTableColumn
modul_var_para_10_mod_s_8 = _Modul_var_para_10_mod_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 9, 1, 16),
    _Modul_var_para_10_mod_s_8_Type()
)
modul_var_para_10_mod_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_10_mod_s_8.setStatus("current")
_Modul_var_para_11_mod_s_8_Type = DisplayString
_Modul_var_para_11_mod_s_8_Object = MibTableColumn
modul_var_para_11_mod_s_8 = _Modul_var_para_11_mod_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 9, 1, 17),
    _Modul_var_para_11_mod_s_8_Type()
)
modul_var_para_11_mod_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_11_mod_s_8.setStatus("current")
_Modul_var_para_12_mod_s_8_Type = DisplayString
_Modul_var_para_12_mod_s_8_Object = MibTableColumn
modul_var_para_12_mod_s_8 = _Modul_var_para_12_mod_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 9, 1, 18),
    _Modul_var_para_12_mod_s_8_Type()
)
modul_var_para_12_mod_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_12_mod_s_8.setStatus("current")
_Modul_var_para_13_mod_s_8_Type = DisplayString
_Modul_var_para_13_mod_s_8_Object = MibTableColumn
modul_var_para_13_mod_s_8 = _Modul_var_para_13_mod_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 9, 1, 19),
    _Modul_var_para_13_mod_s_8_Type()
)
modul_var_para_13_mod_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_13_mod_s_8.setStatus("current")
_Modul_var_para_14_mod_s_8_Type = DisplayString
_Modul_var_para_14_mod_s_8_Object = MibTableColumn
modul_var_para_14_mod_s_8 = _Modul_var_para_14_mod_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 9, 1, 20),
    _Modul_var_para_14_mod_s_8_Type()
)
modul_var_para_14_mod_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_14_mod_s_8.setStatus("current")
_Modul_var_para_15_mod_s_8_Type = DisplayString
_Modul_var_para_15_mod_s_8_Object = MibTableColumn
modul_var_para_15_mod_s_8 = _Modul_var_para_15_mod_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 9, 1, 21),
    _Modul_var_para_15_mod_s_8_Type()
)
modul_var_para_15_mod_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_15_mod_s_8.setStatus("current")
_Modul_var_para_16_mod_s_8_Type = DisplayString
_Modul_var_para_16_mod_s_8_Object = MibTableColumn
modul_var_para_16_mod_s_8 = _Modul_var_para_16_mod_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 9, 1, 22),
    _Modul_var_para_16_mod_s_8_Type()
)
modul_var_para_16_mod_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_16_mod_s_8.setStatus("current")
_Modul_var_para_17_mod_s_8_Type = DisplayString
_Modul_var_para_17_mod_s_8_Object = MibTableColumn
modul_var_para_17_mod_s_8 = _Modul_var_para_17_mod_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 9, 1, 23),
    _Modul_var_para_17_mod_s_8_Type()
)
modul_var_para_17_mod_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_17_mod_s_8.setStatus("current")
_Modul_var_para_18_mod_s_8_Type = DisplayString
_Modul_var_para_18_mod_s_8_Object = MibTableColumn
modul_var_para_18_mod_s_8 = _Modul_var_para_18_mod_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 9, 1, 24),
    _Modul_var_para_18_mod_s_8_Type()
)
modul_var_para_18_mod_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_18_mod_s_8.setStatus("current")
_Modul_var_para_19_mod_s_8_Type = DisplayString
_Modul_var_para_19_mod_s_8_Object = MibTableColumn
modul_var_para_19_mod_s_8 = _Modul_var_para_19_mod_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 9, 1, 25),
    _Modul_var_para_19_mod_s_8_Type()
)
modul_var_para_19_mod_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_19_mod_s_8.setStatus("current")
_ModulTable_mod_s_9_Object = MibTable
modulTable_mod_s_9 = _ModulTable_mod_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 10)
)
if mibBuilder.loadTexts:
    modulTable_mod_s_9.setStatus("current")
_ModulEntry_mod_s_9_Object = MibTableRow
modulEntry_mod_s_9 = _ModulEntry_mod_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 10, 1)
)
modulEntry_mod_s_9.setIndexNames(
    (0, "AK-FUNKTECHNIK-MIB", "modulindex-mod-s-9"),
)
if mibBuilder.loadTexts:
    modulEntry_mod_s_9.setStatus("current")
_Modulindex_mod_s_9_Type = DisplayString
_Modulindex_mod_s_9_Object = MibTableColumn
modulindex_mod_s_9 = _Modulindex_mod_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 10, 1, 1),
    _Modulindex_mod_s_9_Type()
)
modulindex_mod_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulindex_mod_s_9.setStatus("current")
_Modul_typ_mod_s_9_Type = DisplayString
_Modul_typ_mod_s_9_Object = MibTableColumn
modul_typ_mod_s_9 = _Modul_typ_mod_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 10, 1, 2),
    _Modul_typ_mod_s_9_Type()
)
modul_typ_mod_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_typ_mod_s_9.setStatus("current")
_Seriennummer_mod_s_9_Type = DisplayString
_Seriennummer_mod_s_9_Object = MibTableColumn
seriennummer_mod_s_9 = _Seriennummer_mod_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 10, 1, 3),
    _Seriennummer_mod_s_9_Type()
)
seriennummer_mod_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seriennummer_mod_s_9.setStatus("current")
_Firmware_version_mod_s_9_Type = DisplayString
_Firmware_version_mod_s_9_Object = MibTableColumn
firmware_version_mod_s_9 = _Firmware_version_mod_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 10, 1, 4),
    _Firmware_version_mod_s_9_Type()
)
firmware_version_mod_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmware_version_mod_s_9.setStatus("current")
_Hardware_zustand_mod_s_9_Type = DisplayString
_Hardware_zustand_mod_s_9_Object = MibTableColumn
hardware_zustand_mod_s_9 = _Hardware_zustand_mod_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 10, 1, 5),
    _Hardware_zustand_mod_s_9_Type()
)
hardware_zustand_mod_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardware_zustand_mod_s_9.setStatus("current")
_Betriebs_status_mod_s_9_Type = DisplayString
_Betriebs_status_mod_s_9_Object = MibTableColumn
betriebs_status_mod_s_9 = _Betriebs_status_mod_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 10, 1, 6),
    _Betriebs_status_mod_s_9_Type()
)
betriebs_status_mod_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    betriebs_status_mod_s_9.setStatus("current")
_Modul_var_para_1_mod_s_9_Type = DisplayString
_Modul_var_para_1_mod_s_9_Object = MibTableColumn
modul_var_para_1_mod_s_9 = _Modul_var_para_1_mod_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 10, 1, 7),
    _Modul_var_para_1_mod_s_9_Type()
)
modul_var_para_1_mod_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_1_mod_s_9.setStatus("current")
_Modul_var_para_2_mod_s_9_Type = DisplayString
_Modul_var_para_2_mod_s_9_Object = MibTableColumn
modul_var_para_2_mod_s_9 = _Modul_var_para_2_mod_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 10, 1, 8),
    _Modul_var_para_2_mod_s_9_Type()
)
modul_var_para_2_mod_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_2_mod_s_9.setStatus("current")
_Modul_var_para_3_mod_s_9_Type = DisplayString
_Modul_var_para_3_mod_s_9_Object = MibTableColumn
modul_var_para_3_mod_s_9 = _Modul_var_para_3_mod_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 10, 1, 9),
    _Modul_var_para_3_mod_s_9_Type()
)
modul_var_para_3_mod_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_3_mod_s_9.setStatus("current")
_Modul_var_para_4_mod_s_9_Type = DisplayString
_Modul_var_para_4_mod_s_9_Object = MibTableColumn
modul_var_para_4_mod_s_9 = _Modul_var_para_4_mod_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 10, 1, 10),
    _Modul_var_para_4_mod_s_9_Type()
)
modul_var_para_4_mod_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_4_mod_s_9.setStatus("current")
_Modul_var_para_5_mod_s_9_Type = DisplayString
_Modul_var_para_5_mod_s_9_Object = MibTableColumn
modul_var_para_5_mod_s_9 = _Modul_var_para_5_mod_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 10, 1, 11),
    _Modul_var_para_5_mod_s_9_Type()
)
modul_var_para_5_mod_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_5_mod_s_9.setStatus("current")
_Modul_var_para_6_mod_s_9_Type = DisplayString
_Modul_var_para_6_mod_s_9_Object = MibTableColumn
modul_var_para_6_mod_s_9 = _Modul_var_para_6_mod_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 10, 1, 12),
    _Modul_var_para_6_mod_s_9_Type()
)
modul_var_para_6_mod_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_6_mod_s_9.setStatus("current")
_Modul_var_para_7_mod_s_9_Type = DisplayString
_Modul_var_para_7_mod_s_9_Object = MibTableColumn
modul_var_para_7_mod_s_9 = _Modul_var_para_7_mod_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 10, 1, 13),
    _Modul_var_para_7_mod_s_9_Type()
)
modul_var_para_7_mod_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_7_mod_s_9.setStatus("current")
_Modul_var_para_8_mod_s_9_Type = DisplayString
_Modul_var_para_8_mod_s_9_Object = MibTableColumn
modul_var_para_8_mod_s_9 = _Modul_var_para_8_mod_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 10, 1, 14),
    _Modul_var_para_8_mod_s_9_Type()
)
modul_var_para_8_mod_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_8_mod_s_9.setStatus("current")
_Modul_var_para_9_mod_s_9_Type = DisplayString
_Modul_var_para_9_mod_s_9_Object = MibTableColumn
modul_var_para_9_mod_s_9 = _Modul_var_para_9_mod_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 10, 1, 15),
    _Modul_var_para_9_mod_s_9_Type()
)
modul_var_para_9_mod_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_9_mod_s_9.setStatus("current")
_Modul_var_para_10_mod_s_9_Type = DisplayString
_Modul_var_para_10_mod_s_9_Object = MibTableColumn
modul_var_para_10_mod_s_9 = _Modul_var_para_10_mod_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 10, 1, 16),
    _Modul_var_para_10_mod_s_9_Type()
)
modul_var_para_10_mod_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_10_mod_s_9.setStatus("current")
_Modul_var_para_11_mod_s_9_Type = DisplayString
_Modul_var_para_11_mod_s_9_Object = MibTableColumn
modul_var_para_11_mod_s_9 = _Modul_var_para_11_mod_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 10, 1, 17),
    _Modul_var_para_11_mod_s_9_Type()
)
modul_var_para_11_mod_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_11_mod_s_9.setStatus("current")
_Modul_var_para_12_mod_s_9_Type = DisplayString
_Modul_var_para_12_mod_s_9_Object = MibTableColumn
modul_var_para_12_mod_s_9 = _Modul_var_para_12_mod_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 10, 1, 18),
    _Modul_var_para_12_mod_s_9_Type()
)
modul_var_para_12_mod_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_12_mod_s_9.setStatus("current")
_Modul_var_para_13_mod_s_9_Type = DisplayString
_Modul_var_para_13_mod_s_9_Object = MibTableColumn
modul_var_para_13_mod_s_9 = _Modul_var_para_13_mod_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 10, 1, 19),
    _Modul_var_para_13_mod_s_9_Type()
)
modul_var_para_13_mod_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_13_mod_s_9.setStatus("current")
_Modul_var_para_14_mod_s_9_Type = DisplayString
_Modul_var_para_14_mod_s_9_Object = MibTableColumn
modul_var_para_14_mod_s_9 = _Modul_var_para_14_mod_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 10, 1, 20),
    _Modul_var_para_14_mod_s_9_Type()
)
modul_var_para_14_mod_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_14_mod_s_9.setStatus("current")
_Modul_var_para_15_mod_s_9_Type = DisplayString
_Modul_var_para_15_mod_s_9_Object = MibTableColumn
modul_var_para_15_mod_s_9 = _Modul_var_para_15_mod_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 10, 1, 21),
    _Modul_var_para_15_mod_s_9_Type()
)
modul_var_para_15_mod_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_15_mod_s_9.setStatus("current")
_Modul_var_para_16_mod_s_9_Type = DisplayString
_Modul_var_para_16_mod_s_9_Object = MibTableColumn
modul_var_para_16_mod_s_9 = _Modul_var_para_16_mod_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 10, 1, 22),
    _Modul_var_para_16_mod_s_9_Type()
)
modul_var_para_16_mod_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_16_mod_s_9.setStatus("current")
_Modul_var_para_17_mod_s_9_Type = DisplayString
_Modul_var_para_17_mod_s_9_Object = MibTableColumn
modul_var_para_17_mod_s_9 = _Modul_var_para_17_mod_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 10, 1, 23),
    _Modul_var_para_17_mod_s_9_Type()
)
modul_var_para_17_mod_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_17_mod_s_9.setStatus("current")
_Modul_var_para_18_mod_s_9_Type = DisplayString
_Modul_var_para_18_mod_s_9_Object = MibTableColumn
modul_var_para_18_mod_s_9 = _Modul_var_para_18_mod_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 10, 1, 24),
    _Modul_var_para_18_mod_s_9_Type()
)
modul_var_para_18_mod_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_18_mod_s_9.setStatus("current")
_Modul_var_para_19_mod_s_9_Type = DisplayString
_Modul_var_para_19_mod_s_9_Object = MibTableColumn
modul_var_para_19_mod_s_9 = _Modul_var_para_19_mod_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 10, 1, 25),
    _Modul_var_para_19_mod_s_9_Type()
)
modul_var_para_19_mod_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_19_mod_s_9.setStatus("current")
_ModulTable_mod_s_10_Object = MibTable
modulTable_mod_s_10 = _ModulTable_mod_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 11)
)
if mibBuilder.loadTexts:
    modulTable_mod_s_10.setStatus("current")
_ModulEntry_mod_s_10_Object = MibTableRow
modulEntry_mod_s_10 = _ModulEntry_mod_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 11, 1)
)
modulEntry_mod_s_10.setIndexNames(
    (0, "AK-FUNKTECHNIK-MIB", "modulindex-mod-s-10"),
)
if mibBuilder.loadTexts:
    modulEntry_mod_s_10.setStatus("current")
_Modulindex_mod_s_10_Type = DisplayString
_Modulindex_mod_s_10_Object = MibTableColumn
modulindex_mod_s_10 = _Modulindex_mod_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 11, 1, 1),
    _Modulindex_mod_s_10_Type()
)
modulindex_mod_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulindex_mod_s_10.setStatus("current")
_Modul_typ_mod_s_10_Type = DisplayString
_Modul_typ_mod_s_10_Object = MibTableColumn
modul_typ_mod_s_10 = _Modul_typ_mod_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 11, 1, 2),
    _Modul_typ_mod_s_10_Type()
)
modul_typ_mod_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_typ_mod_s_10.setStatus("current")
_Seriennummer_mod_s_10_Type = DisplayString
_Seriennummer_mod_s_10_Object = MibTableColumn
seriennummer_mod_s_10 = _Seriennummer_mod_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 11, 1, 3),
    _Seriennummer_mod_s_10_Type()
)
seriennummer_mod_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seriennummer_mod_s_10.setStatus("current")
_Firmware_version_mod_s_10_Type = DisplayString
_Firmware_version_mod_s_10_Object = MibTableColumn
firmware_version_mod_s_10 = _Firmware_version_mod_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 11, 1, 4),
    _Firmware_version_mod_s_10_Type()
)
firmware_version_mod_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmware_version_mod_s_10.setStatus("current")
_Hardware_zustand_mod_s_10_Type = DisplayString
_Hardware_zustand_mod_s_10_Object = MibTableColumn
hardware_zustand_mod_s_10 = _Hardware_zustand_mod_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 11, 1, 5),
    _Hardware_zustand_mod_s_10_Type()
)
hardware_zustand_mod_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardware_zustand_mod_s_10.setStatus("current")
_Betriebs_status_mod_s_10_Type = DisplayString
_Betriebs_status_mod_s_10_Object = MibTableColumn
betriebs_status_mod_s_10 = _Betriebs_status_mod_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 11, 1, 6),
    _Betriebs_status_mod_s_10_Type()
)
betriebs_status_mod_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    betriebs_status_mod_s_10.setStatus("current")
_Modul_var_para_1_mod_s_10_Type = DisplayString
_Modul_var_para_1_mod_s_10_Object = MibTableColumn
modul_var_para_1_mod_s_10 = _Modul_var_para_1_mod_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 11, 1, 7),
    _Modul_var_para_1_mod_s_10_Type()
)
modul_var_para_1_mod_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_1_mod_s_10.setStatus("current")
_Modul_var_para_2_mod_s_10_Type = DisplayString
_Modul_var_para_2_mod_s_10_Object = MibTableColumn
modul_var_para_2_mod_s_10 = _Modul_var_para_2_mod_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 11, 1, 8),
    _Modul_var_para_2_mod_s_10_Type()
)
modul_var_para_2_mod_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_2_mod_s_10.setStatus("current")
_Modul_var_para_3_mod_s_10_Type = DisplayString
_Modul_var_para_3_mod_s_10_Object = MibTableColumn
modul_var_para_3_mod_s_10 = _Modul_var_para_3_mod_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 11, 1, 9),
    _Modul_var_para_3_mod_s_10_Type()
)
modul_var_para_3_mod_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_3_mod_s_10.setStatus("current")
_Modul_var_para_4_mod_s_10_Type = DisplayString
_Modul_var_para_4_mod_s_10_Object = MibTableColumn
modul_var_para_4_mod_s_10 = _Modul_var_para_4_mod_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 11, 1, 10),
    _Modul_var_para_4_mod_s_10_Type()
)
modul_var_para_4_mod_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_4_mod_s_10.setStatus("current")
_Modul_var_para_5_mod_s_10_Type = DisplayString
_Modul_var_para_5_mod_s_10_Object = MibTableColumn
modul_var_para_5_mod_s_10 = _Modul_var_para_5_mod_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 11, 1, 11),
    _Modul_var_para_5_mod_s_10_Type()
)
modul_var_para_5_mod_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_5_mod_s_10.setStatus("current")
_Modul_var_para_6_mod_s_10_Type = DisplayString
_Modul_var_para_6_mod_s_10_Object = MibTableColumn
modul_var_para_6_mod_s_10 = _Modul_var_para_6_mod_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 11, 1, 12),
    _Modul_var_para_6_mod_s_10_Type()
)
modul_var_para_6_mod_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_6_mod_s_10.setStatus("current")
_Modul_var_para_7_mod_s_10_Type = DisplayString
_Modul_var_para_7_mod_s_10_Object = MibTableColumn
modul_var_para_7_mod_s_10 = _Modul_var_para_7_mod_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 11, 1, 13),
    _Modul_var_para_7_mod_s_10_Type()
)
modul_var_para_7_mod_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_7_mod_s_10.setStatus("current")
_Modul_var_para_8_mod_s_10_Type = DisplayString
_Modul_var_para_8_mod_s_10_Object = MibTableColumn
modul_var_para_8_mod_s_10 = _Modul_var_para_8_mod_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 11, 1, 14),
    _Modul_var_para_8_mod_s_10_Type()
)
modul_var_para_8_mod_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_8_mod_s_10.setStatus("current")
_Modul_var_para_9_mod_s_10_Type = DisplayString
_Modul_var_para_9_mod_s_10_Object = MibTableColumn
modul_var_para_9_mod_s_10 = _Modul_var_para_9_mod_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 11, 1, 15),
    _Modul_var_para_9_mod_s_10_Type()
)
modul_var_para_9_mod_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_9_mod_s_10.setStatus("current")
_Modul_var_para_10_mod_s_10_Type = DisplayString
_Modul_var_para_10_mod_s_10_Object = MibTableColumn
modul_var_para_10_mod_s_10 = _Modul_var_para_10_mod_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 11, 1, 16),
    _Modul_var_para_10_mod_s_10_Type()
)
modul_var_para_10_mod_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_10_mod_s_10.setStatus("current")
_Modul_var_para_11_mod_s_10_Type = DisplayString
_Modul_var_para_11_mod_s_10_Object = MibTableColumn
modul_var_para_11_mod_s_10 = _Modul_var_para_11_mod_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 11, 1, 17),
    _Modul_var_para_11_mod_s_10_Type()
)
modul_var_para_11_mod_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_11_mod_s_10.setStatus("current")
_Modul_var_para_12_mod_s_10_Type = DisplayString
_Modul_var_para_12_mod_s_10_Object = MibTableColumn
modul_var_para_12_mod_s_10 = _Modul_var_para_12_mod_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 11, 1, 18),
    _Modul_var_para_12_mod_s_10_Type()
)
modul_var_para_12_mod_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_12_mod_s_10.setStatus("current")
_Modul_var_para_13_mod_s_10_Type = DisplayString
_Modul_var_para_13_mod_s_10_Object = MibTableColumn
modul_var_para_13_mod_s_10 = _Modul_var_para_13_mod_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 11, 1, 19),
    _Modul_var_para_13_mod_s_10_Type()
)
modul_var_para_13_mod_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_13_mod_s_10.setStatus("current")
_Modul_var_para_14_mod_s_10_Type = DisplayString
_Modul_var_para_14_mod_s_10_Object = MibTableColumn
modul_var_para_14_mod_s_10 = _Modul_var_para_14_mod_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 11, 1, 20),
    _Modul_var_para_14_mod_s_10_Type()
)
modul_var_para_14_mod_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_14_mod_s_10.setStatus("current")
_Modul_var_para_15_mod_s_10_Type = DisplayString
_Modul_var_para_15_mod_s_10_Object = MibTableColumn
modul_var_para_15_mod_s_10 = _Modul_var_para_15_mod_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 11, 1, 21),
    _Modul_var_para_15_mod_s_10_Type()
)
modul_var_para_15_mod_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_15_mod_s_10.setStatus("current")
_Modul_var_para_16_mod_s_10_Type = DisplayString
_Modul_var_para_16_mod_s_10_Object = MibTableColumn
modul_var_para_16_mod_s_10 = _Modul_var_para_16_mod_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 11, 1, 22),
    _Modul_var_para_16_mod_s_10_Type()
)
modul_var_para_16_mod_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_16_mod_s_10.setStatus("current")
_Modul_var_para_17_mod_s_10_Type = DisplayString
_Modul_var_para_17_mod_s_10_Object = MibTableColumn
modul_var_para_17_mod_s_10 = _Modul_var_para_17_mod_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 11, 1, 23),
    _Modul_var_para_17_mod_s_10_Type()
)
modul_var_para_17_mod_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_17_mod_s_10.setStatus("current")
_Modul_var_para_18_mod_s_10_Type = DisplayString
_Modul_var_para_18_mod_s_10_Object = MibTableColumn
modul_var_para_18_mod_s_10 = _Modul_var_para_18_mod_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 11, 1, 24),
    _Modul_var_para_18_mod_s_10_Type()
)
modul_var_para_18_mod_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_18_mod_s_10.setStatus("current")
_Modul_var_para_19_mod_s_10_Type = DisplayString
_Modul_var_para_19_mod_s_10_Object = MibTableColumn
modul_var_para_19_mod_s_10 = _Modul_var_para_19_mod_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 11, 1, 25),
    _Modul_var_para_19_mod_s_10_Type()
)
modul_var_para_19_mod_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_19_mod_s_10.setStatus("current")
_ModulTable_mod_s_11_Object = MibTable
modulTable_mod_s_11 = _ModulTable_mod_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 12)
)
if mibBuilder.loadTexts:
    modulTable_mod_s_11.setStatus("current")
_ModulEntry_mod_s_11_Object = MibTableRow
modulEntry_mod_s_11 = _ModulEntry_mod_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 12, 1)
)
modulEntry_mod_s_11.setIndexNames(
    (0, "AK-FUNKTECHNIK-MIB", "modulindex-mod-s-11"),
)
if mibBuilder.loadTexts:
    modulEntry_mod_s_11.setStatus("current")
_Modulindex_mod_s_11_Type = DisplayString
_Modulindex_mod_s_11_Object = MibTableColumn
modulindex_mod_s_11 = _Modulindex_mod_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 12, 1, 1),
    _Modulindex_mod_s_11_Type()
)
modulindex_mod_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulindex_mod_s_11.setStatus("current")
_Modul_typ_mod_s_11_Type = DisplayString
_Modul_typ_mod_s_11_Object = MibTableColumn
modul_typ_mod_s_11 = _Modul_typ_mod_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 12, 1, 2),
    _Modul_typ_mod_s_11_Type()
)
modul_typ_mod_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_typ_mod_s_11.setStatus("current")
_Seriennummer_mod_s_11_Type = DisplayString
_Seriennummer_mod_s_11_Object = MibTableColumn
seriennummer_mod_s_11 = _Seriennummer_mod_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 12, 1, 3),
    _Seriennummer_mod_s_11_Type()
)
seriennummer_mod_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    seriennummer_mod_s_11.setStatus("current")
_Firmware_version_mod_s_11_Type = DisplayString
_Firmware_version_mod_s_11_Object = MibTableColumn
firmware_version_mod_s_11 = _Firmware_version_mod_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 12, 1, 4),
    _Firmware_version_mod_s_11_Type()
)
firmware_version_mod_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmware_version_mod_s_11.setStatus("current")
_Hardware_zustand_mod_s_11_Type = DisplayString
_Hardware_zustand_mod_s_11_Object = MibTableColumn
hardware_zustand_mod_s_11 = _Hardware_zustand_mod_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 12, 1, 5),
    _Hardware_zustand_mod_s_11_Type()
)
hardware_zustand_mod_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardware_zustand_mod_s_11.setStatus("current")
_Betriebs_status_mod_s_11_Type = DisplayString
_Betriebs_status_mod_s_11_Object = MibTableColumn
betriebs_status_mod_s_11 = _Betriebs_status_mod_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 12, 1, 6),
    _Betriebs_status_mod_s_11_Type()
)
betriebs_status_mod_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    betriebs_status_mod_s_11.setStatus("current")
_Modul_var_para_1_mod_s_11_Type = DisplayString
_Modul_var_para_1_mod_s_11_Object = MibTableColumn
modul_var_para_1_mod_s_11 = _Modul_var_para_1_mod_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 12, 1, 7),
    _Modul_var_para_1_mod_s_11_Type()
)
modul_var_para_1_mod_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_1_mod_s_11.setStatus("current")
_Modul_var_para_2_mod_s_11_Type = DisplayString
_Modul_var_para_2_mod_s_11_Object = MibTableColumn
modul_var_para_2_mod_s_11 = _Modul_var_para_2_mod_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 12, 1, 8),
    _Modul_var_para_2_mod_s_11_Type()
)
modul_var_para_2_mod_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_2_mod_s_11.setStatus("current")
_Modul_var_para_3_mod_s_11_Type = DisplayString
_Modul_var_para_3_mod_s_11_Object = MibTableColumn
modul_var_para_3_mod_s_11 = _Modul_var_para_3_mod_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 12, 1, 9),
    _Modul_var_para_3_mod_s_11_Type()
)
modul_var_para_3_mod_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_3_mod_s_11.setStatus("current")
_Modul_var_para_4_mod_s_11_Type = DisplayString
_Modul_var_para_4_mod_s_11_Object = MibTableColumn
modul_var_para_4_mod_s_11 = _Modul_var_para_4_mod_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 12, 1, 10),
    _Modul_var_para_4_mod_s_11_Type()
)
modul_var_para_4_mod_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_4_mod_s_11.setStatus("current")
_Modul_var_para_5_mod_s_11_Type = DisplayString
_Modul_var_para_5_mod_s_11_Object = MibTableColumn
modul_var_para_5_mod_s_11 = _Modul_var_para_5_mod_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 12, 1, 11),
    _Modul_var_para_5_mod_s_11_Type()
)
modul_var_para_5_mod_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_5_mod_s_11.setStatus("current")
_Modul_var_para_6_mod_s_11_Type = DisplayString
_Modul_var_para_6_mod_s_11_Object = MibTableColumn
modul_var_para_6_mod_s_11 = _Modul_var_para_6_mod_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 12, 1, 12),
    _Modul_var_para_6_mod_s_11_Type()
)
modul_var_para_6_mod_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_6_mod_s_11.setStatus("current")
_Modul_var_para_7_mod_s_11_Type = DisplayString
_Modul_var_para_7_mod_s_11_Object = MibTableColumn
modul_var_para_7_mod_s_11 = _Modul_var_para_7_mod_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 12, 1, 13),
    _Modul_var_para_7_mod_s_11_Type()
)
modul_var_para_7_mod_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_7_mod_s_11.setStatus("current")
_Modul_var_para_8_mod_s_11_Type = DisplayString
_Modul_var_para_8_mod_s_11_Object = MibTableColumn
modul_var_para_8_mod_s_11 = _Modul_var_para_8_mod_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 12, 1, 14),
    _Modul_var_para_8_mod_s_11_Type()
)
modul_var_para_8_mod_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_8_mod_s_11.setStatus("current")
_Modul_var_para_9_mod_s_11_Type = DisplayString
_Modul_var_para_9_mod_s_11_Object = MibTableColumn
modul_var_para_9_mod_s_11 = _Modul_var_para_9_mod_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 12, 1, 15),
    _Modul_var_para_9_mod_s_11_Type()
)
modul_var_para_9_mod_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_9_mod_s_11.setStatus("current")
_Modul_var_para_10_mod_s_11_Type = DisplayString
_Modul_var_para_10_mod_s_11_Object = MibTableColumn
modul_var_para_10_mod_s_11 = _Modul_var_para_10_mod_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 12, 1, 16),
    _Modul_var_para_10_mod_s_11_Type()
)
modul_var_para_10_mod_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_10_mod_s_11.setStatus("current")
_Modul_var_para_11_mod_s_11_Type = DisplayString
_Modul_var_para_11_mod_s_11_Object = MibTableColumn
modul_var_para_11_mod_s_11 = _Modul_var_para_11_mod_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 12, 1, 17),
    _Modul_var_para_11_mod_s_11_Type()
)
modul_var_para_11_mod_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_11_mod_s_11.setStatus("current")
_Modul_var_para_12_mod_s_11_Type = DisplayString
_Modul_var_para_12_mod_s_11_Object = MibTableColumn
modul_var_para_12_mod_s_11 = _Modul_var_para_12_mod_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 12, 1, 18),
    _Modul_var_para_12_mod_s_11_Type()
)
modul_var_para_12_mod_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_12_mod_s_11.setStatus("current")
_Modul_var_para_13_mod_s_11_Type = DisplayString
_Modul_var_para_13_mod_s_11_Object = MibTableColumn
modul_var_para_13_mod_s_11 = _Modul_var_para_13_mod_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 12, 1, 19),
    _Modul_var_para_13_mod_s_11_Type()
)
modul_var_para_13_mod_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_13_mod_s_11.setStatus("current")
_Modul_var_para_14_mod_s_11_Type = DisplayString
_Modul_var_para_14_mod_s_11_Object = MibTableColumn
modul_var_para_14_mod_s_11 = _Modul_var_para_14_mod_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 12, 1, 20),
    _Modul_var_para_14_mod_s_11_Type()
)
modul_var_para_14_mod_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_14_mod_s_11.setStatus("current")
_Modul_var_para_15_mod_s_11_Type = DisplayString
_Modul_var_para_15_mod_s_11_Object = MibTableColumn
modul_var_para_15_mod_s_11 = _Modul_var_para_15_mod_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 12, 1, 21),
    _Modul_var_para_15_mod_s_11_Type()
)
modul_var_para_15_mod_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_15_mod_s_11.setStatus("current")
_Modul_var_para_16_mod_s_11_Type = DisplayString
_Modul_var_para_16_mod_s_11_Object = MibTableColumn
modul_var_para_16_mod_s_11 = _Modul_var_para_16_mod_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 12, 1, 22),
    _Modul_var_para_16_mod_s_11_Type()
)
modul_var_para_16_mod_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_16_mod_s_11.setStatus("current")
_Modul_var_para_17_mod_s_11_Type = DisplayString
_Modul_var_para_17_mod_s_11_Object = MibTableColumn
modul_var_para_17_mod_s_11 = _Modul_var_para_17_mod_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 12, 1, 23),
    _Modul_var_para_17_mod_s_11_Type()
)
modul_var_para_17_mod_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_17_mod_s_11.setStatus("current")
_Modul_var_para_18_mod_s_11_Type = DisplayString
_Modul_var_para_18_mod_s_11_Object = MibTableColumn
modul_var_para_18_mod_s_11 = _Modul_var_para_18_mod_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 12, 1, 24),
    _Modul_var_para_18_mod_s_11_Type()
)
modul_var_para_18_mod_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_18_mod_s_11.setStatus("current")
_Modul_var_para_19_mod_s_11_Type = DisplayString
_Modul_var_para_19_mod_s_11_Object = MibTableColumn
modul_var_para_19_mod_s_11 = _Modul_var_para_19_mod_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 1, 5, 2, 12, 1, 25),
    _Modul_var_para_19_mod_s_11_Type()
)
modul_var_para_19_mod_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul_var_para_19_mod_s_11.setStatus("current")
_Ak_mgmt_i_ObjectIdentity = ObjectIdentity
ak_mgmt_i = _Ak_mgmt_i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 2)
)
_Ak_intern_ip_Type = DisplayString
_Ak_intern_ip_Object = MibScalar
ak_intern_ip = _Ak_intern_ip_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 2, 1),
    _Ak_intern_ip_Type()
)
ak_intern_ip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ak_intern_ip.setStatus("current")
_Ak_extern_ip_Type = DisplayString
_Ak_extern_ip_Object = MibScalar
ak_extern_ip = _Ak_extern_ip_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 2, 2),
    _Ak_extern_ip_Type()
)
ak_extern_ip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ak_extern_ip.setStatus("current")
_Ak_intern_subnetmask_ip_Type = DisplayString
_Ak_intern_subnetmask_ip_Object = MibScalar
ak_intern_subnetmask_ip = _Ak_intern_subnetmask_ip_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 2, 3),
    _Ak_intern_subnetmask_ip_Type()
)
ak_intern_subnetmask_ip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ak_intern_subnetmask_ip.setStatus("current")
_Ak_router_ip_Type = DisplayString
_Ak_router_ip_Object = MibScalar
ak_router_ip = _Ak_router_ip_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 2, 4),
    _Ak_router_ip_Type()
)
ak_router_ip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ak_router_ip.setStatus("current")
_Ak_divers_i_ObjectIdentity = ObjectIdentity
ak_divers_i = _Ak_divers_i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 3)
)
_To_be_defined_1_Type = DisplayString
_To_be_defined_1_Object = MibScalar
to_be_defined_1 = _To_be_defined_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 3, 1),
    _To_be_defined_1_Type()
)
to_be_defined_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    to_be_defined_1.setStatus("current")
_To_be_defined_2_Type = DisplayString
_To_be_defined_2_Object = MibScalar
to_be_defined_2 = _To_be_defined_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 3, 2),
    _To_be_defined_2_Type()
)
to_be_defined_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    to_be_defined_2.setStatus("current")
_Ak_traps_i_ObjectIdentity = ObjectIdentity
ak_traps_i = _Ak_traps_i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4)
)
_Ak_master_i_ObjectIdentity = ObjectIdentity
ak_master_i = _Ak_master_i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1)
)
_Ak_slave_1_i_ObjectIdentity = ObjectIdentity
ak_slave_1_i = _Ak_slave_1_i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1)
)
_ModulTable_s_1_Object = MibTable
modulTable_s_1 = _ModulTable_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    modulTable_s_1.setStatus("current")
_ModulEntry_s_1_Object = MibTableRow
modulEntry_s_1 = _ModulEntry_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1)
)
modulEntry_s_1.setIndexNames(
    (0, "AK-FUNKTECHNIK-MIB", "modulIndex-s-1"),
)
if mibBuilder.loadTexts:
    modulEntry_s_1.setStatus("current")
_ModulIndex_s_1_Type = DisplayString
_ModulIndex_s_1_Object = MibTableColumn
modulIndex_s_1 = _ModulIndex_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 1),
    _ModulIndex_s_1_Type()
)
modulIndex_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulIndex_s_1.setStatus("current")
_Geraete_typ_s_1_Type = DisplayString
_Geraete_typ_s_1_Object = MibTableColumn
geraete_typ_s_1 = _Geraete_typ_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 2),
    _Geraete_typ_s_1_Type()
)
geraete_typ_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geraete_typ_s_1.setStatus("current")
_Betriebsstatus_s_1_Type = DisplayString
_Betriebsstatus_s_1_Object = MibTableColumn
betriebsstatus_s_1 = _Betriebsstatus_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 3),
    _Betriebsstatus_s_1_Type()
)
betriebsstatus_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    betriebsstatus_s_1.setStatus("current")
_Senderstatus_s_1_Type = DisplayString
_Senderstatus_s_1_Object = MibTableColumn
senderstatus_s_1 = _Senderstatus_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 4),
    _Senderstatus_s_1_Type()
)
senderstatus_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    senderstatus_s_1.setStatus("current")
_Fehlerstatus_s_1_Type = DisplayString
_Fehlerstatus_s_1_Object = MibTableColumn
fehlerstatus_s_1 = _Fehlerstatus_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 5),
    _Fehlerstatus_s_1_Type()
)
fehlerstatus_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fehlerstatus_s_1.setStatus("current")
_Dem_adapter_zugeordnete_funkgeraetetype_s_1_Type = DisplayString
_Dem_adapter_zugeordnete_funkgeraetetype_s_1_Object = MibTableColumn
dem_adapter_zugeordnete_funkgeraetetype_s_1 = _Dem_adapter_zugeordnete_funkgeraetetype_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 6),
    _Dem_adapter_zugeordnete_funkgeraetetype_s_1_Type()
)
dem_adapter_zugeordnete_funkgeraetetype_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dem_adapter_zugeordnete_funkgeraetetype_s_1.setStatus("current")
_Eingabe_und_anzeigemodul_s_1_Type = DisplayString
_Eingabe_und_anzeigemodul_s_1_Object = MibTableColumn
eingabe_und_anzeigemodul_s_1 = _Eingabe_und_anzeigemodul_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 7),
    _Eingabe_und_anzeigemodul_s_1_Type()
)
eingabe_und_anzeigemodul_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eingabe_und_anzeigemodul_s_1.setStatus("current")
_Mod_bus_verbindung_module_s_1_Type = DisplayString
_Mod_bus_verbindung_module_s_1_Object = MibTableColumn
mod_bus_verbindung_module_s_1 = _Mod_bus_verbindung_module_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 8),
    _Mod_bus_verbindung_module_s_1_Type()
)
mod_bus_verbindung_module_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mod_bus_verbindung_module_s_1.setStatus("current")
_Gemessene_sendeleistung_im_testmode_s_1_Type = DisplayString
_Gemessene_sendeleistung_im_testmode_s_1_Object = MibTableColumn
gemessene_sendeleistung_im_testmode_s_1 = _Gemessene_sendeleistung_im_testmode_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 9),
    _Gemessene_sendeleistung_im_testmode_s_1_Type()
)
gemessene_sendeleistung_im_testmode_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemessene_sendeleistung_im_testmode_s_1.setStatus("current")
_Aktuelle_sendeleistung_s_1_Type = DisplayString
_Aktuelle_sendeleistung_s_1_Object = MibTableColumn
aktuelle_sendeleistung_s_1 = _Aktuelle_sendeleistung_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 10),
    _Aktuelle_sendeleistung_s_1_Type()
)
aktuelle_sendeleistung_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_sendeleistung_s_1.setStatus("current")
_Gemessene_reflexion_im_testmode_s_1_Type = DisplayString
_Gemessene_reflexion_im_testmode_s_1_Object = MibTableColumn
gemessene_reflexion_im_testmode_s_1 = _Gemessene_reflexion_im_testmode_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 11),
    _Gemessene_reflexion_im_testmode_s_1_Type()
)
gemessene_reflexion_im_testmode_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemessene_reflexion_im_testmode_s_1.setStatus("current")
_Aktuelle_reflexion_s_1_Type = DisplayString
_Aktuelle_reflexion_s_1_Object = MibTableColumn
aktuelle_reflexion_s_1 = _Aktuelle_reflexion_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 12),
    _Aktuelle_reflexion_s_1_Type()
)
aktuelle_reflexion_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_reflexion_s_1.setStatus("current")
_Letzte_gemessene_donor_sendeleistung_s_1_Type = DisplayString
_Letzte_gemessene_donor_sendeleistung_s_1_Object = MibTableColumn
letzte_gemessene_donor_sendeleistung_s_1 = _Letzte_gemessene_donor_sendeleistung_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 13),
    _Letzte_gemessene_donor_sendeleistung_s_1_Type()
)
letzte_gemessene_donor_sendeleistung_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    letzte_gemessene_donor_sendeleistung_s_1.setStatus("current")
_Aktuelle_donor_sendeleistung_s_1_Type = DisplayString
_Aktuelle_donor_sendeleistung_s_1_Object = MibTableColumn
aktuelle_donor_sendeleistung_s_1 = _Aktuelle_donor_sendeleistung_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 14),
    _Aktuelle_donor_sendeleistung_s_1_Type()
)
aktuelle_donor_sendeleistung_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_donor_sendeleistung_s_1.setStatus("current")
_Letzte_gemessene_donor_reflexion_s_1_Type = DisplayString
_Letzte_gemessene_donor_reflexion_s_1_Object = MibTableColumn
letzte_gemessene_donor_reflexion_s_1 = _Letzte_gemessene_donor_reflexion_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 15),
    _Letzte_gemessene_donor_reflexion_s_1_Type()
)
letzte_gemessene_donor_reflexion_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    letzte_gemessene_donor_reflexion_s_1.setStatus("current")
_Aktuelle_donor_reflexion_s_1_Type = DisplayString
_Aktuelle_donor_reflexion_s_1_Object = MibTableColumn
aktuelle_donor_reflexion_s_1 = _Aktuelle_donor_reflexion_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 16),
    _Aktuelle_donor_reflexion_s_1_Type()
)
aktuelle_donor_reflexion_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_donor_reflexion_s_1.setStatus("current")
_Anzahl_gemessener_praesenzsignale_im_testmode_s_1_Type = DisplayString
_Anzahl_gemessener_praesenzsignale_im_testmode_s_1_Object = MibTableColumn
anzahl_gemessener_praesenzsignale_im_testmode_s_1 = _Anzahl_gemessener_praesenzsignale_im_testmode_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 18),
    _Anzahl_gemessener_praesenzsignale_im_testmode_s_1_Type()
)
anzahl_gemessener_praesenzsignale_im_testmode_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anzahl_gemessener_praesenzsignale_im_testmode_s_1.setStatus("current")
_Aktuelle_ausgangsspannung_ub_s_1_Type = DisplayString
_Aktuelle_ausgangsspannung_ub_s_1_Object = MibTableColumn
aktuelle_ausgangsspannung_ub_s_1 = _Aktuelle_ausgangsspannung_ub_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 19),
    _Aktuelle_ausgangsspannung_ub_s_1_Type()
)
aktuelle_ausgangsspannung_ub_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_ub_s_1.setStatus("current")
_Aktuelle_ausgangsspannung_u1_s_1_Type = DisplayString
_Aktuelle_ausgangsspannung_u1_s_1_Object = MibTableColumn
aktuelle_ausgangsspannung_u1_s_1 = _Aktuelle_ausgangsspannung_u1_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 20),
    _Aktuelle_ausgangsspannung_u1_s_1_Type()
)
aktuelle_ausgangsspannung_u1_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u1_s_1.setStatus("current")
_Aktuelle_ausgangsspannung_u2_s_1_Type = DisplayString
_Aktuelle_ausgangsspannung_u2_s_1_Object = MibTableColumn
aktuelle_ausgangsspannung_u2_s_1 = _Aktuelle_ausgangsspannung_u2_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 21),
    _Aktuelle_ausgangsspannung_u2_s_1_Type()
)
aktuelle_ausgangsspannung_u2_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u2_s_1.setStatus("current")
_Aktuelle_ausgangsspannung_u3_s_1_Type = DisplayString
_Aktuelle_ausgangsspannung_u3_s_1_Object = MibTableColumn
aktuelle_ausgangsspannung_u3_s_1 = _Aktuelle_ausgangsspannung_u3_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 22),
    _Aktuelle_ausgangsspannung_u3_s_1_Type()
)
aktuelle_ausgangsspannung_u3_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u3_s_1.setStatus("current")
_Aktuelle_ausgangsspannung_u4_s_1_Type = DisplayString
_Aktuelle_ausgangsspannung_u4_s_1_Object = MibTableColumn
aktuelle_ausgangsspannung_u4_s_1 = _Aktuelle_ausgangsspannung_u4_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 23),
    _Aktuelle_ausgangsspannung_u4_s_1_Type()
)
aktuelle_ausgangsspannung_u4_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u4_s_1.setStatus("current")
_Aktuelle_ausgangsspannung_u5_s_1_Type = DisplayString
_Aktuelle_ausgangsspannung_u5_s_1_Object = MibTableColumn
aktuelle_ausgangsspannung_u5_s_1 = _Aktuelle_ausgangsspannung_u5_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 24),
    _Aktuelle_ausgangsspannung_u5_s_1_Type()
)
aktuelle_ausgangsspannung_u5_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u5_s_1.setStatus("current")
_Aktuelle_ausgangsspannung_u6_s_1_Type = DisplayString
_Aktuelle_ausgangsspannung_u6_s_1_Object = MibTableColumn
aktuelle_ausgangsspannung_u6_s_1 = _Aktuelle_ausgangsspannung_u6_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 25),
    _Aktuelle_ausgangsspannung_u6_s_1_Type()
)
aktuelle_ausgangsspannung_u6_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u6_s_1.setStatus("current")
_Aktuelle_ausgangsspannung_u7_s_1_Type = DisplayString
_Aktuelle_ausgangsspannung_u7_s_1_Object = MibTableColumn
aktuelle_ausgangsspannung_u7_s_1 = _Aktuelle_ausgangsspannung_u7_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 26),
    _Aktuelle_ausgangsspannung_u7_s_1_Type()
)
aktuelle_ausgangsspannung_u7_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u7_s_1.setStatus("current")
_Aktuelle_ausgangsspannung_u8_s_1_Type = DisplayString
_Aktuelle_ausgangsspannung_u8_s_1_Object = MibTableColumn
aktuelle_ausgangsspannung_u8_s_1 = _Aktuelle_ausgangsspannung_u8_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 27),
    _Aktuelle_ausgangsspannung_u8_s_1_Type()
)
aktuelle_ausgangsspannung_u8_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u8_s_1.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_1_s_1_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_1_s_1_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_1_s_1 = _Aktuelle_ladespannung_an_akku_kreis_1_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 28),
    _Aktuelle_ladespannung_an_akku_kreis_1_s_1_Type()
)
aktuelle_ladespannung_an_akku_kreis_1_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_1_s_1.setStatus("current")
_Aktuelle_ladespannung_an_akku_Kreis_2_s_1_Type = DisplayString
_Aktuelle_ladespannung_an_akku_Kreis_2_s_1_Object = MibTableColumn
aktuelle_ladespannung_an_akku_Kreis_2_s_1 = _Aktuelle_ladespannung_an_akku_Kreis_2_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 29),
    _Aktuelle_ladespannung_an_akku_Kreis_2_s_1_Type()
)
aktuelle_ladespannung_an_akku_Kreis_2_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_Kreis_2_s_1.setStatus("current")
_Aktuelle_ladespannung_an_akku_Kreis_3_s_1_Type = DisplayString
_Aktuelle_ladespannung_an_akku_Kreis_3_s_1_Object = MibTableColumn
aktuelle_ladespannung_an_akku_Kreis_3_s_1 = _Aktuelle_ladespannung_an_akku_Kreis_3_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 30),
    _Aktuelle_ladespannung_an_akku_Kreis_3_s_1_Type()
)
aktuelle_ladespannung_an_akku_Kreis_3_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_Kreis_3_s_1.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_4_s_1_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_4_s_1_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_4_s_1 = _Aktuelle_ladespannung_an_akku_kreis_4_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 31),
    _Aktuelle_ladespannung_an_akku_kreis_4_s_1_Type()
)
aktuelle_ladespannung_an_akku_kreis_4_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_4_s_1.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_5_s_1_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_5_s_1_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_5_s_1 = _Aktuelle_ladespannung_an_akku_kreis_5_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 32),
    _Aktuelle_ladespannung_an_akku_kreis_5_s_1_Type()
)
aktuelle_ladespannung_an_akku_kreis_5_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_5_s_1.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_6_s_1_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_6_s_1_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_6_s_1 = _Aktuelle_ladespannung_an_akku_kreis_6_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 33),
    _Aktuelle_ladespannung_an_akku_kreis_6_s_1_Type()
)
aktuelle_ladespannung_an_akku_kreis_6_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_6_s_1.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_7_s_1_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_7_s_1_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_7_s_1 = _Aktuelle_ladespannung_an_akku_kreis_7_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 34),
    _Aktuelle_ladespannung_an_akku_kreis_7_s_1_Type()
)
aktuelle_ladespannung_an_akku_kreis_7_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_7_s_1.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_8_s_1_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_8_s_1_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_8_s_1 = _Aktuelle_ladespannung_an_akku_kreis_8_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 35),
    _Aktuelle_ladespannung_an_akku_kreis_8_s_1_Type()
)
aktuelle_ladespannung_an_akku_kreis_8_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_8_s_1.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_1_s_1_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_1_s_1_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_1_s_1 = _Aktuelle_spannung_an_akku_kreis_1_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 36),
    _Aktuelle_spannung_an_akku_kreis_1_s_1_Type()
)
aktuelle_spannung_an_akku_kreis_1_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_1_s_1.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_2_s_1_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_2_s_1_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_2_s_1 = _Aktuelle_spannung_an_akku_kreis_2_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 37),
    _Aktuelle_spannung_an_akku_kreis_2_s_1_Type()
)
aktuelle_spannung_an_akku_kreis_2_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_2_s_1.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_3_s_1_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_3_s_1_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_3_s_1 = _Aktuelle_spannung_an_akku_kreis_3_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 38),
    _Aktuelle_spannung_an_akku_kreis_3_s_1_Type()
)
aktuelle_spannung_an_akku_kreis_3_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_3_s_1.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_4_s_1_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_4_s_1_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_4_s_1 = _Aktuelle_spannung_an_akku_kreis_4_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 39),
    _Aktuelle_spannung_an_akku_kreis_4_s_1_Type()
)
aktuelle_spannung_an_akku_kreis_4_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_4_s_1.setStatus("current")
_Aktuelle_spannung_an_akku_reis_5_s_1_Type = DisplayString
_Aktuelle_spannung_an_akku_reis_5_s_1_Object = MibTableColumn
aktuelle_spannung_an_akku_reis_5_s_1 = _Aktuelle_spannung_an_akku_reis_5_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 40),
    _Aktuelle_spannung_an_akku_reis_5_s_1_Type()
)
aktuelle_spannung_an_akku_reis_5_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_reis_5_s_1.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_6_s_1_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_6_s_1_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_6_s_1 = _Aktuelle_spannung_an_akku_kreis_6_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 41),
    _Aktuelle_spannung_an_akku_kreis_6_s_1_Type()
)
aktuelle_spannung_an_akku_kreis_6_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_6_s_1.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_7_s_1_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_7_s_1_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_7_s_1 = _Aktuelle_spannung_an_akku_kreis_7_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 42),
    _Aktuelle_spannung_an_akku_kreis_7_s_1_Type()
)
aktuelle_spannung_an_akku_kreis_7_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_7_s_1.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_8_s_1_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_8_s_1_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_8_s_1 = _Aktuelle_spannung_an_akku_kreis_8_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 43),
    _Aktuelle_spannung_an_akku_kreis_8_s_1_Type()
)
aktuelle_spannung_an_akku_kreis_8_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_8_s_1.setStatus("current")
_Testergebnis_lastspannung_an_akku_reis_1_s_1_Type = DisplayString
_Testergebnis_lastspannung_an_akku_reis_1_s_1_Object = MibTableColumn
testergebnis_lastspannung_an_akku_reis_1_s_1 = _Testergebnis_lastspannung_an_akku_reis_1_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 44),
    _Testergebnis_lastspannung_an_akku_reis_1_s_1_Type()
)
testergebnis_lastspannung_an_akku_reis_1_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_reis_1_s_1.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_2_s_1_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_2_s_1_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_2_s_1 = _Testergebnis_lastspannung_an_akku_kreis_2_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 45),
    _Testergebnis_lastspannung_an_akku_kreis_2_s_1_Type()
)
testergebnis_lastspannung_an_akku_kreis_2_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_2_s_1.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_3_s_1_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_3_s_1_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_3_s_1 = _Testergebnis_lastspannung_an_akku_kreis_3_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 46),
    _Testergebnis_lastspannung_an_akku_kreis_3_s_1_Type()
)
testergebnis_lastspannung_an_akku_kreis_3_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_3_s_1.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_4_s_1_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_4_s_1_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_4_s_1 = _Testergebnis_lastspannung_an_akku_kreis_4_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 47),
    _Testergebnis_lastspannung_an_akku_kreis_4_s_1_Type()
)
testergebnis_lastspannung_an_akku_kreis_4_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_4_s_1.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_5_s_1_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_5_s_1_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_5_s_1 = _Testergebnis_lastspannung_an_akku_kreis_5_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 48),
    _Testergebnis_lastspannung_an_akku_kreis_5_s_1_Type()
)
testergebnis_lastspannung_an_akku_kreis_5_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_5_s_1.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_6_s_1_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_6_s_1_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_6_s_1 = _Testergebnis_lastspannung_an_akku_kreis_6_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 49),
    _Testergebnis_lastspannung_an_akku_kreis_6_s_1_Type()
)
testergebnis_lastspannung_an_akku_kreis_6_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_6_s_1.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_7_s_1_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_7_s_1_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_7_s_1 = _Testergebnis_lastspannung_an_akku_kreis_7_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 50),
    _Testergebnis_lastspannung_an_akku_kreis_7_s_1_Type()
)
testergebnis_lastspannung_an_akku_kreis_7_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_7_s_1.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_8_s_1_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_8_s_1_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_8_s_1 = _Testergebnis_lastspannung_an_akku_kreis_8_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 51),
    _Testergebnis_lastspannung_an_akku_kreis_8_s_1_Type()
)
testergebnis_lastspannung_an_akku_kreis_8_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_8_s_1.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_1_s_1_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_1_s_1_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_1_s_1 = _Testergebnis_innenwiderstand_akku_kreis_1_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 52),
    _Testergebnis_innenwiderstand_akku_kreis_1_s_1_Type()
)
testergebnis_innenwiderstand_akku_kreis_1_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_1_s_1.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_2_s_1_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_2_s_1_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_2_s_1 = _Testergebnis_innenwiderstand_akku_kreis_2_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 53),
    _Testergebnis_innenwiderstand_akku_kreis_2_s_1_Type()
)
testergebnis_innenwiderstand_akku_kreis_2_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_2_s_1.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_3_s_1_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_3_s_1_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_3_s_1 = _Testergebnis_innenwiderstand_akku_kreis_3_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 54),
    _Testergebnis_innenwiderstand_akku_kreis_3_s_1_Type()
)
testergebnis_innenwiderstand_akku_kreis_3_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_3_s_1.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_4_s_1_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_4_s_1_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_4_s_1 = _Testergebnis_innenwiderstand_akku_kreis_4_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 56),
    _Testergebnis_innenwiderstand_akku_kreis_4_s_1_Type()
)
testergebnis_innenwiderstand_akku_kreis_4_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_4_s_1.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_5_s_1_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_5_s_1_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_5_s_1 = _Testergebnis_innenwiderstand_akku_kreis_5_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 57),
    _Testergebnis_innenwiderstand_akku_kreis_5_s_1_Type()
)
testergebnis_innenwiderstand_akku_kreis_5_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_5_s_1.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_6_s_1_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_6_s_1_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_6_s_1 = _Testergebnis_innenwiderstand_akku_kreis_6_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 58),
    _Testergebnis_innenwiderstand_akku_kreis_6_s_1_Type()
)
testergebnis_innenwiderstand_akku_kreis_6_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_6_s_1.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_7_s_1_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_7_s_1_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_7_s_1 = _Testergebnis_innenwiderstand_akku_kreis_7_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 59),
    _Testergebnis_innenwiderstand_akku_kreis_7_s_1_Type()
)
testergebnis_innenwiderstand_akku_kreis_7_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_7_s_1.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_8_s_1_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_8_s_1_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_8_s_1 = _Testergebnis_innenwiderstand_akku_kreis_8_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 60),
    _Testergebnis_innenwiderstand_akku_kreis_8_s_1_Type()
)
testergebnis_innenwiderstand_akku_kreis_8_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_8_s_1.setStatus("current")
_Netzteilspannung_uin1_s_1_Type = DisplayString
_Netzteilspannung_uin1_s_1_Object = MibTableColumn
netzteilspannung_uin1_s_1 = _Netzteilspannung_uin1_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 61),
    _Netzteilspannung_uin1_s_1_Type()
)
netzteilspannung_uin1_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzteilspannung_uin1_s_1.setStatus("current")
_Netzteilspannung_uin2_s_1_Type = DisplayString
_Netzteilspannung_uin2_s_1_Object = MibTableColumn
netzteilspannung_uin2_s_1 = _Netzteilspannung_uin2_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 62),
    _Netzteilspannung_uin2_s_1_Type()
)
netzteilspannung_uin2_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzteilspannung_uin2_s_1.setStatus("current")
_Programmierte_minimale_soll_sendeleistung_s_1_Type = DisplayString
_Programmierte_minimale_soll_sendeleistung_s_1_Object = MibTableColumn
programmierte_minimale_soll_sendeleistung_s_1 = _Programmierte_minimale_soll_sendeleistung_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 63),
    _Programmierte_minimale_soll_sendeleistung_s_1_Type()
)
programmierte_minimale_soll_sendeleistung_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programmierte_minimale_soll_sendeleistung_s_1.setStatus("current")
_Programmierte_maximale_antennen_reflexion_s_1_Type = DisplayString
_Programmierte_maximale_antennen_reflexion_s_1_Object = MibTableColumn
programmierte_maximale_antennen_reflexion_s_1 = _Programmierte_maximale_antennen_reflexion_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 64),
    _Programmierte_maximale_antennen_reflexion_s_1_Type()
)
programmierte_maximale_antennen_reflexion_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programmierte_maximale_antennen_reflexion_s_1.setStatus("current")
_Programmierte_minimale_anzahl_praesenzsignale_s_1_Type = DisplayString
_Programmierte_minimale_anzahl_praesenzsignale_s_1_Object = MibTableColumn
programmierte_minimale_anzahl_praesenzsignale_s_1 = _Programmierte_minimale_anzahl_praesenzsignale_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 65),
    _Programmierte_minimale_anzahl_praesenzsignale_s_1_Type()
)
programmierte_minimale_anzahl_praesenzsignale_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programmierte_minimale_anzahl_praesenzsignale_s_1.setStatus("current")
_Summen_fehlerstatus_von_tmoa_anlage_s_1_Type = DisplayString
_Summen_fehlerstatus_von_tmoa_anlage_s_1_Object = MibTableColumn
summen_fehlerstatus_von_tmoa_anlage_s_1 = _Summen_fehlerstatus_von_tmoa_anlage_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 66),
    _Summen_fehlerstatus_von_tmoa_anlage_s_1_Type()
)
summen_fehlerstatus_von_tmoa_anlage_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summen_fehlerstatus_von_tmoa_anlage_s_1.setStatus("current")
_Summen_fehlerstatus_von_anbinderepeater_s_1_Type = DisplayString
_Summen_fehlerstatus_von_anbinderepeater_s_1_Object = MibTableColumn
summen_fehlerstatus_von_anbinderepeater_s_1 = _Summen_fehlerstatus_von_anbinderepeater_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 67),
    _Summen_fehlerstatus_von_anbinderepeater_s_1_Type()
)
summen_fehlerstatus_von_anbinderepeater_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summen_fehlerstatus_von_anbinderepeater_s_1.setStatus("current")
_Summen_fehlerstatus_von_analogem_repeater_s_1_Type = DisplayString
_Summen_fehlerstatus_von_analogem_repeater_s_1_Object = MibTableColumn
summen_fehlerstatus_von_analogem_repeater_s_1 = _Summen_fehlerstatus_von_analogem_repeater_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 68),
    _Summen_fehlerstatus_von_analogem_repeater_s_1_Type()
)
summen_fehlerstatus_von_analogem_repeater_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summen_fehlerstatus_von_analogem_repeater_s_1.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_1_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_1_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_1 = _Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 69),
    _Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_1_Type()
)
aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_1.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_1_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_1_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_1 = _Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 70),
    _Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_1_Type()
)
aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_1.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_1_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_1_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_1 = _Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 71),
    _Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_1_Type()
)
aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_1.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_1_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_1_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_1 = _Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 72),
    _Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_1_Type()
)
aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_1.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_1_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_1_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_1 = _Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 73),
    _Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_1_Type()
)
aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_1.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_1_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_1_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_1 = _Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 74),
    _Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_1_Type()
)
aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_1.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_1_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_1_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_1 = _Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 75),
    _Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_1_Type()
)
aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_1.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_1_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_1_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_1 = _Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 76),
    _Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_1_Type()
)
aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_1.setStatus("current")
_Netzspannungsversorgung_von_tmoa_anlage_s_1_Type = DisplayString
_Netzspannungsversorgung_von_tmoa_anlage_s_1_Object = MibTableColumn
netzspannungsversorgung_von_tmoa_anlage_s_1 = _Netzspannungsversorgung_von_tmoa_anlage_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 77),
    _Netzspannungsversorgung_von_tmoa_anlage_s_1_Type()
)
netzspannungsversorgung_von_tmoa_anlage_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzspannungsversorgung_von_tmoa_anlage_s_1.setStatus("current")
_Netzspannungsversorgung_von_anbinderepeater_s_1_Type = DisplayString
_Netzspannungsversorgung_von_anbinderepeater_s_1_Object = MibTableColumn
netzspannungsversorgung_von_anbinderepeater_s_1 = _Netzspannungsversorgung_von_anbinderepeater_s_1_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 1, 1, 78),
    _Netzspannungsversorgung_von_anbinderepeater_s_1_Type()
)
netzspannungsversorgung_von_anbinderepeater_s_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzspannungsversorgung_von_anbinderepeater_s_1.setStatus("current")
_Ak_slave_2_i_ObjectIdentity = ObjectIdentity
ak_slave_2_i = _Ak_slave_2_i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2)
)
_ModulTable_s_2_Object = MibTable
modulTable_s_2 = _ModulTable_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    modulTable_s_2.setStatus("current")
_ModulEntry_s_2_Object = MibTableRow
modulEntry_s_2 = _ModulEntry_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1)
)
modulEntry_s_2.setIndexNames(
    (0, "AK-FUNKTECHNIK-MIB", "modulIndex-s-2"),
)
if mibBuilder.loadTexts:
    modulEntry_s_2.setStatus("current")
_ModulIndex_s_2_Type = DisplayString
_ModulIndex_s_2_Object = MibTableColumn
modulIndex_s_2 = _ModulIndex_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 1),
    _ModulIndex_s_2_Type()
)
modulIndex_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulIndex_s_2.setStatus("current")
_Geraete_typ_s_2_Type = DisplayString
_Geraete_typ_s_2_Object = MibTableColumn
geraete_typ_s_2 = _Geraete_typ_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 2),
    _Geraete_typ_s_2_Type()
)
geraete_typ_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geraete_typ_s_2.setStatus("current")
_Betriebsstatus_s_2_Type = DisplayString
_Betriebsstatus_s_2_Object = MibTableColumn
betriebsstatus_s_2 = _Betriebsstatus_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 3),
    _Betriebsstatus_s_2_Type()
)
betriebsstatus_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    betriebsstatus_s_2.setStatus("current")
_Senderstatus_s_2_Type = DisplayString
_Senderstatus_s_2_Object = MibTableColumn
senderstatus_s_2 = _Senderstatus_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 4),
    _Senderstatus_s_2_Type()
)
senderstatus_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    senderstatus_s_2.setStatus("current")
_Fehlerstatus_s_2_Type = DisplayString
_Fehlerstatus_s_2_Object = MibTableColumn
fehlerstatus_s_2 = _Fehlerstatus_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 5),
    _Fehlerstatus_s_2_Type()
)
fehlerstatus_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fehlerstatus_s_2.setStatus("current")
_Dem_adapter_zugeordnete_funkgeraetetype_s_2_Type = DisplayString
_Dem_adapter_zugeordnete_funkgeraetetype_s_2_Object = MibTableColumn
dem_adapter_zugeordnete_funkgeraetetype_s_2 = _Dem_adapter_zugeordnete_funkgeraetetype_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 6),
    _Dem_adapter_zugeordnete_funkgeraetetype_s_2_Type()
)
dem_adapter_zugeordnete_funkgeraetetype_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dem_adapter_zugeordnete_funkgeraetetype_s_2.setStatus("current")
_Eingabe_und_anzeigemodul_s_2_Type = DisplayString
_Eingabe_und_anzeigemodul_s_2_Object = MibTableColumn
eingabe_und_anzeigemodul_s_2 = _Eingabe_und_anzeigemodul_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 7),
    _Eingabe_und_anzeigemodul_s_2_Type()
)
eingabe_und_anzeigemodul_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eingabe_und_anzeigemodul_s_2.setStatus("current")
_Mod_bus_verbindung_module_s_2_Type = DisplayString
_Mod_bus_verbindung_module_s_2_Object = MibTableColumn
mod_bus_verbindung_module_s_2 = _Mod_bus_verbindung_module_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 8),
    _Mod_bus_verbindung_module_s_2_Type()
)
mod_bus_verbindung_module_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mod_bus_verbindung_module_s_2.setStatus("current")
_Gemessene_sendeleistung_im_testmode_s_2_Type = DisplayString
_Gemessene_sendeleistung_im_testmode_s_2_Object = MibTableColumn
gemessene_sendeleistung_im_testmode_s_2 = _Gemessene_sendeleistung_im_testmode_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 9),
    _Gemessene_sendeleistung_im_testmode_s_2_Type()
)
gemessene_sendeleistung_im_testmode_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemessene_sendeleistung_im_testmode_s_2.setStatus("current")
_Aktuelle_sendeleistung_s_2_Type = DisplayString
_Aktuelle_sendeleistung_s_2_Object = MibTableColumn
aktuelle_sendeleistung_s_2 = _Aktuelle_sendeleistung_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 10),
    _Aktuelle_sendeleistung_s_2_Type()
)
aktuelle_sendeleistung_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_sendeleistung_s_2.setStatus("current")
_Gemessene_reflexion_im_testmode_s_2_Type = DisplayString
_Gemessene_reflexion_im_testmode_s_2_Object = MibTableColumn
gemessene_reflexion_im_testmode_s_2 = _Gemessene_reflexion_im_testmode_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 11),
    _Gemessene_reflexion_im_testmode_s_2_Type()
)
gemessene_reflexion_im_testmode_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemessene_reflexion_im_testmode_s_2.setStatus("current")
_Aktuelle_reflexion_s_2_Type = DisplayString
_Aktuelle_reflexion_s_2_Object = MibTableColumn
aktuelle_reflexion_s_2 = _Aktuelle_reflexion_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 12),
    _Aktuelle_reflexion_s_2_Type()
)
aktuelle_reflexion_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_reflexion_s_2.setStatus("current")
_Letzte_gemessene_donor_sendeleistung_s_2_Type = DisplayString
_Letzte_gemessene_donor_sendeleistung_s_2_Object = MibTableColumn
letzte_gemessene_donor_sendeleistung_s_2 = _Letzte_gemessene_donor_sendeleistung_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 13),
    _Letzte_gemessene_donor_sendeleistung_s_2_Type()
)
letzte_gemessene_donor_sendeleistung_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    letzte_gemessene_donor_sendeleistung_s_2.setStatus("current")
_Aktuelle_donor_sendeleistung_s_2_Type = DisplayString
_Aktuelle_donor_sendeleistung_s_2_Object = MibTableColumn
aktuelle_donor_sendeleistung_s_2 = _Aktuelle_donor_sendeleistung_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 14),
    _Aktuelle_donor_sendeleistung_s_2_Type()
)
aktuelle_donor_sendeleistung_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_donor_sendeleistung_s_2.setStatus("current")
_Letzte_gemessene_donor_reflexion_s_2_Type = DisplayString
_Letzte_gemessene_donor_reflexion_s_2_Object = MibTableColumn
letzte_gemessene_donor_reflexion_s_2 = _Letzte_gemessene_donor_reflexion_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 15),
    _Letzte_gemessene_donor_reflexion_s_2_Type()
)
letzte_gemessene_donor_reflexion_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    letzte_gemessene_donor_reflexion_s_2.setStatus("current")
_Aktuelle_donor_reflexion_s_2_Type = DisplayString
_Aktuelle_donor_reflexion_s_2_Object = MibTableColumn
aktuelle_donor_reflexion_s_2 = _Aktuelle_donor_reflexion_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 16),
    _Aktuelle_donor_reflexion_s_2_Type()
)
aktuelle_donor_reflexion_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_donor_reflexion_s_2.setStatus("current")
_Anzahl_gemessener_praesenzsignale_im_testmode_s_2_Type = DisplayString
_Anzahl_gemessener_praesenzsignale_im_testmode_s_2_Object = MibTableColumn
anzahl_gemessener_praesenzsignale_im_testmode_s_2 = _Anzahl_gemessener_praesenzsignale_im_testmode_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 18),
    _Anzahl_gemessener_praesenzsignale_im_testmode_s_2_Type()
)
anzahl_gemessener_praesenzsignale_im_testmode_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anzahl_gemessener_praesenzsignale_im_testmode_s_2.setStatus("current")
_Aktuelle_ausgangsspannung_ub_s_2_Type = DisplayString
_Aktuelle_ausgangsspannung_ub_s_2_Object = MibTableColumn
aktuelle_ausgangsspannung_ub_s_2 = _Aktuelle_ausgangsspannung_ub_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 19),
    _Aktuelle_ausgangsspannung_ub_s_2_Type()
)
aktuelle_ausgangsspannung_ub_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_ub_s_2.setStatus("current")
_Aktuelle_ausgangsspannung_u1_s_2_Type = DisplayString
_Aktuelle_ausgangsspannung_u1_s_2_Object = MibTableColumn
aktuelle_ausgangsspannung_u1_s_2 = _Aktuelle_ausgangsspannung_u1_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 20),
    _Aktuelle_ausgangsspannung_u1_s_2_Type()
)
aktuelle_ausgangsspannung_u1_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u1_s_2.setStatus("current")
_Aktuelle_ausgangsspannung_u2_s_2_Type = DisplayString
_Aktuelle_ausgangsspannung_u2_s_2_Object = MibTableColumn
aktuelle_ausgangsspannung_u2_s_2 = _Aktuelle_ausgangsspannung_u2_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 21),
    _Aktuelle_ausgangsspannung_u2_s_2_Type()
)
aktuelle_ausgangsspannung_u2_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u2_s_2.setStatus("current")
_Aktuelle_ausgangsspannung_u3_s_2_Type = DisplayString
_Aktuelle_ausgangsspannung_u3_s_2_Object = MibTableColumn
aktuelle_ausgangsspannung_u3_s_2 = _Aktuelle_ausgangsspannung_u3_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 22),
    _Aktuelle_ausgangsspannung_u3_s_2_Type()
)
aktuelle_ausgangsspannung_u3_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u3_s_2.setStatus("current")
_Aktuelle_ausgangsspannung_u4_s_2_Type = DisplayString
_Aktuelle_ausgangsspannung_u4_s_2_Object = MibTableColumn
aktuelle_ausgangsspannung_u4_s_2 = _Aktuelle_ausgangsspannung_u4_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 23),
    _Aktuelle_ausgangsspannung_u4_s_2_Type()
)
aktuelle_ausgangsspannung_u4_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u4_s_2.setStatus("current")
_Aktuelle_ausgangsspannung_u5_s_2_Type = DisplayString
_Aktuelle_ausgangsspannung_u5_s_2_Object = MibTableColumn
aktuelle_ausgangsspannung_u5_s_2 = _Aktuelle_ausgangsspannung_u5_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 24),
    _Aktuelle_ausgangsspannung_u5_s_2_Type()
)
aktuelle_ausgangsspannung_u5_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u5_s_2.setStatus("current")
_Aktuelle_ausgangsspannung_u6_s_2_Type = DisplayString
_Aktuelle_ausgangsspannung_u6_s_2_Object = MibTableColumn
aktuelle_ausgangsspannung_u6_s_2 = _Aktuelle_ausgangsspannung_u6_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 25),
    _Aktuelle_ausgangsspannung_u6_s_2_Type()
)
aktuelle_ausgangsspannung_u6_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u6_s_2.setStatus("current")
_Aktuelle_ausgangsspannung_u7_s_2_Type = DisplayString
_Aktuelle_ausgangsspannung_u7_s_2_Object = MibTableColumn
aktuelle_ausgangsspannung_u7_s_2 = _Aktuelle_ausgangsspannung_u7_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 26),
    _Aktuelle_ausgangsspannung_u7_s_2_Type()
)
aktuelle_ausgangsspannung_u7_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u7_s_2.setStatus("current")
_Aktuelle_ausgangsspannung_u8_s_2_Type = DisplayString
_Aktuelle_ausgangsspannung_u8_s_2_Object = MibTableColumn
aktuelle_ausgangsspannung_u8_s_2 = _Aktuelle_ausgangsspannung_u8_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 27),
    _Aktuelle_ausgangsspannung_u8_s_2_Type()
)
aktuelle_ausgangsspannung_u8_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u8_s_2.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_1_s_2_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_1_s_2_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_1_s_2 = _Aktuelle_ladespannung_an_akku_kreis_1_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 28),
    _Aktuelle_ladespannung_an_akku_kreis_1_s_2_Type()
)
aktuelle_ladespannung_an_akku_kreis_1_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_1_s_2.setStatus("current")
_Aktuelle_ladespannung_an_akku_Kreis_2_s_2_Type = DisplayString
_Aktuelle_ladespannung_an_akku_Kreis_2_s_2_Object = MibTableColumn
aktuelle_ladespannung_an_akku_Kreis_2_s_2 = _Aktuelle_ladespannung_an_akku_Kreis_2_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 29),
    _Aktuelle_ladespannung_an_akku_Kreis_2_s_2_Type()
)
aktuelle_ladespannung_an_akku_Kreis_2_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_Kreis_2_s_2.setStatus("current")
_Aktuelle_ladespannung_an_akku_Kreis_3_s_2_Type = DisplayString
_Aktuelle_ladespannung_an_akku_Kreis_3_s_2_Object = MibTableColumn
aktuelle_ladespannung_an_akku_Kreis_3_s_2 = _Aktuelle_ladespannung_an_akku_Kreis_3_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 30),
    _Aktuelle_ladespannung_an_akku_Kreis_3_s_2_Type()
)
aktuelle_ladespannung_an_akku_Kreis_3_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_Kreis_3_s_2.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_4_s_2_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_4_s_2_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_4_s_2 = _Aktuelle_ladespannung_an_akku_kreis_4_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 31),
    _Aktuelle_ladespannung_an_akku_kreis_4_s_2_Type()
)
aktuelle_ladespannung_an_akku_kreis_4_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_4_s_2.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_5_s_2_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_5_s_2_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_5_s_2 = _Aktuelle_ladespannung_an_akku_kreis_5_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 32),
    _Aktuelle_ladespannung_an_akku_kreis_5_s_2_Type()
)
aktuelle_ladespannung_an_akku_kreis_5_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_5_s_2.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_6_s_2_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_6_s_2_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_6_s_2 = _Aktuelle_ladespannung_an_akku_kreis_6_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 33),
    _Aktuelle_ladespannung_an_akku_kreis_6_s_2_Type()
)
aktuelle_ladespannung_an_akku_kreis_6_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_6_s_2.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_7_s_2_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_7_s_2_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_7_s_2 = _Aktuelle_ladespannung_an_akku_kreis_7_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 34),
    _Aktuelle_ladespannung_an_akku_kreis_7_s_2_Type()
)
aktuelle_ladespannung_an_akku_kreis_7_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_7_s_2.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_8_s_2_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_8_s_2_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_8_s_2 = _Aktuelle_ladespannung_an_akku_kreis_8_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 35),
    _Aktuelle_ladespannung_an_akku_kreis_8_s_2_Type()
)
aktuelle_ladespannung_an_akku_kreis_8_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_8_s_2.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_1_s_2_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_1_s_2_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_1_s_2 = _Aktuelle_spannung_an_akku_kreis_1_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 36),
    _Aktuelle_spannung_an_akku_kreis_1_s_2_Type()
)
aktuelle_spannung_an_akku_kreis_1_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_1_s_2.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_2_s_2_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_2_s_2_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_2_s_2 = _Aktuelle_spannung_an_akku_kreis_2_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 37),
    _Aktuelle_spannung_an_akku_kreis_2_s_2_Type()
)
aktuelle_spannung_an_akku_kreis_2_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_2_s_2.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_3_s_2_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_3_s_2_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_3_s_2 = _Aktuelle_spannung_an_akku_kreis_3_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 38),
    _Aktuelle_spannung_an_akku_kreis_3_s_2_Type()
)
aktuelle_spannung_an_akku_kreis_3_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_3_s_2.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_4_s_2_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_4_s_2_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_4_s_2 = _Aktuelle_spannung_an_akku_kreis_4_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 39),
    _Aktuelle_spannung_an_akku_kreis_4_s_2_Type()
)
aktuelle_spannung_an_akku_kreis_4_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_4_s_2.setStatus("current")
_Aktuelle_spannung_an_akku_reis_5_s_2_Type = DisplayString
_Aktuelle_spannung_an_akku_reis_5_s_2_Object = MibTableColumn
aktuelle_spannung_an_akku_reis_5_s_2 = _Aktuelle_spannung_an_akku_reis_5_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 40),
    _Aktuelle_spannung_an_akku_reis_5_s_2_Type()
)
aktuelle_spannung_an_akku_reis_5_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_reis_5_s_2.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_6_s_2_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_6_s_2_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_6_s_2 = _Aktuelle_spannung_an_akku_kreis_6_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 41),
    _Aktuelle_spannung_an_akku_kreis_6_s_2_Type()
)
aktuelle_spannung_an_akku_kreis_6_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_6_s_2.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_7_s_2_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_7_s_2_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_7_s_2 = _Aktuelle_spannung_an_akku_kreis_7_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 42),
    _Aktuelle_spannung_an_akku_kreis_7_s_2_Type()
)
aktuelle_spannung_an_akku_kreis_7_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_7_s_2.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_8_s_2_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_8_s_2_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_8_s_2 = _Aktuelle_spannung_an_akku_kreis_8_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 43),
    _Aktuelle_spannung_an_akku_kreis_8_s_2_Type()
)
aktuelle_spannung_an_akku_kreis_8_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_8_s_2.setStatus("current")
_Testergebnis_lastspannung_an_akku_reis_1_s_2_Type = DisplayString
_Testergebnis_lastspannung_an_akku_reis_1_s_2_Object = MibTableColumn
testergebnis_lastspannung_an_akku_reis_1_s_2 = _Testergebnis_lastspannung_an_akku_reis_1_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 44),
    _Testergebnis_lastspannung_an_akku_reis_1_s_2_Type()
)
testergebnis_lastspannung_an_akku_reis_1_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_reis_1_s_2.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_2_s_2_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_2_s_2_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_2_s_2 = _Testergebnis_lastspannung_an_akku_kreis_2_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 45),
    _Testergebnis_lastspannung_an_akku_kreis_2_s_2_Type()
)
testergebnis_lastspannung_an_akku_kreis_2_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_2_s_2.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_3_s_2_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_3_s_2_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_3_s_2 = _Testergebnis_lastspannung_an_akku_kreis_3_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 46),
    _Testergebnis_lastspannung_an_akku_kreis_3_s_2_Type()
)
testergebnis_lastspannung_an_akku_kreis_3_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_3_s_2.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_4_s_2_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_4_s_2_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_4_s_2 = _Testergebnis_lastspannung_an_akku_kreis_4_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 47),
    _Testergebnis_lastspannung_an_akku_kreis_4_s_2_Type()
)
testergebnis_lastspannung_an_akku_kreis_4_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_4_s_2.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_5_s_2_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_5_s_2_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_5_s_2 = _Testergebnis_lastspannung_an_akku_kreis_5_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 48),
    _Testergebnis_lastspannung_an_akku_kreis_5_s_2_Type()
)
testergebnis_lastspannung_an_akku_kreis_5_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_5_s_2.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_6_s_2_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_6_s_2_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_6_s_2 = _Testergebnis_lastspannung_an_akku_kreis_6_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 49),
    _Testergebnis_lastspannung_an_akku_kreis_6_s_2_Type()
)
testergebnis_lastspannung_an_akku_kreis_6_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_6_s_2.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_7_s_2_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_7_s_2_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_7_s_2 = _Testergebnis_lastspannung_an_akku_kreis_7_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 50),
    _Testergebnis_lastspannung_an_akku_kreis_7_s_2_Type()
)
testergebnis_lastspannung_an_akku_kreis_7_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_7_s_2.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_8_s_2_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_8_s_2_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_8_s_2 = _Testergebnis_lastspannung_an_akku_kreis_8_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 51),
    _Testergebnis_lastspannung_an_akku_kreis_8_s_2_Type()
)
testergebnis_lastspannung_an_akku_kreis_8_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_8_s_2.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_1_s_2_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_1_s_2_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_1_s_2 = _Testergebnis_innenwiderstand_akku_kreis_1_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 52),
    _Testergebnis_innenwiderstand_akku_kreis_1_s_2_Type()
)
testergebnis_innenwiderstand_akku_kreis_1_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_1_s_2.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_2_s_2_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_2_s_2_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_2_s_2 = _Testergebnis_innenwiderstand_akku_kreis_2_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 53),
    _Testergebnis_innenwiderstand_akku_kreis_2_s_2_Type()
)
testergebnis_innenwiderstand_akku_kreis_2_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_2_s_2.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_3_s_2_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_3_s_2_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_3_s_2 = _Testergebnis_innenwiderstand_akku_kreis_3_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 54),
    _Testergebnis_innenwiderstand_akku_kreis_3_s_2_Type()
)
testergebnis_innenwiderstand_akku_kreis_3_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_3_s_2.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_4_s_2_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_4_s_2_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_4_s_2 = _Testergebnis_innenwiderstand_akku_kreis_4_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 56),
    _Testergebnis_innenwiderstand_akku_kreis_4_s_2_Type()
)
testergebnis_innenwiderstand_akku_kreis_4_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_4_s_2.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_5_s_2_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_5_s_2_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_5_s_2 = _Testergebnis_innenwiderstand_akku_kreis_5_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 57),
    _Testergebnis_innenwiderstand_akku_kreis_5_s_2_Type()
)
testergebnis_innenwiderstand_akku_kreis_5_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_5_s_2.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_6_s_2_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_6_s_2_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_6_s_2 = _Testergebnis_innenwiderstand_akku_kreis_6_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 58),
    _Testergebnis_innenwiderstand_akku_kreis_6_s_2_Type()
)
testergebnis_innenwiderstand_akku_kreis_6_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_6_s_2.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_7_s_2_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_7_s_2_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_7_s_2 = _Testergebnis_innenwiderstand_akku_kreis_7_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 59),
    _Testergebnis_innenwiderstand_akku_kreis_7_s_2_Type()
)
testergebnis_innenwiderstand_akku_kreis_7_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_7_s_2.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_8_s_2_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_8_s_2_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_8_s_2 = _Testergebnis_innenwiderstand_akku_kreis_8_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 60),
    _Testergebnis_innenwiderstand_akku_kreis_8_s_2_Type()
)
testergebnis_innenwiderstand_akku_kreis_8_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_8_s_2.setStatus("current")
_Netzteilspannung_uin1_s_2_Type = DisplayString
_Netzteilspannung_uin1_s_2_Object = MibTableColumn
netzteilspannung_uin1_s_2 = _Netzteilspannung_uin1_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 61),
    _Netzteilspannung_uin1_s_2_Type()
)
netzteilspannung_uin1_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzteilspannung_uin1_s_2.setStatus("current")
_Netzteilspannung_uin2_s_2_Type = DisplayString
_Netzteilspannung_uin2_s_2_Object = MibTableColumn
netzteilspannung_uin2_s_2 = _Netzteilspannung_uin2_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 62),
    _Netzteilspannung_uin2_s_2_Type()
)
netzteilspannung_uin2_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzteilspannung_uin2_s_2.setStatus("current")
_Programmierte_minimale_soll_sendeleistung_s_2_Type = DisplayString
_Programmierte_minimale_soll_sendeleistung_s_2_Object = MibTableColumn
programmierte_minimale_soll_sendeleistung_s_2 = _Programmierte_minimale_soll_sendeleistung_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 63),
    _Programmierte_minimale_soll_sendeleistung_s_2_Type()
)
programmierte_minimale_soll_sendeleistung_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programmierte_minimale_soll_sendeleistung_s_2.setStatus("current")
_Programmierte_maximale_antennen_reflexion_s_2_Type = DisplayString
_Programmierte_maximale_antennen_reflexion_s_2_Object = MibTableColumn
programmierte_maximale_antennen_reflexion_s_2 = _Programmierte_maximale_antennen_reflexion_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 64),
    _Programmierte_maximale_antennen_reflexion_s_2_Type()
)
programmierte_maximale_antennen_reflexion_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programmierte_maximale_antennen_reflexion_s_2.setStatus("current")
_Programmierte_minimale_anzahl_praesenzsignale_s_2_Type = DisplayString
_Programmierte_minimale_anzahl_praesenzsignale_s_2_Object = MibTableColumn
programmierte_minimale_anzahl_praesenzsignale_s_2 = _Programmierte_minimale_anzahl_praesenzsignale_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 65),
    _Programmierte_minimale_anzahl_praesenzsignale_s_2_Type()
)
programmierte_minimale_anzahl_praesenzsignale_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programmierte_minimale_anzahl_praesenzsignale_s_2.setStatus("current")
_Summen_fehlerstatus_von_tmoa_anlage_s_2_Type = DisplayString
_Summen_fehlerstatus_von_tmoa_anlage_s_2_Object = MibTableColumn
summen_fehlerstatus_von_tmoa_anlage_s_2 = _Summen_fehlerstatus_von_tmoa_anlage_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 66),
    _Summen_fehlerstatus_von_tmoa_anlage_s_2_Type()
)
summen_fehlerstatus_von_tmoa_anlage_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summen_fehlerstatus_von_tmoa_anlage_s_2.setStatus("current")
_Summen_fehlerstatus_von_anbinderepeater_s_2_Type = DisplayString
_Summen_fehlerstatus_von_anbinderepeater_s_2_Object = MibTableColumn
summen_fehlerstatus_von_anbinderepeater_s_2 = _Summen_fehlerstatus_von_anbinderepeater_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 67),
    _Summen_fehlerstatus_von_anbinderepeater_s_2_Type()
)
summen_fehlerstatus_von_anbinderepeater_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summen_fehlerstatus_von_anbinderepeater_s_2.setStatus("current")
_Summen_fehlerstatus_von_analogem_repeater_s_2_Type = DisplayString
_Summen_fehlerstatus_von_analogem_repeater_s_2_Object = MibTableColumn
summen_fehlerstatus_von_analogem_repeater_s_2 = _Summen_fehlerstatus_von_analogem_repeater_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 68),
    _Summen_fehlerstatus_von_analogem_repeater_s_2_Type()
)
summen_fehlerstatus_von_analogem_repeater_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summen_fehlerstatus_von_analogem_repeater_s_2.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_2_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_2_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_2 = _Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 69),
    _Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_2_Type()
)
aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_2.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_2_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_2_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_2 = _Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 70),
    _Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_2_Type()
)
aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_2.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_2_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_2_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_2 = _Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 71),
    _Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_2_Type()
)
aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_2.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_2_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_2_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_2 = _Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 72),
    _Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_2_Type()
)
aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_2.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_2_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_2_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_2 = _Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 73),
    _Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_2_Type()
)
aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_2.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_2_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_2_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_2 = _Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 74),
    _Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_2_Type()
)
aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_2.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_2_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_2_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_2 = _Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 75),
    _Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_2_Type()
)
aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_2.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_2_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_2_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_2 = _Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 76),
    _Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_2_Type()
)
aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_2.setStatus("current")
_Netzspannungsversorgung_von_tmoa_anlage_s_2_Type = DisplayString
_Netzspannungsversorgung_von_tmoa_anlage_s_2_Object = MibTableColumn
netzspannungsversorgung_von_tmoa_anlage_s_2 = _Netzspannungsversorgung_von_tmoa_anlage_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 77),
    _Netzspannungsversorgung_von_tmoa_anlage_s_2_Type()
)
netzspannungsversorgung_von_tmoa_anlage_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzspannungsversorgung_von_tmoa_anlage_s_2.setStatus("current")
_Netzspannungsversorgung_von_anbinderepeater_s_2_Type = DisplayString
_Netzspannungsversorgung_von_anbinderepeater_s_2_Object = MibTableColumn
netzspannungsversorgung_von_anbinderepeater_s_2 = _Netzspannungsversorgung_von_anbinderepeater_s_2_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 1, 1, 78),
    _Netzspannungsversorgung_von_anbinderepeater_s_2_Type()
)
netzspannungsversorgung_von_anbinderepeater_s_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzspannungsversorgung_von_anbinderepeater_s_2.setStatus("current")
_Ak_slave_3_i_ObjectIdentity = ObjectIdentity
ak_slave_3_i = _Ak_slave_3_i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3)
)
_ModulTable_s_3_Object = MibTable
modulTable_s_3 = _ModulTable_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    modulTable_s_3.setStatus("current")
_ModulEntry_s_3_Object = MibTableRow
modulEntry_s_3 = _ModulEntry_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1)
)
modulEntry_s_3.setIndexNames(
    (0, "AK-FUNKTECHNIK-MIB", "modulIndex-s-3"),
)
if mibBuilder.loadTexts:
    modulEntry_s_3.setStatus("current")
_ModulIndex_s_3_Type = DisplayString
_ModulIndex_s_3_Object = MibTableColumn
modulIndex_s_3 = _ModulIndex_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 1),
    _ModulIndex_s_3_Type()
)
modulIndex_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulIndex_s_3.setStatus("current")
_Geraete_typ_s_3_Type = DisplayString
_Geraete_typ_s_3_Object = MibTableColumn
geraete_typ_s_3 = _Geraete_typ_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 2),
    _Geraete_typ_s_3_Type()
)
geraete_typ_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geraete_typ_s_3.setStatus("current")
_Betriebsstatus_s_3_Type = DisplayString
_Betriebsstatus_s_3_Object = MibTableColumn
betriebsstatus_s_3 = _Betriebsstatus_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 3),
    _Betriebsstatus_s_3_Type()
)
betriebsstatus_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    betriebsstatus_s_3.setStatus("current")
_Senderstatus_s_3_Type = DisplayString
_Senderstatus_s_3_Object = MibTableColumn
senderstatus_s_3 = _Senderstatus_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 4),
    _Senderstatus_s_3_Type()
)
senderstatus_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    senderstatus_s_3.setStatus("current")
_Fehlerstatus_s_3_Type = DisplayString
_Fehlerstatus_s_3_Object = MibTableColumn
fehlerstatus_s_3 = _Fehlerstatus_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 5),
    _Fehlerstatus_s_3_Type()
)
fehlerstatus_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fehlerstatus_s_3.setStatus("current")
_Dem_adapter_zugeordnete_funkgeraetetype_s_3_Type = DisplayString
_Dem_adapter_zugeordnete_funkgeraetetype_s_3_Object = MibTableColumn
dem_adapter_zugeordnete_funkgeraetetype_s_3 = _Dem_adapter_zugeordnete_funkgeraetetype_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 6),
    _Dem_adapter_zugeordnete_funkgeraetetype_s_3_Type()
)
dem_adapter_zugeordnete_funkgeraetetype_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dem_adapter_zugeordnete_funkgeraetetype_s_3.setStatus("current")
_Eingabe_und_anzeigemodul_s_3_Type = DisplayString
_Eingabe_und_anzeigemodul_s_3_Object = MibTableColumn
eingabe_und_anzeigemodul_s_3 = _Eingabe_und_anzeigemodul_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 7),
    _Eingabe_und_anzeigemodul_s_3_Type()
)
eingabe_und_anzeigemodul_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eingabe_und_anzeigemodul_s_3.setStatus("current")
_Mod_bus_verbindung_module_s_3_Type = DisplayString
_Mod_bus_verbindung_module_s_3_Object = MibTableColumn
mod_bus_verbindung_module_s_3 = _Mod_bus_verbindung_module_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 8),
    _Mod_bus_verbindung_module_s_3_Type()
)
mod_bus_verbindung_module_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mod_bus_verbindung_module_s_3.setStatus("current")
_Gemessene_sendeleistung_im_testmode_s_3_Type = DisplayString
_Gemessene_sendeleistung_im_testmode_s_3_Object = MibTableColumn
gemessene_sendeleistung_im_testmode_s_3 = _Gemessene_sendeleistung_im_testmode_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 9),
    _Gemessene_sendeleistung_im_testmode_s_3_Type()
)
gemessene_sendeleistung_im_testmode_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemessene_sendeleistung_im_testmode_s_3.setStatus("current")
_Aktuelle_sendeleistung_s_3_Type = DisplayString
_Aktuelle_sendeleistung_s_3_Object = MibTableColumn
aktuelle_sendeleistung_s_3 = _Aktuelle_sendeleistung_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 10),
    _Aktuelle_sendeleistung_s_3_Type()
)
aktuelle_sendeleistung_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_sendeleistung_s_3.setStatus("current")
_Gemessene_reflexion_im_testmode_s_3_Type = DisplayString
_Gemessene_reflexion_im_testmode_s_3_Object = MibTableColumn
gemessene_reflexion_im_testmode_s_3 = _Gemessene_reflexion_im_testmode_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 11),
    _Gemessene_reflexion_im_testmode_s_3_Type()
)
gemessene_reflexion_im_testmode_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemessene_reflexion_im_testmode_s_3.setStatus("current")
_Aktuelle_reflexion_s_3_Type = DisplayString
_Aktuelle_reflexion_s_3_Object = MibTableColumn
aktuelle_reflexion_s_3 = _Aktuelle_reflexion_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 12),
    _Aktuelle_reflexion_s_3_Type()
)
aktuelle_reflexion_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_reflexion_s_3.setStatus("current")
_Letzte_gemessene_donor_sendeleistung_s_3_Type = DisplayString
_Letzte_gemessene_donor_sendeleistung_s_3_Object = MibTableColumn
letzte_gemessene_donor_sendeleistung_s_3 = _Letzte_gemessene_donor_sendeleistung_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 13),
    _Letzte_gemessene_donor_sendeleistung_s_3_Type()
)
letzte_gemessene_donor_sendeleistung_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    letzte_gemessene_donor_sendeleistung_s_3.setStatus("current")
_Aktuelle_donor_sendeleistung_s_3_Type = DisplayString
_Aktuelle_donor_sendeleistung_s_3_Object = MibTableColumn
aktuelle_donor_sendeleistung_s_3 = _Aktuelle_donor_sendeleistung_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 14),
    _Aktuelle_donor_sendeleistung_s_3_Type()
)
aktuelle_donor_sendeleistung_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_donor_sendeleistung_s_3.setStatus("current")
_Letzte_gemessene_donor_reflexion_s_3_Type = DisplayString
_Letzte_gemessene_donor_reflexion_s_3_Object = MibTableColumn
letzte_gemessene_donor_reflexion_s_3 = _Letzte_gemessene_donor_reflexion_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 15),
    _Letzte_gemessene_donor_reflexion_s_3_Type()
)
letzte_gemessene_donor_reflexion_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    letzte_gemessene_donor_reflexion_s_3.setStatus("current")
_Aktuelle_donor_reflexion_s_3_Type = DisplayString
_Aktuelle_donor_reflexion_s_3_Object = MibTableColumn
aktuelle_donor_reflexion_s_3 = _Aktuelle_donor_reflexion_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 16),
    _Aktuelle_donor_reflexion_s_3_Type()
)
aktuelle_donor_reflexion_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_donor_reflexion_s_3.setStatus("current")
_Anzahl_gemessener_praesenzsignale_im_testmode_s_3_Type = DisplayString
_Anzahl_gemessener_praesenzsignale_im_testmode_s_3_Object = MibTableColumn
anzahl_gemessener_praesenzsignale_im_testmode_s_3 = _Anzahl_gemessener_praesenzsignale_im_testmode_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 18),
    _Anzahl_gemessener_praesenzsignale_im_testmode_s_3_Type()
)
anzahl_gemessener_praesenzsignale_im_testmode_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anzahl_gemessener_praesenzsignale_im_testmode_s_3.setStatus("current")
_Aktuelle_ausgangsspannung_ub_s_3_Type = DisplayString
_Aktuelle_ausgangsspannung_ub_s_3_Object = MibTableColumn
aktuelle_ausgangsspannung_ub_s_3 = _Aktuelle_ausgangsspannung_ub_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 19),
    _Aktuelle_ausgangsspannung_ub_s_3_Type()
)
aktuelle_ausgangsspannung_ub_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_ub_s_3.setStatus("current")
_Aktuelle_ausgangsspannung_u1_s_3_Type = DisplayString
_Aktuelle_ausgangsspannung_u1_s_3_Object = MibTableColumn
aktuelle_ausgangsspannung_u1_s_3 = _Aktuelle_ausgangsspannung_u1_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 20),
    _Aktuelle_ausgangsspannung_u1_s_3_Type()
)
aktuelle_ausgangsspannung_u1_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u1_s_3.setStatus("current")
_Aktuelle_ausgangsspannung_u2_s_3_Type = DisplayString
_Aktuelle_ausgangsspannung_u2_s_3_Object = MibTableColumn
aktuelle_ausgangsspannung_u2_s_3 = _Aktuelle_ausgangsspannung_u2_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 21),
    _Aktuelle_ausgangsspannung_u2_s_3_Type()
)
aktuelle_ausgangsspannung_u2_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u2_s_3.setStatus("current")
_Aktuelle_ausgangsspannung_u3_s_3_Type = DisplayString
_Aktuelle_ausgangsspannung_u3_s_3_Object = MibTableColumn
aktuelle_ausgangsspannung_u3_s_3 = _Aktuelle_ausgangsspannung_u3_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 22),
    _Aktuelle_ausgangsspannung_u3_s_3_Type()
)
aktuelle_ausgangsspannung_u3_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u3_s_3.setStatus("current")
_Aktuelle_ausgangsspannung_u4_s_3_Type = DisplayString
_Aktuelle_ausgangsspannung_u4_s_3_Object = MibTableColumn
aktuelle_ausgangsspannung_u4_s_3 = _Aktuelle_ausgangsspannung_u4_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 23),
    _Aktuelle_ausgangsspannung_u4_s_3_Type()
)
aktuelle_ausgangsspannung_u4_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u4_s_3.setStatus("current")
_Aktuelle_ausgangsspannung_u5_s_3_Type = DisplayString
_Aktuelle_ausgangsspannung_u5_s_3_Object = MibTableColumn
aktuelle_ausgangsspannung_u5_s_3 = _Aktuelle_ausgangsspannung_u5_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 24),
    _Aktuelle_ausgangsspannung_u5_s_3_Type()
)
aktuelle_ausgangsspannung_u5_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u5_s_3.setStatus("current")
_Aktuelle_ausgangsspannung_u6_s_3_Type = DisplayString
_Aktuelle_ausgangsspannung_u6_s_3_Object = MibTableColumn
aktuelle_ausgangsspannung_u6_s_3 = _Aktuelle_ausgangsspannung_u6_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 25),
    _Aktuelle_ausgangsspannung_u6_s_3_Type()
)
aktuelle_ausgangsspannung_u6_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u6_s_3.setStatus("current")
_Aktuelle_ausgangsspannung_u7_s_3_Type = DisplayString
_Aktuelle_ausgangsspannung_u7_s_3_Object = MibTableColumn
aktuelle_ausgangsspannung_u7_s_3 = _Aktuelle_ausgangsspannung_u7_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 26),
    _Aktuelle_ausgangsspannung_u7_s_3_Type()
)
aktuelle_ausgangsspannung_u7_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u7_s_3.setStatus("current")
_Aktuelle_ausgangsspannung_u8_s_3_Type = DisplayString
_Aktuelle_ausgangsspannung_u8_s_3_Object = MibTableColumn
aktuelle_ausgangsspannung_u8_s_3 = _Aktuelle_ausgangsspannung_u8_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 27),
    _Aktuelle_ausgangsspannung_u8_s_3_Type()
)
aktuelle_ausgangsspannung_u8_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u8_s_3.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_1_s_3_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_1_s_3_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_1_s_3 = _Aktuelle_ladespannung_an_akku_kreis_1_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 28),
    _Aktuelle_ladespannung_an_akku_kreis_1_s_3_Type()
)
aktuelle_ladespannung_an_akku_kreis_1_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_1_s_3.setStatus("current")
_Aktuelle_ladespannung_an_akku_Kreis_2_s_3_Type = DisplayString
_Aktuelle_ladespannung_an_akku_Kreis_2_s_3_Object = MibTableColumn
aktuelle_ladespannung_an_akku_Kreis_2_s_3 = _Aktuelle_ladespannung_an_akku_Kreis_2_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 29),
    _Aktuelle_ladespannung_an_akku_Kreis_2_s_3_Type()
)
aktuelle_ladespannung_an_akku_Kreis_2_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_Kreis_2_s_3.setStatus("current")
_Aktuelle_ladespannung_an_akku_Kreis_3_s_3_Type = DisplayString
_Aktuelle_ladespannung_an_akku_Kreis_3_s_3_Object = MibTableColumn
aktuelle_ladespannung_an_akku_Kreis_3_s_3 = _Aktuelle_ladespannung_an_akku_Kreis_3_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 30),
    _Aktuelle_ladespannung_an_akku_Kreis_3_s_3_Type()
)
aktuelle_ladespannung_an_akku_Kreis_3_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_Kreis_3_s_3.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_4_s_3_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_4_s_3_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_4_s_3 = _Aktuelle_ladespannung_an_akku_kreis_4_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 31),
    _Aktuelle_ladespannung_an_akku_kreis_4_s_3_Type()
)
aktuelle_ladespannung_an_akku_kreis_4_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_4_s_3.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_5_s_3_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_5_s_3_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_5_s_3 = _Aktuelle_ladespannung_an_akku_kreis_5_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 32),
    _Aktuelle_ladespannung_an_akku_kreis_5_s_3_Type()
)
aktuelle_ladespannung_an_akku_kreis_5_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_5_s_3.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_6_s_3_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_6_s_3_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_6_s_3 = _Aktuelle_ladespannung_an_akku_kreis_6_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 33),
    _Aktuelle_ladespannung_an_akku_kreis_6_s_3_Type()
)
aktuelle_ladespannung_an_akku_kreis_6_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_6_s_3.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_7_s_3_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_7_s_3_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_7_s_3 = _Aktuelle_ladespannung_an_akku_kreis_7_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 34),
    _Aktuelle_ladespannung_an_akku_kreis_7_s_3_Type()
)
aktuelle_ladespannung_an_akku_kreis_7_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_7_s_3.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_8_s_3_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_8_s_3_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_8_s_3 = _Aktuelle_ladespannung_an_akku_kreis_8_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 35),
    _Aktuelle_ladespannung_an_akku_kreis_8_s_3_Type()
)
aktuelle_ladespannung_an_akku_kreis_8_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_8_s_3.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_1_s_3_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_1_s_3_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_1_s_3 = _Aktuelle_spannung_an_akku_kreis_1_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 36),
    _Aktuelle_spannung_an_akku_kreis_1_s_3_Type()
)
aktuelle_spannung_an_akku_kreis_1_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_1_s_3.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_2_s_3_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_2_s_3_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_2_s_3 = _Aktuelle_spannung_an_akku_kreis_2_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 37),
    _Aktuelle_spannung_an_akku_kreis_2_s_3_Type()
)
aktuelle_spannung_an_akku_kreis_2_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_2_s_3.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_3_s_3_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_3_s_3_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_3_s_3 = _Aktuelle_spannung_an_akku_kreis_3_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 38),
    _Aktuelle_spannung_an_akku_kreis_3_s_3_Type()
)
aktuelle_spannung_an_akku_kreis_3_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_3_s_3.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_4_s_3_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_4_s_3_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_4_s_3 = _Aktuelle_spannung_an_akku_kreis_4_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 39),
    _Aktuelle_spannung_an_akku_kreis_4_s_3_Type()
)
aktuelle_spannung_an_akku_kreis_4_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_4_s_3.setStatus("current")
_Aktuelle_spannung_an_akku_reis_5_s_3_Type = DisplayString
_Aktuelle_spannung_an_akku_reis_5_s_3_Object = MibTableColumn
aktuelle_spannung_an_akku_reis_5_s_3 = _Aktuelle_spannung_an_akku_reis_5_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 40),
    _Aktuelle_spannung_an_akku_reis_5_s_3_Type()
)
aktuelle_spannung_an_akku_reis_5_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_reis_5_s_3.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_6_s_3_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_6_s_3_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_6_s_3 = _Aktuelle_spannung_an_akku_kreis_6_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 41),
    _Aktuelle_spannung_an_akku_kreis_6_s_3_Type()
)
aktuelle_spannung_an_akku_kreis_6_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_6_s_3.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_7_s_3_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_7_s_3_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_7_s_3 = _Aktuelle_spannung_an_akku_kreis_7_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 42),
    _Aktuelle_spannung_an_akku_kreis_7_s_3_Type()
)
aktuelle_spannung_an_akku_kreis_7_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_7_s_3.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_8_s_3_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_8_s_3_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_8_s_3 = _Aktuelle_spannung_an_akku_kreis_8_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 43),
    _Aktuelle_spannung_an_akku_kreis_8_s_3_Type()
)
aktuelle_spannung_an_akku_kreis_8_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_8_s_3.setStatus("current")
_Testergebnis_lastspannung_an_akku_reis_1_s_3_Type = DisplayString
_Testergebnis_lastspannung_an_akku_reis_1_s_3_Object = MibTableColumn
testergebnis_lastspannung_an_akku_reis_1_s_3 = _Testergebnis_lastspannung_an_akku_reis_1_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 44),
    _Testergebnis_lastspannung_an_akku_reis_1_s_3_Type()
)
testergebnis_lastspannung_an_akku_reis_1_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_reis_1_s_3.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_2_s_3_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_2_s_3_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_2_s_3 = _Testergebnis_lastspannung_an_akku_kreis_2_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 45),
    _Testergebnis_lastspannung_an_akku_kreis_2_s_3_Type()
)
testergebnis_lastspannung_an_akku_kreis_2_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_2_s_3.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_3_s_3_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_3_s_3_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_3_s_3 = _Testergebnis_lastspannung_an_akku_kreis_3_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 46),
    _Testergebnis_lastspannung_an_akku_kreis_3_s_3_Type()
)
testergebnis_lastspannung_an_akku_kreis_3_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_3_s_3.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_4_s_3_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_4_s_3_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_4_s_3 = _Testergebnis_lastspannung_an_akku_kreis_4_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 47),
    _Testergebnis_lastspannung_an_akku_kreis_4_s_3_Type()
)
testergebnis_lastspannung_an_akku_kreis_4_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_4_s_3.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_5_s_3_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_5_s_3_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_5_s_3 = _Testergebnis_lastspannung_an_akku_kreis_5_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 48),
    _Testergebnis_lastspannung_an_akku_kreis_5_s_3_Type()
)
testergebnis_lastspannung_an_akku_kreis_5_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_5_s_3.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_6_s_3_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_6_s_3_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_6_s_3 = _Testergebnis_lastspannung_an_akku_kreis_6_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 49),
    _Testergebnis_lastspannung_an_akku_kreis_6_s_3_Type()
)
testergebnis_lastspannung_an_akku_kreis_6_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_6_s_3.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_7_s_3_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_7_s_3_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_7_s_3 = _Testergebnis_lastspannung_an_akku_kreis_7_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 50),
    _Testergebnis_lastspannung_an_akku_kreis_7_s_3_Type()
)
testergebnis_lastspannung_an_akku_kreis_7_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_7_s_3.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_8_s_3_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_8_s_3_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_8_s_3 = _Testergebnis_lastspannung_an_akku_kreis_8_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 51),
    _Testergebnis_lastspannung_an_akku_kreis_8_s_3_Type()
)
testergebnis_lastspannung_an_akku_kreis_8_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_8_s_3.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_1_s_3_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_1_s_3_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_1_s_3 = _Testergebnis_innenwiderstand_akku_kreis_1_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 52),
    _Testergebnis_innenwiderstand_akku_kreis_1_s_3_Type()
)
testergebnis_innenwiderstand_akku_kreis_1_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_1_s_3.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_2_s_3_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_2_s_3_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_2_s_3 = _Testergebnis_innenwiderstand_akku_kreis_2_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 53),
    _Testergebnis_innenwiderstand_akku_kreis_2_s_3_Type()
)
testergebnis_innenwiderstand_akku_kreis_2_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_2_s_3.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_3_s_3_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_3_s_3_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_3_s_3 = _Testergebnis_innenwiderstand_akku_kreis_3_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 54),
    _Testergebnis_innenwiderstand_akku_kreis_3_s_3_Type()
)
testergebnis_innenwiderstand_akku_kreis_3_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_3_s_3.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_4_s_3_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_4_s_3_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_4_s_3 = _Testergebnis_innenwiderstand_akku_kreis_4_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 56),
    _Testergebnis_innenwiderstand_akku_kreis_4_s_3_Type()
)
testergebnis_innenwiderstand_akku_kreis_4_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_4_s_3.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_5_s_3_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_5_s_3_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_5_s_3 = _Testergebnis_innenwiderstand_akku_kreis_5_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 57),
    _Testergebnis_innenwiderstand_akku_kreis_5_s_3_Type()
)
testergebnis_innenwiderstand_akku_kreis_5_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_5_s_3.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_6_s_3_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_6_s_3_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_6_s_3 = _Testergebnis_innenwiderstand_akku_kreis_6_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 58),
    _Testergebnis_innenwiderstand_akku_kreis_6_s_3_Type()
)
testergebnis_innenwiderstand_akku_kreis_6_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_6_s_3.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_7_s_3_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_7_s_3_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_7_s_3 = _Testergebnis_innenwiderstand_akku_kreis_7_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 59),
    _Testergebnis_innenwiderstand_akku_kreis_7_s_3_Type()
)
testergebnis_innenwiderstand_akku_kreis_7_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_7_s_3.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_8_s_3_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_8_s_3_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_8_s_3 = _Testergebnis_innenwiderstand_akku_kreis_8_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 60),
    _Testergebnis_innenwiderstand_akku_kreis_8_s_3_Type()
)
testergebnis_innenwiderstand_akku_kreis_8_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_8_s_3.setStatus("current")
_Netzteilspannung_uin1_s_3_Type = DisplayString
_Netzteilspannung_uin1_s_3_Object = MibTableColumn
netzteilspannung_uin1_s_3 = _Netzteilspannung_uin1_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 61),
    _Netzteilspannung_uin1_s_3_Type()
)
netzteilspannung_uin1_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzteilspannung_uin1_s_3.setStatus("current")
_Netzteilspannung_uin2_s_3_Type = DisplayString
_Netzteilspannung_uin2_s_3_Object = MibTableColumn
netzteilspannung_uin2_s_3 = _Netzteilspannung_uin2_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 62),
    _Netzteilspannung_uin2_s_3_Type()
)
netzteilspannung_uin2_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzteilspannung_uin2_s_3.setStatus("current")
_Programmierte_minimale_soll_sendeleistung_s_3_Type = DisplayString
_Programmierte_minimale_soll_sendeleistung_s_3_Object = MibTableColumn
programmierte_minimale_soll_sendeleistung_s_3 = _Programmierte_minimale_soll_sendeleistung_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 63),
    _Programmierte_minimale_soll_sendeleistung_s_3_Type()
)
programmierte_minimale_soll_sendeleistung_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programmierte_minimale_soll_sendeleistung_s_3.setStatus("current")
_Programmierte_maximale_antennen_reflexion_s_3_Type = DisplayString
_Programmierte_maximale_antennen_reflexion_s_3_Object = MibTableColumn
programmierte_maximale_antennen_reflexion_s_3 = _Programmierte_maximale_antennen_reflexion_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 64),
    _Programmierte_maximale_antennen_reflexion_s_3_Type()
)
programmierte_maximale_antennen_reflexion_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programmierte_maximale_antennen_reflexion_s_3.setStatus("current")
_Programmierte_minimale_anzahl_praesenzsignale_s_3_Type = DisplayString
_Programmierte_minimale_anzahl_praesenzsignale_s_3_Object = MibTableColumn
programmierte_minimale_anzahl_praesenzsignale_s_3 = _Programmierte_minimale_anzahl_praesenzsignale_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 65),
    _Programmierte_minimale_anzahl_praesenzsignale_s_3_Type()
)
programmierte_minimale_anzahl_praesenzsignale_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programmierte_minimale_anzahl_praesenzsignale_s_3.setStatus("current")
_Summen_fehlerstatus_von_tmoa_anlage_s_3_Type = DisplayString
_Summen_fehlerstatus_von_tmoa_anlage_s_3_Object = MibTableColumn
summen_fehlerstatus_von_tmoa_anlage_s_3 = _Summen_fehlerstatus_von_tmoa_anlage_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 66),
    _Summen_fehlerstatus_von_tmoa_anlage_s_3_Type()
)
summen_fehlerstatus_von_tmoa_anlage_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summen_fehlerstatus_von_tmoa_anlage_s_3.setStatus("current")
_Summen_fehlerstatus_von_anbinderepeater_s_3_Type = DisplayString
_Summen_fehlerstatus_von_anbinderepeater_s_3_Object = MibTableColumn
summen_fehlerstatus_von_anbinderepeater_s_3 = _Summen_fehlerstatus_von_anbinderepeater_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 67),
    _Summen_fehlerstatus_von_anbinderepeater_s_3_Type()
)
summen_fehlerstatus_von_anbinderepeater_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summen_fehlerstatus_von_anbinderepeater_s_3.setStatus("current")
_Summen_fehlerstatus_von_analogem_repeater_s_3_Type = DisplayString
_Summen_fehlerstatus_von_analogem_repeater_s_3_Object = MibTableColumn
summen_fehlerstatus_von_analogem_repeater_s_3 = _Summen_fehlerstatus_von_analogem_repeater_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 68),
    _Summen_fehlerstatus_von_analogem_repeater_s_3_Type()
)
summen_fehlerstatus_von_analogem_repeater_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summen_fehlerstatus_von_analogem_repeater_s_3.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_3_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_3_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_3 = _Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 69),
    _Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_3_Type()
)
aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_3.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_3_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_3_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_3 = _Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 70),
    _Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_3_Type()
)
aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_3.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_3_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_3_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_3 = _Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 71),
    _Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_3_Type()
)
aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_3.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_3_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_3_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_3 = _Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 72),
    _Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_3_Type()
)
aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_3.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_3_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_3_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_3 = _Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 73),
    _Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_3_Type()
)
aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_3.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_3_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_3_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_3 = _Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 74),
    _Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_3_Type()
)
aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_3.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_3_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_3_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_3 = _Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 75),
    _Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_3_Type()
)
aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_3.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_3_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_3_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_3 = _Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 76),
    _Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_3_Type()
)
aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_3.setStatus("current")
_Netzspannungsversorgung_von_tmoa_anlage_s_3_Type = DisplayString
_Netzspannungsversorgung_von_tmoa_anlage_s_3_Object = MibTableColumn
netzspannungsversorgung_von_tmoa_anlage_s_3 = _Netzspannungsversorgung_von_tmoa_anlage_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 77),
    _Netzspannungsversorgung_von_tmoa_anlage_s_3_Type()
)
netzspannungsversorgung_von_tmoa_anlage_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzspannungsversorgung_von_tmoa_anlage_s_3.setStatus("current")
_Netzspannungsversorgung_von_anbinderepeater_s_3_Type = DisplayString
_Netzspannungsversorgung_von_anbinderepeater_s_3_Object = MibTableColumn
netzspannungsversorgung_von_anbinderepeater_s_3 = _Netzspannungsversorgung_von_anbinderepeater_s_3_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 1, 1, 78),
    _Netzspannungsversorgung_von_anbinderepeater_s_3_Type()
)
netzspannungsversorgung_von_anbinderepeater_s_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzspannungsversorgung_von_anbinderepeater_s_3.setStatus("current")
_Ak_slave_4_i_ObjectIdentity = ObjectIdentity
ak_slave_4_i = _Ak_slave_4_i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4)
)
_ModulTable_s_4_Object = MibTable
modulTable_s_4 = _ModulTable_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1)
)
if mibBuilder.loadTexts:
    modulTable_s_4.setStatus("current")
_ModulEntry_s_4_Object = MibTableRow
modulEntry_s_4 = _ModulEntry_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1)
)
modulEntry_s_4.setIndexNames(
    (0, "AK-FUNKTECHNIK-MIB", "modulIndex-s-4"),
)
if mibBuilder.loadTexts:
    modulEntry_s_4.setStatus("current")
_ModulIndex_s_4_Type = DisplayString
_ModulIndex_s_4_Object = MibTableColumn
modulIndex_s_4 = _ModulIndex_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 1),
    _ModulIndex_s_4_Type()
)
modulIndex_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulIndex_s_4.setStatus("current")
_Geraete_typ_s_4_Type = DisplayString
_Geraete_typ_s_4_Object = MibTableColumn
geraete_typ_s_4 = _Geraete_typ_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 2),
    _Geraete_typ_s_4_Type()
)
geraete_typ_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geraete_typ_s_4.setStatus("current")
_Betriebsstatus_s_4_Type = DisplayString
_Betriebsstatus_s_4_Object = MibTableColumn
betriebsstatus_s_4 = _Betriebsstatus_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 3),
    _Betriebsstatus_s_4_Type()
)
betriebsstatus_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    betriebsstatus_s_4.setStatus("current")
_Senderstatus_s_4_Type = DisplayString
_Senderstatus_s_4_Object = MibTableColumn
senderstatus_s_4 = _Senderstatus_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 4),
    _Senderstatus_s_4_Type()
)
senderstatus_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    senderstatus_s_4.setStatus("current")
_Fehlerstatus_s_4_Type = DisplayString
_Fehlerstatus_s_4_Object = MibTableColumn
fehlerstatus_s_4 = _Fehlerstatus_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 5),
    _Fehlerstatus_s_4_Type()
)
fehlerstatus_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fehlerstatus_s_4.setStatus("current")
_Dem_adapter_zugeordnete_funkgeraetetype_s_4_Type = DisplayString
_Dem_adapter_zugeordnete_funkgeraetetype_s_4_Object = MibTableColumn
dem_adapter_zugeordnete_funkgeraetetype_s_4 = _Dem_adapter_zugeordnete_funkgeraetetype_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 6),
    _Dem_adapter_zugeordnete_funkgeraetetype_s_4_Type()
)
dem_adapter_zugeordnete_funkgeraetetype_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dem_adapter_zugeordnete_funkgeraetetype_s_4.setStatus("current")
_Eingabe_und_anzeigemodul_s_4_Type = DisplayString
_Eingabe_und_anzeigemodul_s_4_Object = MibTableColumn
eingabe_und_anzeigemodul_s_4 = _Eingabe_und_anzeigemodul_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 7),
    _Eingabe_und_anzeigemodul_s_4_Type()
)
eingabe_und_anzeigemodul_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eingabe_und_anzeigemodul_s_4.setStatus("current")
_Mod_bus_verbindung_module_s_4_Type = DisplayString
_Mod_bus_verbindung_module_s_4_Object = MibTableColumn
mod_bus_verbindung_module_s_4 = _Mod_bus_verbindung_module_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 8),
    _Mod_bus_verbindung_module_s_4_Type()
)
mod_bus_verbindung_module_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mod_bus_verbindung_module_s_4.setStatus("current")
_Gemessene_sendeleistung_im_testmode_s_4_Type = DisplayString
_Gemessene_sendeleistung_im_testmode_s_4_Object = MibTableColumn
gemessene_sendeleistung_im_testmode_s_4 = _Gemessene_sendeleistung_im_testmode_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 9),
    _Gemessene_sendeleistung_im_testmode_s_4_Type()
)
gemessene_sendeleistung_im_testmode_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemessene_sendeleistung_im_testmode_s_4.setStatus("current")
_Aktuelle_sendeleistung_s_4_Type = DisplayString
_Aktuelle_sendeleistung_s_4_Object = MibTableColumn
aktuelle_sendeleistung_s_4 = _Aktuelle_sendeleistung_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 10),
    _Aktuelle_sendeleistung_s_4_Type()
)
aktuelle_sendeleistung_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_sendeleistung_s_4.setStatus("current")
_Gemessene_reflexion_im_testmode_s_4_Type = DisplayString
_Gemessene_reflexion_im_testmode_s_4_Object = MibTableColumn
gemessene_reflexion_im_testmode_s_4 = _Gemessene_reflexion_im_testmode_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 11),
    _Gemessene_reflexion_im_testmode_s_4_Type()
)
gemessene_reflexion_im_testmode_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemessene_reflexion_im_testmode_s_4.setStatus("current")
_Aktuelle_reflexion_s_4_Type = DisplayString
_Aktuelle_reflexion_s_4_Object = MibTableColumn
aktuelle_reflexion_s_4 = _Aktuelle_reflexion_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 12),
    _Aktuelle_reflexion_s_4_Type()
)
aktuelle_reflexion_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_reflexion_s_4.setStatus("current")
_Letzte_gemessene_donor_sendeleistung_s_4_Type = DisplayString
_Letzte_gemessene_donor_sendeleistung_s_4_Object = MibTableColumn
letzte_gemessene_donor_sendeleistung_s_4 = _Letzte_gemessene_donor_sendeleistung_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 13),
    _Letzte_gemessene_donor_sendeleistung_s_4_Type()
)
letzte_gemessene_donor_sendeleistung_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    letzte_gemessene_donor_sendeleistung_s_4.setStatus("current")
_Aktuelle_donor_sendeleistung_s_4_Type = DisplayString
_Aktuelle_donor_sendeleistung_s_4_Object = MibTableColumn
aktuelle_donor_sendeleistung_s_4 = _Aktuelle_donor_sendeleistung_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 14),
    _Aktuelle_donor_sendeleistung_s_4_Type()
)
aktuelle_donor_sendeleistung_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_donor_sendeleistung_s_4.setStatus("current")
_Letzte_gemessene_donor_reflexion_s_4_Type = DisplayString
_Letzte_gemessene_donor_reflexion_s_4_Object = MibTableColumn
letzte_gemessene_donor_reflexion_s_4 = _Letzte_gemessene_donor_reflexion_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 15),
    _Letzte_gemessene_donor_reflexion_s_4_Type()
)
letzte_gemessene_donor_reflexion_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    letzte_gemessene_donor_reflexion_s_4.setStatus("current")
_Aktuelle_donor_reflexion_s_4_Type = DisplayString
_Aktuelle_donor_reflexion_s_4_Object = MibTableColumn
aktuelle_donor_reflexion_s_4 = _Aktuelle_donor_reflexion_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 16),
    _Aktuelle_donor_reflexion_s_4_Type()
)
aktuelle_donor_reflexion_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_donor_reflexion_s_4.setStatus("current")
_Anzahl_gemessener_praesenzsignale_im_testmode_s_4_Type = DisplayString
_Anzahl_gemessener_praesenzsignale_im_testmode_s_4_Object = MibTableColumn
anzahl_gemessener_praesenzsignale_im_testmode_s_4 = _Anzahl_gemessener_praesenzsignale_im_testmode_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 18),
    _Anzahl_gemessener_praesenzsignale_im_testmode_s_4_Type()
)
anzahl_gemessener_praesenzsignale_im_testmode_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anzahl_gemessener_praesenzsignale_im_testmode_s_4.setStatus("current")
_Aktuelle_ausgangsspannung_ub_s_4_Type = DisplayString
_Aktuelle_ausgangsspannung_ub_s_4_Object = MibTableColumn
aktuelle_ausgangsspannung_ub_s_4 = _Aktuelle_ausgangsspannung_ub_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 19),
    _Aktuelle_ausgangsspannung_ub_s_4_Type()
)
aktuelle_ausgangsspannung_ub_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_ub_s_4.setStatus("current")
_Aktuelle_ausgangsspannung_u1_s_4_Type = DisplayString
_Aktuelle_ausgangsspannung_u1_s_4_Object = MibTableColumn
aktuelle_ausgangsspannung_u1_s_4 = _Aktuelle_ausgangsspannung_u1_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 20),
    _Aktuelle_ausgangsspannung_u1_s_4_Type()
)
aktuelle_ausgangsspannung_u1_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u1_s_4.setStatus("current")
_Aktuelle_ausgangsspannung_u2_s_4_Type = DisplayString
_Aktuelle_ausgangsspannung_u2_s_4_Object = MibTableColumn
aktuelle_ausgangsspannung_u2_s_4 = _Aktuelle_ausgangsspannung_u2_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 21),
    _Aktuelle_ausgangsspannung_u2_s_4_Type()
)
aktuelle_ausgangsspannung_u2_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u2_s_4.setStatus("current")
_Aktuelle_ausgangsspannung_u3_s_4_Type = DisplayString
_Aktuelle_ausgangsspannung_u3_s_4_Object = MibTableColumn
aktuelle_ausgangsspannung_u3_s_4 = _Aktuelle_ausgangsspannung_u3_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 22),
    _Aktuelle_ausgangsspannung_u3_s_4_Type()
)
aktuelle_ausgangsspannung_u3_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u3_s_4.setStatus("current")
_Aktuelle_ausgangsspannung_u4_s_4_Type = DisplayString
_Aktuelle_ausgangsspannung_u4_s_4_Object = MibTableColumn
aktuelle_ausgangsspannung_u4_s_4 = _Aktuelle_ausgangsspannung_u4_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 23),
    _Aktuelle_ausgangsspannung_u4_s_4_Type()
)
aktuelle_ausgangsspannung_u4_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u4_s_4.setStatus("current")
_Aktuelle_ausgangsspannung_u5_s_4_Type = DisplayString
_Aktuelle_ausgangsspannung_u5_s_4_Object = MibTableColumn
aktuelle_ausgangsspannung_u5_s_4 = _Aktuelle_ausgangsspannung_u5_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 24),
    _Aktuelle_ausgangsspannung_u5_s_4_Type()
)
aktuelle_ausgangsspannung_u5_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u5_s_4.setStatus("current")
_Aktuelle_ausgangsspannung_u6_s_4_Type = DisplayString
_Aktuelle_ausgangsspannung_u6_s_4_Object = MibTableColumn
aktuelle_ausgangsspannung_u6_s_4 = _Aktuelle_ausgangsspannung_u6_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 25),
    _Aktuelle_ausgangsspannung_u6_s_4_Type()
)
aktuelle_ausgangsspannung_u6_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u6_s_4.setStatus("current")
_Aktuelle_ausgangsspannung_u7_s_4_Type = DisplayString
_Aktuelle_ausgangsspannung_u7_s_4_Object = MibTableColumn
aktuelle_ausgangsspannung_u7_s_4 = _Aktuelle_ausgangsspannung_u7_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 26),
    _Aktuelle_ausgangsspannung_u7_s_4_Type()
)
aktuelle_ausgangsspannung_u7_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u7_s_4.setStatus("current")
_Aktuelle_ausgangsspannung_u8_s_4_Type = DisplayString
_Aktuelle_ausgangsspannung_u8_s_4_Object = MibTableColumn
aktuelle_ausgangsspannung_u8_s_4 = _Aktuelle_ausgangsspannung_u8_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 27),
    _Aktuelle_ausgangsspannung_u8_s_4_Type()
)
aktuelle_ausgangsspannung_u8_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u8_s_4.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_1_s_4_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_1_s_4_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_1_s_4 = _Aktuelle_ladespannung_an_akku_kreis_1_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 28),
    _Aktuelle_ladespannung_an_akku_kreis_1_s_4_Type()
)
aktuelle_ladespannung_an_akku_kreis_1_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_1_s_4.setStatus("current")
_Aktuelle_ladespannung_an_akku_Kreis_2_s_4_Type = DisplayString
_Aktuelle_ladespannung_an_akku_Kreis_2_s_4_Object = MibTableColumn
aktuelle_ladespannung_an_akku_Kreis_2_s_4 = _Aktuelle_ladespannung_an_akku_Kreis_2_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 29),
    _Aktuelle_ladespannung_an_akku_Kreis_2_s_4_Type()
)
aktuelle_ladespannung_an_akku_Kreis_2_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_Kreis_2_s_4.setStatus("current")
_Aktuelle_ladespannung_an_akku_Kreis_3_s_4_Type = DisplayString
_Aktuelle_ladespannung_an_akku_Kreis_3_s_4_Object = MibTableColumn
aktuelle_ladespannung_an_akku_Kreis_3_s_4 = _Aktuelle_ladespannung_an_akku_Kreis_3_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 30),
    _Aktuelle_ladespannung_an_akku_Kreis_3_s_4_Type()
)
aktuelle_ladespannung_an_akku_Kreis_3_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_Kreis_3_s_4.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_4_s_4_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_4_s_4_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_4_s_4 = _Aktuelle_ladespannung_an_akku_kreis_4_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 31),
    _Aktuelle_ladespannung_an_akku_kreis_4_s_4_Type()
)
aktuelle_ladespannung_an_akku_kreis_4_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_4_s_4.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_5_s_4_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_5_s_4_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_5_s_4 = _Aktuelle_ladespannung_an_akku_kreis_5_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 32),
    _Aktuelle_ladespannung_an_akku_kreis_5_s_4_Type()
)
aktuelle_ladespannung_an_akku_kreis_5_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_5_s_4.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_6_s_4_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_6_s_4_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_6_s_4 = _Aktuelle_ladespannung_an_akku_kreis_6_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 33),
    _Aktuelle_ladespannung_an_akku_kreis_6_s_4_Type()
)
aktuelle_ladespannung_an_akku_kreis_6_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_6_s_4.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_7_s_4_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_7_s_4_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_7_s_4 = _Aktuelle_ladespannung_an_akku_kreis_7_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 34),
    _Aktuelle_ladespannung_an_akku_kreis_7_s_4_Type()
)
aktuelle_ladespannung_an_akku_kreis_7_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_7_s_4.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_8_s_4_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_8_s_4_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_8_s_4 = _Aktuelle_ladespannung_an_akku_kreis_8_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 35),
    _Aktuelle_ladespannung_an_akku_kreis_8_s_4_Type()
)
aktuelle_ladespannung_an_akku_kreis_8_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_8_s_4.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_1_s_4_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_1_s_4_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_1_s_4 = _Aktuelle_spannung_an_akku_kreis_1_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 36),
    _Aktuelle_spannung_an_akku_kreis_1_s_4_Type()
)
aktuelle_spannung_an_akku_kreis_1_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_1_s_4.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_2_s_4_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_2_s_4_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_2_s_4 = _Aktuelle_spannung_an_akku_kreis_2_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 37),
    _Aktuelle_spannung_an_akku_kreis_2_s_4_Type()
)
aktuelle_spannung_an_akku_kreis_2_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_2_s_4.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_3_s_4_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_3_s_4_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_3_s_4 = _Aktuelle_spannung_an_akku_kreis_3_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 38),
    _Aktuelle_spannung_an_akku_kreis_3_s_4_Type()
)
aktuelle_spannung_an_akku_kreis_3_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_3_s_4.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_4_s_4_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_4_s_4_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_4_s_4 = _Aktuelle_spannung_an_akku_kreis_4_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 39),
    _Aktuelle_spannung_an_akku_kreis_4_s_4_Type()
)
aktuelle_spannung_an_akku_kreis_4_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_4_s_4.setStatus("current")
_Aktuelle_spannung_an_akku_reis_5_s_4_Type = DisplayString
_Aktuelle_spannung_an_akku_reis_5_s_4_Object = MibTableColumn
aktuelle_spannung_an_akku_reis_5_s_4 = _Aktuelle_spannung_an_akku_reis_5_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 40),
    _Aktuelle_spannung_an_akku_reis_5_s_4_Type()
)
aktuelle_spannung_an_akku_reis_5_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_reis_5_s_4.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_6_s_4_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_6_s_4_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_6_s_4 = _Aktuelle_spannung_an_akku_kreis_6_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 41),
    _Aktuelle_spannung_an_akku_kreis_6_s_4_Type()
)
aktuelle_spannung_an_akku_kreis_6_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_6_s_4.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_7_s_4_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_7_s_4_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_7_s_4 = _Aktuelle_spannung_an_akku_kreis_7_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 42),
    _Aktuelle_spannung_an_akku_kreis_7_s_4_Type()
)
aktuelle_spannung_an_akku_kreis_7_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_7_s_4.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_8_s_4_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_8_s_4_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_8_s_4 = _Aktuelle_spannung_an_akku_kreis_8_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 43),
    _Aktuelle_spannung_an_akku_kreis_8_s_4_Type()
)
aktuelle_spannung_an_akku_kreis_8_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_8_s_4.setStatus("current")
_Testergebnis_lastspannung_an_akku_reis_1_s_4_Type = DisplayString
_Testergebnis_lastspannung_an_akku_reis_1_s_4_Object = MibTableColumn
testergebnis_lastspannung_an_akku_reis_1_s_4 = _Testergebnis_lastspannung_an_akku_reis_1_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 44),
    _Testergebnis_lastspannung_an_akku_reis_1_s_4_Type()
)
testergebnis_lastspannung_an_akku_reis_1_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_reis_1_s_4.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_2_s_4_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_2_s_4_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_2_s_4 = _Testergebnis_lastspannung_an_akku_kreis_2_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 45),
    _Testergebnis_lastspannung_an_akku_kreis_2_s_4_Type()
)
testergebnis_lastspannung_an_akku_kreis_2_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_2_s_4.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_3_s_4_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_3_s_4_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_3_s_4 = _Testergebnis_lastspannung_an_akku_kreis_3_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 46),
    _Testergebnis_lastspannung_an_akku_kreis_3_s_4_Type()
)
testergebnis_lastspannung_an_akku_kreis_3_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_3_s_4.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_4_s_4_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_4_s_4_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_4_s_4 = _Testergebnis_lastspannung_an_akku_kreis_4_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 47),
    _Testergebnis_lastspannung_an_akku_kreis_4_s_4_Type()
)
testergebnis_lastspannung_an_akku_kreis_4_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_4_s_4.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_5_s_4_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_5_s_4_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_5_s_4 = _Testergebnis_lastspannung_an_akku_kreis_5_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 48),
    _Testergebnis_lastspannung_an_akku_kreis_5_s_4_Type()
)
testergebnis_lastspannung_an_akku_kreis_5_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_5_s_4.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_6_s_4_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_6_s_4_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_6_s_4 = _Testergebnis_lastspannung_an_akku_kreis_6_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 49),
    _Testergebnis_lastspannung_an_akku_kreis_6_s_4_Type()
)
testergebnis_lastspannung_an_akku_kreis_6_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_6_s_4.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_7_s_4_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_7_s_4_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_7_s_4 = _Testergebnis_lastspannung_an_akku_kreis_7_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 50),
    _Testergebnis_lastspannung_an_akku_kreis_7_s_4_Type()
)
testergebnis_lastspannung_an_akku_kreis_7_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_7_s_4.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_8_s_4_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_8_s_4_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_8_s_4 = _Testergebnis_lastspannung_an_akku_kreis_8_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 51),
    _Testergebnis_lastspannung_an_akku_kreis_8_s_4_Type()
)
testergebnis_lastspannung_an_akku_kreis_8_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_8_s_4.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_1_s_4_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_1_s_4_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_1_s_4 = _Testergebnis_innenwiderstand_akku_kreis_1_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 52),
    _Testergebnis_innenwiderstand_akku_kreis_1_s_4_Type()
)
testergebnis_innenwiderstand_akku_kreis_1_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_1_s_4.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_2_s_4_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_2_s_4_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_2_s_4 = _Testergebnis_innenwiderstand_akku_kreis_2_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 53),
    _Testergebnis_innenwiderstand_akku_kreis_2_s_4_Type()
)
testergebnis_innenwiderstand_akku_kreis_2_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_2_s_4.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_3_s_4_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_3_s_4_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_3_s_4 = _Testergebnis_innenwiderstand_akku_kreis_3_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 54),
    _Testergebnis_innenwiderstand_akku_kreis_3_s_4_Type()
)
testergebnis_innenwiderstand_akku_kreis_3_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_3_s_4.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_4_s_4_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_4_s_4_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_4_s_4 = _Testergebnis_innenwiderstand_akku_kreis_4_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 56),
    _Testergebnis_innenwiderstand_akku_kreis_4_s_4_Type()
)
testergebnis_innenwiderstand_akku_kreis_4_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_4_s_4.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_5_s_4_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_5_s_4_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_5_s_4 = _Testergebnis_innenwiderstand_akku_kreis_5_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 57),
    _Testergebnis_innenwiderstand_akku_kreis_5_s_4_Type()
)
testergebnis_innenwiderstand_akku_kreis_5_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_5_s_4.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_6_s_4_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_6_s_4_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_6_s_4 = _Testergebnis_innenwiderstand_akku_kreis_6_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 58),
    _Testergebnis_innenwiderstand_akku_kreis_6_s_4_Type()
)
testergebnis_innenwiderstand_akku_kreis_6_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_6_s_4.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_7_s_4_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_7_s_4_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_7_s_4 = _Testergebnis_innenwiderstand_akku_kreis_7_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 59),
    _Testergebnis_innenwiderstand_akku_kreis_7_s_4_Type()
)
testergebnis_innenwiderstand_akku_kreis_7_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_7_s_4.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_8_s_4_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_8_s_4_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_8_s_4 = _Testergebnis_innenwiderstand_akku_kreis_8_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 60),
    _Testergebnis_innenwiderstand_akku_kreis_8_s_4_Type()
)
testergebnis_innenwiderstand_akku_kreis_8_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_8_s_4.setStatus("current")
_Netzteilspannung_uin1_s_4_Type = DisplayString
_Netzteilspannung_uin1_s_4_Object = MibTableColumn
netzteilspannung_uin1_s_4 = _Netzteilspannung_uin1_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 61),
    _Netzteilspannung_uin1_s_4_Type()
)
netzteilspannung_uin1_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzteilspannung_uin1_s_4.setStatus("current")
_Netzteilspannung_uin2_s_4_Type = DisplayString
_Netzteilspannung_uin2_s_4_Object = MibTableColumn
netzteilspannung_uin2_s_4 = _Netzteilspannung_uin2_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 62),
    _Netzteilspannung_uin2_s_4_Type()
)
netzteilspannung_uin2_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzteilspannung_uin2_s_4.setStatus("current")
_Programmierte_minimale_soll_sendeleistung_s_4_Type = DisplayString
_Programmierte_minimale_soll_sendeleistung_s_4_Object = MibTableColumn
programmierte_minimale_soll_sendeleistung_s_4 = _Programmierte_minimale_soll_sendeleistung_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 63),
    _Programmierte_minimale_soll_sendeleistung_s_4_Type()
)
programmierte_minimale_soll_sendeleistung_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programmierte_minimale_soll_sendeleistung_s_4.setStatus("current")
_Programmierte_maximale_antennen_reflexion_s_4_Type = DisplayString
_Programmierte_maximale_antennen_reflexion_s_4_Object = MibTableColumn
programmierte_maximale_antennen_reflexion_s_4 = _Programmierte_maximale_antennen_reflexion_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 64),
    _Programmierte_maximale_antennen_reflexion_s_4_Type()
)
programmierte_maximale_antennen_reflexion_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programmierte_maximale_antennen_reflexion_s_4.setStatus("current")
_Programmierte_minimale_anzahl_praesenzsignale_s_4_Type = DisplayString
_Programmierte_minimale_anzahl_praesenzsignale_s_4_Object = MibTableColumn
programmierte_minimale_anzahl_praesenzsignale_s_4 = _Programmierte_minimale_anzahl_praesenzsignale_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 65),
    _Programmierte_minimale_anzahl_praesenzsignale_s_4_Type()
)
programmierte_minimale_anzahl_praesenzsignale_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programmierte_minimale_anzahl_praesenzsignale_s_4.setStatus("current")
_Summen_fehlerstatus_von_tmoa_anlage_s_4_Type = DisplayString
_Summen_fehlerstatus_von_tmoa_anlage_s_4_Object = MibTableColumn
summen_fehlerstatus_von_tmoa_anlage_s_4 = _Summen_fehlerstatus_von_tmoa_anlage_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 66),
    _Summen_fehlerstatus_von_tmoa_anlage_s_4_Type()
)
summen_fehlerstatus_von_tmoa_anlage_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summen_fehlerstatus_von_tmoa_anlage_s_4.setStatus("current")
_Summen_fehlerstatus_von_anbinderepeater_s_4_Type = DisplayString
_Summen_fehlerstatus_von_anbinderepeater_s_4_Object = MibTableColumn
summen_fehlerstatus_von_anbinderepeater_s_4 = _Summen_fehlerstatus_von_anbinderepeater_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 67),
    _Summen_fehlerstatus_von_anbinderepeater_s_4_Type()
)
summen_fehlerstatus_von_anbinderepeater_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summen_fehlerstatus_von_anbinderepeater_s_4.setStatus("current")
_Summen_fehlerstatus_von_analogem_repeater_s_4_Type = DisplayString
_Summen_fehlerstatus_von_analogem_repeater_s_4_Object = MibTableColumn
summen_fehlerstatus_von_analogem_repeater_s_4 = _Summen_fehlerstatus_von_analogem_repeater_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 68),
    _Summen_fehlerstatus_von_analogem_repeater_s_4_Type()
)
summen_fehlerstatus_von_analogem_repeater_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summen_fehlerstatus_von_analogem_repeater_s_4.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_4_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_4_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_4 = _Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 69),
    _Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_4_Type()
)
aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_4.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_4_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_4_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_4 = _Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 70),
    _Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_4_Type()
)
aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_4.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_4_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_4_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_4 = _Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 71),
    _Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_4_Type()
)
aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_4.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_4_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_4_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_4 = _Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 72),
    _Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_4_Type()
)
aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_4.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_4_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_4_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_4 = _Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 73),
    _Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_4_Type()
)
aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_4.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_4_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_4_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_4 = _Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 74),
    _Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_4_Type()
)
aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_4.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_4_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_4_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_4 = _Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 75),
    _Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_4_Type()
)
aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_4.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_4_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_4_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_4 = _Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 76),
    _Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_4_Type()
)
aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_4.setStatus("current")
_Netzspannungsversorgung_von_tmoa_anlage_s_4_Type = DisplayString
_Netzspannungsversorgung_von_tmoa_anlage_s_4_Object = MibTableColumn
netzspannungsversorgung_von_tmoa_anlage_s_4 = _Netzspannungsversorgung_von_tmoa_anlage_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 77),
    _Netzspannungsversorgung_von_tmoa_anlage_s_4_Type()
)
netzspannungsversorgung_von_tmoa_anlage_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzspannungsversorgung_von_tmoa_anlage_s_4.setStatus("current")
_Netzspannungsversorgung_von_anbinderepeater_s_4_Type = DisplayString
_Netzspannungsversorgung_von_anbinderepeater_s_4_Object = MibTableColumn
netzspannungsversorgung_von_anbinderepeater_s_4 = _Netzspannungsversorgung_von_anbinderepeater_s_4_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 1, 1, 78),
    _Netzspannungsversorgung_von_anbinderepeater_s_4_Type()
)
netzspannungsversorgung_von_anbinderepeater_s_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzspannungsversorgung_von_anbinderepeater_s_4.setStatus("current")
_Ak_slave_5_i_ObjectIdentity = ObjectIdentity
ak_slave_5_i = _Ak_slave_5_i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5)
)
_ModulTable_s_5_Object = MibTable
modulTable_s_5 = _ModulTable_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1)
)
if mibBuilder.loadTexts:
    modulTable_s_5.setStatus("current")
_ModulEntry_s_5_Object = MibTableRow
modulEntry_s_5 = _ModulEntry_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1)
)
modulEntry_s_5.setIndexNames(
    (0, "AK-FUNKTECHNIK-MIB", "modulIndex-s-5"),
)
if mibBuilder.loadTexts:
    modulEntry_s_5.setStatus("current")
_ModulIndex_s_5_Type = DisplayString
_ModulIndex_s_5_Object = MibTableColumn
modulIndex_s_5 = _ModulIndex_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 1),
    _ModulIndex_s_5_Type()
)
modulIndex_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulIndex_s_5.setStatus("current")
_Geraete_typ_s_5_Type = DisplayString
_Geraete_typ_s_5_Object = MibTableColumn
geraete_typ_s_5 = _Geraete_typ_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 2),
    _Geraete_typ_s_5_Type()
)
geraete_typ_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geraete_typ_s_5.setStatus("current")
_Betriebsstatus_s_5_Type = DisplayString
_Betriebsstatus_s_5_Object = MibTableColumn
betriebsstatus_s_5 = _Betriebsstatus_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 3),
    _Betriebsstatus_s_5_Type()
)
betriebsstatus_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    betriebsstatus_s_5.setStatus("current")
_Senderstatus_s_5_Type = DisplayString
_Senderstatus_s_5_Object = MibTableColumn
senderstatus_s_5 = _Senderstatus_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 4),
    _Senderstatus_s_5_Type()
)
senderstatus_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    senderstatus_s_5.setStatus("current")
_Fehlerstatus_s_5_Type = DisplayString
_Fehlerstatus_s_5_Object = MibTableColumn
fehlerstatus_s_5 = _Fehlerstatus_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 5),
    _Fehlerstatus_s_5_Type()
)
fehlerstatus_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fehlerstatus_s_5.setStatus("current")
_Dem_adapter_zugeordnete_funkgeraetetype_s_5_Type = DisplayString
_Dem_adapter_zugeordnete_funkgeraetetype_s_5_Object = MibTableColumn
dem_adapter_zugeordnete_funkgeraetetype_s_5 = _Dem_adapter_zugeordnete_funkgeraetetype_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 6),
    _Dem_adapter_zugeordnete_funkgeraetetype_s_5_Type()
)
dem_adapter_zugeordnete_funkgeraetetype_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dem_adapter_zugeordnete_funkgeraetetype_s_5.setStatus("current")
_Eingabe_und_anzeigemodul_s_5_Type = DisplayString
_Eingabe_und_anzeigemodul_s_5_Object = MibTableColumn
eingabe_und_anzeigemodul_s_5 = _Eingabe_und_anzeigemodul_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 7),
    _Eingabe_und_anzeigemodul_s_5_Type()
)
eingabe_und_anzeigemodul_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eingabe_und_anzeigemodul_s_5.setStatus("current")
_Mod_bus_verbindung_module_s_5_Type = DisplayString
_Mod_bus_verbindung_module_s_5_Object = MibTableColumn
mod_bus_verbindung_module_s_5 = _Mod_bus_verbindung_module_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 8),
    _Mod_bus_verbindung_module_s_5_Type()
)
mod_bus_verbindung_module_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mod_bus_verbindung_module_s_5.setStatus("current")
_Gemessene_sendeleistung_im_testmode_s_5_Type = DisplayString
_Gemessene_sendeleistung_im_testmode_s_5_Object = MibTableColumn
gemessene_sendeleistung_im_testmode_s_5 = _Gemessene_sendeleistung_im_testmode_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 9),
    _Gemessene_sendeleistung_im_testmode_s_5_Type()
)
gemessene_sendeleistung_im_testmode_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemessene_sendeleistung_im_testmode_s_5.setStatus("current")
_Aktuelle_sendeleistung_s_5_Type = DisplayString
_Aktuelle_sendeleistung_s_5_Object = MibTableColumn
aktuelle_sendeleistung_s_5 = _Aktuelle_sendeleistung_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 10),
    _Aktuelle_sendeleistung_s_5_Type()
)
aktuelle_sendeleistung_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_sendeleistung_s_5.setStatus("current")
_Gemessene_reflexion_im_testmode_s_5_Type = DisplayString
_Gemessene_reflexion_im_testmode_s_5_Object = MibTableColumn
gemessene_reflexion_im_testmode_s_5 = _Gemessene_reflexion_im_testmode_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 11),
    _Gemessene_reflexion_im_testmode_s_5_Type()
)
gemessene_reflexion_im_testmode_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemessene_reflexion_im_testmode_s_5.setStatus("current")
_Aktuelle_reflexion_s_5_Type = DisplayString
_Aktuelle_reflexion_s_5_Object = MibTableColumn
aktuelle_reflexion_s_5 = _Aktuelle_reflexion_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 12),
    _Aktuelle_reflexion_s_5_Type()
)
aktuelle_reflexion_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_reflexion_s_5.setStatus("current")
_Letzte_gemessene_donor_sendeleistung_s_5_Type = DisplayString
_Letzte_gemessene_donor_sendeleistung_s_5_Object = MibTableColumn
letzte_gemessene_donor_sendeleistung_s_5 = _Letzte_gemessene_donor_sendeleistung_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 13),
    _Letzte_gemessene_donor_sendeleistung_s_5_Type()
)
letzte_gemessene_donor_sendeleistung_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    letzte_gemessene_donor_sendeleistung_s_5.setStatus("current")
_Aktuelle_donor_sendeleistung_s_5_Type = DisplayString
_Aktuelle_donor_sendeleistung_s_5_Object = MibTableColumn
aktuelle_donor_sendeleistung_s_5 = _Aktuelle_donor_sendeleistung_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 14),
    _Aktuelle_donor_sendeleistung_s_5_Type()
)
aktuelle_donor_sendeleistung_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_donor_sendeleistung_s_5.setStatus("current")
_Letzte_gemessene_donor_reflexion_s_5_Type = DisplayString
_Letzte_gemessene_donor_reflexion_s_5_Object = MibTableColumn
letzte_gemessene_donor_reflexion_s_5 = _Letzte_gemessene_donor_reflexion_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 15),
    _Letzte_gemessene_donor_reflexion_s_5_Type()
)
letzte_gemessene_donor_reflexion_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    letzte_gemessene_donor_reflexion_s_5.setStatus("current")
_Aktuelle_donor_reflexion_s_5_Type = DisplayString
_Aktuelle_donor_reflexion_s_5_Object = MibTableColumn
aktuelle_donor_reflexion_s_5 = _Aktuelle_donor_reflexion_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 16),
    _Aktuelle_donor_reflexion_s_5_Type()
)
aktuelle_donor_reflexion_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_donor_reflexion_s_5.setStatus("current")
_Anzahl_gemessener_praesenzsignale_im_testmode_s_5_Type = DisplayString
_Anzahl_gemessener_praesenzsignale_im_testmode_s_5_Object = MibTableColumn
anzahl_gemessener_praesenzsignale_im_testmode_s_5 = _Anzahl_gemessener_praesenzsignale_im_testmode_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 18),
    _Anzahl_gemessener_praesenzsignale_im_testmode_s_5_Type()
)
anzahl_gemessener_praesenzsignale_im_testmode_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anzahl_gemessener_praesenzsignale_im_testmode_s_5.setStatus("current")
_Aktuelle_ausgangsspannung_ub_s_5_Type = DisplayString
_Aktuelle_ausgangsspannung_ub_s_5_Object = MibTableColumn
aktuelle_ausgangsspannung_ub_s_5 = _Aktuelle_ausgangsspannung_ub_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 19),
    _Aktuelle_ausgangsspannung_ub_s_5_Type()
)
aktuelle_ausgangsspannung_ub_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_ub_s_5.setStatus("current")
_Aktuelle_ausgangsspannung_u1_s_5_Type = DisplayString
_Aktuelle_ausgangsspannung_u1_s_5_Object = MibTableColumn
aktuelle_ausgangsspannung_u1_s_5 = _Aktuelle_ausgangsspannung_u1_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 20),
    _Aktuelle_ausgangsspannung_u1_s_5_Type()
)
aktuelle_ausgangsspannung_u1_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u1_s_5.setStatus("current")
_Aktuelle_ausgangsspannung_u2_s_5_Type = DisplayString
_Aktuelle_ausgangsspannung_u2_s_5_Object = MibTableColumn
aktuelle_ausgangsspannung_u2_s_5 = _Aktuelle_ausgangsspannung_u2_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 21),
    _Aktuelle_ausgangsspannung_u2_s_5_Type()
)
aktuelle_ausgangsspannung_u2_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u2_s_5.setStatus("current")
_Aktuelle_ausgangsspannung_u3_s_5_Type = DisplayString
_Aktuelle_ausgangsspannung_u3_s_5_Object = MibTableColumn
aktuelle_ausgangsspannung_u3_s_5 = _Aktuelle_ausgangsspannung_u3_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 22),
    _Aktuelle_ausgangsspannung_u3_s_5_Type()
)
aktuelle_ausgangsspannung_u3_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u3_s_5.setStatus("current")
_Aktuelle_ausgangsspannung_u4_s_5_Type = DisplayString
_Aktuelle_ausgangsspannung_u4_s_5_Object = MibTableColumn
aktuelle_ausgangsspannung_u4_s_5 = _Aktuelle_ausgangsspannung_u4_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 23),
    _Aktuelle_ausgangsspannung_u4_s_5_Type()
)
aktuelle_ausgangsspannung_u4_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u4_s_5.setStatus("current")
_Aktuelle_ausgangsspannung_u5_s_5_Type = DisplayString
_Aktuelle_ausgangsspannung_u5_s_5_Object = MibTableColumn
aktuelle_ausgangsspannung_u5_s_5 = _Aktuelle_ausgangsspannung_u5_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 24),
    _Aktuelle_ausgangsspannung_u5_s_5_Type()
)
aktuelle_ausgangsspannung_u5_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u5_s_5.setStatus("current")
_Aktuelle_ausgangsspannung_u6_s_5_Type = DisplayString
_Aktuelle_ausgangsspannung_u6_s_5_Object = MibTableColumn
aktuelle_ausgangsspannung_u6_s_5 = _Aktuelle_ausgangsspannung_u6_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 25),
    _Aktuelle_ausgangsspannung_u6_s_5_Type()
)
aktuelle_ausgangsspannung_u6_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u6_s_5.setStatus("current")
_Aktuelle_ausgangsspannung_u7_s_5_Type = DisplayString
_Aktuelle_ausgangsspannung_u7_s_5_Object = MibTableColumn
aktuelle_ausgangsspannung_u7_s_5 = _Aktuelle_ausgangsspannung_u7_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 26),
    _Aktuelle_ausgangsspannung_u7_s_5_Type()
)
aktuelle_ausgangsspannung_u7_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u7_s_5.setStatus("current")
_Aktuelle_ausgangsspannung_u8_s_5_Type = DisplayString
_Aktuelle_ausgangsspannung_u8_s_5_Object = MibTableColumn
aktuelle_ausgangsspannung_u8_s_5 = _Aktuelle_ausgangsspannung_u8_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 27),
    _Aktuelle_ausgangsspannung_u8_s_5_Type()
)
aktuelle_ausgangsspannung_u8_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u8_s_5.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_1_s_5_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_1_s_5_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_1_s_5 = _Aktuelle_ladespannung_an_akku_kreis_1_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 28),
    _Aktuelle_ladespannung_an_akku_kreis_1_s_5_Type()
)
aktuelle_ladespannung_an_akku_kreis_1_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_1_s_5.setStatus("current")
_Aktuelle_ladespannung_an_akku_Kreis_2_s_5_Type = DisplayString
_Aktuelle_ladespannung_an_akku_Kreis_2_s_5_Object = MibTableColumn
aktuelle_ladespannung_an_akku_Kreis_2_s_5 = _Aktuelle_ladespannung_an_akku_Kreis_2_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 29),
    _Aktuelle_ladespannung_an_akku_Kreis_2_s_5_Type()
)
aktuelle_ladespannung_an_akku_Kreis_2_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_Kreis_2_s_5.setStatus("current")
_Aktuelle_ladespannung_an_akku_Kreis_3_s_5_Type = DisplayString
_Aktuelle_ladespannung_an_akku_Kreis_3_s_5_Object = MibTableColumn
aktuelle_ladespannung_an_akku_Kreis_3_s_5 = _Aktuelle_ladespannung_an_akku_Kreis_3_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 30),
    _Aktuelle_ladespannung_an_akku_Kreis_3_s_5_Type()
)
aktuelle_ladespannung_an_akku_Kreis_3_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_Kreis_3_s_5.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_4_s_5_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_4_s_5_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_4_s_5 = _Aktuelle_ladespannung_an_akku_kreis_4_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 31),
    _Aktuelle_ladespannung_an_akku_kreis_4_s_5_Type()
)
aktuelle_ladespannung_an_akku_kreis_4_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_4_s_5.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_5_s_5_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_5_s_5_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_5_s_5 = _Aktuelle_ladespannung_an_akku_kreis_5_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 32),
    _Aktuelle_ladespannung_an_akku_kreis_5_s_5_Type()
)
aktuelle_ladespannung_an_akku_kreis_5_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_5_s_5.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_6_s_5_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_6_s_5_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_6_s_5 = _Aktuelle_ladespannung_an_akku_kreis_6_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 33),
    _Aktuelle_ladespannung_an_akku_kreis_6_s_5_Type()
)
aktuelle_ladespannung_an_akku_kreis_6_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_6_s_5.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_7_s_5_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_7_s_5_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_7_s_5 = _Aktuelle_ladespannung_an_akku_kreis_7_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 34),
    _Aktuelle_ladespannung_an_akku_kreis_7_s_5_Type()
)
aktuelle_ladespannung_an_akku_kreis_7_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_7_s_5.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_8_s_5_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_8_s_5_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_8_s_5 = _Aktuelle_ladespannung_an_akku_kreis_8_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 35),
    _Aktuelle_ladespannung_an_akku_kreis_8_s_5_Type()
)
aktuelle_ladespannung_an_akku_kreis_8_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_8_s_5.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_1_s_5_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_1_s_5_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_1_s_5 = _Aktuelle_spannung_an_akku_kreis_1_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 36),
    _Aktuelle_spannung_an_akku_kreis_1_s_5_Type()
)
aktuelle_spannung_an_akku_kreis_1_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_1_s_5.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_2_s_5_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_2_s_5_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_2_s_5 = _Aktuelle_spannung_an_akku_kreis_2_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 37),
    _Aktuelle_spannung_an_akku_kreis_2_s_5_Type()
)
aktuelle_spannung_an_akku_kreis_2_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_2_s_5.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_3_s_5_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_3_s_5_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_3_s_5 = _Aktuelle_spannung_an_akku_kreis_3_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 38),
    _Aktuelle_spannung_an_akku_kreis_3_s_5_Type()
)
aktuelle_spannung_an_akku_kreis_3_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_3_s_5.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_4_s_5_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_4_s_5_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_4_s_5 = _Aktuelle_spannung_an_akku_kreis_4_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 39),
    _Aktuelle_spannung_an_akku_kreis_4_s_5_Type()
)
aktuelle_spannung_an_akku_kreis_4_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_4_s_5.setStatus("current")
_Aktuelle_spannung_an_akku_reis_5_s_5_Type = DisplayString
_Aktuelle_spannung_an_akku_reis_5_s_5_Object = MibTableColumn
aktuelle_spannung_an_akku_reis_5_s_5 = _Aktuelle_spannung_an_akku_reis_5_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 40),
    _Aktuelle_spannung_an_akku_reis_5_s_5_Type()
)
aktuelle_spannung_an_akku_reis_5_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_reis_5_s_5.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_6_s_5_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_6_s_5_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_6_s_5 = _Aktuelle_spannung_an_akku_kreis_6_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 41),
    _Aktuelle_spannung_an_akku_kreis_6_s_5_Type()
)
aktuelle_spannung_an_akku_kreis_6_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_6_s_5.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_7_s_5_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_7_s_5_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_7_s_5 = _Aktuelle_spannung_an_akku_kreis_7_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 42),
    _Aktuelle_spannung_an_akku_kreis_7_s_5_Type()
)
aktuelle_spannung_an_akku_kreis_7_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_7_s_5.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_8_s_5_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_8_s_5_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_8_s_5 = _Aktuelle_spannung_an_akku_kreis_8_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 43),
    _Aktuelle_spannung_an_akku_kreis_8_s_5_Type()
)
aktuelle_spannung_an_akku_kreis_8_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_8_s_5.setStatus("current")
_Testergebnis_lastspannung_an_akku_reis_1_s_5_Type = DisplayString
_Testergebnis_lastspannung_an_akku_reis_1_s_5_Object = MibTableColumn
testergebnis_lastspannung_an_akku_reis_1_s_5 = _Testergebnis_lastspannung_an_akku_reis_1_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 44),
    _Testergebnis_lastspannung_an_akku_reis_1_s_5_Type()
)
testergebnis_lastspannung_an_akku_reis_1_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_reis_1_s_5.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_2_s_5_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_2_s_5_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_2_s_5 = _Testergebnis_lastspannung_an_akku_kreis_2_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 45),
    _Testergebnis_lastspannung_an_akku_kreis_2_s_5_Type()
)
testergebnis_lastspannung_an_akku_kreis_2_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_2_s_5.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_3_s_5_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_3_s_5_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_3_s_5 = _Testergebnis_lastspannung_an_akku_kreis_3_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 46),
    _Testergebnis_lastspannung_an_akku_kreis_3_s_5_Type()
)
testergebnis_lastspannung_an_akku_kreis_3_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_3_s_5.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_4_s_5_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_4_s_5_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_4_s_5 = _Testergebnis_lastspannung_an_akku_kreis_4_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 47),
    _Testergebnis_lastspannung_an_akku_kreis_4_s_5_Type()
)
testergebnis_lastspannung_an_akku_kreis_4_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_4_s_5.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_5_s_5_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_5_s_5_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_5_s_5 = _Testergebnis_lastspannung_an_akku_kreis_5_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 48),
    _Testergebnis_lastspannung_an_akku_kreis_5_s_5_Type()
)
testergebnis_lastspannung_an_akku_kreis_5_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_5_s_5.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_6_s_5_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_6_s_5_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_6_s_5 = _Testergebnis_lastspannung_an_akku_kreis_6_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 49),
    _Testergebnis_lastspannung_an_akku_kreis_6_s_5_Type()
)
testergebnis_lastspannung_an_akku_kreis_6_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_6_s_5.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_7_s_5_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_7_s_5_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_7_s_5 = _Testergebnis_lastspannung_an_akku_kreis_7_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 50),
    _Testergebnis_lastspannung_an_akku_kreis_7_s_5_Type()
)
testergebnis_lastspannung_an_akku_kreis_7_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_7_s_5.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_8_s_5_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_8_s_5_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_8_s_5 = _Testergebnis_lastspannung_an_akku_kreis_8_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 51),
    _Testergebnis_lastspannung_an_akku_kreis_8_s_5_Type()
)
testergebnis_lastspannung_an_akku_kreis_8_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_8_s_5.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_1_s_5_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_1_s_5_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_1_s_5 = _Testergebnis_innenwiderstand_akku_kreis_1_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 52),
    _Testergebnis_innenwiderstand_akku_kreis_1_s_5_Type()
)
testergebnis_innenwiderstand_akku_kreis_1_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_1_s_5.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_2_s_5_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_2_s_5_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_2_s_5 = _Testergebnis_innenwiderstand_akku_kreis_2_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 53),
    _Testergebnis_innenwiderstand_akku_kreis_2_s_5_Type()
)
testergebnis_innenwiderstand_akku_kreis_2_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_2_s_5.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_3_s_5_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_3_s_5_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_3_s_5 = _Testergebnis_innenwiderstand_akku_kreis_3_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 54),
    _Testergebnis_innenwiderstand_akku_kreis_3_s_5_Type()
)
testergebnis_innenwiderstand_akku_kreis_3_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_3_s_5.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_4_s_5_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_4_s_5_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_4_s_5 = _Testergebnis_innenwiderstand_akku_kreis_4_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 56),
    _Testergebnis_innenwiderstand_akku_kreis_4_s_5_Type()
)
testergebnis_innenwiderstand_akku_kreis_4_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_4_s_5.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_5_s_5_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_5_s_5_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_5_s_5 = _Testergebnis_innenwiderstand_akku_kreis_5_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 57),
    _Testergebnis_innenwiderstand_akku_kreis_5_s_5_Type()
)
testergebnis_innenwiderstand_akku_kreis_5_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_5_s_5.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_6_s_5_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_6_s_5_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_6_s_5 = _Testergebnis_innenwiderstand_akku_kreis_6_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 58),
    _Testergebnis_innenwiderstand_akku_kreis_6_s_5_Type()
)
testergebnis_innenwiderstand_akku_kreis_6_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_6_s_5.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_7_s_5_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_7_s_5_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_7_s_5 = _Testergebnis_innenwiderstand_akku_kreis_7_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 59),
    _Testergebnis_innenwiderstand_akku_kreis_7_s_5_Type()
)
testergebnis_innenwiderstand_akku_kreis_7_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_7_s_5.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_8_s_5_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_8_s_5_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_8_s_5 = _Testergebnis_innenwiderstand_akku_kreis_8_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 60),
    _Testergebnis_innenwiderstand_akku_kreis_8_s_5_Type()
)
testergebnis_innenwiderstand_akku_kreis_8_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_8_s_5.setStatus("current")
_Netzteilspannung_uin1_s_5_Type = DisplayString
_Netzteilspannung_uin1_s_5_Object = MibTableColumn
netzteilspannung_uin1_s_5 = _Netzteilspannung_uin1_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 61),
    _Netzteilspannung_uin1_s_5_Type()
)
netzteilspannung_uin1_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzteilspannung_uin1_s_5.setStatus("current")
_Netzteilspannung_uin2_s_5_Type = DisplayString
_Netzteilspannung_uin2_s_5_Object = MibTableColumn
netzteilspannung_uin2_s_5 = _Netzteilspannung_uin2_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 62),
    _Netzteilspannung_uin2_s_5_Type()
)
netzteilspannung_uin2_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzteilspannung_uin2_s_5.setStatus("current")
_Programmierte_minimale_soll_sendeleistung_s_5_Type = DisplayString
_Programmierte_minimale_soll_sendeleistung_s_5_Object = MibTableColumn
programmierte_minimale_soll_sendeleistung_s_5 = _Programmierte_minimale_soll_sendeleistung_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 63),
    _Programmierte_minimale_soll_sendeleistung_s_5_Type()
)
programmierte_minimale_soll_sendeleistung_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programmierte_minimale_soll_sendeleistung_s_5.setStatus("current")
_Programmierte_maximale_antennen_reflexion_s_5_Type = DisplayString
_Programmierte_maximale_antennen_reflexion_s_5_Object = MibTableColumn
programmierte_maximale_antennen_reflexion_s_5 = _Programmierte_maximale_antennen_reflexion_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 64),
    _Programmierte_maximale_antennen_reflexion_s_5_Type()
)
programmierte_maximale_antennen_reflexion_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programmierte_maximale_antennen_reflexion_s_5.setStatus("current")
_Programmierte_minimale_anzahl_praesenzsignale_s_5_Type = DisplayString
_Programmierte_minimale_anzahl_praesenzsignale_s_5_Object = MibTableColumn
programmierte_minimale_anzahl_praesenzsignale_s_5 = _Programmierte_minimale_anzahl_praesenzsignale_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 65),
    _Programmierte_minimale_anzahl_praesenzsignale_s_5_Type()
)
programmierte_minimale_anzahl_praesenzsignale_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programmierte_minimale_anzahl_praesenzsignale_s_5.setStatus("current")
_Summen_fehlerstatus_von_tmoa_anlage_s_5_Type = DisplayString
_Summen_fehlerstatus_von_tmoa_anlage_s_5_Object = MibTableColumn
summen_fehlerstatus_von_tmoa_anlage_s_5 = _Summen_fehlerstatus_von_tmoa_anlage_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 66),
    _Summen_fehlerstatus_von_tmoa_anlage_s_5_Type()
)
summen_fehlerstatus_von_tmoa_anlage_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summen_fehlerstatus_von_tmoa_anlage_s_5.setStatus("current")
_Summen_fehlerstatus_von_anbinderepeater_s_5_Type = DisplayString
_Summen_fehlerstatus_von_anbinderepeater_s_5_Object = MibTableColumn
summen_fehlerstatus_von_anbinderepeater_s_5 = _Summen_fehlerstatus_von_anbinderepeater_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 67),
    _Summen_fehlerstatus_von_anbinderepeater_s_5_Type()
)
summen_fehlerstatus_von_anbinderepeater_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summen_fehlerstatus_von_anbinderepeater_s_5.setStatus("current")
_Summen_fehlerstatus_von_analogem_repeater_s_5_Type = DisplayString
_Summen_fehlerstatus_von_analogem_repeater_s_5_Object = MibTableColumn
summen_fehlerstatus_von_analogem_repeater_s_5 = _Summen_fehlerstatus_von_analogem_repeater_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 68),
    _Summen_fehlerstatus_von_analogem_repeater_s_5_Type()
)
summen_fehlerstatus_von_analogem_repeater_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summen_fehlerstatus_von_analogem_repeater_s_5.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_5_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_5_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_5 = _Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 69),
    _Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_5_Type()
)
aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_5.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_5_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_5_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_5 = _Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 70),
    _Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_5_Type()
)
aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_5.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_5_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_5_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_5 = _Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 71),
    _Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_5_Type()
)
aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_5.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_5_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_5_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_5 = _Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 72),
    _Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_5_Type()
)
aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_5.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_5_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_5_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_5 = _Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 73),
    _Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_5_Type()
)
aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_5.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_5_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_5_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_5 = _Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 74),
    _Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_5_Type()
)
aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_5.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_5_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_5_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_5 = _Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 75),
    _Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_5_Type()
)
aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_5.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_5_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_5_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_5 = _Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 76),
    _Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_5_Type()
)
aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_5.setStatus("current")
_Netzspannungsversorgung_von_tmoa_anlage_s_5_Type = DisplayString
_Netzspannungsversorgung_von_tmoa_anlage_s_5_Object = MibTableColumn
netzspannungsversorgung_von_tmoa_anlage_s_5 = _Netzspannungsversorgung_von_tmoa_anlage_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 77),
    _Netzspannungsversorgung_von_tmoa_anlage_s_5_Type()
)
netzspannungsversorgung_von_tmoa_anlage_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzspannungsversorgung_von_tmoa_anlage_s_5.setStatus("current")
_Netzspannungsversorgung_von_anbinderepeater_s_5_Type = DisplayString
_Netzspannungsversorgung_von_anbinderepeater_s_5_Object = MibTableColumn
netzspannungsversorgung_von_anbinderepeater_s_5 = _Netzspannungsversorgung_von_anbinderepeater_s_5_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 1, 1, 78),
    _Netzspannungsversorgung_von_anbinderepeater_s_5_Type()
)
netzspannungsversorgung_von_anbinderepeater_s_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzspannungsversorgung_von_anbinderepeater_s_5.setStatus("current")
_Ak_slave_6_i_ObjectIdentity = ObjectIdentity
ak_slave_6_i = _Ak_slave_6_i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6)
)
_ModulTable_s_6_Object = MibTable
modulTable_s_6 = _ModulTable_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1)
)
if mibBuilder.loadTexts:
    modulTable_s_6.setStatus("current")
_ModulEntry_s_6_Object = MibTableRow
modulEntry_s_6 = _ModulEntry_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1)
)
modulEntry_s_6.setIndexNames(
    (0, "AK-FUNKTECHNIK-MIB", "modulIndex-s-6"),
)
if mibBuilder.loadTexts:
    modulEntry_s_6.setStatus("current")
_ModulIndex_s_6_Type = DisplayString
_ModulIndex_s_6_Object = MibTableColumn
modulIndex_s_6 = _ModulIndex_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 1),
    _ModulIndex_s_6_Type()
)
modulIndex_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulIndex_s_6.setStatus("current")
_Geraete_typ_s_6_Type = DisplayString
_Geraete_typ_s_6_Object = MibTableColumn
geraete_typ_s_6 = _Geraete_typ_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 2),
    _Geraete_typ_s_6_Type()
)
geraete_typ_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geraete_typ_s_6.setStatus("current")
_Betriebsstatus_s_6_Type = DisplayString
_Betriebsstatus_s_6_Object = MibTableColumn
betriebsstatus_s_6 = _Betriebsstatus_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 3),
    _Betriebsstatus_s_6_Type()
)
betriebsstatus_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    betriebsstatus_s_6.setStatus("current")
_Senderstatus_s_6_Type = DisplayString
_Senderstatus_s_6_Object = MibTableColumn
senderstatus_s_6 = _Senderstatus_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 4),
    _Senderstatus_s_6_Type()
)
senderstatus_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    senderstatus_s_6.setStatus("current")
_Fehlerstatus_s_6_Type = DisplayString
_Fehlerstatus_s_6_Object = MibTableColumn
fehlerstatus_s_6 = _Fehlerstatus_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 5),
    _Fehlerstatus_s_6_Type()
)
fehlerstatus_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fehlerstatus_s_6.setStatus("current")
_Dem_adapter_zugeordnete_funkgeraetetype_s_6_Type = DisplayString
_Dem_adapter_zugeordnete_funkgeraetetype_s_6_Object = MibTableColumn
dem_adapter_zugeordnete_funkgeraetetype_s_6 = _Dem_adapter_zugeordnete_funkgeraetetype_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 6),
    _Dem_adapter_zugeordnete_funkgeraetetype_s_6_Type()
)
dem_adapter_zugeordnete_funkgeraetetype_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dem_adapter_zugeordnete_funkgeraetetype_s_6.setStatus("current")
_Eingabe_und_anzeigemodul_s_6_Type = DisplayString
_Eingabe_und_anzeigemodul_s_6_Object = MibTableColumn
eingabe_und_anzeigemodul_s_6 = _Eingabe_und_anzeigemodul_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 7),
    _Eingabe_und_anzeigemodul_s_6_Type()
)
eingabe_und_anzeigemodul_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eingabe_und_anzeigemodul_s_6.setStatus("current")
_Mod_bus_verbindung_module_s_6_Type = DisplayString
_Mod_bus_verbindung_module_s_6_Object = MibTableColumn
mod_bus_verbindung_module_s_6 = _Mod_bus_verbindung_module_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 8),
    _Mod_bus_verbindung_module_s_6_Type()
)
mod_bus_verbindung_module_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mod_bus_verbindung_module_s_6.setStatus("current")
_Gemessene_sendeleistung_im_testmode_s_6_Type = DisplayString
_Gemessene_sendeleistung_im_testmode_s_6_Object = MibTableColumn
gemessene_sendeleistung_im_testmode_s_6 = _Gemessene_sendeleistung_im_testmode_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 9),
    _Gemessene_sendeleistung_im_testmode_s_6_Type()
)
gemessene_sendeleistung_im_testmode_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemessene_sendeleistung_im_testmode_s_6.setStatus("current")
_Aktuelle_sendeleistung_s_6_Type = DisplayString
_Aktuelle_sendeleistung_s_6_Object = MibTableColumn
aktuelle_sendeleistung_s_6 = _Aktuelle_sendeleistung_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 10),
    _Aktuelle_sendeleistung_s_6_Type()
)
aktuelle_sendeleistung_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_sendeleistung_s_6.setStatus("current")
_Gemessene_reflexion_im_testmode_s_6_Type = DisplayString
_Gemessene_reflexion_im_testmode_s_6_Object = MibTableColumn
gemessene_reflexion_im_testmode_s_6 = _Gemessene_reflexion_im_testmode_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 11),
    _Gemessene_reflexion_im_testmode_s_6_Type()
)
gemessene_reflexion_im_testmode_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemessene_reflexion_im_testmode_s_6.setStatus("current")
_Aktuelle_reflexion_s_6_Type = DisplayString
_Aktuelle_reflexion_s_6_Object = MibTableColumn
aktuelle_reflexion_s_6 = _Aktuelle_reflexion_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 12),
    _Aktuelle_reflexion_s_6_Type()
)
aktuelle_reflexion_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_reflexion_s_6.setStatus("current")
_Letzte_gemessene_donor_sendeleistung_s_6_Type = DisplayString
_Letzte_gemessene_donor_sendeleistung_s_6_Object = MibTableColumn
letzte_gemessene_donor_sendeleistung_s_6 = _Letzte_gemessene_donor_sendeleistung_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 13),
    _Letzte_gemessene_donor_sendeleistung_s_6_Type()
)
letzte_gemessene_donor_sendeleistung_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    letzte_gemessene_donor_sendeleistung_s_6.setStatus("current")
_Aktuelle_donor_sendeleistung_s_6_Type = DisplayString
_Aktuelle_donor_sendeleistung_s_6_Object = MibTableColumn
aktuelle_donor_sendeleistung_s_6 = _Aktuelle_donor_sendeleistung_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 14),
    _Aktuelle_donor_sendeleistung_s_6_Type()
)
aktuelle_donor_sendeleistung_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_donor_sendeleistung_s_6.setStatus("current")
_Letzte_gemessene_donor_reflexion_s_6_Type = DisplayString
_Letzte_gemessene_donor_reflexion_s_6_Object = MibTableColumn
letzte_gemessene_donor_reflexion_s_6 = _Letzte_gemessene_donor_reflexion_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 15),
    _Letzte_gemessene_donor_reflexion_s_6_Type()
)
letzte_gemessene_donor_reflexion_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    letzte_gemessene_donor_reflexion_s_6.setStatus("current")
_Aktuelle_donor_reflexion_s_6_Type = DisplayString
_Aktuelle_donor_reflexion_s_6_Object = MibTableColumn
aktuelle_donor_reflexion_s_6 = _Aktuelle_donor_reflexion_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 16),
    _Aktuelle_donor_reflexion_s_6_Type()
)
aktuelle_donor_reflexion_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_donor_reflexion_s_6.setStatus("current")
_Anzahl_gemessener_praesenzsignale_im_testmode_s_6_Type = DisplayString
_Anzahl_gemessener_praesenzsignale_im_testmode_s_6_Object = MibTableColumn
anzahl_gemessener_praesenzsignale_im_testmode_s_6 = _Anzahl_gemessener_praesenzsignale_im_testmode_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 18),
    _Anzahl_gemessener_praesenzsignale_im_testmode_s_6_Type()
)
anzahl_gemessener_praesenzsignale_im_testmode_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anzahl_gemessener_praesenzsignale_im_testmode_s_6.setStatus("current")
_Aktuelle_ausgangsspannung_ub_s_6_Type = DisplayString
_Aktuelle_ausgangsspannung_ub_s_6_Object = MibTableColumn
aktuelle_ausgangsspannung_ub_s_6 = _Aktuelle_ausgangsspannung_ub_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 19),
    _Aktuelle_ausgangsspannung_ub_s_6_Type()
)
aktuelle_ausgangsspannung_ub_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_ub_s_6.setStatus("current")
_Aktuelle_ausgangsspannung_u1_s_6_Type = DisplayString
_Aktuelle_ausgangsspannung_u1_s_6_Object = MibTableColumn
aktuelle_ausgangsspannung_u1_s_6 = _Aktuelle_ausgangsspannung_u1_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 20),
    _Aktuelle_ausgangsspannung_u1_s_6_Type()
)
aktuelle_ausgangsspannung_u1_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u1_s_6.setStatus("current")
_Aktuelle_ausgangsspannung_u2_s_6_Type = DisplayString
_Aktuelle_ausgangsspannung_u2_s_6_Object = MibTableColumn
aktuelle_ausgangsspannung_u2_s_6 = _Aktuelle_ausgangsspannung_u2_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 21),
    _Aktuelle_ausgangsspannung_u2_s_6_Type()
)
aktuelle_ausgangsspannung_u2_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u2_s_6.setStatus("current")
_Aktuelle_ausgangsspannung_u3_s_6_Type = DisplayString
_Aktuelle_ausgangsspannung_u3_s_6_Object = MibTableColumn
aktuelle_ausgangsspannung_u3_s_6 = _Aktuelle_ausgangsspannung_u3_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 22),
    _Aktuelle_ausgangsspannung_u3_s_6_Type()
)
aktuelle_ausgangsspannung_u3_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u3_s_6.setStatus("current")
_Aktuelle_ausgangsspannung_u4_s_6_Type = DisplayString
_Aktuelle_ausgangsspannung_u4_s_6_Object = MibTableColumn
aktuelle_ausgangsspannung_u4_s_6 = _Aktuelle_ausgangsspannung_u4_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 23),
    _Aktuelle_ausgangsspannung_u4_s_6_Type()
)
aktuelle_ausgangsspannung_u4_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u4_s_6.setStatus("current")
_Aktuelle_ausgangsspannung_u5_s_6_Type = DisplayString
_Aktuelle_ausgangsspannung_u5_s_6_Object = MibTableColumn
aktuelle_ausgangsspannung_u5_s_6 = _Aktuelle_ausgangsspannung_u5_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 24),
    _Aktuelle_ausgangsspannung_u5_s_6_Type()
)
aktuelle_ausgangsspannung_u5_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u5_s_6.setStatus("current")
_Aktuelle_ausgangsspannung_u6_s_6_Type = DisplayString
_Aktuelle_ausgangsspannung_u6_s_6_Object = MibTableColumn
aktuelle_ausgangsspannung_u6_s_6 = _Aktuelle_ausgangsspannung_u6_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 25),
    _Aktuelle_ausgangsspannung_u6_s_6_Type()
)
aktuelle_ausgangsspannung_u6_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u6_s_6.setStatus("current")
_Aktuelle_ausgangsspannung_u7_s_6_Type = DisplayString
_Aktuelle_ausgangsspannung_u7_s_6_Object = MibTableColumn
aktuelle_ausgangsspannung_u7_s_6 = _Aktuelle_ausgangsspannung_u7_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 26),
    _Aktuelle_ausgangsspannung_u7_s_6_Type()
)
aktuelle_ausgangsspannung_u7_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u7_s_6.setStatus("current")
_Aktuelle_ausgangsspannung_u8_s_6_Type = DisplayString
_Aktuelle_ausgangsspannung_u8_s_6_Object = MibTableColumn
aktuelle_ausgangsspannung_u8_s_6 = _Aktuelle_ausgangsspannung_u8_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 27),
    _Aktuelle_ausgangsspannung_u8_s_6_Type()
)
aktuelle_ausgangsspannung_u8_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u8_s_6.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_1_s_6_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_1_s_6_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_1_s_6 = _Aktuelle_ladespannung_an_akku_kreis_1_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 28),
    _Aktuelle_ladespannung_an_akku_kreis_1_s_6_Type()
)
aktuelle_ladespannung_an_akku_kreis_1_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_1_s_6.setStatus("current")
_Aktuelle_ladespannung_an_akku_Kreis_2_s_6_Type = DisplayString
_Aktuelle_ladespannung_an_akku_Kreis_2_s_6_Object = MibTableColumn
aktuelle_ladespannung_an_akku_Kreis_2_s_6 = _Aktuelle_ladespannung_an_akku_Kreis_2_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 29),
    _Aktuelle_ladespannung_an_akku_Kreis_2_s_6_Type()
)
aktuelle_ladespannung_an_akku_Kreis_2_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_Kreis_2_s_6.setStatus("current")
_Aktuelle_ladespannung_an_akku_Kreis_3_s_6_Type = DisplayString
_Aktuelle_ladespannung_an_akku_Kreis_3_s_6_Object = MibTableColumn
aktuelle_ladespannung_an_akku_Kreis_3_s_6 = _Aktuelle_ladespannung_an_akku_Kreis_3_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 30),
    _Aktuelle_ladespannung_an_akku_Kreis_3_s_6_Type()
)
aktuelle_ladespannung_an_akku_Kreis_3_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_Kreis_3_s_6.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_4_s_6_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_4_s_6_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_4_s_6 = _Aktuelle_ladespannung_an_akku_kreis_4_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 31),
    _Aktuelle_ladespannung_an_akku_kreis_4_s_6_Type()
)
aktuelle_ladespannung_an_akku_kreis_4_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_4_s_6.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_5_s_6_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_5_s_6_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_5_s_6 = _Aktuelle_ladespannung_an_akku_kreis_5_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 32),
    _Aktuelle_ladespannung_an_akku_kreis_5_s_6_Type()
)
aktuelle_ladespannung_an_akku_kreis_5_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_5_s_6.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_6_s_6_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_6_s_6_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_6_s_6 = _Aktuelle_ladespannung_an_akku_kreis_6_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 33),
    _Aktuelle_ladespannung_an_akku_kreis_6_s_6_Type()
)
aktuelle_ladespannung_an_akku_kreis_6_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_6_s_6.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_7_s_6_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_7_s_6_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_7_s_6 = _Aktuelle_ladespannung_an_akku_kreis_7_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 34),
    _Aktuelle_ladespannung_an_akku_kreis_7_s_6_Type()
)
aktuelle_ladespannung_an_akku_kreis_7_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_7_s_6.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_8_s_6_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_8_s_6_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_8_s_6 = _Aktuelle_ladespannung_an_akku_kreis_8_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 35),
    _Aktuelle_ladespannung_an_akku_kreis_8_s_6_Type()
)
aktuelle_ladespannung_an_akku_kreis_8_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_8_s_6.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_1_s_6_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_1_s_6_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_1_s_6 = _Aktuelle_spannung_an_akku_kreis_1_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 36),
    _Aktuelle_spannung_an_akku_kreis_1_s_6_Type()
)
aktuelle_spannung_an_akku_kreis_1_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_1_s_6.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_2_s_6_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_2_s_6_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_2_s_6 = _Aktuelle_spannung_an_akku_kreis_2_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 37),
    _Aktuelle_spannung_an_akku_kreis_2_s_6_Type()
)
aktuelle_spannung_an_akku_kreis_2_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_2_s_6.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_3_s_6_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_3_s_6_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_3_s_6 = _Aktuelle_spannung_an_akku_kreis_3_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 38),
    _Aktuelle_spannung_an_akku_kreis_3_s_6_Type()
)
aktuelle_spannung_an_akku_kreis_3_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_3_s_6.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_4_s_6_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_4_s_6_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_4_s_6 = _Aktuelle_spannung_an_akku_kreis_4_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 39),
    _Aktuelle_spannung_an_akku_kreis_4_s_6_Type()
)
aktuelle_spannung_an_akku_kreis_4_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_4_s_6.setStatus("current")
_Aktuelle_spannung_an_akku_reis_5_s_6_Type = DisplayString
_Aktuelle_spannung_an_akku_reis_5_s_6_Object = MibTableColumn
aktuelle_spannung_an_akku_reis_5_s_6 = _Aktuelle_spannung_an_akku_reis_5_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 40),
    _Aktuelle_spannung_an_akku_reis_5_s_6_Type()
)
aktuelle_spannung_an_akku_reis_5_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_reis_5_s_6.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_6_s_6_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_6_s_6_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_6_s_6 = _Aktuelle_spannung_an_akku_kreis_6_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 41),
    _Aktuelle_spannung_an_akku_kreis_6_s_6_Type()
)
aktuelle_spannung_an_akku_kreis_6_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_6_s_6.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_7_s_6_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_7_s_6_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_7_s_6 = _Aktuelle_spannung_an_akku_kreis_7_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 42),
    _Aktuelle_spannung_an_akku_kreis_7_s_6_Type()
)
aktuelle_spannung_an_akku_kreis_7_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_7_s_6.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_8_s_6_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_8_s_6_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_8_s_6 = _Aktuelle_spannung_an_akku_kreis_8_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 43),
    _Aktuelle_spannung_an_akku_kreis_8_s_6_Type()
)
aktuelle_spannung_an_akku_kreis_8_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_8_s_6.setStatus("current")
_Testergebnis_lastspannung_an_akku_reis_1_s_6_Type = DisplayString
_Testergebnis_lastspannung_an_akku_reis_1_s_6_Object = MibTableColumn
testergebnis_lastspannung_an_akku_reis_1_s_6 = _Testergebnis_lastspannung_an_akku_reis_1_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 44),
    _Testergebnis_lastspannung_an_akku_reis_1_s_6_Type()
)
testergebnis_lastspannung_an_akku_reis_1_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_reis_1_s_6.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_2_s_6_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_2_s_6_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_2_s_6 = _Testergebnis_lastspannung_an_akku_kreis_2_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 45),
    _Testergebnis_lastspannung_an_akku_kreis_2_s_6_Type()
)
testergebnis_lastspannung_an_akku_kreis_2_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_2_s_6.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_3_s_6_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_3_s_6_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_3_s_6 = _Testergebnis_lastspannung_an_akku_kreis_3_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 46),
    _Testergebnis_lastspannung_an_akku_kreis_3_s_6_Type()
)
testergebnis_lastspannung_an_akku_kreis_3_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_3_s_6.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_4_s_6_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_4_s_6_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_4_s_6 = _Testergebnis_lastspannung_an_akku_kreis_4_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 47),
    _Testergebnis_lastspannung_an_akku_kreis_4_s_6_Type()
)
testergebnis_lastspannung_an_akku_kreis_4_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_4_s_6.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_5_s_6_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_5_s_6_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_5_s_6 = _Testergebnis_lastspannung_an_akku_kreis_5_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 48),
    _Testergebnis_lastspannung_an_akku_kreis_5_s_6_Type()
)
testergebnis_lastspannung_an_akku_kreis_5_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_5_s_6.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_6_s_6_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_6_s_6_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_6_s_6 = _Testergebnis_lastspannung_an_akku_kreis_6_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 49),
    _Testergebnis_lastspannung_an_akku_kreis_6_s_6_Type()
)
testergebnis_lastspannung_an_akku_kreis_6_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_6_s_6.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_7_s_6_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_7_s_6_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_7_s_6 = _Testergebnis_lastspannung_an_akku_kreis_7_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 50),
    _Testergebnis_lastspannung_an_akku_kreis_7_s_6_Type()
)
testergebnis_lastspannung_an_akku_kreis_7_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_7_s_6.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_8_s_6_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_8_s_6_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_8_s_6 = _Testergebnis_lastspannung_an_akku_kreis_8_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 51),
    _Testergebnis_lastspannung_an_akku_kreis_8_s_6_Type()
)
testergebnis_lastspannung_an_akku_kreis_8_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_8_s_6.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_1_s_6_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_1_s_6_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_1_s_6 = _Testergebnis_innenwiderstand_akku_kreis_1_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 52),
    _Testergebnis_innenwiderstand_akku_kreis_1_s_6_Type()
)
testergebnis_innenwiderstand_akku_kreis_1_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_1_s_6.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_2_s_6_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_2_s_6_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_2_s_6 = _Testergebnis_innenwiderstand_akku_kreis_2_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 53),
    _Testergebnis_innenwiderstand_akku_kreis_2_s_6_Type()
)
testergebnis_innenwiderstand_akku_kreis_2_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_2_s_6.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_3_s_6_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_3_s_6_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_3_s_6 = _Testergebnis_innenwiderstand_akku_kreis_3_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 54),
    _Testergebnis_innenwiderstand_akku_kreis_3_s_6_Type()
)
testergebnis_innenwiderstand_akku_kreis_3_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_3_s_6.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_4_s_6_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_4_s_6_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_4_s_6 = _Testergebnis_innenwiderstand_akku_kreis_4_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 56),
    _Testergebnis_innenwiderstand_akku_kreis_4_s_6_Type()
)
testergebnis_innenwiderstand_akku_kreis_4_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_4_s_6.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_5_s_6_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_5_s_6_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_5_s_6 = _Testergebnis_innenwiderstand_akku_kreis_5_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 57),
    _Testergebnis_innenwiderstand_akku_kreis_5_s_6_Type()
)
testergebnis_innenwiderstand_akku_kreis_5_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_5_s_6.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_6_s_6_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_6_s_6_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_6_s_6 = _Testergebnis_innenwiderstand_akku_kreis_6_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 58),
    _Testergebnis_innenwiderstand_akku_kreis_6_s_6_Type()
)
testergebnis_innenwiderstand_akku_kreis_6_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_6_s_6.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_7_s_6_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_7_s_6_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_7_s_6 = _Testergebnis_innenwiderstand_akku_kreis_7_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 59),
    _Testergebnis_innenwiderstand_akku_kreis_7_s_6_Type()
)
testergebnis_innenwiderstand_akku_kreis_7_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_7_s_6.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_8_s_6_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_8_s_6_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_8_s_6 = _Testergebnis_innenwiderstand_akku_kreis_8_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 60),
    _Testergebnis_innenwiderstand_akku_kreis_8_s_6_Type()
)
testergebnis_innenwiderstand_akku_kreis_8_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_8_s_6.setStatus("current")
_Netzteilspannung_uin1_s_6_Type = DisplayString
_Netzteilspannung_uin1_s_6_Object = MibTableColumn
netzteilspannung_uin1_s_6 = _Netzteilspannung_uin1_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 61),
    _Netzteilspannung_uin1_s_6_Type()
)
netzteilspannung_uin1_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzteilspannung_uin1_s_6.setStatus("current")
_Netzteilspannung_uin2_s_6_Type = DisplayString
_Netzteilspannung_uin2_s_6_Object = MibTableColumn
netzteilspannung_uin2_s_6 = _Netzteilspannung_uin2_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 62),
    _Netzteilspannung_uin2_s_6_Type()
)
netzteilspannung_uin2_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzteilspannung_uin2_s_6.setStatus("current")
_Programmierte_minimale_soll_sendeleistung_s_6_Type = DisplayString
_Programmierte_minimale_soll_sendeleistung_s_6_Object = MibTableColumn
programmierte_minimale_soll_sendeleistung_s_6 = _Programmierte_minimale_soll_sendeleistung_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 63),
    _Programmierte_minimale_soll_sendeleistung_s_6_Type()
)
programmierte_minimale_soll_sendeleistung_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programmierte_minimale_soll_sendeleistung_s_6.setStatus("current")
_Programmierte_maximale_antennen_reflexion_s_6_Type = DisplayString
_Programmierte_maximale_antennen_reflexion_s_6_Object = MibTableColumn
programmierte_maximale_antennen_reflexion_s_6 = _Programmierte_maximale_antennen_reflexion_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 64),
    _Programmierte_maximale_antennen_reflexion_s_6_Type()
)
programmierte_maximale_antennen_reflexion_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programmierte_maximale_antennen_reflexion_s_6.setStatus("current")
_Programmierte_minimale_anzahl_praesenzsignale_s_6_Type = DisplayString
_Programmierte_minimale_anzahl_praesenzsignale_s_6_Object = MibTableColumn
programmierte_minimale_anzahl_praesenzsignale_s_6 = _Programmierte_minimale_anzahl_praesenzsignale_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 65),
    _Programmierte_minimale_anzahl_praesenzsignale_s_6_Type()
)
programmierte_minimale_anzahl_praesenzsignale_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programmierte_minimale_anzahl_praesenzsignale_s_6.setStatus("current")
_Summen_fehlerstatus_von_tmoa_anlage_s_6_Type = DisplayString
_Summen_fehlerstatus_von_tmoa_anlage_s_6_Object = MibTableColumn
summen_fehlerstatus_von_tmoa_anlage_s_6 = _Summen_fehlerstatus_von_tmoa_anlage_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 66),
    _Summen_fehlerstatus_von_tmoa_anlage_s_6_Type()
)
summen_fehlerstatus_von_tmoa_anlage_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summen_fehlerstatus_von_tmoa_anlage_s_6.setStatus("current")
_Summen_fehlerstatus_von_anbinderepeater_s_6_Type = DisplayString
_Summen_fehlerstatus_von_anbinderepeater_s_6_Object = MibTableColumn
summen_fehlerstatus_von_anbinderepeater_s_6 = _Summen_fehlerstatus_von_anbinderepeater_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 67),
    _Summen_fehlerstatus_von_anbinderepeater_s_6_Type()
)
summen_fehlerstatus_von_anbinderepeater_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summen_fehlerstatus_von_anbinderepeater_s_6.setStatus("current")
_Summen_fehlerstatus_von_analogem_repeater_s_6_Type = DisplayString
_Summen_fehlerstatus_von_analogem_repeater_s_6_Object = MibTableColumn
summen_fehlerstatus_von_analogem_repeater_s_6 = _Summen_fehlerstatus_von_analogem_repeater_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 68),
    _Summen_fehlerstatus_von_analogem_repeater_s_6_Type()
)
summen_fehlerstatus_von_analogem_repeater_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summen_fehlerstatus_von_analogem_repeater_s_6.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_6_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_6_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_6 = _Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 69),
    _Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_6_Type()
)
aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_6.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_6_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_6_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_6 = _Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 70),
    _Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_6_Type()
)
aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_6.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_6_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_6_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_6 = _Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 71),
    _Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_6_Type()
)
aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_6.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_6_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_6_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_6 = _Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 72),
    _Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_6_Type()
)
aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_6.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_6_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_6_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_6 = _Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 73),
    _Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_6_Type()
)
aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_6.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_6_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_6_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_6 = _Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 74),
    _Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_6_Type()
)
aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_6.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_6_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_6_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_6 = _Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 75),
    _Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_6_Type()
)
aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_6.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_6_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_6_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_6 = _Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 76),
    _Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_6_Type()
)
aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_6.setStatus("current")
_Netzspannungsversorgung_von_tmoa_anlage_s_6_Type = DisplayString
_Netzspannungsversorgung_von_tmoa_anlage_s_6_Object = MibTableColumn
netzspannungsversorgung_von_tmoa_anlage_s_6 = _Netzspannungsversorgung_von_tmoa_anlage_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 77),
    _Netzspannungsversorgung_von_tmoa_anlage_s_6_Type()
)
netzspannungsversorgung_von_tmoa_anlage_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzspannungsversorgung_von_tmoa_anlage_s_6.setStatus("current")
_Netzspannungsversorgung_von_anbinderepeater_s_6_Type = DisplayString
_Netzspannungsversorgung_von_anbinderepeater_s_6_Object = MibTableColumn
netzspannungsversorgung_von_anbinderepeater_s_6 = _Netzspannungsversorgung_von_anbinderepeater_s_6_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 1, 1, 78),
    _Netzspannungsversorgung_von_anbinderepeater_s_6_Type()
)
netzspannungsversorgung_von_anbinderepeater_s_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzspannungsversorgung_von_anbinderepeater_s_6.setStatus("current")
_Ak_slave_7_i_ObjectIdentity = ObjectIdentity
ak_slave_7_i = _Ak_slave_7_i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7)
)
_ModulTable_s_7_Object = MibTable
modulTable_s_7 = _ModulTable_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1)
)
if mibBuilder.loadTexts:
    modulTable_s_7.setStatus("current")
_ModulEntry_s_7_Object = MibTableRow
modulEntry_s_7 = _ModulEntry_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1)
)
modulEntry_s_7.setIndexNames(
    (0, "AK-FUNKTECHNIK-MIB", "modulIndex-s-7"),
)
if mibBuilder.loadTexts:
    modulEntry_s_7.setStatus("current")
_ModulIndex_s_7_Type = DisplayString
_ModulIndex_s_7_Object = MibTableColumn
modulIndex_s_7 = _ModulIndex_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 1),
    _ModulIndex_s_7_Type()
)
modulIndex_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulIndex_s_7.setStatus("current")
_Geraete_typ_s_7_Type = DisplayString
_Geraete_typ_s_7_Object = MibTableColumn
geraete_typ_s_7 = _Geraete_typ_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 2),
    _Geraete_typ_s_7_Type()
)
geraete_typ_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geraete_typ_s_7.setStatus("current")
_Betriebsstatus_s_7_Type = DisplayString
_Betriebsstatus_s_7_Object = MibTableColumn
betriebsstatus_s_7 = _Betriebsstatus_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 3),
    _Betriebsstatus_s_7_Type()
)
betriebsstatus_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    betriebsstatus_s_7.setStatus("current")
_Senderstatus_s_7_Type = DisplayString
_Senderstatus_s_7_Object = MibTableColumn
senderstatus_s_7 = _Senderstatus_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 4),
    _Senderstatus_s_7_Type()
)
senderstatus_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    senderstatus_s_7.setStatus("current")
_Fehlerstatus_s_7_Type = DisplayString
_Fehlerstatus_s_7_Object = MibTableColumn
fehlerstatus_s_7 = _Fehlerstatus_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 5),
    _Fehlerstatus_s_7_Type()
)
fehlerstatus_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fehlerstatus_s_7.setStatus("current")
_Dem_adapter_zugeordnete_funkgeraetetype_s_7_Type = DisplayString
_Dem_adapter_zugeordnete_funkgeraetetype_s_7_Object = MibTableColumn
dem_adapter_zugeordnete_funkgeraetetype_s_7 = _Dem_adapter_zugeordnete_funkgeraetetype_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 6),
    _Dem_adapter_zugeordnete_funkgeraetetype_s_7_Type()
)
dem_adapter_zugeordnete_funkgeraetetype_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dem_adapter_zugeordnete_funkgeraetetype_s_7.setStatus("current")
_Eingabe_und_anzeigemodul_s_7_Type = DisplayString
_Eingabe_und_anzeigemodul_s_7_Object = MibTableColumn
eingabe_und_anzeigemodul_s_7 = _Eingabe_und_anzeigemodul_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 7),
    _Eingabe_und_anzeigemodul_s_7_Type()
)
eingabe_und_anzeigemodul_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eingabe_und_anzeigemodul_s_7.setStatus("current")
_Mod_bus_verbindung_module_s_7_Type = DisplayString
_Mod_bus_verbindung_module_s_7_Object = MibTableColumn
mod_bus_verbindung_module_s_7 = _Mod_bus_verbindung_module_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 8),
    _Mod_bus_verbindung_module_s_7_Type()
)
mod_bus_verbindung_module_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mod_bus_verbindung_module_s_7.setStatus("current")
_Gemessene_sendeleistung_im_testmode_s_7_Type = DisplayString
_Gemessene_sendeleistung_im_testmode_s_7_Object = MibTableColumn
gemessene_sendeleistung_im_testmode_s_7 = _Gemessene_sendeleistung_im_testmode_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 9),
    _Gemessene_sendeleistung_im_testmode_s_7_Type()
)
gemessene_sendeleistung_im_testmode_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemessene_sendeleistung_im_testmode_s_7.setStatus("current")
_Aktuelle_sendeleistung_s_7_Type = DisplayString
_Aktuelle_sendeleistung_s_7_Object = MibTableColumn
aktuelle_sendeleistung_s_7 = _Aktuelle_sendeleistung_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 10),
    _Aktuelle_sendeleistung_s_7_Type()
)
aktuelle_sendeleistung_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_sendeleistung_s_7.setStatus("current")
_Gemessene_reflexion_im_testmode_s_7_Type = DisplayString
_Gemessene_reflexion_im_testmode_s_7_Object = MibTableColumn
gemessene_reflexion_im_testmode_s_7 = _Gemessene_reflexion_im_testmode_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 11),
    _Gemessene_reflexion_im_testmode_s_7_Type()
)
gemessene_reflexion_im_testmode_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemessene_reflexion_im_testmode_s_7.setStatus("current")
_Aktuelle_reflexion_s_7_Type = DisplayString
_Aktuelle_reflexion_s_7_Object = MibTableColumn
aktuelle_reflexion_s_7 = _Aktuelle_reflexion_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 12),
    _Aktuelle_reflexion_s_7_Type()
)
aktuelle_reflexion_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_reflexion_s_7.setStatus("current")
_Letzte_gemessene_donor_sendeleistung_s_7_Type = DisplayString
_Letzte_gemessene_donor_sendeleistung_s_7_Object = MibTableColumn
letzte_gemessene_donor_sendeleistung_s_7 = _Letzte_gemessene_donor_sendeleistung_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 13),
    _Letzte_gemessene_donor_sendeleistung_s_7_Type()
)
letzte_gemessene_donor_sendeleistung_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    letzte_gemessene_donor_sendeleistung_s_7.setStatus("current")
_Aktuelle_donor_sendeleistung_s_7_Type = DisplayString
_Aktuelle_donor_sendeleistung_s_7_Object = MibTableColumn
aktuelle_donor_sendeleistung_s_7 = _Aktuelle_donor_sendeleistung_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 14),
    _Aktuelle_donor_sendeleistung_s_7_Type()
)
aktuelle_donor_sendeleistung_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_donor_sendeleistung_s_7.setStatus("current")
_Letzte_gemessene_donor_reflexion_s_7_Type = DisplayString
_Letzte_gemessene_donor_reflexion_s_7_Object = MibTableColumn
letzte_gemessene_donor_reflexion_s_7 = _Letzte_gemessene_donor_reflexion_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 15),
    _Letzte_gemessene_donor_reflexion_s_7_Type()
)
letzte_gemessene_donor_reflexion_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    letzte_gemessene_donor_reflexion_s_7.setStatus("current")
_Aktuelle_donor_reflexion_s_7_Type = DisplayString
_Aktuelle_donor_reflexion_s_7_Object = MibTableColumn
aktuelle_donor_reflexion_s_7 = _Aktuelle_donor_reflexion_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 16),
    _Aktuelle_donor_reflexion_s_7_Type()
)
aktuelle_donor_reflexion_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_donor_reflexion_s_7.setStatus("current")
_Anzahl_gemessener_praesenzsignale_im_testmode_s_7_Type = DisplayString
_Anzahl_gemessener_praesenzsignale_im_testmode_s_7_Object = MibTableColumn
anzahl_gemessener_praesenzsignale_im_testmode_s_7 = _Anzahl_gemessener_praesenzsignale_im_testmode_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 18),
    _Anzahl_gemessener_praesenzsignale_im_testmode_s_7_Type()
)
anzahl_gemessener_praesenzsignale_im_testmode_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anzahl_gemessener_praesenzsignale_im_testmode_s_7.setStatus("current")
_Aktuelle_ausgangsspannung_ub_s_7_Type = DisplayString
_Aktuelle_ausgangsspannung_ub_s_7_Object = MibTableColumn
aktuelle_ausgangsspannung_ub_s_7 = _Aktuelle_ausgangsspannung_ub_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 19),
    _Aktuelle_ausgangsspannung_ub_s_7_Type()
)
aktuelle_ausgangsspannung_ub_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_ub_s_7.setStatus("current")
_Aktuelle_ausgangsspannung_u1_s_7_Type = DisplayString
_Aktuelle_ausgangsspannung_u1_s_7_Object = MibTableColumn
aktuelle_ausgangsspannung_u1_s_7 = _Aktuelle_ausgangsspannung_u1_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 20),
    _Aktuelle_ausgangsspannung_u1_s_7_Type()
)
aktuelle_ausgangsspannung_u1_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u1_s_7.setStatus("current")
_Aktuelle_ausgangsspannung_u2_s_7_Type = DisplayString
_Aktuelle_ausgangsspannung_u2_s_7_Object = MibTableColumn
aktuelle_ausgangsspannung_u2_s_7 = _Aktuelle_ausgangsspannung_u2_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 21),
    _Aktuelle_ausgangsspannung_u2_s_7_Type()
)
aktuelle_ausgangsspannung_u2_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u2_s_7.setStatus("current")
_Aktuelle_ausgangsspannung_u3_s_7_Type = DisplayString
_Aktuelle_ausgangsspannung_u3_s_7_Object = MibTableColumn
aktuelle_ausgangsspannung_u3_s_7 = _Aktuelle_ausgangsspannung_u3_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 22),
    _Aktuelle_ausgangsspannung_u3_s_7_Type()
)
aktuelle_ausgangsspannung_u3_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u3_s_7.setStatus("current")
_Aktuelle_ausgangsspannung_u4_s_7_Type = DisplayString
_Aktuelle_ausgangsspannung_u4_s_7_Object = MibTableColumn
aktuelle_ausgangsspannung_u4_s_7 = _Aktuelle_ausgangsspannung_u4_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 23),
    _Aktuelle_ausgangsspannung_u4_s_7_Type()
)
aktuelle_ausgangsspannung_u4_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u4_s_7.setStatus("current")
_Aktuelle_ausgangsspannung_u5_s_7_Type = DisplayString
_Aktuelle_ausgangsspannung_u5_s_7_Object = MibTableColumn
aktuelle_ausgangsspannung_u5_s_7 = _Aktuelle_ausgangsspannung_u5_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 24),
    _Aktuelle_ausgangsspannung_u5_s_7_Type()
)
aktuelle_ausgangsspannung_u5_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u5_s_7.setStatus("current")
_Aktuelle_ausgangsspannung_u6_s_7_Type = DisplayString
_Aktuelle_ausgangsspannung_u6_s_7_Object = MibTableColumn
aktuelle_ausgangsspannung_u6_s_7 = _Aktuelle_ausgangsspannung_u6_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 25),
    _Aktuelle_ausgangsspannung_u6_s_7_Type()
)
aktuelle_ausgangsspannung_u6_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u6_s_7.setStatus("current")
_Aktuelle_ausgangsspannung_u7_s_7_Type = DisplayString
_Aktuelle_ausgangsspannung_u7_s_7_Object = MibTableColumn
aktuelle_ausgangsspannung_u7_s_7 = _Aktuelle_ausgangsspannung_u7_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 26),
    _Aktuelle_ausgangsspannung_u7_s_7_Type()
)
aktuelle_ausgangsspannung_u7_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u7_s_7.setStatus("current")
_Aktuelle_ausgangsspannung_u8_s_7_Type = DisplayString
_Aktuelle_ausgangsspannung_u8_s_7_Object = MibTableColumn
aktuelle_ausgangsspannung_u8_s_7 = _Aktuelle_ausgangsspannung_u8_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 27),
    _Aktuelle_ausgangsspannung_u8_s_7_Type()
)
aktuelle_ausgangsspannung_u8_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u8_s_7.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_1_s_7_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_1_s_7_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_1_s_7 = _Aktuelle_ladespannung_an_akku_kreis_1_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 28),
    _Aktuelle_ladespannung_an_akku_kreis_1_s_7_Type()
)
aktuelle_ladespannung_an_akku_kreis_1_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_1_s_7.setStatus("current")
_Aktuelle_ladespannung_an_akku_Kreis_2_s_7_Type = DisplayString
_Aktuelle_ladespannung_an_akku_Kreis_2_s_7_Object = MibTableColumn
aktuelle_ladespannung_an_akku_Kreis_2_s_7 = _Aktuelle_ladespannung_an_akku_Kreis_2_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 29),
    _Aktuelle_ladespannung_an_akku_Kreis_2_s_7_Type()
)
aktuelle_ladespannung_an_akku_Kreis_2_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_Kreis_2_s_7.setStatus("current")
_Aktuelle_ladespannung_an_akku_Kreis_3_s_7_Type = DisplayString
_Aktuelle_ladespannung_an_akku_Kreis_3_s_7_Object = MibTableColumn
aktuelle_ladespannung_an_akku_Kreis_3_s_7 = _Aktuelle_ladespannung_an_akku_Kreis_3_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 30),
    _Aktuelle_ladespannung_an_akku_Kreis_3_s_7_Type()
)
aktuelle_ladespannung_an_akku_Kreis_3_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_Kreis_3_s_7.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_4_s_7_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_4_s_7_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_4_s_7 = _Aktuelle_ladespannung_an_akku_kreis_4_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 31),
    _Aktuelle_ladespannung_an_akku_kreis_4_s_7_Type()
)
aktuelle_ladespannung_an_akku_kreis_4_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_4_s_7.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_5_s_7_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_5_s_7_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_5_s_7 = _Aktuelle_ladespannung_an_akku_kreis_5_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 32),
    _Aktuelle_ladespannung_an_akku_kreis_5_s_7_Type()
)
aktuelle_ladespannung_an_akku_kreis_5_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_5_s_7.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_6_s_7_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_6_s_7_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_6_s_7 = _Aktuelle_ladespannung_an_akku_kreis_6_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 33),
    _Aktuelle_ladespannung_an_akku_kreis_6_s_7_Type()
)
aktuelle_ladespannung_an_akku_kreis_6_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_6_s_7.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_7_s_7_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_7_s_7_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_7_s_7 = _Aktuelle_ladespannung_an_akku_kreis_7_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 34),
    _Aktuelle_ladespannung_an_akku_kreis_7_s_7_Type()
)
aktuelle_ladespannung_an_akku_kreis_7_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_7_s_7.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_8_s_7_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_8_s_7_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_8_s_7 = _Aktuelle_ladespannung_an_akku_kreis_8_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 35),
    _Aktuelle_ladespannung_an_akku_kreis_8_s_7_Type()
)
aktuelle_ladespannung_an_akku_kreis_8_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_8_s_7.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_1_s_7_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_1_s_7_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_1_s_7 = _Aktuelle_spannung_an_akku_kreis_1_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 36),
    _Aktuelle_spannung_an_akku_kreis_1_s_7_Type()
)
aktuelle_spannung_an_akku_kreis_1_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_1_s_7.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_2_s_7_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_2_s_7_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_2_s_7 = _Aktuelle_spannung_an_akku_kreis_2_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 37),
    _Aktuelle_spannung_an_akku_kreis_2_s_7_Type()
)
aktuelle_spannung_an_akku_kreis_2_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_2_s_7.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_3_s_7_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_3_s_7_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_3_s_7 = _Aktuelle_spannung_an_akku_kreis_3_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 38),
    _Aktuelle_spannung_an_akku_kreis_3_s_7_Type()
)
aktuelle_spannung_an_akku_kreis_3_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_3_s_7.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_4_s_7_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_4_s_7_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_4_s_7 = _Aktuelle_spannung_an_akku_kreis_4_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 39),
    _Aktuelle_spannung_an_akku_kreis_4_s_7_Type()
)
aktuelle_spannung_an_akku_kreis_4_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_4_s_7.setStatus("current")
_Aktuelle_spannung_an_akku_reis_5_s_7_Type = DisplayString
_Aktuelle_spannung_an_akku_reis_5_s_7_Object = MibTableColumn
aktuelle_spannung_an_akku_reis_5_s_7 = _Aktuelle_spannung_an_akku_reis_5_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 40),
    _Aktuelle_spannung_an_akku_reis_5_s_7_Type()
)
aktuelle_spannung_an_akku_reis_5_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_reis_5_s_7.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_6_s_7_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_6_s_7_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_6_s_7 = _Aktuelle_spannung_an_akku_kreis_6_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 41),
    _Aktuelle_spannung_an_akku_kreis_6_s_7_Type()
)
aktuelle_spannung_an_akku_kreis_6_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_6_s_7.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_7_s_7_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_7_s_7_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_7_s_7 = _Aktuelle_spannung_an_akku_kreis_7_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 42),
    _Aktuelle_spannung_an_akku_kreis_7_s_7_Type()
)
aktuelle_spannung_an_akku_kreis_7_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_7_s_7.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_8_s_7_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_8_s_7_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_8_s_7 = _Aktuelle_spannung_an_akku_kreis_8_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 43),
    _Aktuelle_spannung_an_akku_kreis_8_s_7_Type()
)
aktuelle_spannung_an_akku_kreis_8_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_8_s_7.setStatus("current")
_Testergebnis_lastspannung_an_akku_reis_1_s_7_Type = DisplayString
_Testergebnis_lastspannung_an_akku_reis_1_s_7_Object = MibTableColumn
testergebnis_lastspannung_an_akku_reis_1_s_7 = _Testergebnis_lastspannung_an_akku_reis_1_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 44),
    _Testergebnis_lastspannung_an_akku_reis_1_s_7_Type()
)
testergebnis_lastspannung_an_akku_reis_1_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_reis_1_s_7.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_2_s_7_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_2_s_7_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_2_s_7 = _Testergebnis_lastspannung_an_akku_kreis_2_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 45),
    _Testergebnis_lastspannung_an_akku_kreis_2_s_7_Type()
)
testergebnis_lastspannung_an_akku_kreis_2_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_2_s_7.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_3_s_7_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_3_s_7_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_3_s_7 = _Testergebnis_lastspannung_an_akku_kreis_3_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 46),
    _Testergebnis_lastspannung_an_akku_kreis_3_s_7_Type()
)
testergebnis_lastspannung_an_akku_kreis_3_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_3_s_7.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_4_s_7_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_4_s_7_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_4_s_7 = _Testergebnis_lastspannung_an_akku_kreis_4_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 47),
    _Testergebnis_lastspannung_an_akku_kreis_4_s_7_Type()
)
testergebnis_lastspannung_an_akku_kreis_4_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_4_s_7.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_5_s_7_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_5_s_7_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_5_s_7 = _Testergebnis_lastspannung_an_akku_kreis_5_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 48),
    _Testergebnis_lastspannung_an_akku_kreis_5_s_7_Type()
)
testergebnis_lastspannung_an_akku_kreis_5_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_5_s_7.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_6_s_7_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_6_s_7_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_6_s_7 = _Testergebnis_lastspannung_an_akku_kreis_6_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 49),
    _Testergebnis_lastspannung_an_akku_kreis_6_s_7_Type()
)
testergebnis_lastspannung_an_akku_kreis_6_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_6_s_7.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_7_s_7_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_7_s_7_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_7_s_7 = _Testergebnis_lastspannung_an_akku_kreis_7_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 50),
    _Testergebnis_lastspannung_an_akku_kreis_7_s_7_Type()
)
testergebnis_lastspannung_an_akku_kreis_7_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_7_s_7.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_8_s_7_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_8_s_7_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_8_s_7 = _Testergebnis_lastspannung_an_akku_kreis_8_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 51),
    _Testergebnis_lastspannung_an_akku_kreis_8_s_7_Type()
)
testergebnis_lastspannung_an_akku_kreis_8_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_8_s_7.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_1_s_7_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_1_s_7_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_1_s_7 = _Testergebnis_innenwiderstand_akku_kreis_1_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 52),
    _Testergebnis_innenwiderstand_akku_kreis_1_s_7_Type()
)
testergebnis_innenwiderstand_akku_kreis_1_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_1_s_7.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_2_s_7_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_2_s_7_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_2_s_7 = _Testergebnis_innenwiderstand_akku_kreis_2_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 53),
    _Testergebnis_innenwiderstand_akku_kreis_2_s_7_Type()
)
testergebnis_innenwiderstand_akku_kreis_2_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_2_s_7.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_3_s_7_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_3_s_7_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_3_s_7 = _Testergebnis_innenwiderstand_akku_kreis_3_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 54),
    _Testergebnis_innenwiderstand_akku_kreis_3_s_7_Type()
)
testergebnis_innenwiderstand_akku_kreis_3_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_3_s_7.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_4_s_7_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_4_s_7_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_4_s_7 = _Testergebnis_innenwiderstand_akku_kreis_4_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 56),
    _Testergebnis_innenwiderstand_akku_kreis_4_s_7_Type()
)
testergebnis_innenwiderstand_akku_kreis_4_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_4_s_7.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_5_s_7_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_5_s_7_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_5_s_7 = _Testergebnis_innenwiderstand_akku_kreis_5_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 57),
    _Testergebnis_innenwiderstand_akku_kreis_5_s_7_Type()
)
testergebnis_innenwiderstand_akku_kreis_5_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_5_s_7.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_6_s_7_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_6_s_7_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_6_s_7 = _Testergebnis_innenwiderstand_akku_kreis_6_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 58),
    _Testergebnis_innenwiderstand_akku_kreis_6_s_7_Type()
)
testergebnis_innenwiderstand_akku_kreis_6_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_6_s_7.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_7_s_7_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_7_s_7_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_7_s_7 = _Testergebnis_innenwiderstand_akku_kreis_7_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 59),
    _Testergebnis_innenwiderstand_akku_kreis_7_s_7_Type()
)
testergebnis_innenwiderstand_akku_kreis_7_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_7_s_7.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_8_s_7_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_8_s_7_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_8_s_7 = _Testergebnis_innenwiderstand_akku_kreis_8_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 60),
    _Testergebnis_innenwiderstand_akku_kreis_8_s_7_Type()
)
testergebnis_innenwiderstand_akku_kreis_8_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_8_s_7.setStatus("current")
_Netzteilspannung_uin1_s_7_Type = DisplayString
_Netzteilspannung_uin1_s_7_Object = MibTableColumn
netzteilspannung_uin1_s_7 = _Netzteilspannung_uin1_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 61),
    _Netzteilspannung_uin1_s_7_Type()
)
netzteilspannung_uin1_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzteilspannung_uin1_s_7.setStatus("current")
_Netzteilspannung_uin2_s_7_Type = DisplayString
_Netzteilspannung_uin2_s_7_Object = MibTableColumn
netzteilspannung_uin2_s_7 = _Netzteilspannung_uin2_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 62),
    _Netzteilspannung_uin2_s_7_Type()
)
netzteilspannung_uin2_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzteilspannung_uin2_s_7.setStatus("current")
_Programmierte_minimale_soll_sendeleistung_s_7_Type = DisplayString
_Programmierte_minimale_soll_sendeleistung_s_7_Object = MibTableColumn
programmierte_minimale_soll_sendeleistung_s_7 = _Programmierte_minimale_soll_sendeleistung_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 63),
    _Programmierte_minimale_soll_sendeleistung_s_7_Type()
)
programmierte_minimale_soll_sendeleistung_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programmierte_minimale_soll_sendeleistung_s_7.setStatus("current")
_Programmierte_maximale_antennen_reflexion_s_7_Type = DisplayString
_Programmierte_maximale_antennen_reflexion_s_7_Object = MibTableColumn
programmierte_maximale_antennen_reflexion_s_7 = _Programmierte_maximale_antennen_reflexion_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 64),
    _Programmierte_maximale_antennen_reflexion_s_7_Type()
)
programmierte_maximale_antennen_reflexion_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programmierte_maximale_antennen_reflexion_s_7.setStatus("current")
_Programmierte_minimale_anzahl_praesenzsignale_s_7_Type = DisplayString
_Programmierte_minimale_anzahl_praesenzsignale_s_7_Object = MibTableColumn
programmierte_minimale_anzahl_praesenzsignale_s_7 = _Programmierte_minimale_anzahl_praesenzsignale_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 65),
    _Programmierte_minimale_anzahl_praesenzsignale_s_7_Type()
)
programmierte_minimale_anzahl_praesenzsignale_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programmierte_minimale_anzahl_praesenzsignale_s_7.setStatus("current")
_Summen_fehlerstatus_von_tmoa_anlage_s_7_Type = DisplayString
_Summen_fehlerstatus_von_tmoa_anlage_s_7_Object = MibTableColumn
summen_fehlerstatus_von_tmoa_anlage_s_7 = _Summen_fehlerstatus_von_tmoa_anlage_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 66),
    _Summen_fehlerstatus_von_tmoa_anlage_s_7_Type()
)
summen_fehlerstatus_von_tmoa_anlage_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summen_fehlerstatus_von_tmoa_anlage_s_7.setStatus("current")
_Summen_fehlerstatus_von_anbinderepeater_s_7_Type = DisplayString
_Summen_fehlerstatus_von_anbinderepeater_s_7_Object = MibTableColumn
summen_fehlerstatus_von_anbinderepeater_s_7 = _Summen_fehlerstatus_von_anbinderepeater_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 67),
    _Summen_fehlerstatus_von_anbinderepeater_s_7_Type()
)
summen_fehlerstatus_von_anbinderepeater_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summen_fehlerstatus_von_anbinderepeater_s_7.setStatus("current")
_Summen_fehlerstatus_von_analogem_repeater_s_7_Type = DisplayString
_Summen_fehlerstatus_von_analogem_repeater_s_7_Object = MibTableColumn
summen_fehlerstatus_von_analogem_repeater_s_7 = _Summen_fehlerstatus_von_analogem_repeater_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 68),
    _Summen_fehlerstatus_von_analogem_repeater_s_7_Type()
)
summen_fehlerstatus_von_analogem_repeater_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summen_fehlerstatus_von_analogem_repeater_s_7.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_7_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_7_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_7 = _Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 69),
    _Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_7_Type()
)
aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_7.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_7_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_7_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_7 = _Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 70),
    _Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_7_Type()
)
aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_7.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_7_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_7_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_7 = _Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 71),
    _Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_7_Type()
)
aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_7.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_7_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_7_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_7 = _Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 72),
    _Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_7_Type()
)
aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_7.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_7_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_7_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_7 = _Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 73),
    _Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_7_Type()
)
aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_7.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_7_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_7_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_7 = _Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 74),
    _Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_7_Type()
)
aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_7.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_7_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_7_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_7 = _Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 75),
    _Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_7_Type()
)
aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_7.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_7_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_7_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_7 = _Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 76),
    _Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_7_Type()
)
aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_7.setStatus("current")
_Netzspannungsversorgung_von_tmoa_anlage_s_7_Type = DisplayString
_Netzspannungsversorgung_von_tmoa_anlage_s_7_Object = MibTableColumn
netzspannungsversorgung_von_tmoa_anlage_s_7 = _Netzspannungsversorgung_von_tmoa_anlage_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 77),
    _Netzspannungsversorgung_von_tmoa_anlage_s_7_Type()
)
netzspannungsversorgung_von_tmoa_anlage_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzspannungsversorgung_von_tmoa_anlage_s_7.setStatus("current")
_Netzspannungsversorgung_von_anbinderepeater_s_7_Type = DisplayString
_Netzspannungsversorgung_von_anbinderepeater_s_7_Object = MibTableColumn
netzspannungsversorgung_von_anbinderepeater_s_7 = _Netzspannungsversorgung_von_anbinderepeater_s_7_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 1, 1, 78),
    _Netzspannungsversorgung_von_anbinderepeater_s_7_Type()
)
netzspannungsversorgung_von_anbinderepeater_s_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzspannungsversorgung_von_anbinderepeater_s_7.setStatus("current")
_Ak_slave_8_i_ObjectIdentity = ObjectIdentity
ak_slave_8_i = _Ak_slave_8_i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8)
)
_ModulTable_s_8_Object = MibTable
modulTable_s_8 = _ModulTable_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1)
)
if mibBuilder.loadTexts:
    modulTable_s_8.setStatus("current")
_ModulEntry_s_8_Object = MibTableRow
modulEntry_s_8 = _ModulEntry_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1)
)
modulEntry_s_8.setIndexNames(
    (0, "AK-FUNKTECHNIK-MIB", "modulIndex-s-8"),
)
if mibBuilder.loadTexts:
    modulEntry_s_8.setStatus("current")
_ModulIndex_s_8_Type = DisplayString
_ModulIndex_s_8_Object = MibTableColumn
modulIndex_s_8 = _ModulIndex_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 1),
    _ModulIndex_s_8_Type()
)
modulIndex_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulIndex_s_8.setStatus("current")
_Geraete_typ_s_8_Type = DisplayString
_Geraete_typ_s_8_Object = MibTableColumn
geraete_typ_s_8 = _Geraete_typ_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 2),
    _Geraete_typ_s_8_Type()
)
geraete_typ_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geraete_typ_s_8.setStatus("current")
_Betriebsstatus_s_8_Type = DisplayString
_Betriebsstatus_s_8_Object = MibTableColumn
betriebsstatus_s_8 = _Betriebsstatus_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 3),
    _Betriebsstatus_s_8_Type()
)
betriebsstatus_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    betriebsstatus_s_8.setStatus("current")
_Senderstatus_s_8_Type = DisplayString
_Senderstatus_s_8_Object = MibTableColumn
senderstatus_s_8 = _Senderstatus_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 4),
    _Senderstatus_s_8_Type()
)
senderstatus_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    senderstatus_s_8.setStatus("current")
_Fehlerstatus_s_8_Type = DisplayString
_Fehlerstatus_s_8_Object = MibTableColumn
fehlerstatus_s_8 = _Fehlerstatus_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 5),
    _Fehlerstatus_s_8_Type()
)
fehlerstatus_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fehlerstatus_s_8.setStatus("current")
_Dem_adapter_zugeordnete_funkgeraetetype_s_8_Type = DisplayString
_Dem_adapter_zugeordnete_funkgeraetetype_s_8_Object = MibTableColumn
dem_adapter_zugeordnete_funkgeraetetype_s_8 = _Dem_adapter_zugeordnete_funkgeraetetype_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 6),
    _Dem_adapter_zugeordnete_funkgeraetetype_s_8_Type()
)
dem_adapter_zugeordnete_funkgeraetetype_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dem_adapter_zugeordnete_funkgeraetetype_s_8.setStatus("current")
_Eingabe_und_anzeigemodul_s_8_Type = DisplayString
_Eingabe_und_anzeigemodul_s_8_Object = MibTableColumn
eingabe_und_anzeigemodul_s_8 = _Eingabe_und_anzeigemodul_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 7),
    _Eingabe_und_anzeigemodul_s_8_Type()
)
eingabe_und_anzeigemodul_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eingabe_und_anzeigemodul_s_8.setStatus("current")
_Mod_bus_verbindung_module_s_8_Type = DisplayString
_Mod_bus_verbindung_module_s_8_Object = MibTableColumn
mod_bus_verbindung_module_s_8 = _Mod_bus_verbindung_module_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 8),
    _Mod_bus_verbindung_module_s_8_Type()
)
mod_bus_verbindung_module_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mod_bus_verbindung_module_s_8.setStatus("current")
_Gemessene_sendeleistung_im_testmode_s_8_Type = DisplayString
_Gemessene_sendeleistung_im_testmode_s_8_Object = MibTableColumn
gemessene_sendeleistung_im_testmode_s_8 = _Gemessene_sendeleistung_im_testmode_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 9),
    _Gemessene_sendeleistung_im_testmode_s_8_Type()
)
gemessene_sendeleistung_im_testmode_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemessene_sendeleistung_im_testmode_s_8.setStatus("current")
_Aktuelle_sendeleistung_s_8_Type = DisplayString
_Aktuelle_sendeleistung_s_8_Object = MibTableColumn
aktuelle_sendeleistung_s_8 = _Aktuelle_sendeleistung_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 10),
    _Aktuelle_sendeleistung_s_8_Type()
)
aktuelle_sendeleistung_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_sendeleistung_s_8.setStatus("current")
_Gemessene_reflexion_im_testmode_s_8_Type = DisplayString
_Gemessene_reflexion_im_testmode_s_8_Object = MibTableColumn
gemessene_reflexion_im_testmode_s_8 = _Gemessene_reflexion_im_testmode_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 11),
    _Gemessene_reflexion_im_testmode_s_8_Type()
)
gemessene_reflexion_im_testmode_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemessene_reflexion_im_testmode_s_8.setStatus("current")
_Aktuelle_reflexion_s_8_Type = DisplayString
_Aktuelle_reflexion_s_8_Object = MibTableColumn
aktuelle_reflexion_s_8 = _Aktuelle_reflexion_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 12),
    _Aktuelle_reflexion_s_8_Type()
)
aktuelle_reflexion_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_reflexion_s_8.setStatus("current")
_Letzte_gemessene_donor_sendeleistung_s_8_Type = DisplayString
_Letzte_gemessene_donor_sendeleistung_s_8_Object = MibTableColumn
letzte_gemessene_donor_sendeleistung_s_8 = _Letzte_gemessene_donor_sendeleistung_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 13),
    _Letzte_gemessene_donor_sendeleistung_s_8_Type()
)
letzte_gemessene_donor_sendeleistung_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    letzte_gemessene_donor_sendeleistung_s_8.setStatus("current")
_Aktuelle_donor_sendeleistung_s_8_Type = DisplayString
_Aktuelle_donor_sendeleistung_s_8_Object = MibTableColumn
aktuelle_donor_sendeleistung_s_8 = _Aktuelle_donor_sendeleistung_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 14),
    _Aktuelle_donor_sendeleistung_s_8_Type()
)
aktuelle_donor_sendeleistung_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_donor_sendeleistung_s_8.setStatus("current")
_Letzte_gemessene_donor_reflexion_s_8_Type = DisplayString
_Letzte_gemessene_donor_reflexion_s_8_Object = MibTableColumn
letzte_gemessene_donor_reflexion_s_8 = _Letzte_gemessene_donor_reflexion_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 15),
    _Letzte_gemessene_donor_reflexion_s_8_Type()
)
letzte_gemessene_donor_reflexion_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    letzte_gemessene_donor_reflexion_s_8.setStatus("current")
_Aktuelle_donor_reflexion_s_8_Type = DisplayString
_Aktuelle_donor_reflexion_s_8_Object = MibTableColumn
aktuelle_donor_reflexion_s_8 = _Aktuelle_donor_reflexion_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 16),
    _Aktuelle_donor_reflexion_s_8_Type()
)
aktuelle_donor_reflexion_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_donor_reflexion_s_8.setStatus("current")
_Anzahl_gemessener_praesenzsignale_im_testmode_s_8_Type = DisplayString
_Anzahl_gemessener_praesenzsignale_im_testmode_s_8_Object = MibTableColumn
anzahl_gemessener_praesenzsignale_im_testmode_s_8 = _Anzahl_gemessener_praesenzsignale_im_testmode_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 18),
    _Anzahl_gemessener_praesenzsignale_im_testmode_s_8_Type()
)
anzahl_gemessener_praesenzsignale_im_testmode_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anzahl_gemessener_praesenzsignale_im_testmode_s_8.setStatus("current")
_Aktuelle_ausgangsspannung_ub_s_8_Type = DisplayString
_Aktuelle_ausgangsspannung_ub_s_8_Object = MibTableColumn
aktuelle_ausgangsspannung_ub_s_8 = _Aktuelle_ausgangsspannung_ub_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 19),
    _Aktuelle_ausgangsspannung_ub_s_8_Type()
)
aktuelle_ausgangsspannung_ub_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_ub_s_8.setStatus("current")
_Aktuelle_ausgangsspannung_u1_s_8_Type = DisplayString
_Aktuelle_ausgangsspannung_u1_s_8_Object = MibTableColumn
aktuelle_ausgangsspannung_u1_s_8 = _Aktuelle_ausgangsspannung_u1_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 20),
    _Aktuelle_ausgangsspannung_u1_s_8_Type()
)
aktuelle_ausgangsspannung_u1_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u1_s_8.setStatus("current")
_Aktuelle_ausgangsspannung_u2_s_8_Type = DisplayString
_Aktuelle_ausgangsspannung_u2_s_8_Object = MibTableColumn
aktuelle_ausgangsspannung_u2_s_8 = _Aktuelle_ausgangsspannung_u2_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 21),
    _Aktuelle_ausgangsspannung_u2_s_8_Type()
)
aktuelle_ausgangsspannung_u2_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u2_s_8.setStatus("current")
_Aktuelle_ausgangsspannung_u3_s_8_Type = DisplayString
_Aktuelle_ausgangsspannung_u3_s_8_Object = MibTableColumn
aktuelle_ausgangsspannung_u3_s_8 = _Aktuelle_ausgangsspannung_u3_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 22),
    _Aktuelle_ausgangsspannung_u3_s_8_Type()
)
aktuelle_ausgangsspannung_u3_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u3_s_8.setStatus("current")
_Aktuelle_ausgangsspannung_u4_s_8_Type = DisplayString
_Aktuelle_ausgangsspannung_u4_s_8_Object = MibTableColumn
aktuelle_ausgangsspannung_u4_s_8 = _Aktuelle_ausgangsspannung_u4_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 23),
    _Aktuelle_ausgangsspannung_u4_s_8_Type()
)
aktuelle_ausgangsspannung_u4_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u4_s_8.setStatus("current")
_Aktuelle_ausgangsspannung_u5_s_8_Type = DisplayString
_Aktuelle_ausgangsspannung_u5_s_8_Object = MibTableColumn
aktuelle_ausgangsspannung_u5_s_8 = _Aktuelle_ausgangsspannung_u5_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 24),
    _Aktuelle_ausgangsspannung_u5_s_8_Type()
)
aktuelle_ausgangsspannung_u5_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u5_s_8.setStatus("current")
_Aktuelle_ausgangsspannung_u6_s_8_Type = DisplayString
_Aktuelle_ausgangsspannung_u6_s_8_Object = MibTableColumn
aktuelle_ausgangsspannung_u6_s_8 = _Aktuelle_ausgangsspannung_u6_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 25),
    _Aktuelle_ausgangsspannung_u6_s_8_Type()
)
aktuelle_ausgangsspannung_u6_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u6_s_8.setStatus("current")
_Aktuelle_ausgangsspannung_u7_s_8_Type = DisplayString
_Aktuelle_ausgangsspannung_u7_s_8_Object = MibTableColumn
aktuelle_ausgangsspannung_u7_s_8 = _Aktuelle_ausgangsspannung_u7_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 26),
    _Aktuelle_ausgangsspannung_u7_s_8_Type()
)
aktuelle_ausgangsspannung_u7_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u7_s_8.setStatus("current")
_Aktuelle_ausgangsspannung_u8_s_8_Type = DisplayString
_Aktuelle_ausgangsspannung_u8_s_8_Object = MibTableColumn
aktuelle_ausgangsspannung_u8_s_8 = _Aktuelle_ausgangsspannung_u8_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 27),
    _Aktuelle_ausgangsspannung_u8_s_8_Type()
)
aktuelle_ausgangsspannung_u8_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u8_s_8.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_1_s_8_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_1_s_8_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_1_s_8 = _Aktuelle_ladespannung_an_akku_kreis_1_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 28),
    _Aktuelle_ladespannung_an_akku_kreis_1_s_8_Type()
)
aktuelle_ladespannung_an_akku_kreis_1_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_1_s_8.setStatus("current")
_Aktuelle_ladespannung_an_akku_Kreis_2_s_8_Type = DisplayString
_Aktuelle_ladespannung_an_akku_Kreis_2_s_8_Object = MibTableColumn
aktuelle_ladespannung_an_akku_Kreis_2_s_8 = _Aktuelle_ladespannung_an_akku_Kreis_2_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 29),
    _Aktuelle_ladespannung_an_akku_Kreis_2_s_8_Type()
)
aktuelle_ladespannung_an_akku_Kreis_2_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_Kreis_2_s_8.setStatus("current")
_Aktuelle_ladespannung_an_akku_Kreis_3_s_8_Type = DisplayString
_Aktuelle_ladespannung_an_akku_Kreis_3_s_8_Object = MibTableColumn
aktuelle_ladespannung_an_akku_Kreis_3_s_8 = _Aktuelle_ladespannung_an_akku_Kreis_3_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 30),
    _Aktuelle_ladespannung_an_akku_Kreis_3_s_8_Type()
)
aktuelle_ladespannung_an_akku_Kreis_3_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_Kreis_3_s_8.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_4_s_8_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_4_s_8_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_4_s_8 = _Aktuelle_ladespannung_an_akku_kreis_4_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 31),
    _Aktuelle_ladespannung_an_akku_kreis_4_s_8_Type()
)
aktuelle_ladespannung_an_akku_kreis_4_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_4_s_8.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_5_s_8_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_5_s_8_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_5_s_8 = _Aktuelle_ladespannung_an_akku_kreis_5_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 32),
    _Aktuelle_ladespannung_an_akku_kreis_5_s_8_Type()
)
aktuelle_ladespannung_an_akku_kreis_5_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_5_s_8.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_6_s_8_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_6_s_8_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_6_s_8 = _Aktuelle_ladespannung_an_akku_kreis_6_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 33),
    _Aktuelle_ladespannung_an_akku_kreis_6_s_8_Type()
)
aktuelle_ladespannung_an_akku_kreis_6_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_6_s_8.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_7_s_8_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_7_s_8_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_7_s_8 = _Aktuelle_ladespannung_an_akku_kreis_7_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 34),
    _Aktuelle_ladespannung_an_akku_kreis_7_s_8_Type()
)
aktuelle_ladespannung_an_akku_kreis_7_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_7_s_8.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_8_s_8_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_8_s_8_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_8_s_8 = _Aktuelle_ladespannung_an_akku_kreis_8_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 35),
    _Aktuelle_ladespannung_an_akku_kreis_8_s_8_Type()
)
aktuelle_ladespannung_an_akku_kreis_8_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_8_s_8.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_1_s_8_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_1_s_8_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_1_s_8 = _Aktuelle_spannung_an_akku_kreis_1_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 36),
    _Aktuelle_spannung_an_akku_kreis_1_s_8_Type()
)
aktuelle_spannung_an_akku_kreis_1_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_1_s_8.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_2_s_8_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_2_s_8_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_2_s_8 = _Aktuelle_spannung_an_akku_kreis_2_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 37),
    _Aktuelle_spannung_an_akku_kreis_2_s_8_Type()
)
aktuelle_spannung_an_akku_kreis_2_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_2_s_8.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_3_s_8_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_3_s_8_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_3_s_8 = _Aktuelle_spannung_an_akku_kreis_3_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 38),
    _Aktuelle_spannung_an_akku_kreis_3_s_8_Type()
)
aktuelle_spannung_an_akku_kreis_3_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_3_s_8.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_4_s_8_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_4_s_8_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_4_s_8 = _Aktuelle_spannung_an_akku_kreis_4_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 39),
    _Aktuelle_spannung_an_akku_kreis_4_s_8_Type()
)
aktuelle_spannung_an_akku_kreis_4_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_4_s_8.setStatus("current")
_Aktuelle_spannung_an_akku_reis_5_s_8_Type = DisplayString
_Aktuelle_spannung_an_akku_reis_5_s_8_Object = MibTableColumn
aktuelle_spannung_an_akku_reis_5_s_8 = _Aktuelle_spannung_an_akku_reis_5_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 40),
    _Aktuelle_spannung_an_akku_reis_5_s_8_Type()
)
aktuelle_spannung_an_akku_reis_5_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_reis_5_s_8.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_6_s_8_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_6_s_8_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_6_s_8 = _Aktuelle_spannung_an_akku_kreis_6_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 41),
    _Aktuelle_spannung_an_akku_kreis_6_s_8_Type()
)
aktuelle_spannung_an_akku_kreis_6_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_6_s_8.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_7_s_8_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_7_s_8_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_7_s_8 = _Aktuelle_spannung_an_akku_kreis_7_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 42),
    _Aktuelle_spannung_an_akku_kreis_7_s_8_Type()
)
aktuelle_spannung_an_akku_kreis_7_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_7_s_8.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_8_s_8_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_8_s_8_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_8_s_8 = _Aktuelle_spannung_an_akku_kreis_8_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 43),
    _Aktuelle_spannung_an_akku_kreis_8_s_8_Type()
)
aktuelle_spannung_an_akku_kreis_8_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_8_s_8.setStatus("current")
_Testergebnis_lastspannung_an_akku_reis_1_s_8_Type = DisplayString
_Testergebnis_lastspannung_an_akku_reis_1_s_8_Object = MibTableColumn
testergebnis_lastspannung_an_akku_reis_1_s_8 = _Testergebnis_lastspannung_an_akku_reis_1_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 44),
    _Testergebnis_lastspannung_an_akku_reis_1_s_8_Type()
)
testergebnis_lastspannung_an_akku_reis_1_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_reis_1_s_8.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_2_s_8_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_2_s_8_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_2_s_8 = _Testergebnis_lastspannung_an_akku_kreis_2_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 45),
    _Testergebnis_lastspannung_an_akku_kreis_2_s_8_Type()
)
testergebnis_lastspannung_an_akku_kreis_2_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_2_s_8.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_3_s_8_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_3_s_8_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_3_s_8 = _Testergebnis_lastspannung_an_akku_kreis_3_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 46),
    _Testergebnis_lastspannung_an_akku_kreis_3_s_8_Type()
)
testergebnis_lastspannung_an_akku_kreis_3_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_3_s_8.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_4_s_8_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_4_s_8_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_4_s_8 = _Testergebnis_lastspannung_an_akku_kreis_4_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 47),
    _Testergebnis_lastspannung_an_akku_kreis_4_s_8_Type()
)
testergebnis_lastspannung_an_akku_kreis_4_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_4_s_8.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_5_s_8_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_5_s_8_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_5_s_8 = _Testergebnis_lastspannung_an_akku_kreis_5_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 48),
    _Testergebnis_lastspannung_an_akku_kreis_5_s_8_Type()
)
testergebnis_lastspannung_an_akku_kreis_5_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_5_s_8.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_6_s_8_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_6_s_8_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_6_s_8 = _Testergebnis_lastspannung_an_akku_kreis_6_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 49),
    _Testergebnis_lastspannung_an_akku_kreis_6_s_8_Type()
)
testergebnis_lastspannung_an_akku_kreis_6_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_6_s_8.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_7_s_8_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_7_s_8_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_7_s_8 = _Testergebnis_lastspannung_an_akku_kreis_7_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 50),
    _Testergebnis_lastspannung_an_akku_kreis_7_s_8_Type()
)
testergebnis_lastspannung_an_akku_kreis_7_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_7_s_8.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_8_s_8_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_8_s_8_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_8_s_8 = _Testergebnis_lastspannung_an_akku_kreis_8_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 51),
    _Testergebnis_lastspannung_an_akku_kreis_8_s_8_Type()
)
testergebnis_lastspannung_an_akku_kreis_8_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_8_s_8.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_1_s_8_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_1_s_8_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_1_s_8 = _Testergebnis_innenwiderstand_akku_kreis_1_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 52),
    _Testergebnis_innenwiderstand_akku_kreis_1_s_8_Type()
)
testergebnis_innenwiderstand_akku_kreis_1_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_1_s_8.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_2_s_8_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_2_s_8_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_2_s_8 = _Testergebnis_innenwiderstand_akku_kreis_2_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 53),
    _Testergebnis_innenwiderstand_akku_kreis_2_s_8_Type()
)
testergebnis_innenwiderstand_akku_kreis_2_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_2_s_8.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_3_s_8_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_3_s_8_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_3_s_8 = _Testergebnis_innenwiderstand_akku_kreis_3_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 54),
    _Testergebnis_innenwiderstand_akku_kreis_3_s_8_Type()
)
testergebnis_innenwiderstand_akku_kreis_3_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_3_s_8.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_4_s_8_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_4_s_8_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_4_s_8 = _Testergebnis_innenwiderstand_akku_kreis_4_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 56),
    _Testergebnis_innenwiderstand_akku_kreis_4_s_8_Type()
)
testergebnis_innenwiderstand_akku_kreis_4_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_4_s_8.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_5_s_8_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_5_s_8_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_5_s_8 = _Testergebnis_innenwiderstand_akku_kreis_5_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 57),
    _Testergebnis_innenwiderstand_akku_kreis_5_s_8_Type()
)
testergebnis_innenwiderstand_akku_kreis_5_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_5_s_8.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_6_s_8_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_6_s_8_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_6_s_8 = _Testergebnis_innenwiderstand_akku_kreis_6_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 58),
    _Testergebnis_innenwiderstand_akku_kreis_6_s_8_Type()
)
testergebnis_innenwiderstand_akku_kreis_6_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_6_s_8.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_7_s_8_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_7_s_8_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_7_s_8 = _Testergebnis_innenwiderstand_akku_kreis_7_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 59),
    _Testergebnis_innenwiderstand_akku_kreis_7_s_8_Type()
)
testergebnis_innenwiderstand_akku_kreis_7_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_7_s_8.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_8_s_8_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_8_s_8_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_8_s_8 = _Testergebnis_innenwiderstand_akku_kreis_8_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 60),
    _Testergebnis_innenwiderstand_akku_kreis_8_s_8_Type()
)
testergebnis_innenwiderstand_akku_kreis_8_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_8_s_8.setStatus("current")
_Netzteilspannung_uin1_s_8_Type = DisplayString
_Netzteilspannung_uin1_s_8_Object = MibTableColumn
netzteilspannung_uin1_s_8 = _Netzteilspannung_uin1_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 61),
    _Netzteilspannung_uin1_s_8_Type()
)
netzteilspannung_uin1_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzteilspannung_uin1_s_8.setStatus("current")
_Netzteilspannung_uin2_s_8_Type = DisplayString
_Netzteilspannung_uin2_s_8_Object = MibTableColumn
netzteilspannung_uin2_s_8 = _Netzteilspannung_uin2_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 62),
    _Netzteilspannung_uin2_s_8_Type()
)
netzteilspannung_uin2_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzteilspannung_uin2_s_8.setStatus("current")
_Programmierte_minimale_soll_sendeleistung_s_8_Type = DisplayString
_Programmierte_minimale_soll_sendeleistung_s_8_Object = MibTableColumn
programmierte_minimale_soll_sendeleistung_s_8 = _Programmierte_minimale_soll_sendeleistung_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 63),
    _Programmierte_minimale_soll_sendeleistung_s_8_Type()
)
programmierte_minimale_soll_sendeleistung_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programmierte_minimale_soll_sendeleistung_s_8.setStatus("current")
_Programmierte_maximale_antennen_reflexion_s_8_Type = DisplayString
_Programmierte_maximale_antennen_reflexion_s_8_Object = MibTableColumn
programmierte_maximale_antennen_reflexion_s_8 = _Programmierte_maximale_antennen_reflexion_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 64),
    _Programmierte_maximale_antennen_reflexion_s_8_Type()
)
programmierte_maximale_antennen_reflexion_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programmierte_maximale_antennen_reflexion_s_8.setStatus("current")
_Programmierte_minimale_anzahl_praesenzsignale_s_8_Type = DisplayString
_Programmierte_minimale_anzahl_praesenzsignale_s_8_Object = MibTableColumn
programmierte_minimale_anzahl_praesenzsignale_s_8 = _Programmierte_minimale_anzahl_praesenzsignale_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 65),
    _Programmierte_minimale_anzahl_praesenzsignale_s_8_Type()
)
programmierte_minimale_anzahl_praesenzsignale_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programmierte_minimale_anzahl_praesenzsignale_s_8.setStatus("current")
_Summen_fehlerstatus_von_tmoa_anlage_s_8_Type = DisplayString
_Summen_fehlerstatus_von_tmoa_anlage_s_8_Object = MibTableColumn
summen_fehlerstatus_von_tmoa_anlage_s_8 = _Summen_fehlerstatus_von_tmoa_anlage_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 66),
    _Summen_fehlerstatus_von_tmoa_anlage_s_8_Type()
)
summen_fehlerstatus_von_tmoa_anlage_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summen_fehlerstatus_von_tmoa_anlage_s_8.setStatus("current")
_Summen_fehlerstatus_von_anbinderepeater_s_8_Type = DisplayString
_Summen_fehlerstatus_von_anbinderepeater_s_8_Object = MibTableColumn
summen_fehlerstatus_von_anbinderepeater_s_8 = _Summen_fehlerstatus_von_anbinderepeater_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 67),
    _Summen_fehlerstatus_von_anbinderepeater_s_8_Type()
)
summen_fehlerstatus_von_anbinderepeater_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summen_fehlerstatus_von_anbinderepeater_s_8.setStatus("current")
_Summen_fehlerstatus_von_analogem_repeater_s_8_Type = DisplayString
_Summen_fehlerstatus_von_analogem_repeater_s_8_Object = MibTableColumn
summen_fehlerstatus_von_analogem_repeater_s_8 = _Summen_fehlerstatus_von_analogem_repeater_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 68),
    _Summen_fehlerstatus_von_analogem_repeater_s_8_Type()
)
summen_fehlerstatus_von_analogem_repeater_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summen_fehlerstatus_von_analogem_repeater_s_8.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_8_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_8_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_8 = _Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 69),
    _Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_8_Type()
)
aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_8.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_8_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_8_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_8 = _Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 70),
    _Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_8_Type()
)
aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_8.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_8_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_8_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_8 = _Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 71),
    _Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_8_Type()
)
aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_8.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_8_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_8_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_8 = _Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 72),
    _Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_8_Type()
)
aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_8.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_8_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_8_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_8 = _Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 73),
    _Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_8_Type()
)
aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_8.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_8_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_8_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_8 = _Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 74),
    _Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_8_Type()
)
aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_8.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_8_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_8_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_8 = _Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 75),
    _Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_8_Type()
)
aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_8.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_8_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_8_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_8 = _Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 76),
    _Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_8_Type()
)
aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_8.setStatus("current")
_Netzspannungsversorgung_von_tmoa_anlage_s_8_Type = DisplayString
_Netzspannungsversorgung_von_tmoa_anlage_s_8_Object = MibTableColumn
netzspannungsversorgung_von_tmoa_anlage_s_8 = _Netzspannungsversorgung_von_tmoa_anlage_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 77),
    _Netzspannungsversorgung_von_tmoa_anlage_s_8_Type()
)
netzspannungsversorgung_von_tmoa_anlage_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzspannungsversorgung_von_tmoa_anlage_s_8.setStatus("current")
_Netzspannungsversorgung_von_anbinderepeater_s_8_Type = DisplayString
_Netzspannungsversorgung_von_anbinderepeater_s_8_Object = MibTableColumn
netzspannungsversorgung_von_anbinderepeater_s_8 = _Netzspannungsversorgung_von_anbinderepeater_s_8_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 1, 1, 78),
    _Netzspannungsversorgung_von_anbinderepeater_s_8_Type()
)
netzspannungsversorgung_von_anbinderepeater_s_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzspannungsversorgung_von_anbinderepeater_s_8.setStatus("current")
_Ak_slave_9_i_ObjectIdentity = ObjectIdentity
ak_slave_9_i = _Ak_slave_9_i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9)
)
_ModulTable_s_9_Object = MibTable
modulTable_s_9 = _ModulTable_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1)
)
if mibBuilder.loadTexts:
    modulTable_s_9.setStatus("current")
_ModulEntry_s_9_Object = MibTableRow
modulEntry_s_9 = _ModulEntry_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1)
)
modulEntry_s_9.setIndexNames(
    (0, "AK-FUNKTECHNIK-MIB", "modulIndex-s-9"),
)
if mibBuilder.loadTexts:
    modulEntry_s_9.setStatus("current")
_ModulIndex_s_9_Type = DisplayString
_ModulIndex_s_9_Object = MibTableColumn
modulIndex_s_9 = _ModulIndex_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 1),
    _ModulIndex_s_9_Type()
)
modulIndex_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulIndex_s_9.setStatus("current")
_Geraete_typ_s_9_Type = DisplayString
_Geraete_typ_s_9_Object = MibTableColumn
geraete_typ_s_9 = _Geraete_typ_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 2),
    _Geraete_typ_s_9_Type()
)
geraete_typ_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geraete_typ_s_9.setStatus("current")
_Betriebsstatus_s_9_Type = DisplayString
_Betriebsstatus_s_9_Object = MibTableColumn
betriebsstatus_s_9 = _Betriebsstatus_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 3),
    _Betriebsstatus_s_9_Type()
)
betriebsstatus_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    betriebsstatus_s_9.setStatus("current")
_Senderstatus_s_9_Type = DisplayString
_Senderstatus_s_9_Object = MibTableColumn
senderstatus_s_9 = _Senderstatus_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 4),
    _Senderstatus_s_9_Type()
)
senderstatus_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    senderstatus_s_9.setStatus("current")
_Fehlerstatus_s_9_Type = DisplayString
_Fehlerstatus_s_9_Object = MibTableColumn
fehlerstatus_s_9 = _Fehlerstatus_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 5),
    _Fehlerstatus_s_9_Type()
)
fehlerstatus_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fehlerstatus_s_9.setStatus("current")
_Dem_adapter_zugeordnete_funkgeraetetype_s_9_Type = DisplayString
_Dem_adapter_zugeordnete_funkgeraetetype_s_9_Object = MibTableColumn
dem_adapter_zugeordnete_funkgeraetetype_s_9 = _Dem_adapter_zugeordnete_funkgeraetetype_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 6),
    _Dem_adapter_zugeordnete_funkgeraetetype_s_9_Type()
)
dem_adapter_zugeordnete_funkgeraetetype_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dem_adapter_zugeordnete_funkgeraetetype_s_9.setStatus("current")
_Eingabe_und_anzeigemodul_s_9_Type = DisplayString
_Eingabe_und_anzeigemodul_s_9_Object = MibTableColumn
eingabe_und_anzeigemodul_s_9 = _Eingabe_und_anzeigemodul_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 7),
    _Eingabe_und_anzeigemodul_s_9_Type()
)
eingabe_und_anzeigemodul_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eingabe_und_anzeigemodul_s_9.setStatus("current")
_Mod_bus_verbindung_module_s_9_Type = DisplayString
_Mod_bus_verbindung_module_s_9_Object = MibTableColumn
mod_bus_verbindung_module_s_9 = _Mod_bus_verbindung_module_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 8),
    _Mod_bus_verbindung_module_s_9_Type()
)
mod_bus_verbindung_module_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mod_bus_verbindung_module_s_9.setStatus("current")
_Gemessene_sendeleistung_im_testmode_s_9_Type = DisplayString
_Gemessene_sendeleistung_im_testmode_s_9_Object = MibTableColumn
gemessene_sendeleistung_im_testmode_s_9 = _Gemessene_sendeleistung_im_testmode_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 9),
    _Gemessene_sendeleistung_im_testmode_s_9_Type()
)
gemessene_sendeleistung_im_testmode_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemessene_sendeleistung_im_testmode_s_9.setStatus("current")
_Aktuelle_sendeleistung_s_9_Type = DisplayString
_Aktuelle_sendeleistung_s_9_Object = MibTableColumn
aktuelle_sendeleistung_s_9 = _Aktuelle_sendeleistung_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 10),
    _Aktuelle_sendeleistung_s_9_Type()
)
aktuelle_sendeleistung_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_sendeleistung_s_9.setStatus("current")
_Gemessene_reflexion_im_testmode_s_9_Type = DisplayString
_Gemessene_reflexion_im_testmode_s_9_Object = MibTableColumn
gemessene_reflexion_im_testmode_s_9 = _Gemessene_reflexion_im_testmode_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 11),
    _Gemessene_reflexion_im_testmode_s_9_Type()
)
gemessene_reflexion_im_testmode_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemessene_reflexion_im_testmode_s_9.setStatus("current")
_Aktuelle_reflexion_s_9_Type = DisplayString
_Aktuelle_reflexion_s_9_Object = MibTableColumn
aktuelle_reflexion_s_9 = _Aktuelle_reflexion_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 12),
    _Aktuelle_reflexion_s_9_Type()
)
aktuelle_reflexion_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_reflexion_s_9.setStatus("current")
_Letzte_gemessene_donor_sendeleistung_s_9_Type = DisplayString
_Letzte_gemessene_donor_sendeleistung_s_9_Object = MibTableColumn
letzte_gemessene_donor_sendeleistung_s_9 = _Letzte_gemessene_donor_sendeleistung_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 13),
    _Letzte_gemessene_donor_sendeleistung_s_9_Type()
)
letzte_gemessene_donor_sendeleistung_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    letzte_gemessene_donor_sendeleistung_s_9.setStatus("current")
_Aktuelle_donor_sendeleistung_s_9_Type = DisplayString
_Aktuelle_donor_sendeleistung_s_9_Object = MibTableColumn
aktuelle_donor_sendeleistung_s_9 = _Aktuelle_donor_sendeleistung_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 14),
    _Aktuelle_donor_sendeleistung_s_9_Type()
)
aktuelle_donor_sendeleistung_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_donor_sendeleistung_s_9.setStatus("current")
_Letzte_gemessene_donor_reflexion_s_9_Type = DisplayString
_Letzte_gemessene_donor_reflexion_s_9_Object = MibTableColumn
letzte_gemessene_donor_reflexion_s_9 = _Letzte_gemessene_donor_reflexion_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 15),
    _Letzte_gemessene_donor_reflexion_s_9_Type()
)
letzte_gemessene_donor_reflexion_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    letzte_gemessene_donor_reflexion_s_9.setStatus("current")
_Aktuelle_donor_reflexion_s_9_Type = DisplayString
_Aktuelle_donor_reflexion_s_9_Object = MibTableColumn
aktuelle_donor_reflexion_s_9 = _Aktuelle_donor_reflexion_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 16),
    _Aktuelle_donor_reflexion_s_9_Type()
)
aktuelle_donor_reflexion_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_donor_reflexion_s_9.setStatus("current")
_Anzahl_gemessener_praesenzsignale_im_testmode_s_9_Type = DisplayString
_Anzahl_gemessener_praesenzsignale_im_testmode_s_9_Object = MibTableColumn
anzahl_gemessener_praesenzsignale_im_testmode_s_9 = _Anzahl_gemessener_praesenzsignale_im_testmode_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 18),
    _Anzahl_gemessener_praesenzsignale_im_testmode_s_9_Type()
)
anzahl_gemessener_praesenzsignale_im_testmode_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anzahl_gemessener_praesenzsignale_im_testmode_s_9.setStatus("current")
_Aktuelle_ausgangsspannung_ub_s_9_Type = DisplayString
_Aktuelle_ausgangsspannung_ub_s_9_Object = MibTableColumn
aktuelle_ausgangsspannung_ub_s_9 = _Aktuelle_ausgangsspannung_ub_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 19),
    _Aktuelle_ausgangsspannung_ub_s_9_Type()
)
aktuelle_ausgangsspannung_ub_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_ub_s_9.setStatus("current")
_Aktuelle_ausgangsspannung_u1_s_9_Type = DisplayString
_Aktuelle_ausgangsspannung_u1_s_9_Object = MibTableColumn
aktuelle_ausgangsspannung_u1_s_9 = _Aktuelle_ausgangsspannung_u1_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 20),
    _Aktuelle_ausgangsspannung_u1_s_9_Type()
)
aktuelle_ausgangsspannung_u1_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u1_s_9.setStatus("current")
_Aktuelle_ausgangsspannung_u2_s_9_Type = DisplayString
_Aktuelle_ausgangsspannung_u2_s_9_Object = MibTableColumn
aktuelle_ausgangsspannung_u2_s_9 = _Aktuelle_ausgangsspannung_u2_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 21),
    _Aktuelle_ausgangsspannung_u2_s_9_Type()
)
aktuelle_ausgangsspannung_u2_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u2_s_9.setStatus("current")
_Aktuelle_ausgangsspannung_u3_s_9_Type = DisplayString
_Aktuelle_ausgangsspannung_u3_s_9_Object = MibTableColumn
aktuelle_ausgangsspannung_u3_s_9 = _Aktuelle_ausgangsspannung_u3_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 22),
    _Aktuelle_ausgangsspannung_u3_s_9_Type()
)
aktuelle_ausgangsspannung_u3_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u3_s_9.setStatus("current")
_Aktuelle_ausgangsspannung_u4_s_9_Type = DisplayString
_Aktuelle_ausgangsspannung_u4_s_9_Object = MibTableColumn
aktuelle_ausgangsspannung_u4_s_9 = _Aktuelle_ausgangsspannung_u4_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 23),
    _Aktuelle_ausgangsspannung_u4_s_9_Type()
)
aktuelle_ausgangsspannung_u4_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u4_s_9.setStatus("current")
_Aktuelle_ausgangsspannung_u5_s_9_Type = DisplayString
_Aktuelle_ausgangsspannung_u5_s_9_Object = MibTableColumn
aktuelle_ausgangsspannung_u5_s_9 = _Aktuelle_ausgangsspannung_u5_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 24),
    _Aktuelle_ausgangsspannung_u5_s_9_Type()
)
aktuelle_ausgangsspannung_u5_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u5_s_9.setStatus("current")
_Aktuelle_ausgangsspannung_u6_s_9_Type = DisplayString
_Aktuelle_ausgangsspannung_u6_s_9_Object = MibTableColumn
aktuelle_ausgangsspannung_u6_s_9 = _Aktuelle_ausgangsspannung_u6_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 25),
    _Aktuelle_ausgangsspannung_u6_s_9_Type()
)
aktuelle_ausgangsspannung_u6_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u6_s_9.setStatus("current")
_Aktuelle_ausgangsspannung_u7_s_9_Type = DisplayString
_Aktuelle_ausgangsspannung_u7_s_9_Object = MibTableColumn
aktuelle_ausgangsspannung_u7_s_9 = _Aktuelle_ausgangsspannung_u7_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 26),
    _Aktuelle_ausgangsspannung_u7_s_9_Type()
)
aktuelle_ausgangsspannung_u7_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u7_s_9.setStatus("current")
_Aktuelle_ausgangsspannung_u8_s_9_Type = DisplayString
_Aktuelle_ausgangsspannung_u8_s_9_Object = MibTableColumn
aktuelle_ausgangsspannung_u8_s_9 = _Aktuelle_ausgangsspannung_u8_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 27),
    _Aktuelle_ausgangsspannung_u8_s_9_Type()
)
aktuelle_ausgangsspannung_u8_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u8_s_9.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_1_s_9_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_1_s_9_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_1_s_9 = _Aktuelle_ladespannung_an_akku_kreis_1_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 28),
    _Aktuelle_ladespannung_an_akku_kreis_1_s_9_Type()
)
aktuelle_ladespannung_an_akku_kreis_1_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_1_s_9.setStatus("current")
_Aktuelle_ladespannung_an_akku_Kreis_2_s_9_Type = DisplayString
_Aktuelle_ladespannung_an_akku_Kreis_2_s_9_Object = MibTableColumn
aktuelle_ladespannung_an_akku_Kreis_2_s_9 = _Aktuelle_ladespannung_an_akku_Kreis_2_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 29),
    _Aktuelle_ladespannung_an_akku_Kreis_2_s_9_Type()
)
aktuelle_ladespannung_an_akku_Kreis_2_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_Kreis_2_s_9.setStatus("current")
_Aktuelle_ladespannung_an_akku_Kreis_3_s_9_Type = DisplayString
_Aktuelle_ladespannung_an_akku_Kreis_3_s_9_Object = MibTableColumn
aktuelle_ladespannung_an_akku_Kreis_3_s_9 = _Aktuelle_ladespannung_an_akku_Kreis_3_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 30),
    _Aktuelle_ladespannung_an_akku_Kreis_3_s_9_Type()
)
aktuelle_ladespannung_an_akku_Kreis_3_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_Kreis_3_s_9.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_4_s_9_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_4_s_9_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_4_s_9 = _Aktuelle_ladespannung_an_akku_kreis_4_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 31),
    _Aktuelle_ladespannung_an_akku_kreis_4_s_9_Type()
)
aktuelle_ladespannung_an_akku_kreis_4_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_4_s_9.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_5_s_9_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_5_s_9_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_5_s_9 = _Aktuelle_ladespannung_an_akku_kreis_5_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 32),
    _Aktuelle_ladespannung_an_akku_kreis_5_s_9_Type()
)
aktuelle_ladespannung_an_akku_kreis_5_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_5_s_9.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_6_s_9_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_6_s_9_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_6_s_9 = _Aktuelle_ladespannung_an_akku_kreis_6_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 33),
    _Aktuelle_ladespannung_an_akku_kreis_6_s_9_Type()
)
aktuelle_ladespannung_an_akku_kreis_6_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_6_s_9.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_7_s_9_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_7_s_9_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_7_s_9 = _Aktuelle_ladespannung_an_akku_kreis_7_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 34),
    _Aktuelle_ladespannung_an_akku_kreis_7_s_9_Type()
)
aktuelle_ladespannung_an_akku_kreis_7_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_7_s_9.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_8_s_9_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_8_s_9_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_8_s_9 = _Aktuelle_ladespannung_an_akku_kreis_8_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 35),
    _Aktuelle_ladespannung_an_akku_kreis_8_s_9_Type()
)
aktuelle_ladespannung_an_akku_kreis_8_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_8_s_9.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_1_s_9_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_1_s_9_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_1_s_9 = _Aktuelle_spannung_an_akku_kreis_1_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 36),
    _Aktuelle_spannung_an_akku_kreis_1_s_9_Type()
)
aktuelle_spannung_an_akku_kreis_1_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_1_s_9.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_2_s_9_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_2_s_9_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_2_s_9 = _Aktuelle_spannung_an_akku_kreis_2_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 37),
    _Aktuelle_spannung_an_akku_kreis_2_s_9_Type()
)
aktuelle_spannung_an_akku_kreis_2_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_2_s_9.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_3_s_9_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_3_s_9_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_3_s_9 = _Aktuelle_spannung_an_akku_kreis_3_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 38),
    _Aktuelle_spannung_an_akku_kreis_3_s_9_Type()
)
aktuelle_spannung_an_akku_kreis_3_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_3_s_9.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_4_s_9_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_4_s_9_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_4_s_9 = _Aktuelle_spannung_an_akku_kreis_4_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 39),
    _Aktuelle_spannung_an_akku_kreis_4_s_9_Type()
)
aktuelle_spannung_an_akku_kreis_4_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_4_s_9.setStatus("current")
_Aktuelle_spannung_an_akku_reis_5_s_9_Type = DisplayString
_Aktuelle_spannung_an_akku_reis_5_s_9_Object = MibTableColumn
aktuelle_spannung_an_akku_reis_5_s_9 = _Aktuelle_spannung_an_akku_reis_5_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 40),
    _Aktuelle_spannung_an_akku_reis_5_s_9_Type()
)
aktuelle_spannung_an_akku_reis_5_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_reis_5_s_9.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_6_s_9_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_6_s_9_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_6_s_9 = _Aktuelle_spannung_an_akku_kreis_6_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 41),
    _Aktuelle_spannung_an_akku_kreis_6_s_9_Type()
)
aktuelle_spannung_an_akku_kreis_6_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_6_s_9.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_7_s_9_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_7_s_9_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_7_s_9 = _Aktuelle_spannung_an_akku_kreis_7_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 42),
    _Aktuelle_spannung_an_akku_kreis_7_s_9_Type()
)
aktuelle_spannung_an_akku_kreis_7_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_7_s_9.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_8_s_9_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_8_s_9_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_8_s_9 = _Aktuelle_spannung_an_akku_kreis_8_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 43),
    _Aktuelle_spannung_an_akku_kreis_8_s_9_Type()
)
aktuelle_spannung_an_akku_kreis_8_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_8_s_9.setStatus("current")
_Testergebnis_lastspannung_an_akku_reis_1_s_9_Type = DisplayString
_Testergebnis_lastspannung_an_akku_reis_1_s_9_Object = MibTableColumn
testergebnis_lastspannung_an_akku_reis_1_s_9 = _Testergebnis_lastspannung_an_akku_reis_1_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 44),
    _Testergebnis_lastspannung_an_akku_reis_1_s_9_Type()
)
testergebnis_lastspannung_an_akku_reis_1_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_reis_1_s_9.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_2_s_9_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_2_s_9_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_2_s_9 = _Testergebnis_lastspannung_an_akku_kreis_2_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 45),
    _Testergebnis_lastspannung_an_akku_kreis_2_s_9_Type()
)
testergebnis_lastspannung_an_akku_kreis_2_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_2_s_9.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_3_s_9_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_3_s_9_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_3_s_9 = _Testergebnis_lastspannung_an_akku_kreis_3_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 46),
    _Testergebnis_lastspannung_an_akku_kreis_3_s_9_Type()
)
testergebnis_lastspannung_an_akku_kreis_3_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_3_s_9.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_4_s_9_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_4_s_9_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_4_s_9 = _Testergebnis_lastspannung_an_akku_kreis_4_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 47),
    _Testergebnis_lastspannung_an_akku_kreis_4_s_9_Type()
)
testergebnis_lastspannung_an_akku_kreis_4_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_4_s_9.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_5_s_9_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_5_s_9_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_5_s_9 = _Testergebnis_lastspannung_an_akku_kreis_5_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 48),
    _Testergebnis_lastspannung_an_akku_kreis_5_s_9_Type()
)
testergebnis_lastspannung_an_akku_kreis_5_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_5_s_9.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_6_s_9_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_6_s_9_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_6_s_9 = _Testergebnis_lastspannung_an_akku_kreis_6_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 49),
    _Testergebnis_lastspannung_an_akku_kreis_6_s_9_Type()
)
testergebnis_lastspannung_an_akku_kreis_6_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_6_s_9.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_7_s_9_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_7_s_9_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_7_s_9 = _Testergebnis_lastspannung_an_akku_kreis_7_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 50),
    _Testergebnis_lastspannung_an_akku_kreis_7_s_9_Type()
)
testergebnis_lastspannung_an_akku_kreis_7_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_7_s_9.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_8_s_9_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_8_s_9_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_8_s_9 = _Testergebnis_lastspannung_an_akku_kreis_8_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 51),
    _Testergebnis_lastspannung_an_akku_kreis_8_s_9_Type()
)
testergebnis_lastspannung_an_akku_kreis_8_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_8_s_9.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_1_s_9_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_1_s_9_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_1_s_9 = _Testergebnis_innenwiderstand_akku_kreis_1_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 52),
    _Testergebnis_innenwiderstand_akku_kreis_1_s_9_Type()
)
testergebnis_innenwiderstand_akku_kreis_1_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_1_s_9.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_2_s_9_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_2_s_9_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_2_s_9 = _Testergebnis_innenwiderstand_akku_kreis_2_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 53),
    _Testergebnis_innenwiderstand_akku_kreis_2_s_9_Type()
)
testergebnis_innenwiderstand_akku_kreis_2_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_2_s_9.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_3_s_9_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_3_s_9_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_3_s_9 = _Testergebnis_innenwiderstand_akku_kreis_3_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 54),
    _Testergebnis_innenwiderstand_akku_kreis_3_s_9_Type()
)
testergebnis_innenwiderstand_akku_kreis_3_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_3_s_9.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_4_s_9_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_4_s_9_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_4_s_9 = _Testergebnis_innenwiderstand_akku_kreis_4_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 56),
    _Testergebnis_innenwiderstand_akku_kreis_4_s_9_Type()
)
testergebnis_innenwiderstand_akku_kreis_4_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_4_s_9.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_5_s_9_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_5_s_9_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_5_s_9 = _Testergebnis_innenwiderstand_akku_kreis_5_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 57),
    _Testergebnis_innenwiderstand_akku_kreis_5_s_9_Type()
)
testergebnis_innenwiderstand_akku_kreis_5_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_5_s_9.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_6_s_9_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_6_s_9_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_6_s_9 = _Testergebnis_innenwiderstand_akku_kreis_6_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 58),
    _Testergebnis_innenwiderstand_akku_kreis_6_s_9_Type()
)
testergebnis_innenwiderstand_akku_kreis_6_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_6_s_9.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_7_s_9_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_7_s_9_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_7_s_9 = _Testergebnis_innenwiderstand_akku_kreis_7_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 59),
    _Testergebnis_innenwiderstand_akku_kreis_7_s_9_Type()
)
testergebnis_innenwiderstand_akku_kreis_7_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_7_s_9.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_8_s_9_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_8_s_9_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_8_s_9 = _Testergebnis_innenwiderstand_akku_kreis_8_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 60),
    _Testergebnis_innenwiderstand_akku_kreis_8_s_9_Type()
)
testergebnis_innenwiderstand_akku_kreis_8_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_8_s_9.setStatus("current")
_Netzteilspannung_uin1_s_9_Type = DisplayString
_Netzteilspannung_uin1_s_9_Object = MibTableColumn
netzteilspannung_uin1_s_9 = _Netzteilspannung_uin1_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 61),
    _Netzteilspannung_uin1_s_9_Type()
)
netzteilspannung_uin1_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzteilspannung_uin1_s_9.setStatus("current")
_Netzteilspannung_uin2_s_9_Type = DisplayString
_Netzteilspannung_uin2_s_9_Object = MibTableColumn
netzteilspannung_uin2_s_9 = _Netzteilspannung_uin2_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 62),
    _Netzteilspannung_uin2_s_9_Type()
)
netzteilspannung_uin2_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzteilspannung_uin2_s_9.setStatus("current")
_Programmierte_minimale_soll_sendeleistung_s_9_Type = DisplayString
_Programmierte_minimale_soll_sendeleistung_s_9_Object = MibTableColumn
programmierte_minimale_soll_sendeleistung_s_9 = _Programmierte_minimale_soll_sendeleistung_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 63),
    _Programmierte_minimale_soll_sendeleistung_s_9_Type()
)
programmierte_minimale_soll_sendeleistung_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programmierte_minimale_soll_sendeleistung_s_9.setStatus("current")
_Programmierte_maximale_antennen_reflexion_s_9_Type = DisplayString
_Programmierte_maximale_antennen_reflexion_s_9_Object = MibTableColumn
programmierte_maximale_antennen_reflexion_s_9 = _Programmierte_maximale_antennen_reflexion_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 64),
    _Programmierte_maximale_antennen_reflexion_s_9_Type()
)
programmierte_maximale_antennen_reflexion_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programmierte_maximale_antennen_reflexion_s_9.setStatus("current")
_Programmierte_minimale_anzahl_praesenzsignale_s_9_Type = DisplayString
_Programmierte_minimale_anzahl_praesenzsignale_s_9_Object = MibTableColumn
programmierte_minimale_anzahl_praesenzsignale_s_9 = _Programmierte_minimale_anzahl_praesenzsignale_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 65),
    _Programmierte_minimale_anzahl_praesenzsignale_s_9_Type()
)
programmierte_minimale_anzahl_praesenzsignale_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programmierte_minimale_anzahl_praesenzsignale_s_9.setStatus("current")
_Summen_fehlerstatus_von_tmoa_anlage_s_9_Type = DisplayString
_Summen_fehlerstatus_von_tmoa_anlage_s_9_Object = MibTableColumn
summen_fehlerstatus_von_tmoa_anlage_s_9 = _Summen_fehlerstatus_von_tmoa_anlage_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 66),
    _Summen_fehlerstatus_von_tmoa_anlage_s_9_Type()
)
summen_fehlerstatus_von_tmoa_anlage_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summen_fehlerstatus_von_tmoa_anlage_s_9.setStatus("current")
_Summen_fehlerstatus_von_anbinderepeater_s_9_Type = DisplayString
_Summen_fehlerstatus_von_anbinderepeater_s_9_Object = MibTableColumn
summen_fehlerstatus_von_anbinderepeater_s_9 = _Summen_fehlerstatus_von_anbinderepeater_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 67),
    _Summen_fehlerstatus_von_anbinderepeater_s_9_Type()
)
summen_fehlerstatus_von_anbinderepeater_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summen_fehlerstatus_von_anbinderepeater_s_9.setStatus("current")
_Summen_fehlerstatus_von_analogem_repeater_s_9_Type = DisplayString
_Summen_fehlerstatus_von_analogem_repeater_s_9_Object = MibTableColumn
summen_fehlerstatus_von_analogem_repeater_s_9 = _Summen_fehlerstatus_von_analogem_repeater_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 68),
    _Summen_fehlerstatus_von_analogem_repeater_s_9_Type()
)
summen_fehlerstatus_von_analogem_repeater_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summen_fehlerstatus_von_analogem_repeater_s_9.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_9_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_9_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_9 = _Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 69),
    _Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_9_Type()
)
aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_9.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_9_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_9_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_9 = _Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 70),
    _Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_9_Type()
)
aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_9.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_9_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_9_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_9 = _Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 71),
    _Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_9_Type()
)
aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_9.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_9_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_9_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_9 = _Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 72),
    _Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_9_Type()
)
aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_9.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_9_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_9_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_9 = _Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 73),
    _Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_9_Type()
)
aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_9.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_9_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_9_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_9 = _Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 74),
    _Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_9_Type()
)
aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_9.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_9_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_9_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_9 = _Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 75),
    _Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_9_Type()
)
aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_9.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_9_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_9_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_9 = _Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 76),
    _Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_9_Type()
)
aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_9.setStatus("current")
_Netzspannungsversorgung_von_tmoa_anlage_s_9_Type = DisplayString
_Netzspannungsversorgung_von_tmoa_anlage_s_9_Object = MibTableColumn
netzspannungsversorgung_von_tmoa_anlage_s_9 = _Netzspannungsversorgung_von_tmoa_anlage_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 77),
    _Netzspannungsversorgung_von_tmoa_anlage_s_9_Type()
)
netzspannungsversorgung_von_tmoa_anlage_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzspannungsversorgung_von_tmoa_anlage_s_9.setStatus("current")
_Netzspannungsversorgung_von_anbinderepeater_s_9_Type = DisplayString
_Netzspannungsversorgung_von_anbinderepeater_s_9_Object = MibTableColumn
netzspannungsversorgung_von_anbinderepeater_s_9 = _Netzspannungsversorgung_von_anbinderepeater_s_9_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 1, 1, 78),
    _Netzspannungsversorgung_von_anbinderepeater_s_9_Type()
)
netzspannungsversorgung_von_anbinderepeater_s_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzspannungsversorgung_von_anbinderepeater_s_9.setStatus("current")
_Ak_slave_10_i_ObjectIdentity = ObjectIdentity
ak_slave_10_i = _Ak_slave_10_i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10)
)
_ModulTable_s_10_Object = MibTable
modulTable_s_10 = _ModulTable_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1)
)
if mibBuilder.loadTexts:
    modulTable_s_10.setStatus("current")
_ModulEntry_s_10_Object = MibTableRow
modulEntry_s_10 = _ModulEntry_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1)
)
modulEntry_s_10.setIndexNames(
    (0, "AK-FUNKTECHNIK-MIB", "modulIndex-s-10"),
)
if mibBuilder.loadTexts:
    modulEntry_s_10.setStatus("current")
_ModulIndex_s_10_Type = DisplayString
_ModulIndex_s_10_Object = MibTableColumn
modulIndex_s_10 = _ModulIndex_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 1),
    _ModulIndex_s_10_Type()
)
modulIndex_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulIndex_s_10.setStatus("current")
_Geraete_typ_s_10_Type = DisplayString
_Geraete_typ_s_10_Object = MibTableColumn
geraete_typ_s_10 = _Geraete_typ_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 2),
    _Geraete_typ_s_10_Type()
)
geraete_typ_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geraete_typ_s_10.setStatus("current")
_Betriebsstatus_s_10_Type = DisplayString
_Betriebsstatus_s_10_Object = MibTableColumn
betriebsstatus_s_10 = _Betriebsstatus_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 3),
    _Betriebsstatus_s_10_Type()
)
betriebsstatus_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    betriebsstatus_s_10.setStatus("current")
_Senderstatus_s_10_Type = DisplayString
_Senderstatus_s_10_Object = MibTableColumn
senderstatus_s_10 = _Senderstatus_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 4),
    _Senderstatus_s_10_Type()
)
senderstatus_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    senderstatus_s_10.setStatus("current")
_Fehlerstatus_s_10_Type = DisplayString
_Fehlerstatus_s_10_Object = MibTableColumn
fehlerstatus_s_10 = _Fehlerstatus_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 5),
    _Fehlerstatus_s_10_Type()
)
fehlerstatus_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fehlerstatus_s_10.setStatus("current")
_Dem_adapter_zugeordnete_funkgeraetetype_s_10_Type = DisplayString
_Dem_adapter_zugeordnete_funkgeraetetype_s_10_Object = MibTableColumn
dem_adapter_zugeordnete_funkgeraetetype_s_10 = _Dem_adapter_zugeordnete_funkgeraetetype_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 6),
    _Dem_adapter_zugeordnete_funkgeraetetype_s_10_Type()
)
dem_adapter_zugeordnete_funkgeraetetype_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dem_adapter_zugeordnete_funkgeraetetype_s_10.setStatus("current")
_Eingabe_und_anzeigemodul_s_10_Type = DisplayString
_Eingabe_und_anzeigemodul_s_10_Object = MibTableColumn
eingabe_und_anzeigemodul_s_10 = _Eingabe_und_anzeigemodul_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 7),
    _Eingabe_und_anzeigemodul_s_10_Type()
)
eingabe_und_anzeigemodul_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eingabe_und_anzeigemodul_s_10.setStatus("current")
_Mod_bus_verbindung_module_s_10_Type = DisplayString
_Mod_bus_verbindung_module_s_10_Object = MibTableColumn
mod_bus_verbindung_module_s_10 = _Mod_bus_verbindung_module_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 8),
    _Mod_bus_verbindung_module_s_10_Type()
)
mod_bus_verbindung_module_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mod_bus_verbindung_module_s_10.setStatus("current")
_Gemessene_sendeleistung_im_testmode_s_10_Type = DisplayString
_Gemessene_sendeleistung_im_testmode_s_10_Object = MibTableColumn
gemessene_sendeleistung_im_testmode_s_10 = _Gemessene_sendeleistung_im_testmode_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 9),
    _Gemessene_sendeleistung_im_testmode_s_10_Type()
)
gemessene_sendeleistung_im_testmode_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemessene_sendeleistung_im_testmode_s_10.setStatus("current")
_Aktuelle_sendeleistung_s_10_Type = DisplayString
_Aktuelle_sendeleistung_s_10_Object = MibTableColumn
aktuelle_sendeleistung_s_10 = _Aktuelle_sendeleistung_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 10),
    _Aktuelle_sendeleistung_s_10_Type()
)
aktuelle_sendeleistung_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_sendeleistung_s_10.setStatus("current")
_Gemessene_reflexion_im_testmode_s_10_Type = DisplayString
_Gemessene_reflexion_im_testmode_s_10_Object = MibTableColumn
gemessene_reflexion_im_testmode_s_10 = _Gemessene_reflexion_im_testmode_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 11),
    _Gemessene_reflexion_im_testmode_s_10_Type()
)
gemessene_reflexion_im_testmode_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemessene_reflexion_im_testmode_s_10.setStatus("current")
_Aktuelle_reflexion_s_10_Type = DisplayString
_Aktuelle_reflexion_s_10_Object = MibTableColumn
aktuelle_reflexion_s_10 = _Aktuelle_reflexion_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 12),
    _Aktuelle_reflexion_s_10_Type()
)
aktuelle_reflexion_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_reflexion_s_10.setStatus("current")
_Letzte_gemessene_donor_sendeleistung_s_10_Type = DisplayString
_Letzte_gemessene_donor_sendeleistung_s_10_Object = MibTableColumn
letzte_gemessene_donor_sendeleistung_s_10 = _Letzte_gemessene_donor_sendeleistung_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 13),
    _Letzte_gemessene_donor_sendeleistung_s_10_Type()
)
letzte_gemessene_donor_sendeleistung_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    letzte_gemessene_donor_sendeleistung_s_10.setStatus("current")
_Aktuelle_donor_sendeleistung_s_10_Type = DisplayString
_Aktuelle_donor_sendeleistung_s_10_Object = MibTableColumn
aktuelle_donor_sendeleistung_s_10 = _Aktuelle_donor_sendeleistung_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 14),
    _Aktuelle_donor_sendeleistung_s_10_Type()
)
aktuelle_donor_sendeleistung_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_donor_sendeleistung_s_10.setStatus("current")
_Letzte_gemessene_donor_reflexion_s_10_Type = DisplayString
_Letzte_gemessene_donor_reflexion_s_10_Object = MibTableColumn
letzte_gemessene_donor_reflexion_s_10 = _Letzte_gemessene_donor_reflexion_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 15),
    _Letzte_gemessene_donor_reflexion_s_10_Type()
)
letzte_gemessene_donor_reflexion_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    letzte_gemessene_donor_reflexion_s_10.setStatus("current")
_Aktuelle_donor_reflexion_s_10_Type = DisplayString
_Aktuelle_donor_reflexion_s_10_Object = MibTableColumn
aktuelle_donor_reflexion_s_10 = _Aktuelle_donor_reflexion_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 16),
    _Aktuelle_donor_reflexion_s_10_Type()
)
aktuelle_donor_reflexion_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_donor_reflexion_s_10.setStatus("current")
_Anzahl_gemessener_praesenzsignale_im_testmode_s_10_Type = DisplayString
_Anzahl_gemessener_praesenzsignale_im_testmode_s_10_Object = MibTableColumn
anzahl_gemessener_praesenzsignale_im_testmode_s_10 = _Anzahl_gemessener_praesenzsignale_im_testmode_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 18),
    _Anzahl_gemessener_praesenzsignale_im_testmode_s_10_Type()
)
anzahl_gemessener_praesenzsignale_im_testmode_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anzahl_gemessener_praesenzsignale_im_testmode_s_10.setStatus("current")
_Aktuelle_ausgangsspannung_ub_s_10_Type = DisplayString
_Aktuelle_ausgangsspannung_ub_s_10_Object = MibTableColumn
aktuelle_ausgangsspannung_ub_s_10 = _Aktuelle_ausgangsspannung_ub_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 19),
    _Aktuelle_ausgangsspannung_ub_s_10_Type()
)
aktuelle_ausgangsspannung_ub_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_ub_s_10.setStatus("current")
_Aktuelle_ausgangsspannung_u1_s_10_Type = DisplayString
_Aktuelle_ausgangsspannung_u1_s_10_Object = MibTableColumn
aktuelle_ausgangsspannung_u1_s_10 = _Aktuelle_ausgangsspannung_u1_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 20),
    _Aktuelle_ausgangsspannung_u1_s_10_Type()
)
aktuelle_ausgangsspannung_u1_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u1_s_10.setStatus("current")
_Aktuelle_ausgangsspannung_u2_s_10_Type = DisplayString
_Aktuelle_ausgangsspannung_u2_s_10_Object = MibTableColumn
aktuelle_ausgangsspannung_u2_s_10 = _Aktuelle_ausgangsspannung_u2_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 21),
    _Aktuelle_ausgangsspannung_u2_s_10_Type()
)
aktuelle_ausgangsspannung_u2_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u2_s_10.setStatus("current")
_Aktuelle_ausgangsspannung_u3_s_10_Type = DisplayString
_Aktuelle_ausgangsspannung_u3_s_10_Object = MibTableColumn
aktuelle_ausgangsspannung_u3_s_10 = _Aktuelle_ausgangsspannung_u3_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 22),
    _Aktuelle_ausgangsspannung_u3_s_10_Type()
)
aktuelle_ausgangsspannung_u3_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u3_s_10.setStatus("current")
_Aktuelle_ausgangsspannung_u4_s_10_Type = DisplayString
_Aktuelle_ausgangsspannung_u4_s_10_Object = MibTableColumn
aktuelle_ausgangsspannung_u4_s_10 = _Aktuelle_ausgangsspannung_u4_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 23),
    _Aktuelle_ausgangsspannung_u4_s_10_Type()
)
aktuelle_ausgangsspannung_u4_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u4_s_10.setStatus("current")
_Aktuelle_ausgangsspannung_u5_s_10_Type = DisplayString
_Aktuelle_ausgangsspannung_u5_s_10_Object = MibTableColumn
aktuelle_ausgangsspannung_u5_s_10 = _Aktuelle_ausgangsspannung_u5_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 24),
    _Aktuelle_ausgangsspannung_u5_s_10_Type()
)
aktuelle_ausgangsspannung_u5_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u5_s_10.setStatus("current")
_Aktuelle_ausgangsspannung_u6_s_10_Type = DisplayString
_Aktuelle_ausgangsspannung_u6_s_10_Object = MibTableColumn
aktuelle_ausgangsspannung_u6_s_10 = _Aktuelle_ausgangsspannung_u6_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 25),
    _Aktuelle_ausgangsspannung_u6_s_10_Type()
)
aktuelle_ausgangsspannung_u6_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u6_s_10.setStatus("current")
_Aktuelle_ausgangsspannung_u7_s_10_Type = DisplayString
_Aktuelle_ausgangsspannung_u7_s_10_Object = MibTableColumn
aktuelle_ausgangsspannung_u7_s_10 = _Aktuelle_ausgangsspannung_u7_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 26),
    _Aktuelle_ausgangsspannung_u7_s_10_Type()
)
aktuelle_ausgangsspannung_u7_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u7_s_10.setStatus("current")
_Aktuelle_ausgangsspannung_u8_s_10_Type = DisplayString
_Aktuelle_ausgangsspannung_u8_s_10_Object = MibTableColumn
aktuelle_ausgangsspannung_u8_s_10 = _Aktuelle_ausgangsspannung_u8_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 27),
    _Aktuelle_ausgangsspannung_u8_s_10_Type()
)
aktuelle_ausgangsspannung_u8_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u8_s_10.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_1_s_10_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_1_s_10_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_1_s_10 = _Aktuelle_ladespannung_an_akku_kreis_1_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 28),
    _Aktuelle_ladespannung_an_akku_kreis_1_s_10_Type()
)
aktuelle_ladespannung_an_akku_kreis_1_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_1_s_10.setStatus("current")
_Aktuelle_ladespannung_an_akku_Kreis_2_s_10_Type = DisplayString
_Aktuelle_ladespannung_an_akku_Kreis_2_s_10_Object = MibTableColumn
aktuelle_ladespannung_an_akku_Kreis_2_s_10 = _Aktuelle_ladespannung_an_akku_Kreis_2_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 29),
    _Aktuelle_ladespannung_an_akku_Kreis_2_s_10_Type()
)
aktuelle_ladespannung_an_akku_Kreis_2_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_Kreis_2_s_10.setStatus("current")
_Aktuelle_ladespannung_an_akku_Kreis_3_s_10_Type = DisplayString
_Aktuelle_ladespannung_an_akku_Kreis_3_s_10_Object = MibTableColumn
aktuelle_ladespannung_an_akku_Kreis_3_s_10 = _Aktuelle_ladespannung_an_akku_Kreis_3_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 30),
    _Aktuelle_ladespannung_an_akku_Kreis_3_s_10_Type()
)
aktuelle_ladespannung_an_akku_Kreis_3_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_Kreis_3_s_10.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_4_s_10_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_4_s_10_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_4_s_10 = _Aktuelle_ladespannung_an_akku_kreis_4_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 31),
    _Aktuelle_ladespannung_an_akku_kreis_4_s_10_Type()
)
aktuelle_ladespannung_an_akku_kreis_4_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_4_s_10.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_5_s_10_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_5_s_10_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_5_s_10 = _Aktuelle_ladespannung_an_akku_kreis_5_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 32),
    _Aktuelle_ladespannung_an_akku_kreis_5_s_10_Type()
)
aktuelle_ladespannung_an_akku_kreis_5_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_5_s_10.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_6_s_10_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_6_s_10_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_6_s_10 = _Aktuelle_ladespannung_an_akku_kreis_6_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 33),
    _Aktuelle_ladespannung_an_akku_kreis_6_s_10_Type()
)
aktuelle_ladespannung_an_akku_kreis_6_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_6_s_10.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_7_s_10_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_7_s_10_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_7_s_10 = _Aktuelle_ladespannung_an_akku_kreis_7_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 34),
    _Aktuelle_ladespannung_an_akku_kreis_7_s_10_Type()
)
aktuelle_ladespannung_an_akku_kreis_7_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_7_s_10.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_8_s_10_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_8_s_10_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_8_s_10 = _Aktuelle_ladespannung_an_akku_kreis_8_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 35),
    _Aktuelle_ladespannung_an_akku_kreis_8_s_10_Type()
)
aktuelle_ladespannung_an_akku_kreis_8_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_8_s_10.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_1_s_10_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_1_s_10_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_1_s_10 = _Aktuelle_spannung_an_akku_kreis_1_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 36),
    _Aktuelle_spannung_an_akku_kreis_1_s_10_Type()
)
aktuelle_spannung_an_akku_kreis_1_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_1_s_10.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_2_s_10_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_2_s_10_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_2_s_10 = _Aktuelle_spannung_an_akku_kreis_2_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 37),
    _Aktuelle_spannung_an_akku_kreis_2_s_10_Type()
)
aktuelle_spannung_an_akku_kreis_2_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_2_s_10.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_3_s_10_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_3_s_10_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_3_s_10 = _Aktuelle_spannung_an_akku_kreis_3_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 38),
    _Aktuelle_spannung_an_akku_kreis_3_s_10_Type()
)
aktuelle_spannung_an_akku_kreis_3_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_3_s_10.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_4_s_10_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_4_s_10_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_4_s_10 = _Aktuelle_spannung_an_akku_kreis_4_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 39),
    _Aktuelle_spannung_an_akku_kreis_4_s_10_Type()
)
aktuelle_spannung_an_akku_kreis_4_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_4_s_10.setStatus("current")
_Aktuelle_spannung_an_akku_reis_5_s_10_Type = DisplayString
_Aktuelle_spannung_an_akku_reis_5_s_10_Object = MibTableColumn
aktuelle_spannung_an_akku_reis_5_s_10 = _Aktuelle_spannung_an_akku_reis_5_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 40),
    _Aktuelle_spannung_an_akku_reis_5_s_10_Type()
)
aktuelle_spannung_an_akku_reis_5_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_reis_5_s_10.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_6_s_10_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_6_s_10_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_6_s_10 = _Aktuelle_spannung_an_akku_kreis_6_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 41),
    _Aktuelle_spannung_an_akku_kreis_6_s_10_Type()
)
aktuelle_spannung_an_akku_kreis_6_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_6_s_10.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_7_s_10_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_7_s_10_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_7_s_10 = _Aktuelle_spannung_an_akku_kreis_7_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 42),
    _Aktuelle_spannung_an_akku_kreis_7_s_10_Type()
)
aktuelle_spannung_an_akku_kreis_7_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_7_s_10.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_8_s_10_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_8_s_10_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_8_s_10 = _Aktuelle_spannung_an_akku_kreis_8_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 43),
    _Aktuelle_spannung_an_akku_kreis_8_s_10_Type()
)
aktuelle_spannung_an_akku_kreis_8_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_8_s_10.setStatus("current")
_Testergebnis_lastspannung_an_akku_reis_1_s_10_Type = DisplayString
_Testergebnis_lastspannung_an_akku_reis_1_s_10_Object = MibTableColumn
testergebnis_lastspannung_an_akku_reis_1_s_10 = _Testergebnis_lastspannung_an_akku_reis_1_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 44),
    _Testergebnis_lastspannung_an_akku_reis_1_s_10_Type()
)
testergebnis_lastspannung_an_akku_reis_1_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_reis_1_s_10.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_2_s_10_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_2_s_10_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_2_s_10 = _Testergebnis_lastspannung_an_akku_kreis_2_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 45),
    _Testergebnis_lastspannung_an_akku_kreis_2_s_10_Type()
)
testergebnis_lastspannung_an_akku_kreis_2_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_2_s_10.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_3_s_10_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_3_s_10_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_3_s_10 = _Testergebnis_lastspannung_an_akku_kreis_3_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 46),
    _Testergebnis_lastspannung_an_akku_kreis_3_s_10_Type()
)
testergebnis_lastspannung_an_akku_kreis_3_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_3_s_10.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_4_s_10_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_4_s_10_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_4_s_10 = _Testergebnis_lastspannung_an_akku_kreis_4_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 47),
    _Testergebnis_lastspannung_an_akku_kreis_4_s_10_Type()
)
testergebnis_lastspannung_an_akku_kreis_4_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_4_s_10.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_5_s_10_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_5_s_10_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_5_s_10 = _Testergebnis_lastspannung_an_akku_kreis_5_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 48),
    _Testergebnis_lastspannung_an_akku_kreis_5_s_10_Type()
)
testergebnis_lastspannung_an_akku_kreis_5_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_5_s_10.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_6_s_10_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_6_s_10_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_6_s_10 = _Testergebnis_lastspannung_an_akku_kreis_6_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 49),
    _Testergebnis_lastspannung_an_akku_kreis_6_s_10_Type()
)
testergebnis_lastspannung_an_akku_kreis_6_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_6_s_10.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_7_s_10_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_7_s_10_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_7_s_10 = _Testergebnis_lastspannung_an_akku_kreis_7_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 50),
    _Testergebnis_lastspannung_an_akku_kreis_7_s_10_Type()
)
testergebnis_lastspannung_an_akku_kreis_7_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_7_s_10.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_8_s_10_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_8_s_10_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_8_s_10 = _Testergebnis_lastspannung_an_akku_kreis_8_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 51),
    _Testergebnis_lastspannung_an_akku_kreis_8_s_10_Type()
)
testergebnis_lastspannung_an_akku_kreis_8_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_8_s_10.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_1_s_10_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_1_s_10_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_1_s_10 = _Testergebnis_innenwiderstand_akku_kreis_1_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 52),
    _Testergebnis_innenwiderstand_akku_kreis_1_s_10_Type()
)
testergebnis_innenwiderstand_akku_kreis_1_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_1_s_10.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_2_s_10_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_2_s_10_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_2_s_10 = _Testergebnis_innenwiderstand_akku_kreis_2_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 53),
    _Testergebnis_innenwiderstand_akku_kreis_2_s_10_Type()
)
testergebnis_innenwiderstand_akku_kreis_2_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_2_s_10.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_3_s_10_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_3_s_10_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_3_s_10 = _Testergebnis_innenwiderstand_akku_kreis_3_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 54),
    _Testergebnis_innenwiderstand_akku_kreis_3_s_10_Type()
)
testergebnis_innenwiderstand_akku_kreis_3_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_3_s_10.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_4_s_10_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_4_s_10_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_4_s_10 = _Testergebnis_innenwiderstand_akku_kreis_4_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 56),
    _Testergebnis_innenwiderstand_akku_kreis_4_s_10_Type()
)
testergebnis_innenwiderstand_akku_kreis_4_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_4_s_10.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_5_s_10_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_5_s_10_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_5_s_10 = _Testergebnis_innenwiderstand_akku_kreis_5_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 57),
    _Testergebnis_innenwiderstand_akku_kreis_5_s_10_Type()
)
testergebnis_innenwiderstand_akku_kreis_5_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_5_s_10.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_6_s_10_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_6_s_10_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_6_s_10 = _Testergebnis_innenwiderstand_akku_kreis_6_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 58),
    _Testergebnis_innenwiderstand_akku_kreis_6_s_10_Type()
)
testergebnis_innenwiderstand_akku_kreis_6_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_6_s_10.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_7_s_10_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_7_s_10_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_7_s_10 = _Testergebnis_innenwiderstand_akku_kreis_7_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 59),
    _Testergebnis_innenwiderstand_akku_kreis_7_s_10_Type()
)
testergebnis_innenwiderstand_akku_kreis_7_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_7_s_10.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_8_s_10_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_8_s_10_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_8_s_10 = _Testergebnis_innenwiderstand_akku_kreis_8_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 60),
    _Testergebnis_innenwiderstand_akku_kreis_8_s_10_Type()
)
testergebnis_innenwiderstand_akku_kreis_8_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_8_s_10.setStatus("current")
_Netzteilspannung_uin1_s_10_Type = DisplayString
_Netzteilspannung_uin1_s_10_Object = MibTableColumn
netzteilspannung_uin1_s_10 = _Netzteilspannung_uin1_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 61),
    _Netzteilspannung_uin1_s_10_Type()
)
netzteilspannung_uin1_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzteilspannung_uin1_s_10.setStatus("current")
_Netzteilspannung_uin2_s_10_Type = DisplayString
_Netzteilspannung_uin2_s_10_Object = MibTableColumn
netzteilspannung_uin2_s_10 = _Netzteilspannung_uin2_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 62),
    _Netzteilspannung_uin2_s_10_Type()
)
netzteilspannung_uin2_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzteilspannung_uin2_s_10.setStatus("current")
_Programmierte_minimale_soll_sendeleistung_s_10_Type = DisplayString
_Programmierte_minimale_soll_sendeleistung_s_10_Object = MibTableColumn
programmierte_minimale_soll_sendeleistung_s_10 = _Programmierte_minimale_soll_sendeleistung_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 63),
    _Programmierte_minimale_soll_sendeleistung_s_10_Type()
)
programmierte_minimale_soll_sendeleistung_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programmierte_minimale_soll_sendeleistung_s_10.setStatus("current")
_Programmierte_maximale_antennen_reflexion_s_10_Type = DisplayString
_Programmierte_maximale_antennen_reflexion_s_10_Object = MibTableColumn
programmierte_maximale_antennen_reflexion_s_10 = _Programmierte_maximale_antennen_reflexion_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 64),
    _Programmierte_maximale_antennen_reflexion_s_10_Type()
)
programmierte_maximale_antennen_reflexion_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programmierte_maximale_antennen_reflexion_s_10.setStatus("current")
_Programmierte_minimale_anzahl_praesenzsignale_s_10_Type = DisplayString
_Programmierte_minimale_anzahl_praesenzsignale_s_10_Object = MibTableColumn
programmierte_minimale_anzahl_praesenzsignale_s_10 = _Programmierte_minimale_anzahl_praesenzsignale_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 65),
    _Programmierte_minimale_anzahl_praesenzsignale_s_10_Type()
)
programmierte_minimale_anzahl_praesenzsignale_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programmierte_minimale_anzahl_praesenzsignale_s_10.setStatus("current")
_Summen_fehlerstatus_von_tmoa_anlage_s_10_Type = DisplayString
_Summen_fehlerstatus_von_tmoa_anlage_s_10_Object = MibTableColumn
summen_fehlerstatus_von_tmoa_anlage_s_10 = _Summen_fehlerstatus_von_tmoa_anlage_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 66),
    _Summen_fehlerstatus_von_tmoa_anlage_s_10_Type()
)
summen_fehlerstatus_von_tmoa_anlage_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summen_fehlerstatus_von_tmoa_anlage_s_10.setStatus("current")
_Summen_fehlerstatus_von_anbinderepeater_s_10_Type = DisplayString
_Summen_fehlerstatus_von_anbinderepeater_s_10_Object = MibTableColumn
summen_fehlerstatus_von_anbinderepeater_s_10 = _Summen_fehlerstatus_von_anbinderepeater_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 67),
    _Summen_fehlerstatus_von_anbinderepeater_s_10_Type()
)
summen_fehlerstatus_von_anbinderepeater_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summen_fehlerstatus_von_anbinderepeater_s_10.setStatus("current")
_Summen_fehlerstatus_von_analogem_repeater_s_10_Type = DisplayString
_Summen_fehlerstatus_von_analogem_repeater_s_10_Object = MibTableColumn
summen_fehlerstatus_von_analogem_repeater_s_10 = _Summen_fehlerstatus_von_analogem_repeater_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 68),
    _Summen_fehlerstatus_von_analogem_repeater_s_10_Type()
)
summen_fehlerstatus_von_analogem_repeater_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summen_fehlerstatus_von_analogem_repeater_s_10.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_10_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_10_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_10 = _Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 69),
    _Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_10_Type()
)
aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_10.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_10_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_10_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_10 = _Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 70),
    _Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_10_Type()
)
aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_10.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_10_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_10_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_10 = _Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 71),
    _Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_10_Type()
)
aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_10.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_10_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_10_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_10 = _Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 72),
    _Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_10_Type()
)
aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_10.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_10_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_10_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_10 = _Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 73),
    _Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_10_Type()
)
aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_10.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_10_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_10_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_10 = _Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 74),
    _Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_10_Type()
)
aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_10.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_10_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_10_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_10 = _Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 75),
    _Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_10_Type()
)
aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_10.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_10_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_10_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_10 = _Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 76),
    _Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_10_Type()
)
aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_10.setStatus("current")
_Netzspannungsversorgung_von_tmoa_anlage_s_10_Type = DisplayString
_Netzspannungsversorgung_von_tmoa_anlage_s_10_Object = MibTableColumn
netzspannungsversorgung_von_tmoa_anlage_s_10 = _Netzspannungsversorgung_von_tmoa_anlage_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 77),
    _Netzspannungsversorgung_von_tmoa_anlage_s_10_Type()
)
netzspannungsversorgung_von_tmoa_anlage_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzspannungsversorgung_von_tmoa_anlage_s_10.setStatus("current")
_Netzspannungsversorgung_von_anbinderepeater_s_10_Type = DisplayString
_Netzspannungsversorgung_von_anbinderepeater_s_10_Object = MibTableColumn
netzspannungsversorgung_von_anbinderepeater_s_10 = _Netzspannungsversorgung_von_anbinderepeater_s_10_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 1, 1, 78),
    _Netzspannungsversorgung_von_anbinderepeater_s_10_Type()
)
netzspannungsversorgung_von_anbinderepeater_s_10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzspannungsversorgung_von_anbinderepeater_s_10.setStatus("current")
_Ak_slave_11_i_ObjectIdentity = ObjectIdentity
ak_slave_11_i = _Ak_slave_11_i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11)
)
_ModulTable_s_11_Object = MibTable
modulTable_s_11 = _ModulTable_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1)
)
if mibBuilder.loadTexts:
    modulTable_s_11.setStatus("current")
_ModulEntry_s_11_Object = MibTableRow
modulEntry_s_11 = _ModulEntry_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1)
)
modulEntry_s_11.setIndexNames(
    (0, "AK-FUNKTECHNIK-MIB", "modulIndex-s-11"),
)
if mibBuilder.loadTexts:
    modulEntry_s_11.setStatus("current")
_ModulIndex_s_11_Type = DisplayString
_ModulIndex_s_11_Object = MibTableColumn
modulIndex_s_11 = _ModulIndex_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 1),
    _ModulIndex_s_11_Type()
)
modulIndex_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulIndex_s_11.setStatus("current")
_Geraete_typ_s_11_Type = DisplayString
_Geraete_typ_s_11_Object = MibTableColumn
geraete_typ_s_11 = _Geraete_typ_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 2),
    _Geraete_typ_s_11_Type()
)
geraete_typ_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geraete_typ_s_11.setStatus("current")
_Betriebsstatus_s_11_Type = DisplayString
_Betriebsstatus_s_11_Object = MibTableColumn
betriebsstatus_s_11 = _Betriebsstatus_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 3),
    _Betriebsstatus_s_11_Type()
)
betriebsstatus_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    betriebsstatus_s_11.setStatus("current")
_Senderstatus_s_11_Type = DisplayString
_Senderstatus_s_11_Object = MibTableColumn
senderstatus_s_11 = _Senderstatus_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 4),
    _Senderstatus_s_11_Type()
)
senderstatus_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    senderstatus_s_11.setStatus("current")
_Fehlerstatus_s_11_Type = DisplayString
_Fehlerstatus_s_11_Object = MibTableColumn
fehlerstatus_s_11 = _Fehlerstatus_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 5),
    _Fehlerstatus_s_11_Type()
)
fehlerstatus_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fehlerstatus_s_11.setStatus("current")
_Dem_adapter_zugeordnete_funkgeraetetype_s_11_Type = DisplayString
_Dem_adapter_zugeordnete_funkgeraetetype_s_11_Object = MibTableColumn
dem_adapter_zugeordnete_funkgeraetetype_s_11 = _Dem_adapter_zugeordnete_funkgeraetetype_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 6),
    _Dem_adapter_zugeordnete_funkgeraetetype_s_11_Type()
)
dem_adapter_zugeordnete_funkgeraetetype_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dem_adapter_zugeordnete_funkgeraetetype_s_11.setStatus("current")
_Eingabe_und_anzeigemodul_s_11_Type = DisplayString
_Eingabe_und_anzeigemodul_s_11_Object = MibTableColumn
eingabe_und_anzeigemodul_s_11 = _Eingabe_und_anzeigemodul_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 7),
    _Eingabe_und_anzeigemodul_s_11_Type()
)
eingabe_und_anzeigemodul_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eingabe_und_anzeigemodul_s_11.setStatus("current")
_Mod_bus_verbindung_module_s_11_Type = DisplayString
_Mod_bus_verbindung_module_s_11_Object = MibTableColumn
mod_bus_verbindung_module_s_11 = _Mod_bus_verbindung_module_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 8),
    _Mod_bus_verbindung_module_s_11_Type()
)
mod_bus_verbindung_module_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mod_bus_verbindung_module_s_11.setStatus("current")
_Gemessene_sendeleistung_im_testmode_s_11_Type = DisplayString
_Gemessene_sendeleistung_im_testmode_s_11_Object = MibTableColumn
gemessene_sendeleistung_im_testmode_s_11 = _Gemessene_sendeleistung_im_testmode_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 9),
    _Gemessene_sendeleistung_im_testmode_s_11_Type()
)
gemessene_sendeleistung_im_testmode_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemessene_sendeleistung_im_testmode_s_11.setStatus("current")
_Aktuelle_sendeleistung_s_11_Type = DisplayString
_Aktuelle_sendeleistung_s_11_Object = MibTableColumn
aktuelle_sendeleistung_s_11 = _Aktuelle_sendeleistung_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 10),
    _Aktuelle_sendeleistung_s_11_Type()
)
aktuelle_sendeleistung_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_sendeleistung_s_11.setStatus("current")
_Gemessene_reflexion_im_testmode_s_11_Type = DisplayString
_Gemessene_reflexion_im_testmode_s_11_Object = MibTableColumn
gemessene_reflexion_im_testmode_s_11 = _Gemessene_reflexion_im_testmode_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 11),
    _Gemessene_reflexion_im_testmode_s_11_Type()
)
gemessene_reflexion_im_testmode_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemessene_reflexion_im_testmode_s_11.setStatus("current")
_Aktuelle_reflexion_s_11_Type = DisplayString
_Aktuelle_reflexion_s_11_Object = MibTableColumn
aktuelle_reflexion_s_11 = _Aktuelle_reflexion_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 12),
    _Aktuelle_reflexion_s_11_Type()
)
aktuelle_reflexion_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_reflexion_s_11.setStatus("current")
_Letzte_gemessene_donor_sendeleistung_s_11_Type = DisplayString
_Letzte_gemessene_donor_sendeleistung_s_11_Object = MibTableColumn
letzte_gemessene_donor_sendeleistung_s_11 = _Letzte_gemessene_donor_sendeleistung_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 13),
    _Letzte_gemessene_donor_sendeleistung_s_11_Type()
)
letzte_gemessene_donor_sendeleistung_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    letzte_gemessene_donor_sendeleistung_s_11.setStatus("current")
_Aktuelle_donor_sendeleistung_s_11_Type = DisplayString
_Aktuelle_donor_sendeleistung_s_11_Object = MibTableColumn
aktuelle_donor_sendeleistung_s_11 = _Aktuelle_donor_sendeleistung_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 14),
    _Aktuelle_donor_sendeleistung_s_11_Type()
)
aktuelle_donor_sendeleistung_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_donor_sendeleistung_s_11.setStatus("current")
_Letzte_gemessene_donor_reflexion_s_11_Type = DisplayString
_Letzte_gemessene_donor_reflexion_s_11_Object = MibTableColumn
letzte_gemessene_donor_reflexion_s_11 = _Letzte_gemessene_donor_reflexion_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 15),
    _Letzte_gemessene_donor_reflexion_s_11_Type()
)
letzte_gemessene_donor_reflexion_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    letzte_gemessene_donor_reflexion_s_11.setStatus("current")
_Aktuelle_donor_reflexion_s_11_Type = DisplayString
_Aktuelle_donor_reflexion_s_11_Object = MibTableColumn
aktuelle_donor_reflexion_s_11 = _Aktuelle_donor_reflexion_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 16),
    _Aktuelle_donor_reflexion_s_11_Type()
)
aktuelle_donor_reflexion_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_donor_reflexion_s_11.setStatus("current")
_Anzahl_gemessener_praesenzsignale_im_testmode_s_11_Type = DisplayString
_Anzahl_gemessener_praesenzsignale_im_testmode_s_11_Object = MibTableColumn
anzahl_gemessener_praesenzsignale_im_testmode_s_11 = _Anzahl_gemessener_praesenzsignale_im_testmode_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 18),
    _Anzahl_gemessener_praesenzsignale_im_testmode_s_11_Type()
)
anzahl_gemessener_praesenzsignale_im_testmode_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anzahl_gemessener_praesenzsignale_im_testmode_s_11.setStatus("current")
_Aktuelle_ausgangsspannung_ub_s_11_Type = DisplayString
_Aktuelle_ausgangsspannung_ub_s_11_Object = MibTableColumn
aktuelle_ausgangsspannung_ub_s_11 = _Aktuelle_ausgangsspannung_ub_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 19),
    _Aktuelle_ausgangsspannung_ub_s_11_Type()
)
aktuelle_ausgangsspannung_ub_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_ub_s_11.setStatus("current")
_Aktuelle_ausgangsspannung_u1_s_11_Type = DisplayString
_Aktuelle_ausgangsspannung_u1_s_11_Object = MibTableColumn
aktuelle_ausgangsspannung_u1_s_11 = _Aktuelle_ausgangsspannung_u1_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 20),
    _Aktuelle_ausgangsspannung_u1_s_11_Type()
)
aktuelle_ausgangsspannung_u1_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u1_s_11.setStatus("current")
_Aktuelle_ausgangsspannung_u2_s_11_Type = DisplayString
_Aktuelle_ausgangsspannung_u2_s_11_Object = MibTableColumn
aktuelle_ausgangsspannung_u2_s_11 = _Aktuelle_ausgangsspannung_u2_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 21),
    _Aktuelle_ausgangsspannung_u2_s_11_Type()
)
aktuelle_ausgangsspannung_u2_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u2_s_11.setStatus("current")
_Aktuelle_ausgangsspannung_u3_s_11_Type = DisplayString
_Aktuelle_ausgangsspannung_u3_s_11_Object = MibTableColumn
aktuelle_ausgangsspannung_u3_s_11 = _Aktuelle_ausgangsspannung_u3_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 22),
    _Aktuelle_ausgangsspannung_u3_s_11_Type()
)
aktuelle_ausgangsspannung_u3_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u3_s_11.setStatus("current")
_Aktuelle_ausgangsspannung_u4_s_11_Type = DisplayString
_Aktuelle_ausgangsspannung_u4_s_11_Object = MibTableColumn
aktuelle_ausgangsspannung_u4_s_11 = _Aktuelle_ausgangsspannung_u4_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 23),
    _Aktuelle_ausgangsspannung_u4_s_11_Type()
)
aktuelle_ausgangsspannung_u4_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u4_s_11.setStatus("current")
_Aktuelle_ausgangsspannung_u5_s_11_Type = DisplayString
_Aktuelle_ausgangsspannung_u5_s_11_Object = MibTableColumn
aktuelle_ausgangsspannung_u5_s_11 = _Aktuelle_ausgangsspannung_u5_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 24),
    _Aktuelle_ausgangsspannung_u5_s_11_Type()
)
aktuelle_ausgangsspannung_u5_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u5_s_11.setStatus("current")
_Aktuelle_ausgangsspannung_u6_s_11_Type = DisplayString
_Aktuelle_ausgangsspannung_u6_s_11_Object = MibTableColumn
aktuelle_ausgangsspannung_u6_s_11 = _Aktuelle_ausgangsspannung_u6_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 25),
    _Aktuelle_ausgangsspannung_u6_s_11_Type()
)
aktuelle_ausgangsspannung_u6_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u6_s_11.setStatus("current")
_Aktuelle_ausgangsspannung_u7_s_11_Type = DisplayString
_Aktuelle_ausgangsspannung_u7_s_11_Object = MibTableColumn
aktuelle_ausgangsspannung_u7_s_11 = _Aktuelle_ausgangsspannung_u7_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 26),
    _Aktuelle_ausgangsspannung_u7_s_11_Type()
)
aktuelle_ausgangsspannung_u7_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u7_s_11.setStatus("current")
_Aktuelle_ausgangsspannung_u8_s_11_Type = DisplayString
_Aktuelle_ausgangsspannung_u8_s_11_Object = MibTableColumn
aktuelle_ausgangsspannung_u8_s_11 = _Aktuelle_ausgangsspannung_u8_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 27),
    _Aktuelle_ausgangsspannung_u8_s_11_Type()
)
aktuelle_ausgangsspannung_u8_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u8_s_11.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_1_s_11_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_1_s_11_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_1_s_11 = _Aktuelle_ladespannung_an_akku_kreis_1_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 28),
    _Aktuelle_ladespannung_an_akku_kreis_1_s_11_Type()
)
aktuelle_ladespannung_an_akku_kreis_1_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_1_s_11.setStatus("current")
_Aktuelle_ladespannung_an_akku_Kreis_2_s_11_Type = DisplayString
_Aktuelle_ladespannung_an_akku_Kreis_2_s_11_Object = MibTableColumn
aktuelle_ladespannung_an_akku_Kreis_2_s_11 = _Aktuelle_ladespannung_an_akku_Kreis_2_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 29),
    _Aktuelle_ladespannung_an_akku_Kreis_2_s_11_Type()
)
aktuelle_ladespannung_an_akku_Kreis_2_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_Kreis_2_s_11.setStatus("current")
_Aktuelle_ladespannung_an_akku_Kreis_3_s_11_Type = DisplayString
_Aktuelle_ladespannung_an_akku_Kreis_3_s_11_Object = MibTableColumn
aktuelle_ladespannung_an_akku_Kreis_3_s_11 = _Aktuelle_ladespannung_an_akku_Kreis_3_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 30),
    _Aktuelle_ladespannung_an_akku_Kreis_3_s_11_Type()
)
aktuelle_ladespannung_an_akku_Kreis_3_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_Kreis_3_s_11.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_4_s_11_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_4_s_11_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_4_s_11 = _Aktuelle_ladespannung_an_akku_kreis_4_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 31),
    _Aktuelle_ladespannung_an_akku_kreis_4_s_11_Type()
)
aktuelle_ladespannung_an_akku_kreis_4_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_4_s_11.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_5_s_11_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_5_s_11_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_5_s_11 = _Aktuelle_ladespannung_an_akku_kreis_5_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 32),
    _Aktuelle_ladespannung_an_akku_kreis_5_s_11_Type()
)
aktuelle_ladespannung_an_akku_kreis_5_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_5_s_11.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_6_s_11_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_6_s_11_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_6_s_11 = _Aktuelle_ladespannung_an_akku_kreis_6_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 33),
    _Aktuelle_ladespannung_an_akku_kreis_6_s_11_Type()
)
aktuelle_ladespannung_an_akku_kreis_6_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_6_s_11.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_7_s_11_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_7_s_11_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_7_s_11 = _Aktuelle_ladespannung_an_akku_kreis_7_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 34),
    _Aktuelle_ladespannung_an_akku_kreis_7_s_11_Type()
)
aktuelle_ladespannung_an_akku_kreis_7_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_7_s_11.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_8_s_11_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_8_s_11_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_8_s_11 = _Aktuelle_ladespannung_an_akku_kreis_8_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 35),
    _Aktuelle_ladespannung_an_akku_kreis_8_s_11_Type()
)
aktuelle_ladespannung_an_akku_kreis_8_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_8_s_11.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_1_s_11_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_1_s_11_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_1_s_11 = _Aktuelle_spannung_an_akku_kreis_1_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 36),
    _Aktuelle_spannung_an_akku_kreis_1_s_11_Type()
)
aktuelle_spannung_an_akku_kreis_1_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_1_s_11.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_2_s_11_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_2_s_11_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_2_s_11 = _Aktuelle_spannung_an_akku_kreis_2_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 37),
    _Aktuelle_spannung_an_akku_kreis_2_s_11_Type()
)
aktuelle_spannung_an_akku_kreis_2_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_2_s_11.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_3_s_11_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_3_s_11_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_3_s_11 = _Aktuelle_spannung_an_akku_kreis_3_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 38),
    _Aktuelle_spannung_an_akku_kreis_3_s_11_Type()
)
aktuelle_spannung_an_akku_kreis_3_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_3_s_11.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_4_s_11_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_4_s_11_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_4_s_11 = _Aktuelle_spannung_an_akku_kreis_4_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 39),
    _Aktuelle_spannung_an_akku_kreis_4_s_11_Type()
)
aktuelle_spannung_an_akku_kreis_4_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_4_s_11.setStatus("current")
_Aktuelle_spannung_an_akku_reis_5_s_11_Type = DisplayString
_Aktuelle_spannung_an_akku_reis_5_s_11_Object = MibTableColumn
aktuelle_spannung_an_akku_reis_5_s_11 = _Aktuelle_spannung_an_akku_reis_5_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 40),
    _Aktuelle_spannung_an_akku_reis_5_s_11_Type()
)
aktuelle_spannung_an_akku_reis_5_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_reis_5_s_11.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_6_s_11_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_6_s_11_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_6_s_11 = _Aktuelle_spannung_an_akku_kreis_6_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 41),
    _Aktuelle_spannung_an_akku_kreis_6_s_11_Type()
)
aktuelle_spannung_an_akku_kreis_6_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_6_s_11.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_7_s_11_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_7_s_11_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_7_s_11 = _Aktuelle_spannung_an_akku_kreis_7_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 42),
    _Aktuelle_spannung_an_akku_kreis_7_s_11_Type()
)
aktuelle_spannung_an_akku_kreis_7_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_7_s_11.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_8_s_11_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_8_s_11_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_8_s_11 = _Aktuelle_spannung_an_akku_kreis_8_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 43),
    _Aktuelle_spannung_an_akku_kreis_8_s_11_Type()
)
aktuelle_spannung_an_akku_kreis_8_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_8_s_11.setStatus("current")
_Testergebnis_lastspannung_an_akku_reis_1_s_11_Type = DisplayString
_Testergebnis_lastspannung_an_akku_reis_1_s_11_Object = MibTableColumn
testergebnis_lastspannung_an_akku_reis_1_s_11 = _Testergebnis_lastspannung_an_akku_reis_1_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 44),
    _Testergebnis_lastspannung_an_akku_reis_1_s_11_Type()
)
testergebnis_lastspannung_an_akku_reis_1_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_reis_1_s_11.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_2_s_11_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_2_s_11_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_2_s_11 = _Testergebnis_lastspannung_an_akku_kreis_2_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 45),
    _Testergebnis_lastspannung_an_akku_kreis_2_s_11_Type()
)
testergebnis_lastspannung_an_akku_kreis_2_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_2_s_11.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_3_s_11_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_3_s_11_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_3_s_11 = _Testergebnis_lastspannung_an_akku_kreis_3_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 46),
    _Testergebnis_lastspannung_an_akku_kreis_3_s_11_Type()
)
testergebnis_lastspannung_an_akku_kreis_3_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_3_s_11.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_4_s_11_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_4_s_11_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_4_s_11 = _Testergebnis_lastspannung_an_akku_kreis_4_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 47),
    _Testergebnis_lastspannung_an_akku_kreis_4_s_11_Type()
)
testergebnis_lastspannung_an_akku_kreis_4_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_4_s_11.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_5_s_11_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_5_s_11_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_5_s_11 = _Testergebnis_lastspannung_an_akku_kreis_5_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 48),
    _Testergebnis_lastspannung_an_akku_kreis_5_s_11_Type()
)
testergebnis_lastspannung_an_akku_kreis_5_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_5_s_11.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_6_s_11_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_6_s_11_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_6_s_11 = _Testergebnis_lastspannung_an_akku_kreis_6_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 49),
    _Testergebnis_lastspannung_an_akku_kreis_6_s_11_Type()
)
testergebnis_lastspannung_an_akku_kreis_6_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_6_s_11.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_7_s_11_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_7_s_11_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_7_s_11 = _Testergebnis_lastspannung_an_akku_kreis_7_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 50),
    _Testergebnis_lastspannung_an_akku_kreis_7_s_11_Type()
)
testergebnis_lastspannung_an_akku_kreis_7_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_7_s_11.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_8_s_11_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_8_s_11_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_8_s_11 = _Testergebnis_lastspannung_an_akku_kreis_8_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 51),
    _Testergebnis_lastspannung_an_akku_kreis_8_s_11_Type()
)
testergebnis_lastspannung_an_akku_kreis_8_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_8_s_11.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_1_s_11_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_1_s_11_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_1_s_11 = _Testergebnis_innenwiderstand_akku_kreis_1_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 52),
    _Testergebnis_innenwiderstand_akku_kreis_1_s_11_Type()
)
testergebnis_innenwiderstand_akku_kreis_1_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_1_s_11.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_2_s_11_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_2_s_11_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_2_s_11 = _Testergebnis_innenwiderstand_akku_kreis_2_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 53),
    _Testergebnis_innenwiderstand_akku_kreis_2_s_11_Type()
)
testergebnis_innenwiderstand_akku_kreis_2_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_2_s_11.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_3_s_11_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_3_s_11_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_3_s_11 = _Testergebnis_innenwiderstand_akku_kreis_3_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 54),
    _Testergebnis_innenwiderstand_akku_kreis_3_s_11_Type()
)
testergebnis_innenwiderstand_akku_kreis_3_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_3_s_11.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_4_s_11_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_4_s_11_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_4_s_11 = _Testergebnis_innenwiderstand_akku_kreis_4_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 56),
    _Testergebnis_innenwiderstand_akku_kreis_4_s_11_Type()
)
testergebnis_innenwiderstand_akku_kreis_4_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_4_s_11.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_5_s_11_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_5_s_11_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_5_s_11 = _Testergebnis_innenwiderstand_akku_kreis_5_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 57),
    _Testergebnis_innenwiderstand_akku_kreis_5_s_11_Type()
)
testergebnis_innenwiderstand_akku_kreis_5_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_5_s_11.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_6_s_11_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_6_s_11_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_6_s_11 = _Testergebnis_innenwiderstand_akku_kreis_6_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 58),
    _Testergebnis_innenwiderstand_akku_kreis_6_s_11_Type()
)
testergebnis_innenwiderstand_akku_kreis_6_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_6_s_11.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_7_s_11_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_7_s_11_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_7_s_11 = _Testergebnis_innenwiderstand_akku_kreis_7_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 59),
    _Testergebnis_innenwiderstand_akku_kreis_7_s_11_Type()
)
testergebnis_innenwiderstand_akku_kreis_7_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_7_s_11.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_8_s_11_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_8_s_11_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_8_s_11 = _Testergebnis_innenwiderstand_akku_kreis_8_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 60),
    _Testergebnis_innenwiderstand_akku_kreis_8_s_11_Type()
)
testergebnis_innenwiderstand_akku_kreis_8_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_8_s_11.setStatus("current")
_Netzteilspannung_uin1_s_11_Type = DisplayString
_Netzteilspannung_uin1_s_11_Object = MibTableColumn
netzteilspannung_uin1_s_11 = _Netzteilspannung_uin1_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 61),
    _Netzteilspannung_uin1_s_11_Type()
)
netzteilspannung_uin1_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzteilspannung_uin1_s_11.setStatus("current")
_Netzteilspannung_uin2_s_11_Type = DisplayString
_Netzteilspannung_uin2_s_11_Object = MibTableColumn
netzteilspannung_uin2_s_11 = _Netzteilspannung_uin2_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 62),
    _Netzteilspannung_uin2_s_11_Type()
)
netzteilspannung_uin2_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzteilspannung_uin2_s_11.setStatus("current")
_Programmierte_minimale_soll_sendeleistung_s_11_Type = DisplayString
_Programmierte_minimale_soll_sendeleistung_s_11_Object = MibTableColumn
programmierte_minimale_soll_sendeleistung_s_11 = _Programmierte_minimale_soll_sendeleistung_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 63),
    _Programmierte_minimale_soll_sendeleistung_s_11_Type()
)
programmierte_minimale_soll_sendeleistung_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programmierte_minimale_soll_sendeleistung_s_11.setStatus("current")
_Programmierte_maximale_antennen_reflexion_s_11_Type = DisplayString
_Programmierte_maximale_antennen_reflexion_s_11_Object = MibTableColumn
programmierte_maximale_antennen_reflexion_s_11 = _Programmierte_maximale_antennen_reflexion_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 64),
    _Programmierte_maximale_antennen_reflexion_s_11_Type()
)
programmierte_maximale_antennen_reflexion_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programmierte_maximale_antennen_reflexion_s_11.setStatus("current")
_Programmierte_minimale_anzahl_praesenzsignale_s_11_Type = DisplayString
_Programmierte_minimale_anzahl_praesenzsignale_s_11_Object = MibTableColumn
programmierte_minimale_anzahl_praesenzsignale_s_11 = _Programmierte_minimale_anzahl_praesenzsignale_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 65),
    _Programmierte_minimale_anzahl_praesenzsignale_s_11_Type()
)
programmierte_minimale_anzahl_praesenzsignale_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programmierte_minimale_anzahl_praesenzsignale_s_11.setStatus("current")
_Summen_fehlerstatus_von_tmoa_anlage_s_11_Type = DisplayString
_Summen_fehlerstatus_von_tmoa_anlage_s_11_Object = MibTableColumn
summen_fehlerstatus_von_tmoa_anlage_s_11 = _Summen_fehlerstatus_von_tmoa_anlage_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 66),
    _Summen_fehlerstatus_von_tmoa_anlage_s_11_Type()
)
summen_fehlerstatus_von_tmoa_anlage_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summen_fehlerstatus_von_tmoa_anlage_s_11.setStatus("current")
_Summen_fehlerstatus_von_anbinderepeater_s_11_Type = DisplayString
_Summen_fehlerstatus_von_anbinderepeater_s_11_Object = MibTableColumn
summen_fehlerstatus_von_anbinderepeater_s_11 = _Summen_fehlerstatus_von_anbinderepeater_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 67),
    _Summen_fehlerstatus_von_anbinderepeater_s_11_Type()
)
summen_fehlerstatus_von_anbinderepeater_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summen_fehlerstatus_von_anbinderepeater_s_11.setStatus("current")
_Summen_fehlerstatus_von_analogem_repeater_s_11_Type = DisplayString
_Summen_fehlerstatus_von_analogem_repeater_s_11_Object = MibTableColumn
summen_fehlerstatus_von_analogem_repeater_s_11 = _Summen_fehlerstatus_von_analogem_repeater_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 68),
    _Summen_fehlerstatus_von_analogem_repeater_s_11_Type()
)
summen_fehlerstatus_von_analogem_repeater_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summen_fehlerstatus_von_analogem_repeater_s_11.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_11_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_11_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_11 = _Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 69),
    _Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_11_Type()
)
aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_11.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_11_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_11_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_11 = _Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 70),
    _Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_11_Type()
)
aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_11.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_11_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_11_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_11 = _Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 71),
    _Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_11_Type()
)
aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_11.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_11_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_11_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_11 = _Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 72),
    _Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_11_Type()
)
aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_11.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_11_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_11_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_11 = _Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 73),
    _Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_11_Type()
)
aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_11.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_11_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_11_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_11 = _Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 74),
    _Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_11_Type()
)
aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_11.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_11_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_11_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_11 = _Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 75),
    _Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_11_Type()
)
aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_11.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_11_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_11_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_11 = _Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 76),
    _Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_11_Type()
)
aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_11.setStatus("current")
_Netzspannungsversorgung_von_tmoa_anlage_s_11_Type = DisplayString
_Netzspannungsversorgung_von_tmoa_anlage_s_11_Object = MibTableColumn
netzspannungsversorgung_von_tmoa_anlage_s_11 = _Netzspannungsversorgung_von_tmoa_anlage_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 77),
    _Netzspannungsversorgung_von_tmoa_anlage_s_11_Type()
)
netzspannungsversorgung_von_tmoa_anlage_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzspannungsversorgung_von_tmoa_anlage_s_11.setStatus("current")
_Netzspannungsversorgung_von_anbinderepeater_s_11_Type = DisplayString
_Netzspannungsversorgung_von_anbinderepeater_s_11_Object = MibTableColumn
netzspannungsversorgung_von_anbinderepeater_s_11 = _Netzspannungsversorgung_von_anbinderepeater_s_11_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 1, 1, 78),
    _Netzspannungsversorgung_von_anbinderepeater_s_11_Type()
)
netzspannungsversorgung_von_anbinderepeater_s_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzspannungsversorgung_von_anbinderepeater_s_11.setStatus("current")
_ModulTable_traps_m_Object = MibTable
modulTable_traps_m = _ModulTable_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12)
)
if mibBuilder.loadTexts:
    modulTable_traps_m.setStatus("current")
_ModulEntry_traps_m_Object = MibTableRow
modulEntry_traps_m = _ModulEntry_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1)
)
modulEntry_traps_m.setIndexNames(
    (0, "AK-FUNKTECHNIK-MIB", "modulIndex-traps-m"),
)
if mibBuilder.loadTexts:
    modulEntry_traps_m.setStatus("current")
_ModulIndex_traps_m_Type = DisplayString
_ModulIndex_traps_m_Object = MibTableColumn
modulIndex_traps_m = _ModulIndex_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 1),
    _ModulIndex_traps_m_Type()
)
modulIndex_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulIndex_traps_m.setStatus("current")
_Geraete_typ_traps_m_Type = DisplayString
_Geraete_typ_traps_m_Object = MibTableColumn
geraete_typ_traps_m = _Geraete_typ_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 2),
    _Geraete_typ_traps_m_Type()
)
geraete_typ_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geraete_typ_traps_m.setStatus("current")
_Betriebsstatus_traps_m_Type = DisplayString
_Betriebsstatus_traps_m_Object = MibTableColumn
betriebsstatus_traps_m = _Betriebsstatus_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 3),
    _Betriebsstatus_traps_m_Type()
)
betriebsstatus_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    betriebsstatus_traps_m.setStatus("current")
_Senderstatus_traps_m_Type = DisplayString
_Senderstatus_traps_m_Object = MibTableColumn
senderstatus_traps_m = _Senderstatus_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 4),
    _Senderstatus_traps_m_Type()
)
senderstatus_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    senderstatus_traps_m.setStatus("current")
_Fehlerstatus_traps_m_Type = DisplayString
_Fehlerstatus_traps_m_Object = MibTableColumn
fehlerstatus_traps_m = _Fehlerstatus_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 5),
    _Fehlerstatus_traps_m_Type()
)
fehlerstatus_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fehlerstatus_traps_m.setStatus("current")
_Dem_adapter_zugeordnete_funkgeraetetype_traps_m_Type = DisplayString
_Dem_adapter_zugeordnete_funkgeraetetype_traps_m_Object = MibTableColumn
dem_adapter_zugeordnete_funkgeraetetype_traps_m = _Dem_adapter_zugeordnete_funkgeraetetype_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 6),
    _Dem_adapter_zugeordnete_funkgeraetetype_traps_m_Type()
)
dem_adapter_zugeordnete_funkgeraetetype_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dem_adapter_zugeordnete_funkgeraetetype_traps_m.setStatus("current")
_Eingabe_und_anzeigemodul_traps_m_Type = DisplayString
_Eingabe_und_anzeigemodul_traps_m_Object = MibTableColumn
eingabe_und_anzeigemodul_traps_m = _Eingabe_und_anzeigemodul_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 7),
    _Eingabe_und_anzeigemodul_traps_m_Type()
)
eingabe_und_anzeigemodul_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eingabe_und_anzeigemodul_traps_m.setStatus("current")
_Mod_bus_verbindung_module_traps_m_Type = DisplayString
_Mod_bus_verbindung_module_traps_m_Object = MibTableColumn
mod_bus_verbindung_module_traps_m = _Mod_bus_verbindung_module_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 8),
    _Mod_bus_verbindung_module_traps_m_Type()
)
mod_bus_verbindung_module_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mod_bus_verbindung_module_traps_m.setStatus("current")
_Gemessene_sendeleistung_im_testmode_traps_m_Type = DisplayString
_Gemessene_sendeleistung_im_testmode_traps_m_Object = MibTableColumn
gemessene_sendeleistung_im_testmode_traps_m = _Gemessene_sendeleistung_im_testmode_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 9),
    _Gemessene_sendeleistung_im_testmode_traps_m_Type()
)
gemessene_sendeleistung_im_testmode_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemessene_sendeleistung_im_testmode_traps_m.setStatus("current")
_Aktuelle_sendeleistung_traps_m_Type = DisplayString
_Aktuelle_sendeleistung_traps_m_Object = MibTableColumn
aktuelle_sendeleistung_traps_m = _Aktuelle_sendeleistung_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 10),
    _Aktuelle_sendeleistung_traps_m_Type()
)
aktuelle_sendeleistung_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_sendeleistung_traps_m.setStatus("current")
_Gemessene_reflexion_im_testmode_traps_m_Type = DisplayString
_Gemessene_reflexion_im_testmode_traps_m_Object = MibTableColumn
gemessene_reflexion_im_testmode_traps_m = _Gemessene_reflexion_im_testmode_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 11),
    _Gemessene_reflexion_im_testmode_traps_m_Type()
)
gemessene_reflexion_im_testmode_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gemessene_reflexion_im_testmode_traps_m.setStatus("current")
_Aktuelle_reflexion_traps_m_Type = DisplayString
_Aktuelle_reflexion_traps_m_Object = MibTableColumn
aktuelle_reflexion_traps_m = _Aktuelle_reflexion_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 12),
    _Aktuelle_reflexion_traps_m_Type()
)
aktuelle_reflexion_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_reflexion_traps_m.setStatus("current")
_Letzte_gemessene_donor_sendeleistung_traps_m_Type = DisplayString
_Letzte_gemessene_donor_sendeleistung_traps_m_Object = MibTableColumn
letzte_gemessene_donor_sendeleistung_traps_m = _Letzte_gemessene_donor_sendeleistung_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 13),
    _Letzte_gemessene_donor_sendeleistung_traps_m_Type()
)
letzte_gemessene_donor_sendeleistung_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    letzte_gemessene_donor_sendeleistung_traps_m.setStatus("current")
_Aktuelle_donor_sendeleistung_traps_m_Type = DisplayString
_Aktuelle_donor_sendeleistung_traps_m_Object = MibTableColumn
aktuelle_donor_sendeleistung_traps_m = _Aktuelle_donor_sendeleistung_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 14),
    _Aktuelle_donor_sendeleistung_traps_m_Type()
)
aktuelle_donor_sendeleistung_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_donor_sendeleistung_traps_m.setStatus("current")
_Letzte_gemessene_donor_reflexion_traps_m_Type = DisplayString
_Letzte_gemessene_donor_reflexion_traps_m_Object = MibTableColumn
letzte_gemessene_donor_reflexion_traps_m = _Letzte_gemessene_donor_reflexion_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 15),
    _Letzte_gemessene_donor_reflexion_traps_m_Type()
)
letzte_gemessene_donor_reflexion_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    letzte_gemessene_donor_reflexion_traps_m.setStatus("current")
_Aktuelle_donor_reflexion_traps_m_Type = DisplayString
_Aktuelle_donor_reflexion_traps_m_Object = MibTableColumn
aktuelle_donor_reflexion_traps_m = _Aktuelle_donor_reflexion_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 16),
    _Aktuelle_donor_reflexion_traps_m_Type()
)
aktuelle_donor_reflexion_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_donor_reflexion_traps_m.setStatus("current")
_Anzahl_gemessener_praesenzsignale_im_testmode_traps_m_Type = DisplayString
_Anzahl_gemessener_praesenzsignale_im_testmode_traps_m_Object = MibTableColumn
anzahl_gemessener_praesenzsignale_im_testmode_traps_m = _Anzahl_gemessener_praesenzsignale_im_testmode_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 18),
    _Anzahl_gemessener_praesenzsignale_im_testmode_traps_m_Type()
)
anzahl_gemessener_praesenzsignale_im_testmode_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anzahl_gemessener_praesenzsignale_im_testmode_traps_m.setStatus("current")
_Aktuelle_ausgangsspannung_ub_traps_m_Type = DisplayString
_Aktuelle_ausgangsspannung_ub_traps_m_Object = MibTableColumn
aktuelle_ausgangsspannung_ub_traps_m = _Aktuelle_ausgangsspannung_ub_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 19),
    _Aktuelle_ausgangsspannung_ub_traps_m_Type()
)
aktuelle_ausgangsspannung_ub_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_ub_traps_m.setStatus("current")
_Aktuelle_ausgangsspannung_u1_traps_m_Type = DisplayString
_Aktuelle_ausgangsspannung_u1_traps_m_Object = MibTableColumn
aktuelle_ausgangsspannung_u1_traps_m = _Aktuelle_ausgangsspannung_u1_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 20),
    _Aktuelle_ausgangsspannung_u1_traps_m_Type()
)
aktuelle_ausgangsspannung_u1_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u1_traps_m.setStatus("current")
_Aktuelle_ausgangsspannung_u2_traps_m_Type = DisplayString
_Aktuelle_ausgangsspannung_u2_traps_m_Object = MibTableColumn
aktuelle_ausgangsspannung_u2_traps_m = _Aktuelle_ausgangsspannung_u2_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 21),
    _Aktuelle_ausgangsspannung_u2_traps_m_Type()
)
aktuelle_ausgangsspannung_u2_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u2_traps_m.setStatus("current")
_Aktuelle_ausgangsspannung_u3_traps_m_Type = DisplayString
_Aktuelle_ausgangsspannung_u3_traps_m_Object = MibTableColumn
aktuelle_ausgangsspannung_u3_traps_m = _Aktuelle_ausgangsspannung_u3_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 22),
    _Aktuelle_ausgangsspannung_u3_traps_m_Type()
)
aktuelle_ausgangsspannung_u3_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u3_traps_m.setStatus("current")
_Aktuelle_ausgangsspannung_u4_traps_m_Type = DisplayString
_Aktuelle_ausgangsspannung_u4_traps_m_Object = MibTableColumn
aktuelle_ausgangsspannung_u4_traps_m = _Aktuelle_ausgangsspannung_u4_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 23),
    _Aktuelle_ausgangsspannung_u4_traps_m_Type()
)
aktuelle_ausgangsspannung_u4_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u4_traps_m.setStatus("current")
_Aktuelle_ausgangsspannung_u5_traps_m_Type = DisplayString
_Aktuelle_ausgangsspannung_u5_traps_m_Object = MibTableColumn
aktuelle_ausgangsspannung_u5_traps_m = _Aktuelle_ausgangsspannung_u5_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 24),
    _Aktuelle_ausgangsspannung_u5_traps_m_Type()
)
aktuelle_ausgangsspannung_u5_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u5_traps_m.setStatus("current")
_Aktuelle_ausgangsspannung_u6_traps_m_Type = DisplayString
_Aktuelle_ausgangsspannung_u6_traps_m_Object = MibTableColumn
aktuelle_ausgangsspannung_u6_traps_m = _Aktuelle_ausgangsspannung_u6_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 25),
    _Aktuelle_ausgangsspannung_u6_traps_m_Type()
)
aktuelle_ausgangsspannung_u6_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u6_traps_m.setStatus("current")
_Aktuelle_ausgangsspannung_u7_traps_m_Type = DisplayString
_Aktuelle_ausgangsspannung_u7_traps_m_Object = MibTableColumn
aktuelle_ausgangsspannung_u7_traps_m = _Aktuelle_ausgangsspannung_u7_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 26),
    _Aktuelle_ausgangsspannung_u7_traps_m_Type()
)
aktuelle_ausgangsspannung_u7_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u7_traps_m.setStatus("current")
_Aktuelle_ausgangsspannung_u8_traps_m_Type = DisplayString
_Aktuelle_ausgangsspannung_u8_traps_m_Object = MibTableColumn
aktuelle_ausgangsspannung_u8_traps_m = _Aktuelle_ausgangsspannung_u8_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 27),
    _Aktuelle_ausgangsspannung_u8_traps_m_Type()
)
aktuelle_ausgangsspannung_u8_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ausgangsspannung_u8_traps_m.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_1_traps_m_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_1_traps_m_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_1_traps_m = _Aktuelle_ladespannung_an_akku_kreis_1_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 28),
    _Aktuelle_ladespannung_an_akku_kreis_1_traps_m_Type()
)
aktuelle_ladespannung_an_akku_kreis_1_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_1_traps_m.setStatus("current")
_Aktuelle_ladespannung_an_akku_Kreis_2_traps_m_Type = DisplayString
_Aktuelle_ladespannung_an_akku_Kreis_2_traps_m_Object = MibTableColumn
aktuelle_ladespannung_an_akku_Kreis_2_traps_m = _Aktuelle_ladespannung_an_akku_Kreis_2_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 29),
    _Aktuelle_ladespannung_an_akku_Kreis_2_traps_m_Type()
)
aktuelle_ladespannung_an_akku_Kreis_2_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_Kreis_2_traps_m.setStatus("current")
_Aktuelle_ladespannung_an_akku_Kreis_3_traps_m_Type = DisplayString
_Aktuelle_ladespannung_an_akku_Kreis_3_traps_m_Object = MibTableColumn
aktuelle_ladespannung_an_akku_Kreis_3_traps_m = _Aktuelle_ladespannung_an_akku_Kreis_3_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 30),
    _Aktuelle_ladespannung_an_akku_Kreis_3_traps_m_Type()
)
aktuelle_ladespannung_an_akku_Kreis_3_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_Kreis_3_traps_m.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_4_traps_m_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_4_traps_m_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_4_traps_m = _Aktuelle_ladespannung_an_akku_kreis_4_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 31),
    _Aktuelle_ladespannung_an_akku_kreis_4_traps_m_Type()
)
aktuelle_ladespannung_an_akku_kreis_4_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_4_traps_m.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_5_traps_m_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_5_traps_m_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_5_traps_m = _Aktuelle_ladespannung_an_akku_kreis_5_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 32),
    _Aktuelle_ladespannung_an_akku_kreis_5_traps_m_Type()
)
aktuelle_ladespannung_an_akku_kreis_5_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_5_traps_m.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_6_traps_m_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_6_traps_m_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_6_traps_m = _Aktuelle_ladespannung_an_akku_kreis_6_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 33),
    _Aktuelle_ladespannung_an_akku_kreis_6_traps_m_Type()
)
aktuelle_ladespannung_an_akku_kreis_6_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_6_traps_m.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_7_traps_m_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_7_traps_m_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_7_traps_m = _Aktuelle_ladespannung_an_akku_kreis_7_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 34),
    _Aktuelle_ladespannung_an_akku_kreis_7_traps_m_Type()
)
aktuelle_ladespannung_an_akku_kreis_7_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_7_traps_m.setStatus("current")
_Aktuelle_ladespannung_an_akku_kreis_8_traps_m_Type = DisplayString
_Aktuelle_ladespannung_an_akku_kreis_8_traps_m_Object = MibTableColumn
aktuelle_ladespannung_an_akku_kreis_8_traps_m = _Aktuelle_ladespannung_an_akku_kreis_8_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 35),
    _Aktuelle_ladespannung_an_akku_kreis_8_traps_m_Type()
)
aktuelle_ladespannung_an_akku_kreis_8_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_an_akku_kreis_8_traps_m.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_1_traps_m_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_1_traps_m_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_1_traps_m = _Aktuelle_spannung_an_akku_kreis_1_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 36),
    _Aktuelle_spannung_an_akku_kreis_1_traps_m_Type()
)
aktuelle_spannung_an_akku_kreis_1_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_1_traps_m.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_2_traps_m_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_2_traps_m_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_2_traps_m = _Aktuelle_spannung_an_akku_kreis_2_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 37),
    _Aktuelle_spannung_an_akku_kreis_2_traps_m_Type()
)
aktuelle_spannung_an_akku_kreis_2_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_2_traps_m.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_3_traps_m_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_3_traps_m_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_3_traps_m = _Aktuelle_spannung_an_akku_kreis_3_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 38),
    _Aktuelle_spannung_an_akku_kreis_3_traps_m_Type()
)
aktuelle_spannung_an_akku_kreis_3_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_3_traps_m.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_4_traps_m_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_4_traps_m_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_4_traps_m = _Aktuelle_spannung_an_akku_kreis_4_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 39),
    _Aktuelle_spannung_an_akku_kreis_4_traps_m_Type()
)
aktuelle_spannung_an_akku_kreis_4_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_4_traps_m.setStatus("current")
_Aktuelle_spannung_an_akku_reis_5_traps_m_Type = DisplayString
_Aktuelle_spannung_an_akku_reis_5_traps_m_Object = MibTableColumn
aktuelle_spannung_an_akku_reis_5_traps_m = _Aktuelle_spannung_an_akku_reis_5_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 40),
    _Aktuelle_spannung_an_akku_reis_5_traps_m_Type()
)
aktuelle_spannung_an_akku_reis_5_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_reis_5_traps_m.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_6_traps_m_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_6_traps_m_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_6_traps_m = _Aktuelle_spannung_an_akku_kreis_6_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 41),
    _Aktuelle_spannung_an_akku_kreis_6_traps_m_Type()
)
aktuelle_spannung_an_akku_kreis_6_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_6_traps_m.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_7_traps_m_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_7_traps_m_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_7_traps_m = _Aktuelle_spannung_an_akku_kreis_7_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 42),
    _Aktuelle_spannung_an_akku_kreis_7_traps_m_Type()
)
aktuelle_spannung_an_akku_kreis_7_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_7_traps_m.setStatus("current")
_Aktuelle_spannung_an_akku_kreis_8_traps_m_Type = DisplayString
_Aktuelle_spannung_an_akku_kreis_8_traps_m_Object = MibTableColumn
aktuelle_spannung_an_akku_kreis_8_traps_m = _Aktuelle_spannung_an_akku_kreis_8_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 43),
    _Aktuelle_spannung_an_akku_kreis_8_traps_m_Type()
)
aktuelle_spannung_an_akku_kreis_8_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_spannung_an_akku_kreis_8_traps_m.setStatus("current")
_Testergebnis_lastspannung_an_akku_reis_1_traps_m_Type = DisplayString
_Testergebnis_lastspannung_an_akku_reis_1_traps_m_Object = MibTableColumn
testergebnis_lastspannung_an_akku_reis_1_traps_m = _Testergebnis_lastspannung_an_akku_reis_1_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 44),
    _Testergebnis_lastspannung_an_akku_reis_1_traps_m_Type()
)
testergebnis_lastspannung_an_akku_reis_1_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_reis_1_traps_m.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_2_traps_m_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_2_traps_m_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_2_traps_m = _Testergebnis_lastspannung_an_akku_kreis_2_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 45),
    _Testergebnis_lastspannung_an_akku_kreis_2_traps_m_Type()
)
testergebnis_lastspannung_an_akku_kreis_2_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_2_traps_m.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_3_traps_m_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_3_traps_m_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_3_traps_m = _Testergebnis_lastspannung_an_akku_kreis_3_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 46),
    _Testergebnis_lastspannung_an_akku_kreis_3_traps_m_Type()
)
testergebnis_lastspannung_an_akku_kreis_3_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_3_traps_m.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_4_traps_m_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_4_traps_m_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_4_traps_m = _Testergebnis_lastspannung_an_akku_kreis_4_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 47),
    _Testergebnis_lastspannung_an_akku_kreis_4_traps_m_Type()
)
testergebnis_lastspannung_an_akku_kreis_4_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_4_traps_m.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_5_traps_m_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_5_traps_m_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_5_traps_m = _Testergebnis_lastspannung_an_akku_kreis_5_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 48),
    _Testergebnis_lastspannung_an_akku_kreis_5_traps_m_Type()
)
testergebnis_lastspannung_an_akku_kreis_5_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_5_traps_m.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_6_traps_m_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_6_traps_m_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_6_traps_m = _Testergebnis_lastspannung_an_akku_kreis_6_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 49),
    _Testergebnis_lastspannung_an_akku_kreis_6_traps_m_Type()
)
testergebnis_lastspannung_an_akku_kreis_6_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_6_traps_m.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_7_traps_m_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_7_traps_m_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_7_traps_m = _Testergebnis_lastspannung_an_akku_kreis_7_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 50),
    _Testergebnis_lastspannung_an_akku_kreis_7_traps_m_Type()
)
testergebnis_lastspannung_an_akku_kreis_7_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_7_traps_m.setStatus("current")
_Testergebnis_lastspannung_an_akku_kreis_8_traps_m_Type = DisplayString
_Testergebnis_lastspannung_an_akku_kreis_8_traps_m_Object = MibTableColumn
testergebnis_lastspannung_an_akku_kreis_8_traps_m = _Testergebnis_lastspannung_an_akku_kreis_8_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 51),
    _Testergebnis_lastspannung_an_akku_kreis_8_traps_m_Type()
)
testergebnis_lastspannung_an_akku_kreis_8_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_lastspannung_an_akku_kreis_8_traps_m.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_1_traps_m_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_1_traps_m_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_1_traps_m = _Testergebnis_innenwiderstand_akku_kreis_1_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 52),
    _Testergebnis_innenwiderstand_akku_kreis_1_traps_m_Type()
)
testergebnis_innenwiderstand_akku_kreis_1_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_1_traps_m.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_2_traps_m_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_2_traps_m_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_2_traps_m = _Testergebnis_innenwiderstand_akku_kreis_2_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 53),
    _Testergebnis_innenwiderstand_akku_kreis_2_traps_m_Type()
)
testergebnis_innenwiderstand_akku_kreis_2_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_2_traps_m.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_3_traps_m_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_3_traps_m_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_3_traps_m = _Testergebnis_innenwiderstand_akku_kreis_3_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 54),
    _Testergebnis_innenwiderstand_akku_kreis_3_traps_m_Type()
)
testergebnis_innenwiderstand_akku_kreis_3_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_3_traps_m.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_4_traps_m_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_4_traps_m_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_4_traps_m = _Testergebnis_innenwiderstand_akku_kreis_4_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 56),
    _Testergebnis_innenwiderstand_akku_kreis_4_traps_m_Type()
)
testergebnis_innenwiderstand_akku_kreis_4_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_4_traps_m.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_5_traps_m_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_5_traps_m_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_5_traps_m = _Testergebnis_innenwiderstand_akku_kreis_5_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 57),
    _Testergebnis_innenwiderstand_akku_kreis_5_traps_m_Type()
)
testergebnis_innenwiderstand_akku_kreis_5_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_5_traps_m.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_6_traps_m_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_6_traps_m_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_6_traps_m = _Testergebnis_innenwiderstand_akku_kreis_6_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 58),
    _Testergebnis_innenwiderstand_akku_kreis_6_traps_m_Type()
)
testergebnis_innenwiderstand_akku_kreis_6_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_6_traps_m.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_7_traps_m_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_7_traps_m_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_7_traps_m = _Testergebnis_innenwiderstand_akku_kreis_7_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 59),
    _Testergebnis_innenwiderstand_akku_kreis_7_traps_m_Type()
)
testergebnis_innenwiderstand_akku_kreis_7_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_7_traps_m.setStatus("current")
_Testergebnis_innenwiderstand_akku_kreis_8_traps_m_Type = DisplayString
_Testergebnis_innenwiderstand_akku_kreis_8_traps_m_Object = MibTableColumn
testergebnis_innenwiderstand_akku_kreis_8_traps_m = _Testergebnis_innenwiderstand_akku_kreis_8_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 60),
    _Testergebnis_innenwiderstand_akku_kreis_8_traps_m_Type()
)
testergebnis_innenwiderstand_akku_kreis_8_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testergebnis_innenwiderstand_akku_kreis_8_traps_m.setStatus("current")
_Netzteilspannung_uin1_traps_m_Type = DisplayString
_Netzteilspannung_uin1_traps_m_Object = MibTableColumn
netzteilspannung_uin1_traps_m = _Netzteilspannung_uin1_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 61),
    _Netzteilspannung_uin1_traps_m_Type()
)
netzteilspannung_uin1_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzteilspannung_uin1_traps_m.setStatus("current")
_Netzteilspannung_uin2_traps_m_Type = DisplayString
_Netzteilspannung_uin2_traps_m_Object = MibTableColumn
netzteilspannung_uin2_traps_m = _Netzteilspannung_uin2_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 62),
    _Netzteilspannung_uin2_traps_m_Type()
)
netzteilspannung_uin2_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzteilspannung_uin2_traps_m.setStatus("current")
_Programmierte_minimale_soll_sendeleistung_traps_m_Type = DisplayString
_Programmierte_minimale_soll_sendeleistung_traps_m_Object = MibTableColumn
programmierte_minimale_soll_sendeleistung_traps_m = _Programmierte_minimale_soll_sendeleistung_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 63),
    _Programmierte_minimale_soll_sendeleistung_traps_m_Type()
)
programmierte_minimale_soll_sendeleistung_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programmierte_minimale_soll_sendeleistung_traps_m.setStatus("current")
_Programmierte_maximale_antennen_reflexion_traps_m_Type = DisplayString
_Programmierte_maximale_antennen_reflexion_traps_m_Object = MibTableColumn
programmierte_maximale_antennen_reflexion_traps_m = _Programmierte_maximale_antennen_reflexion_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 64),
    _Programmierte_maximale_antennen_reflexion_traps_m_Type()
)
programmierte_maximale_antennen_reflexion_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programmierte_maximale_antennen_reflexion_traps_m.setStatus("current")
_Programmierte_minimale_anzahl_praesenzsignale_traps_m_Type = DisplayString
_Programmierte_minimale_anzahl_praesenzsignale_traps_m_Object = MibTableColumn
programmierte_minimale_anzahl_praesenzsignale_traps_m = _Programmierte_minimale_anzahl_praesenzsignale_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 65),
    _Programmierte_minimale_anzahl_praesenzsignale_traps_m_Type()
)
programmierte_minimale_anzahl_praesenzsignale_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    programmierte_minimale_anzahl_praesenzsignale_traps_m.setStatus("current")
_Summen_fehlerstatus_von_tmoa_anlage_traps_m_Type = DisplayString
_Summen_fehlerstatus_von_tmoa_anlage_traps_m_Object = MibTableColumn
summen_fehlerstatus_von_tmoa_anlage_traps_m = _Summen_fehlerstatus_von_tmoa_anlage_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 66),
    _Summen_fehlerstatus_von_tmoa_anlage_traps_m_Type()
)
summen_fehlerstatus_von_tmoa_anlage_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summen_fehlerstatus_von_tmoa_anlage_traps_m.setStatus("current")
_Summen_fehlerstatus_von_anbinderepeater_traps_m_Type = DisplayString
_Summen_fehlerstatus_von_anbinderepeater_traps_m_Object = MibTableColumn
summen_fehlerstatus_von_anbinderepeater_traps_m = _Summen_fehlerstatus_von_anbinderepeater_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 67),
    _Summen_fehlerstatus_von_anbinderepeater_traps_m_Type()
)
summen_fehlerstatus_von_anbinderepeater_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summen_fehlerstatus_von_anbinderepeater_traps_m.setStatus("current")
_Summen_fehlerstatus_von_analogem_repeater_traps_m_Type = DisplayString
_Summen_fehlerstatus_von_analogem_repeater_traps_m_Object = MibTableColumn
summen_fehlerstatus_von_analogem_repeater_traps_m = _Summen_fehlerstatus_von_analogem_repeater_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 68),
    _Summen_fehlerstatus_von_analogem_repeater_traps_m_Type()
)
summen_fehlerstatus_von_analogem_repeater_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summen_fehlerstatus_von_analogem_repeater_traps_m.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_traps_m_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_traps_m_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_traps_m = _Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 69),
    _Aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_traps_m_Type()
)
aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_traps_m.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_traps_m_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_traps_m_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_traps_m = _Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 70),
    _Aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_traps_m_Type()
)
aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_traps_m.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_traps_m_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_traps_m_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_traps_m = _Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 71),
    _Aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_traps_m_Type()
)
aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_traps_m.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_traps_m_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_traps_m_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_traps_m = _Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 72),
    _Aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_traps_m_Type()
)
aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_traps_m.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_traps_m_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_traps_m_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_traps_m = _Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 73),
    _Aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_traps_m_Type()
)
aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_traps_m.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_traps_m_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_traps_m_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_traps_m = _Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 74),
    _Aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_traps_m_Type()
)
aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_traps_m.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_traps_m_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_traps_m_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_traps_m = _Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 75),
    _Aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_traps_m_Type()
)
aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_traps_m.setStatus("current")
_Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_traps_m_Type = DisplayString
_Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_traps_m_Object = MibTableColumn
aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_traps_m = _Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 76),
    _Aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_traps_m_Type()
)
aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_traps_m.setStatus("current")
_Netzspannungsversorgung_von_tmoa_anlage_traps_m_Type = DisplayString
_Netzspannungsversorgung_von_tmoa_anlage_traps_m_Object = MibTableColumn
netzspannungsversorgung_von_tmoa_anlage_traps_m = _Netzspannungsversorgung_von_tmoa_anlage_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 77),
    _Netzspannungsversorgung_von_tmoa_anlage_traps_m_Type()
)
netzspannungsversorgung_von_tmoa_anlage_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzspannungsversorgung_von_tmoa_anlage_traps_m.setStatus("current")
_Netzspannungsversorgung_von_anbinderepeater_traps_m_Type = DisplayString
_Netzspannungsversorgung_von_anbinderepeater_traps_m_Object = MibTableColumn
netzspannungsversorgung_von_anbinderepeater_traps_m = _Netzspannungsversorgung_von_anbinderepeater_traps_m_Object(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 12, 1, 78),
    _Netzspannungsversorgung_von_anbinderepeater_traps_m_Type()
)
netzspannungsversorgung_von_anbinderepeater_traps_m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netzspannungsversorgung_von_anbinderepeater_traps_m.setStatus("current")
_Ak_gesamtsystem_i_ObjectIdentity = ObjectIdentity
ak_gesamtsystem_i = _Ak_gesamtsystem_i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 2)
)
_Ak_funk_i_ObjectIdentity = ObjectIdentity
ak_funk_i = _Ak_funk_i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 2)
)
_Ak_info_f_i_ObjectIdentity = ObjectIdentity
ak_info_f_i = _Ak_info_f_i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 2, 1)
)
_Ak_mgmt_f_i_ObjectIdentity = ObjectIdentity
ak_mgmt_f_i = _Ak_mgmt_f_i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 2, 2)
)
_Ak_divers_f_i_ObjectIdentity = ObjectIdentity
ak_divers_f_i = _Ak_divers_f_i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 2, 3)
)
_Ak_traps_f_i_ObjectIdentity = ObjectIdentity
ak_traps_f_i = _Ak_traps_f_i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 2, 4)
)
_Ak_custom_i_ObjectIdentity = ObjectIdentity
ak_custom_i = _Ak_custom_i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 3)
)
_Ak_info_c_i_ObjectIdentity = ObjectIdentity
ak_info_c_i = _Ak_info_c_i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 3, 1)
)
_Ak_mgmt_c_i_ObjectIdentity = ObjectIdentity
ak_mgmt_c_i = _Ak_mgmt_c_i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 3, 2)
)
_Ak_divers_c_i_ObjectIdentity = ObjectIdentity
ak_divers_c_i = _Ak_divers_c_i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 3, 3)
)
_Ak_traps_c_i_ObjectIdentity = ObjectIdentity
ak_traps_c_i = _Ak_traps_c_i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 3, 4)
)
_Ak_devices_ii_ObjectIdentity = ObjectIdentity
ak_devices_ii = _Ak_devices_ii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 2)
)
_Tbd_1_ObjectIdentity = ObjectIdentity
tbd_1 = _Tbd_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 2, 1)
)
_Ext_devices_i_ObjectIdentity = ObjectIdentity
ext_devices_i = _Ext_devices_i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 3)
)
_Tbd_2_ObjectIdentity = ObjectIdentity
tbd_2 = _Tbd_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 3, 1)
)
_Ext_devices_ii_ObjectIdentity = ObjectIdentity
ext_devices_ii = _Ext_devices_ii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 4)
)
_Tbd_3_ObjectIdentity = ObjectIdentity
tbd_3 = _Tbd_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 4, 1)
)
_Ak_mib_conformance_ObjectIdentity = ObjectIdentity
ak_mib_conformance = _Ak_mib_conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 5)
)
_Ak_mib_compliance_ObjectIdentity = ObjectIdentity
ak_mib_compliance = _Ak_mib_compliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49240, 1, 5, 1)
)

# Managed Objects groups


# Notification objects

fgb_id1_verbindungsstatus_s_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 12)
)
if mibBuilder.loadTexts:
    fgb_id1_verbindungsstatus_s_1.setStatus(
        "current"
    )

fgb_id2_verbindungsstatus_s_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 13)
)
if mibBuilder.loadTexts:
    fgb_id2_verbindungsstatus_s_1.setStatus(
        "current"
    )

fgb_id3_verbindungsstatus_s_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 14)
)
if mibBuilder.loadTexts:
    fgb_id3_verbindungsstatus_s_1.setStatus(
        "current"
    )

fgb_id4_verbindungsstatus_s_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 15)
)
if mibBuilder.loadTexts:
    fgb_id4_verbindungsstatus_s_1.setStatus(
        "current"
    )

fgb_id5_verbindungsstatus_s_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 16)
)
if mibBuilder.loadTexts:
    fgb_id5_verbindungsstatus_s_1.setStatus(
        "current"
    )

fgb_id6_verbindungsstatus_s_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 17)
)
if mibBuilder.loadTexts:
    fgb_id6_verbindungsstatus_s_1.setStatus(
        "current"
    )

fgb_id7_verbindungsstatus_s_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 18)
)
if mibBuilder.loadTexts:
    fgb_id7_verbindungsstatus_s_1.setStatus(
        "current"
    )

fgb_id8_verbindungsstatus_s_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 19)
)
if mibBuilder.loadTexts:
    fgb_id8_verbindungsstatus_s_1.setStatus(
        "current"
    )

fgb_id9_verbindungsstatus_s_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 20)
)
if mibBuilder.loadTexts:
    fgb_id9_verbindungsstatus_s_1.setStatus(
        "current"
    )

fgb_id10_verbindungsstatus_s_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 21)
)
if mibBuilder.loadTexts:
    fgb_id10_verbindungsstatus_s_1.setStatus(
        "current"
    )

fgb_id11_verbindungsstatus_s_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 22)
)
if mibBuilder.loadTexts:
    fgb_id11_verbindungsstatus_s_1.setStatus(
        "current"
    )

mod_bus_verbindungsstatus_s_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 128)
)
if mibBuilder.loadTexts:
    mod_bus_verbindungsstatus_s_1.setStatus(
        "current"
    )

fgb_bus_verbindungsstatus_s_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 129)
)
if mibBuilder.loadTexts:
    fgb_bus_verbindungsstatus_s_1.setStatus(
        "current"
    )

slave_bus_verbindungsstatus_s_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 130)
)
if mibBuilder.loadTexts:
    slave_bus_verbindungsstatus_s_1.setStatus(
        "current"
    )

gsm_modem_verbindungsstatus_s_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 131)
)
if mibBuilder.loadTexts:
    gsm_modem_verbindungsstatus_s_1.setStatus(
        "current"
    )

gsm_modem_sim_karte_s_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 132)
)
if mibBuilder.loadTexts:
    gsm_modem_sim_karte_s_1.setStatus(
        "current"
    )

gsm_modem_pin_nummer_s_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 133)
)
if mibBuilder.loadTexts:
    gsm_modem_pin_nummer_s_1.setStatus(
        "current"
    )

gsm_modem_provider_service_s_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 134)
)
if mibBuilder.loadTexts:
    gsm_modem_provider_service_s_1.setStatus(
        "current"
    )

gsm_modem_empfangspegel_s_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 135)
)
if mibBuilder.loadTexts:
    gsm_modem_empfangspegel_s_1.setStatus(
        "current"
    )

lte_router_verbindungsstatus_s_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 136)
)
if mibBuilder.loadTexts:
    lte_router_verbindungsstatus_s_1.setStatus(
        "current"
    )

lte_router_provider_service_s_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 137)
)
if mibBuilder.loadTexts:
    lte_router_provider_service_s_1.setStatus(
        "current"
    )

lte_router_empfangspegel_s_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 138)
)
if mibBuilder.loadTexts:
    lte_router_empfangspegel_s_1.setStatus(
        "current"
    )

antennenleitungsueberwachung_1_s_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 139)
)
if mibBuilder.loadTexts:
    antennenleitungsueberwachung_1_s_1.setStatus(
        "current"
    )

antennenleitungsueberwachung_2_s_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 140)
)
if mibBuilder.loadTexts:
    antennenleitungsueberwachung_2_s_1.setStatus(
        "current"
    )

antennenleitungseuberwachung_3_s_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 141)
)
if mibBuilder.loadTexts:
    antennenleitungseuberwachung_3_s_1.setStatus(
        "current"
    )

interne_temperaturuebwerwachung_s_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 142)
)
if mibBuilder.loadTexts:
    interne_temperaturuebwerwachung_s_1.setStatus(
        "current"
    )

stoerueberwachung_optisches_verteilsystem_1_s_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 143)
)
if mibBuilder.loadTexts:
    stoerueberwachung_optisches_verteilsystem_1_s_1.setStatus(
        "current"
    )

stoerueberwachung_optisches_verteilsystem_2_s_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 144)
)
if mibBuilder.loadTexts:
    stoerueberwachung_optisches_verteilsystem_2_s_1.setStatus(
        "current"
    )

lte_router_sim_karte_s_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 145)
)
if mibBuilder.loadTexts:
    lte_router_sim_karte_s_1.setStatus(
        "current"
    )

lte_router_pin_nummer_s_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 1, 146)
)
if mibBuilder.loadTexts:
    lte_router_pin_nummer_s_1.setStatus(
        "current"
    )

fgb_id1_verbindungsstatus_s_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 12)
)
if mibBuilder.loadTexts:
    fgb_id1_verbindungsstatus_s_2.setStatus(
        "current"
    )

fgb_id2_verbindungsstatus_s_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 13)
)
if mibBuilder.loadTexts:
    fgb_id2_verbindungsstatus_s_2.setStatus(
        "current"
    )

fgb_id3_verbindungsstatus_s_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 14)
)
if mibBuilder.loadTexts:
    fgb_id3_verbindungsstatus_s_2.setStatus(
        "current"
    )

fgb_id4_verbindungsstatus_s_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 15)
)
if mibBuilder.loadTexts:
    fgb_id4_verbindungsstatus_s_2.setStatus(
        "current"
    )

fgb_id5_verbindungsstatus_s_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 16)
)
if mibBuilder.loadTexts:
    fgb_id5_verbindungsstatus_s_2.setStatus(
        "current"
    )

fgb_id6_verbindungsstatus_s_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 17)
)
if mibBuilder.loadTexts:
    fgb_id6_verbindungsstatus_s_2.setStatus(
        "current"
    )

fgb_id7_verbindungsstatus_s_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 18)
)
if mibBuilder.loadTexts:
    fgb_id7_verbindungsstatus_s_2.setStatus(
        "current"
    )

fgb_id8_verbindungsstatus_s_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 19)
)
if mibBuilder.loadTexts:
    fgb_id8_verbindungsstatus_s_2.setStatus(
        "current"
    )

fgb_id9_verbindungsstatus_s_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 20)
)
if mibBuilder.loadTexts:
    fgb_id9_verbindungsstatus_s_2.setStatus(
        "current"
    )

fgb_id10_verbindungsstatus_s_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 21)
)
if mibBuilder.loadTexts:
    fgb_id10_verbindungsstatus_s_2.setStatus(
        "current"
    )

fgb_id11_verbindungsstatus_s_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 22)
)
if mibBuilder.loadTexts:
    fgb_id11_verbindungsstatus_s_2.setStatus(
        "current"
    )

mod_bus_verbindungsstatus_s_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 128)
)
if mibBuilder.loadTexts:
    mod_bus_verbindungsstatus_s_2.setStatus(
        "current"
    )

fgb_bus_verbindungsstatus_s_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 129)
)
if mibBuilder.loadTexts:
    fgb_bus_verbindungsstatus_s_2.setStatus(
        "current"
    )

slave_bus_verbindungsstatus_s_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 130)
)
if mibBuilder.loadTexts:
    slave_bus_verbindungsstatus_s_2.setStatus(
        "current"
    )

gsm_modem_verbindungsstatus_s_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 131)
)
if mibBuilder.loadTexts:
    gsm_modem_verbindungsstatus_s_2.setStatus(
        "current"
    )

gsm_modem_sim_karte_s_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 132)
)
if mibBuilder.loadTexts:
    gsm_modem_sim_karte_s_2.setStatus(
        "current"
    )

gsm_modem_pin_nummer_s_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 133)
)
if mibBuilder.loadTexts:
    gsm_modem_pin_nummer_s_2.setStatus(
        "current"
    )

gsm_modem_provider_service_s_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 134)
)
if mibBuilder.loadTexts:
    gsm_modem_provider_service_s_2.setStatus(
        "current"
    )

gsm_modem_empfangspegel_s_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 135)
)
if mibBuilder.loadTexts:
    gsm_modem_empfangspegel_s_2.setStatus(
        "current"
    )

lte_router_verbindungsstatus_s_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 136)
)
if mibBuilder.loadTexts:
    lte_router_verbindungsstatus_s_2.setStatus(
        "current"
    )

lte_router_provider_service_s_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 137)
)
if mibBuilder.loadTexts:
    lte_router_provider_service_s_2.setStatus(
        "current"
    )

lte_router_empfangspegel_s_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 138)
)
if mibBuilder.loadTexts:
    lte_router_empfangspegel_s_2.setStatus(
        "current"
    )

antennenleitungsueberwachung_1_s_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 139)
)
if mibBuilder.loadTexts:
    antennenleitungsueberwachung_1_s_2.setStatus(
        "current"
    )

antennenleitungsueberwachung_2_s_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 140)
)
if mibBuilder.loadTexts:
    antennenleitungsueberwachung_2_s_2.setStatus(
        "current"
    )

antennenleitungseuberwachung_3_s_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 141)
)
if mibBuilder.loadTexts:
    antennenleitungseuberwachung_3_s_2.setStatus(
        "current"
    )

interne_temperaturuebwerwachung_s_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 142)
)
if mibBuilder.loadTexts:
    interne_temperaturuebwerwachung_s_2.setStatus(
        "current"
    )

stoerueberwachung_optisches_verteilsystem_1_s_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 143)
)
if mibBuilder.loadTexts:
    stoerueberwachung_optisches_verteilsystem_1_s_2.setStatus(
        "current"
    )

stoerueberwachung_optisches_verteilsystem_2_s_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 144)
)
if mibBuilder.loadTexts:
    stoerueberwachung_optisches_verteilsystem_2_s_2.setStatus(
        "current"
    )

lte_router_sim_karte_s_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 145)
)
if mibBuilder.loadTexts:
    lte_router_sim_karte_s_2.setStatus(
        "current"
    )

lte_router_pin_nummer_s_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 2, 146)
)
if mibBuilder.loadTexts:
    lte_router_pin_nummer_s_2.setStatus(
        "current"
    )

fgb_id1_verbindungsstatus_s_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 12)
)
if mibBuilder.loadTexts:
    fgb_id1_verbindungsstatus_s_3.setStatus(
        "current"
    )

fgb_id2_verbindungsstatus_s_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 13)
)
if mibBuilder.loadTexts:
    fgb_id2_verbindungsstatus_s_3.setStatus(
        "current"
    )

fgb_id3_verbindungsstatus_s_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 14)
)
if mibBuilder.loadTexts:
    fgb_id3_verbindungsstatus_s_3.setStatus(
        "current"
    )

fgb_id4_verbindungsstatus_s_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 15)
)
if mibBuilder.loadTexts:
    fgb_id4_verbindungsstatus_s_3.setStatus(
        "current"
    )

fgb_id5_verbindungsstatus_s_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 16)
)
if mibBuilder.loadTexts:
    fgb_id5_verbindungsstatus_s_3.setStatus(
        "current"
    )

fgb_id6_verbindungsstatus_s_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 17)
)
if mibBuilder.loadTexts:
    fgb_id6_verbindungsstatus_s_3.setStatus(
        "current"
    )

fgb_id7_verbindungsstatus_s_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 18)
)
if mibBuilder.loadTexts:
    fgb_id7_verbindungsstatus_s_3.setStatus(
        "current"
    )

fgb_id8_verbindungsstatus_s_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 19)
)
if mibBuilder.loadTexts:
    fgb_id8_verbindungsstatus_s_3.setStatus(
        "current"
    )

fgb_id9_verbindungsstatus_s_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 20)
)
if mibBuilder.loadTexts:
    fgb_id9_verbindungsstatus_s_3.setStatus(
        "current"
    )

fgb_id10_verbindungsstatus_s_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 21)
)
if mibBuilder.loadTexts:
    fgb_id10_verbindungsstatus_s_3.setStatus(
        "current"
    )

fgb_id11_verbindungsstatus_s_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 22)
)
if mibBuilder.loadTexts:
    fgb_id11_verbindungsstatus_s_3.setStatus(
        "current"
    )

mod_bus_verbindungsstatus_s_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 128)
)
if mibBuilder.loadTexts:
    mod_bus_verbindungsstatus_s_3.setStatus(
        "current"
    )

fgb_bus_verbindungsstatus_s_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 129)
)
if mibBuilder.loadTexts:
    fgb_bus_verbindungsstatus_s_3.setStatus(
        "current"
    )

slave_bus_verbindungsstatus_s_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 130)
)
if mibBuilder.loadTexts:
    slave_bus_verbindungsstatus_s_3.setStatus(
        "current"
    )

gsm_modem_verbindungsstatus_s_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 131)
)
if mibBuilder.loadTexts:
    gsm_modem_verbindungsstatus_s_3.setStatus(
        "current"
    )

gsm_modem_sim_karte_s_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 132)
)
if mibBuilder.loadTexts:
    gsm_modem_sim_karte_s_3.setStatus(
        "current"
    )

gsm_modem_pin_nummer_s_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 133)
)
if mibBuilder.loadTexts:
    gsm_modem_pin_nummer_s_3.setStatus(
        "current"
    )

gsm_modem_provider_service_s_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 134)
)
if mibBuilder.loadTexts:
    gsm_modem_provider_service_s_3.setStatus(
        "current"
    )

gsm_modem_empfangspegel_s_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 135)
)
if mibBuilder.loadTexts:
    gsm_modem_empfangspegel_s_3.setStatus(
        "current"
    )

lte_router_verbindungsstatus_s_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 136)
)
if mibBuilder.loadTexts:
    lte_router_verbindungsstatus_s_3.setStatus(
        "current"
    )

lte_router_provider_service_s_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 137)
)
if mibBuilder.loadTexts:
    lte_router_provider_service_s_3.setStatus(
        "current"
    )

lte_router_empfangspegel_s_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 138)
)
if mibBuilder.loadTexts:
    lte_router_empfangspegel_s_3.setStatus(
        "current"
    )

antennenleitungsueberwachung_1_s_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 139)
)
if mibBuilder.loadTexts:
    antennenleitungsueberwachung_1_s_3.setStatus(
        "current"
    )

antennenleitungsueberwachung_2_s_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 140)
)
if mibBuilder.loadTexts:
    antennenleitungsueberwachung_2_s_3.setStatus(
        "current"
    )

antennenleitungseuberwachung_3_s_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 141)
)
if mibBuilder.loadTexts:
    antennenleitungseuberwachung_3_s_3.setStatus(
        "current"
    )

interne_temperaturuebwerwachung_s_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 142)
)
if mibBuilder.loadTexts:
    interne_temperaturuebwerwachung_s_3.setStatus(
        "current"
    )

stoerueberwachung_optisches_verteilsystem_1_s_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 143)
)
if mibBuilder.loadTexts:
    stoerueberwachung_optisches_verteilsystem_1_s_3.setStatus(
        "current"
    )

stoerueberwachung_optisches_verteilsystem_2_s_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 144)
)
if mibBuilder.loadTexts:
    stoerueberwachung_optisches_verteilsystem_2_s_3.setStatus(
        "current"
    )

lte_router_sim_karte_s_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 145)
)
if mibBuilder.loadTexts:
    lte_router_sim_karte_s_3.setStatus(
        "current"
    )

lte_router_pin_nummer_s_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 3, 146)
)
if mibBuilder.loadTexts:
    lte_router_pin_nummer_s_3.setStatus(
        "current"
    )

fgb_id1_verbindungsstatus_s_4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 12)
)
if mibBuilder.loadTexts:
    fgb_id1_verbindungsstatus_s_4.setStatus(
        "current"
    )

fgb_id2_verbindungsstatus_s_4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 13)
)
if mibBuilder.loadTexts:
    fgb_id2_verbindungsstatus_s_4.setStatus(
        "current"
    )

fgb_id3_verbindungsstatus_s_4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 14)
)
if mibBuilder.loadTexts:
    fgb_id3_verbindungsstatus_s_4.setStatus(
        "current"
    )

fgb_id4_verbindungsstatus_s_4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 15)
)
if mibBuilder.loadTexts:
    fgb_id4_verbindungsstatus_s_4.setStatus(
        "current"
    )

fgb_id5_verbindungsstatus_s_4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 16)
)
if mibBuilder.loadTexts:
    fgb_id5_verbindungsstatus_s_4.setStatus(
        "current"
    )

fgb_id6_verbindungsstatus_s_4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 17)
)
if mibBuilder.loadTexts:
    fgb_id6_verbindungsstatus_s_4.setStatus(
        "current"
    )

fgb_id7_verbindungsstatus_s_4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 18)
)
if mibBuilder.loadTexts:
    fgb_id7_verbindungsstatus_s_4.setStatus(
        "current"
    )

fgb_id8_verbindungsstatus_s_4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 19)
)
if mibBuilder.loadTexts:
    fgb_id8_verbindungsstatus_s_4.setStatus(
        "current"
    )

fgb_id9_verbindungsstatus_s_4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 20)
)
if mibBuilder.loadTexts:
    fgb_id9_verbindungsstatus_s_4.setStatus(
        "current"
    )

fgb_id10_verbindungsstatus_s_4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 21)
)
if mibBuilder.loadTexts:
    fgb_id10_verbindungsstatus_s_4.setStatus(
        "current"
    )

fgb_id11_verbindungsstatus_s_4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 22)
)
if mibBuilder.loadTexts:
    fgb_id11_verbindungsstatus_s_4.setStatus(
        "current"
    )

mod_bus_verbindungsstatus_s_4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 128)
)
if mibBuilder.loadTexts:
    mod_bus_verbindungsstatus_s_4.setStatus(
        "current"
    )

fgb_bus_verbindungsstatus_s_4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 129)
)
if mibBuilder.loadTexts:
    fgb_bus_verbindungsstatus_s_4.setStatus(
        "current"
    )

slave_bus_verbindungsstatus_s_4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 130)
)
if mibBuilder.loadTexts:
    slave_bus_verbindungsstatus_s_4.setStatus(
        "current"
    )

gsm_modem_verbindungsstatus_s_4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 131)
)
if mibBuilder.loadTexts:
    gsm_modem_verbindungsstatus_s_4.setStatus(
        "current"
    )

gsm_modem_sim_karte_s_4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 132)
)
if mibBuilder.loadTexts:
    gsm_modem_sim_karte_s_4.setStatus(
        "current"
    )

gsm_modem_pin_nummer_s_4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 133)
)
if mibBuilder.loadTexts:
    gsm_modem_pin_nummer_s_4.setStatus(
        "current"
    )

gsm_modem_provider_service_s_4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 134)
)
if mibBuilder.loadTexts:
    gsm_modem_provider_service_s_4.setStatus(
        "current"
    )

gsm_modem_empfangspegel_s_4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 135)
)
if mibBuilder.loadTexts:
    gsm_modem_empfangspegel_s_4.setStatus(
        "current"
    )

lte_router_verbindungsstatus_s_4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 136)
)
if mibBuilder.loadTexts:
    lte_router_verbindungsstatus_s_4.setStatus(
        "current"
    )

lte_router_provider_service_s_4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 137)
)
if mibBuilder.loadTexts:
    lte_router_provider_service_s_4.setStatus(
        "current"
    )

lte_router_empfangspegel_s_4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 138)
)
if mibBuilder.loadTexts:
    lte_router_empfangspegel_s_4.setStatus(
        "current"
    )

antennenleitungsueberwachung_1_s_4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 139)
)
if mibBuilder.loadTexts:
    antennenleitungsueberwachung_1_s_4.setStatus(
        "current"
    )

antennenleitungsueberwachung_2_s_4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 140)
)
if mibBuilder.loadTexts:
    antennenleitungsueberwachung_2_s_4.setStatus(
        "current"
    )

antennenleitungseuberwachung_3_s_4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 141)
)
if mibBuilder.loadTexts:
    antennenleitungseuberwachung_3_s_4.setStatus(
        "current"
    )

interne_temperaturuebwerwachung_s_4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 142)
)
if mibBuilder.loadTexts:
    interne_temperaturuebwerwachung_s_4.setStatus(
        "current"
    )

stoerueberwachung_optisches_verteilsystem_1_s_4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 143)
)
if mibBuilder.loadTexts:
    stoerueberwachung_optisches_verteilsystem_1_s_4.setStatus(
        "current"
    )

stoerueberwachung_optisches_verteilsystem_2_s_4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 144)
)
if mibBuilder.loadTexts:
    stoerueberwachung_optisches_verteilsystem_2_s_4.setStatus(
        "current"
    )

lte_router_sim_karte_s_4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 145)
)
if mibBuilder.loadTexts:
    lte_router_sim_karte_s_4.setStatus(
        "current"
    )

lte_router_pin_nummer_s_4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 4, 146)
)
if mibBuilder.loadTexts:
    lte_router_pin_nummer_s_4.setStatus(
        "current"
    )

fgb_id1_verbindungsstatus_s_5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 12)
)
if mibBuilder.loadTexts:
    fgb_id1_verbindungsstatus_s_5.setStatus(
        "current"
    )

fgb_id2_verbindungsstatus_s_5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 13)
)
if mibBuilder.loadTexts:
    fgb_id2_verbindungsstatus_s_5.setStatus(
        "current"
    )

fgb_id3_verbindungsstatus_s_5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 14)
)
if mibBuilder.loadTexts:
    fgb_id3_verbindungsstatus_s_5.setStatus(
        "current"
    )

fgb_id4_verbindungsstatus_s_5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 15)
)
if mibBuilder.loadTexts:
    fgb_id4_verbindungsstatus_s_5.setStatus(
        "current"
    )

fgb_id5_verbindungsstatus_s_5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 16)
)
if mibBuilder.loadTexts:
    fgb_id5_verbindungsstatus_s_5.setStatus(
        "current"
    )

fgb_id6_verbindungsstatus_s_5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 17)
)
if mibBuilder.loadTexts:
    fgb_id6_verbindungsstatus_s_5.setStatus(
        "current"
    )

fgb_id7_verbindungsstatus_s_5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 18)
)
if mibBuilder.loadTexts:
    fgb_id7_verbindungsstatus_s_5.setStatus(
        "current"
    )

fgb_id8_verbindungsstatus_s_5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 19)
)
if mibBuilder.loadTexts:
    fgb_id8_verbindungsstatus_s_5.setStatus(
        "current"
    )

fgb_id9_verbindungsstatus_s_5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 20)
)
if mibBuilder.loadTexts:
    fgb_id9_verbindungsstatus_s_5.setStatus(
        "current"
    )

fgb_id10_verbindungsstatus_s_5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 21)
)
if mibBuilder.loadTexts:
    fgb_id10_verbindungsstatus_s_5.setStatus(
        "current"
    )

fgb_id11_verbindungsstatus_s_5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 22)
)
if mibBuilder.loadTexts:
    fgb_id11_verbindungsstatus_s_5.setStatus(
        "current"
    )

mod_bus_verbindungsstatus_s_5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 128)
)
if mibBuilder.loadTexts:
    mod_bus_verbindungsstatus_s_5.setStatus(
        "current"
    )

fgb_bus_verbindungsstatus_s_5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 129)
)
if mibBuilder.loadTexts:
    fgb_bus_verbindungsstatus_s_5.setStatus(
        "current"
    )

slave_bus_verbindungsstatus_s_5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 130)
)
if mibBuilder.loadTexts:
    slave_bus_verbindungsstatus_s_5.setStatus(
        "current"
    )

gsm_modem_verbindungsstatus_s_5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 131)
)
if mibBuilder.loadTexts:
    gsm_modem_verbindungsstatus_s_5.setStatus(
        "current"
    )

gsm_modem_sim_karte_s_5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 132)
)
if mibBuilder.loadTexts:
    gsm_modem_sim_karte_s_5.setStatus(
        "current"
    )

gsm_modem_pin_nummer_s_5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 133)
)
if mibBuilder.loadTexts:
    gsm_modem_pin_nummer_s_5.setStatus(
        "current"
    )

gsm_modem_provider_service_s_5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 134)
)
if mibBuilder.loadTexts:
    gsm_modem_provider_service_s_5.setStatus(
        "current"
    )

gsm_modem_empfangspegel_s_5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 135)
)
if mibBuilder.loadTexts:
    gsm_modem_empfangspegel_s_5.setStatus(
        "current"
    )

lte_router_verbindungsstatus_s_5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 136)
)
if mibBuilder.loadTexts:
    lte_router_verbindungsstatus_s_5.setStatus(
        "current"
    )

lte_router_provider_service_s_5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 137)
)
if mibBuilder.loadTexts:
    lte_router_provider_service_s_5.setStatus(
        "current"
    )

lte_router_empfangspegel_s_5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 138)
)
if mibBuilder.loadTexts:
    lte_router_empfangspegel_s_5.setStatus(
        "current"
    )

antennenleitungsueberwachung_1_s_5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 139)
)
if mibBuilder.loadTexts:
    antennenleitungsueberwachung_1_s_5.setStatus(
        "current"
    )

antennenleitungsueberwachung_2_s_5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 140)
)
if mibBuilder.loadTexts:
    antennenleitungsueberwachung_2_s_5.setStatus(
        "current"
    )

antennenleitungseuberwachung_3_s_5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 141)
)
if mibBuilder.loadTexts:
    antennenleitungseuberwachung_3_s_5.setStatus(
        "current"
    )

interne_temperaturuebwerwachung_s_5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 142)
)
if mibBuilder.loadTexts:
    interne_temperaturuebwerwachung_s_5.setStatus(
        "current"
    )

stoerueberwachung_optisches_verteilsystem_1_s_5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 143)
)
if mibBuilder.loadTexts:
    stoerueberwachung_optisches_verteilsystem_1_s_5.setStatus(
        "current"
    )

stoerueberwachung_optisches_verteilsystem_2_s_5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 144)
)
if mibBuilder.loadTexts:
    stoerueberwachung_optisches_verteilsystem_2_s_5.setStatus(
        "current"
    )

lte_router_sim_karte_s_5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 145)
)
if mibBuilder.loadTexts:
    lte_router_sim_karte_s_5.setStatus(
        "current"
    )

lte_router_pin_nummer_s_5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 5, 146)
)
if mibBuilder.loadTexts:
    lte_router_pin_nummer_s_5.setStatus(
        "current"
    )

fgb_id1_verbindungsstatus_s_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 12)
)
if mibBuilder.loadTexts:
    fgb_id1_verbindungsstatus_s_6.setStatus(
        "current"
    )

fgb_id2_verbindungsstatus_s_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 13)
)
if mibBuilder.loadTexts:
    fgb_id2_verbindungsstatus_s_6.setStatus(
        "current"
    )

fgb_id3_verbindungsstatus_s_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 14)
)
if mibBuilder.loadTexts:
    fgb_id3_verbindungsstatus_s_6.setStatus(
        "current"
    )

fgb_id4_verbindungsstatus_s_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 15)
)
if mibBuilder.loadTexts:
    fgb_id4_verbindungsstatus_s_6.setStatus(
        "current"
    )

fgb_id5_verbindungsstatus_s_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 16)
)
if mibBuilder.loadTexts:
    fgb_id5_verbindungsstatus_s_6.setStatus(
        "current"
    )

fgb_id6_verbindungsstatus_s_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 17)
)
if mibBuilder.loadTexts:
    fgb_id6_verbindungsstatus_s_6.setStatus(
        "current"
    )

fgb_id7_verbindungsstatus_s_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 18)
)
if mibBuilder.loadTexts:
    fgb_id7_verbindungsstatus_s_6.setStatus(
        "current"
    )

fgb_id8_verbindungsstatus_s_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 19)
)
if mibBuilder.loadTexts:
    fgb_id8_verbindungsstatus_s_6.setStatus(
        "current"
    )

fgb_id9_verbindungsstatus_s_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 20)
)
if mibBuilder.loadTexts:
    fgb_id9_verbindungsstatus_s_6.setStatus(
        "current"
    )

fgb_id10_verbindungsstatus_s_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 21)
)
if mibBuilder.loadTexts:
    fgb_id10_verbindungsstatus_s_6.setStatus(
        "current"
    )

fgb_id11_verbindungsstatus_s_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 22)
)
if mibBuilder.loadTexts:
    fgb_id11_verbindungsstatus_s_6.setStatus(
        "current"
    )

mod_bus_verbindungsstatus_s_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 128)
)
if mibBuilder.loadTexts:
    mod_bus_verbindungsstatus_s_6.setStatus(
        "current"
    )

fgb_bus_verbindungsstatus_s_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 129)
)
if mibBuilder.loadTexts:
    fgb_bus_verbindungsstatus_s_6.setStatus(
        "current"
    )

slave_bus_verbindungsstatus_s_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 130)
)
if mibBuilder.loadTexts:
    slave_bus_verbindungsstatus_s_6.setStatus(
        "current"
    )

gsm_modem_verbindungsstatus_s_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 131)
)
if mibBuilder.loadTexts:
    gsm_modem_verbindungsstatus_s_6.setStatus(
        "current"
    )

gsm_modem_sim_karte_s_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 132)
)
if mibBuilder.loadTexts:
    gsm_modem_sim_karte_s_6.setStatus(
        "current"
    )

gsm_modem_pin_nummer_s_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 133)
)
if mibBuilder.loadTexts:
    gsm_modem_pin_nummer_s_6.setStatus(
        "current"
    )

gsm_modem_provider_service_s_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 134)
)
if mibBuilder.loadTexts:
    gsm_modem_provider_service_s_6.setStatus(
        "current"
    )

gsm_modem_empfangspegel_s_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 135)
)
if mibBuilder.loadTexts:
    gsm_modem_empfangspegel_s_6.setStatus(
        "current"
    )

lte_router_verbindungsstatus_s_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 136)
)
if mibBuilder.loadTexts:
    lte_router_verbindungsstatus_s_6.setStatus(
        "current"
    )

lte_router_provider_service_s_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 137)
)
if mibBuilder.loadTexts:
    lte_router_provider_service_s_6.setStatus(
        "current"
    )

lte_router_empfangspegel_s_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 138)
)
if mibBuilder.loadTexts:
    lte_router_empfangspegel_s_6.setStatus(
        "current"
    )

antennenleitungsueberwachung_1_s_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 139)
)
if mibBuilder.loadTexts:
    antennenleitungsueberwachung_1_s_6.setStatus(
        "current"
    )

antennenleitungsueberwachung_2_s_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 140)
)
if mibBuilder.loadTexts:
    antennenleitungsueberwachung_2_s_6.setStatus(
        "current"
    )

antennenleitungseuberwachung_3_s_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 141)
)
if mibBuilder.loadTexts:
    antennenleitungseuberwachung_3_s_6.setStatus(
        "current"
    )

interne_temperaturuebwerwachung_s_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 142)
)
if mibBuilder.loadTexts:
    interne_temperaturuebwerwachung_s_6.setStatus(
        "current"
    )

stoerueberwachung_optisches_verteilsystem_1_s_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 143)
)
if mibBuilder.loadTexts:
    stoerueberwachung_optisches_verteilsystem_1_s_6.setStatus(
        "current"
    )

stoerueberwachung_optisches_verteilsystem_2_s_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 144)
)
if mibBuilder.loadTexts:
    stoerueberwachung_optisches_verteilsystem_2_s_6.setStatus(
        "current"
    )

lte_router_sim_karte_s_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 145)
)
if mibBuilder.loadTexts:
    lte_router_sim_karte_s_6.setStatus(
        "current"
    )

lte_router_pin_nummer_s_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 6, 146)
)
if mibBuilder.loadTexts:
    lte_router_pin_nummer_s_6.setStatus(
        "current"
    )

fgb_id1_verbindungsstatus_s_7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 12)
)
if mibBuilder.loadTexts:
    fgb_id1_verbindungsstatus_s_7.setStatus(
        "current"
    )

fgb_id2_verbindungsstatus_s_7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 13)
)
if mibBuilder.loadTexts:
    fgb_id2_verbindungsstatus_s_7.setStatus(
        "current"
    )

fgb_id3_verbindungsstatus_s_7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 14)
)
if mibBuilder.loadTexts:
    fgb_id3_verbindungsstatus_s_7.setStatus(
        "current"
    )

fgb_id4_verbindungsstatus_s_7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 15)
)
if mibBuilder.loadTexts:
    fgb_id4_verbindungsstatus_s_7.setStatus(
        "current"
    )

fgb_id5_verbindungsstatus_s_7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 16)
)
if mibBuilder.loadTexts:
    fgb_id5_verbindungsstatus_s_7.setStatus(
        "current"
    )

fgb_id6_verbindungsstatus_s_7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 17)
)
if mibBuilder.loadTexts:
    fgb_id6_verbindungsstatus_s_7.setStatus(
        "current"
    )

fgb_id7_verbindungsstatus_s_7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 18)
)
if mibBuilder.loadTexts:
    fgb_id7_verbindungsstatus_s_7.setStatus(
        "current"
    )

fgb_id8_verbindungsstatus_s_7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 19)
)
if mibBuilder.loadTexts:
    fgb_id8_verbindungsstatus_s_7.setStatus(
        "current"
    )

fgb_id9_verbindungsstatus_s_7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 20)
)
if mibBuilder.loadTexts:
    fgb_id9_verbindungsstatus_s_7.setStatus(
        "current"
    )

fgb_id10_verbindungsstatus_s_7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 21)
)
if mibBuilder.loadTexts:
    fgb_id10_verbindungsstatus_s_7.setStatus(
        "current"
    )

fgb_id11_verbindungsstatus_s_7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 22)
)
if mibBuilder.loadTexts:
    fgb_id11_verbindungsstatus_s_7.setStatus(
        "current"
    )

mod_bus_verbindungsstatus_s_7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 128)
)
if mibBuilder.loadTexts:
    mod_bus_verbindungsstatus_s_7.setStatus(
        "current"
    )

fgb_bus_verbindungsstatus_s_7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 129)
)
if mibBuilder.loadTexts:
    fgb_bus_verbindungsstatus_s_7.setStatus(
        "current"
    )

slave_bus_verbindungsstatus_s_7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 130)
)
if mibBuilder.loadTexts:
    slave_bus_verbindungsstatus_s_7.setStatus(
        "current"
    )

gsm_modem_verbindungsstatus_s_7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 131)
)
if mibBuilder.loadTexts:
    gsm_modem_verbindungsstatus_s_7.setStatus(
        "current"
    )

gsm_modem_sim_karte_s_7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 132)
)
if mibBuilder.loadTexts:
    gsm_modem_sim_karte_s_7.setStatus(
        "current"
    )

gsm_modem_pin_nummer_s_7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 133)
)
if mibBuilder.loadTexts:
    gsm_modem_pin_nummer_s_7.setStatus(
        "current"
    )

gsm_modem_provider_service_s_7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 134)
)
if mibBuilder.loadTexts:
    gsm_modem_provider_service_s_7.setStatus(
        "current"
    )

gsm_modem_empfangspegel_s_7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 135)
)
if mibBuilder.loadTexts:
    gsm_modem_empfangspegel_s_7.setStatus(
        "current"
    )

lte_router_verbindungsstatus_s_7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 136)
)
if mibBuilder.loadTexts:
    lte_router_verbindungsstatus_s_7.setStatus(
        "current"
    )

lte_router_provider_service_s_7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 137)
)
if mibBuilder.loadTexts:
    lte_router_provider_service_s_7.setStatus(
        "current"
    )

lte_router_empfangspegel_s_7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 138)
)
if mibBuilder.loadTexts:
    lte_router_empfangspegel_s_7.setStatus(
        "current"
    )

antennenleitungsueberwachung_1_s_7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 139)
)
if mibBuilder.loadTexts:
    antennenleitungsueberwachung_1_s_7.setStatus(
        "current"
    )

antennenleitungsueberwachung_2_s_7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 140)
)
if mibBuilder.loadTexts:
    antennenleitungsueberwachung_2_s_7.setStatus(
        "current"
    )

antennenleitungseuberwachung_3_s_7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 141)
)
if mibBuilder.loadTexts:
    antennenleitungseuberwachung_3_s_7.setStatus(
        "current"
    )

interne_temperaturuebwerwachung_s_7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 142)
)
if mibBuilder.loadTexts:
    interne_temperaturuebwerwachung_s_7.setStatus(
        "current"
    )

stoerueberwachung_optisches_verteilsystem_1_s_7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 143)
)
if mibBuilder.loadTexts:
    stoerueberwachung_optisches_verteilsystem_1_s_7.setStatus(
        "current"
    )

stoerueberwachung_optisches_verteilsystem_2_s_7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 144)
)
if mibBuilder.loadTexts:
    stoerueberwachung_optisches_verteilsystem_2_s_7.setStatus(
        "current"
    )

lte_router_sim_karte_s_7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 145)
)
if mibBuilder.loadTexts:
    lte_router_sim_karte_s_7.setStatus(
        "current"
    )

lte_router_pin_nummer_s_7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 7, 146)
)
if mibBuilder.loadTexts:
    lte_router_pin_nummer_s_7.setStatus(
        "current"
    )

fgb_id1_verbindungsstatus_s_8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 12)
)
if mibBuilder.loadTexts:
    fgb_id1_verbindungsstatus_s_8.setStatus(
        "current"
    )

fgb_id2_verbindungsstatus_s_8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 13)
)
if mibBuilder.loadTexts:
    fgb_id2_verbindungsstatus_s_8.setStatus(
        "current"
    )

fgb_id3_verbindungsstatus_s_8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 14)
)
if mibBuilder.loadTexts:
    fgb_id3_verbindungsstatus_s_8.setStatus(
        "current"
    )

fgb_id4_verbindungsstatus_s_8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 15)
)
if mibBuilder.loadTexts:
    fgb_id4_verbindungsstatus_s_8.setStatus(
        "current"
    )

fgb_id5_verbindungsstatus_s_8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 16)
)
if mibBuilder.loadTexts:
    fgb_id5_verbindungsstatus_s_8.setStatus(
        "current"
    )

fgb_id6_verbindungsstatus_s_8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 17)
)
if mibBuilder.loadTexts:
    fgb_id6_verbindungsstatus_s_8.setStatus(
        "current"
    )

fgb_id7_verbindungsstatus_s_8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 18)
)
if mibBuilder.loadTexts:
    fgb_id7_verbindungsstatus_s_8.setStatus(
        "current"
    )

fgb_id8_verbindungsstatus_s_8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 19)
)
if mibBuilder.loadTexts:
    fgb_id8_verbindungsstatus_s_8.setStatus(
        "current"
    )

fgb_id9_verbindungsstatus_s_8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 20)
)
if mibBuilder.loadTexts:
    fgb_id9_verbindungsstatus_s_8.setStatus(
        "current"
    )

fgb_id10_verbindungsstatus_s_8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 21)
)
if mibBuilder.loadTexts:
    fgb_id10_verbindungsstatus_s_8.setStatus(
        "current"
    )

fgb_id11_verbindungsstatus_s_8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 22)
)
if mibBuilder.loadTexts:
    fgb_id11_verbindungsstatus_s_8.setStatus(
        "current"
    )

mod_bus_verbindungsstatus_s_8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 128)
)
if mibBuilder.loadTexts:
    mod_bus_verbindungsstatus_s_8.setStatus(
        "current"
    )

fgb_bus_verbindungsstatus_s_8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 129)
)
if mibBuilder.loadTexts:
    fgb_bus_verbindungsstatus_s_8.setStatus(
        "current"
    )

slave_bus_verbindungsstatus_s_8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 130)
)
if mibBuilder.loadTexts:
    slave_bus_verbindungsstatus_s_8.setStatus(
        "current"
    )

gsm_modem_verbindungsstatus_s_8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 131)
)
if mibBuilder.loadTexts:
    gsm_modem_verbindungsstatus_s_8.setStatus(
        "current"
    )

gsm_modem_sim_karte_s_8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 132)
)
if mibBuilder.loadTexts:
    gsm_modem_sim_karte_s_8.setStatus(
        "current"
    )

gsm_modem_pin_nummer_s_8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 133)
)
if mibBuilder.loadTexts:
    gsm_modem_pin_nummer_s_8.setStatus(
        "current"
    )

gsm_modem_provider_service_s_8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 134)
)
if mibBuilder.loadTexts:
    gsm_modem_provider_service_s_8.setStatus(
        "current"
    )

gsm_modem_empfangspegel_s_8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 135)
)
if mibBuilder.loadTexts:
    gsm_modem_empfangspegel_s_8.setStatus(
        "current"
    )

lte_router_verbindungsstatus_s_8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 136)
)
if mibBuilder.loadTexts:
    lte_router_verbindungsstatus_s_8.setStatus(
        "current"
    )

lte_router_provider_service_s_8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 137)
)
if mibBuilder.loadTexts:
    lte_router_provider_service_s_8.setStatus(
        "current"
    )

lte_router_empfangspegel_s_8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 138)
)
if mibBuilder.loadTexts:
    lte_router_empfangspegel_s_8.setStatus(
        "current"
    )

antennenleitungsueberwachung_1_s_8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 139)
)
if mibBuilder.loadTexts:
    antennenleitungsueberwachung_1_s_8.setStatus(
        "current"
    )

antennenleitungsueberwachung_2_s_8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 140)
)
if mibBuilder.loadTexts:
    antennenleitungsueberwachung_2_s_8.setStatus(
        "current"
    )

antennenleitungseuberwachung_3_s_8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 141)
)
if mibBuilder.loadTexts:
    antennenleitungseuberwachung_3_s_8.setStatus(
        "current"
    )

interne_temperaturuebwerwachung_s_8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 142)
)
if mibBuilder.loadTexts:
    interne_temperaturuebwerwachung_s_8.setStatus(
        "current"
    )

stoerueberwachung_optisches_verteilsystem_1_s_8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 143)
)
if mibBuilder.loadTexts:
    stoerueberwachung_optisches_verteilsystem_1_s_8.setStatus(
        "current"
    )

stoerueberwachung_optisches_verteilsystem_2_s_8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 144)
)
if mibBuilder.loadTexts:
    stoerueberwachung_optisches_verteilsystem_2_s_8.setStatus(
        "current"
    )

lte_router_sim_karte_s_8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 145)
)
if mibBuilder.loadTexts:
    lte_router_sim_karte_s_8.setStatus(
        "current"
    )

lte_router_pin_nummer_s_8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 8, 146)
)
if mibBuilder.loadTexts:
    lte_router_pin_nummer_s_8.setStatus(
        "current"
    )

fgb_id1_verbindungsstatus_s_9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 12)
)
if mibBuilder.loadTexts:
    fgb_id1_verbindungsstatus_s_9.setStatus(
        "current"
    )

fgb_id2_verbindungsstatus_s_9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 13)
)
if mibBuilder.loadTexts:
    fgb_id2_verbindungsstatus_s_9.setStatus(
        "current"
    )

fgb_id3_verbindungsstatus_s_9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 14)
)
if mibBuilder.loadTexts:
    fgb_id3_verbindungsstatus_s_9.setStatus(
        "current"
    )

fgb_id4_verbindungsstatus_s_9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 15)
)
if mibBuilder.loadTexts:
    fgb_id4_verbindungsstatus_s_9.setStatus(
        "current"
    )

fgb_id5_verbindungsstatus_s_9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 16)
)
if mibBuilder.loadTexts:
    fgb_id5_verbindungsstatus_s_9.setStatus(
        "current"
    )

fgb_id6_verbindungsstatus_s_9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 17)
)
if mibBuilder.loadTexts:
    fgb_id6_verbindungsstatus_s_9.setStatus(
        "current"
    )

fgb_id7_verbindungsstatus_s_9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 18)
)
if mibBuilder.loadTexts:
    fgb_id7_verbindungsstatus_s_9.setStatus(
        "current"
    )

fgb_id8_verbindungsstatus_s_9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 19)
)
if mibBuilder.loadTexts:
    fgb_id8_verbindungsstatus_s_9.setStatus(
        "current"
    )

fgb_id9_verbindungsstatus_s_9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 20)
)
if mibBuilder.loadTexts:
    fgb_id9_verbindungsstatus_s_9.setStatus(
        "current"
    )

fgb_id10_verbindungsstatus_s_9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 21)
)
if mibBuilder.loadTexts:
    fgb_id10_verbindungsstatus_s_9.setStatus(
        "current"
    )

fgb_id11_verbindungsstatus_s_9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 22)
)
if mibBuilder.loadTexts:
    fgb_id11_verbindungsstatus_s_9.setStatus(
        "current"
    )

mod_bus_verbindungsstatus_s_9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 128)
)
if mibBuilder.loadTexts:
    mod_bus_verbindungsstatus_s_9.setStatus(
        "current"
    )

fgb_bus_verbindungsstatus_s_9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 129)
)
if mibBuilder.loadTexts:
    fgb_bus_verbindungsstatus_s_9.setStatus(
        "current"
    )

slave_bus_verbindungsstatus_s_9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 130)
)
if mibBuilder.loadTexts:
    slave_bus_verbindungsstatus_s_9.setStatus(
        "current"
    )

gsm_modem_verbindungsstatus_s_9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 131)
)
if mibBuilder.loadTexts:
    gsm_modem_verbindungsstatus_s_9.setStatus(
        "current"
    )

gsm_modem_sim_karte_s_9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 132)
)
if mibBuilder.loadTexts:
    gsm_modem_sim_karte_s_9.setStatus(
        "current"
    )

gsm_modem_pin_nummer_s_9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 133)
)
if mibBuilder.loadTexts:
    gsm_modem_pin_nummer_s_9.setStatus(
        "current"
    )

gsm_modem_provider_service_s_9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 134)
)
if mibBuilder.loadTexts:
    gsm_modem_provider_service_s_9.setStatus(
        "current"
    )

gsm_modem_empfangspegel_s_9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 135)
)
if mibBuilder.loadTexts:
    gsm_modem_empfangspegel_s_9.setStatus(
        "current"
    )

lte_router_verbindungsstatus_s_9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 136)
)
if mibBuilder.loadTexts:
    lte_router_verbindungsstatus_s_9.setStatus(
        "current"
    )

lte_router_provider_service_s_9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 137)
)
if mibBuilder.loadTexts:
    lte_router_provider_service_s_9.setStatus(
        "current"
    )

lte_router_empfangspegel_s_9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 138)
)
if mibBuilder.loadTexts:
    lte_router_empfangspegel_s_9.setStatus(
        "current"
    )

antennenleitungsueberwachung_1_s_9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 139)
)
if mibBuilder.loadTexts:
    antennenleitungsueberwachung_1_s_9.setStatus(
        "current"
    )

antennenleitungsueberwachung_2_s_9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 140)
)
if mibBuilder.loadTexts:
    antennenleitungsueberwachung_2_s_9.setStatus(
        "current"
    )

antennenleitungseuberwachung_3_s_9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 141)
)
if mibBuilder.loadTexts:
    antennenleitungseuberwachung_3_s_9.setStatus(
        "current"
    )

interne_temperaturuebwerwachung_s_9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 142)
)
if mibBuilder.loadTexts:
    interne_temperaturuebwerwachung_s_9.setStatus(
        "current"
    )

stoerueberwachung_optisches_verteilsystem_1_s_9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 143)
)
if mibBuilder.loadTexts:
    stoerueberwachung_optisches_verteilsystem_1_s_9.setStatus(
        "current"
    )

stoerueberwachung_optisches_verteilsystem_2_s_9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 144)
)
if mibBuilder.loadTexts:
    stoerueberwachung_optisches_verteilsystem_2_s_9.setStatus(
        "current"
    )

lte_router_sim_karte_s_9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 145)
)
if mibBuilder.loadTexts:
    lte_router_sim_karte_s_9.setStatus(
        "current"
    )

lte_router_pin_nummer_s_9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 9, 146)
)
if mibBuilder.loadTexts:
    lte_router_pin_nummer_s_9.setStatus(
        "current"
    )

fgb_id1_verbindungsstatus_s_10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 12)
)
if mibBuilder.loadTexts:
    fgb_id1_verbindungsstatus_s_10.setStatus(
        "current"
    )

fgb_id2_verbindungsstatus_s_10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 13)
)
if mibBuilder.loadTexts:
    fgb_id2_verbindungsstatus_s_10.setStatus(
        "current"
    )

fgb_id3_verbindungsstatus_s_10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 14)
)
if mibBuilder.loadTexts:
    fgb_id3_verbindungsstatus_s_10.setStatus(
        "current"
    )

fgb_id4_verbindungsstatus_s_10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 15)
)
if mibBuilder.loadTexts:
    fgb_id4_verbindungsstatus_s_10.setStatus(
        "current"
    )

fgb_id5_verbindungsstatus_s_10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 16)
)
if mibBuilder.loadTexts:
    fgb_id5_verbindungsstatus_s_10.setStatus(
        "current"
    )

fgb_id6_verbindungsstatus_s_10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 17)
)
if mibBuilder.loadTexts:
    fgb_id6_verbindungsstatus_s_10.setStatus(
        "current"
    )

fgb_id7_verbindungsstatus_s_10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 18)
)
if mibBuilder.loadTexts:
    fgb_id7_verbindungsstatus_s_10.setStatus(
        "current"
    )

fgb_id8_verbindungsstatus_s_10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 19)
)
if mibBuilder.loadTexts:
    fgb_id8_verbindungsstatus_s_10.setStatus(
        "current"
    )

fgb_id9_verbindungsstatus_s_10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 20)
)
if mibBuilder.loadTexts:
    fgb_id9_verbindungsstatus_s_10.setStatus(
        "current"
    )

fgb_id10_verbindungsstatus_s_10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 21)
)
if mibBuilder.loadTexts:
    fgb_id10_verbindungsstatus_s_10.setStatus(
        "current"
    )

fgb_id11_verbindungsstatus_s_10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 22)
)
if mibBuilder.loadTexts:
    fgb_id11_verbindungsstatus_s_10.setStatus(
        "current"
    )

mod_bus_verbindungsstatus_s_10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 128)
)
if mibBuilder.loadTexts:
    mod_bus_verbindungsstatus_s_10.setStatus(
        "current"
    )

fgb_bus_verbindungsstatus_s_10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 129)
)
if mibBuilder.loadTexts:
    fgb_bus_verbindungsstatus_s_10.setStatus(
        "current"
    )

slave_bus_verbindungsstatus_s_10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 130)
)
if mibBuilder.loadTexts:
    slave_bus_verbindungsstatus_s_10.setStatus(
        "current"
    )

gsm_modem_verbindungsstatus_s_10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 131)
)
if mibBuilder.loadTexts:
    gsm_modem_verbindungsstatus_s_10.setStatus(
        "current"
    )

gsm_modem_sim_karte_s_10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 132)
)
if mibBuilder.loadTexts:
    gsm_modem_sim_karte_s_10.setStatus(
        "current"
    )

gsm_modem_pin_nummer_s_10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 133)
)
if mibBuilder.loadTexts:
    gsm_modem_pin_nummer_s_10.setStatus(
        "current"
    )

gsm_modem_provider_service_s_10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 134)
)
if mibBuilder.loadTexts:
    gsm_modem_provider_service_s_10.setStatus(
        "current"
    )

gsm_modem_empfangspegel_s_10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 135)
)
if mibBuilder.loadTexts:
    gsm_modem_empfangspegel_s_10.setStatus(
        "current"
    )

lte_router_verbindungsstatus_s_10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 136)
)
if mibBuilder.loadTexts:
    lte_router_verbindungsstatus_s_10.setStatus(
        "current"
    )

lte_router_provider_service_s_10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 137)
)
if mibBuilder.loadTexts:
    lte_router_provider_service_s_10.setStatus(
        "current"
    )

lte_router_empfangspegel_s_10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 138)
)
if mibBuilder.loadTexts:
    lte_router_empfangspegel_s_10.setStatus(
        "current"
    )

antennenleitungsueberwachung_1_s_10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 139)
)
if mibBuilder.loadTexts:
    antennenleitungsueberwachung_1_s_10.setStatus(
        "current"
    )

antennenleitungsueberwachung_2_s_10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 140)
)
if mibBuilder.loadTexts:
    antennenleitungsueberwachung_2_s_10.setStatus(
        "current"
    )

antennenleitungseuberwachung_3_s_10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 141)
)
if mibBuilder.loadTexts:
    antennenleitungseuberwachung_3_s_10.setStatus(
        "current"
    )

interne_temperaturuebwerwachung_s_10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 142)
)
if mibBuilder.loadTexts:
    interne_temperaturuebwerwachung_s_10.setStatus(
        "current"
    )

stoerueberwachung_optisches_verteilsystem_1_s_10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 143)
)
if mibBuilder.loadTexts:
    stoerueberwachung_optisches_verteilsystem_1_s_10.setStatus(
        "current"
    )

stoerueberwachung_optisches_verteilsystem_2_s_10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 144)
)
if mibBuilder.loadTexts:
    stoerueberwachung_optisches_verteilsystem_2_s_10.setStatus(
        "current"
    )

lte_router_sim_karte_s_10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 145)
)
if mibBuilder.loadTexts:
    lte_router_sim_karte_s_10.setStatus(
        "current"
    )

lte_router_pin_nummer_s_10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 10, 146)
)
if mibBuilder.loadTexts:
    lte_router_pin_nummer_s_10.setStatus(
        "current"
    )

fgb_id1_verbindungsstatus_s_11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 12)
)
if mibBuilder.loadTexts:
    fgb_id1_verbindungsstatus_s_11.setStatus(
        "current"
    )

fgb_id2_verbindungsstatus_s_11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 13)
)
if mibBuilder.loadTexts:
    fgb_id2_verbindungsstatus_s_11.setStatus(
        "current"
    )

fgb_id3_verbindungsstatus_s_11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 14)
)
if mibBuilder.loadTexts:
    fgb_id3_verbindungsstatus_s_11.setStatus(
        "current"
    )

fgb_id4_verbindungsstatus_s_11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 15)
)
if mibBuilder.loadTexts:
    fgb_id4_verbindungsstatus_s_11.setStatus(
        "current"
    )

fgb_id5_verbindungsstatus_s_11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 16)
)
if mibBuilder.loadTexts:
    fgb_id5_verbindungsstatus_s_11.setStatus(
        "current"
    )

fgb_id6_verbindungsstatus_s_11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 17)
)
if mibBuilder.loadTexts:
    fgb_id6_verbindungsstatus_s_11.setStatus(
        "current"
    )

fgb_id7_verbindungsstatus_s_11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 18)
)
if mibBuilder.loadTexts:
    fgb_id7_verbindungsstatus_s_11.setStatus(
        "current"
    )

fgb_id8_verbindungsstatus_s_11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 19)
)
if mibBuilder.loadTexts:
    fgb_id8_verbindungsstatus_s_11.setStatus(
        "current"
    )

fgb_id9_verbindungsstatus_s_11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 20)
)
if mibBuilder.loadTexts:
    fgb_id9_verbindungsstatus_s_11.setStatus(
        "current"
    )

fgb_id10_verbindungsstatus_s_11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 21)
)
if mibBuilder.loadTexts:
    fgb_id10_verbindungsstatus_s_11.setStatus(
        "current"
    )

fgb_id11_verbindungsstatus_s_11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 22)
)
if mibBuilder.loadTexts:
    fgb_id11_verbindungsstatus_s_11.setStatus(
        "current"
    )

mod_bus_verbindungsstatus_s_11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 128)
)
if mibBuilder.loadTexts:
    mod_bus_verbindungsstatus_s_11.setStatus(
        "current"
    )

fgb_bus_verbindungsstatus_s_11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 129)
)
if mibBuilder.loadTexts:
    fgb_bus_verbindungsstatus_s_11.setStatus(
        "current"
    )

slave_bus_verbindungsstatus_s_11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 130)
)
if mibBuilder.loadTexts:
    slave_bus_verbindungsstatus_s_11.setStatus(
        "current"
    )

gsm_modem_verbindungsstatus_s_11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 131)
)
if mibBuilder.loadTexts:
    gsm_modem_verbindungsstatus_s_11.setStatus(
        "current"
    )

gsm_modem_sim_karte_s_11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 132)
)
if mibBuilder.loadTexts:
    gsm_modem_sim_karte_s_11.setStatus(
        "current"
    )

gsm_modem_pin_nummer_s_11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 133)
)
if mibBuilder.loadTexts:
    gsm_modem_pin_nummer_s_11.setStatus(
        "current"
    )

gsm_modem_provider_service_s_11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 134)
)
if mibBuilder.loadTexts:
    gsm_modem_provider_service_s_11.setStatus(
        "current"
    )

gsm_modem_empfangspegel_s_11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 135)
)
if mibBuilder.loadTexts:
    gsm_modem_empfangspegel_s_11.setStatus(
        "current"
    )

lte_router_verbindungsstatus_s_11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 136)
)
if mibBuilder.loadTexts:
    lte_router_verbindungsstatus_s_11.setStatus(
        "current"
    )

lte_router_provider_service_s_11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 137)
)
if mibBuilder.loadTexts:
    lte_router_provider_service_s_11.setStatus(
        "current"
    )

lte_router_empfangspegel_s_11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 138)
)
if mibBuilder.loadTexts:
    lte_router_empfangspegel_s_11.setStatus(
        "current"
    )

antennenleitungsueberwachung_1_s_11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 139)
)
if mibBuilder.loadTexts:
    antennenleitungsueberwachung_1_s_11.setStatus(
        "current"
    )

antennenleitungsueberwachung_2_s_11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 140)
)
if mibBuilder.loadTexts:
    antennenleitungsueberwachung_2_s_11.setStatus(
        "current"
    )

antennenleitungseuberwachung_3_s_11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 141)
)
if mibBuilder.loadTexts:
    antennenleitungseuberwachung_3_s_11.setStatus(
        "current"
    )

interne_temperaturuebwerwachung_s_11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 142)
)
if mibBuilder.loadTexts:
    interne_temperaturuebwerwachung_s_11.setStatus(
        "current"
    )

stoerueberwachung_optisches_verteilsystem_1_s_11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 143)
)
if mibBuilder.loadTexts:
    stoerueberwachung_optisches_verteilsystem_1_s_11.setStatus(
        "current"
    )

stoerueberwachung_optisches_verteilsystem_2_s_11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 144)
)
if mibBuilder.loadTexts:
    stoerueberwachung_optisches_verteilsystem_2_s_11.setStatus(
        "current"
    )

lte_router_sim_karte_s_11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 145)
)
if mibBuilder.loadTexts:
    lte_router_sim_karte_s_11.setStatus(
        "current"
    )

lte_router_pin_nummer_s_11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 11, 146)
)
if mibBuilder.loadTexts:
    lte_router_pin_nummer_s_11.setStatus(
        "current"
    )

fgb_id1_verbindungsstatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 23)
)
if mibBuilder.loadTexts:
    fgb_id1_verbindungsstatus.setStatus(
        "current"
    )

fgb_id2_verbindungsstatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 24)
)
if mibBuilder.loadTexts:
    fgb_id2_verbindungsstatus.setStatus(
        "current"
    )

fgb_id3_verbindungsstatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 25)
)
if mibBuilder.loadTexts:
    fgb_id3_verbindungsstatus.setStatus(
        "current"
    )

fgb_id4_verbindungsstatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 26)
)
if mibBuilder.loadTexts:
    fgb_id4_verbindungsstatus.setStatus(
        "current"
    )

fgb_id5_verbindungsstatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 27)
)
if mibBuilder.loadTexts:
    fgb_id5_verbindungsstatus.setStatus(
        "current"
    )

fgb_id6_verbindungsstatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 28)
)
if mibBuilder.loadTexts:
    fgb_id6_verbindungsstatus.setStatus(
        "current"
    )

fgb_id7_verbindungsstatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 29)
)
if mibBuilder.loadTexts:
    fgb_id7_verbindungsstatus.setStatus(
        "current"
    )

fgb_id8_verbindungsstatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 30)
)
if mibBuilder.loadTexts:
    fgb_id8_verbindungsstatus.setStatus(
        "current"
    )

fgb_id9_verbindungsstatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 31)
)
if mibBuilder.loadTexts:
    fgb_id9_verbindungsstatus.setStatus(
        "current"
    )

fgb_id10_verbindungsstatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 32)
)
if mibBuilder.loadTexts:
    fgb_id10_verbindungsstatus.setStatus(
        "current"
    )

fgb_id11_verbindungsstatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 33)
)
if mibBuilder.loadTexts:
    fgb_id11_verbindungsstatus.setStatus(
        "current"
    )

mod_bus_verbindungsstatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 128)
)
if mibBuilder.loadTexts:
    mod_bus_verbindungsstatus.setStatus(
        "current"
    )

fgb_bus_verbindungsstatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 129)
)
if mibBuilder.loadTexts:
    fgb_bus_verbindungsstatus.setStatus(
        "current"
    )

slave_bus_verbindungsstatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 130)
)
if mibBuilder.loadTexts:
    slave_bus_verbindungsstatus.setStatus(
        "current"
    )

gsm_modem_verbindungsstatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 131)
)
if mibBuilder.loadTexts:
    gsm_modem_verbindungsstatus.setStatus(
        "current"
    )

gsm_modem_sim_karte = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 132)
)
if mibBuilder.loadTexts:
    gsm_modem_sim_karte.setStatus(
        "current"
    )

gsm_modem_pin_nummer = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 133)
)
if mibBuilder.loadTexts:
    gsm_modem_pin_nummer.setStatus(
        "current"
    )

gsm_modem_provider_service = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 134)
)
if mibBuilder.loadTexts:
    gsm_modem_provider_service.setStatus(
        "current"
    )

gsm_modem_empfangspegel = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 135)
)
if mibBuilder.loadTexts:
    gsm_modem_empfangspegel.setStatus(
        "current"
    )

lte_router_verbindungsstatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 136)
)
if mibBuilder.loadTexts:
    lte_router_verbindungsstatus.setStatus(
        "current"
    )

lte_router_provider_service = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 137)
)
if mibBuilder.loadTexts:
    lte_router_provider_service.setStatus(
        "current"
    )

lte_router_empfangspegel = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 138)
)
if mibBuilder.loadTexts:
    lte_router_empfangspegel.setStatus(
        "current"
    )

antennenleitungsueberwachung_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 139)
)
if mibBuilder.loadTexts:
    antennenleitungsueberwachung_1.setStatus(
        "current"
    )

antennenleitungsueberwachung_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 140)
)
if mibBuilder.loadTexts:
    antennenleitungsueberwachung_2.setStatus(
        "current"
    )

antennenleitungseuberwachung_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 141)
)
if mibBuilder.loadTexts:
    antennenleitungseuberwachung_3.setStatus(
        "current"
    )

interne_temperaturuebwerwachung = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 142)
)
if mibBuilder.loadTexts:
    interne_temperaturuebwerwachung.setStatus(
        "current"
    )

stoerueberwachung_optisches_verteilsystem_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 143)
)
if mibBuilder.loadTexts:
    stoerueberwachung_optisches_verteilsystem_1.setStatus(
        "current"
    )

stoerueberwachung_optisches_verteilsystem_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 144)
)
if mibBuilder.loadTexts:
    stoerueberwachung_optisches_verteilsystem_2.setStatus(
        "current"
    )

lte_router_sim_karte = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 145)
)
if mibBuilder.loadTexts:
    lte_router_sim_karte.setStatus(
        "current"
    )

lte_router_pin_nummer = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 1, 146)
)
if mibBuilder.loadTexts:
    lte_router_pin_nummer.setStatus(
        "current"
    )

gesamtsystem_antennenleitung_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    gesamtsystem_antennenleitung_1.setStatus(
        "current"
    )

gesamtsystem_antennenleitung_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    gesamtsystem_antennenleitung_2.setStatus(
        "current"
    )

gesamtsystem_antennenleitung_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 2, 3)
)
if mibBuilder.loadTexts:
    gesamtsystem_antennenleitung_3.setStatus(
        "current"
    )

gesamtsystem_temperaturfehler = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 2, 4)
)
if mibBuilder.loadTexts:
    gesamtsystem_temperaturfehler.setStatus(
        "current"
    )

gesamtsystem_gsmfehler = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 2, 5)
)
if mibBuilder.loadTexts:
    gesamtsystem_gsmfehler.setStatus(
        "current"
    )

gesamtsystem_ltefehler = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 2, 6)
)
if mibBuilder.loadTexts:
    gesamtsystem_ltefehler.setStatus(
        "current"
    )

gesamtsystem_fgb_verbindungs_fehler = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 2, 7)
)
if mibBuilder.loadTexts:
    gesamtsystem_fgb_verbindungs_fehler.setStatus(
        "current"
    )

gesamtsystem_fgbfehler = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 2, 8)
)
if mibBuilder.loadTexts:
    gesamtsystem_fgbfehler.setStatus(
        "current"
    )

gesamtsystem_slave_verbindungs_fehler = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 2, 9)
)
if mibBuilder.loadTexts:
    gesamtsystem_slave_verbindungs_fehler.setStatus(
        "current"
    )

gesamtsystem_slave_fehler = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 2, 10)
)
if mibBuilder.loadTexts:
    gesamtsystem_slave_fehler.setStatus(
        "current"
    )

gesamtsystem_modul_verbindungs_fehler = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 2, 11)
)
if mibBuilder.loadTexts:
    gesamtsystem_modul_verbindungs_fehler.setStatus(
        "current"
    )

gesamtsystem_Modul_fehler = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 2, 12)
)
if mibBuilder.loadTexts:
    gesamtsystem_Modul_fehler.setStatus(
        "current"
    )

gesamtsystem_ov1_fehler = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 2, 13)
)
if mibBuilder.loadTexts:
    gesamtsystem_ov1_fehler.setStatus(
        "current"
    )

gesamtsystem_ov2_fehler = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 2, 14)
)
if mibBuilder.loadTexts:
    gesamtsystem_ov2_fehler.setStatus(
        "current"
    )

gesamtsystem_option_1_fehler = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 2, 15)
)
if mibBuilder.loadTexts:
    gesamtsystem_option_1_fehler.setStatus(
        "current"
    )

gesamtsystem_option_2_fehler = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 2, 16)
)
if mibBuilder.loadTexts:
    gesamtsystem_option_2_fehler.setStatus(
        "current"
    )

gesamtsystem_bma_in = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 2, 17)
)
if mibBuilder.loadTexts:
    gesamtsystem_bma_in.setStatus(
        "current"
    )

gesamtsystem_modul_summenfehler = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 2, 18)
)
if mibBuilder.loadTexts:
    gesamtsystem_modul_summenfehler.setStatus(
        "current"
    )

gesamtsystem_modul_netzfehler = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 2, 19)
)
if mibBuilder.loadTexts:
    gesamtsystem_modul_netzfehler.setStatus(
        "current"
    )

gesamtsystem_usvfehler = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 2, 20)
)
if mibBuilder.loadTexts:
    gesamtsystem_usvfehler.setStatus(
        "current"
    )

gesamtsystem_akkufehler = NotificationType(
    (1, 3, 6, 1, 4, 1, 49240, 1, 1, 1, 4, 2, 21)
)
if mibBuilder.loadTexts:
    gesamtsystem_akkufehler.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AK-FUNKTECHNIK-MIB",
    **{"ak-funktechnik": ak_funktechnik,
       "ak-mib-i": ak_mib_i,
       "ak-devices-i": ak_devices_i,
       "ak-ofu-i": ak_ofu_i,
       "ak-info-i": ak_info_i,
       "ak-device-name": ak_device_name,
       "ak-custom-name": ak_custom_name,
       "ak-location-name": ak_location_name,
       "ak-master-slave-parameter": ak_master_slave_parameter,
       "ak-antennenkabel-ueberwachung-1": ak_antennenkabel_ueberwachung_1,
       "ak-antennenkabel-ueberwachung-2": ak_antennenkabel_ueberwachung_2,
       "ak-antennenkabel-ueberwachung-3": ak_antennenkabel_ueberwachung_3,
       "ak-schranktemperatur-ueberwachung": ak_schranktemperatur_ueberwachung,
       "ak-datum-zeit": ak_datum_zeit,
       "ak-status-informationen": ak_status_informationen,
       "info-interne-master-module": info_interne_master_module,
       "masterTable-basisinfo": masterTable_basisinfo,
       "modulEntry-basis-master": modulEntry_basis_master,
       "modulindex-master": modulindex_master,
       "ska-fehlerstat-master": ska_fehlerstat_master,
       "ska-betriebsstat-master": ska_betriebsstat_master,
       "ska-betriebsstat-quelle-master": ska_betriebsstat_quelle_master,
       "ska-autom-abschaltzeit-master": ska_autom_abschaltzeit_master,
       "skb-fehlerstat-master": skb_fehlerstat_master,
       "skb-betriebsstat-master": skb_betriebsstat_master,
       "skb-betriebsstat-quelle-master": skb_betriebsstat_quelle_master,
       "skb-autom-abschaltzeit-master": skb_autom_abschaltzeit_master,
       "skc-fehlerstat-master": skc_fehlerstat_master,
       "skc-betriebsstat-master": skc_betriebsstat_master,
       "skc-betriebsstat-quelle-master": skc_betriebsstat_quelle_master,
       "skc-autom-abschaltzeit-master": skc_autom_abschaltzeit_master,
       "fehlerausgang-rel-1-master": fehlerausgang_rel_1_master,
       "fehlerausgang-rel-2-master": fehlerausgang_rel_2_master,
       "steuerausgang-x1000-master": steuerausgang_x1000_master,
       "steuerausgang-x1002-master": steuerausgang_x1002_master,
       "steuerausgang-x2001-8-master": steuerausgang_x2001_8_master,
       "steuerausgang-x2001-10-master": steuerausgang_x2001_10_master,
       "serviceschalter-master": serviceschalter_master,
       "steuereingang-bma-master": steuereingang_bma_master,
       "steuereingang-opt1-master": steuereingang_opt1_master,
       "steuereingang-opt2-master": steuereingang_opt2_master,
       "antennenleitungs-ueberwachung-1-master": antennenleitungs_ueberwachung_1_master,
       "antennenleitungs-ueberwachung-2-master": antennenleitungs_ueberwachung_2_master,
       "antennenleitungs-ueberwachung-3-master": antennenleitungs_ueberwachung_3_master,
       "interne-temp-ueberwachung-master": interne_temp_ueberwachung_master,
       "ueberwachung-ov-1-master": ueberwachung_ov_1_master,
       "ueberwachung-ov-2-master": ueberwachung_ov_2_master,
       "zustand-gesamtsystem-master": zustand_gesamtsystem_master,
       "zustand-netzversorgung-master": zustand_netzversorgung_master,
       "zustand-fernwirkmodule-master": zustand_fernwirkmodule_master,
       "zustand-ofu-modulbaugruppen-master": zustand_ofu_modulbaugruppen_master,
       "zustand-ofu-fgb-master": zustand_ofu_fgb_master,
       "zustand-ofu-slaves-master": zustand_ofu_slaves_master,
       "modulTable-mod-m-1": modulTable_mod_m_1,
       "modulEntry-mod-m-1": modulEntry_mod_m_1,
       "modulindex-mod-m-1": modulindex_mod_m_1,
       "modul-typ-mod-m-1": modul_typ_mod_m_1,
       "seriennummer-mod-m-1": seriennummer_mod_m_1,
       "firmware-version-mod-m-1": firmware_version_mod_m_1,
       "hardware-zustand-mod-m-1": hardware_zustand_mod_m_1,
       "betriebs-status-mod-m-1": betriebs_status_mod_m_1,
       "modul-var-para-1-mod-m-1": modul_var_para_1_mod_m_1,
       "modul-var-para-2-mod-m-1": modul_var_para_2_mod_m_1,
       "modul-var-para-3-mod-m-1": modul_var_para_3_mod_m_1,
       "modul-var-para-4-mod-m-1": modul_var_para_4_mod_m_1,
       "modul-var-para-5-mod-m-1": modul_var_para_5_mod_m_1,
       "modul-var-para-6-mod-m-1": modul_var_para_6_mod_m_1,
       "modul-var-para-7-mod-m-1": modul_var_para_7_mod_m_1,
       "modul-var-para-8-mod-m-1": modul_var_para_8_mod_m_1,
       "modul-var-para-9-mod-m-1": modul_var_para_9_mod_m_1,
       "modul-var-para-10-mod-m-1": modul_var_para_10_mod_m_1,
       "modul-var-para-11-mod-m-1": modul_var_para_11_mod_m_1,
       "modul-var-para-12-mod-m-1": modul_var_para_12_mod_m_1,
       "modul-var-para-13-mod-m-1": modul_var_para_13_mod_m_1,
       "modul-var-para-14-mod-m-1": modul_var_para_14_mod_m_1,
       "modul-var-para-15-mod-m-1": modul_var_para_15_mod_m_1,
       "modul-var-para-16-mod-m-1": modul_var_para_16_mod_m_1,
       "modul-var-para-17-mod-m-1": modul_var_para_17_mod_m_1,
       "modul-var-para-18-mod-m-1": modul_var_para_18_mod_m_1,
       "modul-var-para-19-mod-m-1": modul_var_para_19_mod_m_1,
       "info-externe-slave-module": info_externe_slave_module,
       "slaveTable-basisinfo": slaveTable_basisinfo,
       "modulEntry-basis-slave-1": modulEntry_basis_slave_1,
       "modulindex-basis-slave-1": modulindex_basis_slave_1,
       "ska-fehlerstat-basis-slave-1": ska_fehlerstat_basis_slave_1,
       "ska-betriebsstat-basis-slave-1": ska_betriebsstat_basis_slave_1,
       "ska-betriebsstat-quelle-basis-slave-1": ska_betriebsstat_quelle_basis_slave_1,
       "ska-autom-abschaltzeit-basis-slave-1": ska_autom_abschaltzeit_basis_slave_1,
       "skb-fehlerstat-basis-slave-1": skb_fehlerstat_basis_slave_1,
       "skb-betriebsstat-basis-slave-1": skb_betriebsstat_basis_slave_1,
       "skb-betriebsstat-quelle-basis-slave-1": skb_betriebsstat_quelle_basis_slave_1,
       "skb-autom-abschaltzeit-basis-slave-1": skb_autom_abschaltzeit_basis_slave_1,
       "skc-fehlerstat-basis-slave-1": skc_fehlerstat_basis_slave_1,
       "skc-betriebsstat-basis-slave-1": skc_betriebsstat_basis_slave_1,
       "skc-betriebsstat-quelle-basis-slave-1": skc_betriebsstat_quelle_basis_slave_1,
       "skc-autom-abschaltzeit-basis-slave-1": skc_autom_abschaltzeit_basis_slave_1,
       "fehlerausgang-rel-1-basis-slave-1": fehlerausgang_rel_1_basis_slave_1,
       "fehlerausgang-rel-2-basis-slave-1": fehlerausgang_rel_2_basis_slave_1,
       "steuerausgang-x1000-basis-slave-1": steuerausgang_x1000_basis_slave_1,
       "steuerausgang-x1002-basis-slave-1": steuerausgang_x1002_basis_slave_1,
       "steuerausgang-x2001-8-basis-slave-1": steuerausgang_x2001_8_basis_slave_1,
       "steuerausgang-x2001-10-basis-slave-1": steuerausgang_x2001_10_basis_slave_1,
       "serviceschalter-basis-slave-1": serviceschalter_basis_slave_1,
       "steuereingang-bma-basis-slave-1": steuereingang_bma_basis_slave_1,
       "steuereingang-opt1-basis-slave-1": steuereingang_opt1_basis_slave_1,
       "steuereingang-opt2-basis-slave-1": steuereingang_opt2_basis_slave_1,
       "antennenleitungs-ueberwachung-1-basis-slave-1": antennenleitungs_ueberwachung_1_basis_slave_1,
       "antennenleitungs-ueberwachung-2-basis-slave-1": antennenleitungs_ueberwachung_2_basis_slave_1,
       "antennenleitungs-ueberwachung-3-basis-slave-1": antennenleitungs_ueberwachung_3_basis_slave_1,
       "interne-temp-ueberwachung-basis-slave-1": interne_temp_ueberwachung_basis_slave_1,
       "ueberwachung-ov-1-basis-slave-1": ueberwachung_ov_1_basis_slave_1,
       "ueberwachung-ov-2-basis-slave-1": ueberwachung_ov_2_basis_slave_1,
       "zustand-gesamtsystem-basis-slave-1": zustand_gesamtsystem_basis_slave_1,
       "zustand-netzversorgung-basis-slave-1": zustand_netzversorgung_basis_slave_1,
       "zustand-fernwirkmodule-basis-slave-1": zustand_fernwirkmodule_basis_slave_1,
       "zustand-ofu-modulbaugruppen-basis-slave-1": zustand_ofu_modulbaugruppen_basis_slave_1,
       "zustand-ofu-fgb-basis-slave-1": zustand_ofu_fgb_basis_slave_1,
       "zustand-ofu-slaves-basis-slave-1": zustand_ofu_slaves_basis_slave_1,
       "modulTable-mod-s-1": modulTable_mod_s_1,
       "modulEntry-mod-s-1": modulEntry_mod_s_1,
       "modulindex-mod-s-1": modulindex_mod_s_1,
       "modul-typ-mod-s-1": modul_typ_mod_s_1,
       "seriennummer-mod-s-1": seriennummer_mod_s_1,
       "firmware-version-mod-s-1": firmware_version_mod_s_1,
       "hardware-zustand-mod-s-1": hardware_zustand_mod_s_1,
       "betriebs-status-mod-s-1": betriebs_status_mod_s_1,
       "modul-var-para-1-mod-s-1": modul_var_para_1_mod_s_1,
       "modul-var-para-2-mod-s-1": modul_var_para_2_mod_s_1,
       "modul-var-para-3-mod-s-1": modul_var_para_3_mod_s_1,
       "modul-var-para-4-mod-s-1": modul_var_para_4_mod_s_1,
       "modul-var-para-5-mod-s-1": modul_var_para_5_mod_s_1,
       "modul-var-para-6-mod-s-1": modul_var_para_6_mod_s_1,
       "modul-var-para-7-mod-s-1": modul_var_para_7_mod_s_1,
       "modul-var-para-8-mod-s-1": modul_var_para_8_mod_s_1,
       "modul-var-para-9-mod-s-1": modul_var_para_9_mod_s_1,
       "modul-var-para-10-mod-s-1": modul_var_para_10_mod_s_1,
       "modul-var-para-11-mod-s-1": modul_var_para_11_mod_s_1,
       "modul-var-para-12-mod-s-1": modul_var_para_12_mod_s_1,
       "modul-var-para-13-mod-s-1": modul_var_para_13_mod_s_1,
       "modul-var-para-14-mod-s-1": modul_var_para_14_mod_s_1,
       "modul-var-para-15-mod-s-1": modul_var_para_15_mod_s_1,
       "modul-var-para-16-mod-s-1": modul_var_para_16_mod_s_1,
       "modul-var-para-17-mod-s-1": modul_var_para_17_mod_s_1,
       "modul-var-para-18-mod-s-1": modul_var_para_18_mod_s_1,
       "modul-var-para-19-mod-s-1": modul_var_para_19_mod_s_1,
       "modulTable-mod-s-2": modulTable_mod_s_2,
       "modulEntry-mod-s-2": modulEntry_mod_s_2,
       "modulindex-mod-s-2": modulindex_mod_s_2,
       "modul-typ-mod-s-2": modul_typ_mod_s_2,
       "seriennummer-mod-s-2": seriennummer_mod_s_2,
       "firmware-version-mod-s-2": firmware_version_mod_s_2,
       "hardware-zustand-mod-s-2": hardware_zustand_mod_s_2,
       "betriebs-status-mod-s-2": betriebs_status_mod_s_2,
       "modul-var-para-1-mod-s-2": modul_var_para_1_mod_s_2,
       "modul-var-para-2-mod-s-2": modul_var_para_2_mod_s_2,
       "modul-var-para-3-mod-s-2": modul_var_para_3_mod_s_2,
       "modul-var-para-4-mod-s-2": modul_var_para_4_mod_s_2,
       "modul-var-para-5-mod-s-2": modul_var_para_5_mod_s_2,
       "modul-var-para-6-mod-s-2": modul_var_para_6_mod_s_2,
       "modul-var-para-7-mod-s-2": modul_var_para_7_mod_s_2,
       "modul-var-para-8-mod-s-2": modul_var_para_8_mod_s_2,
       "modul-var-para-9-mod-s-2": modul_var_para_9_mod_s_2,
       "modul-var-para-10-mod-s-2": modul_var_para_10_mod_s_2,
       "modul-var-para-11-mod-s-2": modul_var_para_11_mod_s_2,
       "modul-var-para-12-mod-s-2": modul_var_para_12_mod_s_2,
       "modul-var-para-13-mod-s-2": modul_var_para_13_mod_s_2,
       "modul-var-para-14-mod-s-2": modul_var_para_14_mod_s_2,
       "modul-var-para-15-mod-s-2": modul_var_para_15_mod_s_2,
       "modul-var-para-16-mod-s-2": modul_var_para_16_mod_s_2,
       "modul-var-para-17-mod-s-2": modul_var_para_17_mod_s_2,
       "modul-var-para-18-mod-s-2": modul_var_para_18_mod_s_2,
       "modul-var-para-19-mod-s-2": modul_var_para_19_mod_s_2,
       "modulTable-mod-s-3": modulTable_mod_s_3,
       "modulEntry-mod-s-3": modulEntry_mod_s_3,
       "modulindex-mod-s-3": modulindex_mod_s_3,
       "modul-typ-mod-s-3": modul_typ_mod_s_3,
       "seriennummer-mod-s-3": seriennummer_mod_s_3,
       "firmware-version-mod-s-3": firmware_version_mod_s_3,
       "hardware-zustand-mod-s-3": hardware_zustand_mod_s_3,
       "betriebs-status-mod-s-3": betriebs_status_mod_s_3,
       "modul-var-para-1-mod-s-3": modul_var_para_1_mod_s_3,
       "modul-var-para-2-mod-s-3": modul_var_para_2_mod_s_3,
       "modul-var-para-3-mod-s-3": modul_var_para_3_mod_s_3,
       "modul-var-para-4-mod-s-3": modul_var_para_4_mod_s_3,
       "modul-var-para-5-mod-s-3": modul_var_para_5_mod_s_3,
       "modul-var-para-6-mod-s-3": modul_var_para_6_mod_s_3,
       "modul-var-para-7-mod-s-3": modul_var_para_7_mod_s_3,
       "modul-var-para-8-mod-s-3": modul_var_para_8_mod_s_3,
       "modul-var-para-9-mod-s-3": modul_var_para_9_mod_s_3,
       "modul-var-para-10-mod-s-3": modul_var_para_10_mod_s_3,
       "modul-var-para-11-mod-s-3": modul_var_para_11_mod_s_3,
       "modul-var-para-12-mod-s-3": modul_var_para_12_mod_s_3,
       "modul-var-para-13-mod-s-3": modul_var_para_13_mod_s_3,
       "modul-var-para-14-mod-s-3": modul_var_para_14_mod_s_3,
       "modul-var-para-15-mod-s-3": modul_var_para_15_mod_s_3,
       "modul-var-para-16-mod-s-3": modul_var_para_16_mod_s_3,
       "modul-var-para-17-mod-s-3": modul_var_para_17_mod_s_3,
       "modul-var-para-18-mod-s-3": modul_var_para_18_mod_s_3,
       "modul-var-para-19-mod-s-3": modul_var_para_19_mod_s_3,
       "modulTable-mod-s-4": modulTable_mod_s_4,
       "modulEntry-mod-s-4": modulEntry_mod_s_4,
       "modulindex-mod-s-4": modulindex_mod_s_4,
       "modul-typ-mod-s-4": modul_typ_mod_s_4,
       "seriennummer-mod-s-4": seriennummer_mod_s_4,
       "firmware-version-mod-s-4": firmware_version_mod_s_4,
       "hardware-zustand-mod-s-4": hardware_zustand_mod_s_4,
       "betriebs-status-mod-s-4": betriebs_status_mod_s_4,
       "modul-var-para-1-mod-s-4": modul_var_para_1_mod_s_4,
       "modul-var-para-2-mod-s-4": modul_var_para_2_mod_s_4,
       "modul-var-para-3-mod-s-4": modul_var_para_3_mod_s_4,
       "modul-var-para-4-mod-s-4": modul_var_para_4_mod_s_4,
       "modul-var-para-5-mod-s-4": modul_var_para_5_mod_s_4,
       "modul-var-para-6-mod-s-4": modul_var_para_6_mod_s_4,
       "modul-var-para-7-mod-s-4": modul_var_para_7_mod_s_4,
       "modul-var-para-8-mod-s-4": modul_var_para_8_mod_s_4,
       "modul-var-para-9-mod-s-4": modul_var_para_9_mod_s_4,
       "modul-var-para-10-mod-s-4": modul_var_para_10_mod_s_4,
       "modul-var-para-11-mod-s-4": modul_var_para_11_mod_s_4,
       "modul-var-para-12-mod-s-4": modul_var_para_12_mod_s_4,
       "modul-var-para-13-mod-s-4": modul_var_para_13_mod_s_4,
       "modul-var-para-14-mod-s-4": modul_var_para_14_mod_s_4,
       "modul-var-para-15-mod-s-4": modul_var_para_15_mod_s_4,
       "modul-var-para-16-mod-s-4": modul_var_para_16_mod_s_4,
       "modul-var-para-17-mod-s-4": modul_var_para_17_mod_s_4,
       "modul-var-para-18-mod-s-4": modul_var_para_18_mod_s_4,
       "modul-var-para-19-mod-s-4": modul_var_para_19_mod_s_4,
       "modulTable-mod-s-5": modulTable_mod_s_5,
       "modulEntry-mod-s-5": modulEntry_mod_s_5,
       "modulindex-mod-s-5": modulindex_mod_s_5,
       "modul-typ-mod-s-5": modul_typ_mod_s_5,
       "seriennummer-mod-s-5": seriennummer_mod_s_5,
       "firmware-version-mod-s-5": firmware_version_mod_s_5,
       "hardware-zustand-mod-s-5": hardware_zustand_mod_s_5,
       "betriebs-status-mod-s-5": betriebs_status_mod_s_5,
       "modul-var-para-1-mod-s-5": modul_var_para_1_mod_s_5,
       "modul-var-para-2-mod-s-5": modul_var_para_2_mod_s_5,
       "modul-var-para-3-mod-s-5": modul_var_para_3_mod_s_5,
       "modul-var-para-4-mod-s-5": modul_var_para_4_mod_s_5,
       "modul-var-para-5-mod-s-5": modul_var_para_5_mod_s_5,
       "modul-var-para-6-mod-s-5": modul_var_para_6_mod_s_5,
       "modul-var-para-7-mod-s-5": modul_var_para_7_mod_s_5,
       "modul-var-para-8-mod-s-5": modul_var_para_8_mod_s_5,
       "modul-var-para-9-mod-s-5": modul_var_para_9_mod_s_5,
       "modul-var-para-10-mod-s-5": modul_var_para_10_mod_s_5,
       "modul-var-para-11-mod-s-5": modul_var_para_11_mod_s_5,
       "modul-var-para-12-mod-s-5": modul_var_para_12_mod_s_5,
       "modul-var-para-13-mod-s-5": modul_var_para_13_mod_s_5,
       "modul-var-para-14-mod-s-5": modul_var_para_14_mod_s_5,
       "modul-var-para-15-mod-s-5": modul_var_para_15_mod_s_5,
       "modul-var-para-16-mod-s-5": modul_var_para_16_mod_s_5,
       "modul-var-para-17-mod-s-5": modul_var_para_17_mod_s_5,
       "modul-var-para-18-mod-s-5": modul_var_para_18_mod_s_5,
       "modul-var-para-19-mod-s-5": modul_var_para_19_mod_s_5,
       "modulTable-mod-s-6": modulTable_mod_s_6,
       "modulEntry-mod-s-6": modulEntry_mod_s_6,
       "modulindex-mod-s-6": modulindex_mod_s_6,
       "modul-typ-mod-s-6": modul_typ_mod_s_6,
       "seriennummer-mod-s-6": seriennummer_mod_s_6,
       "firmware-version-mod-s-6": firmware_version_mod_s_6,
       "hardware-zustand-mod-s-6": hardware_zustand_mod_s_6,
       "betriebs-status-mod-s-6": betriebs_status_mod_s_6,
       "modul-var-para-1-mod-s-6": modul_var_para_1_mod_s_6,
       "modul-var-para-2-mod-s-6": modul_var_para_2_mod_s_6,
       "modul-var-para-3-mod-s-6": modul_var_para_3_mod_s_6,
       "modul-var-para-4-mod-s-6": modul_var_para_4_mod_s_6,
       "modul-var-para-5-mod-s-6": modul_var_para_5_mod_s_6,
       "modul-var-para-6-mod-s-6": modul_var_para_6_mod_s_6,
       "modul-var-para-7-mod-s-6": modul_var_para_7_mod_s_6,
       "modul-var-para-8-mod-s-6": modul_var_para_8_mod_s_6,
       "modul-var-para-9-mod-s-6": modul_var_para_9_mod_s_6,
       "modul-var-para-10-mod-s-6": modul_var_para_10_mod_s_6,
       "modul-var-para-11-mod-s-6": modul_var_para_11_mod_s_6,
       "modul-var-para-12-mod-s-6": modul_var_para_12_mod_s_6,
       "modul-var-para-13-mod-s-6": modul_var_para_13_mod_s_6,
       "modul-var-para-14-mod-s-6": modul_var_para_14_mod_s_6,
       "modul-var-para-15-mod-s-6": modul_var_para_15_mod_s_6,
       "modul-var-para-16-mod-s-6": modul_var_para_16_mod_s_6,
       "modul-var-para-17-mod-s-6": modul_var_para_17_mod_s_6,
       "modul-var-para-18-mod-s-6": modul_var_para_18_mod_s_6,
       "modul-var-para-19-mod-s-6": modul_var_para_19_mod_s_6,
       "modulTable-mod-s-7": modulTable_mod_s_7,
       "modulEntry-mod-s-7": modulEntry_mod_s_7,
       "modulindex-mod-s-7": modulindex_mod_s_7,
       "modul-typ-mod-s-7": modul_typ_mod_s_7,
       "seriennummer-mod-s-7": seriennummer_mod_s_7,
       "firmware-version-mod-s-7": firmware_version_mod_s_7,
       "hardware-zustand-mod-s-7": hardware_zustand_mod_s_7,
       "betriebs-status-mod-s-7": betriebs_status_mod_s_7,
       "modul-var-para-1-mod-s-7": modul_var_para_1_mod_s_7,
       "modul-var-para-2-mod-s-7": modul_var_para_2_mod_s_7,
       "modul-var-para-3-mod-s-7": modul_var_para_3_mod_s_7,
       "modul-var-para-4-mod-s-7": modul_var_para_4_mod_s_7,
       "modul-var-para-5-mod-s-7": modul_var_para_5_mod_s_7,
       "modul-var-para-6-mod-s-7": modul_var_para_6_mod_s_7,
       "modul-var-para-7-mod-s-7": modul_var_para_7_mod_s_7,
       "modul-var-para-8-mod-s-7": modul_var_para_8_mod_s_7,
       "modul-var-para-9-mod-s-7": modul_var_para_9_mod_s_7,
       "modul-var-para-10-mod-s-7": modul_var_para_10_mod_s_7,
       "modul-var-para-11-mod-s-7": modul_var_para_11_mod_s_7,
       "modul-var-para-12-mod-s-7": modul_var_para_12_mod_s_7,
       "modul-var-para-13-mod-s-7": modul_var_para_13_mod_s_7,
       "modul-var-para-14-mod-s-7": modul_var_para_14_mod_s_7,
       "modul-var-para-15-mod-s-7": modul_var_para_15_mod_s_7,
       "modul-var-para-16-mod-s-7": modul_var_para_16_mod_s_7,
       "modul-var-para-17-mod-s-7": modul_var_para_17_mod_s_7,
       "modul-var-para-18-mod-s-7": modul_var_para_18_mod_s_7,
       "modul-var-para-19-mod-s-7": modul_var_para_19_mod_s_7,
       "modulTable-mod-s-8": modulTable_mod_s_8,
       "modulEntry-mod-s-8": modulEntry_mod_s_8,
       "modulindex-mod-s-8": modulindex_mod_s_8,
       "modul-typ-mod-s-8": modul_typ_mod_s_8,
       "seriennummer-mod-s-8": seriennummer_mod_s_8,
       "firmware-version-mod-s-8": firmware_version_mod_s_8,
       "hardware-zustand-mod-s-8": hardware_zustand_mod_s_8,
       "betriebs-status-mod-s-8": betriebs_status_mod_s_8,
       "modul-var-para-1-mod-s-8": modul_var_para_1_mod_s_8,
       "modul-var-para-2-mod-s-8": modul_var_para_2_mod_s_8,
       "modul-var-para-3-mod-s-8": modul_var_para_3_mod_s_8,
       "modul-var-para-4-mod-s-8": modul_var_para_4_mod_s_8,
       "modul-var-para-5-mod-s-8": modul_var_para_5_mod_s_8,
       "modul-var-para-6-mod-s-8": modul_var_para_6_mod_s_8,
       "modul-var-para-7-mod-s-8": modul_var_para_7_mod_s_8,
       "modul-var-para-8-mod-s-8": modul_var_para_8_mod_s_8,
       "modul-var-para-9-mod-s-8": modul_var_para_9_mod_s_8,
       "modul-var-para-10-mod-s-8": modul_var_para_10_mod_s_8,
       "modul-var-para-11-mod-s-8": modul_var_para_11_mod_s_8,
       "modul-var-para-12-mod-s-8": modul_var_para_12_mod_s_8,
       "modul-var-para-13-mod-s-8": modul_var_para_13_mod_s_8,
       "modul-var-para-14-mod-s-8": modul_var_para_14_mod_s_8,
       "modul-var-para-15-mod-s-8": modul_var_para_15_mod_s_8,
       "modul-var-para-16-mod-s-8": modul_var_para_16_mod_s_8,
       "modul-var-para-17-mod-s-8": modul_var_para_17_mod_s_8,
       "modul-var-para-18-mod-s-8": modul_var_para_18_mod_s_8,
       "modul-var-para-19-mod-s-8": modul_var_para_19_mod_s_8,
       "modulTable-mod-s-9": modulTable_mod_s_9,
       "modulEntry-mod-s-9": modulEntry_mod_s_9,
       "modulindex-mod-s-9": modulindex_mod_s_9,
       "modul-typ-mod-s-9": modul_typ_mod_s_9,
       "seriennummer-mod-s-9": seriennummer_mod_s_9,
       "firmware-version-mod-s-9": firmware_version_mod_s_9,
       "hardware-zustand-mod-s-9": hardware_zustand_mod_s_9,
       "betriebs-status-mod-s-9": betriebs_status_mod_s_9,
       "modul-var-para-1-mod-s-9": modul_var_para_1_mod_s_9,
       "modul-var-para-2-mod-s-9": modul_var_para_2_mod_s_9,
       "modul-var-para-3-mod-s-9": modul_var_para_3_mod_s_9,
       "modul-var-para-4-mod-s-9": modul_var_para_4_mod_s_9,
       "modul-var-para-5-mod-s-9": modul_var_para_5_mod_s_9,
       "modul-var-para-6-mod-s-9": modul_var_para_6_mod_s_9,
       "modul-var-para-7-mod-s-9": modul_var_para_7_mod_s_9,
       "modul-var-para-8-mod-s-9": modul_var_para_8_mod_s_9,
       "modul-var-para-9-mod-s-9": modul_var_para_9_mod_s_9,
       "modul-var-para-10-mod-s-9": modul_var_para_10_mod_s_9,
       "modul-var-para-11-mod-s-9": modul_var_para_11_mod_s_9,
       "modul-var-para-12-mod-s-9": modul_var_para_12_mod_s_9,
       "modul-var-para-13-mod-s-9": modul_var_para_13_mod_s_9,
       "modul-var-para-14-mod-s-9": modul_var_para_14_mod_s_9,
       "modul-var-para-15-mod-s-9": modul_var_para_15_mod_s_9,
       "modul-var-para-16-mod-s-9": modul_var_para_16_mod_s_9,
       "modul-var-para-17-mod-s-9": modul_var_para_17_mod_s_9,
       "modul-var-para-18-mod-s-9": modul_var_para_18_mod_s_9,
       "modul-var-para-19-mod-s-9": modul_var_para_19_mod_s_9,
       "modulTable-mod-s-10": modulTable_mod_s_10,
       "modulEntry-mod-s-10": modulEntry_mod_s_10,
       "modulindex-mod-s-10": modulindex_mod_s_10,
       "modul-typ-mod-s-10": modul_typ_mod_s_10,
       "seriennummer-mod-s-10": seriennummer_mod_s_10,
       "firmware-version-mod-s-10": firmware_version_mod_s_10,
       "hardware-zustand-mod-s-10": hardware_zustand_mod_s_10,
       "betriebs-status-mod-s-10": betriebs_status_mod_s_10,
       "modul-var-para-1-mod-s-10": modul_var_para_1_mod_s_10,
       "modul-var-para-2-mod-s-10": modul_var_para_2_mod_s_10,
       "modul-var-para-3-mod-s-10": modul_var_para_3_mod_s_10,
       "modul-var-para-4-mod-s-10": modul_var_para_4_mod_s_10,
       "modul-var-para-5-mod-s-10": modul_var_para_5_mod_s_10,
       "modul-var-para-6-mod-s-10": modul_var_para_6_mod_s_10,
       "modul-var-para-7-mod-s-10": modul_var_para_7_mod_s_10,
       "modul-var-para-8-mod-s-10": modul_var_para_8_mod_s_10,
       "modul-var-para-9-mod-s-10": modul_var_para_9_mod_s_10,
       "modul-var-para-10-mod-s-10": modul_var_para_10_mod_s_10,
       "modul-var-para-11-mod-s-10": modul_var_para_11_mod_s_10,
       "modul-var-para-12-mod-s-10": modul_var_para_12_mod_s_10,
       "modul-var-para-13-mod-s-10": modul_var_para_13_mod_s_10,
       "modul-var-para-14-mod-s-10": modul_var_para_14_mod_s_10,
       "modul-var-para-15-mod-s-10": modul_var_para_15_mod_s_10,
       "modul-var-para-16-mod-s-10": modul_var_para_16_mod_s_10,
       "modul-var-para-17-mod-s-10": modul_var_para_17_mod_s_10,
       "modul-var-para-18-mod-s-10": modul_var_para_18_mod_s_10,
       "modul-var-para-19-mod-s-10": modul_var_para_19_mod_s_10,
       "modulTable-mod-s-11": modulTable_mod_s_11,
       "modulEntry-mod-s-11": modulEntry_mod_s_11,
       "modulindex-mod-s-11": modulindex_mod_s_11,
       "modul-typ-mod-s-11": modul_typ_mod_s_11,
       "seriennummer-mod-s-11": seriennummer_mod_s_11,
       "firmware-version-mod-s-11": firmware_version_mod_s_11,
       "hardware-zustand-mod-s-11": hardware_zustand_mod_s_11,
       "betriebs-status-mod-s-11": betriebs_status_mod_s_11,
       "modul-var-para-1-mod-s-11": modul_var_para_1_mod_s_11,
       "modul-var-para-2-mod-s-11": modul_var_para_2_mod_s_11,
       "modul-var-para-3-mod-s-11": modul_var_para_3_mod_s_11,
       "modul-var-para-4-mod-s-11": modul_var_para_4_mod_s_11,
       "modul-var-para-5-mod-s-11": modul_var_para_5_mod_s_11,
       "modul-var-para-6-mod-s-11": modul_var_para_6_mod_s_11,
       "modul-var-para-7-mod-s-11": modul_var_para_7_mod_s_11,
       "modul-var-para-8-mod-s-11": modul_var_para_8_mod_s_11,
       "modul-var-para-9-mod-s-11": modul_var_para_9_mod_s_11,
       "modul-var-para-10-mod-s-11": modul_var_para_10_mod_s_11,
       "modul-var-para-11-mod-s-11": modul_var_para_11_mod_s_11,
       "modul-var-para-12-mod-s-11": modul_var_para_12_mod_s_11,
       "modul-var-para-13-mod-s-11": modul_var_para_13_mod_s_11,
       "modul-var-para-14-mod-s-11": modul_var_para_14_mod_s_11,
       "modul-var-para-15-mod-s-11": modul_var_para_15_mod_s_11,
       "modul-var-para-16-mod-s-11": modul_var_para_16_mod_s_11,
       "modul-var-para-17-mod-s-11": modul_var_para_17_mod_s_11,
       "modul-var-para-18-mod-s-11": modul_var_para_18_mod_s_11,
       "modul-var-para-19-mod-s-11": modul_var_para_19_mod_s_11,
       "ak-mgmt-i": ak_mgmt_i,
       "ak-intern-ip": ak_intern_ip,
       "ak-extern-ip": ak_extern_ip,
       "ak-intern-subnetmask-ip": ak_intern_subnetmask_ip,
       "ak-router-ip": ak_router_ip,
       "ak-divers-i": ak_divers_i,
       "to-be-defined-1": to_be_defined_1,
       "to-be-defined-2": to_be_defined_2,
       "ak-traps-i": ak_traps_i,
       "ak-master-i": ak_master_i,
       "ak-slave-1-i": ak_slave_1_i,
       "modulTable-s-1": modulTable_s_1,
       "modulEntry-s-1": modulEntry_s_1,
       "modulIndex-s-1": modulIndex_s_1,
       "geraete-typ-s-1": geraete_typ_s_1,
       "betriebsstatus-s-1": betriebsstatus_s_1,
       "senderstatus-s-1": senderstatus_s_1,
       "fehlerstatus-s-1": fehlerstatus_s_1,
       "dem-adapter-zugeordnete-funkgeraetetype-s-1": dem_adapter_zugeordnete_funkgeraetetype_s_1,
       "eingabe-und-anzeigemodul-s-1": eingabe_und_anzeigemodul_s_1,
       "mod-bus-verbindung-module-s-1": mod_bus_verbindung_module_s_1,
       "gemessene-sendeleistung-im-testmode-s-1": gemessene_sendeleistung_im_testmode_s_1,
       "aktuelle-sendeleistung-s-1": aktuelle_sendeleistung_s_1,
       "gemessene-reflexion-im-testmode-s-1": gemessene_reflexion_im_testmode_s_1,
       "aktuelle-reflexion-s-1": aktuelle_reflexion_s_1,
       "letzte-gemessene-donor-sendeleistung-s-1": letzte_gemessene_donor_sendeleistung_s_1,
       "aktuelle-donor-sendeleistung-s-1": aktuelle_donor_sendeleistung_s_1,
       "letzte-gemessene-donor-reflexion-s-1": letzte_gemessene_donor_reflexion_s_1,
       "aktuelle-donor-reflexion-s-1": aktuelle_donor_reflexion_s_1,
       "anzahl-gemessener-praesenzsignale-im-testmode-s-1": anzahl_gemessener_praesenzsignale_im_testmode_s_1,
       "aktuelle-ausgangsspannung-ub-s-1": aktuelle_ausgangsspannung_ub_s_1,
       "aktuelle-ausgangsspannung-u1-s-1": aktuelle_ausgangsspannung_u1_s_1,
       "aktuelle-ausgangsspannung-u2-s-1": aktuelle_ausgangsspannung_u2_s_1,
       "aktuelle-ausgangsspannung-u3-s-1": aktuelle_ausgangsspannung_u3_s_1,
       "aktuelle-ausgangsspannung-u4-s-1": aktuelle_ausgangsspannung_u4_s_1,
       "aktuelle-ausgangsspannung-u5-s-1": aktuelle_ausgangsspannung_u5_s_1,
       "aktuelle-ausgangsspannung-u6-s-1": aktuelle_ausgangsspannung_u6_s_1,
       "aktuelle-ausgangsspannung-u7-s-1": aktuelle_ausgangsspannung_u7_s_1,
       "aktuelle-ausgangsspannung-u8-s-1": aktuelle_ausgangsspannung_u8_s_1,
       "aktuelle-ladespannung-an-akku-kreis-1-s-1": aktuelle_ladespannung_an_akku_kreis_1_s_1,
       "aktuelle-ladespannung-an-akku-Kreis-2-s-1": aktuelle_ladespannung_an_akku_Kreis_2_s_1,
       "aktuelle-ladespannung-an-akku-Kreis-3-s-1": aktuelle_ladespannung_an_akku_Kreis_3_s_1,
       "aktuelle-ladespannung-an-akku-kreis-4-s-1": aktuelle_ladespannung_an_akku_kreis_4_s_1,
       "aktuelle-ladespannung-an-akku-kreis-5-s-1": aktuelle_ladespannung_an_akku_kreis_5_s_1,
       "aktuelle-ladespannung-an-akku-kreis-6-s-1": aktuelle_ladespannung_an_akku_kreis_6_s_1,
       "aktuelle-ladespannung-an-akku-kreis-7-s-1": aktuelle_ladespannung_an_akku_kreis_7_s_1,
       "aktuelle-ladespannung-an-akku-kreis-8-s-1": aktuelle_ladespannung_an_akku_kreis_8_s_1,
       "aktuelle-spannung-an-akku-kreis-1-s-1": aktuelle_spannung_an_akku_kreis_1_s_1,
       "aktuelle-spannung-an-akku-kreis-2-s-1": aktuelle_spannung_an_akku_kreis_2_s_1,
       "aktuelle-spannung-an-akku-kreis-3-s-1": aktuelle_spannung_an_akku_kreis_3_s_1,
       "aktuelle-spannung-an-akku-kreis-4-s-1": aktuelle_spannung_an_akku_kreis_4_s_1,
       "aktuelle-spannung-an-akku-reis-5-s-1": aktuelle_spannung_an_akku_reis_5_s_1,
       "aktuelle-spannung-an-akku-kreis-6-s-1": aktuelle_spannung_an_akku_kreis_6_s_1,
       "aktuelle-spannung-an-akku-kreis-7-s-1": aktuelle_spannung_an_akku_kreis_7_s_1,
       "aktuelle-spannung-an-akku-kreis-8-s-1": aktuelle_spannung_an_akku_kreis_8_s_1,
       "testergebnis-lastspannung-an-akku-reis-1-s-1": testergebnis_lastspannung_an_akku_reis_1_s_1,
       "testergebnis-lastspannung-an-akku-kreis-2-s-1": testergebnis_lastspannung_an_akku_kreis_2_s_1,
       "testergebnis-lastspannung-an-akku-kreis-3-s-1": testergebnis_lastspannung_an_akku_kreis_3_s_1,
       "testergebnis-lastspannung-an-akku-kreis-4-s-1": testergebnis_lastspannung_an_akku_kreis_4_s_1,
       "testergebnis-lastspannung-an-akku-kreis-5-s-1": testergebnis_lastspannung_an_akku_kreis_5_s_1,
       "testergebnis-lastspannung-an-akku-kreis-6-s-1": testergebnis_lastspannung_an_akku_kreis_6_s_1,
       "testergebnis-lastspannung-an-akku-kreis-7-s-1": testergebnis_lastspannung_an_akku_kreis_7_s_1,
       "testergebnis-lastspannung-an-akku-kreis-8-s-1": testergebnis_lastspannung_an_akku_kreis_8_s_1,
       "testergebnis-innenwiderstand-akku-kreis-1-s-1": testergebnis_innenwiderstand_akku_kreis_1_s_1,
       "testergebnis-innenwiderstand-akku-kreis-2-s-1": testergebnis_innenwiderstand_akku_kreis_2_s_1,
       "testergebnis-innenwiderstand-akku-kreis-3-s-1": testergebnis_innenwiderstand_akku_kreis_3_s_1,
       "testergebnis-innenwiderstand-akku-kreis-4-s-1": testergebnis_innenwiderstand_akku_kreis_4_s_1,
       "testergebnis-innenwiderstand-akku-kreis-5-s-1": testergebnis_innenwiderstand_akku_kreis_5_s_1,
       "testergebnis-innenwiderstand-akku-kreis-6-s-1": testergebnis_innenwiderstand_akku_kreis_6_s_1,
       "testergebnis-innenwiderstand-akku-kreis-7-s-1": testergebnis_innenwiderstand_akku_kreis_7_s_1,
       "testergebnis-innenwiderstand-akku-kreis-8-s-1": testergebnis_innenwiderstand_akku_kreis_8_s_1,
       "netzteilspannung-uin1-s-1": netzteilspannung_uin1_s_1,
       "netzteilspannung-uin2-s-1": netzteilspannung_uin2_s_1,
       "programmierte-minimale-soll-sendeleistung-s-1": programmierte_minimale_soll_sendeleistung_s_1,
       "programmierte-maximale-antennen-reflexion-s-1": programmierte_maximale_antennen_reflexion_s_1,
       "programmierte-minimale-anzahl-praesenzsignale-s-1": programmierte_minimale_anzahl_praesenzsignale_s_1,
       "summen-fehlerstatus-von-tmoa-anlage-s-1": summen_fehlerstatus_von_tmoa_anlage_s_1,
       "summen-fehlerstatus-von-anbinderepeater-s-1": summen_fehlerstatus_von_anbinderepeater_s_1,
       "summen-fehlerstatus-von-analogem-repeater-s-1": summen_fehlerstatus_von_analogem_repeater_s_1,
       "aktuelle-ladespannung-akku-kreis-1-int-sicherung-defekt-s-1": aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_1,
       "aktuelle-ladespannung-akku-kreis-2-int-sicherung-defekt-s-1": aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_1,
       "aktuelle-ladespannung-akku-kreis-3-int-sicherung-defekt-s-1": aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_1,
       "aktuelle-ladespannung-akku-kreis-4-int-sicherung-defekt-s-1": aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_1,
       "aktuelle-ladespannung-akku-kreis-5-int-sicherung-defekt-s-1": aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_1,
       "aktuelle-ladespannung-akku-kreis-6-int-sicherung-defekt-s-1": aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_1,
       "aktuelle-ladespannung-akku-kreis-7-int-sicherung-defekt-s-1": aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_1,
       "aktuelle-ladespannung-akku-kreis-8-int-sicherung-defekt-s-1": aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_1,
       "netzspannungsversorgung-von-tmoa-anlage-s-1": netzspannungsversorgung_von_tmoa_anlage_s_1,
       "netzspannungsversorgung-von-anbinderepeater-s-1": netzspannungsversorgung_von_anbinderepeater_s_1,
       "fgb-id1-verbindungsstatus-s-1": fgb_id1_verbindungsstatus_s_1,
       "fgb-id2-verbindungsstatus-s-1": fgb_id2_verbindungsstatus_s_1,
       "fgb-id3-verbindungsstatus-s-1": fgb_id3_verbindungsstatus_s_1,
       "fgb-id4-verbindungsstatus-s-1": fgb_id4_verbindungsstatus_s_1,
       "fgb-id5-verbindungsstatus-s-1": fgb_id5_verbindungsstatus_s_1,
       "fgb-id6-verbindungsstatus-s-1": fgb_id6_verbindungsstatus_s_1,
       "fgb-id7-verbindungsstatus-s-1": fgb_id7_verbindungsstatus_s_1,
       "fgb-id8-verbindungsstatus-s-1": fgb_id8_verbindungsstatus_s_1,
       "fgb-id9-verbindungsstatus-s-1": fgb_id9_verbindungsstatus_s_1,
       "fgb-id10-verbindungsstatus-s-1": fgb_id10_verbindungsstatus_s_1,
       "fgb-id11-verbindungsstatus-s-1": fgb_id11_verbindungsstatus_s_1,
       "mod-bus-verbindungsstatus-s-1": mod_bus_verbindungsstatus_s_1,
       "fgb-bus-verbindungsstatus-s-1": fgb_bus_verbindungsstatus_s_1,
       "slave-bus-verbindungsstatus-s-1": slave_bus_verbindungsstatus_s_1,
       "gsm-modem-verbindungsstatus-s-1": gsm_modem_verbindungsstatus_s_1,
       "gsm-modem-sim-karte-s-1": gsm_modem_sim_karte_s_1,
       "gsm-modem-pin-nummer-s-1": gsm_modem_pin_nummer_s_1,
       "gsm-modem-provider-service-s-1": gsm_modem_provider_service_s_1,
       "gsm-modem-empfangspegel-s-1": gsm_modem_empfangspegel_s_1,
       "lte-router-verbindungsstatus-s-1": lte_router_verbindungsstatus_s_1,
       "lte-router-provider-service-s-1": lte_router_provider_service_s_1,
       "lte-router-empfangspegel-s-1": lte_router_empfangspegel_s_1,
       "antennenleitungsueberwachung-1-s-1": antennenleitungsueberwachung_1_s_1,
       "antennenleitungsueberwachung-2-s-1": antennenleitungsueberwachung_2_s_1,
       "antennenleitungseuberwachung-3-s-1": antennenleitungseuberwachung_3_s_1,
       "interne-temperaturuebwerwachung-s-1": interne_temperaturuebwerwachung_s_1,
       "stoerueberwachung-optisches-verteilsystem-1-s-1": stoerueberwachung_optisches_verteilsystem_1_s_1,
       "stoerueberwachung-optisches-verteilsystem-2-s-1": stoerueberwachung_optisches_verteilsystem_2_s_1,
       "lte-router-sim-karte-s-1": lte_router_sim_karte_s_1,
       "lte-router-pin-nummer-s-1": lte_router_pin_nummer_s_1,
       "ak-slave-2-i": ak_slave_2_i,
       "modulTable-s-2": modulTable_s_2,
       "modulEntry-s-2": modulEntry_s_2,
       "modulIndex-s-2": modulIndex_s_2,
       "geraete-typ-s-2": geraete_typ_s_2,
       "betriebsstatus-s-2": betriebsstatus_s_2,
       "senderstatus-s-2": senderstatus_s_2,
       "fehlerstatus-s-2": fehlerstatus_s_2,
       "dem-adapter-zugeordnete-funkgeraetetype-s-2": dem_adapter_zugeordnete_funkgeraetetype_s_2,
       "eingabe-und-anzeigemodul-s-2": eingabe_und_anzeigemodul_s_2,
       "mod-bus-verbindung-module-s-2": mod_bus_verbindung_module_s_2,
       "gemessene-sendeleistung-im-testmode-s-2": gemessene_sendeleistung_im_testmode_s_2,
       "aktuelle-sendeleistung-s-2": aktuelle_sendeleistung_s_2,
       "gemessene-reflexion-im-testmode-s-2": gemessene_reflexion_im_testmode_s_2,
       "aktuelle-reflexion-s-2": aktuelle_reflexion_s_2,
       "letzte-gemessene-donor-sendeleistung-s-2": letzte_gemessene_donor_sendeleistung_s_2,
       "aktuelle-donor-sendeleistung-s-2": aktuelle_donor_sendeleistung_s_2,
       "letzte-gemessene-donor-reflexion-s-2": letzte_gemessene_donor_reflexion_s_2,
       "aktuelle-donor-reflexion-s-2": aktuelle_donor_reflexion_s_2,
       "anzahl-gemessener-praesenzsignale-im-testmode-s-2": anzahl_gemessener_praesenzsignale_im_testmode_s_2,
       "aktuelle-ausgangsspannung-ub-s-2": aktuelle_ausgangsspannung_ub_s_2,
       "aktuelle-ausgangsspannung-u1-s-2": aktuelle_ausgangsspannung_u1_s_2,
       "aktuelle-ausgangsspannung-u2-s-2": aktuelle_ausgangsspannung_u2_s_2,
       "aktuelle-ausgangsspannung-u3-s-2": aktuelle_ausgangsspannung_u3_s_2,
       "aktuelle-ausgangsspannung-u4-s-2": aktuelle_ausgangsspannung_u4_s_2,
       "aktuelle-ausgangsspannung-u5-s-2": aktuelle_ausgangsspannung_u5_s_2,
       "aktuelle-ausgangsspannung-u6-s-2": aktuelle_ausgangsspannung_u6_s_2,
       "aktuelle-ausgangsspannung-u7-s-2": aktuelle_ausgangsspannung_u7_s_2,
       "aktuelle-ausgangsspannung-u8-s-2": aktuelle_ausgangsspannung_u8_s_2,
       "aktuelle-ladespannung-an-akku-kreis-1-s-2": aktuelle_ladespannung_an_akku_kreis_1_s_2,
       "aktuelle-ladespannung-an-akku-Kreis-2-s-2": aktuelle_ladespannung_an_akku_Kreis_2_s_2,
       "aktuelle-ladespannung-an-akku-Kreis-3-s-2": aktuelle_ladespannung_an_akku_Kreis_3_s_2,
       "aktuelle-ladespannung-an-akku-kreis-4-s-2": aktuelle_ladespannung_an_akku_kreis_4_s_2,
       "aktuelle-ladespannung-an-akku-kreis-5-s-2": aktuelle_ladespannung_an_akku_kreis_5_s_2,
       "aktuelle-ladespannung-an-akku-kreis-6-s-2": aktuelle_ladespannung_an_akku_kreis_6_s_2,
       "aktuelle-ladespannung-an-akku-kreis-7-s-2": aktuelle_ladespannung_an_akku_kreis_7_s_2,
       "aktuelle-ladespannung-an-akku-kreis-8-s-2": aktuelle_ladespannung_an_akku_kreis_8_s_2,
       "aktuelle-spannung-an-akku-kreis-1-s-2": aktuelle_spannung_an_akku_kreis_1_s_2,
       "aktuelle-spannung-an-akku-kreis-2-s-2": aktuelle_spannung_an_akku_kreis_2_s_2,
       "aktuelle-spannung-an-akku-kreis-3-s-2": aktuelle_spannung_an_akku_kreis_3_s_2,
       "aktuelle-spannung-an-akku-kreis-4-s-2": aktuelle_spannung_an_akku_kreis_4_s_2,
       "aktuelle-spannung-an-akku-reis-5-s-2": aktuelle_spannung_an_akku_reis_5_s_2,
       "aktuelle-spannung-an-akku-kreis-6-s-2": aktuelle_spannung_an_akku_kreis_6_s_2,
       "aktuelle-spannung-an-akku-kreis-7-s-2": aktuelle_spannung_an_akku_kreis_7_s_2,
       "aktuelle-spannung-an-akku-kreis-8-s-2": aktuelle_spannung_an_akku_kreis_8_s_2,
       "testergebnis-lastspannung-an-akku-reis-1-s-2": testergebnis_lastspannung_an_akku_reis_1_s_2,
       "testergebnis-lastspannung-an-akku-kreis-2-s-2": testergebnis_lastspannung_an_akku_kreis_2_s_2,
       "testergebnis-lastspannung-an-akku-kreis-3-s-2": testergebnis_lastspannung_an_akku_kreis_3_s_2,
       "testergebnis-lastspannung-an-akku-kreis-4-s-2": testergebnis_lastspannung_an_akku_kreis_4_s_2,
       "testergebnis-lastspannung-an-akku-kreis-5-s-2": testergebnis_lastspannung_an_akku_kreis_5_s_2,
       "testergebnis-lastspannung-an-akku-kreis-6-s-2": testergebnis_lastspannung_an_akku_kreis_6_s_2,
       "testergebnis-lastspannung-an-akku-kreis-7-s-2": testergebnis_lastspannung_an_akku_kreis_7_s_2,
       "testergebnis-lastspannung-an-akku-kreis-8-s-2": testergebnis_lastspannung_an_akku_kreis_8_s_2,
       "testergebnis-innenwiderstand-akku-kreis-1-s-2": testergebnis_innenwiderstand_akku_kreis_1_s_2,
       "testergebnis-innenwiderstand-akku-kreis-2-s-2": testergebnis_innenwiderstand_akku_kreis_2_s_2,
       "testergebnis-innenwiderstand-akku-kreis-3-s-2": testergebnis_innenwiderstand_akku_kreis_3_s_2,
       "testergebnis-innenwiderstand-akku-kreis-4-s-2": testergebnis_innenwiderstand_akku_kreis_4_s_2,
       "testergebnis-innenwiderstand-akku-kreis-5-s-2": testergebnis_innenwiderstand_akku_kreis_5_s_2,
       "testergebnis-innenwiderstand-akku-kreis-6-s-2": testergebnis_innenwiderstand_akku_kreis_6_s_2,
       "testergebnis-innenwiderstand-akku-kreis-7-s-2": testergebnis_innenwiderstand_akku_kreis_7_s_2,
       "testergebnis-innenwiderstand-akku-kreis-8-s-2": testergebnis_innenwiderstand_akku_kreis_8_s_2,
       "netzteilspannung-uin1-s-2": netzteilspannung_uin1_s_2,
       "netzteilspannung-uin2-s-2": netzteilspannung_uin2_s_2,
       "programmierte-minimale-soll-sendeleistung-s-2": programmierte_minimale_soll_sendeleistung_s_2,
       "programmierte-maximale-antennen-reflexion-s-2": programmierte_maximale_antennen_reflexion_s_2,
       "programmierte-minimale-anzahl-praesenzsignale-s-2": programmierte_minimale_anzahl_praesenzsignale_s_2,
       "summen-fehlerstatus-von-tmoa-anlage-s-2": summen_fehlerstatus_von_tmoa_anlage_s_2,
       "summen-fehlerstatus-von-anbinderepeater-s-2": summen_fehlerstatus_von_anbinderepeater_s_2,
       "summen-fehlerstatus-von-analogem-repeater-s-2": summen_fehlerstatus_von_analogem_repeater_s_2,
       "aktuelle-ladespannung-akku-kreis-1-int-sicherung-defekt-s-2": aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_2,
       "aktuelle-ladespannung-akku-kreis-2-int-sicherung-defekt-s-2": aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_2,
       "aktuelle-ladespannung-akku-kreis-3-int-sicherung-defekt-s-2": aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_2,
       "aktuelle-ladespannung-akku-kreis-4-int-sicherung-defekt-s-2": aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_2,
       "aktuelle-ladespannung-akku-kreis-5-int-sicherung-defekt-s-2": aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_2,
       "aktuelle-ladespannung-akku-kreis-6-int-sicherung-defekt-s-2": aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_2,
       "aktuelle-ladespannung-akku-kreis-7-int-sicherung-defekt-s-2": aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_2,
       "aktuelle-ladespannung-akku-kreis-8-int-sicherung-defekt-s-2": aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_2,
       "netzspannungsversorgung-von-tmoa-anlage-s-2": netzspannungsversorgung_von_tmoa_anlage_s_2,
       "netzspannungsversorgung-von-anbinderepeater-s-2": netzspannungsversorgung_von_anbinderepeater_s_2,
       "fgb-id1-verbindungsstatus-s-2": fgb_id1_verbindungsstatus_s_2,
       "fgb-id2-verbindungsstatus-s-2": fgb_id2_verbindungsstatus_s_2,
       "fgb-id3-verbindungsstatus-s-2": fgb_id3_verbindungsstatus_s_2,
       "fgb-id4-verbindungsstatus-s-2": fgb_id4_verbindungsstatus_s_2,
       "fgb-id5-verbindungsstatus-s-2": fgb_id5_verbindungsstatus_s_2,
       "fgb-id6-verbindungsstatus-s-2": fgb_id6_verbindungsstatus_s_2,
       "fgb-id7-verbindungsstatus-s-2": fgb_id7_verbindungsstatus_s_2,
       "fgb-id8-verbindungsstatus-s-2": fgb_id8_verbindungsstatus_s_2,
       "fgb-id9-verbindungsstatus-s-2": fgb_id9_verbindungsstatus_s_2,
       "fgb-id10-verbindungsstatus-s-2": fgb_id10_verbindungsstatus_s_2,
       "fgb-id11-verbindungsstatus-s-2": fgb_id11_verbindungsstatus_s_2,
       "mod-bus-verbindungsstatus-s-2": mod_bus_verbindungsstatus_s_2,
       "fgb-bus-verbindungsstatus-s-2": fgb_bus_verbindungsstatus_s_2,
       "slave-bus-verbindungsstatus-s-2": slave_bus_verbindungsstatus_s_2,
       "gsm-modem-verbindungsstatus-s-2": gsm_modem_verbindungsstatus_s_2,
       "gsm-modem-sim-karte-s-2": gsm_modem_sim_karte_s_2,
       "gsm-modem-pin-nummer-s-2": gsm_modem_pin_nummer_s_2,
       "gsm-modem-provider-service-s-2": gsm_modem_provider_service_s_2,
       "gsm-modem-empfangspegel-s-2": gsm_modem_empfangspegel_s_2,
       "lte-router-verbindungsstatus-s-2": lte_router_verbindungsstatus_s_2,
       "lte-router-provider-service-s-2": lte_router_provider_service_s_2,
       "lte-router-empfangspegel-s-2": lte_router_empfangspegel_s_2,
       "antennenleitungsueberwachung-1-s-2": antennenleitungsueberwachung_1_s_2,
       "antennenleitungsueberwachung-2-s-2": antennenleitungsueberwachung_2_s_2,
       "antennenleitungseuberwachung-3-s-2": antennenleitungseuberwachung_3_s_2,
       "interne-temperaturuebwerwachung-s-2": interne_temperaturuebwerwachung_s_2,
       "stoerueberwachung-optisches-verteilsystem-1-s-2": stoerueberwachung_optisches_verteilsystem_1_s_2,
       "stoerueberwachung-optisches-verteilsystem-2-s-2": stoerueberwachung_optisches_verteilsystem_2_s_2,
       "lte-router-sim-karte-s-2": lte_router_sim_karte_s_2,
       "lte-router-pin-nummer-s-2": lte_router_pin_nummer_s_2,
       "ak-slave-3-i": ak_slave_3_i,
       "modulTable-s-3": modulTable_s_3,
       "modulEntry-s-3": modulEntry_s_3,
       "modulIndex-s-3": modulIndex_s_3,
       "geraete-typ-s-3": geraete_typ_s_3,
       "betriebsstatus-s-3": betriebsstatus_s_3,
       "senderstatus-s-3": senderstatus_s_3,
       "fehlerstatus-s-3": fehlerstatus_s_3,
       "dem-adapter-zugeordnete-funkgeraetetype-s-3": dem_adapter_zugeordnete_funkgeraetetype_s_3,
       "eingabe-und-anzeigemodul-s-3": eingabe_und_anzeigemodul_s_3,
       "mod-bus-verbindung-module-s-3": mod_bus_verbindung_module_s_3,
       "gemessene-sendeleistung-im-testmode-s-3": gemessene_sendeleistung_im_testmode_s_3,
       "aktuelle-sendeleistung-s-3": aktuelle_sendeleistung_s_3,
       "gemessene-reflexion-im-testmode-s-3": gemessene_reflexion_im_testmode_s_3,
       "aktuelle-reflexion-s-3": aktuelle_reflexion_s_3,
       "letzte-gemessene-donor-sendeleistung-s-3": letzte_gemessene_donor_sendeleistung_s_3,
       "aktuelle-donor-sendeleistung-s-3": aktuelle_donor_sendeleistung_s_3,
       "letzte-gemessene-donor-reflexion-s-3": letzte_gemessene_donor_reflexion_s_3,
       "aktuelle-donor-reflexion-s-3": aktuelle_donor_reflexion_s_3,
       "anzahl-gemessener-praesenzsignale-im-testmode-s-3": anzahl_gemessener_praesenzsignale_im_testmode_s_3,
       "aktuelle-ausgangsspannung-ub-s-3": aktuelle_ausgangsspannung_ub_s_3,
       "aktuelle-ausgangsspannung-u1-s-3": aktuelle_ausgangsspannung_u1_s_3,
       "aktuelle-ausgangsspannung-u2-s-3": aktuelle_ausgangsspannung_u2_s_3,
       "aktuelle-ausgangsspannung-u3-s-3": aktuelle_ausgangsspannung_u3_s_3,
       "aktuelle-ausgangsspannung-u4-s-3": aktuelle_ausgangsspannung_u4_s_3,
       "aktuelle-ausgangsspannung-u5-s-3": aktuelle_ausgangsspannung_u5_s_3,
       "aktuelle-ausgangsspannung-u6-s-3": aktuelle_ausgangsspannung_u6_s_3,
       "aktuelle-ausgangsspannung-u7-s-3": aktuelle_ausgangsspannung_u7_s_3,
       "aktuelle-ausgangsspannung-u8-s-3": aktuelle_ausgangsspannung_u8_s_3,
       "aktuelle-ladespannung-an-akku-kreis-1-s-3": aktuelle_ladespannung_an_akku_kreis_1_s_3,
       "aktuelle-ladespannung-an-akku-Kreis-2-s-3": aktuelle_ladespannung_an_akku_Kreis_2_s_3,
       "aktuelle-ladespannung-an-akku-Kreis-3-s-3": aktuelle_ladespannung_an_akku_Kreis_3_s_3,
       "aktuelle-ladespannung-an-akku-kreis-4-s-3": aktuelle_ladespannung_an_akku_kreis_4_s_3,
       "aktuelle-ladespannung-an-akku-kreis-5-s-3": aktuelle_ladespannung_an_akku_kreis_5_s_3,
       "aktuelle-ladespannung-an-akku-kreis-6-s-3": aktuelle_ladespannung_an_akku_kreis_6_s_3,
       "aktuelle-ladespannung-an-akku-kreis-7-s-3": aktuelle_ladespannung_an_akku_kreis_7_s_3,
       "aktuelle-ladespannung-an-akku-kreis-8-s-3": aktuelle_ladespannung_an_akku_kreis_8_s_3,
       "aktuelle-spannung-an-akku-kreis-1-s-3": aktuelle_spannung_an_akku_kreis_1_s_3,
       "aktuelle-spannung-an-akku-kreis-2-s-3": aktuelle_spannung_an_akku_kreis_2_s_3,
       "aktuelle-spannung-an-akku-kreis-3-s-3": aktuelle_spannung_an_akku_kreis_3_s_3,
       "aktuelle-spannung-an-akku-kreis-4-s-3": aktuelle_spannung_an_akku_kreis_4_s_3,
       "aktuelle-spannung-an-akku-reis-5-s-3": aktuelle_spannung_an_akku_reis_5_s_3,
       "aktuelle-spannung-an-akku-kreis-6-s-3": aktuelle_spannung_an_akku_kreis_6_s_3,
       "aktuelle-spannung-an-akku-kreis-7-s-3": aktuelle_spannung_an_akku_kreis_7_s_3,
       "aktuelle-spannung-an-akku-kreis-8-s-3": aktuelle_spannung_an_akku_kreis_8_s_3,
       "testergebnis-lastspannung-an-akku-reis-1-s-3": testergebnis_lastspannung_an_akku_reis_1_s_3,
       "testergebnis-lastspannung-an-akku-kreis-2-s-3": testergebnis_lastspannung_an_akku_kreis_2_s_3,
       "testergebnis-lastspannung-an-akku-kreis-3-s-3": testergebnis_lastspannung_an_akku_kreis_3_s_3,
       "testergebnis-lastspannung-an-akku-kreis-4-s-3": testergebnis_lastspannung_an_akku_kreis_4_s_3,
       "testergebnis-lastspannung-an-akku-kreis-5-s-3": testergebnis_lastspannung_an_akku_kreis_5_s_3,
       "testergebnis-lastspannung-an-akku-kreis-6-s-3": testergebnis_lastspannung_an_akku_kreis_6_s_3,
       "testergebnis-lastspannung-an-akku-kreis-7-s-3": testergebnis_lastspannung_an_akku_kreis_7_s_3,
       "testergebnis-lastspannung-an-akku-kreis-8-s-3": testergebnis_lastspannung_an_akku_kreis_8_s_3,
       "testergebnis-innenwiderstand-akku-kreis-1-s-3": testergebnis_innenwiderstand_akku_kreis_1_s_3,
       "testergebnis-innenwiderstand-akku-kreis-2-s-3": testergebnis_innenwiderstand_akku_kreis_2_s_3,
       "testergebnis-innenwiderstand-akku-kreis-3-s-3": testergebnis_innenwiderstand_akku_kreis_3_s_3,
       "testergebnis-innenwiderstand-akku-kreis-4-s-3": testergebnis_innenwiderstand_akku_kreis_4_s_3,
       "testergebnis-innenwiderstand-akku-kreis-5-s-3": testergebnis_innenwiderstand_akku_kreis_5_s_3,
       "testergebnis-innenwiderstand-akku-kreis-6-s-3": testergebnis_innenwiderstand_akku_kreis_6_s_3,
       "testergebnis-innenwiderstand-akku-kreis-7-s-3": testergebnis_innenwiderstand_akku_kreis_7_s_3,
       "testergebnis-innenwiderstand-akku-kreis-8-s-3": testergebnis_innenwiderstand_akku_kreis_8_s_3,
       "netzteilspannung-uin1-s-3": netzteilspannung_uin1_s_3,
       "netzteilspannung-uin2-s-3": netzteilspannung_uin2_s_3,
       "programmierte-minimale-soll-sendeleistung-s-3": programmierte_minimale_soll_sendeleistung_s_3,
       "programmierte-maximale-antennen-reflexion-s-3": programmierte_maximale_antennen_reflexion_s_3,
       "programmierte-minimale-anzahl-praesenzsignale-s-3": programmierte_minimale_anzahl_praesenzsignale_s_3,
       "summen-fehlerstatus-von-tmoa-anlage-s-3": summen_fehlerstatus_von_tmoa_anlage_s_3,
       "summen-fehlerstatus-von-anbinderepeater-s-3": summen_fehlerstatus_von_anbinderepeater_s_3,
       "summen-fehlerstatus-von-analogem-repeater-s-3": summen_fehlerstatus_von_analogem_repeater_s_3,
       "aktuelle-ladespannung-akku-kreis-1-int-sicherung-defekt-s-3": aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_3,
       "aktuelle-ladespannung-akku-kreis-2-int-sicherung-defekt-s-3": aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_3,
       "aktuelle-ladespannung-akku-kreis-3-int-sicherung-defekt-s-3": aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_3,
       "aktuelle-ladespannung-akku-kreis-4-int-sicherung-defekt-s-3": aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_3,
       "aktuelle-ladespannung-akku-kreis-5-int-sicherung-defekt-s-3": aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_3,
       "aktuelle-ladespannung-akku-kreis-6-int-sicherung-defekt-s-3": aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_3,
       "aktuelle-ladespannung-akku-kreis-7-int-sicherung-defekt-s-3": aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_3,
       "aktuelle-ladespannung-akku-kreis-8-int-sicherung-defekt-s-3": aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_3,
       "netzspannungsversorgung-von-tmoa-anlage-s-3": netzspannungsversorgung_von_tmoa_anlage_s_3,
       "netzspannungsversorgung-von-anbinderepeater-s-3": netzspannungsversorgung_von_anbinderepeater_s_3,
       "fgb-id1-verbindungsstatus-s-3": fgb_id1_verbindungsstatus_s_3,
       "fgb-id2-verbindungsstatus-s-3": fgb_id2_verbindungsstatus_s_3,
       "fgb-id3-verbindungsstatus-s-3": fgb_id3_verbindungsstatus_s_3,
       "fgb-id4-verbindungsstatus-s-3": fgb_id4_verbindungsstatus_s_3,
       "fgb-id5-verbindungsstatus-s-3": fgb_id5_verbindungsstatus_s_3,
       "fgb-id6-verbindungsstatus-s-3": fgb_id6_verbindungsstatus_s_3,
       "fgb-id7-verbindungsstatus-s-3": fgb_id7_verbindungsstatus_s_3,
       "fgb-id8-verbindungsstatus-s-3": fgb_id8_verbindungsstatus_s_3,
       "fgb-id9-verbindungsstatus-s-3": fgb_id9_verbindungsstatus_s_3,
       "fgb-id10-verbindungsstatus-s-3": fgb_id10_verbindungsstatus_s_3,
       "fgb-id11-verbindungsstatus-s-3": fgb_id11_verbindungsstatus_s_3,
       "mod-bus-verbindungsstatus-s-3": mod_bus_verbindungsstatus_s_3,
       "fgb-bus-verbindungsstatus-s-3": fgb_bus_verbindungsstatus_s_3,
       "slave-bus-verbindungsstatus-s-3": slave_bus_verbindungsstatus_s_3,
       "gsm-modem-verbindungsstatus-s-3": gsm_modem_verbindungsstatus_s_3,
       "gsm-modem-sim-karte-s-3": gsm_modem_sim_karte_s_3,
       "gsm-modem-pin-nummer-s-3": gsm_modem_pin_nummer_s_3,
       "gsm-modem-provider-service-s-3": gsm_modem_provider_service_s_3,
       "gsm-modem-empfangspegel-s-3": gsm_modem_empfangspegel_s_3,
       "lte-router-verbindungsstatus-s-3": lte_router_verbindungsstatus_s_3,
       "lte-router-provider-service-s-3": lte_router_provider_service_s_3,
       "lte-router-empfangspegel-s-3": lte_router_empfangspegel_s_3,
       "antennenleitungsueberwachung-1-s-3": antennenleitungsueberwachung_1_s_3,
       "antennenleitungsueberwachung-2-s-3": antennenleitungsueberwachung_2_s_3,
       "antennenleitungseuberwachung-3-s-3": antennenleitungseuberwachung_3_s_3,
       "interne-temperaturuebwerwachung-s-3": interne_temperaturuebwerwachung_s_3,
       "stoerueberwachung-optisches-verteilsystem-1-s-3": stoerueberwachung_optisches_verteilsystem_1_s_3,
       "stoerueberwachung-optisches-verteilsystem-2-s-3": stoerueberwachung_optisches_verteilsystem_2_s_3,
       "lte-router-sim-karte-s-3": lte_router_sim_karte_s_3,
       "lte-router-pin-nummer-s-3": lte_router_pin_nummer_s_3,
       "ak-slave-4-i": ak_slave_4_i,
       "modulTable-s-4": modulTable_s_4,
       "modulEntry-s-4": modulEntry_s_4,
       "modulIndex-s-4": modulIndex_s_4,
       "geraete-typ-s-4": geraete_typ_s_4,
       "betriebsstatus-s-4": betriebsstatus_s_4,
       "senderstatus-s-4": senderstatus_s_4,
       "fehlerstatus-s-4": fehlerstatus_s_4,
       "dem-adapter-zugeordnete-funkgeraetetype-s-4": dem_adapter_zugeordnete_funkgeraetetype_s_4,
       "eingabe-und-anzeigemodul-s-4": eingabe_und_anzeigemodul_s_4,
       "mod-bus-verbindung-module-s-4": mod_bus_verbindung_module_s_4,
       "gemessene-sendeleistung-im-testmode-s-4": gemessene_sendeleistung_im_testmode_s_4,
       "aktuelle-sendeleistung-s-4": aktuelle_sendeleistung_s_4,
       "gemessene-reflexion-im-testmode-s-4": gemessene_reflexion_im_testmode_s_4,
       "aktuelle-reflexion-s-4": aktuelle_reflexion_s_4,
       "letzte-gemessene-donor-sendeleistung-s-4": letzte_gemessene_donor_sendeleistung_s_4,
       "aktuelle-donor-sendeleistung-s-4": aktuelle_donor_sendeleistung_s_4,
       "letzte-gemessene-donor-reflexion-s-4": letzte_gemessene_donor_reflexion_s_4,
       "aktuelle-donor-reflexion-s-4": aktuelle_donor_reflexion_s_4,
       "anzahl-gemessener-praesenzsignale-im-testmode-s-4": anzahl_gemessener_praesenzsignale_im_testmode_s_4,
       "aktuelle-ausgangsspannung-ub-s-4": aktuelle_ausgangsspannung_ub_s_4,
       "aktuelle-ausgangsspannung-u1-s-4": aktuelle_ausgangsspannung_u1_s_4,
       "aktuelle-ausgangsspannung-u2-s-4": aktuelle_ausgangsspannung_u2_s_4,
       "aktuelle-ausgangsspannung-u3-s-4": aktuelle_ausgangsspannung_u3_s_4,
       "aktuelle-ausgangsspannung-u4-s-4": aktuelle_ausgangsspannung_u4_s_4,
       "aktuelle-ausgangsspannung-u5-s-4": aktuelle_ausgangsspannung_u5_s_4,
       "aktuelle-ausgangsspannung-u6-s-4": aktuelle_ausgangsspannung_u6_s_4,
       "aktuelle-ausgangsspannung-u7-s-4": aktuelle_ausgangsspannung_u7_s_4,
       "aktuelle-ausgangsspannung-u8-s-4": aktuelle_ausgangsspannung_u8_s_4,
       "aktuelle-ladespannung-an-akku-kreis-1-s-4": aktuelle_ladespannung_an_akku_kreis_1_s_4,
       "aktuelle-ladespannung-an-akku-Kreis-2-s-4": aktuelle_ladespannung_an_akku_Kreis_2_s_4,
       "aktuelle-ladespannung-an-akku-Kreis-3-s-4": aktuelle_ladespannung_an_akku_Kreis_3_s_4,
       "aktuelle-ladespannung-an-akku-kreis-4-s-4": aktuelle_ladespannung_an_akku_kreis_4_s_4,
       "aktuelle-ladespannung-an-akku-kreis-5-s-4": aktuelle_ladespannung_an_akku_kreis_5_s_4,
       "aktuelle-ladespannung-an-akku-kreis-6-s-4": aktuelle_ladespannung_an_akku_kreis_6_s_4,
       "aktuelle-ladespannung-an-akku-kreis-7-s-4": aktuelle_ladespannung_an_akku_kreis_7_s_4,
       "aktuelle-ladespannung-an-akku-kreis-8-s-4": aktuelle_ladespannung_an_akku_kreis_8_s_4,
       "aktuelle-spannung-an-akku-kreis-1-s-4": aktuelle_spannung_an_akku_kreis_1_s_4,
       "aktuelle-spannung-an-akku-kreis-2-s-4": aktuelle_spannung_an_akku_kreis_2_s_4,
       "aktuelle-spannung-an-akku-kreis-3-s-4": aktuelle_spannung_an_akku_kreis_3_s_4,
       "aktuelle-spannung-an-akku-kreis-4-s-4": aktuelle_spannung_an_akku_kreis_4_s_4,
       "aktuelle-spannung-an-akku-reis-5-s-4": aktuelle_spannung_an_akku_reis_5_s_4,
       "aktuelle-spannung-an-akku-kreis-6-s-4": aktuelle_spannung_an_akku_kreis_6_s_4,
       "aktuelle-spannung-an-akku-kreis-7-s-4": aktuelle_spannung_an_akku_kreis_7_s_4,
       "aktuelle-spannung-an-akku-kreis-8-s-4": aktuelle_spannung_an_akku_kreis_8_s_4,
       "testergebnis-lastspannung-an-akku-reis-1-s-4": testergebnis_lastspannung_an_akku_reis_1_s_4,
       "testergebnis-lastspannung-an-akku-kreis-2-s-4": testergebnis_lastspannung_an_akku_kreis_2_s_4,
       "testergebnis-lastspannung-an-akku-kreis-3-s-4": testergebnis_lastspannung_an_akku_kreis_3_s_4,
       "testergebnis-lastspannung-an-akku-kreis-4-s-4": testergebnis_lastspannung_an_akku_kreis_4_s_4,
       "testergebnis-lastspannung-an-akku-kreis-5-s-4": testergebnis_lastspannung_an_akku_kreis_5_s_4,
       "testergebnis-lastspannung-an-akku-kreis-6-s-4": testergebnis_lastspannung_an_akku_kreis_6_s_4,
       "testergebnis-lastspannung-an-akku-kreis-7-s-4": testergebnis_lastspannung_an_akku_kreis_7_s_4,
       "testergebnis-lastspannung-an-akku-kreis-8-s-4": testergebnis_lastspannung_an_akku_kreis_8_s_4,
       "testergebnis-innenwiderstand-akku-kreis-1-s-4": testergebnis_innenwiderstand_akku_kreis_1_s_4,
       "testergebnis-innenwiderstand-akku-kreis-2-s-4": testergebnis_innenwiderstand_akku_kreis_2_s_4,
       "testergebnis-innenwiderstand-akku-kreis-3-s-4": testergebnis_innenwiderstand_akku_kreis_3_s_4,
       "testergebnis-innenwiderstand-akku-kreis-4-s-4": testergebnis_innenwiderstand_akku_kreis_4_s_4,
       "testergebnis-innenwiderstand-akku-kreis-5-s-4": testergebnis_innenwiderstand_akku_kreis_5_s_4,
       "testergebnis-innenwiderstand-akku-kreis-6-s-4": testergebnis_innenwiderstand_akku_kreis_6_s_4,
       "testergebnis-innenwiderstand-akku-kreis-7-s-4": testergebnis_innenwiderstand_akku_kreis_7_s_4,
       "testergebnis-innenwiderstand-akku-kreis-8-s-4": testergebnis_innenwiderstand_akku_kreis_8_s_4,
       "netzteilspannung-uin1-s-4": netzteilspannung_uin1_s_4,
       "netzteilspannung-uin2-s-4": netzteilspannung_uin2_s_4,
       "programmierte-minimale-soll-sendeleistung-s-4": programmierte_minimale_soll_sendeleistung_s_4,
       "programmierte-maximale-antennen-reflexion-s-4": programmierte_maximale_antennen_reflexion_s_4,
       "programmierte-minimale-anzahl-praesenzsignale-s-4": programmierte_minimale_anzahl_praesenzsignale_s_4,
       "summen-fehlerstatus-von-tmoa-anlage-s-4": summen_fehlerstatus_von_tmoa_anlage_s_4,
       "summen-fehlerstatus-von-anbinderepeater-s-4": summen_fehlerstatus_von_anbinderepeater_s_4,
       "summen-fehlerstatus-von-analogem-repeater-s-4": summen_fehlerstatus_von_analogem_repeater_s_4,
       "aktuelle-ladespannung-akku-kreis-1-int-sicherung-defekt-s-4": aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_4,
       "aktuelle-ladespannung-akku-kreis-2-int-sicherung-defekt-s-4": aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_4,
       "aktuelle-ladespannung-akku-kreis-3-int-sicherung-defekt-s-4": aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_4,
       "aktuelle-ladespannung-akku-kreis-4-int-sicherung-defekt-s-4": aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_4,
       "aktuelle-ladespannung-akku-kreis-5-int-sicherung-defekt-s-4": aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_4,
       "aktuelle-ladespannung-akku-kreis-6-int-sicherung-defekt-s-4": aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_4,
       "aktuelle-ladespannung-akku-kreis-7-int-sicherung-defekt-s-4": aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_4,
       "aktuelle-ladespannung-akku-kreis-8-int-sicherung-defekt-s-4": aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_4,
       "netzspannungsversorgung-von-tmoa-anlage-s-4": netzspannungsversorgung_von_tmoa_anlage_s_4,
       "netzspannungsversorgung-von-anbinderepeater-s-4": netzspannungsversorgung_von_anbinderepeater_s_4,
       "fgb-id1-verbindungsstatus-s-4": fgb_id1_verbindungsstatus_s_4,
       "fgb-id2-verbindungsstatus-s-4": fgb_id2_verbindungsstatus_s_4,
       "fgb-id3-verbindungsstatus-s-4": fgb_id3_verbindungsstatus_s_4,
       "fgb-id4-verbindungsstatus-s-4": fgb_id4_verbindungsstatus_s_4,
       "fgb-id5-verbindungsstatus-s-4": fgb_id5_verbindungsstatus_s_4,
       "fgb-id6-verbindungsstatus-s-4": fgb_id6_verbindungsstatus_s_4,
       "fgb-id7-verbindungsstatus-s-4": fgb_id7_verbindungsstatus_s_4,
       "fgb-id8-verbindungsstatus-s-4": fgb_id8_verbindungsstatus_s_4,
       "fgb-id9-verbindungsstatus-s-4": fgb_id9_verbindungsstatus_s_4,
       "fgb-id10-verbindungsstatus-s-4": fgb_id10_verbindungsstatus_s_4,
       "fgb-id11-verbindungsstatus-s-4": fgb_id11_verbindungsstatus_s_4,
       "mod-bus-verbindungsstatus-s-4": mod_bus_verbindungsstatus_s_4,
       "fgb-bus-verbindungsstatus-s-4": fgb_bus_verbindungsstatus_s_4,
       "slave-bus-verbindungsstatus-s-4": slave_bus_verbindungsstatus_s_4,
       "gsm-modem-verbindungsstatus-s-4": gsm_modem_verbindungsstatus_s_4,
       "gsm-modem-sim-karte-s-4": gsm_modem_sim_karte_s_4,
       "gsm-modem-pin-nummer-s-4": gsm_modem_pin_nummer_s_4,
       "gsm-modem-provider-service-s-4": gsm_modem_provider_service_s_4,
       "gsm-modem-empfangspegel-s-4": gsm_modem_empfangspegel_s_4,
       "lte-router-verbindungsstatus-s-4": lte_router_verbindungsstatus_s_4,
       "lte-router-provider-service-s-4": lte_router_provider_service_s_4,
       "lte-router-empfangspegel-s-4": lte_router_empfangspegel_s_4,
       "antennenleitungsueberwachung-1-s-4": antennenleitungsueberwachung_1_s_4,
       "antennenleitungsueberwachung-2-s-4": antennenleitungsueberwachung_2_s_4,
       "antennenleitungseuberwachung-3-s-4": antennenleitungseuberwachung_3_s_4,
       "interne-temperaturuebwerwachung-s-4": interne_temperaturuebwerwachung_s_4,
       "stoerueberwachung-optisches-verteilsystem-1-s-4": stoerueberwachung_optisches_verteilsystem_1_s_4,
       "stoerueberwachung-optisches-verteilsystem-2-s-4": stoerueberwachung_optisches_verteilsystem_2_s_4,
       "lte-router-sim-karte-s-4": lte_router_sim_karte_s_4,
       "lte-router-pin-nummer-s-4": lte_router_pin_nummer_s_4,
       "ak-slave-5-i": ak_slave_5_i,
       "modulTable-s-5": modulTable_s_5,
       "modulEntry-s-5": modulEntry_s_5,
       "modulIndex-s-5": modulIndex_s_5,
       "geraete-typ-s-5": geraete_typ_s_5,
       "betriebsstatus-s-5": betriebsstatus_s_5,
       "senderstatus-s-5": senderstatus_s_5,
       "fehlerstatus-s-5": fehlerstatus_s_5,
       "dem-adapter-zugeordnete-funkgeraetetype-s-5": dem_adapter_zugeordnete_funkgeraetetype_s_5,
       "eingabe-und-anzeigemodul-s-5": eingabe_und_anzeigemodul_s_5,
       "mod-bus-verbindung-module-s-5": mod_bus_verbindung_module_s_5,
       "gemessene-sendeleistung-im-testmode-s-5": gemessene_sendeleistung_im_testmode_s_5,
       "aktuelle-sendeleistung-s-5": aktuelle_sendeleistung_s_5,
       "gemessene-reflexion-im-testmode-s-5": gemessene_reflexion_im_testmode_s_5,
       "aktuelle-reflexion-s-5": aktuelle_reflexion_s_5,
       "letzte-gemessene-donor-sendeleistung-s-5": letzte_gemessene_donor_sendeleistung_s_5,
       "aktuelle-donor-sendeleistung-s-5": aktuelle_donor_sendeleistung_s_5,
       "letzte-gemessene-donor-reflexion-s-5": letzte_gemessene_donor_reflexion_s_5,
       "aktuelle-donor-reflexion-s-5": aktuelle_donor_reflexion_s_5,
       "anzahl-gemessener-praesenzsignale-im-testmode-s-5": anzahl_gemessener_praesenzsignale_im_testmode_s_5,
       "aktuelle-ausgangsspannung-ub-s-5": aktuelle_ausgangsspannung_ub_s_5,
       "aktuelle-ausgangsspannung-u1-s-5": aktuelle_ausgangsspannung_u1_s_5,
       "aktuelle-ausgangsspannung-u2-s-5": aktuelle_ausgangsspannung_u2_s_5,
       "aktuelle-ausgangsspannung-u3-s-5": aktuelle_ausgangsspannung_u3_s_5,
       "aktuelle-ausgangsspannung-u4-s-5": aktuelle_ausgangsspannung_u4_s_5,
       "aktuelle-ausgangsspannung-u5-s-5": aktuelle_ausgangsspannung_u5_s_5,
       "aktuelle-ausgangsspannung-u6-s-5": aktuelle_ausgangsspannung_u6_s_5,
       "aktuelle-ausgangsspannung-u7-s-5": aktuelle_ausgangsspannung_u7_s_5,
       "aktuelle-ausgangsspannung-u8-s-5": aktuelle_ausgangsspannung_u8_s_5,
       "aktuelle-ladespannung-an-akku-kreis-1-s-5": aktuelle_ladespannung_an_akku_kreis_1_s_5,
       "aktuelle-ladespannung-an-akku-Kreis-2-s-5": aktuelle_ladespannung_an_akku_Kreis_2_s_5,
       "aktuelle-ladespannung-an-akku-Kreis-3-s-5": aktuelle_ladespannung_an_akku_Kreis_3_s_5,
       "aktuelle-ladespannung-an-akku-kreis-4-s-5": aktuelle_ladespannung_an_akku_kreis_4_s_5,
       "aktuelle-ladespannung-an-akku-kreis-5-s-5": aktuelle_ladespannung_an_akku_kreis_5_s_5,
       "aktuelle-ladespannung-an-akku-kreis-6-s-5": aktuelle_ladespannung_an_akku_kreis_6_s_5,
       "aktuelle-ladespannung-an-akku-kreis-7-s-5": aktuelle_ladespannung_an_akku_kreis_7_s_5,
       "aktuelle-ladespannung-an-akku-kreis-8-s-5": aktuelle_ladespannung_an_akku_kreis_8_s_5,
       "aktuelle-spannung-an-akku-kreis-1-s-5": aktuelle_spannung_an_akku_kreis_1_s_5,
       "aktuelle-spannung-an-akku-kreis-2-s-5": aktuelle_spannung_an_akku_kreis_2_s_5,
       "aktuelle-spannung-an-akku-kreis-3-s-5": aktuelle_spannung_an_akku_kreis_3_s_5,
       "aktuelle-spannung-an-akku-kreis-4-s-5": aktuelle_spannung_an_akku_kreis_4_s_5,
       "aktuelle-spannung-an-akku-reis-5-s-5": aktuelle_spannung_an_akku_reis_5_s_5,
       "aktuelle-spannung-an-akku-kreis-6-s-5": aktuelle_spannung_an_akku_kreis_6_s_5,
       "aktuelle-spannung-an-akku-kreis-7-s-5": aktuelle_spannung_an_akku_kreis_7_s_5,
       "aktuelle-spannung-an-akku-kreis-8-s-5": aktuelle_spannung_an_akku_kreis_8_s_5,
       "testergebnis-lastspannung-an-akku-reis-1-s-5": testergebnis_lastspannung_an_akku_reis_1_s_5,
       "testergebnis-lastspannung-an-akku-kreis-2-s-5": testergebnis_lastspannung_an_akku_kreis_2_s_5,
       "testergebnis-lastspannung-an-akku-kreis-3-s-5": testergebnis_lastspannung_an_akku_kreis_3_s_5,
       "testergebnis-lastspannung-an-akku-kreis-4-s-5": testergebnis_lastspannung_an_akku_kreis_4_s_5,
       "testergebnis-lastspannung-an-akku-kreis-5-s-5": testergebnis_lastspannung_an_akku_kreis_5_s_5,
       "testergebnis-lastspannung-an-akku-kreis-6-s-5": testergebnis_lastspannung_an_akku_kreis_6_s_5,
       "testergebnis-lastspannung-an-akku-kreis-7-s-5": testergebnis_lastspannung_an_akku_kreis_7_s_5,
       "testergebnis-lastspannung-an-akku-kreis-8-s-5": testergebnis_lastspannung_an_akku_kreis_8_s_5,
       "testergebnis-innenwiderstand-akku-kreis-1-s-5": testergebnis_innenwiderstand_akku_kreis_1_s_5,
       "testergebnis-innenwiderstand-akku-kreis-2-s-5": testergebnis_innenwiderstand_akku_kreis_2_s_5,
       "testergebnis-innenwiderstand-akku-kreis-3-s-5": testergebnis_innenwiderstand_akku_kreis_3_s_5,
       "testergebnis-innenwiderstand-akku-kreis-4-s-5": testergebnis_innenwiderstand_akku_kreis_4_s_5,
       "testergebnis-innenwiderstand-akku-kreis-5-s-5": testergebnis_innenwiderstand_akku_kreis_5_s_5,
       "testergebnis-innenwiderstand-akku-kreis-6-s-5": testergebnis_innenwiderstand_akku_kreis_6_s_5,
       "testergebnis-innenwiderstand-akku-kreis-7-s-5": testergebnis_innenwiderstand_akku_kreis_7_s_5,
       "testergebnis-innenwiderstand-akku-kreis-8-s-5": testergebnis_innenwiderstand_akku_kreis_8_s_5,
       "netzteilspannung-uin1-s-5": netzteilspannung_uin1_s_5,
       "netzteilspannung-uin2-s-5": netzteilspannung_uin2_s_5,
       "programmierte-minimale-soll-sendeleistung-s-5": programmierte_minimale_soll_sendeleistung_s_5,
       "programmierte-maximale-antennen-reflexion-s-5": programmierte_maximale_antennen_reflexion_s_5,
       "programmierte-minimale-anzahl-praesenzsignale-s-5": programmierte_minimale_anzahl_praesenzsignale_s_5,
       "summen-fehlerstatus-von-tmoa-anlage-s-5": summen_fehlerstatus_von_tmoa_anlage_s_5,
       "summen-fehlerstatus-von-anbinderepeater-s-5": summen_fehlerstatus_von_anbinderepeater_s_5,
       "summen-fehlerstatus-von-analogem-repeater-s-5": summen_fehlerstatus_von_analogem_repeater_s_5,
       "aktuelle-ladespannung-akku-kreis-1-int-sicherung-defekt-s-5": aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_5,
       "aktuelle-ladespannung-akku-kreis-2-int-sicherung-defekt-s-5": aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_5,
       "aktuelle-ladespannung-akku-kreis-3-int-sicherung-defekt-s-5": aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_5,
       "aktuelle-ladespannung-akku-kreis-4-int-sicherung-defekt-s-5": aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_5,
       "aktuelle-ladespannung-akku-kreis-5-int-sicherung-defekt-s-5": aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_5,
       "aktuelle-ladespannung-akku-kreis-6-int-sicherung-defekt-s-5": aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_5,
       "aktuelle-ladespannung-akku-kreis-7-int-sicherung-defekt-s-5": aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_5,
       "aktuelle-ladespannung-akku-kreis-8-int-sicherung-defekt-s-5": aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_5,
       "netzspannungsversorgung-von-tmoa-anlage-s-5": netzspannungsversorgung_von_tmoa_anlage_s_5,
       "netzspannungsversorgung-von-anbinderepeater-s-5": netzspannungsversorgung_von_anbinderepeater_s_5,
       "fgb-id1-verbindungsstatus-s-5": fgb_id1_verbindungsstatus_s_5,
       "fgb-id2-verbindungsstatus-s-5": fgb_id2_verbindungsstatus_s_5,
       "fgb-id3-verbindungsstatus-s-5": fgb_id3_verbindungsstatus_s_5,
       "fgb-id4-verbindungsstatus-s-5": fgb_id4_verbindungsstatus_s_5,
       "fgb-id5-verbindungsstatus-s-5": fgb_id5_verbindungsstatus_s_5,
       "fgb-id6-verbindungsstatus-s-5": fgb_id6_verbindungsstatus_s_5,
       "fgb-id7-verbindungsstatus-s-5": fgb_id7_verbindungsstatus_s_5,
       "fgb-id8-verbindungsstatus-s-5": fgb_id8_verbindungsstatus_s_5,
       "fgb-id9-verbindungsstatus-s-5": fgb_id9_verbindungsstatus_s_5,
       "fgb-id10-verbindungsstatus-s-5": fgb_id10_verbindungsstatus_s_5,
       "fgb-id11-verbindungsstatus-s-5": fgb_id11_verbindungsstatus_s_5,
       "mod-bus-verbindungsstatus-s-5": mod_bus_verbindungsstatus_s_5,
       "fgb-bus-verbindungsstatus-s-5": fgb_bus_verbindungsstatus_s_5,
       "slave-bus-verbindungsstatus-s-5": slave_bus_verbindungsstatus_s_5,
       "gsm-modem-verbindungsstatus-s-5": gsm_modem_verbindungsstatus_s_5,
       "gsm-modem-sim-karte-s-5": gsm_modem_sim_karte_s_5,
       "gsm-modem-pin-nummer-s-5": gsm_modem_pin_nummer_s_5,
       "gsm-modem-provider-service-s-5": gsm_modem_provider_service_s_5,
       "gsm-modem-empfangspegel-s-5": gsm_modem_empfangspegel_s_5,
       "lte-router-verbindungsstatus-s-5": lte_router_verbindungsstatus_s_5,
       "lte-router-provider-service-s-5": lte_router_provider_service_s_5,
       "lte-router-empfangspegel-s-5": lte_router_empfangspegel_s_5,
       "antennenleitungsueberwachung-1-s-5": antennenleitungsueberwachung_1_s_5,
       "antennenleitungsueberwachung-2-s-5": antennenleitungsueberwachung_2_s_5,
       "antennenleitungseuberwachung-3-s-5": antennenleitungseuberwachung_3_s_5,
       "interne-temperaturuebwerwachung-s-5": interne_temperaturuebwerwachung_s_5,
       "stoerueberwachung-optisches-verteilsystem-1-s-5": stoerueberwachung_optisches_verteilsystem_1_s_5,
       "stoerueberwachung-optisches-verteilsystem-2-s-5": stoerueberwachung_optisches_verteilsystem_2_s_5,
       "lte-router-sim-karte-s-5": lte_router_sim_karte_s_5,
       "lte-router-pin-nummer-s-5": lte_router_pin_nummer_s_5,
       "ak-slave-6-i": ak_slave_6_i,
       "modulTable-s-6": modulTable_s_6,
       "modulEntry-s-6": modulEntry_s_6,
       "modulIndex-s-6": modulIndex_s_6,
       "geraete-typ-s-6": geraete_typ_s_6,
       "betriebsstatus-s-6": betriebsstatus_s_6,
       "senderstatus-s-6": senderstatus_s_6,
       "fehlerstatus-s-6": fehlerstatus_s_6,
       "dem-adapter-zugeordnete-funkgeraetetype-s-6": dem_adapter_zugeordnete_funkgeraetetype_s_6,
       "eingabe-und-anzeigemodul-s-6": eingabe_und_anzeigemodul_s_6,
       "mod-bus-verbindung-module-s-6": mod_bus_verbindung_module_s_6,
       "gemessene-sendeleistung-im-testmode-s-6": gemessene_sendeleistung_im_testmode_s_6,
       "aktuelle-sendeleistung-s-6": aktuelle_sendeleistung_s_6,
       "gemessene-reflexion-im-testmode-s-6": gemessene_reflexion_im_testmode_s_6,
       "aktuelle-reflexion-s-6": aktuelle_reflexion_s_6,
       "letzte-gemessene-donor-sendeleistung-s-6": letzte_gemessene_donor_sendeleistung_s_6,
       "aktuelle-donor-sendeleistung-s-6": aktuelle_donor_sendeleistung_s_6,
       "letzte-gemessene-donor-reflexion-s-6": letzte_gemessene_donor_reflexion_s_6,
       "aktuelle-donor-reflexion-s-6": aktuelle_donor_reflexion_s_6,
       "anzahl-gemessener-praesenzsignale-im-testmode-s-6": anzahl_gemessener_praesenzsignale_im_testmode_s_6,
       "aktuelle-ausgangsspannung-ub-s-6": aktuelle_ausgangsspannung_ub_s_6,
       "aktuelle-ausgangsspannung-u1-s-6": aktuelle_ausgangsspannung_u1_s_6,
       "aktuelle-ausgangsspannung-u2-s-6": aktuelle_ausgangsspannung_u2_s_6,
       "aktuelle-ausgangsspannung-u3-s-6": aktuelle_ausgangsspannung_u3_s_6,
       "aktuelle-ausgangsspannung-u4-s-6": aktuelle_ausgangsspannung_u4_s_6,
       "aktuelle-ausgangsspannung-u5-s-6": aktuelle_ausgangsspannung_u5_s_6,
       "aktuelle-ausgangsspannung-u6-s-6": aktuelle_ausgangsspannung_u6_s_6,
       "aktuelle-ausgangsspannung-u7-s-6": aktuelle_ausgangsspannung_u7_s_6,
       "aktuelle-ausgangsspannung-u8-s-6": aktuelle_ausgangsspannung_u8_s_6,
       "aktuelle-ladespannung-an-akku-kreis-1-s-6": aktuelle_ladespannung_an_akku_kreis_1_s_6,
       "aktuelle-ladespannung-an-akku-Kreis-2-s-6": aktuelle_ladespannung_an_akku_Kreis_2_s_6,
       "aktuelle-ladespannung-an-akku-Kreis-3-s-6": aktuelle_ladespannung_an_akku_Kreis_3_s_6,
       "aktuelle-ladespannung-an-akku-kreis-4-s-6": aktuelle_ladespannung_an_akku_kreis_4_s_6,
       "aktuelle-ladespannung-an-akku-kreis-5-s-6": aktuelle_ladespannung_an_akku_kreis_5_s_6,
       "aktuelle-ladespannung-an-akku-kreis-6-s-6": aktuelle_ladespannung_an_akku_kreis_6_s_6,
       "aktuelle-ladespannung-an-akku-kreis-7-s-6": aktuelle_ladespannung_an_akku_kreis_7_s_6,
       "aktuelle-ladespannung-an-akku-kreis-8-s-6": aktuelle_ladespannung_an_akku_kreis_8_s_6,
       "aktuelle-spannung-an-akku-kreis-1-s-6": aktuelle_spannung_an_akku_kreis_1_s_6,
       "aktuelle-spannung-an-akku-kreis-2-s-6": aktuelle_spannung_an_akku_kreis_2_s_6,
       "aktuelle-spannung-an-akku-kreis-3-s-6": aktuelle_spannung_an_akku_kreis_3_s_6,
       "aktuelle-spannung-an-akku-kreis-4-s-6": aktuelle_spannung_an_akku_kreis_4_s_6,
       "aktuelle-spannung-an-akku-reis-5-s-6": aktuelle_spannung_an_akku_reis_5_s_6,
       "aktuelle-spannung-an-akku-kreis-6-s-6": aktuelle_spannung_an_akku_kreis_6_s_6,
       "aktuelle-spannung-an-akku-kreis-7-s-6": aktuelle_spannung_an_akku_kreis_7_s_6,
       "aktuelle-spannung-an-akku-kreis-8-s-6": aktuelle_spannung_an_akku_kreis_8_s_6,
       "testergebnis-lastspannung-an-akku-reis-1-s-6": testergebnis_lastspannung_an_akku_reis_1_s_6,
       "testergebnis-lastspannung-an-akku-kreis-2-s-6": testergebnis_lastspannung_an_akku_kreis_2_s_6,
       "testergebnis-lastspannung-an-akku-kreis-3-s-6": testergebnis_lastspannung_an_akku_kreis_3_s_6,
       "testergebnis-lastspannung-an-akku-kreis-4-s-6": testergebnis_lastspannung_an_akku_kreis_4_s_6,
       "testergebnis-lastspannung-an-akku-kreis-5-s-6": testergebnis_lastspannung_an_akku_kreis_5_s_6,
       "testergebnis-lastspannung-an-akku-kreis-6-s-6": testergebnis_lastspannung_an_akku_kreis_6_s_6,
       "testergebnis-lastspannung-an-akku-kreis-7-s-6": testergebnis_lastspannung_an_akku_kreis_7_s_6,
       "testergebnis-lastspannung-an-akku-kreis-8-s-6": testergebnis_lastspannung_an_akku_kreis_8_s_6,
       "testergebnis-innenwiderstand-akku-kreis-1-s-6": testergebnis_innenwiderstand_akku_kreis_1_s_6,
       "testergebnis-innenwiderstand-akku-kreis-2-s-6": testergebnis_innenwiderstand_akku_kreis_2_s_6,
       "testergebnis-innenwiderstand-akku-kreis-3-s-6": testergebnis_innenwiderstand_akku_kreis_3_s_6,
       "testergebnis-innenwiderstand-akku-kreis-4-s-6": testergebnis_innenwiderstand_akku_kreis_4_s_6,
       "testergebnis-innenwiderstand-akku-kreis-5-s-6": testergebnis_innenwiderstand_akku_kreis_5_s_6,
       "testergebnis-innenwiderstand-akku-kreis-6-s-6": testergebnis_innenwiderstand_akku_kreis_6_s_6,
       "testergebnis-innenwiderstand-akku-kreis-7-s-6": testergebnis_innenwiderstand_akku_kreis_7_s_6,
       "testergebnis-innenwiderstand-akku-kreis-8-s-6": testergebnis_innenwiderstand_akku_kreis_8_s_6,
       "netzteilspannung-uin1-s-6": netzteilspannung_uin1_s_6,
       "netzteilspannung-uin2-s-6": netzteilspannung_uin2_s_6,
       "programmierte-minimale-soll-sendeleistung-s-6": programmierte_minimale_soll_sendeleistung_s_6,
       "programmierte-maximale-antennen-reflexion-s-6": programmierte_maximale_antennen_reflexion_s_6,
       "programmierte-minimale-anzahl-praesenzsignale-s-6": programmierte_minimale_anzahl_praesenzsignale_s_6,
       "summen-fehlerstatus-von-tmoa-anlage-s-6": summen_fehlerstatus_von_tmoa_anlage_s_6,
       "summen-fehlerstatus-von-anbinderepeater-s-6": summen_fehlerstatus_von_anbinderepeater_s_6,
       "summen-fehlerstatus-von-analogem-repeater-s-6": summen_fehlerstatus_von_analogem_repeater_s_6,
       "aktuelle-ladespannung-akku-kreis-1-int-sicherung-defekt-s-6": aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_6,
       "aktuelle-ladespannung-akku-kreis-2-int-sicherung-defekt-s-6": aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_6,
       "aktuelle-ladespannung-akku-kreis-3-int-sicherung-defekt-s-6": aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_6,
       "aktuelle-ladespannung-akku-kreis-4-int-sicherung-defekt-s-6": aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_6,
       "aktuelle-ladespannung-akku-kreis-5-int-sicherung-defekt-s-6": aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_6,
       "aktuelle-ladespannung-akku-kreis-6-int-sicherung-defekt-s-6": aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_6,
       "aktuelle-ladespannung-akku-kreis-7-int-sicherung-defekt-s-6": aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_6,
       "aktuelle-ladespannung-akku-kreis-8-int-sicherung-defekt-s-6": aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_6,
       "netzspannungsversorgung-von-tmoa-anlage-s-6": netzspannungsversorgung_von_tmoa_anlage_s_6,
       "netzspannungsversorgung-von-anbinderepeater-s-6": netzspannungsversorgung_von_anbinderepeater_s_6,
       "fgb-id1-verbindungsstatus-s-6": fgb_id1_verbindungsstatus_s_6,
       "fgb-id2-verbindungsstatus-s-6": fgb_id2_verbindungsstatus_s_6,
       "fgb-id3-verbindungsstatus-s-6": fgb_id3_verbindungsstatus_s_6,
       "fgb-id4-verbindungsstatus-s-6": fgb_id4_verbindungsstatus_s_6,
       "fgb-id5-verbindungsstatus-s-6": fgb_id5_verbindungsstatus_s_6,
       "fgb-id6-verbindungsstatus-s-6": fgb_id6_verbindungsstatus_s_6,
       "fgb-id7-verbindungsstatus-s-6": fgb_id7_verbindungsstatus_s_6,
       "fgb-id8-verbindungsstatus-s-6": fgb_id8_verbindungsstatus_s_6,
       "fgb-id9-verbindungsstatus-s-6": fgb_id9_verbindungsstatus_s_6,
       "fgb-id10-verbindungsstatus-s-6": fgb_id10_verbindungsstatus_s_6,
       "fgb-id11-verbindungsstatus-s-6": fgb_id11_verbindungsstatus_s_6,
       "mod-bus-verbindungsstatus-s-6": mod_bus_verbindungsstatus_s_6,
       "fgb-bus-verbindungsstatus-s-6": fgb_bus_verbindungsstatus_s_6,
       "slave-bus-verbindungsstatus-s-6": slave_bus_verbindungsstatus_s_6,
       "gsm-modem-verbindungsstatus-s-6": gsm_modem_verbindungsstatus_s_6,
       "gsm-modem-sim-karte-s-6": gsm_modem_sim_karte_s_6,
       "gsm-modem-pin-nummer-s-6": gsm_modem_pin_nummer_s_6,
       "gsm-modem-provider-service-s-6": gsm_modem_provider_service_s_6,
       "gsm-modem-empfangspegel-s-6": gsm_modem_empfangspegel_s_6,
       "lte-router-verbindungsstatus-s-6": lte_router_verbindungsstatus_s_6,
       "lte-router-provider-service-s-6": lte_router_provider_service_s_6,
       "lte-router-empfangspegel-s-6": lte_router_empfangspegel_s_6,
       "antennenleitungsueberwachung-1-s-6": antennenleitungsueberwachung_1_s_6,
       "antennenleitungsueberwachung-2-s-6": antennenleitungsueberwachung_2_s_6,
       "antennenleitungseuberwachung-3-s-6": antennenleitungseuberwachung_3_s_6,
       "interne-temperaturuebwerwachung-s-6": interne_temperaturuebwerwachung_s_6,
       "stoerueberwachung-optisches-verteilsystem-1-s-6": stoerueberwachung_optisches_verteilsystem_1_s_6,
       "stoerueberwachung-optisches-verteilsystem-2-s-6": stoerueberwachung_optisches_verteilsystem_2_s_6,
       "lte-router-sim-karte-s-6": lte_router_sim_karte_s_6,
       "lte-router-pin-nummer-s-6": lte_router_pin_nummer_s_6,
       "ak-slave-7-i": ak_slave_7_i,
       "modulTable-s-7": modulTable_s_7,
       "modulEntry-s-7": modulEntry_s_7,
       "modulIndex-s-7": modulIndex_s_7,
       "geraete-typ-s-7": geraete_typ_s_7,
       "betriebsstatus-s-7": betriebsstatus_s_7,
       "senderstatus-s-7": senderstatus_s_7,
       "fehlerstatus-s-7": fehlerstatus_s_7,
       "dem-adapter-zugeordnete-funkgeraetetype-s-7": dem_adapter_zugeordnete_funkgeraetetype_s_7,
       "eingabe-und-anzeigemodul-s-7": eingabe_und_anzeigemodul_s_7,
       "mod-bus-verbindung-module-s-7": mod_bus_verbindung_module_s_7,
       "gemessene-sendeleistung-im-testmode-s-7": gemessene_sendeleistung_im_testmode_s_7,
       "aktuelle-sendeleistung-s-7": aktuelle_sendeleistung_s_7,
       "gemessene-reflexion-im-testmode-s-7": gemessene_reflexion_im_testmode_s_7,
       "aktuelle-reflexion-s-7": aktuelle_reflexion_s_7,
       "letzte-gemessene-donor-sendeleistung-s-7": letzte_gemessene_donor_sendeleistung_s_7,
       "aktuelle-donor-sendeleistung-s-7": aktuelle_donor_sendeleistung_s_7,
       "letzte-gemessene-donor-reflexion-s-7": letzte_gemessene_donor_reflexion_s_7,
       "aktuelle-donor-reflexion-s-7": aktuelle_donor_reflexion_s_7,
       "anzahl-gemessener-praesenzsignale-im-testmode-s-7": anzahl_gemessener_praesenzsignale_im_testmode_s_7,
       "aktuelle-ausgangsspannung-ub-s-7": aktuelle_ausgangsspannung_ub_s_7,
       "aktuelle-ausgangsspannung-u1-s-7": aktuelle_ausgangsspannung_u1_s_7,
       "aktuelle-ausgangsspannung-u2-s-7": aktuelle_ausgangsspannung_u2_s_7,
       "aktuelle-ausgangsspannung-u3-s-7": aktuelle_ausgangsspannung_u3_s_7,
       "aktuelle-ausgangsspannung-u4-s-7": aktuelle_ausgangsspannung_u4_s_7,
       "aktuelle-ausgangsspannung-u5-s-7": aktuelle_ausgangsspannung_u5_s_7,
       "aktuelle-ausgangsspannung-u6-s-7": aktuelle_ausgangsspannung_u6_s_7,
       "aktuelle-ausgangsspannung-u7-s-7": aktuelle_ausgangsspannung_u7_s_7,
       "aktuelle-ausgangsspannung-u8-s-7": aktuelle_ausgangsspannung_u8_s_7,
       "aktuelle-ladespannung-an-akku-kreis-1-s-7": aktuelle_ladespannung_an_akku_kreis_1_s_7,
       "aktuelle-ladespannung-an-akku-Kreis-2-s-7": aktuelle_ladespannung_an_akku_Kreis_2_s_7,
       "aktuelle-ladespannung-an-akku-Kreis-3-s-7": aktuelle_ladespannung_an_akku_Kreis_3_s_7,
       "aktuelle-ladespannung-an-akku-kreis-4-s-7": aktuelle_ladespannung_an_akku_kreis_4_s_7,
       "aktuelle-ladespannung-an-akku-kreis-5-s-7": aktuelle_ladespannung_an_akku_kreis_5_s_7,
       "aktuelle-ladespannung-an-akku-kreis-6-s-7": aktuelle_ladespannung_an_akku_kreis_6_s_7,
       "aktuelle-ladespannung-an-akku-kreis-7-s-7": aktuelle_ladespannung_an_akku_kreis_7_s_7,
       "aktuelle-ladespannung-an-akku-kreis-8-s-7": aktuelle_ladespannung_an_akku_kreis_8_s_7,
       "aktuelle-spannung-an-akku-kreis-1-s-7": aktuelle_spannung_an_akku_kreis_1_s_7,
       "aktuelle-spannung-an-akku-kreis-2-s-7": aktuelle_spannung_an_akku_kreis_2_s_7,
       "aktuelle-spannung-an-akku-kreis-3-s-7": aktuelle_spannung_an_akku_kreis_3_s_7,
       "aktuelle-spannung-an-akku-kreis-4-s-7": aktuelle_spannung_an_akku_kreis_4_s_7,
       "aktuelle-spannung-an-akku-reis-5-s-7": aktuelle_spannung_an_akku_reis_5_s_7,
       "aktuelle-spannung-an-akku-kreis-6-s-7": aktuelle_spannung_an_akku_kreis_6_s_7,
       "aktuelle-spannung-an-akku-kreis-7-s-7": aktuelle_spannung_an_akku_kreis_7_s_7,
       "aktuelle-spannung-an-akku-kreis-8-s-7": aktuelle_spannung_an_akku_kreis_8_s_7,
       "testergebnis-lastspannung-an-akku-reis-1-s-7": testergebnis_lastspannung_an_akku_reis_1_s_7,
       "testergebnis-lastspannung-an-akku-kreis-2-s-7": testergebnis_lastspannung_an_akku_kreis_2_s_7,
       "testergebnis-lastspannung-an-akku-kreis-3-s-7": testergebnis_lastspannung_an_akku_kreis_3_s_7,
       "testergebnis-lastspannung-an-akku-kreis-4-s-7": testergebnis_lastspannung_an_akku_kreis_4_s_7,
       "testergebnis-lastspannung-an-akku-kreis-5-s-7": testergebnis_lastspannung_an_akku_kreis_5_s_7,
       "testergebnis-lastspannung-an-akku-kreis-6-s-7": testergebnis_lastspannung_an_akku_kreis_6_s_7,
       "testergebnis-lastspannung-an-akku-kreis-7-s-7": testergebnis_lastspannung_an_akku_kreis_7_s_7,
       "testergebnis-lastspannung-an-akku-kreis-8-s-7": testergebnis_lastspannung_an_akku_kreis_8_s_7,
       "testergebnis-innenwiderstand-akku-kreis-1-s-7": testergebnis_innenwiderstand_akku_kreis_1_s_7,
       "testergebnis-innenwiderstand-akku-kreis-2-s-7": testergebnis_innenwiderstand_akku_kreis_2_s_7,
       "testergebnis-innenwiderstand-akku-kreis-3-s-7": testergebnis_innenwiderstand_akku_kreis_3_s_7,
       "testergebnis-innenwiderstand-akku-kreis-4-s-7": testergebnis_innenwiderstand_akku_kreis_4_s_7,
       "testergebnis-innenwiderstand-akku-kreis-5-s-7": testergebnis_innenwiderstand_akku_kreis_5_s_7,
       "testergebnis-innenwiderstand-akku-kreis-6-s-7": testergebnis_innenwiderstand_akku_kreis_6_s_7,
       "testergebnis-innenwiderstand-akku-kreis-7-s-7": testergebnis_innenwiderstand_akku_kreis_7_s_7,
       "testergebnis-innenwiderstand-akku-kreis-8-s-7": testergebnis_innenwiderstand_akku_kreis_8_s_7,
       "netzteilspannung-uin1-s-7": netzteilspannung_uin1_s_7,
       "netzteilspannung-uin2-s-7": netzteilspannung_uin2_s_7,
       "programmierte-minimale-soll-sendeleistung-s-7": programmierte_minimale_soll_sendeleistung_s_7,
       "programmierte-maximale-antennen-reflexion-s-7": programmierte_maximale_antennen_reflexion_s_7,
       "programmierte-minimale-anzahl-praesenzsignale-s-7": programmierte_minimale_anzahl_praesenzsignale_s_7,
       "summen-fehlerstatus-von-tmoa-anlage-s-7": summen_fehlerstatus_von_tmoa_anlage_s_7,
       "summen-fehlerstatus-von-anbinderepeater-s-7": summen_fehlerstatus_von_anbinderepeater_s_7,
       "summen-fehlerstatus-von-analogem-repeater-s-7": summen_fehlerstatus_von_analogem_repeater_s_7,
       "aktuelle-ladespannung-akku-kreis-1-int-sicherung-defekt-s-7": aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_7,
       "aktuelle-ladespannung-akku-kreis-2-int-sicherung-defekt-s-7": aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_7,
       "aktuelle-ladespannung-akku-kreis-3-int-sicherung-defekt-s-7": aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_7,
       "aktuelle-ladespannung-akku-kreis-4-int-sicherung-defekt-s-7": aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_7,
       "aktuelle-ladespannung-akku-kreis-5-int-sicherung-defekt-s-7": aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_7,
       "aktuelle-ladespannung-akku-kreis-6-int-sicherung-defekt-s-7": aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_7,
       "aktuelle-ladespannung-akku-kreis-7-int-sicherung-defekt-s-7": aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_7,
       "aktuelle-ladespannung-akku-kreis-8-int-sicherung-defekt-s-7": aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_7,
       "netzspannungsversorgung-von-tmoa-anlage-s-7": netzspannungsversorgung_von_tmoa_anlage_s_7,
       "netzspannungsversorgung-von-anbinderepeater-s-7": netzspannungsversorgung_von_anbinderepeater_s_7,
       "fgb-id1-verbindungsstatus-s-7": fgb_id1_verbindungsstatus_s_7,
       "fgb-id2-verbindungsstatus-s-7": fgb_id2_verbindungsstatus_s_7,
       "fgb-id3-verbindungsstatus-s-7": fgb_id3_verbindungsstatus_s_7,
       "fgb-id4-verbindungsstatus-s-7": fgb_id4_verbindungsstatus_s_7,
       "fgb-id5-verbindungsstatus-s-7": fgb_id5_verbindungsstatus_s_7,
       "fgb-id6-verbindungsstatus-s-7": fgb_id6_verbindungsstatus_s_7,
       "fgb-id7-verbindungsstatus-s-7": fgb_id7_verbindungsstatus_s_7,
       "fgb-id8-verbindungsstatus-s-7": fgb_id8_verbindungsstatus_s_7,
       "fgb-id9-verbindungsstatus-s-7": fgb_id9_verbindungsstatus_s_7,
       "fgb-id10-verbindungsstatus-s-7": fgb_id10_verbindungsstatus_s_7,
       "fgb-id11-verbindungsstatus-s-7": fgb_id11_verbindungsstatus_s_7,
       "mod-bus-verbindungsstatus-s-7": mod_bus_verbindungsstatus_s_7,
       "fgb-bus-verbindungsstatus-s-7": fgb_bus_verbindungsstatus_s_7,
       "slave-bus-verbindungsstatus-s-7": slave_bus_verbindungsstatus_s_7,
       "gsm-modem-verbindungsstatus-s-7": gsm_modem_verbindungsstatus_s_7,
       "gsm-modem-sim-karte-s-7": gsm_modem_sim_karte_s_7,
       "gsm-modem-pin-nummer-s-7": gsm_modem_pin_nummer_s_7,
       "gsm-modem-provider-service-s-7": gsm_modem_provider_service_s_7,
       "gsm-modem-empfangspegel-s-7": gsm_modem_empfangspegel_s_7,
       "lte-router-verbindungsstatus-s-7": lte_router_verbindungsstatus_s_7,
       "lte-router-provider-service-s-7": lte_router_provider_service_s_7,
       "lte-router-empfangspegel-s-7": lte_router_empfangspegel_s_7,
       "antennenleitungsueberwachung-1-s-7": antennenleitungsueberwachung_1_s_7,
       "antennenleitungsueberwachung-2-s-7": antennenleitungsueberwachung_2_s_7,
       "antennenleitungseuberwachung-3-s-7": antennenleitungseuberwachung_3_s_7,
       "interne-temperaturuebwerwachung-s-7": interne_temperaturuebwerwachung_s_7,
       "stoerueberwachung-optisches-verteilsystem-1-s-7": stoerueberwachung_optisches_verteilsystem_1_s_7,
       "stoerueberwachung-optisches-verteilsystem-2-s-7": stoerueberwachung_optisches_verteilsystem_2_s_7,
       "lte-router-sim-karte-s-7": lte_router_sim_karte_s_7,
       "lte-router-pin-nummer-s-7": lte_router_pin_nummer_s_7,
       "ak-slave-8-i": ak_slave_8_i,
       "modulTable-s-8": modulTable_s_8,
       "modulEntry-s-8": modulEntry_s_8,
       "modulIndex-s-8": modulIndex_s_8,
       "geraete-typ-s-8": geraete_typ_s_8,
       "betriebsstatus-s-8": betriebsstatus_s_8,
       "senderstatus-s-8": senderstatus_s_8,
       "fehlerstatus-s-8": fehlerstatus_s_8,
       "dem-adapter-zugeordnete-funkgeraetetype-s-8": dem_adapter_zugeordnete_funkgeraetetype_s_8,
       "eingabe-und-anzeigemodul-s-8": eingabe_und_anzeigemodul_s_8,
       "mod-bus-verbindung-module-s-8": mod_bus_verbindung_module_s_8,
       "gemessene-sendeleistung-im-testmode-s-8": gemessene_sendeleistung_im_testmode_s_8,
       "aktuelle-sendeleistung-s-8": aktuelle_sendeleistung_s_8,
       "gemessene-reflexion-im-testmode-s-8": gemessene_reflexion_im_testmode_s_8,
       "aktuelle-reflexion-s-8": aktuelle_reflexion_s_8,
       "letzte-gemessene-donor-sendeleistung-s-8": letzte_gemessene_donor_sendeleistung_s_8,
       "aktuelle-donor-sendeleistung-s-8": aktuelle_donor_sendeleistung_s_8,
       "letzte-gemessene-donor-reflexion-s-8": letzte_gemessene_donor_reflexion_s_8,
       "aktuelle-donor-reflexion-s-8": aktuelle_donor_reflexion_s_8,
       "anzahl-gemessener-praesenzsignale-im-testmode-s-8": anzahl_gemessener_praesenzsignale_im_testmode_s_8,
       "aktuelle-ausgangsspannung-ub-s-8": aktuelle_ausgangsspannung_ub_s_8,
       "aktuelle-ausgangsspannung-u1-s-8": aktuelle_ausgangsspannung_u1_s_8,
       "aktuelle-ausgangsspannung-u2-s-8": aktuelle_ausgangsspannung_u2_s_8,
       "aktuelle-ausgangsspannung-u3-s-8": aktuelle_ausgangsspannung_u3_s_8,
       "aktuelle-ausgangsspannung-u4-s-8": aktuelle_ausgangsspannung_u4_s_8,
       "aktuelle-ausgangsspannung-u5-s-8": aktuelle_ausgangsspannung_u5_s_8,
       "aktuelle-ausgangsspannung-u6-s-8": aktuelle_ausgangsspannung_u6_s_8,
       "aktuelle-ausgangsspannung-u7-s-8": aktuelle_ausgangsspannung_u7_s_8,
       "aktuelle-ausgangsspannung-u8-s-8": aktuelle_ausgangsspannung_u8_s_8,
       "aktuelle-ladespannung-an-akku-kreis-1-s-8": aktuelle_ladespannung_an_akku_kreis_1_s_8,
       "aktuelle-ladespannung-an-akku-Kreis-2-s-8": aktuelle_ladespannung_an_akku_Kreis_2_s_8,
       "aktuelle-ladespannung-an-akku-Kreis-3-s-8": aktuelle_ladespannung_an_akku_Kreis_3_s_8,
       "aktuelle-ladespannung-an-akku-kreis-4-s-8": aktuelle_ladespannung_an_akku_kreis_4_s_8,
       "aktuelle-ladespannung-an-akku-kreis-5-s-8": aktuelle_ladespannung_an_akku_kreis_5_s_8,
       "aktuelle-ladespannung-an-akku-kreis-6-s-8": aktuelle_ladespannung_an_akku_kreis_6_s_8,
       "aktuelle-ladespannung-an-akku-kreis-7-s-8": aktuelle_ladespannung_an_akku_kreis_7_s_8,
       "aktuelle-ladespannung-an-akku-kreis-8-s-8": aktuelle_ladespannung_an_akku_kreis_8_s_8,
       "aktuelle-spannung-an-akku-kreis-1-s-8": aktuelle_spannung_an_akku_kreis_1_s_8,
       "aktuelle-spannung-an-akku-kreis-2-s-8": aktuelle_spannung_an_akku_kreis_2_s_8,
       "aktuelle-spannung-an-akku-kreis-3-s-8": aktuelle_spannung_an_akku_kreis_3_s_8,
       "aktuelle-spannung-an-akku-kreis-4-s-8": aktuelle_spannung_an_akku_kreis_4_s_8,
       "aktuelle-spannung-an-akku-reis-5-s-8": aktuelle_spannung_an_akku_reis_5_s_8,
       "aktuelle-spannung-an-akku-kreis-6-s-8": aktuelle_spannung_an_akku_kreis_6_s_8,
       "aktuelle-spannung-an-akku-kreis-7-s-8": aktuelle_spannung_an_akku_kreis_7_s_8,
       "aktuelle-spannung-an-akku-kreis-8-s-8": aktuelle_spannung_an_akku_kreis_8_s_8,
       "testergebnis-lastspannung-an-akku-reis-1-s-8": testergebnis_lastspannung_an_akku_reis_1_s_8,
       "testergebnis-lastspannung-an-akku-kreis-2-s-8": testergebnis_lastspannung_an_akku_kreis_2_s_8,
       "testergebnis-lastspannung-an-akku-kreis-3-s-8": testergebnis_lastspannung_an_akku_kreis_3_s_8,
       "testergebnis-lastspannung-an-akku-kreis-4-s-8": testergebnis_lastspannung_an_akku_kreis_4_s_8,
       "testergebnis-lastspannung-an-akku-kreis-5-s-8": testergebnis_lastspannung_an_akku_kreis_5_s_8,
       "testergebnis-lastspannung-an-akku-kreis-6-s-8": testergebnis_lastspannung_an_akku_kreis_6_s_8,
       "testergebnis-lastspannung-an-akku-kreis-7-s-8": testergebnis_lastspannung_an_akku_kreis_7_s_8,
       "testergebnis-lastspannung-an-akku-kreis-8-s-8": testergebnis_lastspannung_an_akku_kreis_8_s_8,
       "testergebnis-innenwiderstand-akku-kreis-1-s-8": testergebnis_innenwiderstand_akku_kreis_1_s_8,
       "testergebnis-innenwiderstand-akku-kreis-2-s-8": testergebnis_innenwiderstand_akku_kreis_2_s_8,
       "testergebnis-innenwiderstand-akku-kreis-3-s-8": testergebnis_innenwiderstand_akku_kreis_3_s_8,
       "testergebnis-innenwiderstand-akku-kreis-4-s-8": testergebnis_innenwiderstand_akku_kreis_4_s_8,
       "testergebnis-innenwiderstand-akku-kreis-5-s-8": testergebnis_innenwiderstand_akku_kreis_5_s_8,
       "testergebnis-innenwiderstand-akku-kreis-6-s-8": testergebnis_innenwiderstand_akku_kreis_6_s_8,
       "testergebnis-innenwiderstand-akku-kreis-7-s-8": testergebnis_innenwiderstand_akku_kreis_7_s_8,
       "testergebnis-innenwiderstand-akku-kreis-8-s-8": testergebnis_innenwiderstand_akku_kreis_8_s_8,
       "netzteilspannung-uin1-s-8": netzteilspannung_uin1_s_8,
       "netzteilspannung-uin2-s-8": netzteilspannung_uin2_s_8,
       "programmierte-minimale-soll-sendeleistung-s-8": programmierte_minimale_soll_sendeleistung_s_8,
       "programmierte-maximale-antennen-reflexion-s-8": programmierte_maximale_antennen_reflexion_s_8,
       "programmierte-minimale-anzahl-praesenzsignale-s-8": programmierte_minimale_anzahl_praesenzsignale_s_8,
       "summen-fehlerstatus-von-tmoa-anlage-s-8": summen_fehlerstatus_von_tmoa_anlage_s_8,
       "summen-fehlerstatus-von-anbinderepeater-s-8": summen_fehlerstatus_von_anbinderepeater_s_8,
       "summen-fehlerstatus-von-analogem-repeater-s-8": summen_fehlerstatus_von_analogem_repeater_s_8,
       "aktuelle-ladespannung-akku-kreis-1-int-sicherung-defekt-s-8": aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_8,
       "aktuelle-ladespannung-akku-kreis-2-int-sicherung-defekt-s-8": aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_8,
       "aktuelle-ladespannung-akku-kreis-3-int-sicherung-defekt-s-8": aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_8,
       "aktuelle-ladespannung-akku-kreis-4-int-sicherung-defekt-s-8": aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_8,
       "aktuelle-ladespannung-akku-kreis-5-int-sicherung-defekt-s-8": aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_8,
       "aktuelle-ladespannung-akku-kreis-6-int-sicherung-defekt-s-8": aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_8,
       "aktuelle-ladespannung-akku-kreis-7-int-sicherung-defekt-s-8": aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_8,
       "aktuelle-ladespannung-akku-kreis-8-int-sicherung-defekt-s-8": aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_8,
       "netzspannungsversorgung-von-tmoa-anlage-s-8": netzspannungsversorgung_von_tmoa_anlage_s_8,
       "netzspannungsversorgung-von-anbinderepeater-s-8": netzspannungsversorgung_von_anbinderepeater_s_8,
       "fgb-id1-verbindungsstatus-s-8": fgb_id1_verbindungsstatus_s_8,
       "fgb-id2-verbindungsstatus-s-8": fgb_id2_verbindungsstatus_s_8,
       "fgb-id3-verbindungsstatus-s-8": fgb_id3_verbindungsstatus_s_8,
       "fgb-id4-verbindungsstatus-s-8": fgb_id4_verbindungsstatus_s_8,
       "fgb-id5-verbindungsstatus-s-8": fgb_id5_verbindungsstatus_s_8,
       "fgb-id6-verbindungsstatus-s-8": fgb_id6_verbindungsstatus_s_8,
       "fgb-id7-verbindungsstatus-s-8": fgb_id7_verbindungsstatus_s_8,
       "fgb-id8-verbindungsstatus-s-8": fgb_id8_verbindungsstatus_s_8,
       "fgb-id9-verbindungsstatus-s-8": fgb_id9_verbindungsstatus_s_8,
       "fgb-id10-verbindungsstatus-s-8": fgb_id10_verbindungsstatus_s_8,
       "fgb-id11-verbindungsstatus-s-8": fgb_id11_verbindungsstatus_s_8,
       "mod-bus-verbindungsstatus-s-8": mod_bus_verbindungsstatus_s_8,
       "fgb-bus-verbindungsstatus-s-8": fgb_bus_verbindungsstatus_s_8,
       "slave-bus-verbindungsstatus-s-8": slave_bus_verbindungsstatus_s_8,
       "gsm-modem-verbindungsstatus-s-8": gsm_modem_verbindungsstatus_s_8,
       "gsm-modem-sim-karte-s-8": gsm_modem_sim_karte_s_8,
       "gsm-modem-pin-nummer-s-8": gsm_modem_pin_nummer_s_8,
       "gsm-modem-provider-service-s-8": gsm_modem_provider_service_s_8,
       "gsm-modem-empfangspegel-s-8": gsm_modem_empfangspegel_s_8,
       "lte-router-verbindungsstatus-s-8": lte_router_verbindungsstatus_s_8,
       "lte-router-provider-service-s-8": lte_router_provider_service_s_8,
       "lte-router-empfangspegel-s-8": lte_router_empfangspegel_s_8,
       "antennenleitungsueberwachung-1-s-8": antennenleitungsueberwachung_1_s_8,
       "antennenleitungsueberwachung-2-s-8": antennenleitungsueberwachung_2_s_8,
       "antennenleitungseuberwachung-3-s-8": antennenleitungseuberwachung_3_s_8,
       "interne-temperaturuebwerwachung-s-8": interne_temperaturuebwerwachung_s_8,
       "stoerueberwachung-optisches-verteilsystem-1-s-8": stoerueberwachung_optisches_verteilsystem_1_s_8,
       "stoerueberwachung-optisches-verteilsystem-2-s-8": stoerueberwachung_optisches_verteilsystem_2_s_8,
       "lte-router-sim-karte-s-8": lte_router_sim_karte_s_8,
       "lte-router-pin-nummer-s-8": lte_router_pin_nummer_s_8,
       "ak-slave-9-i": ak_slave_9_i,
       "modulTable-s-9": modulTable_s_9,
       "modulEntry-s-9": modulEntry_s_9,
       "modulIndex-s-9": modulIndex_s_9,
       "geraete-typ-s-9": geraete_typ_s_9,
       "betriebsstatus-s-9": betriebsstatus_s_9,
       "senderstatus-s-9": senderstatus_s_9,
       "fehlerstatus-s-9": fehlerstatus_s_9,
       "dem-adapter-zugeordnete-funkgeraetetype-s-9": dem_adapter_zugeordnete_funkgeraetetype_s_9,
       "eingabe-und-anzeigemodul-s-9": eingabe_und_anzeigemodul_s_9,
       "mod-bus-verbindung-module-s-9": mod_bus_verbindung_module_s_9,
       "gemessene-sendeleistung-im-testmode-s-9": gemessene_sendeleistung_im_testmode_s_9,
       "aktuelle-sendeleistung-s-9": aktuelle_sendeleistung_s_9,
       "gemessene-reflexion-im-testmode-s-9": gemessene_reflexion_im_testmode_s_9,
       "aktuelle-reflexion-s-9": aktuelle_reflexion_s_9,
       "letzte-gemessene-donor-sendeleistung-s-9": letzte_gemessene_donor_sendeleistung_s_9,
       "aktuelle-donor-sendeleistung-s-9": aktuelle_donor_sendeleistung_s_9,
       "letzte-gemessene-donor-reflexion-s-9": letzte_gemessene_donor_reflexion_s_9,
       "aktuelle-donor-reflexion-s-9": aktuelle_donor_reflexion_s_9,
       "anzahl-gemessener-praesenzsignale-im-testmode-s-9": anzahl_gemessener_praesenzsignale_im_testmode_s_9,
       "aktuelle-ausgangsspannung-ub-s-9": aktuelle_ausgangsspannung_ub_s_9,
       "aktuelle-ausgangsspannung-u1-s-9": aktuelle_ausgangsspannung_u1_s_9,
       "aktuelle-ausgangsspannung-u2-s-9": aktuelle_ausgangsspannung_u2_s_9,
       "aktuelle-ausgangsspannung-u3-s-9": aktuelle_ausgangsspannung_u3_s_9,
       "aktuelle-ausgangsspannung-u4-s-9": aktuelle_ausgangsspannung_u4_s_9,
       "aktuelle-ausgangsspannung-u5-s-9": aktuelle_ausgangsspannung_u5_s_9,
       "aktuelle-ausgangsspannung-u6-s-9": aktuelle_ausgangsspannung_u6_s_9,
       "aktuelle-ausgangsspannung-u7-s-9": aktuelle_ausgangsspannung_u7_s_9,
       "aktuelle-ausgangsspannung-u8-s-9": aktuelle_ausgangsspannung_u8_s_9,
       "aktuelle-ladespannung-an-akku-kreis-1-s-9": aktuelle_ladespannung_an_akku_kreis_1_s_9,
       "aktuelle-ladespannung-an-akku-Kreis-2-s-9": aktuelle_ladespannung_an_akku_Kreis_2_s_9,
       "aktuelle-ladespannung-an-akku-Kreis-3-s-9": aktuelle_ladespannung_an_akku_Kreis_3_s_9,
       "aktuelle-ladespannung-an-akku-kreis-4-s-9": aktuelle_ladespannung_an_akku_kreis_4_s_9,
       "aktuelle-ladespannung-an-akku-kreis-5-s-9": aktuelle_ladespannung_an_akku_kreis_5_s_9,
       "aktuelle-ladespannung-an-akku-kreis-6-s-9": aktuelle_ladespannung_an_akku_kreis_6_s_9,
       "aktuelle-ladespannung-an-akku-kreis-7-s-9": aktuelle_ladespannung_an_akku_kreis_7_s_9,
       "aktuelle-ladespannung-an-akku-kreis-8-s-9": aktuelle_ladespannung_an_akku_kreis_8_s_9,
       "aktuelle-spannung-an-akku-kreis-1-s-9": aktuelle_spannung_an_akku_kreis_1_s_9,
       "aktuelle-spannung-an-akku-kreis-2-s-9": aktuelle_spannung_an_akku_kreis_2_s_9,
       "aktuelle-spannung-an-akku-kreis-3-s-9": aktuelle_spannung_an_akku_kreis_3_s_9,
       "aktuelle-spannung-an-akku-kreis-4-s-9": aktuelle_spannung_an_akku_kreis_4_s_9,
       "aktuelle-spannung-an-akku-reis-5-s-9": aktuelle_spannung_an_akku_reis_5_s_9,
       "aktuelle-spannung-an-akku-kreis-6-s-9": aktuelle_spannung_an_akku_kreis_6_s_9,
       "aktuelle-spannung-an-akku-kreis-7-s-9": aktuelle_spannung_an_akku_kreis_7_s_9,
       "aktuelle-spannung-an-akku-kreis-8-s-9": aktuelle_spannung_an_akku_kreis_8_s_9,
       "testergebnis-lastspannung-an-akku-reis-1-s-9": testergebnis_lastspannung_an_akku_reis_1_s_9,
       "testergebnis-lastspannung-an-akku-kreis-2-s-9": testergebnis_lastspannung_an_akku_kreis_2_s_9,
       "testergebnis-lastspannung-an-akku-kreis-3-s-9": testergebnis_lastspannung_an_akku_kreis_3_s_9,
       "testergebnis-lastspannung-an-akku-kreis-4-s-9": testergebnis_lastspannung_an_akku_kreis_4_s_9,
       "testergebnis-lastspannung-an-akku-kreis-5-s-9": testergebnis_lastspannung_an_akku_kreis_5_s_9,
       "testergebnis-lastspannung-an-akku-kreis-6-s-9": testergebnis_lastspannung_an_akku_kreis_6_s_9,
       "testergebnis-lastspannung-an-akku-kreis-7-s-9": testergebnis_lastspannung_an_akku_kreis_7_s_9,
       "testergebnis-lastspannung-an-akku-kreis-8-s-9": testergebnis_lastspannung_an_akku_kreis_8_s_9,
       "testergebnis-innenwiderstand-akku-kreis-1-s-9": testergebnis_innenwiderstand_akku_kreis_1_s_9,
       "testergebnis-innenwiderstand-akku-kreis-2-s-9": testergebnis_innenwiderstand_akku_kreis_2_s_9,
       "testergebnis-innenwiderstand-akku-kreis-3-s-9": testergebnis_innenwiderstand_akku_kreis_3_s_9,
       "testergebnis-innenwiderstand-akku-kreis-4-s-9": testergebnis_innenwiderstand_akku_kreis_4_s_9,
       "testergebnis-innenwiderstand-akku-kreis-5-s-9": testergebnis_innenwiderstand_akku_kreis_5_s_9,
       "testergebnis-innenwiderstand-akku-kreis-6-s-9": testergebnis_innenwiderstand_akku_kreis_6_s_9,
       "testergebnis-innenwiderstand-akku-kreis-7-s-9": testergebnis_innenwiderstand_akku_kreis_7_s_9,
       "testergebnis-innenwiderstand-akku-kreis-8-s-9": testergebnis_innenwiderstand_akku_kreis_8_s_9,
       "netzteilspannung-uin1-s-9": netzteilspannung_uin1_s_9,
       "netzteilspannung-uin2-s-9": netzteilspannung_uin2_s_9,
       "programmierte-minimale-soll-sendeleistung-s-9": programmierte_minimale_soll_sendeleistung_s_9,
       "programmierte-maximale-antennen-reflexion-s-9": programmierte_maximale_antennen_reflexion_s_9,
       "programmierte-minimale-anzahl-praesenzsignale-s-9": programmierte_minimale_anzahl_praesenzsignale_s_9,
       "summen-fehlerstatus-von-tmoa-anlage-s-9": summen_fehlerstatus_von_tmoa_anlage_s_9,
       "summen-fehlerstatus-von-anbinderepeater-s-9": summen_fehlerstatus_von_anbinderepeater_s_9,
       "summen-fehlerstatus-von-analogem-repeater-s-9": summen_fehlerstatus_von_analogem_repeater_s_9,
       "aktuelle-ladespannung-akku-kreis-1-int-sicherung-defekt-s-9": aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_9,
       "aktuelle-ladespannung-akku-kreis-2-int-sicherung-defekt-s-9": aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_9,
       "aktuelle-ladespannung-akku-kreis-3-int-sicherung-defekt-s-9": aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_9,
       "aktuelle-ladespannung-akku-kreis-4-int-sicherung-defekt-s-9": aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_9,
       "aktuelle-ladespannung-akku-kreis-5-int-sicherung-defekt-s-9": aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_9,
       "aktuelle-ladespannung-akku-kreis-6-int-sicherung-defekt-s-9": aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_9,
       "aktuelle-ladespannung-akku-kreis-7-int-sicherung-defekt-s-9": aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_9,
       "aktuelle-ladespannung-akku-kreis-8-int-sicherung-defekt-s-9": aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_9,
       "netzspannungsversorgung-von-tmoa-anlage-s-9": netzspannungsversorgung_von_tmoa_anlage_s_9,
       "netzspannungsversorgung-von-anbinderepeater-s-9": netzspannungsversorgung_von_anbinderepeater_s_9,
       "fgb-id1-verbindungsstatus-s-9": fgb_id1_verbindungsstatus_s_9,
       "fgb-id2-verbindungsstatus-s-9": fgb_id2_verbindungsstatus_s_9,
       "fgb-id3-verbindungsstatus-s-9": fgb_id3_verbindungsstatus_s_9,
       "fgb-id4-verbindungsstatus-s-9": fgb_id4_verbindungsstatus_s_9,
       "fgb-id5-verbindungsstatus-s-9": fgb_id5_verbindungsstatus_s_9,
       "fgb-id6-verbindungsstatus-s-9": fgb_id6_verbindungsstatus_s_9,
       "fgb-id7-verbindungsstatus-s-9": fgb_id7_verbindungsstatus_s_9,
       "fgb-id8-verbindungsstatus-s-9": fgb_id8_verbindungsstatus_s_9,
       "fgb-id9-verbindungsstatus-s-9": fgb_id9_verbindungsstatus_s_9,
       "fgb-id10-verbindungsstatus-s-9": fgb_id10_verbindungsstatus_s_9,
       "fgb-id11-verbindungsstatus-s-9": fgb_id11_verbindungsstatus_s_9,
       "mod-bus-verbindungsstatus-s-9": mod_bus_verbindungsstatus_s_9,
       "fgb-bus-verbindungsstatus-s-9": fgb_bus_verbindungsstatus_s_9,
       "slave-bus-verbindungsstatus-s-9": slave_bus_verbindungsstatus_s_9,
       "gsm-modem-verbindungsstatus-s-9": gsm_modem_verbindungsstatus_s_9,
       "gsm-modem-sim-karte-s-9": gsm_modem_sim_karte_s_9,
       "gsm-modem-pin-nummer-s-9": gsm_modem_pin_nummer_s_9,
       "gsm-modem-provider-service-s-9": gsm_modem_provider_service_s_9,
       "gsm-modem-empfangspegel-s-9": gsm_modem_empfangspegel_s_9,
       "lte-router-verbindungsstatus-s-9": lte_router_verbindungsstatus_s_9,
       "lte-router-provider-service-s-9": lte_router_provider_service_s_9,
       "lte-router-empfangspegel-s-9": lte_router_empfangspegel_s_9,
       "antennenleitungsueberwachung-1-s-9": antennenleitungsueberwachung_1_s_9,
       "antennenleitungsueberwachung-2-s-9": antennenleitungsueberwachung_2_s_9,
       "antennenleitungseuberwachung-3-s-9": antennenleitungseuberwachung_3_s_9,
       "interne-temperaturuebwerwachung-s-9": interne_temperaturuebwerwachung_s_9,
       "stoerueberwachung-optisches-verteilsystem-1-s-9": stoerueberwachung_optisches_verteilsystem_1_s_9,
       "stoerueberwachung-optisches-verteilsystem-2-s-9": stoerueberwachung_optisches_verteilsystem_2_s_9,
       "lte-router-sim-karte-s-9": lte_router_sim_karte_s_9,
       "lte-router-pin-nummer-s-9": lte_router_pin_nummer_s_9,
       "ak-slave-10-i": ak_slave_10_i,
       "modulTable-s-10": modulTable_s_10,
       "modulEntry-s-10": modulEntry_s_10,
       "modulIndex-s-10": modulIndex_s_10,
       "geraete-typ-s-10": geraete_typ_s_10,
       "betriebsstatus-s-10": betriebsstatus_s_10,
       "senderstatus-s-10": senderstatus_s_10,
       "fehlerstatus-s-10": fehlerstatus_s_10,
       "dem-adapter-zugeordnete-funkgeraetetype-s-10": dem_adapter_zugeordnete_funkgeraetetype_s_10,
       "eingabe-und-anzeigemodul-s-10": eingabe_und_anzeigemodul_s_10,
       "mod-bus-verbindung-module-s-10": mod_bus_verbindung_module_s_10,
       "gemessene-sendeleistung-im-testmode-s-10": gemessene_sendeleistung_im_testmode_s_10,
       "aktuelle-sendeleistung-s-10": aktuelle_sendeleistung_s_10,
       "gemessene-reflexion-im-testmode-s-10": gemessene_reflexion_im_testmode_s_10,
       "aktuelle-reflexion-s-10": aktuelle_reflexion_s_10,
       "letzte-gemessene-donor-sendeleistung-s-10": letzte_gemessene_donor_sendeleistung_s_10,
       "aktuelle-donor-sendeleistung-s-10": aktuelle_donor_sendeleistung_s_10,
       "letzte-gemessene-donor-reflexion-s-10": letzte_gemessene_donor_reflexion_s_10,
       "aktuelle-donor-reflexion-s-10": aktuelle_donor_reflexion_s_10,
       "anzahl-gemessener-praesenzsignale-im-testmode-s-10": anzahl_gemessener_praesenzsignale_im_testmode_s_10,
       "aktuelle-ausgangsspannung-ub-s-10": aktuelle_ausgangsspannung_ub_s_10,
       "aktuelle-ausgangsspannung-u1-s-10": aktuelle_ausgangsspannung_u1_s_10,
       "aktuelle-ausgangsspannung-u2-s-10": aktuelle_ausgangsspannung_u2_s_10,
       "aktuelle-ausgangsspannung-u3-s-10": aktuelle_ausgangsspannung_u3_s_10,
       "aktuelle-ausgangsspannung-u4-s-10": aktuelle_ausgangsspannung_u4_s_10,
       "aktuelle-ausgangsspannung-u5-s-10": aktuelle_ausgangsspannung_u5_s_10,
       "aktuelle-ausgangsspannung-u6-s-10": aktuelle_ausgangsspannung_u6_s_10,
       "aktuelle-ausgangsspannung-u7-s-10": aktuelle_ausgangsspannung_u7_s_10,
       "aktuelle-ausgangsspannung-u8-s-10": aktuelle_ausgangsspannung_u8_s_10,
       "aktuelle-ladespannung-an-akku-kreis-1-s-10": aktuelle_ladespannung_an_akku_kreis_1_s_10,
       "aktuelle-ladespannung-an-akku-Kreis-2-s-10": aktuelle_ladespannung_an_akku_Kreis_2_s_10,
       "aktuelle-ladespannung-an-akku-Kreis-3-s-10": aktuelle_ladespannung_an_akku_Kreis_3_s_10,
       "aktuelle-ladespannung-an-akku-kreis-4-s-10": aktuelle_ladespannung_an_akku_kreis_4_s_10,
       "aktuelle-ladespannung-an-akku-kreis-5-s-10": aktuelle_ladespannung_an_akku_kreis_5_s_10,
       "aktuelle-ladespannung-an-akku-kreis-6-s-10": aktuelle_ladespannung_an_akku_kreis_6_s_10,
       "aktuelle-ladespannung-an-akku-kreis-7-s-10": aktuelle_ladespannung_an_akku_kreis_7_s_10,
       "aktuelle-ladespannung-an-akku-kreis-8-s-10": aktuelle_ladespannung_an_akku_kreis_8_s_10,
       "aktuelle-spannung-an-akku-kreis-1-s-10": aktuelle_spannung_an_akku_kreis_1_s_10,
       "aktuelle-spannung-an-akku-kreis-2-s-10": aktuelle_spannung_an_akku_kreis_2_s_10,
       "aktuelle-spannung-an-akku-kreis-3-s-10": aktuelle_spannung_an_akku_kreis_3_s_10,
       "aktuelle-spannung-an-akku-kreis-4-s-10": aktuelle_spannung_an_akku_kreis_4_s_10,
       "aktuelle-spannung-an-akku-reis-5-s-10": aktuelle_spannung_an_akku_reis_5_s_10,
       "aktuelle-spannung-an-akku-kreis-6-s-10": aktuelle_spannung_an_akku_kreis_6_s_10,
       "aktuelle-spannung-an-akku-kreis-7-s-10": aktuelle_spannung_an_akku_kreis_7_s_10,
       "aktuelle-spannung-an-akku-kreis-8-s-10": aktuelle_spannung_an_akku_kreis_8_s_10,
       "testergebnis-lastspannung-an-akku-reis-1-s-10": testergebnis_lastspannung_an_akku_reis_1_s_10,
       "testergebnis-lastspannung-an-akku-kreis-2-s-10": testergebnis_lastspannung_an_akku_kreis_2_s_10,
       "testergebnis-lastspannung-an-akku-kreis-3-s-10": testergebnis_lastspannung_an_akku_kreis_3_s_10,
       "testergebnis-lastspannung-an-akku-kreis-4-s-10": testergebnis_lastspannung_an_akku_kreis_4_s_10,
       "testergebnis-lastspannung-an-akku-kreis-5-s-10": testergebnis_lastspannung_an_akku_kreis_5_s_10,
       "testergebnis-lastspannung-an-akku-kreis-6-s-10": testergebnis_lastspannung_an_akku_kreis_6_s_10,
       "testergebnis-lastspannung-an-akku-kreis-7-s-10": testergebnis_lastspannung_an_akku_kreis_7_s_10,
       "testergebnis-lastspannung-an-akku-kreis-8-s-10": testergebnis_lastspannung_an_akku_kreis_8_s_10,
       "testergebnis-innenwiderstand-akku-kreis-1-s-10": testergebnis_innenwiderstand_akku_kreis_1_s_10,
       "testergebnis-innenwiderstand-akku-kreis-2-s-10": testergebnis_innenwiderstand_akku_kreis_2_s_10,
       "testergebnis-innenwiderstand-akku-kreis-3-s-10": testergebnis_innenwiderstand_akku_kreis_3_s_10,
       "testergebnis-innenwiderstand-akku-kreis-4-s-10": testergebnis_innenwiderstand_akku_kreis_4_s_10,
       "testergebnis-innenwiderstand-akku-kreis-5-s-10": testergebnis_innenwiderstand_akku_kreis_5_s_10,
       "testergebnis-innenwiderstand-akku-kreis-6-s-10": testergebnis_innenwiderstand_akku_kreis_6_s_10,
       "testergebnis-innenwiderstand-akku-kreis-7-s-10": testergebnis_innenwiderstand_akku_kreis_7_s_10,
       "testergebnis-innenwiderstand-akku-kreis-8-s-10": testergebnis_innenwiderstand_akku_kreis_8_s_10,
       "netzteilspannung-uin1-s-10": netzteilspannung_uin1_s_10,
       "netzteilspannung-uin2-s-10": netzteilspannung_uin2_s_10,
       "programmierte-minimale-soll-sendeleistung-s-10": programmierte_minimale_soll_sendeleistung_s_10,
       "programmierte-maximale-antennen-reflexion-s-10": programmierte_maximale_antennen_reflexion_s_10,
       "programmierte-minimale-anzahl-praesenzsignale-s-10": programmierte_minimale_anzahl_praesenzsignale_s_10,
       "summen-fehlerstatus-von-tmoa-anlage-s-10": summen_fehlerstatus_von_tmoa_anlage_s_10,
       "summen-fehlerstatus-von-anbinderepeater-s-10": summen_fehlerstatus_von_anbinderepeater_s_10,
       "summen-fehlerstatus-von-analogem-repeater-s-10": summen_fehlerstatus_von_analogem_repeater_s_10,
       "aktuelle-ladespannung-akku-kreis-1-int-sicherung-defekt-s-10": aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_10,
       "aktuelle-ladespannung-akku-kreis-2-int-sicherung-defekt-s-10": aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_10,
       "aktuelle-ladespannung-akku-kreis-3-int-sicherung-defekt-s-10": aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_10,
       "aktuelle-ladespannung-akku-kreis-4-int-sicherung-defekt-s-10": aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_10,
       "aktuelle-ladespannung-akku-kreis-5-int-sicherung-defekt-s-10": aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_10,
       "aktuelle-ladespannung-akku-kreis-6-int-sicherung-defekt-s-10": aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_10,
       "aktuelle-ladespannung-akku-kreis-7-int-sicherung-defekt-s-10": aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_10,
       "aktuelle-ladespannung-akku-kreis-8-int-sicherung-defekt-s-10": aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_10,
       "netzspannungsversorgung-von-tmoa-anlage-s-10": netzspannungsversorgung_von_tmoa_anlage_s_10,
       "netzspannungsversorgung-von-anbinderepeater-s-10": netzspannungsversorgung_von_anbinderepeater_s_10,
       "fgb-id1-verbindungsstatus-s-10": fgb_id1_verbindungsstatus_s_10,
       "fgb-id2-verbindungsstatus-s-10": fgb_id2_verbindungsstatus_s_10,
       "fgb-id3-verbindungsstatus-s-10": fgb_id3_verbindungsstatus_s_10,
       "fgb-id4-verbindungsstatus-s-10": fgb_id4_verbindungsstatus_s_10,
       "fgb-id5-verbindungsstatus-s-10": fgb_id5_verbindungsstatus_s_10,
       "fgb-id6-verbindungsstatus-s-10": fgb_id6_verbindungsstatus_s_10,
       "fgb-id7-verbindungsstatus-s-10": fgb_id7_verbindungsstatus_s_10,
       "fgb-id8-verbindungsstatus-s-10": fgb_id8_verbindungsstatus_s_10,
       "fgb-id9-verbindungsstatus-s-10": fgb_id9_verbindungsstatus_s_10,
       "fgb-id10-verbindungsstatus-s-10": fgb_id10_verbindungsstatus_s_10,
       "fgb-id11-verbindungsstatus-s-10": fgb_id11_verbindungsstatus_s_10,
       "mod-bus-verbindungsstatus-s-10": mod_bus_verbindungsstatus_s_10,
       "fgb-bus-verbindungsstatus-s-10": fgb_bus_verbindungsstatus_s_10,
       "slave-bus-verbindungsstatus-s-10": slave_bus_verbindungsstatus_s_10,
       "gsm-modem-verbindungsstatus-s-10": gsm_modem_verbindungsstatus_s_10,
       "gsm-modem-sim-karte-s-10": gsm_modem_sim_karte_s_10,
       "gsm-modem-pin-nummer-s-10": gsm_modem_pin_nummer_s_10,
       "gsm-modem-provider-service-s-10": gsm_modem_provider_service_s_10,
       "gsm-modem-empfangspegel-s-10": gsm_modem_empfangspegel_s_10,
       "lte-router-verbindungsstatus-s-10": lte_router_verbindungsstatus_s_10,
       "lte-router-provider-service-s-10": lte_router_provider_service_s_10,
       "lte-router-empfangspegel-s-10": lte_router_empfangspegel_s_10,
       "antennenleitungsueberwachung-1-s-10": antennenleitungsueberwachung_1_s_10,
       "antennenleitungsueberwachung-2-s-10": antennenleitungsueberwachung_2_s_10,
       "antennenleitungseuberwachung-3-s-10": antennenleitungseuberwachung_3_s_10,
       "interne-temperaturuebwerwachung-s-10": interne_temperaturuebwerwachung_s_10,
       "stoerueberwachung-optisches-verteilsystem-1-s-10": stoerueberwachung_optisches_verteilsystem_1_s_10,
       "stoerueberwachung-optisches-verteilsystem-2-s-10": stoerueberwachung_optisches_verteilsystem_2_s_10,
       "lte-router-sim-karte-s-10": lte_router_sim_karte_s_10,
       "lte-router-pin-nummer-s-10": lte_router_pin_nummer_s_10,
       "ak-slave-11-i": ak_slave_11_i,
       "modulTable-s-11": modulTable_s_11,
       "modulEntry-s-11": modulEntry_s_11,
       "modulIndex-s-11": modulIndex_s_11,
       "geraete-typ-s-11": geraete_typ_s_11,
       "betriebsstatus-s-11": betriebsstatus_s_11,
       "senderstatus-s-11": senderstatus_s_11,
       "fehlerstatus-s-11": fehlerstatus_s_11,
       "dem-adapter-zugeordnete-funkgeraetetype-s-11": dem_adapter_zugeordnete_funkgeraetetype_s_11,
       "eingabe-und-anzeigemodul-s-11": eingabe_und_anzeigemodul_s_11,
       "mod-bus-verbindung-module-s-11": mod_bus_verbindung_module_s_11,
       "gemessene-sendeleistung-im-testmode-s-11": gemessene_sendeleistung_im_testmode_s_11,
       "aktuelle-sendeleistung-s-11": aktuelle_sendeleistung_s_11,
       "gemessene-reflexion-im-testmode-s-11": gemessene_reflexion_im_testmode_s_11,
       "aktuelle-reflexion-s-11": aktuelle_reflexion_s_11,
       "letzte-gemessene-donor-sendeleistung-s-11": letzte_gemessene_donor_sendeleistung_s_11,
       "aktuelle-donor-sendeleistung-s-11": aktuelle_donor_sendeleistung_s_11,
       "letzte-gemessene-donor-reflexion-s-11": letzte_gemessene_donor_reflexion_s_11,
       "aktuelle-donor-reflexion-s-11": aktuelle_donor_reflexion_s_11,
       "anzahl-gemessener-praesenzsignale-im-testmode-s-11": anzahl_gemessener_praesenzsignale_im_testmode_s_11,
       "aktuelle-ausgangsspannung-ub-s-11": aktuelle_ausgangsspannung_ub_s_11,
       "aktuelle-ausgangsspannung-u1-s-11": aktuelle_ausgangsspannung_u1_s_11,
       "aktuelle-ausgangsspannung-u2-s-11": aktuelle_ausgangsspannung_u2_s_11,
       "aktuelle-ausgangsspannung-u3-s-11": aktuelle_ausgangsspannung_u3_s_11,
       "aktuelle-ausgangsspannung-u4-s-11": aktuelle_ausgangsspannung_u4_s_11,
       "aktuelle-ausgangsspannung-u5-s-11": aktuelle_ausgangsspannung_u5_s_11,
       "aktuelle-ausgangsspannung-u6-s-11": aktuelle_ausgangsspannung_u6_s_11,
       "aktuelle-ausgangsspannung-u7-s-11": aktuelle_ausgangsspannung_u7_s_11,
       "aktuelle-ausgangsspannung-u8-s-11": aktuelle_ausgangsspannung_u8_s_11,
       "aktuelle-ladespannung-an-akku-kreis-1-s-11": aktuelle_ladespannung_an_akku_kreis_1_s_11,
       "aktuelle-ladespannung-an-akku-Kreis-2-s-11": aktuelle_ladespannung_an_akku_Kreis_2_s_11,
       "aktuelle-ladespannung-an-akku-Kreis-3-s-11": aktuelle_ladespannung_an_akku_Kreis_3_s_11,
       "aktuelle-ladespannung-an-akku-kreis-4-s-11": aktuelle_ladespannung_an_akku_kreis_4_s_11,
       "aktuelle-ladespannung-an-akku-kreis-5-s-11": aktuelle_ladespannung_an_akku_kreis_5_s_11,
       "aktuelle-ladespannung-an-akku-kreis-6-s-11": aktuelle_ladespannung_an_akku_kreis_6_s_11,
       "aktuelle-ladespannung-an-akku-kreis-7-s-11": aktuelle_ladespannung_an_akku_kreis_7_s_11,
       "aktuelle-ladespannung-an-akku-kreis-8-s-11": aktuelle_ladespannung_an_akku_kreis_8_s_11,
       "aktuelle-spannung-an-akku-kreis-1-s-11": aktuelle_spannung_an_akku_kreis_1_s_11,
       "aktuelle-spannung-an-akku-kreis-2-s-11": aktuelle_spannung_an_akku_kreis_2_s_11,
       "aktuelle-spannung-an-akku-kreis-3-s-11": aktuelle_spannung_an_akku_kreis_3_s_11,
       "aktuelle-spannung-an-akku-kreis-4-s-11": aktuelle_spannung_an_akku_kreis_4_s_11,
       "aktuelle-spannung-an-akku-reis-5-s-11": aktuelle_spannung_an_akku_reis_5_s_11,
       "aktuelle-spannung-an-akku-kreis-6-s-11": aktuelle_spannung_an_akku_kreis_6_s_11,
       "aktuelle-spannung-an-akku-kreis-7-s-11": aktuelle_spannung_an_akku_kreis_7_s_11,
       "aktuelle-spannung-an-akku-kreis-8-s-11": aktuelle_spannung_an_akku_kreis_8_s_11,
       "testergebnis-lastspannung-an-akku-reis-1-s-11": testergebnis_lastspannung_an_akku_reis_1_s_11,
       "testergebnis-lastspannung-an-akku-kreis-2-s-11": testergebnis_lastspannung_an_akku_kreis_2_s_11,
       "testergebnis-lastspannung-an-akku-kreis-3-s-11": testergebnis_lastspannung_an_akku_kreis_3_s_11,
       "testergebnis-lastspannung-an-akku-kreis-4-s-11": testergebnis_lastspannung_an_akku_kreis_4_s_11,
       "testergebnis-lastspannung-an-akku-kreis-5-s-11": testergebnis_lastspannung_an_akku_kreis_5_s_11,
       "testergebnis-lastspannung-an-akku-kreis-6-s-11": testergebnis_lastspannung_an_akku_kreis_6_s_11,
       "testergebnis-lastspannung-an-akku-kreis-7-s-11": testergebnis_lastspannung_an_akku_kreis_7_s_11,
       "testergebnis-lastspannung-an-akku-kreis-8-s-11": testergebnis_lastspannung_an_akku_kreis_8_s_11,
       "testergebnis-innenwiderstand-akku-kreis-1-s-11": testergebnis_innenwiderstand_akku_kreis_1_s_11,
       "testergebnis-innenwiderstand-akku-kreis-2-s-11": testergebnis_innenwiderstand_akku_kreis_2_s_11,
       "testergebnis-innenwiderstand-akku-kreis-3-s-11": testergebnis_innenwiderstand_akku_kreis_3_s_11,
       "testergebnis-innenwiderstand-akku-kreis-4-s-11": testergebnis_innenwiderstand_akku_kreis_4_s_11,
       "testergebnis-innenwiderstand-akku-kreis-5-s-11": testergebnis_innenwiderstand_akku_kreis_5_s_11,
       "testergebnis-innenwiderstand-akku-kreis-6-s-11": testergebnis_innenwiderstand_akku_kreis_6_s_11,
       "testergebnis-innenwiderstand-akku-kreis-7-s-11": testergebnis_innenwiderstand_akku_kreis_7_s_11,
       "testergebnis-innenwiderstand-akku-kreis-8-s-11": testergebnis_innenwiderstand_akku_kreis_8_s_11,
       "netzteilspannung-uin1-s-11": netzteilspannung_uin1_s_11,
       "netzteilspannung-uin2-s-11": netzteilspannung_uin2_s_11,
       "programmierte-minimale-soll-sendeleistung-s-11": programmierte_minimale_soll_sendeleistung_s_11,
       "programmierte-maximale-antennen-reflexion-s-11": programmierte_maximale_antennen_reflexion_s_11,
       "programmierte-minimale-anzahl-praesenzsignale-s-11": programmierte_minimale_anzahl_praesenzsignale_s_11,
       "summen-fehlerstatus-von-tmoa-anlage-s-11": summen_fehlerstatus_von_tmoa_anlage_s_11,
       "summen-fehlerstatus-von-anbinderepeater-s-11": summen_fehlerstatus_von_anbinderepeater_s_11,
       "summen-fehlerstatus-von-analogem-repeater-s-11": summen_fehlerstatus_von_analogem_repeater_s_11,
       "aktuelle-ladespannung-akku-kreis-1-int-sicherung-defekt-s-11": aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_s_11,
       "aktuelle-ladespannung-akku-kreis-2-int-sicherung-defekt-s-11": aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_s_11,
       "aktuelle-ladespannung-akku-kreis-3-int-sicherung-defekt-s-11": aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_s_11,
       "aktuelle-ladespannung-akku-kreis-4-int-sicherung-defekt-s-11": aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_s_11,
       "aktuelle-ladespannung-akku-kreis-5-int-sicherung-defekt-s-11": aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_s_11,
       "aktuelle-ladespannung-akku-kreis-6-int-sicherung-defekt-s-11": aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_s_11,
       "aktuelle-ladespannung-akku-kreis-7-int-sicherung-defekt-s-11": aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_s_11,
       "aktuelle-ladespannung-akku-kreis-8-int-sicherung-defekt-s-11": aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_s_11,
       "netzspannungsversorgung-von-tmoa-anlage-s-11": netzspannungsversorgung_von_tmoa_anlage_s_11,
       "netzspannungsversorgung-von-anbinderepeater-s-11": netzspannungsversorgung_von_anbinderepeater_s_11,
       "fgb-id1-verbindungsstatus-s-11": fgb_id1_verbindungsstatus_s_11,
       "fgb-id2-verbindungsstatus-s-11": fgb_id2_verbindungsstatus_s_11,
       "fgb-id3-verbindungsstatus-s-11": fgb_id3_verbindungsstatus_s_11,
       "fgb-id4-verbindungsstatus-s-11": fgb_id4_verbindungsstatus_s_11,
       "fgb-id5-verbindungsstatus-s-11": fgb_id5_verbindungsstatus_s_11,
       "fgb-id6-verbindungsstatus-s-11": fgb_id6_verbindungsstatus_s_11,
       "fgb-id7-verbindungsstatus-s-11": fgb_id7_verbindungsstatus_s_11,
       "fgb-id8-verbindungsstatus-s-11": fgb_id8_verbindungsstatus_s_11,
       "fgb-id9-verbindungsstatus-s-11": fgb_id9_verbindungsstatus_s_11,
       "fgb-id10-verbindungsstatus-s-11": fgb_id10_verbindungsstatus_s_11,
       "fgb-id11-verbindungsstatus-s-11": fgb_id11_verbindungsstatus_s_11,
       "mod-bus-verbindungsstatus-s-11": mod_bus_verbindungsstatus_s_11,
       "fgb-bus-verbindungsstatus-s-11": fgb_bus_verbindungsstatus_s_11,
       "slave-bus-verbindungsstatus-s-11": slave_bus_verbindungsstatus_s_11,
       "gsm-modem-verbindungsstatus-s-11": gsm_modem_verbindungsstatus_s_11,
       "gsm-modem-sim-karte-s-11": gsm_modem_sim_karte_s_11,
       "gsm-modem-pin-nummer-s-11": gsm_modem_pin_nummer_s_11,
       "gsm-modem-provider-service-s-11": gsm_modem_provider_service_s_11,
       "gsm-modem-empfangspegel-s-11": gsm_modem_empfangspegel_s_11,
       "lte-router-verbindungsstatus-s-11": lte_router_verbindungsstatus_s_11,
       "lte-router-provider-service-s-11": lte_router_provider_service_s_11,
       "lte-router-empfangspegel-s-11": lte_router_empfangspegel_s_11,
       "antennenleitungsueberwachung-1-s-11": antennenleitungsueberwachung_1_s_11,
       "antennenleitungsueberwachung-2-s-11": antennenleitungsueberwachung_2_s_11,
       "antennenleitungseuberwachung-3-s-11": antennenleitungseuberwachung_3_s_11,
       "interne-temperaturuebwerwachung-s-11": interne_temperaturuebwerwachung_s_11,
       "stoerueberwachung-optisches-verteilsystem-1-s-11": stoerueberwachung_optisches_verteilsystem_1_s_11,
       "stoerueberwachung-optisches-verteilsystem-2-s-11": stoerueberwachung_optisches_verteilsystem_2_s_11,
       "lte-router-sim-karte-s-11": lte_router_sim_karte_s_11,
       "lte-router-pin-nummer-s-11": lte_router_pin_nummer_s_11,
       "modulTable-traps-m": modulTable_traps_m,
       "modulEntry-traps-m": modulEntry_traps_m,
       "modulIndex-traps-m": modulIndex_traps_m,
       "geraete-typ-traps-m": geraete_typ_traps_m,
       "betriebsstatus-traps-m": betriebsstatus_traps_m,
       "senderstatus-traps-m": senderstatus_traps_m,
       "fehlerstatus-traps-m": fehlerstatus_traps_m,
       "dem-adapter-zugeordnete-funkgeraetetype-traps-m": dem_adapter_zugeordnete_funkgeraetetype_traps_m,
       "eingabe-und-anzeigemodul-traps-m": eingabe_und_anzeigemodul_traps_m,
       "mod-bus-verbindung-module-traps-m": mod_bus_verbindung_module_traps_m,
       "gemessene-sendeleistung-im-testmode-traps-m": gemessene_sendeleistung_im_testmode_traps_m,
       "aktuelle-sendeleistung-traps-m": aktuelle_sendeleistung_traps_m,
       "gemessene-reflexion-im-testmode-traps-m": gemessene_reflexion_im_testmode_traps_m,
       "aktuelle-reflexion-traps-m": aktuelle_reflexion_traps_m,
       "letzte-gemessene-donor-sendeleistung-traps-m": letzte_gemessene_donor_sendeleistung_traps_m,
       "aktuelle-donor-sendeleistung-traps-m": aktuelle_donor_sendeleistung_traps_m,
       "letzte-gemessene-donor-reflexion-traps-m": letzte_gemessene_donor_reflexion_traps_m,
       "aktuelle-donor-reflexion-traps-m": aktuelle_donor_reflexion_traps_m,
       "anzahl-gemessener-praesenzsignale-im-testmode-traps-m": anzahl_gemessener_praesenzsignale_im_testmode_traps_m,
       "aktuelle-ausgangsspannung-ub-traps-m": aktuelle_ausgangsspannung_ub_traps_m,
       "aktuelle-ausgangsspannung-u1-traps-m": aktuelle_ausgangsspannung_u1_traps_m,
       "aktuelle-ausgangsspannung-u2-traps-m": aktuelle_ausgangsspannung_u2_traps_m,
       "aktuelle-ausgangsspannung-u3-traps-m": aktuelle_ausgangsspannung_u3_traps_m,
       "aktuelle-ausgangsspannung-u4-traps-m": aktuelle_ausgangsspannung_u4_traps_m,
       "aktuelle-ausgangsspannung-u5-traps-m": aktuelle_ausgangsspannung_u5_traps_m,
       "aktuelle-ausgangsspannung-u6-traps-m": aktuelle_ausgangsspannung_u6_traps_m,
       "aktuelle-ausgangsspannung-u7-traps-m": aktuelle_ausgangsspannung_u7_traps_m,
       "aktuelle-ausgangsspannung-u8-traps-m": aktuelle_ausgangsspannung_u8_traps_m,
       "aktuelle-ladespannung-an-akku-kreis-1-traps-m": aktuelle_ladespannung_an_akku_kreis_1_traps_m,
       "aktuelle-ladespannung-an-akku-Kreis-2-traps-m": aktuelle_ladespannung_an_akku_Kreis_2_traps_m,
       "aktuelle-ladespannung-an-akku-Kreis-3-traps-m": aktuelle_ladespannung_an_akku_Kreis_3_traps_m,
       "aktuelle-ladespannung-an-akku-kreis-4-traps-m": aktuelle_ladespannung_an_akku_kreis_4_traps_m,
       "aktuelle-ladespannung-an-akku-kreis-5-traps-m": aktuelle_ladespannung_an_akku_kreis_5_traps_m,
       "aktuelle-ladespannung-an-akku-kreis-6-traps-m": aktuelle_ladespannung_an_akku_kreis_6_traps_m,
       "aktuelle-ladespannung-an-akku-kreis-7-traps-m": aktuelle_ladespannung_an_akku_kreis_7_traps_m,
       "aktuelle-ladespannung-an-akku-kreis-8-traps-m": aktuelle_ladespannung_an_akku_kreis_8_traps_m,
       "aktuelle-spannung-an-akku-kreis-1-traps-m": aktuelle_spannung_an_akku_kreis_1_traps_m,
       "aktuelle-spannung-an-akku-kreis-2-traps-m": aktuelle_spannung_an_akku_kreis_2_traps_m,
       "aktuelle-spannung-an-akku-kreis-3-traps-m": aktuelle_spannung_an_akku_kreis_3_traps_m,
       "aktuelle-spannung-an-akku-kreis-4-traps-m": aktuelle_spannung_an_akku_kreis_4_traps_m,
       "aktuelle-spannung-an-akku-reis-5-traps-m": aktuelle_spannung_an_akku_reis_5_traps_m,
       "aktuelle-spannung-an-akku-kreis-6-traps-m": aktuelle_spannung_an_akku_kreis_6_traps_m,
       "aktuelle-spannung-an-akku-kreis-7-traps-m": aktuelle_spannung_an_akku_kreis_7_traps_m,
       "aktuelle-spannung-an-akku-kreis-8-traps-m": aktuelle_spannung_an_akku_kreis_8_traps_m,
       "testergebnis-lastspannung-an-akku-reis-1-traps-m": testergebnis_lastspannung_an_akku_reis_1_traps_m,
       "testergebnis-lastspannung-an-akku-kreis-2-traps-m": testergebnis_lastspannung_an_akku_kreis_2_traps_m,
       "testergebnis-lastspannung-an-akku-kreis-3-traps-m": testergebnis_lastspannung_an_akku_kreis_3_traps_m,
       "testergebnis-lastspannung-an-akku-kreis-4-traps-m": testergebnis_lastspannung_an_akku_kreis_4_traps_m,
       "testergebnis-lastspannung-an-akku-kreis-5-traps-m": testergebnis_lastspannung_an_akku_kreis_5_traps_m,
       "testergebnis-lastspannung-an-akku-kreis-6-traps-m": testergebnis_lastspannung_an_akku_kreis_6_traps_m,
       "testergebnis-lastspannung-an-akku-kreis-7-traps-m": testergebnis_lastspannung_an_akku_kreis_7_traps_m,
       "testergebnis-lastspannung-an-akku-kreis-8-traps-m": testergebnis_lastspannung_an_akku_kreis_8_traps_m,
       "testergebnis-innenwiderstand-akku-kreis-1-traps-m": testergebnis_innenwiderstand_akku_kreis_1_traps_m,
       "testergebnis-innenwiderstand-akku-kreis-2-traps-m": testergebnis_innenwiderstand_akku_kreis_2_traps_m,
       "testergebnis-innenwiderstand-akku-kreis-3-traps-m": testergebnis_innenwiderstand_akku_kreis_3_traps_m,
       "testergebnis-innenwiderstand-akku-kreis-4-traps-m": testergebnis_innenwiderstand_akku_kreis_4_traps_m,
       "testergebnis-innenwiderstand-akku-kreis-5-traps-m": testergebnis_innenwiderstand_akku_kreis_5_traps_m,
       "testergebnis-innenwiderstand-akku-kreis-6-traps-m": testergebnis_innenwiderstand_akku_kreis_6_traps_m,
       "testergebnis-innenwiderstand-akku-kreis-7-traps-m": testergebnis_innenwiderstand_akku_kreis_7_traps_m,
       "testergebnis-innenwiderstand-akku-kreis-8-traps-m": testergebnis_innenwiderstand_akku_kreis_8_traps_m,
       "netzteilspannung-uin1-traps-m": netzteilspannung_uin1_traps_m,
       "netzteilspannung-uin2-traps-m": netzteilspannung_uin2_traps_m,
       "programmierte-minimale-soll-sendeleistung-traps-m": programmierte_minimale_soll_sendeleistung_traps_m,
       "programmierte-maximale-antennen-reflexion-traps-m": programmierte_maximale_antennen_reflexion_traps_m,
       "programmierte-minimale-anzahl-praesenzsignale-traps-m": programmierte_minimale_anzahl_praesenzsignale_traps_m,
       "summen-fehlerstatus-von-tmoa-anlage-traps-m": summen_fehlerstatus_von_tmoa_anlage_traps_m,
       "summen-fehlerstatus-von-anbinderepeater-traps-m": summen_fehlerstatus_von_anbinderepeater_traps_m,
       "summen-fehlerstatus-von-analogem-repeater-traps-m": summen_fehlerstatus_von_analogem_repeater_traps_m,
       "aktuelle-ladespannung-akku-kreis-1-int-sicherung-defekt-traps-m": aktuelle_ladespannung_akku_kreis_1_int_sicherung_defekt_traps_m,
       "aktuelle-ladespannung-akku-kreis-2-int-sicherung-defekt-traps-m": aktuelle_ladespannung_akku_kreis_2_int_sicherung_defekt_traps_m,
       "aktuelle-ladespannung-akku-kreis-3-int-sicherung-defekt-traps-m": aktuelle_ladespannung_akku_kreis_3_int_sicherung_defekt_traps_m,
       "aktuelle-ladespannung-akku-kreis-4-int-sicherung-defekt-traps-m": aktuelle_ladespannung_akku_kreis_4_int_sicherung_defekt_traps_m,
       "aktuelle-ladespannung-akku-kreis-5-int-sicherung-defekt-traps-m": aktuelle_ladespannung_akku_kreis_5_int_sicherung_defekt_traps_m,
       "aktuelle-ladespannung-akku-kreis-6-int-sicherung-defekt-traps-m": aktuelle_ladespannung_akku_kreis_6_int_sicherung_defekt_traps_m,
       "aktuelle-ladespannung-akku-kreis-7-int-sicherung-defekt-traps-m": aktuelle_ladespannung_akku_kreis_7_int_sicherung_defekt_traps_m,
       "aktuelle-ladespannung-akku-kreis-8-int-sicherung-defekt-traps-m": aktuelle_ladespannung_akku_kreis_8_int_sicherung_defekt_traps_m,
       "netzspannungsversorgung-von-tmoa-anlage-traps-m": netzspannungsversorgung_von_tmoa_anlage_traps_m,
       "netzspannungsversorgung-von-anbinderepeater-traps-m": netzspannungsversorgung_von_anbinderepeater_traps_m,
       "fgb-id1-verbindungsstatus": fgb_id1_verbindungsstatus,
       "fgb-id2-verbindungsstatus": fgb_id2_verbindungsstatus,
       "fgb-id3-verbindungsstatus": fgb_id3_verbindungsstatus,
       "fgb-id4-verbindungsstatus": fgb_id4_verbindungsstatus,
       "fgb-id5-verbindungsstatus": fgb_id5_verbindungsstatus,
       "fgb-id6-verbindungsstatus": fgb_id6_verbindungsstatus,
       "fgb-id7-verbindungsstatus": fgb_id7_verbindungsstatus,
       "fgb-id8-verbindungsstatus": fgb_id8_verbindungsstatus,
       "fgb-id9-verbindungsstatus": fgb_id9_verbindungsstatus,
       "fgb-id10-verbindungsstatus": fgb_id10_verbindungsstatus,
       "fgb-id11-verbindungsstatus": fgb_id11_verbindungsstatus,
       "mod-bus-verbindungsstatus": mod_bus_verbindungsstatus,
       "fgb-bus-verbindungsstatus": fgb_bus_verbindungsstatus,
       "slave-bus-verbindungsstatus": slave_bus_verbindungsstatus,
       "gsm-modem-verbindungsstatus": gsm_modem_verbindungsstatus,
       "gsm-modem-sim-karte": gsm_modem_sim_karte,
       "gsm-modem-pin-nummer": gsm_modem_pin_nummer,
       "gsm-modem-provider-service": gsm_modem_provider_service,
       "gsm-modem-empfangspegel": gsm_modem_empfangspegel,
       "lte-router-verbindungsstatus": lte_router_verbindungsstatus,
       "lte-router-provider-service": lte_router_provider_service,
       "lte-router-empfangspegel": lte_router_empfangspegel,
       "antennenleitungsueberwachung-1": antennenleitungsueberwachung_1,
       "antennenleitungsueberwachung-2": antennenleitungsueberwachung_2,
       "antennenleitungseuberwachung-3": antennenleitungseuberwachung_3,
       "interne-temperaturuebwerwachung": interne_temperaturuebwerwachung,
       "stoerueberwachung-optisches-verteilsystem-1": stoerueberwachung_optisches_verteilsystem_1,
       "stoerueberwachung-optisches-verteilsystem-2": stoerueberwachung_optisches_verteilsystem_2,
       "lte-router-sim-karte": lte_router_sim_karte,
       "lte-router-pin-nummer": lte_router_pin_nummer,
       "ak-gesamtsystem-i": ak_gesamtsystem_i,
       "gesamtsystem-antennenleitung-1": gesamtsystem_antennenleitung_1,
       "gesamtsystem-antennenleitung-2": gesamtsystem_antennenleitung_2,
       "gesamtsystem-antennenleitung-3": gesamtsystem_antennenleitung_3,
       "gesamtsystem-temperaturfehler": gesamtsystem_temperaturfehler,
       "gesamtsystem-gsmfehler": gesamtsystem_gsmfehler,
       "gesamtsystem-ltefehler": gesamtsystem_ltefehler,
       "gesamtsystem-fgb-verbindungs-fehler": gesamtsystem_fgb_verbindungs_fehler,
       "gesamtsystem-fgbfehler": gesamtsystem_fgbfehler,
       "gesamtsystem-slave-verbindungs-fehler": gesamtsystem_slave_verbindungs_fehler,
       "gesamtsystem-slave-fehler": gesamtsystem_slave_fehler,
       "gesamtsystem-modul-verbindungs-fehler": gesamtsystem_modul_verbindungs_fehler,
       "gesamtsystem-Modul-fehler": gesamtsystem_Modul_fehler,
       "gesamtsystem-ov1-fehler": gesamtsystem_ov1_fehler,
       "gesamtsystem-ov2-fehler": gesamtsystem_ov2_fehler,
       "gesamtsystem-option-1-fehler": gesamtsystem_option_1_fehler,
       "gesamtsystem-option-2-fehler": gesamtsystem_option_2_fehler,
       "gesamtsystem-bma-in": gesamtsystem_bma_in,
       "gesamtsystem-modul-summenfehler": gesamtsystem_modul_summenfehler,
       "gesamtsystem-modul-netzfehler": gesamtsystem_modul_netzfehler,
       "gesamtsystem-usvfehler": gesamtsystem_usvfehler,
       "gesamtsystem-akkufehler": gesamtsystem_akkufehler,
       "ak-funk-i": ak_funk_i,
       "ak-info-f-i": ak_info_f_i,
       "ak-mgmt-f-i": ak_mgmt_f_i,
       "ak-divers-f-i": ak_divers_f_i,
       "ak-traps-f-i": ak_traps_f_i,
       "ak-custom-i": ak_custom_i,
       "ak-info-c-i": ak_info_c_i,
       "ak-mgmt-c-i": ak_mgmt_c_i,
       "ak-divers-c-i": ak_divers_c_i,
       "ak-traps-c-i": ak_traps_c_i,
       "ak-devices-ii": ak_devices_ii,
       "tbd-1": tbd_1,
       "ext-devices-i": ext_devices_i,
       "tbd-2": tbd_2,
       "ext-devices-ii": ext_devices_ii,
       "tbd-3": tbd_3,
       "ak-mib-conformance": ak_mib_conformance,
       "ak-mib-compliance": ak_mib_compliance}
)
