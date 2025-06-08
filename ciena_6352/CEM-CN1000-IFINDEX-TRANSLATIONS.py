# SNMP MIB module (CEM-CN1000-IFINDEX-TRANSLATIONS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_6352/CEM-CN1000-IFINDEX-TRANSLATIONS.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:49:20 2025
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

(Cn1000PortRange,
 Cn1000ShelfRange,
 cn1000Hardware,
 cn1000IfTranslatioins,
 cn1000NetSync,
 cn1000VoiceInfrastructure,
 cn1000VoiceLineServices) = mibBuilder.importSymbols(
    "CEM-CN1000",
    "Cn1000PortRange",
    "Cn1000ShelfRange",
    "cn1000Hardware",
    "cn1000IfTranslatioins",
    "cn1000NetSync",
    "cn1000VoiceInfrastructure",
    "cn1000VoiceLineServices")

(CnSlotGroupNameType,) = mibBuilder.importSymbols(
    "CEM-TEXTUAL-CONVENTIONS",
    "CnSlotGroupNameType")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

cn1000IfTranslationsModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cn1000IfTranslationsModule.setRevisions(
        ("2003-03-14 09:45",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Cn1000IfType(TextualConvention, Integer32):
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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62)
        )
    )
    namedValues = NamedValues(
        *(("cn1000Ethernet", 1),
          ("cn1000Ipoa", 2),
          ("cn1000SoftwareLoopback", 3),
          ("cn1000Pots", 4),
          ("cn1000AdslPhysical", 5),
          ("cn1000AdslFast", 6),
          ("cn1000AdslInterleaved", 7),
          ("cn1000AtmOverAdslFast", 8),
          ("cn1000AtmOverAdslnterleaved", 9),
          ("cn1000T1OnT1Card", 10),
          ("cn1000SonetOC3C", 11),
          ("cn1000AtmOverSonetOC3C", 12),
          ("cn1000T1OnWanCard", 13),
          ("cn1000T1OnDs3Card", 14),
          ("cn1000GR303", 15),
          ("cn1000TR08", 16),
          ("cn1000INA", 17),
          ("cn1000Ds3", 18),
          ("cn1000AtmOnDs3", 19),
          ("cn1000AtmOnIma", 20),
          ("cn1000ImaLink", 21),
          ("cn1000CeVoiceSignalling", 22),
          ("cn1000InternalAtmT1CardMicro", 23),
          ("cn1000InternalAtmLineCardCem", 24),
          ("cn1000InternalAtmT1CardCem", 25),
          ("cn1000InternalAtmFeatureCardCem", 26),
          ("cn1000InternalAtmWanCardCem", 27),
          ("cn1000InternalAtmDs3CardCem", 28),
          ("cn1000Mgcp", 29),
          ("cn1000InternalOicCem", 30),
          ("cn1000Slc5Cot", 31),
          ("cn1000InternalQuarkDsp", 32),
          ("cn1000InternalLoopFpgaCe", 33),
          ("cn1000InternalNetFpgaCe", 34),
          ("cn1000InternalDsLoopbackFpgaCe", 35),
          ("cn1000InternalUsLoopbackFpgaCe", 36),
          ("cn1000Dax", 37),
          ("cn1000InternalChannelBankCem", 38),
          ("cn1000E1OnE1Card", 39),
          ("cn1000V5", 40),
          ("cn1000SonetOC12", 41),
          ("cn1000T1OnOc12Card", 42),
          ("cn1000EthernetOverPon", 43),
          ("cn1000InternalOltCem", 44),
          ("cn1000AtmOverDs3", 45),
          ("cn1000Multicast", 46),
          ("cn1000MulticastOverAdslFast", 47),
          ("cn1000MulticastOverAdslInterleaved", 48),
          ("cn1000MulticastOverSonetOC3", 49),
          ("cn1000MulticastOverSonetOC12", 50),
          ("cn1000MulticastOverDs3", 51),
          ("cn1000Internal", 52),
          ("cn1000InternalAtmP2MpRoot", 53),
          ("cn1000InternalAtmP2MpLeaf", 54),
          ("cn1000InternalAtmP2MpConEvent", 55),
          ("cn1000InternalAtmP2MpBwEvent", 56),
          ("cn1000InternalIgmpRtr", 57),
          ("cn1000InternalIgmpCpu", 58),
          ("cn1000InternalIgmpEvent", 59),
          ("cn1000AtmOverSonetOC12C", 60),
          ("cn1000InternalAtmOc12CardCem", 61),
          ("cn1000RingPort", 62))
    )



# MIB Managed Objects in the order of their OIDs

_Cn1000TranslateLocationToIfIndexTable_Object = MibTable
cn1000TranslateLocationToIfIndexTable = _Cn1000TranslateLocationToIfIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    cn1000TranslateLocationToIfIndexTable.setStatus("current")
_Cn1000TranslateLocationToIfIndexEntry_Object = MibTableRow
cn1000TranslateLocationToIfIndexEntry = _Cn1000TranslateLocationToIfIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 5, 1, 2, 1)
)
cn1000TranslateLocationToIfIndexEntry.setIndexNames(
    (0, "CEM-CN1000-IFINDEX-TRANSLATIONS", "cn1000InShelf"),
    (0, "CEM-CN1000-IFINDEX-TRANSLATIONS", "cn1000InSlotGroup"),
    (0, "CEM-CN1000-IFINDEX-TRANSLATIONS", "cn1000InPort"),
    (0, "CEM-CN1000-IFINDEX-TRANSLATIONS", "cn1000InIfType"),
)
if mibBuilder.loadTexts:
    cn1000TranslateLocationToIfIndexEntry.setStatus("current")
_Cn1000InShelf_Type = Cn1000ShelfRange
_Cn1000InShelf_Object = MibTableColumn
cn1000InShelf = _Cn1000InShelf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 5, 1, 2, 1, 1),
    _Cn1000InShelf_Type()
)
cn1000InShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000InShelf.setStatus("current")
_Cn1000InSlotGroup_Type = CnSlotGroupNameType
_Cn1000InSlotGroup_Object = MibTableColumn
cn1000InSlotGroup = _Cn1000InSlotGroup_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 5, 1, 2, 1, 2),
    _Cn1000InSlotGroup_Type()
)
cn1000InSlotGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000InSlotGroup.setStatus("current")
_Cn1000InPort_Type = Cn1000PortRange
_Cn1000InPort_Object = MibTableColumn
cn1000InPort = _Cn1000InPort_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 5, 1, 2, 1, 3),
    _Cn1000InPort_Type()
)
cn1000InPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000InPort.setStatus("current")
_Cn1000InIfType_Type = Cn1000IfType
_Cn1000InIfType_Object = MibTableColumn
cn1000InIfType = _Cn1000InIfType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 5, 1, 2, 1, 4),
    _Cn1000InIfType_Type()
)
cn1000InIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000InIfType.setStatus("current")
_Cn1000OutifIndex_Type = InterfaceIndex
_Cn1000OutifIndex_Object = MibTableColumn
cn1000OutifIndex = _Cn1000OutifIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 5, 1, 2, 1, 5),
    _Cn1000OutifIndex_Type()
)
cn1000OutifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000OutifIndex.setStatus("current")
_Cn1000TranslateIfIndexToLocationTable_Object = MibTable
cn1000TranslateIfIndexToLocationTable = _Cn1000TranslateIfIndexToLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 5, 1, 3)
)
if mibBuilder.loadTexts:
    cn1000TranslateIfIndexToLocationTable.setStatus("current")
_Cn1000TranslateIfIndexToLocationEntry_Object = MibTableRow
cn1000TranslateIfIndexToLocationEntry = _Cn1000TranslateIfIndexToLocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 5, 1, 3, 1)
)
cn1000TranslateIfIndexToLocationEntry.setIndexNames(
    (0, "CEM-CN1000-IFINDEX-TRANSLATIONS", "cn1000InIfIndex"),
    (0, "CEM-CN1000-IFINDEX-TRANSLATIONS", "cn1000IfTypeIn"),
)
if mibBuilder.loadTexts:
    cn1000TranslateIfIndexToLocationEntry.setStatus("current")
_Cn1000InIfIndex_Type = InterfaceIndex
_Cn1000InIfIndex_Object = MibTableColumn
cn1000InIfIndex = _Cn1000InIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 5, 1, 3, 1, 1),
    _Cn1000InIfIndex_Type()
)
cn1000InIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000InIfIndex.setStatus("current")
_Cn1000IfTypeIn_Type = Cn1000IfType
_Cn1000IfTypeIn_Object = MibTableColumn
cn1000IfTypeIn = _Cn1000IfTypeIn_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 5, 1, 3, 1, 2),
    _Cn1000IfTypeIn_Type()
)
cn1000IfTypeIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cn1000IfTypeIn.setStatus("current")
_Cn1000OutShelf_Type = Cn1000ShelfRange
_Cn1000OutShelf_Object = MibTableColumn
cn1000OutShelf = _Cn1000OutShelf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 5, 1, 3, 1, 3),
    _Cn1000OutShelf_Type()
)
cn1000OutShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000OutShelf.setStatus("current")
_Cn1000OutSlotGroup_Type = CnSlotGroupNameType
_Cn1000OutSlotGroup_Object = MibTableColumn
cn1000OutSlotGroup = _Cn1000OutSlotGroup_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 5, 1, 3, 1, 4),
    _Cn1000OutSlotGroup_Type()
)
cn1000OutSlotGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000OutSlotGroup.setStatus("current")
_Cn1000OutPort_Type = Cn1000PortRange
_Cn1000OutPort_Object = MibTableColumn
cn1000OutPort = _Cn1000OutPort_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 5, 1, 3, 1, 5),
    _Cn1000OutPort_Type()
)
cn1000OutPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000OutPort.setStatus("current")
_Cn1000OutIfType_Type = Cn1000IfType
_Cn1000OutIfType_Object = MibTableColumn
cn1000OutIfType = _Cn1000OutIfType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 5, 1, 3, 1, 6),
    _Cn1000OutIfType_Type()
)
cn1000OutIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cn1000OutIfType.setStatus("current")

# Managed Objects groups

cn1000IfTranslations = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 1, 2, 1, 5, 1, 1)
)
cn1000IfTranslations.setObjects(
      *(("CEM-CN1000-IFINDEX-TRANSLATIONS", "cn1000InShelf"),
        ("CEM-CN1000-IFINDEX-TRANSLATIONS", "cn1000InSlotGroup"),
        ("CEM-CN1000-IFINDEX-TRANSLATIONS", "cn1000InPort"),
        ("CEM-CN1000-IFINDEX-TRANSLATIONS", "cn1000InIfType"),
        ("CEM-CN1000-IFINDEX-TRANSLATIONS", "cn1000OutifIndex"),
        ("CEM-CN1000-IFINDEX-TRANSLATIONS", "cn1000InIfIndex"),
        ("CEM-CN1000-IFINDEX-TRANSLATIONS", "cn1000OutShelf"),
        ("CEM-CN1000-IFINDEX-TRANSLATIONS", "cn1000OutSlotGroup"),
        ("CEM-CN1000-IFINDEX-TRANSLATIONS", "cn1000OutPort"),
        ("CEM-CN1000-IFINDEX-TRANSLATIONS", "cn1000OutIfType"),
        ("CEM-CN1000-IFINDEX-TRANSLATIONS", "cn1000IfTypeIn"))
)
if mibBuilder.loadTexts:
    cn1000IfTranslations.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CEM-CN1000-IFINDEX-TRANSLATIONS",
    **{"Cn1000IfType": Cn1000IfType,
       "cn1000IfTranslationsModule": cn1000IfTranslationsModule,
       "cn1000IfTranslations": cn1000IfTranslations,
       "cn1000TranslateLocationToIfIndexTable": cn1000TranslateLocationToIfIndexTable,
       "cn1000TranslateLocationToIfIndexEntry": cn1000TranslateLocationToIfIndexEntry,
       "cn1000InShelf": cn1000InShelf,
       "cn1000InSlotGroup": cn1000InSlotGroup,
       "cn1000InPort": cn1000InPort,
       "cn1000InIfType": cn1000InIfType,
       "cn1000OutifIndex": cn1000OutifIndex,
       "cn1000TranslateIfIndexToLocationTable": cn1000TranslateIfIndexToLocationTable,
       "cn1000TranslateIfIndexToLocationEntry": cn1000TranslateIfIndexToLocationEntry,
       "cn1000InIfIndex": cn1000InIfIndex,
       "cn1000IfTypeIn": cn1000IfTypeIn,
       "cn1000OutShelf": cn1000OutShelf,
       "cn1000OutSlotGroup": cn1000OutSlotGroup,
       "cn1000OutPort": cn1000OutPort,
       "cn1000OutIfType": cn1000OutIfType}
)
